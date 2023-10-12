from langchain.llms import OpenAI

llm = OpenAI(temperature=0.8)
prompt = "Generate a 30-40 word literature review excerpt in an academic tone summarizing the key findings and contributions of the research article titled 'Title of the Article' by Author Name. Ensure that the generated content is concise, precise, and maintains the scholarly style and language. Replace 'Title of the Article' and 'Author Name' with the specific details from the research article you're working with. This prompt instructs the LLM to provide a focused and academically styled summary of the research article, incorporating key findings and the author's name, and keeping the response within the desired word limit."

result = llm.generate([prompt])
print(result)
