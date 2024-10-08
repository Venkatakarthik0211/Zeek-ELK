# !pip install openai
# Assume openai>=1.0.0
from openai import OpenAI
# Create an OpenAI client with your KRUTRIM API KEY and endpoint
  
openai = OpenAI(
    # api_key="3snrwTYR-HZ2kxeb+xIh", # Refer to Create a secret key section
    base_url="https://cloud.olakrutrim.com/v1",
)
  
chat_completion = openai.chat.completions.create(
    model="Meta-Llama-3-8B-Instruct",
    messages=[
        {"role": "system", "content": "I want to know who are you and from where you originated"},
        {"role": "user", "content": "Hello"}
    ],
    frequency_penalty= 0, # Optional, Defaults to 0. Range: -2 to 2
    logit_bias= {2435: -100, 640: -100},
    # logprobs= true, # Optional, Defaults to false
    top_logprobs= 2, # Optional. Range: 0 to 50
    max_tokens= 256, # Optional
    n= 1, # Optional, Defaults to 1
    presence_penalty= 0, # Optional, Defaults to 0. Range: -2 to 2
    response_format= { "type": "text" }, # Optional, Defaults to text
    # stop= null, # Optional, Defaults to null. Can take up to 4 sequences where the API will stop generating further tokens.
    # stream= false, # Optional, Defaults to false
    temperature= 0, # Optional, Defaults to 1. Range: 0 to 2
    top_p= 1 # Optional, Defaults to 1. We generally recommend altering this or temperature but not both.
)
print(chat_completion.choices[0].message.content)