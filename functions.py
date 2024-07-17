from groq import Groq
from prompt import PromptCls

class ChatModel:
  def __init__(self):
    pass
  @staticmethod
  def GroqFunction(message_list: list) -> str:
    
    system_prompt = PromptCls.PromptStyle()
    
    system_messages = {"role" : "system", "content" : system_prompt}
    message_list.append(system_messages)
    
    GROQ_API_KEY = str("Enter API Key")
    
    client = Groq(api_key = str(GROQ_API_KEY))
    
    chat_completion = client.chat.completions.create(
        messages = message_list,
        model = "llama3-70b-8192",
        temperature = 0.5,
        )
    response = chat_completion.choices[0].message.content
    return response
