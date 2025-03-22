import pyautogui

def get_taskbar_height():
    """ Obtém a altura da barra de tarefas do Windows de forma precisa usando pyautogui """
    try:
        screen_width, screen_height = pyautogui.size()  # Obtém a resolução total da tela
        _, work_area_y = pyautogui.position()  # Obtém a posição real do cursor na área de trabalho

        taskbar_height = screen_height - work_area_y
        if taskbar_height > 0:
            return taskbar_height
    except Exception:
        pass  # Se falhar, retorna um valor padrão seguro

    return 40  # Fallback para altura média da barra de tarefas
