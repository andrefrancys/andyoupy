import tkinter as tk
from tkinter import messagebox, ttk, filedialog
from PIL import Image, ImageTk
import yt_dlp

def download_media():
    url = entry.get()
    save_directory = entry_directory.get()
    
    if not url or not save_directory:
        messagebox.showerror("Erro", "Por favor, insira uma URL e selecione um diretório de salvamento.")
        return
    
    try:
        ydl_opts = {
            'outtmpl': f'{save_directory}/%(title)s.%(ext)s',
            'progress_hooks': [progress_hook],
            'format': 'bestvideo+bestaudio/best'
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        messagebox.showinfo("Sucesso", "Download concluído com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", str(e))

def progress_hook(d):
    if d['status'] == 'downloading':
        downloaded = d.get('downloaded_bytes', 0)
        total = d.get('total_bytes', 1)
        percent = (downloaded / total) * 100
        progress_bar["value"] = percent
        window.update_idletasks()

def browse_directory():
    selected_directory = filedialog.askdirectory()
    entry_directory.delete(0, tk.END)
    entry_directory.insert(tk.END, selected_directory)

# Criando a janela principal
window = tk.Tk()
window.title("Baixar Vídeos do YouTube")
window.geometry("400x400")

# Carregando a imagem do logo
try:
    logo_image = Image.open("youtube-logo.png")
    logo_image = logo_image.resize((250, 80), Image.LANCZOS)
    logo_photo = ImageTk.PhotoImage(logo_image)
    logo_label = tk.Label(window, image=logo_photo)
    logo_label.pack()
except:
    pass

# Criando os widgets
label = tk.Label(window, text="URL:")
label.pack()
entry = tk.Entry(window, width=50)
entry.pack()

label_directory = tk.Label(window, text="Diretório de Salvamento:")
label_directory.pack()
entry_directory = tk.Entry(window, width=50)
entry_directory.pack()
button_browse = tk.Button(window, text="Procurar", command=browse_directory)
button_browse.pack()

progress_bar = ttk.Progressbar(window, length=300, mode="determinate")
progress_bar.pack(pady=10)
button = tk.Button(window, text="Baixar", command=download_media)
button.pack()

window.mainloop()
