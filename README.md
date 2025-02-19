
## Como usar

1. Execute o arquivo `main.py` para iniciar o programa.
2. Insira a URL da lista de reprodução ou do vídeo individual no campo de entrada.
3. Selecione o diretório de salvamento clicando no botão "Procurar" ou digitando o caminho manualmente.
4. Clique no botão "Baixar" para iniciar o download.
5. O progresso do download será exibido na barra de progresso.
6. Uma mensagem de sucesso será exibida ao finalizar o download.



andrefrancys@gmail.com 
youtube: @andrefrancys2335

# YouTube Video Downloader

Este é um aplicativo de interface gráfica para baixar vídeos do YouTube usando `yt-dlp`.

## 📌 Funcionalidades
- Baixe vídeos individuais do YouTube
- Escolha o diretório de salvamento
- Barra de progresso para acompanhar o download

## 🛠️ Requisitos
- Python 3.x
- yt-dlp
- Tkinter (incluído na instalação padrão do Python)
- Pillow (para exibir imagens na interface)

## 🚀 Instalação
1. Clone o repositório:
   ```bash
   git clone https://github.com/andrefrancys/andyoupy.git
   cd andyoupy
   ```
2. Instale as dependências:
   ```bash
   pip install yt-dlp pillow
   ```

## 🎯 Como Usar
1. Execute o script:
   ```bash
   python main.py
   ```
2. Insira a URL do vídeo do YouTube.
3. Escolha o diretório de destino.
4. Clique no botão "Baixar" e aguarde a conclusão.





## Requisitos

- Python 3.x
- Biblioteca `pytube`
- Biblioteca `tkinter`

## Instalação

1. Certifique-se de ter o Python 3.x instalado em seu sistema.
2. Clone ou faça o download deste repositório.
3. Instale as dependências executando o seguinte comando: pip install -r requirements.txt


Observações: O erro indica que o tkinter ou ffmpeg não está instalado no seu sistema. O tkinter é um módulo padrão do Python, mas em algumas distribuições do Linux ele precisa ser instalado separadamente.

Solução:
Poder ser necessário instalar o tkinter, dependendo da sua distribuição do Linux:

Ubuntu/Debian:
sudo apt update
sudo apt install python3-tk ffmpeg

Fedora:
sudo dnf install python3-tkinter ffmpeg

Arch Linux
sudo pacman -S tk ffmpeg
Depois de instalar, tente novamente instalar os pacotes do seu projeto:

depois de instalado podem continuar com: pip install -r requirements.txt


