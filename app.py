import chainlit as cl
from langchain_core.messages import HumanMessage
from agent import graph  # Import cái graph đã compile của bro


@cl.on_chat_start
async def on_chat_start():
    # Khởi tạo session và gửi lời chào
    cl.user_session.set("graph", graph)
    cl.user_session.set("thread_id", "chainlit_session_01")

    await cl.Message(content="✈️ **TravelBuddy** đã sẵn sàng! Bro muốn vi vu đi đâu thế?").send()


@cl.on_message
async def main(message: cl.Message):
    # Lấy graph và thread_id từ session
    graph = cl.user_session.get("graph")
    thread_id = cl.user_session.get("thread_id")
    config = {"configurable": {"thread_id": thread_id}}

    # Gửi một tin nhắn trống để hiển thị hiệu ứng "đang xử lý"
    msg = cl.Message(content="")

    # Chạy graph (sử dụng stream để bắt được các bước trung gian nếu muốn)
    # Ở đây dùng invoke cho đơn giản giống code cũ của bro
    input_data = {"messages": [HumanMessage(content=message.content)]}

    # Hiển thị trạng thái đang suy nghĩ
    async with cl.Step(name="TravelBuddy Agent"):
        result = await cl.make_async(graph.invoke)(input_data, config=config)

    # Lấy câu trả lời cuối cùng
    final_answer = result["messages"][-1].content

    # Gửi câu trả lời ra UI
    msg.content = final_answer
    await msg.send()