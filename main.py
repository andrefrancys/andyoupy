import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
from pytube import Playlist, YouTube

def download_media():
    url = entry.get()
    save_directory = entry_directory.get()
    
    try:
        if download_option.get() == "Lista de Reprodução":
            playlist = Playlist(url)
            
            total_videos = len(playlist.video_urls)
            progress_bar["maximum"] = total_videos
            
            for index, video in enumerate(playlist.videos, start=1):
                video.streams.get_highest_resolution().download(output_path=save_directory)
                progress_bar["value"] = index
                window.update_idletasks()
            
            messagebox.showinfo("Sucesso", "Download da lista de reprodução concluído com sucesso!")
        elif download_option.get() == "Vídeo":
            video = YouTube(url)
            video.streams.get_highest_resolution().download(output_path=save_directory)
            
            messagebox.showinfo("Sucesso", "Download do vídeo concluído com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", str(e))

def browse_directory():
    selected_directory = filedialog.askdirectory()
    entry_directory.delete(0, tk.END)
    entry_directory.insert(tk.END, selected_directory)

# Criação da janela
window = tk.Tk()
window.title("Baixar Videos")
window.geometry("400x400")

# Carregamento da imagem de logo
logo_image = Image.open("youtube-logo.png")
logo_image = logo_image.resize((250, 80), Image.LANCZOS)
logo_photo = ImageTk.PhotoImage(logo_image)

# Criação do título
title_label = tk.Label(window, text="Download vídeo Youtube", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Exibição da imagem de logo
logo_label = tk.Label(window, image=logo_photo)
logo_label.pack()

# Criação do campo de entrada de URL
label = tk.Label(window, text="URL:")
label.pack()

entry = tk.Entry(window, width=50)
entry.pack()

# Criação do campo de seleção de download
label_option = tk.Label(window, text="Opção de Download:")
label_option.pack()

download_options = ["Lista de Reprodução", "Vídeo"]
download_option = tk.StringVar(window)
download_option.set(download_options[0])

combobox = ttk.Combobox(window, values=download_options, textvariable=download_option, state="readonly")
combobox.pack()

# Criação do campo de diretório de salvamento
label_directory = tk.Label(window, text="Diretório de Salvamento:")
label_directory.pack()

entry_directory = tk.Entry(window, width=50)
entry_directory.pack()

button_browse = tk.Button(window, text="Procurar", command=browse_directory)
button_browse.pack()

# Criação da barra de progresso
progress_bar = ttk.Progressbar(window, length=300, mode="determinate")
progress_bar.pack(pady=10)

# Criação do botão de download
button = tk.Button(window, text="Baixar", command=download_media)
button.pack()

# Iniciar a interface gráfica
window.mainloop()
