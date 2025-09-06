TIPS = [
    # Cibersegurança - Defesa (Blue Team)
    "Lembre-se de sempre fazer backup dos seus dados importantes! (Regra 3-2-1: 3 cópias, 2 mídias, 1 offline)",
    "Use senhas fortes e únicas para cada conta. Um gerenciador de senhas pode ajudar.",
    "Mantenha seu sistema sempre atualizado com 'sudo apt update && sudo apt full-upgrade'.",
    "Verifique a integridade de downloads com checksums (sha256sum, md5sum).",
    "Use uma VPN confiável ao acessar redes Wi-Fi públicas ou não seguras.",
    "Documente seus procedimentos de segurança. Se não está escrito, não existe.",
    "Use autenticação de dois fatores (2FA) em todos os serviços que o suportam.",
    "Monitore logs do sistema em /var/log para atividades suspeitas. 'journalctl -f' é seu amigo.",
    "Criptografe discos e arquivos sensíveis com LUKS ou GPG.",
    "Teste seus backups regularmente para garantir que a restauração funciona.",
    "Use sandboxes ou máquinas virtuais para analisar software suspeito com segurança.",
    "Use chaves SSH com senhas fortes em vez de autenticação por senha.",
    "Implemente o Princípio do Menor Privilégio: cada usuário/serviço deve ter apenas as permissões necessárias.",
    "Configure o UFW (Uncomplicated Firewall) para bloquear portas não utilizadas.",
    "Já checou as permissões dos arquivos em /etc? Use 'ls -l' para verificar.",
    "Reconhecimento é a fase mais crucial. Use ferramentas como nmap, gobuster e sublist3r.",
    "Um scan com 'nmap -sV -sC -p- <alvo>' pode revelar versões de serviços e scripts úteis.",
    "Não subestime o poder da Engenharia Social. Conhecer o alvo é metade da batalha.",
    "Sempre verifique se há exploits públicos para as versões de software que encontrar (searchsploit).",
    "Escalação de privilégios é a chave. Procure por SUID/SGID, cron jobs e senhas em arquivos.",
    "Use 'linpeas.sh' ou 'lse.sh' para enumerar fraquezas em sistemas Linux.",
    "Um bom pivoteamento pode transformar um acesso limitado em controle total da rede.",
    "Lembre-se de limpar seus rastros e logs após um pentest bem-sucedido.",
    "Web shells são úteis, mas shells reversos com netcat ou socat são mais estáveis.",
    "Aprenda a usar Burp Suite ou OWASP ZAP para interceptar e manipular tráfego web.",
    "Ambientes virtuais (.venv) são essenciais. Use 'python3 -m venv .venv' para criar um.",
    "Use list comprehensions para criar listas de forma concisa e legível. Ex: [x*x for x in range(10)]",
    "O f-string (f'Olá, {variavel}') é a forma moderna e mais eficiente de formatar strings em Python.",
    "Aprenda a usar o debugger do Python: 'import pdb; pdb.set_trace()'.",
    "Sempre use 'with open(...) as f:' para manipular arquivos. Ele fecha o arquivo automaticamente.",
    "Entenda a diferença entre '==' (igualdade de valor) e 'is' (identidade de objeto).",
    "O módulo 'collections' tem estruturas de dados poderosas como defaultdict e Counter.",
    "Decore suas funções com '@functools.lru_cache' para otimizar chamadas repetitivas.",
    "Código limpo e legível é mais importante que código 'inteligente' e complexo.",
    "Versionamento com Git é obrigatório. 'git commit -m \"mensagem clara\"' salva vidas.",
    "Não repita código (DRY - Don't Repeat Yourself). Se você copiou e colou, provavelmente pode criar uma função.",
    "Aprenda a usar o terminal. Ferramentas como grep, awk, sed e curl são superpoderes.",
    "Entender expressões regulares (regex) pode poupar horas de trabalho de manipulação de texto.",
    "Comece o projeto com a estrutura mais simples possível e adicione complexidade conforme a necessidade.",
    "Escreva comentários para explicar o *porquê* do código, não o *o quê*.",
    "Faça uma pausa a cada 25 minutos de trabalho focado (Técnica Pomodoro).",
    "Beba água! Manter-se hidratado é crucial para a concentração.",
    "Organize seu espaço de trabalho. Uma mesa limpa ajuda a ter uma mente clara.",
    "Automatize tarefas repetitivas. Se você faz algo mais de três vezes, escreva um script.",
    "Antes de começar a codificar, planeje em um papel ou pseudocódigo. Isso economiza tempo."
]

TIP_DURATION = 15  # Quanto tempo a dica fica visível
AUTO_INTERVAL = 300  # Intervalo entre dicas automáticas (5 minutos)
WINDOW_TRANSPARENCY = 0.9
BALLOON_WIDTH = 220
BALLOON_HEIGHT = 140
KNIGHT_SIZE = 100
TEXT_WRAP_WIDTH = 25
