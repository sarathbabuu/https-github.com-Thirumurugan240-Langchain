import os

os.environ["OPENAI_API_KEY"] = "OPENAI_API_KEY"
os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGSMITH_API_KEY"] = "LANGSMITH_API_KEY"
os.environ["LANGSMITH_PROJECT"] = "simple-rag-app"

from dotenv import load_dotenv
load_dotenv(override=True)

# from langchain_openai import ChatOpenAI

# llm = ChatOpenAI(
#     model="gpt-4o-mini",
#     temperature=0
# )

# p = "Write a simple Hello World message."
# print(llm.invoke(p).content)

# from langchain_openai import ChatOpenAI
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser

# prompt = ChatPromptTemplate.from_template("Explain {topic} in one simple sentence.")
# model = ChatOpenAI(model="gpt-4o-mini")
# chain = prompt | model | StrOutputParser()

# # This run is automatically recorded in LangSmith.
# print(chain.invoke({"topic": "LangSmith"}))

from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model="gpt-4o-mini")
prompts = ["...", "...", "..."]
for p in prompts:
 print(llm.invoke(p).content)
