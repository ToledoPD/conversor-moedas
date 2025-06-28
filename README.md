# 💱 Conversor de Moedas com Envio via WhatsApp

Este projeto é uma API em Python para realizar conversões de moedas em tempo real usando a [AwesomeAPI](https://economia.awesomeapi.com.br) e enviar o resultado diretamente via WhatsApp usando o [CallMeBot](https://www.callmebot.com/).

---

## 🚀 Funcionalidades

- 🔁 Conversão entre moedas (ex: USD para BRL)
- 📩 Envio automático da cotação via WhatsApp
- 🔒 Suporte a arquivos `.env` para proteger chaves sensíveis
- 🧼 Utiliza boas práticas com `.gitignore` e `requirements.txt`

---

## 🛠 Tecnologias

- Python 3.10+
- [requests](https://pypi.org/project/requests/)
- [AwesomeAPI](https://docs.awesomeapi.com.br/api-de-moedas)
- [CallMeBot API](https://www.callmebot.com/)

---

## 📦 Instalação

1. Clone este repositório:

```bash
git clone https://github.com/ToledoPD/conversor-moedas.git
cd conversor-moedas


2. Crie um ambiente virtual:
python -m venv venv
venv\Scripts\activate  # No Windows
# ou
source venv/bin/activate  # No Linux/macOS


3. Instale as dependencias:
pip install -r requirements.txt
