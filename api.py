# Código do FastAPI que já discutimos
# (coloque este código em um arquivo chamado `api.py` e execute-o)

from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

app = FastAPI()

ALLOWED_ORIGINS = ["http://localhost:8501", "http://127.0.0.1:5001/"]  # Streamlit roda em localhost:8501

SECRET_KEY = "sua_chave_secreta"
ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido ou expirado")

@app.post("/api/sua-rota")
async def sua_rota(request: Request, token_payload: dict = Depends(verify_token)):
    origin = request.headers.get("origin")
    referer = request.headers.get("referer")

    if origin not in ALLOWED_ORIGINS and (referer is None or not any(r in referer for r in ALLOWED_ORIGINS)):
        raise HTTPException(status_code=403, detail="Acesso não autorizado")

    csrf_token = request.headers.get("x-csrf-token")
    if csrf_token is None or csrf_token != token_payload.get("csrf_token"):
        raise HTTPException(status_code=403, detail="Token CSRF inválido ou ausente")

    return {"message": "Requisição válida!"}

@app.post("/token")
async def login():
    payload = {
        "sub": "usuário_id",
        "csrf_token": "token_csrf_gerado_aqui"
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": token, "token_type": "bearer"}
