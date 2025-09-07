# Não testei no windows, uso linux!!
<img width="268" height="203" alt="image" src="https://github.com/user-attachments/assets/122b2535-645d-4226-9526-792b53749968" />
Autor da pixel art original: (finaldemo)(https://imgur.com/gallery/awesome-dark-souls-pixel-art-moUGC)

# Características

- Interface visual com GIF animado do knight (100x100px) e balão de fala (220x140px)
- Ativação/desativação com Ctrl+Alt+Shift+S
- Aparece automaticamente a cada 5 minutos por 15 segundos
- Posicionamento no canto inferior esquerdo da tela
- Fundo transparente
- Sistema de dicas facilmente personalizável
- Layout vertical: balão de fala acima do knightBuddy - Amigo Virtual para Kali Linux

Um assistente virtual inspirado em Dark Souls que aparece na tela com dicas personalizadas de segurança e programação.

## Instalação

1. **Instalar dependências:**
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip python3-tk
   pip3 install --user pillow pynput
   ```

## Como usar

1. **Executar o programa:**
   ```bash
   python3 dark_souls_buddy.py
   ```

2. **Controles:**
   - **Ctrl+Alt+Shift+S**: Mostrar/esconder o buddy manualmente
   - O buddy aparece automaticamente a cada 5 minutos
   - Fica visível por 15 segundos e depois desaparece

## Personalização

### Adicionar suas próprias dicas

Edite o arquivo `config.py` e adicione suas dicas na lista `TIPS`:

```python
TIPS = [
    "Sua dica personalizada aqui!",
    "Outra dica interessante.",
    "Mais uma dica útil.",
    # Adicione quantas quiser...
]
```

### Configurações disponíveis

No arquivo `config.py` você pode alterar:

- **TIP_DURATION**: Tempo que a dica fica visível (segundos)
- **AUTO_INTERVAL**: Intervalo entre dicas automáticas (segundos)
- **WINDOW_TRANSPARENCY**: Transparência da janela (0.0 a 1.0)
- **BALLOON_WIDTH/HEIGHT**: Tamanho do balão de fala
- **KNIGHT_SIZE**: Tamanho do GIF do knight
- **TEXT_WRAP_WIDTH**: Número de caracteres por linha

### Exemplo de personalização:

```python
# Mostrar dicas a cada 10 minutos por 30 segundos
TIP_DURATION = 30
AUTO_INTERVAL = 600  # 10 minutos

# Janela mais transparente
WINDOW_TRANSPARENCY = 0.7

# Balão maior
BALLOON_WIDTH = 400
BALLOON_HEIGHT = 250
```

## Estrutura dos arquivos

```
DarkSoulsBuddy/
├── dark_souls_buddy.py      # Código principal
├── config.py                # Configurações e dicas
├── install_dependencies.sh  # Script de instalação
├── KnightBuddy.gif         # GIF animado do knight
├── balaoFala.png           # Imagem do balão de fala
└── README.md               # Este arquivo
```

## Funcionalidades técnicas

### Sistema de dicas
- Lista configurável de dicas em `config.py`
- Seleção aleatória das dicas
- Método `add_tip()` para adicionar dicas programaticamente
- Método `remove_tip()` para remover dicas

### Interface visual
- Janela transparente sempre no topo
- Posicionamento automático no canto inferior esquerdo
- Animação do GIF do knight
- Texto sobreposto ao balão de fala com quebra automática
- Texto não ultrapassa as bordas do balão

### Sistema de timing
- Timer automático configurável
- Duração de exibição configurável
- Thread separada para não bloquear o sistema
- Sistema de toggle manual

### Detecção de teclas
- Listener global para Ctrl+Alt+S
- Funciona mesmo quando a janela não está em foco
- Thread separada para não interferir na interface

## Solução de problemas

### O buddy não aparece
1. Verifique se as imagens estão na pasta correta
2. Verifique se as dependências estão instaladas
3. Execute no terminal para ver mensagens de erro

### Ctrl+Alt+S não funciona
1. Verifique se o programa tem permissões adequadas
2. Alguns ambientes desktop podem interceptar essa combinação
3. Verifique se não há conflito com outras aplicações

### Problemas de performance
1. Reduza o tamanho das imagens em `config.py`
2. Aumente o intervalo entre dicas automáticas
3. Reduza a transparência da janela

## Personalização avançada

### Modificar o comportamento
Você pode estender a classe `DarkSoulsBuddy` para adicionar funcionalidades:

```python
class CustomBuddy(DarkSoulsBuddy):
    def __init__(self):
        super().__init__()
        # Suas modificações aqui
    
    def custom_tip_logic(self):
        # Lógica personalizada para dicas
        pass
```

### Adicionar novos tipos de dicas
```python
# Dicas baseadas em contexto
def add_contextual_tip(self, context):
    if context == "programming":
        tip = "Lembre-se de comentar seu código!"
    elif context == "security":
        tip = "Verifique logs de segurança regularmente!"
    
    self.show_tip(tip)
```

## Licença

Este projeto é de código aberto. Sinta-se livre para modificar e distribuir.

## Contribuições

Contribuições são bem-vindas! Algumas ideias:
- Novos temas visuais
- Mais opções de configuração
- Integração com outras ferramentas
- Dicas contextuais baseadas no que está sendo executado
- Sistema de notificações mais avançado

---

**Enjoy your Dark Souls Buddy! ⚔️**
