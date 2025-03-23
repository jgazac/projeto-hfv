import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim


def detectar_corte(frame1, frame2, config=None):
    """
    Detecta se houve um corte entre dois frames com base em SSIM e histograma HSV.
    """
    if config is None:
        config = {
            'ssim_strict': 0.5,
            'ssim_soft': 0.8,
            'hist_thresh': 0.3
        }

    # Redimensionar para acelerar o processamento
    frame1_resized = cv2.resize(frame1, (320, 180))
    frame2_resized = cv2.resize(frame2, (320, 180))

    # Converter para escala de cinza para SSIM
    gray1 = cv2.cvtColor(frame1_resized, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(frame2_resized, cv2.COLOR_BGR2GRAY)

    score, _ = ssim(gray1, gray2, full=True)

    if score < config['ssim_strict']:
        return True  # Corte duro

    if score < config['ssim_soft']:
        # Verifica histograma HSV como reforço
        hsv1 = cv2.cvtColor(frame1_resized, cv2.COLOR_BGR2HSV)
        hsv2 = cv2.cvtColor(frame2_resized, cv2.COLOR_BGR2HSV)

        hist1 = cv2.calcHist([hsv1], [0, 1], None, [50, 60], [0, 180, 0, 256])
        hist2 = cv2.calcHist([hsv2], [0, 1], None, [50, 60], [0, 180, 0, 256])

        cv2.normalize(hist1, hist1)
        cv2.normalize(hist2, hist2)

        diff = cv2.compareHist(hist1, hist2, cv2.HISTCMP_BHATTACHARYYA)

        if diff > config['hist_thresh']:
            return True  # Corte sutil confirmado

    return False
