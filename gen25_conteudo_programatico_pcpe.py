# -*- coding: utf-8 -*-
# Adiciona o conteudo programatico OFICIAL do edital 2026 da PC-PE pro
# cargo de Agente de Policia (item 22.2.3, com retificacao do Edital
# no 2 - PCPE, de 15/10/2026), como um novo deck na aba Estrategia.
# Isso substitui a "estimativa baseada em editais anteriores" que
# tinha sido usada antes do edital sair -- agora e o programa real.
import re
import json

with open('app-template.html', encoding='utf-8') as f:
    html = f.read()

ITEMS = [
    {"t": "tit", "x": "CONTEÚDO PROGRAMÁTICO OFICIAL — PC-PE AGENTE DE POLÍCIA (EDITAL 2026)"},
    {"t": "art", "n": "Sobre este conteúdo",
     "x": "Este é o programa OFICIAL do item 22.2.3 do edital da PC-PE 2026 para o cargo de Agente de "
          "Polícia, já com a retificação do Edital nº 2 – PCPE, de 15 de outubro de 2026 (disponível em "
          "www.cebraspe.org.br/concursos/pc_pe_26). Diferente do cronograma estimado que foi montado antes "
          "de o edital sair, esta lista de tópicos é o programa real cobrado na prova — P1 (Noções de "
          "Direito: Legislação Estadual, Direito Constitucional, Direito Administrativo, Direito Penal e "
          "Direito Processual Penal) e P2 (Conhecimentos Específicos: Português, Informática, Raciocínio "
          "Lógico, Contabilidade Geral e Estatística), além de Atualidades só para a prova discursiva.",
     "s": "Da Legislação Estadual, dois itens já estão completos neste app: a Constituição de PE (arts. "
          "101 a 105-B, deck 'Constituição de PE' aqui na Estratégia) e a Lei nº 6.425/1972 — Estatuto do "
          "Policial Civil (deck também aqui na Estratégia). Ainda faltam: Lei nº 6.123/1968 (Estatuto do "
          "Servidor do Estado de PE — a própria Lei 6.425/1972 remete a ela várias vezes), Lei Complementar "
          "nº 137/2008 e Lei Complementar nº 317/2015. Manda esses PDFs quando quiser que eu adicione."},

    {"t": "cap", "x": "P1 — NOÇÕES DE DIREITO"},
    {"t": "art", "n": "Legislação Estadual",
     "x": "1. Constituição do Estado de Pernambuco (artigos 101 a 105-B). 2. Lei nº 6.425/1972 (Estatuto "
          "do Policial Civil). 3. Lei nº 6.123/1968 (Estatuto do Servidor do Estado de Pernambuco). 4. Lei "
          "Complementar nº 137/2008. 5. Lei Complementar nº 317/2015."},
    {"t": "art", "n": "Direito Constitucional",
     "x": "1. Constituição da República Federativa do Brasil de 1988: 1.1 Princípios fundamentais; 1.2 "
          "Poderes constituintes originário, derivado e decorrente. 2. Aplicabilidade das normas "
          "constitucionais. 3. Direitos e garantias fundamentais. 4. Organização político-administrativa "
          "do Estado: 4.1 Estado federal brasileiro, União, estados, Distrito Federal, municípios e "
          "territórios. 5. Administração pública: 5.1 Disposições gerais, servidores públicos. 6. Poder "
          "Executivo. 7. Poder Legislativo. 8. Poder Judiciário. 9. Funções essenciais à justiça: 9.1 "
          "Ministério Público; 9.2 Advocacia pública; 9.3 Defensoria Pública. 10. Defesa do Estado e das "
          "instituições democráticas. 11. Segurança pública na Constituição do Estado de Pernambuco."},
    {"t": "art", "n": "Direito Administrativo",
     "x": "1. Estado, governo e administração pública. 2. Direito administrativo. 3. Ato administrativo. "
          "4. Poderes da administração pública: 4.1 Hierárquico, disciplinar, regulamentar e de polícia; "
          "4.2 Uso e abuso do poder. 5. Regime jurídico-administrativo: 5.1 Conceito; 5.2 Princípios "
          "expressos e implícitos da administração pública. 6. Responsabilidade civil do Estado. 7. "
          "Serviços públicos. 8. Organização administrativa: 8.1 Centralização, descentralização, "
          "concentração e desconcentração; 8.2 Administração direta e indireta. 9. Controle da "
          "administração pública: 9.1 Controle exercido pela administração pública; 9.2 Controle judicial; "
          "9.3 Controle legislativo; 9.4 Improbidade administrativa. 10. Processo administrativo. 11. "
          "Licitações e contratos administrativos. 12. Agente público: 12.1 Legislação pertinente; 12.2 "
          "Disposições constitucionais aplicáveis. 13. Cargo, emprego e função pública."},
    {"t": "art", "n": "Direito Penal",
     "x": "1. Princípios básicos. 2. Crime e contravenção penal. 3. Aplicação da lei penal: 3.1 Lei penal "
          "no tempo e no espaço; 3.2 Tempo e lugar do crime; 3.3 Lei penal excepcional, especial e "
          "temporária; 3.4 Territorialidade e extraterritorialidade da lei penal; 3.5 Contagem de prazo; "
          "3.6 Irretroatividade da lei penal. 4. Crimes contra a pessoa. 5. Crimes contra o patrimônio. 6. "
          "Crimes contra a dignidade sexual. 7. Crimes contra a administração pública. 8. Crimes hediondos "
          "(Lei nº 8.072/1990). 9. Crimes resultantes de preconceito de raça ou de cor (Lei nº 7.716/1989). "
          "10. Crimes de abuso de autoridade (Lei nº 13.869/2019). 11. Crimes de tortura (Lei nº "
          "9.455/1997). 12. Estatuto da Criança e do Adolescente (Lei nº 8.069/1990). 13. Organizações "
          "criminosas (Lei nº 12.850/2013). 14. Crimes de trânsito (Lei nº 9.503/1997). 15. Violência "
          "doméstica e familiar contra a mulher (Lei nº 11.340/2006). 16. Lei de drogas (Lei nº "
          "11.343/2006). 17. Violência doméstica e familiar contra a criança e o adolescente (Lei nº "
          "14.344/2022). 18. Crimes ambientais (Lei nº 9.605/1998). 19. Estatuto do Desarmamento (Lei nº "
          "10.826/2003). 20. Estatuto da Juventude (Lei nº 12.852/2013). 21. Disposições constitucionais "
          "aplicáveis ao direito penal.",
     "s": "É a disciplina com mais leis extravagantes cobradas (16 leis especiais, de hediondos a Estatuto "
          "da Juventude) — vale montar um cronograma próprio só pra essas leis, já que cada uma costuma "
          "render pelo menos 1 questão."},
    {"t": "art", "n": "Direito Processual Penal",
     "x": "1. Aplicação da lei processual no tempo, no espaço e em relação às pessoas. 2. Inquérito "
          "policial. 3. Prova: exame de corpo de delito e perícias em geral; interrogatório do acusado; "
          "confissão do ofendido; testemunhas; reconhecimento de pessoas e coisas; acareação; documentos; "
          "indícios; busca e apreensão. 4. Prisão e liberdade provisória. 5. Medidas cautelares diversas da "
          "prisão. 6. Lei nº 7.960/1989 (prisão temporária). 7. Juizados especiais criminais (Lei nº "
          "9.099/1995). 8. Investigação criminal (Lei nº 12.830/2013). 9. Disposições constitucionais "
          "aplicáveis ao direito processual penal.",
     "s": "Repare que 'Inquérito Policial' é item isolado (item 2) — é literalmente o instrumento de "
          "trabalho do cargo de Agente de Polícia, tende a ser bem explorado."},

    {"t": "cap", "x": "P2 — CONHECIMENTOS ESPECÍFICOS"},
    {"t": "art", "n": "Língua Portuguesa",
     "x": "1. Compreensão e interpretação de textos de gêneros variados. 2. Reconhecimento de tipos e "
          "gêneros textuais. 3. Domínio da ortografia oficial. 4. Domínio dos mecanismos de coesão textual: "
          "4.1 Emprego de elementos de referenciação, substituição e repetição, de conectores e de outros "
          "elementos de sequenciação textual; 4.2 Emprego de tempos e modos verbais. 5. Domínio da "
          "estrutura morfossintática do período: 5.1 Emprego das classes de palavras; 5.2 Relações de "
          "coordenação entre orações e entre termos da oração; 5.3 Relações de subordinação entre orações e "
          "entre termos da oração; 5.4 Emprego dos sinais de pontuação; 5.5 Concordância verbal e nominal; "
          "5.6 Regência verbal e nominal; 5.7 Emprego do sinal indicativo de crase; 5.8 Colocação dos "
          "pronomes átonos. 6. Reescrita de frases e parágrafos do texto: 6.1 Significação das palavras; "
          "6.2 Substituição de palavras ou de trechos de texto; 6.3 Reorganização da estrutura de orações e "
          "de períodos do texto; 6.4 Reescrita de textos de diferentes gêneros e níveis de formalidade. 7. "
          "Correspondência oficial (conforme Manual de Redação da Presidência da República): 7.1 Aspectos "
          "gerais da redação oficial; 7.2 Finalidade dos expedientes oficiais; 7.3 Adequação da linguagem "
          "ao tipo de documento; 7.4 Adequação do formato do texto ao gênero."},
    {"t": "art", "n": "Informática — Windows e Microsoft 365",
     "x": "1. Sistema operacional Windows: fundamentos (janelas, menus, barra de tarefas, área de "
          "trabalho), trabalho com pastas e arquivos, configurações básicas, Windows Explorer. 2. Microsoft "
          "365: 2.1 Word — área de trabalho e menus, formatação de documentos (margens, tabulação, recuo, "
          "espaçamento, fontes, destaques), listas e colunas, tabelas, estilos e modelos, cabeçalhos/"
          "rodapés, configuração de página; 2.2 Excel — área de trabalho e menus, introdução de números/"
          "textos/fórmulas/datas, referência absoluta e relativa, principais funções (matemáticas, "
          "estatísticas, data-hora, financeiras, texto), formatação, edição (copiar/colar/recortar/"
          "limpar), classificação de dados, gráficos; 2.3 PowerPoint — área de trabalho e menus, criação de "
          "apresentações e slides, elementos da tela e modos de visualização, objetos de texto, listas e "
          "objetos de desenho, tabelas/gráficos/planilhas/organogramas, leiaute e slide mestre, animações, "
          "integração com Word e Excel."},
    {"t": "art", "n": "Informática — Redes de computadores",
     "x": "3. Redes de computadores: 3.1 Conceitos básicos, ferramentas, aplicativos e procedimentos de "
          "Internet e intranet, grupos de discussão, redes sociais, computação na nuvem, programas de "
          "navegação, deep web, dark web; 3.2 Correio eletrônico (endereços, recursos típicos); 3.3 "
          "Navegadores, sítios de busca e pesquisa na Internet; 3.4 Conceitos de segurança (procedimentos e "
          "segurança de acessos, programas maliciosos, antivírus, criptografia); 3.5 Procedimentos de "
          "backup, armazenamento de dados na nuvem.",
     "s": "Deep web e dark web estão explicitamente no programa — a banca costuma cobrar a diferença entre "
          "os dois termos."},
    {"t": "art", "n": "Raciocínio Lógico",
     "x": "1. Conjuntos numéricos: inteiros, racionais e reais. 2. Sistema legal de medidas. 3. Razões e "
          "proporções: 3.1 Divisão proporcional; 3.2 Regras de três simples e compostas; 3.3 Porcentagens. "
          "4. Equações e inequações de 1º e de 2º graus. 5. Sistemas lineares. 6. Funções e gráficos. 7. "
          "Princípios de contagem. 8. Progressões aritméticas e geométricas. 9. Compreensão de estruturas "
          "lógicas. 10. Lógica de argumentação: analogias, inferências, deduções e conclusões. 11. Lógica "
          "sentencial (ou proposicional): 11.1 Proposições simples e compostas; 11.2 Tabelas-verdade; 11.3 "
          "Equivalências; 11.4 Leis de De Morgan; 11.5 Diagramas lógicos. 12. Lógica de primeira ordem. 13. "
          "Princípios de contagem e probabilidade. 14. Operações com conjuntos. 15. Raciocínio lógico "
          "envolvendo problemas aritméticos, geométricos e matriciais."},
    {"t": "art", "n": "Contabilidade Geral",
     "x": "1. Conceitos, objetivos e finalidades da contabilidade. 2. Patrimônio: componentes, equação "
          "fundamental do patrimônio, situação líquida, representação gráfica. 3. Atos e fatos "
          "administrativos: conceitos, fatos permutativos, modificativos e mistos. 4. Contas: conceitos, "
          "contas de débitos, contas de créditos e saldos. 5. Plano de contas: conceitos, elenco de contas, "
          "função e funcionamento das contas. 6. Escrituração: conceitos, lançamentos contábeis, elementos "
          "essenciais, fórmulas de lançamentos, livros de escrituração, métodos e processos, regime de "
          "competência e regime de caixa. 7. Contabilização de operações contábeis diversas: juros, "
          "descontos, tributos, aluguéis, variação monetária/cambial, folha de pagamento, compras, vendas e "
          "provisões, depreciações e baixa de bens. 8. Balancete de verificação: conceitos, modelos e "
          "técnicas de elaboração. 9. Balanço patrimonial: conceitos, objetivo, composição. 10. "
          "Demonstração de resultado de exercício: conceito, objetivo, composição. 11. Normas Brasileiras "
          "de Contabilidade."},
    {"t": "art", "n": "Estatística",
     "x": "1. Estatística descritiva e análise exploratória de dados: gráficos, diagramas, tabelas, "
          "medidas descritivas (posição, dispersão, assimetria e curtose). 2. Probabilidade: 2.1 Definições "
          "básicas e axiomas; 2.2 Probabilidade condicional e independência. 3. Técnicas de amostragem: 3.1 "
          "Amostragem aleatória simples, estratificada, sistemática e por conglomerados; 3.2 Tamanho "
          "amostral."},
    {"t": "art", "n": "Atualidades (somente para a prova discursiva)",
     "x": "1. Tópicos relevantes e atuais na área de segurança pública.",
     "s": "Único item do programa que NÃO cai na prova objetiva — só entra na discursiva/redação."},
]

array_literal = '[\n' + ',\n'.join(json.dumps(it, ensure_ascii=False) for it in ITEMS) + '\n]'

m = re.search(r'const LAW_PE_ESTATUTO_POLICIAL\s*=\s*\[[\s\S]*?\n\];', html)
assert m, "bloco LAW_PE_ESTATUTO_POLICIAL nao encontrado"
insertion_point = m.end()

new_block = '\n\nconst PROGRAMA_PCPE_AGENTE = ' + array_literal + ';'
new_html = html[:insertion_point] + new_block + html[insertion_point:]

old_deck_block = ('const ESTRATEGIA_DECKS = {\n'
                   '  cronograma_pcpe: { label: "Edital e Cronograma — PC-PE (Pernambuco), Agente de '
                   'Polícia", data: CRONOGRAMA_PCPE, corp: "PCPE" },\n'
                   '  constituicao_pe: { label: "Constituição de PE (trechos) — Segurança Pública e '
                   'Administração", data: LAW_PE_CONSTITUICAO, corp: "PCPE" },\n'
                   '  estatuto_policial_pe: { label: "Estatuto do Policial Civil de PE (Lei 6.425/1972)", '
                   'data: LAW_PE_ESTATUTO_POLICIAL, corp: "PCPE" }\n'
                   '};')
assert old_deck_block in new_html, "bloco ESTRATEGIA_DECKS nao encontrado como esperado"
new_deck_block = ('const ESTRATEGIA_DECKS = {\n'
                   '  programa_pcpe: { label: "Conteúdo Programático Oficial — PC-PE Agente de Polícia '
                   '(Edital 2026)", data: PROGRAMA_PCPE_AGENTE, corp: "PCPE" },\n'
                   '  cronograma_pcpe: { label: "Edital e Cronograma — PC-PE (Pernambuco), Agente de '
                   'Polícia", data: CRONOGRAMA_PCPE, corp: "PCPE" },\n'
                   '  constituicao_pe: { label: "Constituição de PE (trechos) — Segurança Pública e '
                   'Administração", data: LAW_PE_CONSTITUICAO, corp: "PCPE" },\n'
                   '  estatuto_policial_pe: { label: "Estatuto do Policial Civil de PE (Lei 6.425/1972)", '
                   'data: LAW_PE_ESTATUTO_POLICIAL, corp: "PCPE" }\n'
                   '};')
new_html = new_html.replace(old_deck_block, new_deck_block, 1)

assert 'state.estrategiaDeck = "cronograma_pcpe";' in new_html
new_html = new_html.replace('state.estrategiaDeck = "cronograma_pcpe";',
                             'state.estrategiaDeck = "programa_pcpe";', 1)

with open('app-template.html', 'w', encoding='utf-8', newline='') as f:
    f.write(new_html)
print('PROGRAMA_PCPE_AGENTE adicionada com', len(ITEMS), 'itens; registrada em ESTRATEGIA_DECKS (primeiro deck).')

with open('questions.json', encoding='utf-8') as f:
    qdata = f.read()
with open('app-template.html', encoding='utf-8') as f:
    html2 = f.read()
html2 = html2.replace('__QUESTIONS_JSON__', qdata)
with open('estudo-cebraspe-ma.html', 'w', encoding='utf-8') as f:
    f.write(html2)
print('estudo-cebraspe-ma.html regenerado com sucesso')
