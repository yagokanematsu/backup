import tkinter as tk
import os
import shutil
import yt_dlp  # pip install yt_dlp
import subprocess  

COR_FUNDO = "#66d575"
COR_TEXTO = "black"
COR_BOTAO = "#057ed6"
COR_BOTAO_MOUSE = "#a5d6ff"

def estilizar_botao(botao):
    botao.config(bg=COR_BOTAO, fg=COR_TEXTO, font=("Arial", 12), relief="raised", bd=3)
    botao.bind("<Enter>", lambda x: botao.config(bg=COR_BOTAO_MOUSE))
    botao.bind("<Leave>", lambda x: botao.config(bg=COR_BOTAO))

def baixar_mp3():
    def download_mp3():
        link = url.get()
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])

    nova_janela = tk.Toplevel(aba, bg=COR_FUNDO)
    nova_janela.title("Baixar MP3")
    nova_janela.geometry("350x200")

    tk.Label(nova_janela, text="Digite a URL do vídeo:", bg=COR_FUNDO, fg=COR_TEXTO, font=("Arial", 12)).pack(pady=10)
    url = tk.Entry(nova_janela, width=40)
    url.pack(pady=5)

    botao_baixar = tk.Button(nova_janela, text="Baixar MP3", command=download_mp3)
    estilizar_botao(botao_baixar)
    botao_baixar.pack(pady=10)

    botao_fechar = tk.Button(nova_janela, text="Fechar", command=nova_janela.destroy)
    estilizar_botao(botao_fechar)
    botao_fechar.pack(pady=5)

def baixar_mp4():
    def download_mp4():
        link = url.get()
        
        with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
            info = ydl.extract_info(link, download=False)
            titulo = info.get('title', 'video')
        
        video_opts = {
            'format': 'bestvideo',
            'outtmpl': 'video.mp4'
        }
        audio_opts = {
            'format': 'bestaudio',
            'outtmpl': 'audio.mp3'
        }
        
        with yt_dlp.YoutubeDL(video_opts) as ydl:
            ydl.download([link])
        with yt_dlp.YoutubeDL(audio_opts) as ydl:
            ydl.download([link])
        
        nome_final = f"{titulo}.mp4"
        comando_ffmpeg = ["ffmpeg", "-i", "video.mp4", "-i", "audio.mp3", "-c:v", "copy", "-c:a", "aac", "-strict", "experimental", nome_final, "-y"]
        subprocess.run(comando_ffmpeg, shell=True)
        
        destino = f"C:\\Programas\\media"
        os.makedirs(destino, exist_ok=True)
        shutil.move(f'C:\\Programas\\{nome_final}', destino)
        
        os.remove("video.mp4")
        os.remove("audio.mp3")
    
    nova_janela = tk.Toplevel(aba, bg=COR_FUNDO)
    nova_janela.title("Baixar MP4")
    nova_janela.geometry("350x200")

    tk.Label(nova_janela, text="Digite a URL do vídeo:", bg=COR_FUNDO, fg=COR_TEXTO, font=("Arial", 12)).pack(pady=10)
    url = tk.Entry(nova_janela, width=40)
    url.pack(pady=5)

    botao_baixar = tk.Button(nova_janela, text="Baixar MP4", command=download_mp4)
    estilizar_botao(botao_baixar)
    botao_baixar.pack(pady=10)

    botao_fechar = tk.Button(nova_janela, text="Fechar", command=nova_janela.destroy)
    estilizar_botao(botao_fechar)
    botao_fechar.pack(pady=5)

aba = tk.Tk()
aba.title("YouTube Downloader")
aba.geometry("400x300")
aba.config(bg=COR_FUNDO)

a = tk.Label(aba, text="Baixe vídeos ou áudios do YouTube", bg=COR_FUNDO, fg=COR_TEXTO, font=("Arial", 14, "bold")).pack(pady=20)

botao1 = tk.Button(aba, text="Baixar MP3", command=baixar_mp3, width=20, height=2)
estilizar_botao(botao1)
botao1.pack(pady=10)

botao2 = tk.Button(aba, text="Baixar MP4", command=baixar_mp4, width=20, height=2)
estilizar_botao(botao2)
botao2.pack(pady=10)

botao3 = tk.Button(aba, text="Fechar", command=aba.destroy, width=20, height=2)
estilizar_botao(botao3)
botao3.pack(pady=10)

tk.mainloop()
