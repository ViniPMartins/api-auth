from flask import Flask, render_template, request, redirect, url_for, session
import requests

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'  # Necessário para usar sessões

API_BASE_URL = "http://localhost:8000"  # URL da API FastAPI

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    response = requests.post(f"{API_BASE_URL}/token")
    if response.status_code == 200:
        data = response.json()
        session['access_token'] = data['access_token']
        session['csrf_token'] = "token_csrf_gerado_aqui"  # Token CSRF gerado na API
        return redirect(url_for('protected'))
    else:
        return "Erro na autenticação", 400

@app.route('/protected', methods=['GET', 'POST'])
def protected():
    if 'access_token' not in session:
        return redirect(url_for('index'))
    if request.method == 'POST':
        headers = {
            "Authorization": f"Bearer {session['access_token']}",
            "x-csrf-token": session['csrf_token'],
            "Origin": request.host_url
        }
        print(request.host_url)
        response = requests.post(f"{API_BASE_URL}/api/sua-rota", headers=headers)
        if response.status_code == 200:
            return "Requisição bem-sucedida: " + response.json().get('message', '')
        else:
            return "Erro na requisição: " + response.text, response.status_code
    return render_template('protected.html')

if __name__ == "__main__":
    app.run(debug=True, port=5001)
