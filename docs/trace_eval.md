# 📊 BÁO CÁO THU HOẠCH NGHIỆM THU BÀI LAB 3 (BƯỚC 3 — SUBMISSION ARTIFACT)

> **Họ và Tên Học viên:** Nguyễn Nhân Sâm  
> **Mã Sinh Viên / Mã Học viên:** 2A202602672  
> **Chủ đề Lựa chọn:** Trợ lý Tuyển dụng & Sàng lọc CV: Tra cứu tiêu chí tuyển dụng vị trí và gửi thông báo lịch phỏng vấn.  

---

## 1. BẢNG CHẤM ĐIỂM AGENTIC FIT SCORING MATRIX (ĐÁNH GIÁ CHỦ ĐỀ)

| Tiêu chí Đánh giá | Mức độ (1 - 5) | Giải trình chi tiết lý do chọn điểm |
| :--- | :---: | :--- |
| **1. Multi-step Reasoning** | 5 / 5 | Agent phân tích vị trí, đối chiếu tiêu chí và hỗ trợ quyết định gửi lịch phỏng vấn. |
| **2. Tool Interaction** | 5 / 5 | Cần MCP để tra cứu dữ liệu tuyển dụng và thực hiện gửi thông báo. |
| **3. Dynamic Decision** | 5 / 5 | Hành động tiếp theo phụ thuộc vào kết quả tra cứu; vị trí không có dữ liệu phải dừng và báo rõ. |
| **4. Long Horizon Goal** | 4 / 5 | Mục tiêu tuyển đúng người được duy trì qua tra cứu, sàng lọc và thông báo; phạm vi demo giới hạn một phiên. |
| **TỔNG ĐIỂM AGENTIC FIT** | **19 / 20** | Bài toán rất phù hợp triển khai Agentic System. |

---

## 2. TRÍCH XUẤT KẾT QUẢ WATERFALL TRACE LOG (SAU KHI CHẠY TEST SUITE TRÊN API THẬT)

> ⚠️ **YÊU CẦU NGHIỆM THU:** Mở tệp `.env` điền `GEMINI_API_KEY` (hoặc `OPENAI_API_KEY`) để kết nối LLM thật trước khi thực thi `python src/app.py --all`. Bài nộp chỉ dùng Mock Offline Provider sẽ không đạt điểm nghiệm thực tế.

Dữ liệu dưới đây được trích từ lần chạy `python src/app.py --all` với `GeminiProvider` thật:

```json
[
  {
    "step": 1,
    "action_type": "TOOL_EXECUTION",
    "tool_name": "recruitment_criteria_query",
    "arguments": {
      "position": "Kỹ sư phần mềm"
    },
    "observation": {
      "status": "SUCCESS",
      "position": "Kỹ sư phần mềm",
      "criteria": {
        "title": "Kỹ sư phần mềm",
        "skills": ["Python", "SQL", "Git"],
        "experience_years": 2
      }
    },
    "latency_ms": 2360.41
  }
]
```

---

## 3. TỔNG KẾT KẾT QUẢ NGHIỆM THU & NỘP BÀI

- [x] Đã điền API Key thật trong `.env` (Gemini, model `gemini-2.5-flash`).
- **Tổng số Test Cases đã chạy thành công:** 5 / 5 test cases.
- **Số lượt gọi Tool qua MCP Server:** 5 lượt (TC02: 1, TC03: 1, TC04: 2, TC05: 1).
- **Ghi chú nghiệm thu:** Cả 5 Test Cases đều chạy bằng `GeminiProvider` với API thật; TC04 hoàn thành đúng chuỗi tra cứu tiêu chí → gửi thông báo, TC05 xử lý `NOT_FOUND` không bịa đặt dữ liệu.
- **Kết quả đẩy Repo nộp bài:** [ ] Đã Commit và Push mã nguồn thành công lên GitHub cá nhân.

---

> ✅ **HOÀN TẤT NỘP BÀI:** Sao chép đường link GitHub Repository cá nhân của bạn và dán vào ô nộp bài trên hệ thống LMS VLearn để hoàn tất Bài Lab 3!
