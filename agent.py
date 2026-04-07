from  typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from  tools import  search_flights, search_hotels, calculate_budget
from dotenv import load_dotenv
import datetime
from langgraph.checkpoint.memory import MemorySaver

load_dotenv()

now = datetime.datetime.now()
current_date_str = now.strftime("%d/%m/%Y")

# 1. Đọc System Prompt
with open("system_prompt.txt", "r", encoding="utf-8") as f:
    raw_prompt = f.read()
    # Chèn ngày thực tế vào chỗ trống {current_date} trong file prompt
    SYSTEM_PROMPT = raw_prompt.replace("{current_date}", current_date_str)

# 2. Khai báo State để lưu trữ thông tin cuộc hội thoại
class AgentState(TypedDict):
    messages: Annotated[list, add_messages]

# 3. Khởi tạo LLM và Tools
tools_list = [search_flights, search_hotels, calculate_budget]
llm = ChatOpenAI(model="gpt-4o-mini")
llm_with_tools = llm.bind_tools(tools_list)

# 4. Agent Node để lưu trữ trạng thái cuộc hội thoại và gọi LLM để xử lý
def agent_node(state: AgentState):
    messages = state["messages"]

    # Đảm bảo SystemMessage luôn nằm ở đầu lịch sử hội thoại
    if not any(isinstance(msg, SystemMessage) for msg in messages):
        messages = [SystemMessage(content=SYSTEM_PROMPT)] + messages

    # Gọi LLM
    response = llm_with_tools.invoke(messages)

    # Logging để debug
    if response.tool_calls:
        for tc in response.tool_calls:
            print(f">>> Gọi tool: {tc['name']}")
    else:
        print(f">>> Trả lời trực tiếp")

    # QUAN TRỌNG: Trả về đúng key 'messages' (số nhiều)
    return {"messages": [response]}

# 5. Xây dựng Graph
builder = StateGraph(AgentState)
builder.add_node("agent", agent_node)

tool_node = ToolNode(tools_list)
builder.add_node("tools",tool_node )

# Todo: Sinh viên tự khai báo edges
# builder.add_edge(START,...)
# builder.add_conditional_edge("agent", tools_condition)
# builder.add_edge("tools", "agent")

# bắt đầu:
# 1. Điểm bắt đầu đi vào agent
builder.add_edge(START, "agent")

# 2. Agent quyết định đi tiếp sang tools hoặc kết thúc (END)
builder.add_conditional_edges("agent", tools_condition)

# 3. QUAN TRỌNG: Tool chạy xong phải quay về agent để nó trả lời khách
builder.add_edge("tools", "agent")

memory = MemorySaver()

graph = builder.compile(checkpointer=memory)

def log_chat(user_msg, ai_msg):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("chat_history.log", "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] Bạn: {user_msg}\n")
        f.write(f"[{timestamp}] TravelBuddy: {ai_msg}\n")
        f.write("-" * 50 + "\n")

# 6. Chat loop
if __name__ == "__main__":
    config = {"configurable": {"thread_id": "travel_buddy_session_01"}}
    print("=" * 60)
    print("TravelBuddy – Trợ lý Du lịch Thông minh")
    print("    Gõ 'quit' để thoát")
    print("=" * 60)

    while True:
        user_input = input("\nBạn: ").strip()
        if user_input.lower() in ("quit", "exit", "q"):
            print("Tạm biệt bro! Hẹn gặp lại nhé.")
            break

        print("\nTravelBuddy đang suy nghĩ...")

        # Sử dụng HumanMessage object thay vì tuple để LangGraph nhận diện tốt hơn
        input_data = {"messages": [HumanMessage(content=user_input)]}


        result = graph.invoke(input_data, config=config)


        # Lấy tin nhắn cuối cùng (là AIMessage từ LLM)
        final_message = result["messages"][-1]
        log_chat(user_input, final_message.content)
        print(f"\nTravelBuddy: {final_message.content}")



