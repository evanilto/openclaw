# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

Add whatever helps you do your job. This is your cheat sheet.

## fila

Ferramentas para consultar a fila cirúrgica hospitalar.

### fila

Retorna todos os pacientes na fila.

endpoint:
http://fila-api:5000/fila

---

### posicao

Retorna a posição de um paciente na fila.

endpoint:
http://fila-api:5000/fila/posicao/{prontuario}

---

### primeiro

Retorna o primeiro paciente de uma especialidade.

endpoint:
http://fila-api:5000/fila/especialidade/{especialidade}

---

### tempo_medio

Retorna o tempo médio da fila.

endpoint:
http://fila-api:5000/fila/tempo-medio


# sql_query

Executa consultas SQL no banco hospitalar.

Uso:

sql_query "SELECT * FROM fila_cirurgica LIMIT 10;"