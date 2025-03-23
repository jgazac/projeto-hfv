import cv2
import numpy as np
from .detector_cortes import detectar_corte


def segmentar_video(video_path, frame_inicio, frame_fim, callback_status=None):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise IOError("Não foi possível abrir o vídeo.")

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_fim = min(frame_fim, total_frames - 1)
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_inicio)

    segmentos = []
    ultimo_frame_idx = frame_inicio
    tipo_temporario = "desconhecido"

    _, frame_anterior = cap.read()
    if frame_anterior is None:
        raise ValueError("Frame inicial inválido.")

    for i in range(frame_inicio + 1, frame_fim + 1):
        ret, frame_atual = cap.read()
        if not ret:
            break

        if callback_status and i % 10 == 0:
            callback_status(f"Analisando frame {i}/{frame_fim}")

        corte = detectar_corte(frame_anterior, frame_atual)

        if corte:
            segmentos.append({
                'inicio': ultimo_frame_idx,
                'fim': i - 1,
                'tipo': tipo_temporario
            })
            ultimo_frame_idx = i
            tipo_temporario = "desconhecido"

        frame_anterior = frame_atual

    # Salva o último segmento restante
    if ultimo_frame_idx <= frame_fim:
        segmentos.append({
            'inicio': ultimo_frame_idx,
            'fim': frame_fim,
            'tipo': tipo_temporario
        })

    cap.release()
    return segmentos
