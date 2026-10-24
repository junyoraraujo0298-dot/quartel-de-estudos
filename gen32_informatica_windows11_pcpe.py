# -*- coding: utf-8 -*-
# Adiciona conteudo de Informatica (Sistema Operacional Windows 11)
# pra PC-PE: um deck de teoria na aba Teoria (corp PCPE), com duas
# cenas SVG simples recriando os diagramas do PDF (pirâmide
# hardware/SO/softwares e SO-gerente-recursos) e tabelas pra listas
# (requisitos, atalhos, comandos do Executar, etc.), seguindo o
# pedido do usuario de manter o aspecto visual/didatico sem depender
# de capturas de tela reais. Tambem adiciona as 5 questoes Certo/
# Errado genuinas encontradas no material (as demais questoes do PDF
# sao de multipla escolha A-E, de banca nao-CEBRASPE, e foram
# deixadas de fora pra manter consistencia com o formato real do
# CEBRASPE, igual decidido pro Direito Penal). Fonte: "Sistema
# Operacional Windows 11.pdf", Focus Concursos.
import re
import json

with open('app-template.html', encoding='utf-8') as f:
    html = f.read()

# -------------------- duas cenas SVG novas em TEORIA_SCENES --------------------
OLD_SCENES_TAIL = (
    '    <text x="100" y="112" font-size="10" text-anchor="middle" fill="var(--red)" '
    'font-family="IBM Plex Mono, monospace">compressão abdominal ↑</text></svg>`\n};'
)
assert OLD_SCENES_TAIL in html, "fim de TEORIA_SCENES nao encontrado como esperado"

NEW_SCENES = ''',
  win11Camadas: `<svg viewBox="0 0 200 120">
    <rect x="30" y="10" width="140" height="28" rx="6" fill="var(--gold)" stroke="var(--ink)" stroke-width="2"/>
    <text x="100" y="28" font-size="12" text-anchor="middle" fill="var(--ink)" font-family="IBM Plex Mono, monospace">Softwares</text>
    <rect x="30" y="46" width="140" height="28" rx="6" fill="var(--navy-3)" stroke="var(--ink)" stroke-width="2"/>
    <text x="100" y="64" font-size="10.5" text-anchor="middle" fill="var(--paper)" font-family="IBM Plex Mono, monospace">Sistema Operacional</text>
    <rect x="30" y="82" width="140" height="28" rx="6" fill="var(--gold-deep)" stroke="var(--ink)" stroke-width="2"/>
    <text x="100" y="100" font-size="12" text-anchor="middle" fill="var(--paper)" font-family="IBM Plex Mono, monospace">Hardware</text></svg>`,
  win11Gerente: `<svg viewBox="0 0 200 120">
    <rect x="4" y="46" width="76" height="28" rx="6" fill="var(--navy-3)" stroke="var(--ink)" stroke-width="2"/>
    <text x="42" y="64" font-size="9.5" text-anchor="middle" fill="var(--paper)" font-family="IBM Plex Mono, monospace">SO (gerente)</text>
    <line x1="80" y1="54" x2="120" y2="14" stroke="var(--ink)" stroke-width="2"/>
    <line x1="80" y1="58" x2="120" y2="42" stroke="var(--ink)" stroke-width="2"/>
    <line x1="80" y1="62" x2="120" y2="78" stroke="var(--ink)" stroke-width="2"/>
    <line x1="80" y1="66" x2="120" y2="106" stroke="var(--ink)" stroke-width="2"/>
    <rect x="122" y="4" width="74" height="20" rx="5" fill="var(--gold)" stroke="var(--ink)" stroke-width="1.5"/>
    <text x="159" y="18" font-size="9" text-anchor="middle" fill="var(--ink)" font-family="IBM Plex Mono, monospace">Processos</text>
    <rect x="122" y="32" width="74" height="20" rx="5" fill="var(--gold)" stroke="var(--ink)" stroke-width="1.5"/>
    <text x="159" y="46" font-size="9" text-anchor="middle" fill="var(--ink)" font-family="IBM Plex Mono, monospace">Memória</text>
    <rect x="122" y="68" width="74" height="20" rx="5" fill="var(--gold)" stroke="var(--ink)" stroke-width="1.5"/>
    <text x="159" y="82" font-size="9" text-anchor="middle" fill="var(--ink)" font-family="IBM Plex Mono, monospace">Dispositivos</text>
    <rect x="122" y="96" width="74" height="20" rx="5" fill="var(--gold)" stroke="var(--ink)" stroke-width="1.5"/>
    <text x="159" y="110" font-size="8.3" text-anchor="middle" fill="var(--ink)" font-family="IBM Plex Mono, monospace">Arquivos/Pastas</text></svg>`
};'''

html = html.replace(OLD_SCENES_TAIL, OLD_SCENES_TAIL[:-2] + NEW_SCENES[1:], 1)
# (substitui o ';' final por vírgula + novas cenas + fechamento)

with open('app-template.html', 'w', encoding='utf-8', newline='') as f:
    f.write(html)
print('Duas cenas SVG novas adicionadas a TEORIA_SCENES.')

# -------------------- deck de teoria --------------------
with open('app-template.html', encoding='utf-8') as f:
    html = f.read()

TEORIA_ITEMS = [
    {"t": "tit", "x": "INFORMÁTICA — SISTEMA OPERACIONAL WINDOWS 11 (PC-PE)"},
    {"t": "art", "n": "O que é um Sistema Operacional (SO)", "img": "win11Camadas",
     "x": "Um sistema operacional é um software que gerencia o hardware e os softwares de um computador, "
          "permitindo que o usuário interaja com a máquina de forma eficiente. Ele é a ponte entre os "
          "programas e os componentes físicos do dispositivo. Para instalar outros softwares, primeiro "
          "precisa-se do hardware (componentes físicos) e de um sistema operacional (o software "
          "fundamental que permite o hardware funcionar e gerencia os demais programas)."},
    {"t": "art", "n": "O que o SO gerencia", "img": "win11Gerente",
     "x": "O SO gerencia processos, memória, dispositivos, arquivos e pastas, alocando recursos para que "
          "os programas funcionem eficientemente e garantindo que todos os componentes trabalhem em "
          "harmonia."},
    {"t": "art", "n": "Processos",
     "x": "Um processo é um programa em execução no computador. O SO decide quais processos são "
          "executados, em que ordem e por quanto tempo, garantindo recursos (memória, tempo de "
          "processamento) a cada um. Quando vários processos precisam rodar ao mesmo tempo, o SO alterna "
          "rapidamente entre eles — isso é chamado de multitarefa. O SO também monitora cada processo e "
          "pode interrompê-lo se ele travar, evitando que afete o sistema como um todo."},
    {"t": "art", "n": "Memória",
     "x": "A memória armazena informações temporárias enquanto o computador trabalha. Quando um programa "
          "é executado, o SO reserva uma parte da memória para ele; se muitos programas estiverem "
          "abertos, o SO divide a memória entre eles. O SO também monitora o uso de memória e pode "
          "liberar memória ou encerrar um programa problemático para manter o sistema estável."},
    {"t": "art", "n": "Dispositivos",
     "x": "Dispositivo é qualquer equipamento conectado ao computador (teclado, mouse, impressora, "
          "câmera, pendrive, disco rígido etc.). O SO reconhece novos dispositivos e instala os drivers "
          "necessários. DRIVER é um software que faz com que o Sistema Operacional reconheça um "
          "hardware. O SO também coordena o uso de um mesmo dispositivo por diferentes programas (ex.: "
          "define a ordem de impressões quando dois programas usam a impressora ao mesmo tempo)."},
    {"t": "art", "n": "Arquivos e Pastas",
     "x": "Arquivos são documentos (textos, fotos, músicas, vídeos etc.); pastas organizam esses "
          "documentos em uma estrutura hierárquica. O SO realiza, nos bastidores, as ações de criar, "
          "salvar, mover, copiar ou excluir arquivos, além de controlar a segurança e o acesso a eles "
          "(ex.: exigir senha para abrir um arquivo importante)."},
    {"t": "art", "n": "Requisitos mínimos do Windows 11",
     "x": "Para instalar o Windows 11, a máquina precisa atender aos requisitos mínimos: processador, "
          "memória RAM e armazenamento.",
     "tbl": [["Requisito", "Mínimo exigido"],
             ["Processador", "1 GHz (GHz) ou mais rápido, com 2 ou mais núcleos"],
             ["Memória RAM", "4 GB ou mais"],
             ["Armazenamento", "64 GB ou maior dispositivo de armazenamento"]]},
    {"t": "art", "n": "Área de Trabalho (Desktop)",
     "x": "É a principal interface do Windows 11, onde ficam ícones, atalhos e a Barra de Tarefas — a "
          "tela inicial após o login. Pode ser personalizada com papéis de parede, widgets e ícones. O "
          "Windows 11 permite criar e gerenciar múltiplas Áreas de Trabalho Virtuais, e o Menu Iniciar "
          "foi redesenhado, ficando centralizado na Barra de Tarefas."},
    {"t": "art", "n": "Barra de Tarefas",
     "x": "Fica na parte inferior da tela. Permite fixar programas de uso frequente, ver notificações, "
          "ícones de status e acessar funções essenciais (Gerenciador de Arquivos, Central de Ações). "
          "Tem integração com o Microsoft Teams e inclui widgets (previsão do tempo, notícias). É "
          "personalizável: dá pra mover ícones e ajustar configurações."},
    {"t": "art", "n": "Widgets",
     "x": "São pequenas aplicações que exibem informações úteis (notícias, previsão do tempo, "
          "calendário, bolsa de valores, esportes) diretamente na interface. Acesso rápido pelo atalho "
          "Win + W ou clicando no ícone de Widgets na barra de tarefas. São personalizáveis e "
          "atualizados dinamicamente, sem precisar abrir um aplicativo completo."},
    {"t": "art", "n": "Botão e Menu Iniciar",
     "x": "O Botão Iniciar dá acesso ao Menu Iniciar, onde se abrem aplicativos, pesquisam-se arquivos e "
          "acessam-se configurações. No Windows 11 o botão fica centralizado na barra de tarefas "
          "(diferente do Windows 10, que era à esquerda). Atalho rápido: tecla Windows ou CTRL + ESC. "
          "Pelo Menu Iniciar também é possível pesquisar aplicativos, configurações e documentos."},
    {"t": "art", "n": "Menu Iniciar — Desligar",
     "x": "O botão Desligar fica dentro do Menu Iniciar, no canto inferior direito, com várias opções de "
          "energia. O atalho Alt + F4 na Área de Trabalho também abre a caixa 'Desligar o Windows' com "
          "essas opções (além de Trocar usuário e Sair).",
     "tbl": [["Opção", "O que faz"],
             ["Desligar", "Fecha todos os programas e desliga completamente o PC"],
             ["Reiniciar", "Fecha tudo e reinicia o computador — útil para aplicar atualizações"],
             ["Suspender", "Baixo consumo de energia; o PC liga mais rápido e volta ao ponto onde "
                            "ficou; o Windows salva o trabalho e desliga se a bateria ficar fraca; "
                            "muitos notebooks suspendem ao fechar a tampa"],
             ["Hibernar (se ativado)", "Salva o estado do sistema no disco e desliga o PC, consumindo "
                                       "menos energia que a suspensão"]]},
    {"t": "art", "n": "Caixa de Pesquisa e Visão de Tarefas",
     "x": "A Caixa de Pesquisa encontra rapidamente aplicativos, arquivos, configurações e conteúdo na "
          "web. A Visão de Tarefas (atalho Win + Tab) exibe todas as janelas abertas, permite alternar "
          "entre elas e criar múltiplas Áreas de Trabalho Virtuais — cada uma com suas próprias janelas "
          "e aplicativos, útil para separar trabalho, projetos pessoais e entretenimento. Para criar uma "
          "nova área: Win + Tab e clicar em 'Nova área de trabalho' (+). Para alternar entre áreas: "
          "Win + Ctrl + Seta Direita/Esquerda."},
    {"t": "art", "n": "Jump List",
     "x": "É a lista que exibe rapidamente arquivos ou ações recentes de um aplicativo. Acessada ao "
          "clicar com o botão direito no ícone de um aplicativo fixado na barra de tarefas ou no Menu "
          "Iniciar."},
    {"t": "art", "n": "Aplicativos nativos — extensões padrão",
     "x": "Ao instalar o Windows 11, calculadora, Bloco de Notas, WordPad e Paint já vêm instalados.",
     "tbl": [["Aplicativo", "Tipo", "Extensão padrão"],
             ["Bloco de Notas", "Editor de texto simples (sem formatação)", ".txt"],
             ["Paint", "Editor de imagens", ".png (suporta também JPEG e BMP)"],
             ["WordPad", "Editor de texto com formatação básica", ".rtf (suporta também .txt e .docx)"]]},
    {"t": "art", "n": "Ferramentas Administrativas",
     "x": "Conjunto de utilitários avançados para gerenciar configurações, monitorar e manter o "
          "desempenho do sistema, configurar segurança e realizar manutenção — incluem Visualizador de "
          "Eventos, Gerenciamento de Computadores, Gerenciamento de Disco, Serviços, entre outros. "
          "Acessíveis pelo Painel de Controle, em 'Ferramentas Administrativas'."},
    {"t": "art", "n": "Desfragmentador/Otimizador de Unidades",
     "x": "A fragmentação faz o disco rígido fazer um trabalho extra que pode atrasar o computador. O "
          "Desfragmentador de Disco reorganiza os dados fragmentados para que discos e unidades "
          "funcionem de forma mais eficiente. Roda por agendamento, mas também pode ser executado "
          "manualmente."},
    {"t": "art", "n": "Limpeza de Disco",
     "x": "Examina, exibe e exclui determinados arquivos e pastas, liberando espaço no disco rígido e "
          "melhorando o desempenho. É preciso assinalar (marcar) os arquivos que serão excluídos antes "
          "de confirmar."},
    {"t": "art", "n": "Executar (Win + R) — principais comandos",
     "x": "O Executar permite acessar rapidamente programas, pastas, documentos e configurações, "
          "digitando comandos específicos.",
     "tbl": [["Comando", "O que abre"],
             ["cmd", "Prompt de Comando do DOS"],
             ["control", "Painel de Controle"],
             ["explorer", "Explorador de Arquivos"],
             ["mspaint", "Paint"],
             ["notepad", "Bloco de Notas"],
             ["osk", "Teclado Virtual"],
             ["write", "WordPad"]]},
    {"t": "art", "n": "Gerenciador de Tarefas",
     "x": "Monitora o desempenho do computador, processos e aplicativos; permite encerrar tarefas, "
          "reiniciar ou parar processos, e analisar o uso de recursos. Atalhos: CTRL + SHIFT + ESC (abre "
          "direto) ou CTRL + ALT + DEL (abre uma tela com a opção Gerenciador de Tarefas, além de "
          "Bloquear, Trocar usuário e Sair)."},
    {"t": "art", "n": "Agendador de Tarefas",
     "x": "Permite agendar tarefas para serem executadas automaticamente no computador, em horários ou "
          "eventos específicos."},
    {"t": "art", "n": "Windows Defender — evolução",
     "x": "Protege o computador contra acessos não autorizados e maliciosos, monitorando o tráfego de "
          "rede que entra e sai do dispositivo.",
     "tbl": [["Versão do Windows", "Função do Defender"],
             ["Windows 7", "Antispyware"],
             ["Windows 8 e 8.1", "Antimalware"],
             ["Windows 10 e 11", "Função de antimalware e de firewall"]]},
    {"t": "art", "n": "Windows Defender Firewall — perfis de rede",
     "x": "Os perfis de rede determinam o comportamento do firewall conforme o tipo de rede conectada, "
          "adaptando a proteção ao contexto.",
     "tbl": [["Perfil", "Quando é usado", "Nível de restrição"],
             ["Rede Privada", "Casa ou rede de confiança, com dispositivos conhecidos", "Mais permissivo "
              "— pressupõe-se que a rede é segura"],
             ["Rede Pública", "Ambientes desconhecidos/inseguros (Wi-Fi de cafeteria, aeroporto, hotel)",
              "Mais rigoroso — geralmente bloqueia comunicação de outros dispositivos na rede"],
             ["Rede Domínio", "Ambiente corporativo, dispositivo parte de um domínio de rede", "Aplica "
              "políticas de segurança corporativas, com camada adicional de proteção"]]},
    {"t": "art", "n": "Área de Trabalho Remota",
     "x": "Permite acessar e controlar um computador a partir de um dispositivo remoto (laptop, tablet, "
          "outro PC), bastando uma conexão à internet — útil para acessar o computador do escritório a "
          "partir de casa, por exemplo."},
    {"t": "art", "n": "BitLocker",
     "x": "Ferramenta de segurança que criptografa unidades de disco, protegendo os dados contra roubo "
          "ou perda do dispositivo. A Criptografia de Unidade de Disco BitLocker protege arquivos na "
          "unidade onde o Windows está instalado e em unidades de dados fixas (discos rígidos "
          "internos). Já o BitLocker To Go protege arquivos em unidades de dados EXTERNAS (discos "
          "rígidos externos, pendrives/unidades flash USB)."},
    {"t": "art", "n": "Painel de Controle — categorias",
     "x": "Interface que permite alterar configurações do sistema e personalizar o funcionamento do "
          "computador.",
     "tbl": [["Categoria", "Exemplos do que contém"],
             ["Sistema e Segurança", "Histórico de Arquivos, Windows Defender Firewall, Opções de "
              "Energia, informações do sistema"],
             ["Rede e Internet", "Central de Rede e Compartilhamento, Opções da Internet"],
             ["Hardware e Sons", "Dispositivos e Impressoras, Reprodução Automática, Som, Opções de "
              "Energia"],
             ["Programas", "Programas e Recursos (desinstalar/alterar programas), Programas Padrão"],
             ["Contas de Usuário", "Alterar tipo de conta, Gerenciador de Credenciais"],
             ["Aparência e Personalização", "Barra de Tarefas e Navegação, Central de Facilidade de "
              "Acesso, Opções do Explorador de Arquivos, Fontes"],
             ["Relógio e Região", "Data e Hora, Região"],
             ["Facilidade de Acesso", "Central de Facilidade de Acesso, Reconhecimento de Fala"]]},
    {"t": "art", "n": "Histórico de Arquivos",
     "x": "Funcionalidade de backup que guarda automaticamente cópias dos arquivos e pastas pessoais, "
          "para restaurá-los caso sejam perdidos ou danificados. Faz cópia de segurança automática de "
          "todas as bibliotecas (Documentos, Imagens, Vídeos, Música — predefinidas ou personalizadas). "
          "Precisa ser ativado e ter uma unidade de destino definida (ex.: um disco externo)."},
    {"t": "art", "n": "Configurações (Win + I) — categorias principais",
     "x": "O menu de Configurações é o centro de controle do Windows 11, acessível pelo Menu Iniciar, "
          "pelo atalho Win + I, ou pesquisando 'Configurações'.",
     "tbl": [["Categoria", "Conteúdo típico"],
             ["Sistema", "Tela, som, notificações, foco, energia e bateria, armazenamento"],
             ["Bluetooth e dispositivos", "Impressoras, scanners, mouse, dispositivos emparelhados"],
             ["Rede e Internet", "Wi-Fi, Ethernet, VPN, hotspot móvel, modo avião"],
             ["Personalização", "Tela de fundo, cores, temas, tela de bloqueio, barra de tarefas"],
             ["Aplicativos", "Aplicativos instalados, padrões, inicialização"],
             ["Contas", "Opções de entrada (Windows Hello), contas vinculadas, backup"],
             ["Hora e idioma", "Data e hora, idioma e região, digitação, fala"],
             ["Jogos", "Modo de jogo, barra de jogo, gravação de tela"],
             ["Acessibilidade", "Tamanho do texto, lupa, filtros de cor, narrador"],
             ["Privacidade e segurança", "Segurança do Windows, permissões de apps"],
             ["Windows Update", "Verificar atualizações, histórico, opções avançadas"]]},
    {"t": "art", "n": "Windows Hello",
     "x": "Funcionalidade de autenticação biométrica do Windows 10/11, permitindo acessar dispositivos, "
          "aplicações, dados e redes usando reconhecimento facial, impressão digital ou PIN — uma "
          "alternativa mais rápida e segura que senhas tradicionais. Entrar com o rosto exige câmera "
          "compatível com o Hello; entrar com impressão digital exige leitor de impressões digitais no "
          "dispositivo."},
    {"t": "art", "n": "Windows Update",
     "x": "Mantém o computador atualizado com correções de segurança (proteção contra malware, vírus e "
          "outras ameaças), melhorias de desempenho e novas funcionalidades. Verifica automaticamente "
          "se há atualizações disponíveis e notifica o usuário; é possível instalar imediatamente ou "
          "agendar a instalação."},
    {"t": "art", "n": "Explorador de Arquivos — Acesso Rápido e Propriedades",
     "x": "O Acesso Rápido fixa as pastas e arquivos mais usados para acesso ágil (clicando com o botão "
          "direito sobre a pasta e escolhendo 'Fixar no Acesso rápido', ou pelo botão 'Ver Mais' "
          "(...) do Explorador). Propriedades mostra informações detalhadas de um arquivo/pasta "
          "(permissões, segurança, atributos como somente leitura/oculto). Atalho: Alt + Enter, ou "
          "clicar com o botão direito no item e escolher 'Propriedades'."},
    {"t": "art", "n": "Criar atalho — formas de fazer",
     "x": "Um atalho é um link para um item (arquivo, pasta ou programa); diferencia-se do arquivo "
          "original pela seta no ícone. Principais formas de criar um atalho: (1) menu 'Novo' > "
          "'Atalho'; (2) arrastar o arquivo para a área de trabalho pressionando ALT; (3) arrastar "
          "pressionando CTRL + SHIFT; (4) clicar com o botão direito no item, 'Mostrar mais opções' > "
          "'Criar atalho'; (5) clicar com o botão direito, 'Mostrar mais opções' > 'Enviar para' > "
          "'Área de trabalho (criar atalho)'."},
    {"t": "art", "n": "Caracteres proibidos em nomes de arquivos e pastas",
     "x": "No Windows 11, certos caracteres são proibidos em nomes de arquivos e pastas para evitar "
          "conflitos e erros no sistema: barra invertida (\\\\), barra (/), dois-pontos (:), asterisco "
          "(*), interrogação (?), aspas (\"), sinais de maior/menor (< >) e barra vertical/pipe (|)."},
    {"t": "art", "n": "Operações básicas — arrastar para copiar ou mover",
     "x": "Ao arrastar um item com o mouse no Explorador de Arquivos, o comportamento padrão muda "
          "conforme a unidade de destino, e pode ser forçado com teclas modificadoras.",
     "tbl": [["Ação desejada", "Mesma unidade (ex.: C: para C:)", "Unidades diferentes (ex.: C: para D:/pendrive)"],
             ["Copiar", "Arrastar + CTRL", "Arrastar (comportamento padrão)"],
             ["Mover (recortar)", "Arrastar (comportamento padrão)", "Arrastar + SHIFT"]],
     "s": "Renomear: tecla F2, ou pela barra de menu do Explorador de Arquivos."},
    {"t": "art", "n": "Área de Transferência",
     "x": "Permite copiar, recortar e colar textos, imagens, arquivos e outros dados dentro e entre "
          "aplicativos (Ctrl+C / Ctrl+X / Ctrl+V). Pode armazenar várias entradas, dando acesso a um "
          "histórico dos itens copiados recentemente. Atalho: Win + V. É possível colar itens antigos "
          "do histórico, fixar itens de uso frequente e sincronizar o histórico com a nuvem."},
    {"t": "art", "n": "Lixeira",
     "x": "Localizada na área de trabalho (ou acessível pelo Explorador de Arquivos). Opções principais: "
          "Esvaziar Lixeira (apaga permanentemente todos os itens), Restaurar todos os itens, e "
          "Restaurar itens selecionados (volta cada um à sua localização original).",
     "tbl": [["Onde o arquivo foi excluído", "Vai para a Lixeira?"],
             ["HD interno", "Sim"],
             ["HD externo", "Sim"],
             ["Pendrive", "Não — exclusão definitiva"],
             ["Computador em rede", "Não — exclusão definitiva"]],
     "s": "SHIFT + DEL exclui um item permanentemente em qualquer unidade, sem passar pela Lixeira."},
    {"t": "art", "n": "OneDrive",
     "x": "Serviço de armazenamento em nuvem da Microsoft, integrado ao Windows e ao Microsoft 365. "
          "Permite armazenar documentos, fotos e vídeos na nuvem (liberando espaço local), sincroniza "
          "automaticamente arquivos entre dispositivos conectados à mesma conta, e permite compartilhar "
          "arquivos/pastas com outros usuários definindo permissões (visualizar ou editar)."},
    {"t": "art", "n": "Unidades, Pastas e Arquivos",
     "x": "Unidades são os dispositivos de armazenamento reconhecidos pelo SO (discos rígidos, SSDs, "
          "unidades USB, partições), identificadas por letras (C:, D:) — gerenciadas pelo 'Gerenciamento "
          "de Disco'. Pastas são diretórios que organizam arquivos e outras pastas em estrutura "
          "hierárquica. Arquivos são as unidades básicas de armazenamento de dados; cada um tem um nome "
          "e uma extensão, que define seu tipo e o programa necessário para abri-lo."},
    {"t": "art", "n": "Snap Layouts / Snap Assist",
     "x": "Recurso do Windows 11 (evolução do Snap Assist do Windows 10) que permite redimensionar e "
          "posicionar várias janelas na tela, maximizando o espaço de trabalho. No Windows 11, os "
          "layouts predefinidos aparecem ao passar o cursor do mouse sobre o botão 'Maximizar' de uma "
          "janela."},
    {"t": "art", "n": "Lista de Atalhos do Windows 11",
     "x": "Principais atalhos de teclado cobrados em prova.",
     "tbl": [["Atalho", "Ação"],
             ["CTRL + A", "Seleciona todos os itens"],
             ["CTRL + C", "Copiar os itens selecionados"],
             ["CTRL + X", "Recortar os itens selecionados"],
             ["CTRL + V", "Colar os itens selecionados"],
             ["CTRL + Z", "Desfaz a última ação"],
             ["CTRL + Y", "Refazer"],
             ["CTRL + ESC", "Abre o Menu Iniciar"],
             ["CTRL + SHIFT + ESC", "Abre o Gerenciador de Tarefas"],
             ["CTRL + ALT + DEL", "Tela com Bloquear, Trocar usuário, Sair e Gerenciador de Tarefas"],
             ["ALT + TAB", "Alternar entre as janelas abertas"],
             ["ALT + F4", "Fechar a janela atual (ou abrir 'Desligar o Windows' na área de trabalho)"],
             ["ALT + ENTER", "Abre Propriedades do item selecionado"],
             ["DELETE", "Envia o item selecionado para a Lixeira"],
             ["SHIFT + DELETE", "Exclui o item selecionado permanentemente"],
             ["F2", "Renomear"],
             ["F3", "Pesquisar"],
             ["F5", "Atualizar"],
             ["F10", "Menu Arquivo"],
             ["WIN", "Abre/fecha o Menu Iniciar"],
             ["WIN + D", "Minimizar todas as janelas (mostrar a área de trabalho)"],
             ["WIN + E", "Abre o Explorador de Arquivos"],
             ["WIN + L", "Bloquear o computador"],
             ["WIN + M", "Minimizar todas as janelas"],
             ["WIN + SHIFT + M", "Restaura as janelas minimizadas pelo WIN + M"],
             ["WIN + I", "Abre as Configurações do Windows"],
             ["WIN + R", "Abre o Executar"],
             ["WIN + V", "Abre o histórico da Área de Transferência"],
             ["WIN + W", "Abre o painel de Widgets"],
             ["WIN + TAB", "Abre a Visão de Tarefas"],
             ["WIN + CTRL + Seta Direita/Esquerda", "Alterna entre Áreas de Trabalho Virtuais"],
             ["WIN + Seta Direita/Esquerda", "Encaixa a janela ativa na metade direita/esquerda da tela"],
             ["WIN + Seta para Cima", "Maximiza a janela ativa"],
             ["WIN + Seta para Baixo", "Restaura/minimiza a janela ativa"],
             ["WIN + PAUSE/BREAK", "Abre Propriedades do Sistema"]]},
]

array_literal = '[\n' + ',\n'.join(json.dumps(it, ensure_ascii=False) for it in TEORIA_ITEMS) + '\n]'

m = re.search(r'const TEORIA_LINGUA_PORTUGUESA_PCPE\s*=\s*\[', html)
assert m, "bloco TEORIA_LINGUA_PORTUGUESA_PCPE nao encontrado"
decoder = json.JSONDecoder()
start = m.end() - 1
_arr, end = decoder.raw_decode(html, start)
insertion_point = end + 1  # depois do ';'
new_block = '\n\nconst TEORIA_INFORMATICA_WIN11_PCPE = ' + array_literal + ';'
html = html[:insertion_point] + new_block + html[insertion_point:]

old_teoria_tail = ('  portugues_pcpe: { label: "Língua Portuguesa — Ortografia e Acentuação (PC-PE)", '
                   'data: TEORIA_LINGUA_PORTUGUESA_PCPE, corp: "PCPE" }\n};')
assert old_teoria_tail in html, "final de TEORIA_DECKS nao encontrado como esperado"
new_teoria_tail = ('  portugues_pcpe: { label: "Língua Portuguesa — Ortografia e Acentuação (PC-PE)", '
                   'data: TEORIA_LINGUA_PORTUGUESA_PCPE, corp: "PCPE" },\n'
                   '  informatica_win11_pcpe: { label: "Informática — Sistema Operacional Windows 11 (PC-PE)", '
                   'data: TEORIA_INFORMATICA_WIN11_PCPE, corp: "PCPE" }\n};')
html = html.replace(old_teoria_tail, new_teoria_tail, 1)

old_disc_map_tail = ('const TEORIA_DECK_TO_DISC = {\n'
                      '  direito_penal_pcpe: "Direito Penal",\n'
                      '  portugues_pcpe: "Língua Portuguesa"\n'
                      '};')
assert old_disc_map_tail in html, "TEORIA_DECK_TO_DISC nao encontrado como esperado"
new_disc_map_tail = ('const TEORIA_DECK_TO_DISC = {\n'
                      '  direito_penal_pcpe: "Direito Penal",\n'
                      '  portugues_pcpe: "Língua Portuguesa",\n'
                      '  informatica_win11_pcpe: "Informática"\n'
                      '};')
html = html.replace(old_disc_map_tail, new_disc_map_tail, 1)

with open('app-template.html', 'w', encoding='utf-8', newline='') as f:
    f.write(html)
print('TEORIA_INFORMATICA_WIN11_PCPE adicionada com', len(TEORIA_ITEMS), 'itens; registrada em TEORIA_DECKS e TEORIA_DECK_TO_DISC.')

# -------------------- questoes --------------------
CE_QUESTIONS = [
    ("O Paint e o Bloco de Notas foram descontinuados no Windows 11 em favor de ferramentas de edição "
     "online integradas.", False, "Aplicativos nativos — Bloco de Notas e Paint",
     "Errado — Paint e Bloco de Notas continuam nativos e instalados por padrão no Windows 11, como "
     "aplicativos locais (não foram descontinuados nem substituídos por ferramentas apenas online)."),
    ("No Windows 10, para mitigar o acesso não autorizado a dados, tornando os dados inacessíveis por "
     "meio de criptografia, é correto utilizar o recurso denominado BitLocker.", True, "BitLocker",
     "Correto — o BitLocker é a ferramenta de criptografia de unidades de disco do Windows, usada "
     "justamente para proteger dados contra acesso não autorizado."),
    ("No Windows 11, uma das novidades introduzidas para aprimorar a experiência multitarefa é a "
     "remoção total do Painel de Controle, a ser substituído pelas Configurações.", False,
     "Painel de Controle",
     "Errado — o Painel de Controle ainda existe e é acessível no Windows 11; ele convive com o app "
     "Configurações (que vem assumindo cada vez mais funções), mas não foi totalmente removido."),
    ("Para fixar uma pasta no acesso rápido do painel de navegação do Windows, basta que o usuário a "
     "clique com o botão direito do mouse e selecione a opção Fixar em Acesso Rápido.", True,
     "Explorador de Arquivos — Acesso Rápido",
     "Correto — esse é exatamente o procedimento padrão para fixar uma pasta no Acesso Rápido do "
     "Explorador de Arquivos."),
    ("O gerenciamento de arquivos é um procedimento que envolve a organização, o armazenamento e a "
     "manutenção de arquivos e de pastas no computador.", True, "Arquivos e Pastas",
     "Correto — essa é a definição geral de gerenciamento de arquivos, função realizada pelo sistema "
     "operacional por meio do Explorador de Arquivos."),
]

with open('questions.json', encoding='utf-8') as f:
    qdata = json.load(f)

next_id = max(q['id'] for q in qdata) + 1
added = 0
for enun, resp, assunto, exp in CE_QUESTIONS:
    qdata.append({
        "id": next_id,
        "corp": "PCPE",
        "disc": "Informática",
        "assunto": assunto,
        "tipo": "CE",
        "enun": enun,
        "resp": resp,
        "exp": exp,
    })
    next_id += 1
    added += 1

lines = [json.dumps(q, ensure_ascii=False) for q in qdata]
body = '[' + lines[0]
for line in lines[1:]:
    body += '\r\n, ' + line
body += ']'

with open('questions.json', 'w', encoding='utf-8', newline='') as f:
    f.write(body)

with open('questions.json', encoding='utf-8') as f:
    check = json.load(f)
assert len(check) == len(qdata)
print('OK --', added, 'questoes de Informática (PC-PE) adicionadas. Total no banco:', len(check))

# -------------------- regenera o HTML final --------------------
with open('questions.json', encoding='utf-8') as f:
    qdata_raw = f.read()
with open('app-template.html', encoding='utf-8') as f:
    html2 = f.read()
html2 = html2.replace('__QUESTIONS_JSON__', qdata_raw)
with open('estudo-cebraspe-ma.html', 'w', encoding='utf-8') as f:
    f.write(html2)
print('estudo-cebraspe-ma.html regenerado com sucesso')
