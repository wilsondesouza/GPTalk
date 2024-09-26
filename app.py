from flask import Flask, request, jsonify, render_template
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

app = Flask(__name__)

# Carregar o modelo `gpt-neo-1.3B` ou o `gpt-j-6B`
# Utilize o modelo `gpt-neo-1.3B` caso sua GPU tenha menos que 8GB de memória
# Utilize o modelo `gpt-j-6B` caso sua GPU tenha mais que 8GB de memória
model = AutoModelForCausalLM.from_pretrained("EleutherAI/gpt-neo-1.3B", torch_dtype=torch.float16, device_map="auto").to("cuda")
tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-neo-1.3B")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_text():
    data = request.json
    input_text = data.get('input_text', '')

    # Tokenizar o texto de entrada
    input_ids = tokenizer.encode(input_text, return_tensors="pt").to("cuda")
    
    
    pad_token_id = tokenizer.eos_token_id  # Definir pad_token_id 
    attention_mask = torch.ones(input_ids.shape, device='cuda')  # Cria uma máscara de atenção

    # Gerar o texto
    output = model.generate(
        input_ids, 
        max_length=100, 
        no_repeat_ngram_size=2, 
        top_k=50, 
        do_sample=True,
        pad_token_id=pad_token_id, 
        attention_mask=attention_mask, 
        num_return_sequences=1
        )
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    
    if generated_text.startswith(input_text):
        generated_text = generated_text[len(input_text):].strip()

    return jsonify({'generated_text': generated_text})
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
