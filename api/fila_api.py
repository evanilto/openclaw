from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

def get_conn():
    return psycopg2.connect(
        host=os.environ.get("DB_HOST","postgres"),
        database=os.environ.get("DB_NAME","hospital"),
        user=os.environ.get("DB_USER","hospital"),
        password=os.environ.get("DB_PASSWORD","hospital123")
    )

# -----------------------------
# LISTAR FILA COMPLETA
# -----------------------------

@app.route("/fila")
def fila():

    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
        SELECT paciente, especialidade, procedimento, prioridade, data_inclusao
        FROM vw_fila_cirurgica
        ORDER BY prioridade DESC, data_inclusao
    """)

    rows = cur.fetchall()

    cur.close()
    conn.close()

    resultado = []

    for r in rows:
        resultado.append({
            "paciente": r[0],
            "especialidade": r[1],
            "procedimento": r[2],
            "prioridade": r[3],
            "data_inclusao": str(r[4])
        })

    return jsonify(resultado)

# -----------------------------
# POSIÇÃO DO PACIENTE NA FILA
# -----------------------------

@app.route("/fila/posicao/<prontuario>")
def posicao(prontuario):

    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
        SELECT prontuario,
               ROW_NUMBER() OVER (
                    ORDER BY prioridade DESC, data_inclusao
               ) as posicao
        FROM fila_cirurgica
        WHERE status='aguardando'
    """)

    rows = cur.fetchall()

    cur.close()
    conn.close()

    for r in rows:
        if r[0] == prontuario:
            return jsonify({
                "prontuario": prontuario,
                "posicao": r[1]
            })

    return jsonify({"erro":"paciente não encontrado"}),404

# -----------------------------
# PRIMEIRO DA ESPECIALIDADE
# -----------------------------

@app.route("/fila/especialidade/<esp>")
def especialidade(esp):

    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
        SELECT paciente, procedimento, prioridade, data_inclusao
        FROM vw_fila_cirurgica
        WHERE especialidade=%s
        ORDER BY prioridade DESC, data_inclusao
        LIMIT 1
    """,(esp,))

    row = cur.fetchone()

    cur.close()
    conn.close()

    if row:
        return jsonify({
            "paciente": row[0],
            "procedimento": row[1],
            "prioridade": row[2],
            "data_inclusao": str(row[3])
        })

    return jsonify({"erro":"nenhum paciente encontrado"}),404

# -----------------------------
# QUANTIDADE NA FILA
# -----------------------------

@app.route("/fila/total")
def total():

    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
        SELECT especialidade, COUNT(*)
        FROM vw_fila_cirurgica
        GROUP BY especialidade
    """)

    rows = cur.fetchall()

    cur.close()
    conn.close()

    resultado = {}

    for r in rows:
        resultado[r[0]] = r[1]

    return jsonify(resultado)

@app.route("/fila/tempo-medio")
def tempo_medio():

    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
        SELECT ROUND(AVG(CURRENT_DATE - data_inclusao))
        FROM fila_cirurgica
        WHERE status='aguardando'
    """)

    row = cur.fetchone()

    cur.close()
    conn.close()

    return jsonify({
        "tempo_medio_dias": int(row[0]) if row[0] else 0
    })

@app.route("/fila/tempo-medio/<especialidade>")
def tempo_medio_especialidade(especialidade):

    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
        SELECT ROUND(AVG(CURRENT_DATE - data_inclusao))
        FROM fila_cirurgica
        WHERE status='aguardando'
        AND especialidade=%s
    """,(especialidade,))

    row = cur.fetchone()

    cur.close()
    conn.close()

    return jsonify({
        "especialidade": especialidade,
        "tempo_medio_dias": int(row[0]) if row[0] else 0
    })


app.run(host="0.0.0.0", port=5000)