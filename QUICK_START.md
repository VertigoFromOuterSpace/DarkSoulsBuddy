# INSTRUÇÕES RÁPIDAS - Dark Souls Buddy

## 🚀 EXECUÇÃO RÁPIDA

1. **Instalar dependências (cria ambiente virtual automaticamente):**
   ```bash
   ./install_dependencies.sh
   ```

2. **Executar o buddy:**
   ```bash
   ./run_buddy.sh
   ```
   ou diretamente:
   ```bash
   .venv/bin/python dark_souls_buddy.py
   ```

## ⌨️ CONTROLES

- **Ctrl + Alt + Shift + S**: Mostrar/esconder buddy manualmente
- **Automático**: Aparece a cada 5 minutos por 15 segundos

## 🛠️ PERSONALIZAÇÃO RÁPIDA

1. **Configurar interativamente:**
   ```bash
   python3 configure.py
   ```

2. **Editar dicas manualmente:**
   Edite o arquivo `config.py` e modifique a lista `TIPS`

3. **Usar dicas de exemplo:**
   Veja `example_tips.py` para ideias de dicas

## 📁 ARQUIVOS IMPORTANTES

- `dark_souls_buddy.py` - Código principal
- `config.py` - Configurações e dicas
- `KnightBuddy.gif` - Animação do knight
- `balaoFala.png` - Balão de fala

## 🔧 CONFIGURAÇÕES PRINCIPAIS

No arquivo `config.py`:
- `TIP_DURATION` - Segundos que a dica fica visível
- `AUTO_INTERVAL` - Segundos entre dicas automáticas
- `TIPS` - Lista de dicas

## ❓ PROBLEMAS COMUNS

1. **Não aparece**: Verifique se as imagens estão na pasta
2. **Ctrl+Alt+S não funciona**: Execute com privilégios adequados
3. **Erro de dependências**: Execute `./install_dependencies.sh`

---
**Divirta-se com seu Dark Souls Buddy! ⚔️**
