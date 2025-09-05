#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerador de Configurações para Dark Souls Buddy
Use este script para configurar facilmente seu amigo virtual
"""

import os

def generate_config():
    print("=== Configurador do Dark Souls Buddy ===\n")
    
    # Configurações de tempo
    print("Configurações de Tempo:")
    tip_duration = input("Por quantos segundos as dicas devem ficar visíveis? (padrão: 15): ").strip()
    if not tip_duration:
        tip_duration = "15"
    
    auto_interval = input("A cada quantos minutos mostrar dicas automáticas? (padrão: 5): ").strip()
    if not auto_interval:
        auto_interval = "5"
    
    # Converter minutos para segundos
    auto_interval_seconds = int(auto_interval) * 60
    
    # Configurações visuais
    print("\nConfigurações Visuais:")
    transparency = input("Transparência da janela (0.1 a 1.0, padrão: 0.9): ").strip()
    if not transparency:
        transparency = "0.9"
    
    balloon_width = input("Largura do balão de fala em pixels (padrão: 300): ").strip()
    if not balloon_width:
        balloon_width = "300"
    
    balloon_height = input("Altura do balão de fala em pixels (padrão: 200): ").strip()
    if not balloon_height:
        balloon_height = "200"
    
    knight_size = input("Tamanho do knight em pixels (padrão: 150): ").strip()
    if not knight_size:
        knight_size = "150"
    
    # Dicas personalizadas
    print("\nDicas Personalizadas:")
    print("Digite suas dicas (uma por linha). Digite 'FIM' quando terminar:")
    
    custom_tips = []
    while True:
        tip = input("Dica: ").strip()
        if tip.upper() == 'FIM':
            break
        if tip:
            custom_tips.append(tip)
    
    # Se não digitou dicas personalizadas, usar as padrão
    if not custom_tips:
        print("Nenhuma dica personalizada adicionada. Usando dicas padrão.")
        custom_tips = [
            "Lembre-se de sempre fazer backup dos seus dados importantes!",
            "Use senhas fortes e únicas para cada conta.",
            "Mantenha seu sistema sempre atualizado.",
            "Verifique a integridade dos arquivos com checksums.",
            "Use VPN ao acessar redes públicas."
        ]
    
    # Gerar arquivo de configuração
    config_content = f"""# Configuração do Dark Souls Buddy
# Arquivo gerado automaticamente pelo configurador

# Lista de dicas - adicione quantas quiser, uma por linha
TIPS = [
"""
    
    for tip in custom_tips:
        config_content += f'    "{tip}",\n'
    
    config_content += f"""]

# Configurações de tempo (em segundos)
TIP_DURATION = {tip_duration}  # Quanto tempo a dica fica visível
AUTO_INTERVAL = {auto_interval_seconds}  # Intervalo entre dicas automáticas ({auto_interval} minutos)

# Configurações visuais
WINDOW_TRANSPARENCY = {transparency}  # Transparência da janela (0.0 a 1.0)
BALLOON_WIDTH = {balloon_width}  # Largura do balão de fala
BALLOON_HEIGHT = {balloon_height}  # Altura do balão de fala
KNIGHT_SIZE = {knight_size}  # Tamanho do GIF do knight
TEXT_WRAP_WIDTH = 30  # Número de caracteres por linha no texto
"""
    
    # Salvar arquivo
    with open('config.py', 'w', encoding='utf-8') as f:
        f.write(config_content)
    
    print(f"\n✅ Configuração salva em config.py!")
    print(f"📊 Resumo da configuração:")
    print(f"   - Dicas ficam visíveis por {tip_duration} segundos")
    print(f"   - Dicas automáticas a cada {auto_interval} minutos")
    print(f"   - Transparência: {transparency}")
    print(f"   - Tamanho do balão: {balloon_width}x{balloon_height}")
    print(f"   - Tamanho do knight: {knight_size}x{knight_size}")
    print(f"   - Total de dicas: {len(custom_tips)}")
    print(f"\n🚀 Para executar o Dark Souls Buddy, use: python3 dark_souls_buddy.py")

def main():
    try:
        generate_config()
    except KeyboardInterrupt:
        print("\n\n❌ Configuração cancelada.")
    except Exception as e:
        print(f"\n❌ Erro: {e}")

if __name__ == "__main__":
    main()
