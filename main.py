import os 
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

CHAVE_API_KEY= os.getenv("GEMINI_API_KEY")
genai.configure(api_key=CHAVE_API_KEY)
MODELO_ESCOLHIDO = "gemini-1.5-flash"

prompt_sistema = "Liste apenas o nome dos produtos, e ofereça uma breve descrição de cada um. "
llm= genai.GenerativeModel(
    model_name=MODELO_ESCOLHIDO,
    system_instruction=prompt_sistema
)

pergunta= "Liste tres produtos de moda sustentável para ir ao shopping"

resposta=llm.generate_content(pergunta)
print(f'resposta gerada: {resposta.text}')