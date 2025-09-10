import os
from flask import Flask, request, jsonify, render_template_string
import mysql.connector

app = Flask(__name__)

CONFIG = {
    'host': os.getenv('DB_HOST', '127.0.0.1'),
    'user': os.getenv('DB_USER', 'flaskuser'),
    'password': os.getenv('DB_PASS', 'flaskpass'),
    'database': os.getenv('DB_NAME', 'cp'),
    'charset': 'latin1',
    'use_unicode': True
}

db_config = {
    'host': 'localhost',
    'database': 'codigos_postales	',            
    'user': 'flaskuser',
    'password': 'flaskpass',
    'auth_plugin': 'mysql_native_password'
}

HTML = """
<!doctype html>
<html>
<head>
  <meta charset="latin1"/>
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <title>Buscador de Códigos Postales en México</title>
  <style>
    body{font-family:system-ui,Arial,sans-serif;max-width:900px;margin:2rem auto;padding:0 1rem}
    input{width:100%;padding:.8rem;border:1px solid #ccc;border-radius:.6rem}
    .item{padding:.6rem .4rem;border-bottom:1px solid #eee}
    .small{color:#555;font-size:.9rem}
  </style>
</head>
<body>
  <h1>Buscador de direcciones</h1>
  <p>Escribe parte de una colonia,código postal o municipio:</p>
  <input id="q" placeholder="Ej. Narvarte / Benito Juárez / 01210"/>
  <div id="results"></div>
  <script>
    const q = document.getElementById('q');
    const results = document.getElementById('results');
    let ctrl;
    q.addEventListener('input', async () => {
      const term = q.value.trim();
      if (term.length < 2){ results.innerHTML=''; return; }
      ctrl && ctrl.abort();
      ctrl = new AbortController();
      const res = await fetch('/buscar?q=' + encodeURIComponent(term), {signal: ctrl.signal});
      const data = await res.json();
      results.innerHTML = data.map(r => `
        <div class="item">
          <div><strong>${r.d_asenta}</strong> <span class="small">(${r.d_tipo_asenta||'—'})</span></div>
          <div class="small">${r.D_mnpio}, ${r.d_estado} · CP ${r.d_codigo}${r.d_ciudad? ' · ' + r.d_ciudad : ''}</div>
        </div>`).join('');
    });
  </script>
</body>
</html>
"""


def conn():
#    return mysql.connector.connect(**CONFIG)
    return mysql.connector.connect(**db_config)

@app.get('/')
def home():
    return render_template_string(HTML)

@app.get('/buscar')
def buscar():
    term = request.args.get('q', '').strip()
    if not term or len(term) < 2:
        return jsonify([])

    # Normaliza comodines para LIKE
    like = f"%{term.replace('%','').replace('_',' ')}%"

    sql = (
        "SELECT d_asenta, d_tipo_asenta, D_mnpio, d_estado, d_codigo, d_ciudad "
        "FROM cp "
        "WHERE d_asenta LIKE %s OR D_mnpio LIKE %s OR d_codigo LIKE %s "
        "ORDER BY d_estado, D_mnpio, d_asenta LIMIT 50"
    )

    with conn() as c:
        with c.cursor(dictionary=True) as cur:
            cur.execute(sql, (like, like, like))
            rows = cur.fetchall()
            return jsonify(rows)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
