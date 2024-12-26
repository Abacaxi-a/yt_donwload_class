import yt_dlp as youtube_dl

url = 'Link_class_video'

#baixa utilizando parametros
# ydl_opts = {
#     'format': 'bestaudio/best',  # Melhor qualidade de áudio disponível
#     'postprocessors': [{
#         'key': 'FFmpegExtractAudio',
#         'preferredcodec': 'mp3',  # Formato de áudio desejado
#         'preferredquality': '192',  # Qualidade do áudio
#     }],
#     'outtmpl': '%(title)s.%(ext)s',  # Nome do arquivo de saída baseado no título do vídeo
# }


# mostra opções de formatos
# ydl_opts = {
#     'listformats': True, 
# }

#uitlizar as formatações com base no id 
ydl_opts = {
    'format': '233',
    'outtmpl': '%(title)s.%(ext)s'
}

# Baixar o vídeo
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("Download completo!")

