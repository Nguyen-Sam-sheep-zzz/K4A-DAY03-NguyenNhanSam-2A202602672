"""
🛠️ TOOL DEFINITIONS & EXECUTION BACKEND
Mã nguồn chứa danh sách Tool Schemas (JSON Schema) và Execution Layer phục vụ cho MCP Server.
"""

import json
from typing import Dict, Any

# ==============================================================================
# 1. KHAI BÁO TOOL SCHEMAS CHUẨN NATIVE JSON SCHEMA (TASK 1.2)
# ==============================================================================

TOOLS_SCHEMA = [
    # Tool 1: Tra cứu tiêu chí tuyển dụng theo vị trí.
    {
        "name": "recruitment_criteria_query",
        "description": "Tra cứu tiêu chí tuyển dụng, kỹ năng và kinh nghiệm tối thiểu của một vị trí.",
        "parameters": {
            "type": "object",
            "properties": {
                "position": {
                    "type": "string",
                    "description": "Tên vị trí cần tra cứu, ví dụ: Kỹ sư phần mềm"
                }
            },
            "required": ["position"]
        }
    },
    
    # --------------------------------------------------------------------------
    # Tool 2: Gửi thông báo lịch phỏng vấn.
    # --------------------------------------------------------------------------
    {
        "name": "send_interview_notification",
        "description": "Gửi thông báo lịch phỏng vấn cho ứng viên qua email.",
        "parameters": {
            "type": "object",
            "properties": {
                "candidate_name": {"type": "string", "description": "Họ tên ứng viên"},
                "candidate_email": {"type": "string", "description": "Email ứng viên"},
                "position": {"type": "string", "description": "Vị trí tuyển dụng"},
                "datetime_str": {"type": "string", "description": "Thời gian phỏng vấn"},
                "interviewer": {"type": "string", "description": "Tên người phỏng vấn"}
            },
            "required": ["candidate_name", "candidate_email", "position", "datetime_str", "interviewer"]
        }
    }
]

# ==============================================================================
# 2. MÔ PHỎNG DỮ LIỆU & HÀM THỰC THI TOOL (EXECUTION LAYER)
# ==============================================================================

MOCK_DATABASE = {
    "kỹ sư phần mềm": {"title": "Kỹ sư phần mềm", "skills": ["Python", "SQL", "Git"], "experience_years": 2, "education": "Đại học CNTT"},
    "ky su phan mem": {"title": "Kỹ sư phần mềm", "skills": ["Python", "SQL", "Git"], "experience_years": 2, "education": "Đại học CNTT"},
    "data analyst": {"title": "Data Analyst", "skills": ["SQL", "Excel", "Power BI"], "experience_years": 1, "education": "Kinh tế, CNTT hoặc tương đương"},
    "chuyên viên phân tích dữ liệu": {"title": "Data Analyst", "skills": ["SQL", "Excel", "Power BI"], "experience_years": 1, "education": "Kinh tế, CNTT hoặc tương đương"}
}


def execute_recruitment_criteria_query(position: str) -> str:
    """Tra cứu tiêu chí tuyển dụng theo vị trí."""
    key = position.strip().lower()
    criteria = MOCK_DATABASE.get(key)
    if criteria:
        return json.dumps({
            "status": "SUCCESS",
            "position": position,
            "criteria": criteria
        }, ensure_ascii=False)
    else:
        return json.dumps({
            "status": "NOT_FOUND",
            "message": f"Chưa có tiêu chí tuyển dụng cho vị trí '{position}'."
        }, ensure_ascii=False)


def execute_send_interview_notification(candidate_name: str, candidate_email: str, position: str, datetime_str: str, interviewer: str) -> str:
    """Tạo bản ghi gửi thông báo lịch phỏng vấn."""
    return json.dumps({
        "status": "SUCCESS",
        "notification_id": f"INT-{candidate_email.split('@')[0].upper()}-99",
        "candidate_name": candidate_name,
        "candidate_email": candidate_email,
        "position": position,
        "datetime": datetime_str,
        "interviewer": interviewer,
        "message": f"Đã tạo thông báo phỏng vấn vị trí {position} cho {candidate_name} vào {datetime_str}."
    }, ensure_ascii=False)


# Router gọi tool thực tế
TOOL_ROUTER = {
    "recruitment_criteria_query": execute_recruitment_criteria_query,
    "send_interview_notification": execute_send_interview_notification
}

def dispatch_tool_call(tool_name: str, arguments: Dict[str, Any]) -> str:
    """Hàm trung chuyển thực thi tool"""
    if tool_name in TOOL_ROUTER:
        try:
            return TOOL_ROUTER[tool_name](**arguments)
        except Exception as e:
            return json.dumps({"status": "EXECUTION_ERROR", "error": str(e)}, ensure_ascii=False)
    return json.dumps({"status": "UNKNOWN_TOOL", "error": f"Tool '{tool_name}' không tồn tại!"}, ensure_ascii=False)
