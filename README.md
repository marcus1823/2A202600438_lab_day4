# 🧳 TravelBuddy - AI Travel Planning Agent

**TravelBuddy** là một hệ thống Assistant thông minh được xây dựng trên nền tảng **LangGraph** và **OpenAI**. Hệ thống có khả năng tư vấn lịch trình, tìm kiếm chuyến bay, khách sạn và tính toán ngân sách du lịch thực tế tại Việt Nam.

---

## 🌟 Tính năng nổi bật

- **Lập kế hoạch thông minh:** Tự động truy vấn thông tin chuyến bay và khách sạn dựa trên yêu cầu người dùng.
- **Xâu chuỗi công cụ (Tool Chaining):** Tự động kết hợp nhiều công cụ (search_flights -> search_hotels -> calculate_budget) để tạo giải pháp trọn gói.
- **Trí nhớ dài hạn (Persistence):** Ghi nhớ thông tin khách hàng xuyên suốt cuộc trò chuyện nhờ bộ nhớ MemorySaver.
- **Nhận thức thời gian:** AI tự động cập nhật ngày hiện tại để đưa ra tư vấn chính xác theo ngữ cảnh thời gian thực.
- **Giao diện hiện đại:** Tích hợp giao diện Web trực quan với Chainlit, hỗ trợ hiển thị từng bước xử lý của Agent.

---

## 🛠 Kiến trúc hệ thống

Dự án được xây dựng với các thành phần chính:
- **State Management:** Sử dụng TypedDict và add_messages để quản lý luồng hội thoại đồng nhất.
- **Graph Logic:**
    - agent_node: Xử lý suy nghĩ, gọi LLM và quyết định sử dụng công cụ.
    - tools_condition: Điều hướng thông minh giữa việc trả lời trực tiếp hoặc kích hoạt Node công cụ.
    - ToolNode: Thực thi các hàm Python xử lý dữ liệu thực tế.
- **Data:** Cơ sở dữ liệu mô phỏng (FLIGHTS_DB, HOTELS_DB) cho các thành phố: Hà Nội, Đà Nẵng, TP.HCM, Phú Quốc.

---

## 🚀 Hướng dẫn cài đặt và khởi chạy

### 1. Chuẩn bị môi trường
Yêu cầu Python 3.10 trở lên. Khuyến khích sử dụng môi trường ảo (venv).

# Tạo môi trường ảo
python -m venv venv

# Kích hoạt môi trường ảo (macOS/Linux)
source venv/bin/activate

# Kích hoạt môi trường ảo (Windows)
# venv\Scripts\activate

### 2. Cài đặt thư viện
pip install langchain-openai langgraph chainlit python-dotenv typing-extensions

### 3. Cấu hình biến môi trường
Tạo file .env tại thư mục gốc của dự án:
OPENAI_API_KEY=sk-your-openai-api-key-here

### 4. Khởi chạy ứng dụng
Hệ thống hỗ trợ 2 chế độ khởi chạy:

- Chế độ Console (Terminal):
python agent.py

- Chế độ Giao diện Web (Chainlit UI):
chainlit run app.py -w

---

## 📝 Cấu trúc thư mục dự án

- agent.py: File chính chứa cấu trúc Graph và logic vận hành Agent.
- tools.py: Định nghĩa các công cụ xử lý chuyến bay, khách sạn và ngân sách.
- app.py: Giao diện người dùng trên Chainlit.
- system_prompt.txt: Chứa Persona và các quy tắc hành xử của AI.
- chat_history.json: File tự động lưu trữ lịch sử hội thoại dưới dạng JSON.

---

## 🛡️ Bảo mật & Guardrails

Hệ thống được thiết lập các rào cản bảo mật:
- Phạm vi hỗ trợ: Chỉ xử lý các yêu cầu liên quan đến du lịch.
- Từ chối yêu cầu ngoài: Tự động từ chối các yêu cầu viết code, giải toán, nấu ăn...
- Bảo vệ dữ liệu: API Key được quản lý qua biến môi trường.

---

**Phát triển bởi:** Trương Minh Tiền - 2A202600438 - (Lab 4 - AI Thực Chiến - VinUniversity) 🚀