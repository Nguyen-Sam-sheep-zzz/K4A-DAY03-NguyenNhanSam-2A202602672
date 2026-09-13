"""Web UI server for the recruitment ReAct agent (stdlib only)."""
import json
import os
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
from app import run_react_agent
from mcp_server import MCPAcademicServer
from providers import get_llm_provider

PROVIDER = get_llm_provider()
MCP = MCPAcademicServer()

class Handler(BaseHTTPRequestHandler):
    def _send(self, payload, status=200, content_type="application/json"):
        body = payload if isinstance(payload, bytes) else (json.dumps(payload, ensure_ascii=False).encode("utf-8"))
        self.send_response(status)
        self.send_header("Content-Type", f"{content_type}; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path == "/api/health":
            return self._send({"ok": True, "provider": PROVIDER.__class__.__name__})
        relative = self.path.split("?", 1)[0].lstrip("/") or "index.html"
        target = (ROOT / "web" / relative).resolve()
        if ROOT / "web" not in target.parents or not target.is_file():
            return self._send({"error": "Not found"}, 404)
        content_type = "text/html" if target.suffix == ".html" else "text/css" if target.suffix == ".css" else "application/javascript"
        self._send(target.read_bytes(), content_type=content_type)

    def do_POST(self):
        if self.path != "/api/chat":
            return self._send({"error": "Not found"}, 404)
        try:
            size = int(self.headers.get("Content-Length", "0"))
            message = json.loads(self.rfile.read(size)).get("message", "").strip()
            if not message or len(message) > 4000:
                return self._send({"error": "Tin nhắn không hợp lệ."}, 400)
            logs = run_react_agent(message, PROVIDER, MCP)
            answers = [x.get("output", "") for x in logs if x.get("action_type") == "FINAL_ANSWER"]
            return self._send({"answer": answers[-1] if answers else "Agent chưa tạo câu trả lời.", "trace": logs})
        except Exception as exc:
            return self._send({"error": str(exc)}, 500)

if __name__ == "__main__":
    port = int(os.getenv("PORT", "8000"))
    print(f"TalentFlow UI: http://localhost:{port}")
    ThreadingHTTPServer(("localhost", port), Handler).serve_forever()
