from langchain_ollama import OllamaLLM
from langchain_experimental.agents import create_csv_agent
from langchain_core.runnables.config import RunnableConfig

print("✅ Running latest and fixed version")

llm = OllamaLLM(model="llama3")
csv_path = "generated_employee_data.csv"

# ✅ FIXED config
config = RunnableConfig(configurable={"allow_dangerous_code": True})

agent = create_csv_agent(
    llm,
    csv_path,
    verbose=True,
    allow_dangerous_code=True
).with_config(config)

# ✅ Chat loop
print("🟢 Ask questions about your CSV! (type 'exit' to quit)\n")
while True:
    user_input = input("💬 You: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    result = agent.run(user_input)
    print("🤖 Bot:", result)
