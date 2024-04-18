import openai

openai.api_key = "f5b55c3f2f504eb3a63c1875b0241ce2"
openai.api_base =  "https://sysops-28015.openai.azure.com/" 
openai.api_type = 'azure'
openai.api_version = '2024-02-15-preview'

def get_gpt_response(system_content, user_content):
    response = openai.ChatCompletion.create(
        engine='SYSOPS-28015', 
        messages=get_prompt_message(system_content, user_content),
        max_tokens=1000,
        temperature=0
    )
    return response["choices"][0]["message"]["content"]

def get_prompt_message(system_content, user_content):
    message = [{"role":"system", "content":system_content},{"role":"user", "content":user_content}]
    return message

print(get_gpt_response("Rephrase the sentence into a humble way", "I work at Myntra"))