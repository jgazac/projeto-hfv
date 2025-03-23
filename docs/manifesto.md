# Manifesto Técnico - Projeto HFV

## Visão Geral
Sistema para análise de imagens de partidas esportivas com interface interativa, reprodução de vídeos e estrutura modular para futura extração de dados e geração de relatórios.

---

## Estrutura de Diretórios

projeto-hfv/
├── .gitignore
├── Log_dev.txt
├── requirements.txt
├── README.md (sugerido futuramente)
├── docs/
│   └── manifesto.md     # Este documento
├── outros/              # Documentos auxiliares (ignorada pelo Git)
├── src/
│   ├── main.py          # Ponto de entrada da aplicação
│   ├── interface/
│   │   ├── ui.py            # Interface Tkinter e layout
│   │   └── video_player.py  # Lógica de reprodução de vídeo
│   ├── utils/
│   │   ├── arquivos.py      # Funções de seleção de arquivo
│   │   └── configuracoes.py # Obtenção da altura da taskbar
│   ├── analise/
│   │   ├── segmentador.py       # Controla o processo geral de análise
│   │   └── detector_cortes.py   # Lógica de detecção de cortes na sequência de vídeo
├── tests/                # Estrutura para testes futuros
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
- Integração com os módulos de análise

### utils/arquivos.py
- Função `selecionar_video()` para abrir caixa de diálogo de escolha de vídeo.

### utils/configuracoes.py
- Função `get_taskbar_height()` para detectar altura da barra de tarefas do Windows, garantindo interface visível.

### analise/segmentador.py
- Orquestra o processo de segmentação de trechos do vídeo a partir dos frames selecionados pelo usuário.
- Comunica-se com o detector de cortes e trata mensagens e atualizações na interface.

### analise/detector_cortes.py
- Realiza análise da continuidade visual entre frames consecutivos.
- Utiliza métrica SSIM para identificar mudanças abruptas (cortes de câmera ou replays).

---

## Funcionalidades Implementadas

- Interface Tkinter responsiva e maximizada
- Leitura e exibição de vídeo via OpenCV
- Barra de progresso com controle por slider (seek interativo)
- Contador de frames e tempo (min, seg, milisseg)
- Botões: play, pause, stop, marcar início e fim
- Exibição de informações do vídeo na barra lateral
- Processamento de segmentação acionado via botão "Processar"
- Detecção de cortes baseada em similaridade entre quadros (SSIM)
- Caixa de diálogo para feedback do usuário
- Atualização do status do processamento no painel lateral

---

## Diretrizes para as próximas etapas

- Expandir classificação dos trechos segmentados (ângulos, replays, contextos)
- Associar tipo de análise ao tipo de trecho (lateral, frontal, replay etc.)
- Aprimorar interface com filtros de visualização e status dos blocos segmentados
- Iniciar análises específicas por tipo de câmera (posição, ação, jogadores)
- Otimização futura com `multiprocessing` para paralelizar tarefas intensivas
- Avaliar implementação de “projeto salvo” para retomada sem retrabalho

---

## Dependências principais

- opencv-python
- pillow
- scikit-image

---

## Observações Finais

- Projeto segue diretrizes de praticidade, modularização e eficiência
- Todas as bibliotecas não nativas devem estar listadas no `requirements.txt`
- Projeto desenvolvido exclusivamente em ambiente Windows
- Registro de progresso contínuo mantido em `Log_dev.txt`

---