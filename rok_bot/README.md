# Bot Rise of Kingdoms (RoK-Bot)

Este é um bot autônomo de alta performance desenvolvido em Python para o jogo Rise of Kingdoms.

## Funcionalidades
- **Coleta Automática**: Gerencia todas as marchas para coletar recursos e gemas.
- **Fortes Bárbaros**: Realiza ralis de fortes bárbaros continuamente enquanto houver AP.
- **Gestão de AP**: Quando o AP acaba, a marcha de rali é convertida para coleta. Quando o AP recupera, uma marcha é recolhida para voltar aos fortes.
- **Exploração**: Envia batedores para névoa e explora cavernas/aldeias.
- **Defesa (Escudo)**: Detecta ataques iminentes e ativa o escudo de paz automaticamente.
- **Gestão da Cidade**: Evolui construções e treina tropas sem parar.

## Pré-requisitos
1. **Python 3.10+** instalado.
2. **ADB (Android Debug Bridge)** instalado e no PATH do sistema.
3. **Emulador Android** (BlueStacks, LDPlayer, MSI App Player) configurado com "Depuração USB" ativa.
4. **Resolução**: Recomendado 1280x720 ou 1920x1080.

## Instalação
1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

2. Certifique-se de que o ADB reconhece seu emulador:
   ```bash
   adb devices
   ```

3. Execute o bot:
   ```bash
   python main.py
   ```

## Configuração de Ativos (Assets)
O bot utiliza reconhecimento de imagem. Você deve colocar prints dos botões do jogo na pasta `assets/` seguindo os nomes esperados pelo código:
- `red_screen_indicator.png`: O alerta vermelho de ataque.
- `search_button.png`: Botão de lupa para buscar recursos.
- `march_button.png`: Botão de enviar marcha.
- (Adicione outros conforme as tarefas forem refinadas).

## Estrutura do Projeto
- `core/`: Motores de visão e comunicação ADB.
- `tasks/`: Lógica específica para cada atividade (coleta, combate, etc).
- `assets/`: Templates de imagem para reconhecimento.
