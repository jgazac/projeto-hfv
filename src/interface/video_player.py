import cv2
from PIL import Image, ImageTk

class VideoPlayer:
    def __init__(self, app):
        self.app = app
        self.cap = None
        self.is_playing = False
        self.seek_after_id = None
        self.slider_delay_ms = 1500
        self.slider_locked = False  # flag para ignorar update automático


    def load_video(self, path):
        """ Carrega um vídeo e atualiza as informações na interface """
        self.cap = cv2.VideoCapture(path)

        # Atualiza a interface corretamente
        from os.path import basename, splitext

        nome_arquivo = splitext(basename(path))[0]  # Remove caminho e extensão
        duracao_video = self.get_video_duration()  # Obtém tempo do vídeo

        self.app.info_nome.config(text=nome_arquivo)
        self.app.info_tempo.config(text=duracao_video)
        self.app.info_status.config(text="Pré-processamento")  # Status inicial

        # Prepara o Slider de progresso
        total_frames = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
        self.app.progress_slider.config(to=total_frames)
        self.app.progress_slider.set(0)
        self.app.frame_count_label.config(text=f"000000/{total_frames:06}")

    def update_frame(self):
        """ Atualiza os frames do vídeo na tela e no slider de progresso """
        if self.cap and self.is_playing:
            ret, frame = self.cap.read()
            if ret:
                current_frame = int(self.cap.get(cv2.CAP_PROP_POS_FRAMES))
                total_frames = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))

                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame = cv2.resize(frame, (self.app.video_width, self.app.video_height))
                img = ImageTk.PhotoImage(Image.fromarray(frame))

                self.app.video_frame.config(image=img)
                self.app.video_frame.image = img

                # Somente atualiza o slider se não estiver sendo usado manualmente
                if not self.slider_locked:
                    self.updating_slider = True
                    self.app.progress_slider.set(current_frame)
                    self.updating_slider = False

                self.app.frame_count_label.config(text=f"{current_frame:06}/{total_frames:06}")
                self.app.time_count_label.config(
                text=f"{self.frame_para_tempo(current_frame)}/{self.frame_para_tempo(total_frames)}"
                )
                self.app.root.after(10, self.update_frame)
            else:
                self.stop_video()


    def play_video(self):
        """ Inicia a reprodução do vídeo """
        if self.cap:
            self.is_playing = True
            self.update_frame()

    def pause_video(self):
        """ Pausa o vídeo """
        self.is_playing = False

    def stop_video(self):
        """ Para o vídeo """
        if self.cap:
            self.is_playing = False
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    def get_video_duration(self):
        """ Retorna a duração do vídeo formatada como MM:SS """
        if self.cap:
            fps = self.cap.get(cv2.CAP_PROP_FPS)
            frame_count = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
            total_seconds = int(frame_count / fps) if fps > 0 else 0
            minutes, seconds = divmod(total_seconds, 60)
            return f"{minutes:02}:{seconds:02}"
        return "00:00"
    
    def adiar_seek(self, event=None):
        """ Redefine o temporizador de atualização do frame durante movimento do slider """
        if self.seek_after_id:
            self.app.root.after_cancel(self.seek_after_id)
        self.seek_after_id = self.app.root.after(self.slider_delay_ms, self.executar_seek)

    def finalizar_seek(self, event=None):
        """ Força a execução imediata se o botão do mouse for solto """
        if self.seek_after_id:
            self.app.root.after_cancel(self.seek_after_id)
        self.slider_locked = False
        self.executar_seek()

    def iniciar_slider_interativo(self, event=None):
        """ Informa ao sistema que o usuário está movendo manualmente o slider """
        self.slider_locked = True

    def executar_seek(self):
        """ Move o frame do vídeo para a posição do slider após delay """
        try:
            new_frame = int(self.app.progress_slider.get())
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, new_frame)

            if not self.is_playing:
                # Atualiza frame se estiver pausado
                ret, frame = self.cap.read()
                if ret:
                    self.cap.set(cv2.CAP_PROP_POS_FRAMES, new_frame)
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    frame = cv2.resize(frame, (self.app.video_width, self.app.video_height))
                    img = ImageTk.PhotoImage(Image.fromarray(frame))
                    self.app.video_frame.config(image=img)
                    self.app.video_frame.image = img

            total = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
            self.app.frame_count_label.config(text=f"{new_frame:06}/{total:06}")
        except:
            pass

    def get_marcas_padrao(self):
        """ Retorna as strings iniciais para os pontos de início e fim padrão """
        total_frames = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
        tempo_total = self.frame_para_tempo(total_frames)
        return ("000000 | 00:00.000", f"{total_frames:06} | {tempo_total}")
    
    def frame_para_tempo(self, frame):
        fps = self.cap.get(cv2.CAP_PROP_FPS)
        ms = int((frame / fps) * 1000)
        m, s = divmod(ms // 1000, 60)
        return f"{m:02}:{s:02}.{ms % 1000:03}"

    def marcar_inicio(self):
        frame = int(self.cap.get(cv2.CAP_PROP_POS_FRAMES))
        tempo = self.frame_para_tempo(frame)
        self.app.info_inicio.config(text=f"{frame:06} | {tempo}")

    def marcar_fim(self):
        frame = int(self.cap.get(cv2.CAP_PROP_POS_FRAMES))
        tempo = self.frame_para_tempo(frame)
        self.app.info_fim.config(text=f"{frame:06} | {tempo}")



