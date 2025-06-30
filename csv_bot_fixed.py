from langchain_community.llms import Ollama
from langchain_experimental.agents import create_csv_agent

print("✅ Running the fixed file")

llm = Ollama(model="llama3")
csv_path = "generated_employee_data.csv"

agent = create_csv_agent(llm, csv_path, verbose=True)

print("🟢 Ask questions about your CSV! (type 'exit' to quit)\n")
while True:
    q = input("💬 You: ")
    if q.lower() in ["exit", "quit"]:
        break
    response = agent.run(q)
    print("🤖 Bot:", response)
