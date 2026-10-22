# -*- coding: utf-8 -*-
# Adiciona um novo deck de leitura na aba Estrategia com trechos
# selecionados (ja filtrados para a redacao VIGENTE, descartando
# paragrafos/incisos revogados ou substituidos por emendas) da
# Constituicao do Estado de Pernambuco: Titulo I (Principios
# Fundamentais) e Titulo IV (Administracao Publica, Servidores
# Publicos, Militares do Estado e Sistema de Seguranca Publica) --
# os topicos mais cobrados em prova para o cargo de Agente de
# Policia da PC-PE, conforme escopo escolhido pelo usuario.
import re
import json

with open('app-template.html', encoding='utf-8') as f:
    html = f.read()

ITEMS = [
    {"t": "tit", "x": "CONSTITUIÇÃO DO ESTADO DE PERNAMBUCO — TRECHOS SELECIONADOS (PC-PE)"},
    {"t": "art", "n": "Sobre este resumo",
     "x": "Este resumo reúne apenas os trechos mais cobrados em prova para o cargo de Agente de Polícia da "
          "PC-PE: Princípios Fundamentais, Administração Pública, Servidores Públicos, Militares do Estado "
          "e Sistema de Segurança Pública. É um recorte da Constituição de Pernambuco (promulgada em "
          "5/10/1989), já filtrado para trazer apenas a redação vigente — artigos e parágrafos revogados ou "
          "substituídos por emendas constitucionais foram descartados. Não é a Constituição completa.",
     "s": "Pernambuco já teve dezenas de Emendas Constitucionais até 2023 — muita coisa mudou de número, de "
          "nome de capítulo e de redação. Fique atento à data da emenda mais recente citada entre "
          "parênteses: ela indica a redação que está valendo hoje."},

    {"t": "cap", "x": "TÍTULO I — DOS PRINCÍPIOS FUNDAMENTAIS"},
    {"t": "art", "n": "Art. 1º",
     "x": "Pernambuco, parte integrante da República Federativa do Brasil, é um Estado Constitucional e "
          "Democrático de Direito, tendo como valores supremos a liberdade, a justiça, o pluralismo "
          "político, a dignidade da pessoa humana e os valores sociais do trabalho e da livre iniciativa."},
    {"t": "art", "n": "Art. 2º",
     "x": "O território do Estado é o da antiga Província. Parágrafo único: Recife é a Capital do Estado de "
          "Pernambuco."},
    {"t": "art", "n": "Art. 3º",
     "x": "São símbolos estaduais a bandeira, o escudo e o hino em uso no Estado. § 1º A bandeira é a "
          "idealizada pelos mártires da Revolução Republicana de 1817, hasteada pela primeira vez em 2 de "
          "abril de 1817. § 2º O escudo é o instituído pela Lei nº 75, de 21 de maio de 1895. § 3º O hino é "
          "o guardado pela tradição."},
    {"t": "art", "n": "Art. 4º",
     "x": "Incluem-se entre os bens do Estado (redação da EC 9/1995): I - as águas superficiais ou "
          "subterrâneas, fluentes, emergentes ou em depósito, ressalvadas as decorrentes de obras da "
          "União; II - as áreas nas ilhas oceânicas e costeiras sob seu domínio, incluído o Arquipélago de "
          "Fernando de Noronha, excluídas as sob domínio da União, Municípios ou terceiros; III - as ilhas "
          "fluviais e lacustres não pertencentes à União; IV - as terras devolutas não compreendidas entre "
          "as da União; V - os bens que atualmente lhe pertencem e os que vierem a ser atribuídos. § 1º Os "
          "bens imóveis do Estado, desafetados do uso público, só podem ser alienados, aforados ou cedidos "
          "em virtude de lei específica. § 2º A cessão de uso de bens imóveis do Estado observará limite de "
          "prazo fixado em lei específica, e sua renovação dependerá de nova lei.",
     "s": "O antigo parágrafo único de 1989 foi suprimido pela EC 9/1995 e virou dois parágrafos (§1º e "
          "§2º) com regras mais detalhadas — cuidado com questões que citem a redação original de 1989."},

    {"t": "cap", "x": "TÍTULO IV, CAPÍTULO I — DOS PRINCÍPIOS DA ADMINISTRAÇÃO (Art. 97)"},
    {"t": "art", "n": "Art. 97, caput",
     "x": "A administração pública direta e indireta de qualquer dos Poderes do Estado e dos Municípios "
          "obedecerá aos princípios de legalidade, impessoalidade, moralidade, publicidade e eficiência "
          "(redação da EC 16/1999, que acrescentou 'eficiência' à redação de 1989), além dos relacionados "
          "nos arts. 37 e 38 da CF e dos incisos deste artigo."},
    {"t": "art", "n": "Art. 97, I a V",
     "x": "I - publicidade dos atos legislativos e administrativos para que produzam efeitos, mediante "
          "publicação no órgão oficial do Estado ou do Município (ou jornal local), com regra especial de "
          "publicação em três vezes, ao menos, para edital de concorrência pública; II - prazos legais para "
          "atos administrativos, com recursos e efeitos definidos; III - obrigatoriedade de prestação de "
          "contas por quem recebe dinheiro público; IV - certidão de atos/contratos/decisões em até quinze "
          "dias, sob pena de responsabilização do agente; V - inexistência de limite de idade do servidor "
          "estadual/municipal em atividade para concurso, ressalvada a legislação militar."},
    {"t": "art", "n": "Art. 97, VI",
     "x": "Reserva de vagas em concurso público para pessoas com deficiência: desde a EC 40/2016, o "
          "percentual passou de 3% (mínimo de 1 vaga) para 5% das vagas em concursos públicos e seleções "
          "públicas simplificadas, observada habilitação técnica e critérios de edital.",
     "s": "Pegadinha clássica: antes da EC 40/2016 o texto de PE previa 3% — se a questão citar '3%' como "
          "regra atual de PE, está desatualizada. Hoje é 5%."},
    {"t": "art", "n": "Art. 97, VII a XIII",
     "x": "VII - contratação de pessoal por prazo determinado, na forma e casos da lei, para necessidade "
          "temporária de excepcional interesse público (a partir da EC 16/1999, sem o limite fixo de 1 ano "
          "que existia na redação original); VIII - extensão da proibição de acumular cargos/empregos/"
          "funções a autarquias, empresas públicas, sociedades de economia mista e fundações; IX - vedação "
          "de servidores da administração direta/indireta estadual participarem do produto da arrecadação "
          "de tributos; X - proibição de usar, em publicidade/comunicados/bens públicos, marcas ou símbolos "
          "que não sejam os oficiais do Estado/Município; XI - pagamento pelo Estado e Municípios, com "
          "correção monetária, de valores atrasados devidos a servidores; XII - preparação profissional de "
          "quem atua na Justiça de menores e delegacias especializadas; XIII - proibição de incorporar a "
          "vencimentos/proventos gratificações de cargo comissionado ou função de confiança."},
    {"t": "art", "n": "Art. 97, § 1º e § 2º",
     "x": "§ 1º Só por lei específica pode ser criada autarquia, e só por lei específica pode ser autorizada "
          "a instituição de empresa pública, sociedade de economia mista e fundação — cabendo à lei "
          "complementar definir as áreas de atuação da fundação. § 2º Estado e Municípios disciplinarão "
          "por lei os consórcios públicos e convênios de cooperação entre entes federados, autorizando "
          "gestão associada de serviços públicos e transferência de encargos, serviços, pessoal e bens."},
    {"t": "art", "n": "Art. 97, § 6º",
     "x": "Fixa o subteto remuneratório do funcionalismo de PE (Judiciário, Legislativo, Executivo, MP e "
          "TCE): o subsídio mensal dos desembargadores do TJPE, limitado a 90,25% do subsídio mensal dos "
          "ministros do STF — não se aplica a deputados estaduais e vereadores. A expressão 'e Municípios' "
          "foi declarada inconstitucional pelo STF na ADI 6811/2021.",
     "s": "Cuidado: o STF retirou a extensão do subteto aos Municípios desse parágrafo específico — não "
          "confundir com a regra geral do art. 37, XI, da CF, que continua valendo para Municípios por "
          "outra via."},

    {"t": "cap", "x": "TÍTULO IV, CAPÍTULO II — DOS SERVIDORES PÚBLICOS (Art. 98-99)"},
    {"t": "art", "n": "Art. 98, caput",
     "x": "São direitos dos servidores públicos da administração direta, autárquica e fundacional, "
          "ocupantes de cargo público, os assegurados no art. 39, § 3º, da Constituição Federal, além de "
          "outros do Estatuto próprio (redação da EC 16/1999).",
     "s": "O capítulo mudou de nome: era 'Dos Servidores Públicos Civis' e virou só 'Dos Servidores "
          "Públicos' pela EC 16/1999 — questão pode testar esse detalhe de nomenclatura."},
    {"t": "art", "n": "Art. 98, incisos I a XVI",
     "x": "Lista de direitos equivalentes aos do art. 7º da CF, na redação da EC 16/1999: I - salário "
          "mínimo nacionalmente unificado; II - irredutibilidade de vencimento/subsídio; III - salário/"
          "benefício de prestação continuada nunca inferior ao mínimo; IV - décimo terceiro salário; V - "
          "remuneração do trabalho noturno superior ao diurno; VI - salário-família; VII - jornada de até "
          "8h diárias/44h semanais, com compensação por interesse público ou acordo coletivo; VIII - "
          "repouso semanal remunerado, preferencialmente aos domingos; IX - hora extra com acréscimo "
          "mínimo de 50%; X - férias anuais com pelo menos 1/3 a mais da remuneração normal; XI - "
          "licença-gestante de 120 dias; XII - licença-paternidade na forma da lei; XIII - proteção do "
          "mercado de trabalho da mulher; XIV - redução de riscos do trabalho por normas de saúde/higiene/"
          "segurança; XV - proibição de diferença salarial ou de critério de admissão por sexo, idade, cor "
          "ou estado civil; XVI - reversão ao serviço ativo na forma da lei.",
     "s": "O inciso XVII original (estabilidade financeira de gratificação por 5 anos ininterruptos) foi "
          "declarado inconstitucional pelo STF em 1998 — não existe mais."},
    {"t": "art", "n": "Art. 98, § 1º a § 5º",
     "x": "§ 1º Estabilidade após 3 anos de efetivo exercício em cargo de provimento efetivo via concurso, "
          "condicionada a avaliação especial de desempenho por comissão própria. § 2º O servidor estável só "
          "perde o cargo por: I - sentença transitada em julgado; II - processo administrativo com ampla "
          "defesa; III - avaliação periódica de desempenho (lei complementar), com ampla defesa. § 3º "
          "Demissão de estável invalidada por sentença: reintegração, com o eventual ocupante da vaga (se "
          "estável) reconduzido, aproveitado em outro cargo, ou posto em disponibilidade proporcional ao "
          "tempo de serviço. § 4º Cargo extinto ou desnecessário: servidor estável fica em disponibilidade "
          "com remuneração proporcional até aproveitamento em outro cargo. § 5º Servidor investido em "
          "mandato de vereador ou vice-prefeito tem assegurado exercício funcional em órgão situado no "
          "município do seu domicílio eleitoral, respeitada a compatibilidade de horário."},
    {"t": "art", "n": "Art. 99",
     "x": "Na redação vigente (EC 16/1999), o art. 99 é bem mais enxuto que o original de 1989: 'O Estado e "
          "os Municípios instituirão conselho de política de administração e remuneração de pessoal, "
          "integrado por servidores designados pelos respectivos Poderes.' Todos os incisos antigos (I a "
          "IV, sobre proteção ao mercado de trabalho, exercício funcional de vereador etc.) foram "
          "suprimidos.",
     "s": "Pegadinha: se a questão citar os antigos incisos I-IV do art. 99 como se fossem texto vigente, "
          "está errada — foram todos suprimidos pela EC 16/1999."},

    {"t": "cap", "x": "TÍTULO IV, CAPÍTULO III — DOS MILITARES DO ESTADO (Art. 100)"},
    {"t": "art", "n": "Art. 100, caput",
     "x": "São Militares do Estado os membros da Polícia Militar de Pernambuco e do Corpo de Bombeiros "
          "Militar (redação da EC 16/1999).",
     "s": "O capítulo também mudou de nome: 'Dos Servidores Públicos Militares' virou 'Dos Militares do "
          "Estado' pela EC 16/1999 — mesmo padrão de mudança de nomenclatura do Capítulo II."},
    {"t": "art", "n": "Art. 100, § 1º a § 4º",
     "x": "§ 1º Patentes com prerrogativas/direitos/deveres são asseguradas em plenitude aos oficiais da "
          "ativa, reserva ou reformados, conferidas pelo Governador. § 2º São privativos dos militares os "
          "títulos, postos, graduações, uniformes, insígnias e distintivos militares. § 3º Militar da ativa "
          "empossado em cargo público civil permanente é transferido para a reserva. § 4º Militar da ativa "
          "que aceita cargo/emprego/função pública temporária não eletiva fica agregado ao quadro, só pode "
          "ser promovido por antiguidade (contando o tempo só para essa promoção e para a transferência à "
          "reserva), e é transferido para a inatividade após 2 anos de afastamento (contínuos ou não)."},
    {"t": "art", "n": "Art. 100, § 5º e § 6º",
     "x": "§ 5º O oficial da Polícia Militar OU do Corpo de Bombeiros Militar só perde o posto e a patente "
          "se julgado indigno do oficialato (ou incompatível com ele) por decisão do Tribunal de Justiça "
          "Militar (quando existir) ou do Tribunal de Justiça do Estado, cabendo à lei especificar os casos "
          "de submissão a processo e o rito (redação da EC 4/1994, que estendeu a regra — antes só da PM — "
          "também ao Corpo de Bombeiros). § 6º O oficial condenado (Justiça comum ou militar) a pena "
          "privativa de liberdade superior a 2 anos, com trânsito em julgado, é submetido a esse mesmo "
          "julgamento."},
    {"t": "art", "n": "Art. 100, § 7º a § 14",
     "x": "§ 7º Vedadas ao militar a sindicalização e a greve; proibida filiação partidária enquanto em "
          "efetivo exercício. § 8º O Estado promove post mortem o militar morto em luta contra malfeitores, "
          "em operações de manutenção da ordem pública, na prevenção/combate a incêndios, em operações de "
          "salvamento de pessoas e bens ou de defesa civil, ou por acidente/moléstia decorrente desses "
          "fatos (redação da EC 4/1994, que incluiu expressamente o combate a incêndio e o salvamento, "
          "cobrindo também o Corpo de Bombeiros). § 9º Pensão especial aos beneficiários do militar "
          "falecido nessas circunstâncias, igual à remuneração do posto/graduação da promoção post mortem. "
          "§ 10 Promoções por merecimento e antiguidade, conforme legislação própria (a palavra "
          "'alternadamente' foi retirada pela EC 8/1995). § 11 Lei disporá sobre limites de idade, "
          "estabilidade e condições de transferência para a inatividade. § 12 Aplicam-se aos militares (e, "
          "no que couber, a seus pensionistas) os §§ 7º e 8º do art. 40 da CF. § 13 Aplicam-se também aos "
          "militares os arts. 14, §8º; 37, XI; 40, §9º; 42, §§1º e 2º; 142, §§2º e 3º da CF, e o art. 171, "
          "§§4º, 6º a 12, desta Constituição estadual. § 14 Posto à disposição, o militar é considerado no "
          "exercício de função militar quando ocupar cargo em comissão ou função de confiança declarados "
          "em lei de natureza policial militar ou de bombeiro militar."},

    {"t": "cap", "x": "TÍTULO IV, CAPÍTULO IV — DO SISTEMA DE SEGURANÇA PÚBLICA (Art. 101 a 105-B)"},
    {"t": "art", "n": "Art. 101",
     "x": "A Segurança Pública, dever do Estado, direito e responsabilidade de todos, é exercida para "
          "preservar a ordem pública, a incolumidade das pessoas e do patrimônio, e assegurar a liberdade e "
          "as garantias individuais, através dos seguintes órgãos permanentes: I - Polícia Civil; II - "
          "Polícia Militar; III - Corpo de Bombeiros Militar (acrescido pela EC 4/1994); IV - Polícia "
          "Penal, vinculada ao órgão administrador do sistema penal (acrescido pela EC 53/2020). § 1º As "
          "atividades de Segurança Pública serão organizadas em sistema, na forma da lei. § 2º Cabe ao "
          "Governador do Estado, assessorado por um Conselho de Defesa Social, estabelecer a política de "
          "defesa social e coordenar as ações de Segurança Pública.",
     "s": "A redação original de 1989 só tinha Polícia Civil e Polícia Militar como órgãos de segurança — "
          "Corpo de Bombeiros Militar entrou em 1994 e Polícia Penal só em 2020. São 4 órgãos permanentes "
          "hoje, não 2."},
    {"t": "art", "n": "Art. 102",
     "x": "A Polícia Civil, a Polícia Militar e o Corpo de Bombeiros Militar, integrantes da Secretaria de "
          "Estado responsável pela defesa social, e a Polícia Penal, vinculada ao órgão administrador do "
          "sistema penal, regular-se-ão por estatutos próprios que estabelecerão organização, garantias, "
          "direitos e deveres de seus integrantes, estruturando-os em carreira, tendo por princípio a "
          "hierarquia e a disciplina (redação da EC 53/2020).",
     "s": "Note a mudança de subordinação ao longo do tempo: em 1989 eram 'diretamente subordinadas ao "
          "Governador'; pela EC 15/1999 passaram a ser 'integrantes da Secretaria de Estado responsável "
          "pela defesa social' — hoje a subordinação formal é à Secretaria, não direto ao Governador."},
    {"t": "art", "n": "Art. 103",
     "x": "À Polícia Civil, dirigida por Delegado de Polícia do último nível da carreira, incumbem "
          "privativamente (ressalvada a competência da União): I - funções de Polícia Judiciária e "
          "apuração de infrações penais, exceto as militares; II - repressão da criminalidade. § 1º Lei "
          "complementar (prevista no art. 18, parágrafo único, VII) cria órgãos específicos para: a) "
          "perícias criminais, médico-legais e identificação civil/criminal; b) apuração de atos "
          "infracionais de menores; c) vistoria/matrícula de veículos e exames de habilitação de "
          "condutores. § 2º O órgão de perícias (letra 'a') tem plena independência técnico-científica, "
          "dirigido privativamente por médico-legista ou perito-criminal do último nível da carreira, com "
          "participação obrigatória no Conselho de Defesa Social. § 3º A direção do órgão de identificação "
          "civil/criminal é de livre escolha do Governador entre ocupantes de cargo de nível superior do "
          "quadro policial civil.",
     "s": "A Polícia Civil tem reserva de matéria para lei complementar estadual (art. 18, VII) — isso é "
          "cobrado junto com o art. 103."},
    {"t": "art", "n": "Art. 103, § 5º",
     "x": "O cargo de Delegado de Polícia Civil, privativo de bacharel em Direito, integra as carreiras "
          "jurídicas típicas de Estado (acrescido pela EC 39/2014).",
     "s": "Ponto de prova clássico: Delegado de Polícia é expressamente reconhecido como carreira jurídica "
          "típica de Estado na Constituição de PE."},
    {"t": "art", "n": "Art. 104",
     "x": "À Polícia Penal, vinculada ao órgão administrador do sistema penal de PE, cabe a segurança dos "
          "estabelecimentos penais (redação da EC 53/2020, que substituiu o texto original de 1989 sobre "
          "'manutenção da ordem e segurança interna dos estabelecimentos penais'). § 1º O quadro de "
          "servidores da Polícia Penal é preenchido exclusivamente por concurso público e por "
          "transformação do cargo de Agente de Segurança Penitenciária (Grupo Ocupacional Segurança "
          "Penitenciária de PE). § 2º Organização e funcionamento da Polícia Penal serão definidos em lei."},
    {"t": "art", "n": "Art. 105",
     "x": "À Polícia Militar, força auxiliar e reserva do Exército, cabe com exclusividade a polícia "
          "ostensiva e a preservação da ordem pública; ao Corpo de Bombeiros Militar, também força auxiliar "
          "e reserva do Exército, cabe a execução das atividades de defesa civil, além de outras "
          "atribuições definidas em lei (redação da EC 4/1994, que separou PM e Bombeiros em frases "
          "distintas e reconheceu o Bombeiro Militar também como força auxiliar e reserva do Exército). "
          "Parágrafo único: Os Comandantes Gerais da Polícia Militar e do Corpo de Bombeiros Militar são "
          "nomeados em comissão pelo Governador, entre oficiais da ativa do último posto de cada "
          "corporação.",
     "s": "Tanto a PM quanto o Corpo de Bombeiros Militar de PE são força auxiliar e reserva do Exército — "
          "isso vale para os dois, não só para a PM."},
    {"t": "art", "n": "Art. 105-A",
     "x": "Os municípios poderão constituir guardas municipais destinadas à prevenção, proteção e "
          "preservação de seus bens, serviços e instalações, observados os preceitos da Lei Federal "
          "(acrescido pela EC 42/2018)."},
    {"t": "art", "n": "Art. 105-B",
     "x": "A segurança viária, exercida para a preservação da ordem pública e da incolumidade das pessoas e "
          "do patrimônio nas vias públicas (acrescido pela EC 54/2020): I - compreende educação, "
          "engenharia e fiscalização de trânsito, entre outras, assegurando ao cidadão o direito à "
          "mobilidade urbana eficiente; II - compete, no âmbito do Estado e dos Municípios, aos respectivos "
          "órgãos executivos de trânsito e seus agentes, estruturados em carreira, na forma da lei."},
]

array_literal = '[\n' + ',\n'.join(json.dumps(it, ensure_ascii=False) for it in ITEMS) + '\n]'

m = re.search(r'const CRONOGRAMA_PCPE\s*=\s*\[[\s\S]*?\n\];', html)
assert m, "bloco CRONOGRAMA_PCPE nao encontrado"
insertion_point = m.end()

new_block = '\n\nconst LAW_PE_CONSTITUICAO = ' + array_literal + ';'
new_html = html[:insertion_point] + new_block + html[insertion_point:]

old_deck_block = ('const ESTRATEGIA_DECKS = {\n'
                   '  cronograma_pcpe: { label: "Edital e Cronograma — PC-PE (Pernambuco), Agente de '
                   'Polícia", data: CRONOGRAMA_PCPE, corp: null }\n'
                   '};')
assert old_deck_block in new_html, "bloco ESTRATEGIA_DECKS nao encontrado como esperado"
new_deck_block = ('const ESTRATEGIA_DECKS = {\n'
                   '  cronograma_pcpe: { label: "Edital e Cronograma — PC-PE (Pernambuco), Agente de '
                   'Polícia", data: CRONOGRAMA_PCPE, corp: null },\n'
                   '  constituicao_pe: { label: "Constituição de PE (trechos) — Segurança Pública e '
                   'Administração", data: LAW_PE_CONSTITUICAO, corp: null }\n'
                   '};')
new_html = new_html.replace(old_deck_block, new_deck_block, 1)

with open('app-template.html', 'w', encoding='utf-8', newline='') as f:
    f.write(new_html)
print('LAW_PE_CONSTITUICAO adicionada com', len(ITEMS), 'itens; registrada em ESTRATEGIA_DECKS.')

with open('questions.json', encoding='utf-8') as f:
    qdata = f.read()
with open('app-template.html', encoding='utf-8') as f:
    html2 = f.read()
html2 = html2.replace('__QUESTIONS_JSON__', qdata)
with open('estudo-cebraspe-ma.html', 'w', encoding='utf-8') as f:
    f.write(html2)
print('estudo-cebraspe-ma.html regenerado com sucesso')
