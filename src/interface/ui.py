import tkinter as tk
from tkinter import ttk, messagebox
from .video_player import VideoPlayer
from utils.arquivos import selecionar_video
from utils.configuracoes import get_taskbar_height
from analise.segmentador import segmentar_video  # <- integração aqui


class VideoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Análise Esportiva")
        self.root.state("zoomed")
        self.root.update_idletasks()

        # Dimensões da tela
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height_total = self.root.winfo_screenheight()
        self.taskbar_height = get_taskbar_height()
        self.screen_height = self.screen_height_total - self.taskbar_height

        self.sidebar_width = int(self.screen_width * 0.2)
        self.bottom_bar_height = int(self.screen_height * 0.1)
        self.video_width = self.screen_width - self.sidebar_width
        self.video_height = self.screen_height - self.bottom_bar_height

        self.video_player = VideoPlayer(self)

        self._configure_sidebar()
        self._configure_video_display()
        self._configure_bottom_bar()

    def _configure_sidebar(self):
        self.sidebar = tk.Frame(self.root, width=self.sidebar_width, height=self.screen_height, bg="#333333", relief="ridge", bd=4)
        self.sidebar.place(x=0, y=0)

        top_container_height = int(self.screen_height * 0.4)
        bottom_container_height = self.screen_height - top_container_height

        self.info_frame = tk.Frame(self.sidebar, bg="#444444", height=top_container_height, relief="ridge", bd=3)
        self.info_frame.place(x=0, y=0, width=self.sidebar_width, height=top_container_height)

        self.controls_frame = tk.Frame(self.sidebar, bg="#555555", height=bottom_container_height, relief="ridge", bd=3)
        self.controls_frame.place(x=0, y=top_container_height, width=self.sidebar_width, height=bottom_container_height)

        self.label_nome = tk.Label(self.info_frame, text="Arquivo: ", fg="white", bg="#444444", font=("Arial", 9, "bold"), anchor="w")
        self.label_nome.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.info_nome = tk.Label(self.info_frame, text="---", fg="white", bg="#444444", font=("Arial", 9), anchor="w")
        self.info_nome.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        self.label_tempo = tk.Label(self.info_frame, text="Duração: ", fg="white", bg="#444444", font=("Arial", 9, "bold"), anchor="w")
        self.label_tempo.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.info_tempo = tk.Label(self.info_frame, text="00:00", fg="white", bg="#444444", font=("Arial", 9), anchor="w")
        self.info_tempo.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        self.label_status = tk.Label(self.info_frame, text="Status: ", fg="white", bg="#444444", font=("Arial", 9, "bold"), anchor="w")
        self.label_status.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.info_status = tk.Label(self.info_frame, text="Pré-processamento", fg="cyan", bg="#444444", font=("Arial", 9, "bold"), anchor="w")
        self.info_status.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        self.label_inicio = tk.Label(self.info_frame, text="Início: ", fg="white", bg="#444444", font=("Arial", 9, "bold"), anchor="w")
        self.label_inicio.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.info_inicio = tk.Label(self.info_frame, text="000000 | 00:00.000", fg="white", bg="#444444", font=("Arial", 9), anchor="w")
        self.info_inicio.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        self.label_fim = tk.Label(self.info_frame, text="Fim: ", fg="white", bg="#444444", font=("Arial", 9, "bold"), anchor="w")
        self.label_fim.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.info_fim = tk.Label(self.info_frame, text="000000 | 00:00.000", fg="white", bg="#444444", font=("Arial", 9), anchor="w")
        self.info_fim.grid(row=4, column=1, padx=5, pady=5, sticky="w")

        self.load_button = ttk.Button(self.controls_frame, text="Carregar Vídeo", command=self.load_video)
        self.load_button.pack(pady=10, padx=10, fill=tk.X)

        self.process_button = ttk.Button(self.controls_frame, text="Processar", command=self.process_video)
        self.process_button.pack(pady=10, padx=10, fill=tk.X)

        self.report_button = ttk.Button(self.controls_frame, text="Gerar Relatório", command=self.generate_report)
        self.report_button.pack(pady=10, padx=10, fill=tk.X)

    def _configure_video_display(self):
        self.video_frame = tk.Label(self.root, bg="#1a1a1a", relief="solid", bd=2)
        self.video_frame.place(x=self.sidebar_width, y=0, width=self.video_width, height=self.video_height)

    def _configure_bottom_bar(self):
        self.bottom_bar = tk.Frame(self.root, bg="#222222", height=self.bottom_bar_height, relief="ridge", bd=3)
        self.bottom_bar.place(x=self.sidebar_width, y=self.video_height, width=self.video_width, height=self.bottom_bar_height)

        button_padding_y = int(self.bottom_bar_height * 0.2)

        self.play_button = ttk.Button(self.bottom_bar, text="▶ Play", command=self.video_player.play_video)
        self.play_button.place(x=20, y=button_padding_y, width=80, height=30)

        self.pause_button = ttk.Button(self.bottom_bar, text="⏸ Pause", command=self.video_player.pause_video)
        self.pause_button.place(x=120, y=button_padding_y, width=80, height=30)

        self.stop_button = ttk.Button(self.bottom_bar, text="⏹ Stop", command=self.video_player.stop_video)
        self.stop_button.place(x=220, y=button_padding_y, width=80, height=30)

        self.mark_start_button = ttk.Button(self.bottom_bar, text="'I'", command=self.video_player.marcar_inicio)
        self.mark_start_button.place(x=320, y=button_padding_y, width=30, height=30)

        self.mark_end_button = ttk.Button(self.bottom_bar, text="'F'", command=self.video_player.marcar_fim)
        self.mark_end_button.place(x=370, y=button_padding_y, width=30, height=30)

        self.progress_container = tk.Frame(self.bottom_bar, bg="#222222")
        self.progress_container.place(x=420, y=button_padding_y)

        self.counter_container = tk.Frame(self.progress_container, bg="#222222")
        self.counter_container.pack(side="right", padx=(10, 0))

        self.frame_count_label = tk.Label(self.counter_container, text="000000/000000", fg="white", bg="#222222", font=("Consolas", 9))
        self.frame_count_label.pack(anchor="w")

        self.time_count_label = tk.Label(self.counter_container, text="00:00.000/00:00.000", fg="white", bg="#222222", font=("Consolas", 8))
        self.time_count_label.pack(anchor="w")

        self.progress_slider = tk.Scale(
            self.progress_container,
            from_=0,
            to=100,
            orient="horizontal",
            length=400,
            showvalue=0,
            sliderlength=10,
            resolution=1,
            bg="#222222",
            troughcolor="#444444",
            highlightthickness=0
        )
        self.progress_slider.bind("<ButtonPress-1>", self.video_player.iniciar_slider_interativo)
        self.progress_slider.bind("<ButtonRelease-1>", self.video_player.finalizar_seek)
        self.progress_slider.bind("<B1-Motion>", self.video_player.adiar_seek)
        self.progress_slider.pack(side="left", padx=10)

    def load_video(self):
        video_path = selecionar_video()
        if video_path:
            self.video_player.load_video(video_path)
            self.atualizar_info_video(video_path)

    def atualizar_info_video(self, video_path):
        from os.path import basename, splitext

        nome_arquivo = splitext(basename(video_path))[0]
        duracao_video = self.video_player.get_video_duration()

        self.info_nome.config(text=nome_arquivo)
        self.info_tempo.config(text=duracao_video)
        self.info_status.config(text="Pré-processamento")
        inicio_txt, fim_txt = self.video_player.get_marcas_padrao()
        self.info_inicio.config(text=inicio_txt)
        self.info_fim.config(text=fim_txt)

    def process_video(self):
        """Processa o vídeo via módulo de segmentação"""
        try:
            if not self.video_player.caminho_video:
                messagebox.showwarning("Atenção", "Nenhum vídeo carregado.")
                return

            self.info_status.config(text="Segmentando vídeo...", fg="orange")
            self.root.update_idletasks()

            caminho = self.video_player.caminho_video
            segmentar_video(caminho, self.video_player.frame_inicio, self.video_player.frame_fim)


            self.info_status.config(text="Processado", fg="green")
            messagebox.showinfo("Concluído", "Segmentação finalizada com sucesso.")
        except Exception as e:
            self.info_status.config(text="Erro no processamento", fg="red")
            messagebox.showerror("Erro", f"Erro ao processar vídeo:\n{str(e)}")

    def generate_report(self):
        self.info_status.config(text="Exportado")
        print("Gerando relatório...")
