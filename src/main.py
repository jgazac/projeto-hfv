from tkinter import Tk
from interface.ui import VideoApp

if __name__ == "__main__":
    root = Tk()
    app = VideoApp(root)
    root.mainloop()


# import tkinter as tk
# from tkinter import ttk, filedialog
# import cv2
# from PIL import Image, ImageTk
# import pyautogui

# def get_taskbar_height():
#     """ Obtém a altura da barra de tarefas do Windows de forma precisa usando pyautogui """
#     try:
#         screen_width, screen_height = pyautogui.size()  # Obtém a resolução total da tela
#         _, work_area_y = pyautogui.position()  # Obtém a posição do cursor (topo da barra de tarefas)

#         taskbar_height = screen_height - work_area_y
#         if taskbar_height > 0:
#             return taskbar_height
#     except Exception:
#         pass  # Se falhar, usa o fallback

#     return 40  # Fallback para altura padrão da barra de tarefas

# class VideoApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Análise Esportiva")

#         # Maximiza a janela sem esconder a barra de título e a barra de tarefas
#         self.root.state("zoomed")
#         self.root.update_idletasks()

#         # Obtém dimensões da tela
#         screen_width = self.root.winfo_screenwidth()
#         screen_height_total = self.root.winfo_screenheight()  # Altura total da tela
#         taskbar_height = get_taskbar_height()  # Obtém a altura exata da barra de tarefas

#         # Ajuste da altura útil da interface
#         adjusted_height = screen_height_total - taskbar_height

#         # Definição de proporções fixas
#         sidebar_width = int(screen_width * 0.2)  # 1/5 da largura total
#         sidebar_height = adjusted_height  # Toda a altura disponível
#         top_container_height = int(sidebar_height * 0.4)  # Agora ocupa o dobro do tamanho anterior (40% da barra lateral)
#         bottom_container_height = sidebar_height - top_container_height  # Restante da altura disponível

#         bottom_bar_height = int(adjusted_height * 0.1)  # 1/10 da altura disponível
#         video_width = screen_width - sidebar_width  # Largura da tela de vídeo
#         video_height = adjusted_height - bottom_bar_height  # Altura da tela de vídeo

#         # Painel lateral fixo (Cinza Escuro)
#         self.sidebar = tk.Frame(self.root, width=sidebar_width, height=sidebar_height, bg="#333333", relief="ridge", bd=4)
#         self.sidebar.place(x=0, y=0, width=sidebar_width, height=sidebar_height)

#         # Container superior para informações (Cinza Médio) - Agora ocupa 40% da altura da barra lateral
#         self.info_frame = tk.Frame(self.sidebar, bg="#444444", height=top_container_height, relief="ridge", bd=3)
#         self.info_frame.place(x=0, y=0, width=sidebar_width, height=top_container_height)

#         self.info_label = tk.Label(self.info_frame, text="Informações do Vídeo", fg="white", bg="#444444", font=("Arial", 12, "bold"))
#         self.info_label.pack(pady=10)

#         # Container inferior para botões (Cinza Médio) - Agora ocupa o espaço restante (60%)
#         self.controls_frame = tk.Frame(self.sidebar, bg="#555555", height=bottom_container_height, relief="ridge", bd=3)
#         self.controls_frame.place(x=0, y=top_container_height, width=sidebar_width, height=bottom_container_height)

#         # Botões dentro do container de controles
#         self.load_button = ttk.Button(self.controls_frame, text="Carregar Vídeo", command=self.load_video)
#         self.load_button.pack(pady=10, padx=10, fill=tk.X)

#         self.process_button = ttk.Button(self.controls_frame, text="Processar", command=self.process_video)
#         self.process_button.pack(pady=10, padx=10, fill=tk.X)

#         self.report_button = ttk.Button(self.controls_frame, text="Gerar Relatório", command=self.generate_report)
#         self.report_button.pack(pady=10, padx=10, fill=tk.X)

#         # Frame principal do vídeo (Preto)
#         self.video_frame = tk.Label(self.root, bg="#1a1a1a", relief="solid", bd=2)
#         self.video_frame.place(x=sidebar_width, y=0, width=video_width, height=video_height)

#         # Barra inferior (Agora sempre 100% visível)
#         self.bottom_bar = tk.Frame(self.root, bg="#222222", height=bottom_bar_height, relief="ridge", bd=3)
#         self.bottom_bar.place(x=sidebar_width, y=video_height, width=video_width, height=bottom_bar_height)

#         # Ajuste dos botões para não ficarem colados na borda inferior
#         button_padding_y = int(bottom_bar_height * 0.2)  # Ajusta dinamicamente o padding vertical

#         # Botões de controle de vídeo na barra inferior
#         self.play_button = ttk.Button(self.bottom_bar, text="▶ Play", command=self.play_video)
#         self.play_button.place(x=20, y=button_padding_y, width=80, height=30)

#         self.pause_button = ttk.Button(self.bottom_bar, text="⏸ Pause", command=self.pause_video)
#         self.pause_button.place(x=120, y=button_padding_y, width=80, height=30)

#         self.stop_button = ttk.Button(self.bottom_bar, text="⏹ Stop", command=self.stop_video)
#         self.stop_button.place(x=220, y=button_padding_y, width=80, height=30)

#         # Variáveis do vídeo
#         self.cap = None
#         self.video_path = None
#         self.is_playing = False

#     def load_video(self):
#         """ Abre a caixa de diálogo para selecionar um arquivo de vídeo """
#         self.video_path = filedialog.askopenfilename(filetypes=[("Arquivos de Vídeo", "*.mp4;*.avi;*.mov;*.mkv")])
#         if self.video_path:
#             self.cap = cv2.VideoCapture(self.video_path)
#             self.info_label.config(text=f"Arquivo: {self.video_path.split('/')[-1]}")
#             self.update_frame()

#     def process_video(self):
#         """ Método placeholder para processamento de vídeo """
#         print("Processamento iniciado...")

#     def generate_report(self):
#         """ Método placeholder para geração de relatório """
#         print("Gerando relatório...")

#     def update_frame(self):
#         """ Atualiza os frames do vídeo na tela """
#         if self.cap and self.is_playing:
#             ret, frame = self.cap.read()
#             if ret:
#                 frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#                 frame = cv2.resize(frame, (self.root.winfo_screenwidth() - int(self.root.winfo_screenwidth() * 0.2), self.root.winfo_screenheight() - int(self.root.winfo_screenheight() * 0.1)))
#                 img = ImageTk.PhotoImage(Image.fromarray(frame))
#                 self.video_frame.config(image=img)
#                 self.video_frame.image = img
#                 self.root.after(10, self.update_frame)  # Atualiza a cada 10ms
#             else:
#                 self.stop_video()  # Para o vídeo ao chegar no fim

#     def play_video(self):
#         """ Inicia a reprodução do vídeo """
#         if self.cap:
#             self.is_playing = True
#             self.update_frame()

#     def pause_video(self):
#         """ Pausa o vídeo """
#         self.is_playing = False

#     def stop_video(self):
#         """ Para o vídeo e reseta para o início """
#         if self.cap:
#             self.is_playing = False
#             self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = VideoApp(root)
#     root.mainloop()
