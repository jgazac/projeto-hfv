from tkinter import filedialog

def selecionar_video():
    """ Abre a caixa de diálogo para selecionar um arquivo de vídeo e retorna o caminho do arquivo """
    video_path = filedialog.askopenfilename(filetypes=[("Arquivos de Vídeo", "*.mp4;*.avi;*.mov;*.mkv")])
    return video_path if video_path else None
