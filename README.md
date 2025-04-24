# 🚨 Alertmanager Google Chat Webhook

Este projeto é uma API simples em Python (Flask) que recebe webhooks do [Prometheus Alertmanager](https://prometheus.io/docs/alerting/latest/alertmanager/) e envia alertas formatados para um espaço do [Google Chat](https://chat.google.com) via webhook.

---

## 📦 Requisitos

- Python 3.13+
- [Google Chat Webhook URL](https://developers.google.com/chat/how-tos/webhooks)
- Alertmanager configurado

---

## 🧪 Criando o projeto local com `venv`

```bash
# Clone o projeto
git clone https://github.com/seu-usuario/alertmanager-gchat.git
cd alertmanager-gchat

# Crie um ambiente virtual
python3.13 -m venv venv
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt
```

---

## ⚙️ Configuração

Crie uma variável de ambiente com o webhook do Google Chat:

```bash
export GOOGLE_CHAT_WEBHOOK='https://chat.googleapis.com/v1/spaces/.../messages?key=...&token=...'
```

---

## 🚀 Executando localmente

Com o ambiente virtual ativado e a variável configurada:

```bash
python app.py
```

A API estará disponível em `http://localhost:5000/`.

---

## 📡 Testando a API localmente

Execute o script de teste:

```bash
python test_alertmanager_webhook.py
```

---

## 🐳 Docker (opcional)

Você pode rodar a API com Docker:

```bash
docker build -t alertmanager-gchat .
docker run -p 5000:5000 \
  -e GOOGLE_CHAT_WEBHOOK=https://chat.googleapis.com/... \
  alertmanager-gchat
```

---

## 🧠 Como funciona

1. O Alertmanager envia alertas em formato JSON via POST.
2. A API formata os alertas como texto simples.
3. Envia a mensagem via webhook para o espaço do Google Chat.

---

## 📋 Exemplo de uso no `alertmanager.yaml`

```yaml
receivers:
  - name: google-chat
    webhook_configs:
      - url: 'http://alertmanager-gchat.monitoring.svc:5000'
        send_resolved: true
```

---

## 🧱 Stack utilizada

- Python 3.13
- Flask 3.1.0
- httpx 0.28.1
- Docker (opcional)
- Google Chat Webhook

---

## 🛡️ Licença

MIT - Gustavo @ Accellog