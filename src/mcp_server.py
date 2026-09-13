"""
🔌 MODEL CONTEXT PROTOCOL (MCP) SERVER MODULE
Mô phỏng kiến trúc MCP Server (Client-Server Architecture) cung cấp công cụ chuẩn hóa.
"""

import json
import sys
from typing import Dict, Any, List
from tools import TOOLS_SCHEMA, dispatch_tool_call

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

class MCPAcademicServer:
    """
    Giả lập MCP Server tuân thủ chuẩn giao thức Model Context Protocol
    """
    def __init__(self, server_name: str = "vinuni-recruitment-mcp-server"):
        self.server_name = server_name
        self.version = "2026.1.0"
        
    def list_tools(self) -> List[Dict[str, Any]]:
        """Trả về danh sách các Tools chuẩn giao thức MCP"""
        return TOOLS_SCHEMA
        
    def call_tool(self, tool_name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """
        [TASK 2.1] HỌC VIÊN HOÀN THIỆN HÀM THỰC THI TOOL TRÊN MCP SERVER
        Thực thi request gọi Tool theo chuẩn MCP JSON-RPC
        """
        raw_result = dispatch_tool_call(tool_name, arguments or {})
        try:
            content = json.loads(raw_result)
        except (TypeError, json.JSONDecodeError):
            content = {"status": "EXECUTION_ERROR", "error": "Tool trả về dữ liệu không phải JSON hợp lệ."}
        return {
            "jsonrpc": "2.0",
            "server": self.server_name,
            "tool": tool_name,
            "result": content,
        }


if __name__ == "__main__":
    print("==========================================================")
    print("🔌 KIỂM THỬ ĐỘC LẬP MCP SERVER (vinuni-recruitment-mcp-server)")
    print("==========================================================")
    
    server = MCPAcademicServer()
    tools = server.list_tools()
    print(f"✅ Khởi tạo thành công MCP Server: {server.server_name} (Version: {server.version})")
    print(f"📦 Số lượng Tools công bố: {len(tools)}")
    
    # Kiểm tra schema công cụ.
    sched_tool = next((t for t in tools if t.get("name") == "send_interview_notification"), None)
    if sched_tool and not sched_tool.get("parameters", {}).get("properties"):
        print("⏳ Tool 'send_interview_notification' chưa có schema đầy đủ trong 'src/tools.py'.")
    else:
        print("✅ Tool 'send_interview_notification' đã có schema đầy đủ.")

    # Kiểm tra dispatcher MCP.
    test_result = server.call_tool("recruitment_criteria_query", {"position": "Kỹ sư phần mềm"})
    if not test_result:
        print("⏳ MCP dispatcher chưa trả về dữ liệu.")
    else:
        print(f"✅ MCP dispatcher hoạt động với 'recruitment_criteria_query':")
        print(f"   Phản hồi JSON-RPC: {json.dumps(test_result, ensure_ascii=False)}")
