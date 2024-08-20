from langchain_ollama import OllamaLLM  
from langchain_core.prompts import ChatPromptTemplate

template = """
Answer the following question:

Here is the conversation history {context}

Question: {question}

Answer:

"""

prompt = ChatPromptTemplate.from_template(template)
model = OllamaLLM(model="llama3")
chain = prompt | model

def handle_conversation(): 
    context = ""
    print("Welcome to the AI-WSL chatbot!")
    while True:
        question = input("Ask a question: ")
        if question == "exit":
            break

        result = chain.invoke({"context": context, "question": question})
        print(result)
        context += f"Question: {question}\nAnswer: {result}\n"

if __name__ == "__main__":
    handle_conversation()