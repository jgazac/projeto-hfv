# Manifesto Técnico - Projeto HFV

## Visão Geral
Sistema para análise de imagens de partidas esportivas com interface interativa, reprodução de vídeos e estrutura modular para futura extração de dados e geração de relatórios.

---

## Estrutura de Diretórios

projeto-hfv/
├── .gitignore
├── Log_dev.txt
├── README.md (sugerido futuramente)
├── outros/                # Documentos auxiliares (ignorada pelo Git)
├── src/
│   ├── main.py           # Ponto de entrada da aplicação
│   ├── interface/
│   │   ├── ui.py         # Interface Tkinter e layout
│   │   └── video_player.py # Lógica de reprodução de vídeo
│   ├── utils/
│   │   ├── arquivos.py   # Funções de seleção de arquivo
│   │   └── configuracoes.py # Obtenção da altura da taskbar
│
├── venv/                 # Ambiente virtual (ignorado pelo Git)


---

## Descrição dos Módulos

### main.py
- Inicializa a aplicação e cria a instância da interface principal (`VideoApp`).

### interface/ui.py
- Define a janela principal com layout dividido em:
  - **Barra lateral (esquerda)**: informações do vídeo e botões de ação
  - **Tela de vídeo**: área principal de exibição
  - **Barra inferior**: botões de controle e barra de progresso com contador
- Atualiza dinamicamente os elementos da interface com base nas interações do usuário

### interface/video_player.py
- Reproduz vídeo usando OpenCV
- Controle de execução (play, pause, stop)
- Atualização de frames e sincronia com barra de progresso
- Suporte a marcação de início/fim do trecho de análise
- Controle de delay e travamento do slider

### utils/arquivos.py
- Função `selecionar_video()` para abrir caixa de diálogo de escolha de vídeo.

### utils/configuracoes.py
- Função `get_taskbar_height()` para detectar altura da barra de tarefas do Windows, garantindo interface visível.

---

## Funcionalidades Implementadas

- Interface Tkinter responsiva e maximizada
- Leitura e exibição de vídeo via OpenCV
- Barra de progresso com controle por slider (seek interativo)
- Contador de frames e tempo (min, seg, milisseg)
- Botões: play, pause, stop, marcar início e fim
- Exibição de informações do vídeo na barra lateral

---

## Diretrizes para as próximas etapas

- Iniciar análise frame a frame (continuidade de imagem)
- Identificação de ângulos de filmagem com base em padrões visuais
- Modularizar futuras análises (por objeto, movimento, evento)
- Otimização com `multiprocessing` para análises pesadas
- Expansão do painel de informações e funcionalidades de relatório

---

## Observações Finais

- Projeto segue diretrizes de praticidade, modularização e eficiência
- Todas as bibliotecas não nativas devem estar listadas no `requirements.txt`
- Projeto desenvolvido exclusivamente em ambiente Windows
- Registro de progresso contínuo mantido em `Log_dev.txt`
