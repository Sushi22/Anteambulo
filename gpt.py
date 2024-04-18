import openai

api_key = "f5b55c3f2f504eb3a63c1875b0241ce2"
openai.api_key = api_key

endpoint = "https://sysops-28015.openai.azure.com/"

question = "What is the capital of France?"
response = openai.Completion.create(
  engine="text-davinci-003", 
  prompt=question,
  max_tokens=50 
)

print(response.choices[0].text.strip())