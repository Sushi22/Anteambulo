import openai

api_key = ""
openai.api_key = api_key

endpoint = "https://sysops-28015.openai.azure.com/"

question = "What is the capital of France?"
response = openai.Completion.create(
  engine="gpt-4-turbo", 
  prompt=question,
  max_tokens=50 
)

print(response.choices[0].text.strip())