from llm import get_llm

# Test the LLM connection
llm = get_llm()
response = llm.invoke("Hello, world!")
print(response)