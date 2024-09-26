# 🚀 GPTalk - Aplicação de IA Generativa para Geração de Texto 🎉

## 📚 O que é Inteligência Artificial Generativa?
A Inteligência Artificial Generativa é um ramo da IA focado na criação de novos conteúdos (texto, imagens, música, etc.) com base em dados já existentes. Ao invés de apenas analisar e classificar, a IA generativa cria! Ela aprende padrões de grandes quantidades de dados e os utiliza para gerar algo totalmente novo. Um dos exemplos mais populares dessa tecnologia é a geração de texto, e é exatamente isso que a nossa aplicação faz: gerar textos com base em entradas fornecidas pelo usuário! 📝🤖

---

## 🤔 Modelos Utilizados
Nesta aplicação, utilizamos dois modelos de IA generativa que são populares e acessíveis:

 - GPT-J 6B: Um modelo de IA com 6 bilhões de parâmetros, conhecido por gerar textos mais complexos e coerentes. Ele é mais robusto e produz resultados mais detalhados, exigindo um pouco mais de poder computacional.

 - GPT-Neo 1.3B: Um modelo menor, com 1,3 bilhões de parâmetros, perfeito para quem está começando e quer explorar a geração de texto de maneira rápida e sem muita exigência de hardware. Ideal para setups mais modestos, como uma GPU RTX 4060. 🚀

Ambos os modelos utilizam arquitetura de Transformer, que é extremamente eficiente para tarefas de linguagem natural.

---

## 💻 Como Funciona a Aplicação?
Essa aplicação web usa a IA generativa para criar textos baseados em um input fornecido pelo usuário. Quando você insere um texto na página, o modelo de IA escolhido processa esse input e gera uma sequência de texto que pode continuar a frase, responder perguntas ou até criar algo novo!

Os principais componentes são:

 - Front-end: Feito com HTML, CSS e JavaScript, para uma interface simples e intuitiva onde o usuário insere o texto.
 - Back-end: Um servidor Flask que processa a solicitação, carrega o modelo de IA e gera a resposta.
 - Modelos: GPT-J 6B ou GPT-Neo 1.3B, que são carregados via transformers da Hugging Face e processados usando PyTorch.

---

## 🛠️ Como Instalar e Executar Localmente?
### Pré-requisitos:

 - Python 3.8+
 - Uma GPU compatível com CUDA
 - Virtualenv ou outro ambiente virtual para gerenciar dependências

### Passo a passo:

 1. Clone o Repositório:

 ```bash
 git clone https://github.com/seu-usuario/gptalk.git
 cd gptalk
 ```

 2. Crie e Ative um Ambiente Virtual:

 ```bash
 python -m venv env
 env\Scripts\activate      # Windows
 ```
 3. Instale as Dependências:

 ```bash
 pip install -r requirements.txt --extra-index-url https://download.pytorch.org/whl/cu118
 ```
 **Verifique se a sua GPU é compatível com CUDA**

 4. Baixe o modelo que deseja usar (GPT-J ou GPT-Neo) pela Hugging Face:

 **Execute o arquivo `cuda.py` para verificar se o `PyTorch` reconhece sua GPU**

 ```bash
 from transformers import AutoModelForCausalLM, AutoTokenizer
 model = AutoModelForCausalLM.from_pretrained("EleutherAI/gpt-j-6B")
 tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-j-6B")
```

 5. Inicie o Servidor Flask:

 ```bash
 python app.py
 ```

 1. Acesse a Aplicação no Navegador: Abra o navegador e vá até http://localhost:5000/.

---

## 🌟 Como Usar?

 1. Abra a aplicação no navegador.
 2. Digite qualquer frase ou texto no campo de input.
 3. Clique em "Gerar Texto" e veja a mágica acontecer! ✨
 4. O resultado gerado pela IA será mostrado logo abaixo.

---

## ⚙️ Personalização
Você pode modificar a aplicação para usar diferentes modelos ou ajustar os parâmetros de geração, como o tamanho máximo da sequência de texto ou a temperatura (para controlar a aleatoriedade).

Para isso, basta modificar as configurações no arquivo app.py ao seu gosto.
Lembrando que os modelos propostos são simples por conta da limitação de hardware (o mínimo indicado para um modelo decente são 16GB de VRAM).

---

## 🎯 Aplicações Práticas
Este projeto é perfeito para quem quer explorar as capacidades de IA generativa em diferentes áreas:

 - Criação de conteúdo: Escrever blogs, artigos ou histórias curtas.
 - Assistente pessoal: Respostas automáticas a perguntas e geração de ideias.
 - Exploração de IA: Para estudantes e profissionais de TI que desejam aprender mais sobre machine learning e processamento de linguagem natural.


## 🏁 Próximos Passos

 - Implementar novos modelos de IA.
 - Melhorar a interface do usuário para incluir mais opções de customização.
 - Explorar a geração de texto em múltiplos idiomas.

## 📚 Referência

Essa aplicação usa como base os modelos GPT-J 6B e GPT-Neo 1.3B da [EleutherAI](https://github.com/EleutherAI/gpt-neo)

## 🛡️ Licença
Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE.txt) para mais detalhes.