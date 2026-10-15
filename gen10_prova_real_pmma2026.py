# -*- coding: utf-8 -*-
# Adiciona ao banco as questoes da PROVA REAL CEBRASPE - PMMA, Edital 2026
# (fornecida pelo usuario em PDF, 120 itens: Conhecimentos Gerais 1-50,
# Conhecimentos Especificos 51-120). Cada questao e marcada como IDENTICA
# a prova real (nao e uma questao inedita de pratica), com nota de
# proveniencia no campo "exp" citando o numero do item original.
#
# IMPORTANTE: nao foi fornecido cartao-resposta oficial. O gabarito abaixo
# e um julgamento proprio (C/E), feito com base em conhecimento linguistico,
# historico, geografico, logico, de informatica e no texto das Leis
# 6.513/95, 12.896/2026 e 14.751/2023 ja lidas integralmente neste app.
# Alguns itens (historia/geografia muito especificos, dados de censo
# recentes) tem confianca menor e estao marcados com "CONF: baixa" no
# comentario do script (nao aparece no app) para revisao futura.
#
# Alem disso, os itens 66-75 (Lei 14.751/2023, expressamente "PM e BM")
# ganham uma versao ADAPTADA em multipla escolha para o corp BM, seguindo
# o padrao MC ja usado para esse corp.
import json

with open('questions.json', encoding='utf-8') as f:
    raw = f.read()

data_check = json.loads(raw)
max_id = max(q['id'] for q in data_check)
assert max_id == 826, max_id

FONTE = lambda n: f" Questão idêntica ao item {n} da Prova CEBRASPE – PMMA, Edital 2026 (gabarito próprio do app; não há cartão-resposta oficial anexado)."

PM_CE = []  # (disc, enun, resp_bool, exp, item_num)

def ce(disc, enun, resp, exp, n):
    PM_CE.append((disc, enun, resp, exp, n))

LP = "Língua Portuguesa"
HB = "História do Brasil"
HM = "História do Maranhão"
GB = "Geografia do Brasil"
GM = "Geografia do Maranhão"
RL = "Raciocínio Lógico"
EST = "Estatuto da PM/MA (Lei 6.513/95)"
L12896 = "Lei 12.896/2026 (Organização Básica da PMMA)"
L14751 = "Lei 14.751/2023 (Nacional — PM e BM)"
INFO = "Noções de Informática"

TEXTO_MOBILIDADE = ('Texto-base: "Mobilidade urbana é um tema constantemente discutido no Brasil. ... '
    'Uma das causas do aumento de engarrafamentos é bem óbvia: há mais carros nas ruas. O investimento '
    'no desenvolvimento da indústria automobilística facilitou o acesso a veículos particulares, o que '
    'deixou as vias públicas sobrecarregadas. Na contramão, não houve — e continua não havendo — '
    'programas de incentivo ao transporte público, coletivo, mais econômico. Para explicitar o '
    'contrassenso, basta observar as cidades pelo mundo em que o transporte público é prioridade... '
    'enquanto aqui, pelo contrário, a infraestrutura é inadequada, os veículos são velhos, a malha de '
    'atendimento é ainda restrita; tudo isso dificulta o uso desses modais como prioridade pela '
    'população. Grande parte dessa realidade vem da falta de interesse governamental em estabelecer '
    'programas de desenvolvimento que contemplem a mobilidade urbana sustentável." (Janguiê Diniz, '
    'Mobilidade urbana também é democratização, 2019, com adaptações). ')

TEXTO_TIETE = ('Texto-base: "O rio Tietê não tem nenhum trecho plenamente livre de contaminação... '
    'As análises mostram que o rio tem múltiplas camadas simultâneas de contaminação: microbiológica, '
    'química, farmacológica, plástica, agrícola e orgânica... foram identificados microplásticos em '
    'todos os pontos analisados, além de 25 tipos de agrotóxicos e 16 substâncias entre fármacos e '
    'drogas ilícitas. A expedição mostrou que o problema vai além dos centros urbanos. \'Sempre se tem '
    'a ideia de que só esgoto é o problema do nosso rio, e esse estudo mostra que é muito mais complexo '
    'que isso\', disse Gustavo Veronesi... \'mesmo em áreas bem protegidas e bem cuidadas, como é o caso '
    'do Parque da Nascente do Tietê, a gente pode ter interferência das ações humanas na vizinhança.\'" '
    '(Camila Boehm, Rio Tietê não tem trecho livre de contaminação, 2026, com adaptações). ')

CENARIO_WORD_EXCEL = ('Considere que, durante seu turno de serviço em uma unidade da PMMA, o soldado '
    'Almeida ficou responsável por atividades administrativas de registro de ocorrências, utilizando o '
    'Microsoft Word para elaborar um relatório diário e o Microsoft Excel para atualizar uma planilha '
    'com número da ocorrência, natureza, local, horário, equipe responsável e quantidade de pessoas '
    'abordadas. ')

# ===================== CONHECIMENTOS GERAIS (1-50) =====================

ce(LP, TEXTO_MOBILIDADE + 'No trecho "a infraestrutura é inadequada, os veículos são velhos, a malha de '
   'atendimento é ainda restrita; tudo isso dificulta o uso desses modais como prioridade pela '
   'população", o ponto e vírgula empregado logo após "restrita" delimita a enumeração relacionada à '
   'expressão "tudo isso", que sintetiza as três constatações enumeradas anteriormente.', True,
   'O ponto e vírgula fecha a enumeração das três constatações (infraestrutura, veículos, malha de '
   'atendimento), retomadas em bloco por "tudo isso" na oração seguinte.', 1)

ce(LP, TEXTO_MOBILIDADE + 'No trecho "Na contramão, não houve — e continua não havendo — programas de '
   'incentivo ao transporte público", a substituição das formas verbais "houve" e "havendo" por '
   '"existiu" e "existindo", respectivamente, preservaria a correção gramatical e o sentido do texto.',
   False, 'Errado. "Haver" existencial é impessoal (fica sempre no singular); já "existir" é pessoal e '
   'concordaria com o sujeito plural "programas", exigindo "existiram", e não "existiu" — a '
   'substituição proposta quebraria a concordância.', 2)

ce(LP, TEXTO_MOBILIDADE + 'O texto caracteriza-se como predominantemente narrativo, o que se evidencia '
   'pela sequência de acontecimentos relacionados ao desenvolvimento do transporte urbano e à ampliação '
   'do número de veículos particulares.', False,
   'Errado. O texto é predominantemente dissertativo-argumentativo (defende uma tese sobre a falta de '
   'incentivo ao transporte público), e não narrativo.', 3)

ce(LP, TEXTO_MOBILIDADE + 'O autor do texto sustenta que o aumento do número de veículos particulares '
   'contribuiu para o agravamento dos problemas de mobilidade urbana no Brasil, bem como critica a '
   'insuficiência de iniciativas governamentais de valorização do transporte público.', True,
   'Correto — é exatamente a tese defendida no texto.', 4)

ce(LP, TEXTO_MOBILIDADE + 'No trecho "enquanto aqui, pelo contrário, a infraestrutura é inadequada, os '
   'veículos são velhos, a malha de atendimento é ainda restrita", a conjunção "enquanto" estabelece '
   'uma relação temporal entre a situação do transporte público no Brasil e a de outros países.', False,
   'Errado. Aqui "enquanto" tem valor adversativo/contrastivo (equivale a "ao passo que"), e não '
   'temporal.', 5)

ce(LP, TEXTO_MOBILIDADE + 'No trecho "o que deixou as vias públicas sobrecarregadas", o termo '
   '"sobrecarregadas" poderia ser deslocado para imediatamente após "deixou", sem alteração dos '
   'sentidos e das relações sintáticas originalmente estabelecidas.', True,
   'Correto. Em "deixou sobrecarregadas as vias públicas", o predicativo do objeto apenas muda de '
   'posição, sem alterar sentido ou função sintática.', 6)

ce(LP, TEXTO_MOBILIDADE + 'No trecho "as cidades pelo mundo em que o transporte público é prioridade", '
   'a oração "em que o transporte público é prioridade" caracteriza as cidades mencionadas e restringe '
   'seu sentido.', True,
   'Correto. É oração subordinada adjetiva restritiva, delimitando quais cidades (as que priorizam '
   'transporte público).', 7)

ce(LP, TEXTO_TIETE + 'De acordo com as informações veiculadas no texto, é correto afirmar que a '
   'proteção de áreas naturais, embora auxilie a preservação dos recursos hídricos, não impede '
   'completamente os efeitos de atividades humanas realizadas em seu entorno.', True,
   'Correto, conforme o depoimento citado sobre o Parque da Nascente do Tietê: mesmo em área protegida '
   'há interferência das ações humanas na vizinhança.', 8)

ce(LP, TEXTO_TIETE + 'No trecho "foram identificados microplásticos em todos os pontos analisados", a '
   'locução verbal "foram identificados" poderia ser substituída por "identificou-se", sem prejuízo da '
   'correção gramatical do texto.', False,
   'Errado. A voz passiva sintética deveria concordar no plural com "microplásticos" ("identificaram-'
   'se"), não no singular ("identificou-se").', 9)

ce(LP, TEXTO_TIETE + 'Depreende-se da leitura do texto que o esgoto nos grandes centros urbanos é a '
   'principal causa da contaminação do rio Tietê.', False,
   'Errado. O texto contesta exatamente essa ideia simplista, mostrando que a contaminação é muito mais '
   'complexa que apenas o esgoto urbano.', 10)

ce(LP, TEXTO_TIETE + 'No período "O rio Tietê não tem nenhum trecho plenamente livre de contaminação.", '
   'a substituição do vocábulo "plenamente" por "amplamente" manteria o sentido original do texto.',
   True, 'Correto; no contexto, ambos reforçam a ideia de ausência total/extensiva de trechos livres de '
   'contaminação, sem alterar a conclusão geral do texto.', 11)

ce(LP, TEXTO_TIETE + 'No trecho "Sempre se tem a ideia de que só esgoto é o problema do nosso rio, e '
   'esse estudo mostra que é muito mais complexo que isso", a conjunção "e" está empregada com sentido '
   'de oposição, contraste.', True,
   'Correto. O "e" liga duas ideias contrastantes (a ideia simplista vs. o que o estudo realmente '
   'mostra), com valor adversativo equivalente a "mas".', 12)

ce(LP, TEXTO_TIETE + 'Estariam mantidas a correção gramatical e a coerência do texto caso o trecho "da '
   'nascente em Salesópolis (SP) à foz no rio Paraná" fosse reescrito como "desde a nascente em '
   'Salesópolis (SP) até a foz no rio Paraná".', True,
   'Correto. "De...a" e "desde...até" são construções equivalentes para indicar trajeto, sem prejuízo '
   'de sentido ou correção.', 13)

ce(LP, TEXTO_TIETE + 'No segundo parágrafo, a palavra "simultâneas" tem o mesmo sentido de '
   '"concomitantes".', True, 'Correto; ambas indicam ocorrência ao mesmo tempo.', 14)

ce(LP, TEXTO_TIETE + 'No trecho "Ao longo de mais de 1,1 mil quilômetros", a flexão de plural no '
   'substantivo "quilômetros" justifica-se pela concordância que ele estabelece com o termo "mais".',
   False, 'Errado. "Mais" é advérbio/intensificador invariável e não concorda com substantivos; o '
   'plural de "quilômetros" decorre da quantidade ser superior a um (mais de 1,1 mil), não de '
   'concordância com "mais".', 15)

ce(HB, 'Nos anos finais do regime militar brasileiro, o sistema partidário foi reorganizado, o que '
   'permitiu o surgimento de novos partidos políticos.', True,
   'Correto. A Lei Orgânica dos Partidos de 1979 extinguiu o bipartidarismo (ARENA/MDB), permitindo o '
   'surgimento de PDS, PMDB, PT, PDT, PTB, entre outros.', 16)

ce(HB, 'O governo de João Goulart gozou de estabilidade política até março de 1964, quando a '
   'realização do Comício da Central do Brasil deu início à instabilidade que culminou na instauração '
   'do regime militar.', False,
   'Errado. O governo Goulart foi marcado por forte instabilidade desde 1961 (Crise da Legalidade, '
   'radicalização política); o Comício da Central do Brasil foi um ponto culminante dessa crise '
   'já instalada, não o início dela.', 17)

ce(HB, 'A Constituição de 1967 incorporou mecanismos que permitiam restringir direitos e garantias '
   'individuais previstos nela própria.', True,
   'Correto. A Carta de 1967 (e sua Emenda nº 1/1969) continha dispositivos de exceção (estado de '
   'sítio, atos institucionais incorporados) que permitiam suspender direitos nela mesma assegurados.',
   18)

ce(HB, 'Em 1945, entrou em vigor o decreto-lei conhecido como Lei Agamenon, por meio do qual o caráter '
   'nacional deixou de ser, pela primeira vez na história republicana brasileira, uma condição para '
   'registro de organizações partidárias.', False,
   'Errado. A Lei Agamenon (Decreto-Lei nº 7.586/1945) fez o oposto: instituiu a exigência de caráter '
   'nacional para o registro de partidos, buscando superar o regionalismo partidário anterior.', 19)

ce(HB, 'Foi no período da denominada Primeira República que se consolidou o tripé da industrialização '
   'brasileira, alicerçado nos capitais estatal, nacional privado e estrangeiro.', False,
   'Errado. Esse "tripé" é característico do período desenvolvimentista posterior (a partir dos anos '
   '1950), quando o capital estatal (ex.: Petrobras, siderurgia) passa a ter papel central; na Primeira '
   'República (1889-1930) o Estado teve papel industrial pouco expressivo.', 20)

ce(HB, 'No Brasil, o movimento político-cultural conhecido como integralismo resultou, entre outros '
   'efeitos, na estruturação de um partido político: a Ação Integralista Brasileira (AIB).', True,
   'Correto. A AIB, fundada por Plínio Salgado em 1932, foi a expressão partidária do integralismo '
   'brasileiro.', 21)

ce(HM, 'A expedição do francês Daniel de La Touche à ilha de Maragnan, feita com vistas à fundação de '
   'uma colônia protestante na região, representou uma das maiores ameaças ao domínio luso no norte do '
   'Brasil no período colonial.', False,
   'Errado. A França Equinocial (1612) foi um empreendimento de colonização católica patrocinado pela '
   'coroa francesa (com padres capuchinhos na expedição), ainda que La Touche/Ravardière fosse '
   'huguenote; não se tratou de um projeto de colônia protestante.', 22)

ce(HM, 'No século XVII, após a expulsão dos holandeses do território maranhense, a elite branca '
   'latifundiária local obteve sucesso na tentativa de transferir a capital do recém-criado estado do '
   'Maranhão para Caxias.', False,
   'Errado. São Luís permaneceu como capital; não houve transferência bem-sucedida da capital para '
   'Caxias nesse período.', 23)

ce(HM, 'A Batalha de Guaxenduba, liderada por Gaspar de Sousa, então governador-geral português do '
   'Brasil, marcou a expulsão dos franceses do território maranhense e assegurou a incorporação de um '
   'vasto território do norte aos domínios coloniais portugueses.', False,
   'Errado. A Batalha de Guaxenduba (1614) foi liderada por Jerônimo de Albuquerque, não por Gaspar de '
   'Sousa (que comandava a campanha a partir da Bahia, sem presença direta na batalha); a expulsão '
   'definitiva dos franceses só se consumou em 1615, com a rendição de São Luís.', 24)

ce(HM, 'A Revolta de Bequimão é considerada uma revolta nativista contra o monopólio estatal '
   'português, motivada especialmente pelo alto custo e pelas falhas no fornecimento de escravizados '
   'pela Companhia de Comércio do Maranhão.', True,
   'Correto. A Revolta de Beckman (1684) teve exatamente essas causas, voltando-se contra o monopólio '
   'comercial da Companhia de Comércio do Maranhão.', 25)

ce(HM, 'A cidade de São Luís foi formalmente instituída pelos franceses em 1615, sob a França '
   'equinocial, sendo marcos da presença francesa na região o Fort Saint-Louis e o Port Sainte-Marie '
   '(atual Praia Grande).', False,
   'Errado. São Luís foi fundada em 1612 (não 1615); em 1615 os franceses já haviam sido derrotados e '
   'expulsos pelos portugueses.', 26)

ce(HM, 'A Balaiada foi uma revolta predominantemente situada na região oriental do Maranhão, '
   'especialmente no Vale do Parnaíba, onde predominavam as formas privadas de uso da terra e residiam '
   'grandes proprietários de lavouras de algodão insatisfeitos com os altos impostos.', False,
   'Errado. A Balaiada (1838-1841) teve como protagonistas vaqueiros, sertanejos pobres e escravizados '
   'do interior maranhense, em revolta contra as elites locais — não foi um movimento liderado por '
   'grandes proprietários de algodão insatisfeitos com impostos.', 27)

ce(HM, 'Os "portugueses" do Maranhão, assim denominados pelas relações que mantinham com a '
   'administração lusa, apenas reconheceram a Independência do Brasil após Portugal tê-lo feito.',
   False, 'Errado. A adesão do Maranhão à Independência ocorreu em 1823, por meio da força naval '
   'liderada por Lord Cochrane, ANTES do reconhecimento português (que só veio em 1825).', 28)

ce(HM, 'A Batalha do Jenipapo, embora tenha acontecido no Piauí, contou com a participação de '
   'maranhenses e foi um evento importante para a expulsão do exército lusitano da região, razão pela '
   'qual foi integrada aos marcos da memória da Independência do Brasil.', True,
   'Correto. A Batalha do Jenipapo (1823) contou com patriotas maranhenses e piauienses e é lembrada '
   'como marco da Independência na região.', 29)

ce(HM, 'O caráter público e efusivo da cerimônia que marcou a adesão do Maranhão ao Império do Brasil '
   'expressou o sucesso do projeto da elite local interessada em romper os vínculos administrativos e '
   'comerciais com Portugal.', False,
   'Errado. A adesão do Maranhão se deu sob coerção militar (bloqueio/ataque naval de Lord Cochrane), '
   'com resistência de parte da elite "portuguesista" local, e não como expressão espontânea e efusiva '
   'de um projeto da elite de romper com Portugal.', 30)

ce(GB, 'Os processos produtivos das indústrias de siderurgia e de metalurgia demandam grandes volumes '
   'de água, bem como podem gerar substâncias tóxicas que impactam a qualidade dos recursos hídricos.',
   True, 'Correto — são setores intensivos em uso de água e geração de poluentes.', 31)

ce(GB, 'O transporte ferroviário é a principal modalidade de transporte utilizada no Brasil para o '
   'escoamento da produção de soja.', False,
   'Errado. No Brasil, o escoamento da soja é feito majoritariamente pelo modal rodoviário, com o '
   'ferroviário e o hidroviário em papel complementar.', 32)

ce(GB, 'No Brasil, os arranjos produtivos locais (APLs) são constituídos por aglomerações territoriais '
   'de agentes econômicos, políticos e sociais que compartilham infraestruturas e recursos presentes no '
   'território, sem, entretanto, estabelecer relações de cooperação ou articulação entre si.', False,
   'Errado. A cooperação e a articulação entre os agentes é justamente a característica definidora de '
   'um APL, e não sua ausência.', 33)

ce(GB, 'Desde a década de 70 do século XX, a população rural brasileira tem diminuído, enquanto a '
   'população urbana tem aumentado, dinâmica relacionada a fatores como o processo de êxodo rural e a '
   'mecanização do campo.', True, 'Correto — descreve o processo de urbanização acelerada do Brasil '
   'desde os anos 1970.', 34)

ce(GB, 'Embora ainda expressiva em números absolutos, a população jovem, com idade entre 15 e 29 anos, '
   'tem apresentado redução contínua em sua participação relativa na população brasileira.', True,
   'Correto — reflete o processo de envelhecimento populacional e queda da fecundidade no Brasil.', 35)

ce(GB, 'A maior parte da população indígena brasileira contabilizada no último censo demográfico do '
   'IBGE reside em áreas rurais e enfrenta problemas relacionados à demarcação e à proteção de seus '
   'territórios.', True,
   'Correto, segundo o Censo 2022 do IBGE, que aponta leve maioria da população indígena em área rural, '
   'associada a terras indígenas, com persistentes conflitos fundiários e de demarcação. (CONF: média)',
   36)

ce(GM, 'Uma das características da agricultura maranhense é a forte presença da agricultura familiar, '
   'modelo de produção rural direcionado à produção de alimentos para subsistência, consumo e '
   'comercialização no mercado interno.', True,
   'Correto — a agricultura familiar é predominante em grande parte do território maranhense.', 37)

ce(GM, 'A região sul do Maranhão integra o MATOPIBA e tem como característica a produção de grãos, em '
   'especial a soja, produto classificado como commodity.', True,
   'Correto — a região de Balsas, no sul do MA, é polo do MATOPIBA, voltado à sojicultura.', 38)

ce(GM, 'No Maranhão, verificam-se duas produções agrícolas distintas voltadas à segurança alimentar: o '
   'arroz, produzido em larga escala, com concentração produtiva restrita ao sul do estado, pelo '
   'modelo da agricultura moderna, com uso intensivo de mecanização e irrigação artificial; e a '
   'mandioca, produzida por agricultores familiares em todo o estado.', False,
   'Errado. A produção de arroz em larga escala no Maranhão concentra-se historicamente na região da '
   'Baixada Maranhense, e não no sul do estado — que é a região da soja (MATOPIBA), não do arroz.', 39)

ce(GM, 'A Chapada das Mesas, a Chapada do Araripe e a Chapada dos Guaranis formam o conjunto de '
   'chapadas encontradas no Maranhão, que são um tipo específico de relevo planáltico de origem '
   'vulcânica, com topografia aplainada e encostas íngremes, erodidas pela ação do vento e da chuva.',
   False, 'Errado. A Chapada do Araripe não se localiza no Maranhão; além disso, as chapadas '
   'brasileiras dessa região são de origem SEDIMENTAR, não vulcânica.', 40)

ce(GM, 'A Baixada Maranhense é uma ampla planície aluvial localizada na transição dos biomas Amazônia, '
   'Cerrado e Mata de Cocais, onde a presença de áreas alagáveis condiciona as formas de ocupação '
   'humana.', True, 'Correto — descrição consagrada da Baixada Maranhense.', 41)

ce(GM, 'As reentrâncias maranhenses são vales escavados pela erosão de rios em áreas de relevo '
   'planáltico ao redor das chapadas localizadas no sul do Maranhão, onde rios como o Tocantins, o '
   'Balsas e o Paranaíba são os agentes formadores desse relevo.', False,
   'Errado. As Reentrâncias Maranhenses são um relevo COSTEIRO (litoral recortado por baías, estuários '
   'e manguezais), e não um relevo planáltico interiorano formado por erosão fluvial no sul do estado.',
   42)

ce(GM, 'A área de proteção ambiental de Upaon-Açú, Miritiba e Alto Preguiças é uma extensa unidade de '
   'conservação estadual, criada para proteger recursos naturais, biodiversidade e áreas costeiras '
   'entre o golfão maranhense e o litoral oriental.', True,
   'Correto — é uma das maiores APAs estaduais do Maranhão, cobrindo essa faixa costeira.', 43)

ce(GM, 'As unidades de conservação presentes no Maranhão, protegidas pela legislação estadual em '
   'decorrência da relevância de suas características naturais, restringem-se às áreas amazônicas e '
   'litorâneas do estado.', False,
   'Errado. O Maranhão também possui unidades de conservação em áreas de cerrado e chapadas no sul do '
   'estado (ex.: Parque Nacional da Chapada das Mesas), não se restringindo a áreas amazônicas e '
   'litorâneas.', 44)

ce(GM, 'O Parque Nacional dos Lençóis Maranhenses, reconhecido como patrimônio natural da humanidade '
   'pela UNESCO, localiza-se no litoral oriental do estado, nos municípios de Barreirinhas, Santo Amaro '
   'e Primeira Cruz, em uma paisagem caracterizada por dunas e lagoas.', False,
   'Errado. O Parque Nacional dos Lençóis Maranhenses não integra a lista de Patrimônios Naturais da '
   'Humanidade da UNESCO (embora seja um importante patrimônio natural nacional e sítio Ramsar).', 45)

ce(RL, 'A tabela-verdade referente à proposição lógica (P ∧ Q ∧ R) → (S ∧ (~T)) tem mais de 30 linhas.',
   True, 'Correto. São 5 proposições simples distintas (P, Q, R, S, T), logo a tabela-verdade tem '
   '2⁵ = 32 linhas, mais de 30.', 46)

ce(RL, 'A sentença "Paulo ama Renata, Renata ama João e João ama Amélia" apresenta um argumento '
   'válido.', False,
   'Errado. Trata-se apenas de uma sequência de afirmações (premissas), sem uma conclusão apresentada; '
   'sem conclusão não há argumento a ser avaliado como válido ou inválido.', 47)

ce(RL, 'A proposição ~(P → Q) é equivalente à proposição P ∧ (~Q).', True,
   'Correto. ¬(P→Q) ≡ ¬(¬P∨Q) ≡ P∧¬Q, equivalência clássica da lógica proposicional.', 48)

ce(RL, 'Aplicando-se as leis de Morgan à proposição P ∧ (Q ∨ R), obtém-se a proposição '
   '(P ∨ Q) ∧ (P ∨ R).', False,
   'Errado. As leis de De Morgan tratam da negação de conjunções/disjunções [¬(A∧B)≡¬A∨¬B], e não se '
   'aplicam a essa proposição (que não tem negação); além disso, (P∨Q)∧(P∨R) é a distributiva de '
   'P∨(Q∧R), não de P∧(Q∨R).', 49)

ce(RL, 'A sentença "As organizações de segurança pública, principalmente aquelas mais próximas da '
   'comunidade em que estão inseridas, buscam atuar de forma preventiva como agentes de segurança" '
   'pode ser corretamente expressa pela proposição lógica composta P ∧ Q.', False,
   'Errado. A sentença é uma proposição simples (com um adjunto restritivo/enfático), não a conjunção '
   'de duas proposições distintas ligadas por "e".', 50)

# ===================== CONHECIMENTOS ESPECÍFICOS (51-120) =====================

ce(EST, 'É vedada, independentemente do caso, a promoção em ressarcimento de preterição.', False,
   'Errado. O art. 78, §1º, da Lei nº 6.513/95 admite a promoção em ressarcimento de preterição em '
   'casos extraordinários.', 51)

ce(EST, 'O ingresso no Quadro de Oficiais de Administração (QOA) e no Quadro de Oficiais Especialistas '
   '(QOE) é restrito aos subtenentes e exige, como requisito, o mínimo de 10 anos de efetivo exercício, '
   'além de certificado de conclusão de ensino médio.', False,
   'Errado. O art. 11 exige diploma de curso de NÍVEL SUPERIOR (não ensino médio) e, no mínimo, 18 anos '
   'de efetivo serviço (não 10), além de 2 anos na graduação.', 52)

ce(EST, 'O aprimoramento técnico-profissional é uma das formas de manifestação essencial do valor '
   'policial militar.', True, 'Correto, nos termos do art. 39, VI, da Lei nº 6.513/95.', 53)

ce(EST, 'Constitui prerrogativa dos policiais militares o direito a julgamento em foro especial, nos '
   'crimes militares.', True,
   'Correto — a Justiça Militar Estadual é o foro especial constitucionalmente assegurado para o '
   'julgamento de crimes militares.', 54)

ce(EST, 'É possível a requisição ou a cessão de policial militar da ativa para a Defensoria Pública do '
   'Maranhão por meio de decisão indelegável do chefe do Poder Executivo.', True,
   'Correto. A Defensoria Pública consta do rol do art. 35 como órgão ao qual o militar pode ser posto '
   'à disposição, sendo essa cessão externa, por não constituir provimento de cargo privativo de '
   'Oficial/Praça (hipótese de delegação do art. 26), ato reservado ao Governador. (CONF: média)', 55)

ce(EST, 'A precedência hierárquica é regulada de forma a prestigiar a antiguidade no posto ou '
   'graduação, em vez da precedência funcional.', True,
   'Correto, como regra geral do art. 20 — a antiguidade no posto/graduação é o critério padrão, '
   'cedendo à precedência funcional apenas quando esta for expressamente estabelecida em lei.', 56)

ce(EST, 'O exame toxicológico para os candidatos aos cursos de formação da Polícia Militar do Maranhão '
   'é obrigatório e possui caráter eliminatório.', True,
   'Correto, nos termos do art. 9º, parágrafo único, da Lei nº 6.513/95.', 57)

ce(EST, 'Em caso de concurso de crime militar e de transgressão disciplinar cometidos pelo mesmo '
   'policial militar, devem ser aplicadas cumulativamente a sanção disciplinar e a pena relativa ao '
   'crime.', False,
   'Errado. O art. 55, §2º, determina que, no concurso de crime militar e transgressão disciplinar, '
   'aplica-se SOMENTE a pena relativa ao crime, e não ambas cumulativamente.', 58)

ce(L12896, 'O comandante-geral da PM/MA será nomeado pelo governador do estado entre os oficiais da '
   'ativa do posto de coronel do Quadro de Oficiais de Estado-Maior (QOEM), sendo-lhe garantidos as '
   'mesmas prerrogativas, o mesmo tratamento protocolar e a mesma remuneração conferidos aos '
   'secretários de estado.', True,
   'Correto, nos termos do art. 7º, §§1º e 2º, da Lei nº 12.896/2026.', 59)

ce(L12896, 'O Estado-Maior Geral (EMG) é classificado na organização básica da PM/MA como um órgão de '
   'apoio técnico-logístico e de correição, sendo o responsável direto pela gestão da custódia dos '
   'policiais militares presos à disposição da justiça.', False,
   'Errado. O EMG é órgão de DIREÇÃO GERAL (art. 6º/16); a gestão da custódia de presos é atribuição do '
   'Presídio Militar, subordinado à Corregedoria-Geral (art. 85-87), não ao EMG.', 60)

ce(L12896, 'O Quadro de Oficiais da Reserva e Reformados (QORR) é composto por oficiais da polícia '
   'militar da reserva remunerada e reformados.', True,
   'Correto, nos termos do art. 103 da Lei nº 12.896/2026.', 61)

ce(L12896, 'Compete ao comandante geral da PM/MA dirigir, orientar, coordenar e fiscalizar os planos e '
   'operações da corporação, realizando inspeções periódicas nos diversos órgãos, com vistas ao '
   'eficiente emprego da polícia militar.', False,
   'Errado. Essa atribuição específica (art. 14, V) é do SUBCOMANDANTE-GERAL, não do Comandante-Geral '
   '(cujas competências estão no art. 8º).', 62)

ce(L12896, 'O militar que concluir o curso de formação e ingressar na PM/MA deverá permanecer por um '
   'período mínimo de três anos servindo na área do Comando de Policiamento de sua primeira '
   'classificação, ressalvada a movimentação por necessidade de serviço ou motivo de relevante '
   'interesse público.', True, 'Correto, nos termos do art. 95 da Lei nº 12.896/2026.', 63)

ce(L12896, 'O órgão de direção geral responsável por auxiliar a gestão máxima da instituição é o '
   'Subcomando-Geral.', True, 'Correto, nos termos do art. 12 da Lei nº 12.896/2026.', 64)

ce(L12896, 'A Seção de Inteligência e Contrainteligência integra a Corregedoria-Geral da Polícia '
   'Militar, que, além de zelar pela preservação da ética e da disciplina, exerce as funções de polícia '
   'judiciária militar e de corregedoria administrativa na instituição.', True,
   'Correto, nos termos do art. 85 da Lei nº 12.896/2026.', 65)

ce(L14751, 'Na hierarquia da polícia militar, o aluno-soldado e o aluno-sargento são considerados '
   'praças, e o aluno-oficial, praça especial.', True,
   'Correto, nos termos do art. 12 da Lei nº 14.751/2023.', 66)

ce(L14751, 'Todas as polícias militares estaduais são forças auxiliares e reserva do Exército, '
   'comandadas por oficial da ativa do último posto, integrante do Quadro de Oficiais de Estado-Maior '
   '(QOEM) da respectiva instituição.', True,
   'Correto, nos termos do art. 2º, caput, da Lei nº 14.751/2023.', 67)

ce(L14751, 'O uso racional da força e o uso progressivo dos meios são diretrizes, e não princípios '
   'básicos, a serem observadas pelas polícias militares estaduais.', True,
   'Correto. Constam do art. 4º, XIV (diretrizes), e não do rol de princípios básicos do art. 3º.', 68)

ce(L14751, 'Entre os princípios básicos das polícias militares expressamente previstos em lei estão a '
   'hierarquia, a disciplina, a finalidade e a motivação.', False,
   'Errado. O art. 3º lista hierarquia, disciplina, direitos humanos, legalidade, impessoalidade, '
   'publicidade, moralidade, eficiência, efetividade, razoabilidade/proporcionalidade, universalidade e '
   'participação comunitária; "finalidade" e "motivação" são requisitos do ato administrativo (Direito '
   'Administrativo), não princípios da lei orgânica.', 69)

ce(L14751, 'É da competência das polícias militares emitir manifestação técnica e exercer a '
   'fiscalização em eventos e locais de concentração de público, inclusive a segurança contra pânico e '
   'emergências nesses locais.', False,
   'Errado. A segurança contra incêndio, pânico e emergência em locais de concentração de público é '
   'competência PRIVATIVA dos corpos de bombeiros militares (art. 6º, IX), não das polícias militares.',
   70)

ce(L14751, 'A estabilidade dos policiais militares de carreira ocorre após três anos de efetivo '
   'serviço nas corporações militares.', True,
   'Correto, regra de estabilidade dos militares estaduais de carreira prevista na Lei nº 14.751/2023. '
   '(CONF: média)', 71)

ce(L14751, 'Na forma da legislação de ensino do respectivo ente federado, a instituição militar '
   'estadual pode optar por formar o militar do estado em curso de formação de educação superior, '
   'concedendo-lhe o requisito de ingresso relativo à escolaridade.', True,
   'Correto, nos termos do art. 13, IX, c/c art. 15, da Lei nº 14.751/2023.', 72)

ce(L14751, 'O Sistema de Gerenciamento Militar de Armas (SIGMA) destina-se ao cadastramento de armas '
   'de fogo institucionais das polícias militares, e não das armas particulares dos seus integrantes, '
   'que devem constar somente dos seus registros próprios.', True,
   'Correto — o SIGMA cadastra o armamento institucional das corporações, distinto dos registros de '
   'armas particulares dos militares. (CONF: média)', 73)

ce(L14751, 'Para o ingresso na polícia militar, é vedado possuir qualquer tatuagem que fique visível '
   'quando o indivíduo estiver em uso de uniforme.', False,
   'Errado. O art. 13, X, veda apenas tatuagens visíveis com conteúdo específico (suásticas, '
   'obscenidades, apologia à violência/drogas/terrorismo/discriminação), e não QUALQUER tatuagem '
   'visível.', 74)

ce(L14751, 'O militar com menos de 10 anos de serviço que se candidatar a mandato eletivo será '
   'agregado ao quadro, com remuneração, até o final do pleito eleitoral.', False,
   'Errado. A regra (espelhada também no art. 64, §1º, da Lei nº 6.513/95) é a inversa: quem tem MENOS '
   'de 10 anos de serviço deve AFASTAR-SE da atividade (com suspensão de gratificações); é quem tem '
   'MAIS de 10 anos que é agregado.', 75)

ce(INFO, 'No Windows, a variável de ambiente PATH mantém uma relação de diretórios utilizados na '
   'pesquisa por arquivos executáveis, e a ordem desses diretórios pode interferir na localização de um '
   'comando quando arquivos de mesmo nome e extensão estiverem presentes em mais de um deles.', True,
   'Correto — é exatamente assim que a variável PATH funciona.', 76)

ce(INFO, 'A ocultação do ícone da Lixeira na Área de Trabalho do Windows impede o acesso ao conteúdo '
   'da Lixeira por outros meios disponibilizados pelo sistema operacional.', False,
   'Errado. Ocultar o ícone na Área de Trabalho não bloqueia outras formas de acesso (ex.: pelo '
   'Explorador de Arquivos, digitando o caminho da Lixeira).', 77)

ce(INFO, 'No Windows, a configuração para ocultar extensões de tipos de arquivo conhecidos interfere '
   'na forma como o nome do arquivo é exibido no Explorador de Arquivos, sem que isso implique a '
   'remoção da extensão do arquivo.', True,
   'Correto — é uma configuração apenas de exibição; a extensão real do arquivo permanece inalterada.',
   78)

ce(INFO, 'No Windows, quando selecionado um arquivo e executado o comando Shift+Delete, tal arquivo é '
   'diretamente enviado para a Lixeira, sem exibição de mensagem de confirmação ao usuário.', False,
   'Errado. Shift+Delete exclui o arquivo PERMANENTEMENTE, sem passar pela Lixeira, e por padrão exibe '
   'mensagem de confirmação ao usuário.', 79)

ce(INFO, 'No Windows, as contas de usuário locais são definidas no próprio dispositivo, que atua como '
   'autoridade de segurança dessas contas, de modo que seus direitos e suas permissões se restringem ao '
   'equipamento em que foram criadas.', True,
   'Correto — descrição padrão de contas locais (não associadas a um domínio).', 80)

ce(INFO, 'No Linux, o comando pwd altera o diretório de trabalho atual para o diretório pessoal do '
   'usuário e, em seguida, apresenta o caminho desse diretório na tela.', False,
   'Errado. "pwd" (print working directory) apenas EXIBE o diretório atual; não altera o diretório de '
   'trabalho (quem faz isso é o comando "cd").', 81)

ce(INFO, 'No Linux, a conta root é tradicionalmente identificada pelo UID 0, independentemente do nome '
   'textual associado a essa identificação numérica.', True,
   'Correto — é o UID 0 que confere privilégios de superusuário, não o nome da conta.', 82)

ce(INFO, 'Em sistemas Linux que utilizam systemd, a execução do comando systemctl start '
   'nome.service inicia a unidade de serviço na sessão atual, mas não implica, por si só, que ela seja '
   'iniciada automaticamente nos próximos boots do sistema.', True,
   'Correto. Para iniciar automaticamente no boot é necessário o comando "systemctl enable", separado '
   'do "start".', 83)

ce(INFO, 'No Microsoft Word, quando o usuário insere um cabeçalho em determinada página do documento, '
   'o conteúdo desse cabeçalho passa a integrar individualmente aquela página e pode ser, por padrão, '
   'alterado nela sem afetar outras páginas da mesma seção.', False,
   'Errado. Por padrão, o cabeçalho é definido por SEÇÃO do documento, aplicando-se a todas as páginas '
   'dela, e não individualmente por página.', 84)

ce(INFO, 'A inserção de uma quebra de página manual no Microsoft Word resulta necessariamente na '
   'criação de um novo documento, e o conteúdo inserido posteriormente à quebra fica armazenado em '
   'arquivo separado.', False,
   'Errado. Uma quebra de página apenas desloca o conteúdo para uma nova página dentro do MESMO '
   'documento, sem criar arquivo separado.', 85)

ce(INFO, CENARIO_WORD_EXCEL + 'Caso o soldado Almeida queira substituir, no relatório elaborado no '
   'Word, todas as ocorrências de determinada expressão por outra, ele poderá utilizar o recurso '
   'Localizar e Substituir, que permite realizar a alteração de todas as ocorrências da expressão '
   'encontradas no documento.', True,
   'Correto — função "Substituir Tudo" do recurso Localizar e Substituir.', 86)

ce(INFO, CENARIO_WORD_EXCEL + 'Caso outro policial revise o relatório em Word com o recurso Controlar '
   'Alterações ativado, as inserções e exclusões realizadas poderão ser registradas no documento para '
   'posterior análise das modificações.', True,
   'Correto — é a função padrão do Controlar Alterações (Track Changes).', 87)

ce(INFO, CENARIO_WORD_EXCEL + 'Se o relatório em Word tiver várias páginas e o soldado Almeida inserir '
   'números de página por meio do recurso próprio do programa, a numeração inserida será convertida em '
   'texto comum, de modo que eventual inclusão de novas páginas no meio do documento já existente '
   'exigiria a renumeração manual das novas páginas e das seguintes.', False,
   'Errado. A numeração de página do Word é um CAMPO DINÂMICO, que se atualiza automaticamente quando '
   'páginas são adicionadas ou removidas, sem exigir renumeração manual.', 88)

ce(INFO, CENARIO_WORD_EXCEL + 'Na planilha em Excel, se a coluna B contiver a natureza de cada '
   'ocorrência, a fórmula =CONT.SE(B2:B100;"Furto") poderá ser utilizada para a contagem de quantas '
   'células do intervalo especificado atendem ao critério "Furto".', True,
   'Correto — é exatamente a função da fórmula CONT.SE (COUNTIF).', 89)

ce(INFO, CENARIO_WORD_EXCEL + 'Se o soldado Almeida aplicar um filtro à coluna "Natureza" para exibir '
   'apenas as ocorrências classificadas como "Acidente de trânsito", o Excel excluirá temporariamente '
   'da planilha as linhas referentes às demais naturezas, restaurando-as quando o filtro for removido.',
   True, 'Correto — o AutoFiltro do Excel oculta temporariamente as linhas que não atendem ao critério, '
   'sem excluí-las de fato, restaurando a exibição ao remover o filtro.', 90)

ce(INFO, 'Uma rede WAN cobre uma grande extensão geográfica, como um país ou um continente.', True,
   'Correto — definição padrão de WAN (Wide Area Network).', 91)

ce(INFO, 'A ativação da senha principal no Mozilla Thunderbird impede que terceiros acessem as '
   'mensagens de email salvas no computador.', False,
   'Errado. A senha principal (Master Password) protege principalmente as SENHAS salvas no gerenciador '
   'do Thunderbird, não garante proteção/criptografia geral das mensagens de email armazenadas.', 92)

ce(INFO, 'No Mozilla Thunderbird, a compactação de pastas elimina as lacunas geradas pelo apagamento '
   'de mensagens, preservando os emails mantidos pelo usuário.', True,
   'Correto — é a função da compactação de pastas (recuperar espaço em disco sem apagar emails '
   'restantes).', 93)

ce(INFO, 'No serviço de correio eletrônico, o protocolo IMAP4 é empregado pelo agente de transferência '
   'de mensagem para enviar emails do servidor do remetente ao servidor do destinatário.', False,
   'Errado. A transferência de emails entre servidores é feita pelo protocolo SMTP; o IMAP4 é protocolo '
   'de ACESSO/leitura de mensagens em um servidor, usado pelo cliente de email.', 94)

ce(INFO, 'O protocolo FTP é o responsável por converter nomes de sites (por exemplo, '
   '<www.pm.ma.gov.br>) em seus respectivos endereços IP.', False,
   'Errado. Essa conversão é feita pelo DNS (Domain Name System); o FTP é um protocolo de transferência '
   'de arquivos, sem relação com resolução de nomes.', 95)

ce(INFO, 'No Google Chrome, a verificação do status de segurança da conexão com uma página da Web é '
   'realizada por meio do ícone localizado à esquerda do endereço do site.', True,
   'Correto — o ícone de segurança/cadeado fica à esquerda, na barra de endereços.', 96)

ce(INFO, 'A tecnologia Ethernet, padronizada pelo IEEE 802.3, é a mais difundida no âmbito das redes '
   'locais (LANs) com fio.', True, 'Correto — fato consolidado sobre redes locais cabeadas.', 97)

ce(INFO, 'A aplicação de filtros para personalizar os resultados de uma consulta na pesquisa Google '
   'altera, de modo definitivo, as configurações gerais do usuário, tais como o idioma padrão e o '
   'recurso SafeSearch.', False,
   'Errado. Filtros aplicados a uma consulta específica são ajustes pontuais daquela busca, não alteram '
   'permanentemente as configurações gerais da conta/navegador.', 98)

ce(INFO, 'A identificação de publicações no Instagram consideradas inadequadas ou ofensivas, ainda que '
   'não violem os padrões da comunidade, enseja a imediata remoção do conteúdo da plataforma.', False,
   'Errado. Conteúdo que não viola os padrões da comunidade, em regra, não é removido apenas por ser '
   'considerado inadequado por alguns usuários.', 99)

ce(INFO, 'Uma funcionalidade habilitada por padrão em perfis de criadores de conteúdo no Instagram é a '
   'autenticação de dois fatores, ferramenta de segurança que exige um código de validação em logins '
   'realizados via dispositivos não reconhecidos.', False,
   'Errado. A autenticação de dois fatores é um recurso que precisa ser ativado manualmente pelo '
   'usuário, não vem habilitada por padrão.', 100)

ce(INFO, 'A ampla compatibilidade entre as plataformas de cloud computing garante ao usuário a fácil '
   'migração de serviços entre diferentes provedores, o que reduz o risco de dependência de '
   'fornecedor.', False,
   'Errado. Um dos desafios conhecidos da computação em nuvem é justamente a falta de padronização '
   'entre provedores, gerando risco de aprisionamento tecnológico (vendor lock-in), e não fácil '
   'migração garantida.', 101)

ce(INFO, 'No Windows, quando restaurado um arquivo presente na Lixeira, ele retorna automaticamente a '
   'seu local de origem.', True, 'Correto — é o comportamento padrão da função "Restaurar".', 102)

ce(INFO, 'No Windows 11 (versão 22H2 em diante), as pastas padrão do usuário não são exibidas em Este '
   'PC, ficando esta seção destinada à visualização das unidades de disco e dos locais de rede.', False,
   'Errado. Em "Este PC" continuam sendo exibidas as pastas padrão do usuário (Área de Trabalho, '
   'Documentos, Downloads etc.) junto com as unidades de disco.', 103)

ce(INFO, 'Entre os benefícios da cloud computing, destaca-se a redução de custos, que, no entanto, '
   'depende necessariamente do investimento inicial na aquisição de ativos de infraestrutura.', False,
   'Errado. Um dos principais atrativos da nuvem é justamente DISPENSAR o investimento inicial em '
   'infraestrutura própria, adotando modelo de pagamento sob demanda.', 104)

ce(INFO, 'A computação em nuvem possibilita a conversão de despesas de capital (capex) em despesas '
   'operacionais (opex) por meio da contratação de recursos sob demanda e do pagamento proporcional ao '
   'uso.', True, 'Correto — é a lógica clássica de capex-to-opex da nuvem.', 105)

ce(INFO, 'Um software de firewall pessoal pode bloquear conexões de rede não autorizadas com base em '
   'regras predeterminadas que analisam portas lógicas e endereços IP de origem e destino dos pacotes '
   'de dados.', True, 'Correto — descrição padrão de firewall por filtragem de pacotes.', 106)

ce(INFO, 'A concessão de privilégios de administrador de sistema aos operadores em suas tarefas '
   'rotineiras de escritório previne a exploração de brechas de segurança decorrentes de falhas em '
   'aplicativos de terceiros.', False,
   'Errado. Pelo princípio do menor privilégio, conceder privilégios administrativos desnecessários '
   'AUMENTA (não previne) o risco de exploração de vulnerabilidades.', 107)

ce(INFO, 'A tecnologia de firewall com inspeção de estado realiza a filtragem tratando cada pacote de '
   'dados de forma isolada, impedindo o rastreamento das conexões ativas que transitam pelas camadas '
   'da rede.', False,
   'Errado. É o firewall de filtragem SEM estado (stateless) que trata pacotes isoladamente; o firewall '
   'com inspeção de estado (stateful) faz justamente o oposto: rastreia o estado das conexões ativas.',
   108)

ce(INFO, 'O método de varredura por assinatura empregado por antivírus atua bloqueando ameaças '
   'desconhecidas no momento de sua execução mediante a análise dinâmica de comportamentos suspeitos no '
   'fluxo de memória.', False,
   'Errado. Essa descrição corresponde à análise HEURÍSTICA/comportamental; a varredura por ASSINATURA '
   'detecta ameaças já CONHECIDAS, por comparação com um banco de assinaturas.', 109)

ce(INFO, 'A política de controle de acesso fundamentada no princípio da necessidade de conhecer '
   '(need-to-know) visa resguardar a confidencialidade dos dados ao delimitar o acesso do agente '
   'público às informações indispensáveis ao exercício de suas atribuições.', True,
   'Correto — definição padrão do princípio need-to-know.', 110)

ce(INFO, 'O procedimento que envolve a exigência de confirmação de identidade por meio de um código '
   'numérico temporário enviado ao dispositivo do usuário, além do preenchimento habitual de senha, '
   'fortalece a segurança do acesso a sistemas corporativos contra fraudes oriundas de credenciais '
   'comprometidas.', True, 'Correto — é a autenticação de dois fatores (2FA/MFA).', 111)

ce(INFO, 'Um rootkit pode se alojar em camadas profundas do sistema operacional ou no firmware da '
   'placa-mãe com o propósito de ocultar a presença de outros softwares maliciosos da listagem de '
   'processos exibida pelo gerenciador de tarefas.', True,
   'Correto — descrição padrão de rootkit, incluindo variantes em firmware/bootkit.', 112)

ce(INFO, 'Ataques baseados em ransomware realizam a criptografia indevida de repositórios de dados no '
   'equipamento afetado, condicionando a eventual restauração das chaves criptográficas à aceitação de '
   'exigências financeiras emitidas pelos fraudadores.', True,
   'Correto — definição padrão de ransomware.', 113)

ce(INFO, 'O vírus denominado cavalo de Troia atua alterando o setor de inicialização do sistema para '
   'gerar cópias automáticas de si mesmo e transmitir tais arquivos aos contatos de correio eletrônico '
   'da vítima.', False,
   'Errado. O cavalo de Troia (Trojan) se disfarça de programa legítimo e NÃO se autorreplica nem altera '
   'o setor de boot — essas características são de vírus de boot/worms, não de Trojans.', 114)

ce(INFO, 'O worm é uma praga virtual cuja propagação pela rede local depende da inclusão de seu código '
   'malicioso no interior de arquivos executáveis preexistentes.', False,
   'Errado. É o VÍRUS clássico que precisa infectar um arquivo hospedeiro; o worm é autônomo/standalone '
   'e se propaga pela rede independentemente de arquivos executáveis preexistentes.', 115)

ce(INFO, 'A utilização de plataformas de armazenamento em nuvem possibilita a sincronização de pastas '
   'de trabalho entre diferentes estações conectadas à Internet, facilitando a recuperação de arquivos '
   'em caso de falha física no disco local.', True,
   'Correto — vantagem clássica do armazenamento em nuvem.', 116)

ce(INFO, 'A recomposição integral de uma base de dados gerenciada por um ciclo semanal de salvamento '
   'completo acrescido de salvamentos diários incrementais requer a recuperação da cópia completa de '
   'origem associada a cada um dos arquivos gerados nas etapas diárias subsequentes até a data do '
   'incidente.', True,
   'Correto — a restauração de uma cadeia de backup completo + incrementais exige recuperar o backup '
   'completo mais recente e, em sequência, cada um dos incrementais gerados até a data do incidente. '
   '(CONF: média)', 117)

ce(INFO, 'A contratação de serviços de armazenamento em nuvem transfere a custódia operacional da '
   'infraestrutura física para a empresa contratada, dispensando o gerenciamento interno das '
   'permissões de acesso aos diretórios institucionais compartilhados.', False,
   'Errado. Pelo modelo de responsabilidade compartilhada, a segurança da infraestrutura física é do '
   'provedor, mas o gerenciamento de permissões de acesso aos próprios dados permanece responsabilidade '
   'do contratante.', 118)

ce(INFO, 'Na estratégia de backup diferencial de segurança, cada rotina intermediária registra as '
   'alterações ocorridas a partir do momento em que o último backup completo foi consolidado.', True,
   'Correto — é a definição de backup DIFERENCIAL (sempre em relação ao último completo), diferente do '
   'incremental (que se baseia no último backup de qualquer tipo).', 119)

ce(INFO, 'A execução de uma rotina de backup incremental de dados demanda a duplicação integral de '
   'todos os arquivos do volume selecionado a cada novo ciclo de salvamento.', False,
   'Errado. Isso descreve o backup COMPLETO; o incremental copia apenas os arquivos alterados desde o '
   'último backup (de qualquer tipo).', 120)

assert len(PM_CE) == 120, len(PM_CE)

decoder_dummy = None
new_pm_questions = []
next_id = 827
for disc, enun, resp, exp, n in PM_CE:
    new_pm_questions.append({
        "id": next_id, "corp": "PM", "disc": disc, "tipo": "CE",
        "enun": enun, "resp": resp, "exp": exp.rstrip() + FONTE(n),
    })
    next_id += 1

# ===================== VERSÃO ADAPTADA PARA O CORP "BM" (itens 66-75) =====================
# Mesmo conteudo/pegadinhas da Lei 14.751/2023, em formato MC (padrao do corp BM).

BM_MC = [
    {"enun": "Na hierarquia estabelecida pela Lei nº 14.751/2023, aplicável também ao Corpo de "
             "Bombeiros Militar, o aluno-soldado e o aluno-sargento são classificados como:",
     "alts": ["Praças, e o aluno-oficial como praça especial.",
              "Praças especiais, e o aluno-oficial como praça.",
              "Oficiais subalternos.",
              "Categoria à parte, fora da hierarquia militar.",
              "Praças apenas na Polícia Militar, não no Corpo de Bombeiros."],
     "resp": 0,
     "exp": "Correto, nos termos do art. 12 da Lei nº 14.751/2023: aluno-soldado e aluno-sargento são "
            "praças; aspirante a oficial, cadete e aluno-oficial são praças especiais."},

    {"enun": "Segundo a Lei nº 14.751/2023, todos os corpos de bombeiros militares estaduais são:",
     "alts": ["Órgãos civis vinculados ao Ministério Público estadual.",
              "Forças auxiliares e reserva da Marinha do Brasil.",
              "Forças auxiliares e reserva do Exército, comandadas por oficial da ativa do último "
              "posto do respectivo QOEM.",
              "Subordinados diretamente ao Comando do Exército, sem vínculo com o Governador.",
              "Organizados sem base em hierarquia e disciplina, por não exercerem função policial."],
     "resp": 2,
     "exp": "Correto, nos termos do art. 2º, caput, da Lei nº 14.751/2023, aplicável tanto às PMs "
            "quanto aos CBMs."},

    {"enun": "O uso racional da força e o uso progressivo dos meios, aplicáveis também à atuação do "
             "corpo de bombeiros militar, são classificados pela Lei nº 14.751/2023 como:",
     "alts": ["Princípios básicos, no mesmo nível da hierarquia e da disciplina.",
              "Diretrizes, e não princípios básicos.",
              "Cláusulas pétreas da organização militar.",
              "Normas de eficácia limitada, sem aplicação prática.",
              "Exclusividade da Polícia Militar, não se aplicando ao Corpo de Bombeiros."],
     "resp": 1,
     "exp": "Correto, nos termos do art. 4º, XIV, da Lei nº 14.751/2023 — são diretrizes (art. 4º), "
            "distintas do rol de princípios básicos (art. 3º)."},

    {"enun": "Entre os princípios básicos das polícias militares e dos corpos de bombeiros militares "
             "expressamente previstos no art. 3º da Lei nº 14.751/2023, estão:",
     "alts": ["Finalidade e motivação, como nos atos administrativos em geral.",
              "Hierarquia, disciplina, direitos humanos, legalidade, impessoalidade, publicidade, "
              "moralidade e eficiência, entre outros.",
              "Exclusivamente hierarquia e disciplina, sem qualquer outro princípio.",
              "Competência, forma e objeto.",
              "Supremacia do interesse militar sobre os direitos humanos."],
     "resp": 1,
     "exp": "Correto, nos termos do art. 3º da Lei nº 14.751/2023. 'Finalidade' e 'motivação' são "
            "requisitos do ato administrativo (Direito Administrativo), não princípios desta lei."},

    {"enun": "A segurança contra incêndio, pânico e emergência em eventos e locais de concentração de "
             "público é, nos termos da Lei nº 14.751/2023, competência:",
     "alts": ["Privativa das polícias militares.",
              "Compartilhada igualmente entre polícia militar e corpo de bombeiros, sem distinção.",
              "Privativa dos corpos de bombeiros militares.",
              "Do Poder Judiciário estadual.",
              "Exclusiva da Defesa Civil municipal, vedada a atuação do Corpo de Bombeiros."],
     "resp": 2,
     "exp": "Correto, nos termos do art. 6º, IX, da Lei nº 14.751/2023 — é atribuição PRIVATIVA do "
            "corpo de bombeiros militar, e não da polícia militar."},

    {"enun": "Segundo a Lei nº 14.751/2023, a estabilidade do militar estadual de carreira, inclusive "
             "do bombeiro militar, ocorre após:",
     "alts": ["Um ano de efetivo serviço.", "Três anos de efetivo serviço.",
              "Cinco anos de efetivo serviço.", "Dez anos de efetivo serviço.",
              "Não há previsão de estabilidade para militares estaduais."],
     "resp": 1,
     "exp": "Correto — a estabilidade do militar estadual de carreira ocorre após três anos de efetivo "
            "serviço, nos termos da Lei nº 14.751/2023."},

    {"enun": "Na forma da legislação de ensino do respectivo ente federado, a instituição militar "
             "estadual (incluindo o corpo de bombeiros militar) pode:",
     "alts": ["Dispensar integralmente qualquer exigência de escolaridade para o ingresso.",
              "Formar o militar em curso de formação de educação superior, suprindo-se assim o "
              "requisito de escolaridade para o ingresso.",
              "Exigir apenas o ensino fundamental completo, vedada qualquer outra exigência.",
              "Delegar a exigência de escolaridade a convênio com instituição privada estrangeira.",
              "Reduzir a escolaridade mínima por ato do Comandante-Geral, independentemente de lei."],
     "resp": 1,
     "exp": "Correto, nos termos do art. 13, IX, c/c art. 15, da Lei nº 14.751/2023."},

    {"enun": "O Sistema de Gerenciamento Militar de Armas (SIGMA), previsto na Lei nº 14.751/2023, "
             "destina-se ao cadastramento:",
     "alts": ["Das armas de fogo institucionais das corporações militares, e não das armas "
              "particulares dos seus integrantes.",
              "Exclusivamente das armas particulares dos militares, registradas também no SINARM.",
              "De qualquer arma de fogo no território nacional, substituindo o SINARM.",
              "Somente de armamento de uso restrito das Forças Armadas.",
              "De veículos operacionais das corporações militares estaduais."],
     "resp": 0,
     "exp": "Correto — o SIGMA cadastra o armamento institucional da corporação; as armas particulares "
            "dos militares seguem seus próprios registros."},

    {"enun": "Para o ingresso na polícia militar ou no corpo de bombeiros militar, a Lei nº "
             "14.751/2023 veda a posse de tatuagem visível em uso de uniforme:",
     "alts": ["De qualquer tipo, sem exceção.",
              "Apenas se a tatuagem for colorida.",
              "Apenas de conteúdo específico (suásticas, obscenidades, apologia à violência, às "
              "drogas ilícitas, ao terrorismo ou à discriminação), não qualquer tatuagem visível.",
              "Somente se a tatuagem for de autoria de tatuador não licenciado.",
              "Somente em candidatos do sexo masculino."],
     "resp": 2,
     "exp": "Correto, nos termos do art. 13, X, da Lei nº 14.751/2023 — a vedação é restrita a "
            "conteúdos específicos, não a qualquer tatuagem visível."},

    {"enun": "O militar estadual (de qualquer corporação) com menos de 10 anos de serviço que se "
             "candidatar a mandato eletivo deverá, segundo a regra geral aplicável:",
     "alts": ["Ser agregado ao quadro, com remuneração, até o final do pleito eleitoral.",
              "Afastar-se da atividade, com suspensão das gratificações e indenizações, salvo "
              "exceções legais.",
              "Ser automaticamente excluído da corporação, sem direito a retorno.",
              "Permanecer em serviço normalmente, sem qualquer afastamento.",
              "Ser promovido ao posto imediatamente superior como incentivo à candidatura."],
     "resp": 1,
     "exp": "Correto — quem tem menos de 10 anos de serviço deve afastar-se da atividade; é quem tem "
            "mais de 10 anos que é agregado, com passagem automática à inatividade em caso de eleição."},
]

assert len(BM_MC) == 10

new_bm_questions = []
for item in BM_MC:
    new_bm_questions.append({
        "id": next_id, "corp": "BM", "disc": L14751, "tipo": "MC",
        "enun": item["enun"], "alts": item["alts"], "resp": item["resp"],
        "exp": item["exp"] + " (Adaptação, em múltipla escolha, de item da Prova CEBRASPE – PMMA, "
               "Edital 2026, sobre a Lei nº 14.751/2023, expressamente aplicável a PM e BM.)",
    })
    next_id += 1

all_new = new_pm_questions + new_bm_questions
assert all_new[0]['id'] == 827
assert all_new[-1]['id'] == 826 + 130

body = raw[:-1]  # remove o "]" final
for q in all_new:
    body += '\r\n, ' + json.dumps(q, ensure_ascii=False)
body += ']'

with open('questions.json', 'w', encoding='utf-8', newline='') as f:
    f.write(body)

with open('questions.json', encoding='utf-8') as f:
    data = json.load(f)
assert len(data) == len(data_check) + len(all_new)
print('OK -- total de questoes agora:', len(data))
print('novo total PM:', sum(1 for q in data if q['corp'] == 'PM'))
print('novo total BM:', sum(1 for q in data if q['corp'] == 'BM'))

with open('questions.json', encoding='utf-8') as f:
    qdata = f.read()
with open('app-template.html', encoding='utf-8') as f:
    html = f.read()
html = html.replace('__QUESTIONS_JSON__', qdata)
with open('estudo-cebraspe-ma.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('estudo-cebraspe-ma.html regenerado com sucesso')
