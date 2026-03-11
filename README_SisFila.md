# Assistente de Fila Cirúrgica com OpenClaw

## Visão Geral

Este projeto implementa um **assistente inteligente para consulta da fila cirúrgica hospitalar**.

O sistema permite que médicos consultem informações da fila através de linguagem natural usando o **OpenClaw**, que consulta uma **API Python** conectada a um **banco PostgreSQL**.

Exemplos de perguntas:

* Quem é o primeiro paciente da fila de cardiologia?
* Qual a posição do paciente João da Silva?
* Quantos pacientes aguardam cirurgia ortopédica?
* Qual o tempo médio de espera da fila?

---

# Arquitetura do Sistema

```
Usuário / Médico
        ↓
      HTTPS
        ↓
      NGINX
        ↓
    OpenClaw
        ↓
     API Python
        ↓
    PostgreSQL
```

Componentes:

| Serviço  | Função                     |
| -------- | -------------------------- |
| nginx    | proxy HTTPS                |
| openclaw | agente conversacional      |
| fila-api | API para consultas da fila |
| postgres | banco de dados hospitalar  |

---

# Estrutura de Diretórios

```
openclaw/
│
├─ docker-compose.yml
├─ nginx.conf
├─ README.md
│
├─ api/
│   ├─ Dockerfile
│   ├─ fila_api.py
│   └─ requirements.txt
│
├─ db/
│   └─ init.sql
│
├─ config/        # configuração do OpenClaw
├─ workspace/     # agentes e sessões
└─ certs/         # certificados HTTPS
```

---

# Containers Docker

Após subir o sistema teremos:

```
openclaw
openclaw-nginx
fila-api
fila-db
```

Rede docker:

```
openclaw-net
```

---

# Portas Utilizadas

| Porta | Serviço          |
| ----- | ---------------- |
| 8443  | acesso HTTPS     |
| 18789 | gateway OpenClaw |
| 5000  | API da fila      |
| 5432  | PostgreSQL       |

---

# Banco de Dados

Banco:

```
hospital
```

Tabela principal:

```
fila_cirurgica
```

Estrutura:

```
id
paciente
prontuario
especialidade
procedimento
prioridade
data_inclusao
status
```

---

# View de Consulta

Para facilitar consultas foi criada a view:

```
vw_fila_cirurgica
```

Ela retorna apenas pacientes com status:

```
aguardando
```

---

# API REST

Endpoint principal:

```
GET /fila
```

Exemplo:

```
curl http://localhost:5000/fila
```

Resposta:

```
[
 {
  "paciente": "João da Silva",
  "especialidade": "cardiologia",
  "procedimento": "revascularização",
  "prioridade": "alta",
  "data_inclusao": "2025-11-02"
 }
]
```

---

# Subir o Sistema

Primeira instalação:

```
docker compose up -d --build
```

Verificar containers:

```
docker ps
```

---

# Resetar Banco de Dados

Para recriar o banco:

```
docker compose down -v
docker compose up -d
```

Isso executará novamente:

```
db/init.sql
```

---

# Logs dos Containers

OpenClaw:

```
docker logs openclaw
```

API:

```
docker logs fila-api
```

Banco:

```
docker logs fila-db
```

---

# Testes

Testar API:

```
curl http://localhost:5000/fila
```

Testar acesso interno Docker:

```
docker exec -it openclaw curl http://fila-api:5000/fila
```

---

# Segurança

O acesso externo é protegido por:

* HTTPS via nginx
* token do gateway OpenClaw

Variáveis de ambiente importantes:

```
OPENCLAW_GATEWAY_TOKEN
OPENAI_API_KEY
```

---

# Próximas Evoluções

Possíveis melhorias:

* cálculo automático da posição na fila
* tempo médio de espera por especialidade
* alertas de pacientes prioritários
* dashboard da fila cirúrgica
* integração com WhatsApp
* integração com sistema hospitalar (AGHU / MV / Tasy)

---

# Autor

Projeto desenvolvido para suporte à gestão da fila cirúrgica hospitalar.
