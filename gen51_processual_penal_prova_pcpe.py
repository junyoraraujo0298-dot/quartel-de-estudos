# -*- coding: utf-8 -*-
"""
Segundo conteudo de Direito Processual Penal do app (PC-PE) -- a partir
do PDF "Teoria Geral da Prova" (Focus Concursos), que cobre o item 3 do
edital (Prova: exame de corpo de delito e pericias em geral;
interrogatorio do acusado; confissao do ofendido; testemunhas;
reconhecimento de pessoas e coisas; acareacao; documentos; indicios;
busca e apreensao). Disciplina ate entao com cobertura so do item 1
(Disposicoes Preliminares, gen50); este PDF adiciona o item 3 inteiro.

A mudanca estrutural em app-template.html ja foi feita via Edit antes
deste script rodar: foram acrescentados 79 novos itens ao final do
TEORIA_DIREITO_PROCESSUAL_PENAL_PCPE ja existente (mesmo deck, nao um
novo), cobrindo: teoria geral da prova (conceito, prova x elemento de
informacao, provas cautelares/nao repetiveis/antecipadas, os 3 sistemas
de valoracao da prova, objeto da prova, os 4 criterios de classificacao
da prova, onus da prova + art. 156 + art. 3-A, provas ilicitas e prova
ilicita por derivacao) e os 9 meios de prova em especie (pericia e
cadeia de custodia -- arts. 158 a 158-F --, demais exames periciais,
interrogatorio judicial, confissao, perguntas ao ofendido, testemunhas,
reconhecimento de pessoas e coisas, acareacao, documentos, indicios, e
busca e apreensao).

Diferente dos PDFs anteriores, este nao trazia uma "Maratona" de
questoes prontas -- e um material 100% teorico. Por isso todas as 24
questoes abaixo sao originais, elaboradas a partir do proprio conteudo
teorico incorporado, priorizando os pontos mais cobrados e as pegadinhas
mais classicas de cada subtema (prova x elemento de informacao; sistema
acusatorio x iniciativa do juiz; exame de corpo de delito; cadeia de
custodia; interrogatorio; testemunhas/dispensa; busca e apreensao).

Este script cuida so de: (1) acrescentar as questoes a questions.json,
(2) regenerar estudo-cebraspe-ma.html a partir do app-template.html ja
editado.
"""
import json

ASSUNTO = "3 — Direito Processual Penal: Prova (Teoria Geral e Meios de Prova, arts. 155 a 250, CPP)"

MC_QUESTIONS = [
    (
        "Nos termos do art. 155 do CPP, assinale a alternativa correta quanto à distinção entre \"prova\" e \"elementos de informação\":",
        [
            "Prova e elemento de informação são sinônimos, podendo o juiz fundamentar a condenação exclusivamente nos elementos colhidos no inquérito.",
            "Prova é o que se produz, em regra, no curso do processo judicial, sob o crivo do contraditório e da ampla defesa; elemento de informação é o que se colhe na fase investigatória, sem a necessária participação das partes.",
            "Elemento de informação é sinônimo de prova cautelar, não repetível ou antecipada.",
            "O juiz pode fundamentar sua decisão exclusivamente em elementos de informação, desde que fundamente a sentença.",
            "Prova é apenas a produzida no inquérito policial; elemento de informação é a produzida em juízo.",
        ],
        1,
        ASSUNTO,
        "Correto o item B. O art. 155, caput, do CPP veda ao juiz fundamentar sua decisão EXCLUSIVAMENTE nos elementos informativos colhidos na investigação (ressalvadas as provas cautelares, não repetíveis e antecipadas), reservando o termo \"prova\" ao que é produzido em contraditório judicial.",
    ),
    (
        "Sobre as provas cautelares, não repetíveis e antecipadas (os chamados \"elementos migratórios\"), assinale a alternativa correta:",
        [
            "Prova não repetível é aquela que pode ser produzida novamente a qualquer momento, sem prejuízo.",
            "Prova cautelar é aquela em que há risco de desaparecimento do objeto da prova em razão do decurso do tempo.",
            "Prova antecipada é sempre produzida sem contraditório, por sua própria natureza de urgência.",
            "Nenhuma prova produzida no inquérito policial pode, em qualquer hipótese, fundamentar a decisão judicial.",
            "Prova cautelar, não repetível e antecipada são sinônimos de prova ilícita.",
        ],
        1,
        ASSUNTO,
        "Correto o item B. Prova cautelar é aquela em que há risco de desaparecimento do objeto da prova com o decurso do tempo. Prova não repetível é a que, uma vez produzida, não pode ser refeita por desaparecimento/destruição da fonte. Prova antecipada é produzida com contraditório REAL, perante autoridade judicial, em momento distinto do legalmente previsto, diante de urgência e relevância.",
    ),
    (
        "Quanto aos sistemas de valoração da prova pelo magistrado, assinale a alternativa correta:",
        [
            "O sistema da prova tarifada, em que a confissão teria valor máximo e vincularia o juiz, é o adotado pelo CPP.",
            "O sistema da íntima convicção, em que o juiz não precisa fundamentar seu convencimento, é o sistema regra do ordenamento brasileiro.",
            "O sistema do livre convencimento motivado, vigente no Brasil por força do art. 93, IX, da CF e do art. 155, caput, do CPP, confere ao juiz liberdade para valorar as provas dos autos, mas exige fundamentação da decisão.",
            "No sistema do livre convencimento motivado, o juiz pode valorar livremente provas que não constem dos autos do processo.",
            "O Brasil não adota nenhum dos três sistemas clássicos de valoração da prova.",
        ],
        2,
        ASSUNTO,
        "Correto o item C. O sistema do livre convencimento motivado (persuasão racional) é o vigente no Brasil: o juiz tem ampla liberdade para valorar as provas CONSTANTES DOS AUTOS, mas é obrigado a fundamentar sua decisão (art. 93, IX, CF; art. 155, caput, CPP). O sistema da prova tarifada e o da íntima convicção, como regra, NÃO foram adotados.",
    ),
    (
        "Em relação ao objeto da prova e aos fatos que dele independem, assinale a alternativa correta:",
        [
            "Fatos notórios são os conhecidos apenas por uma comunidade específica, ainda que desconhecidos nacionalmente.",
            "A inimputabilidade do menor de 18 anos é exemplo de fato que comporta presunção legal absoluta, não admitindo prova em sentido contrário.",
            "Fatos irrelevantes, impertinentes ou inúteis devem sempre ser objeto de prova, ainda que não digam respeito à solução da causa.",
            "Fatos axiomáticos ou intuitivos são aqueles que exigem sempre perícia complementar para serem considerados provados.",
            "Todo fato alegado pelas partes deve ser necessariamente objeto de prova, independentemente de sua relevância.",
        ],
        1,
        ASSUNTO,
        "Correto o item B. A inimputabilidade do menor de 18 anos é exemplo clássico de fato com presunção legal ABSOLUTA, que não comporta prova em sentido contrário. Fatos notórios são os NACIONALMENTE conhecidos (não os de uma comunidade específica); fatos irrelevantes/impertinentes/inúteis independem de prova, justamente por não dizerem respeito à solução da causa; fatos axiomáticos se autodemonstram, dispensando perícia (ex.: art. 162, CPP, na carbonização cadavérica).",
    ),
    (
        "Quanto à classificação da prova segundo os 4 critérios doutrinários, assinale a alternativa correta:",
        [
            "Quanto ao efeito ou valor, a prova se classifica em direta ou indireta, conforme sua relação com o fato a ser provado.",
            "Quanto ao sujeito ou causa, a prova pode ser plena (apta a gerar certeza) ou não plena/indiciária (apta a gerar apenas probabilidade).",
            "Quanto ao objeto, a prova pode ser real (coisas, como perícia e documentos) ou pessoal (declarações, como testemunho e interrogatório).",
            "Quanto à forma ou aparência, a prova se revela no processo como testemunhal, documental ou material/pericial.",
            "Os 4 critérios de classificação da prova são sinônimos dos 3 sistemas de valoração da prova.",
        ],
        3,
        ASSUNTO,
        "Correto o item D. Quanto à FORMA OU APARÊNCIA, a prova se revela como testemunhal, documental ou material/pericial. Os demais itens trocam os critérios: direta/indireta é o critério do OBJETO; plena/não plena é o critério do EFEITO OU VALOR; real/pessoal é o critério do SUJEITO OU CAUSA (não do objeto). Classificação da prova e sistemas de valoração são temas distintos.",
    ),
    (
        "Sobre o ônus da prova e a iniciativa probatória do juiz no processo penal, assinale a alternativa correta:",
        [
            "Cabe à defesa demonstrar a autoria e a materialidade do crime, e à acusação as causas de exclusão de ilicitude.",
            "O art. 156 do CPP veda, de forma absoluta, qualquer iniciativa do juiz na produção de provas, inclusive para dirimir dúvida sobre ponto relevante já durante a instrução.",
            "O art. 156 do CPP permite ao juiz, mesmo ainda na fase do inquérito policial, valer-se de ofício de medidas cautelares, desde que observados necessidade, proporcionalidade e adequação — o que convive com o sistema acusatório do art. 3º-A, que veda ao juiz iniciar a investigação ou substituir a atuação probatória da acusação.",
            "O sistema acusatório (art. 3º-A, CPP) permite ao juiz iniciar de ofício a investigação criminal sempre que entender necessário.",
            "O ônus da prova pode ser transferido ao magistrado sempre que a acusação não produzir provas suficientes.",
        ],
        2,
        ASSUNTO,
        "Correto o item C. O art. 156 do CPP permite ao juiz dirimir dúvida relevante na instrução (reinterrogar réu, ouvir testemunha referida) e, ainda na fase de inquérito, valer-se de ofício de medidas cautelares (necessidade/proporcionalidade/adequação) — hipóteses pontuais que coexistem com o sistema acusatório (art. 3º-A), que veda a iniciativa do juiz na fase de INVESTIGAÇÃO e a substituição da atuação probatória da acusação. O ônus é da acusação (autoria/materialidade) e da defesa (excludentes), não o inverso.",
    ),
    (
        "Quanto às provas ilícitas e à prova ilícita por derivação, assinale a alternativa correta:",
        [
            "Provas ilícitas são as produzidas mediante violação de normas de direito processual, e não de direito material.",
            "A Teoria dos Frutos da Árvore Envenenada estabelece que a prova derivada de uma prova ilícita é sempre válida, independentemente do nexo entre elas.",
            "A fonte independente (§2º, art. 157, CPP) é uma das exceções à contaminação da prova derivada, aplicável quando se obtém legitimamente novos elementos a partir de fonte autônoma, não decorrente da prova originariamente ilícita.",
            "A utilização da prova ilícita \"pro societate\", em prejuízo do réu, é amplamente admitida pela doutrina e pela jurisprudência.",
            "Preclusa a decisão de desentranhamento da prova ilícita, esta deve permanecer nos autos para consulta das partes.",
        ],
        2,
        ASSUNTO,
        "Correto o item C. A fonte independente é uma das 3 exceções à Teoria dos Frutos da Árvore Envenenada (as outras são a inexistência de nexo e a utilização \"pro reo\"). Provas ilícitas violam normas de direito MATERIAL (constitucionais ou legais); a utilização \"pro societate\" NÃO é admitida; preclusa a decisão de desentranhamento, a prova ilícita é INUTILIZADA (art. 157, §3º, CPP).",
    ),
    (
        "Acerca do exame de corpo de delito, assinale a alternativa correta:",
        [
            "Quando a infração deixar vestígios, o exame de corpo de delito é indispensável, não podendo a confissão do acusado supri-lo.",
            "Delitos transeuntes são os que deixam vestígios materiais, exigindo sempre exame pericial.",
            "O exame indireto ocorre quando os peritos atuam diretamente sobre os vestígios deixados pela infração.",
            "A confissão do acusado sempre supre a ausência de exame de corpo de delito, mesmo quando possível sua realização.",
            "O exame de corpo de delito é sempre obrigatório, mesmo nas infrações de menor potencial ofensivo.",
        ],
        0,
        ASSUNTO,
        "Correto o item A. Art. 158, CPP: havendo vestígios, o exame de corpo de delito é INDISPENSÁVEL, não podendo a confissão do acusado supri-lo. Delitos TRANSEUNTES são os que NÃO deixam vestígios (o oposto do item B); o exame INDIRETO ocorre quando os peritos NÃO dispõem mais dos vestígios (o oposto do item C); e o exame é dispensado nas infrações de menor potencial ofensivo, com boletim médico ou prova equivalente (art. 77, §1º, Lei 9.099/95).",
    ),
    (
        "Sobre quem pode realizar o exame de corpo de delito e a figura do assistente técnico, assinale a alternativa correta:",
        [
            "Na falta de perito oficial, o exame deve ser feito exclusivamente por profissional com diploma de curso superior na área específica.",
            "O assistente técnico é o perito da confiança do contratante e seu parecer técnico só é admitido após a conclusão do laudo oficial, dependendo de deliberação judicial.",
            "O assistente técnico substitui o perito oficial sempre que nomeado pelas partes, dispensando o laudo oficial.",
            "Em caso de perícia complexa, é vedado ao juiz designar mais de um perito.",
            "O prazo para elaboração do laudo pericial é de 30 dias, improrrogáveis.",
        ],
        1,
        ASSUNTO,
        "Correto o item B. O assistente técnico não se confunde com o perito oficial: é de confiança do contratante, e seu parecer só é admitido APÓS a conclusão do laudo pelos peritos da autoridade, dependendo de deliberação judicial. Na falta de perito oficial, bastam duas pessoas idôneas com diploma superior, PREFERENCIALMENTE (não exclusivamente) na área específica; em perícia complexa, o juiz PODE designar mais de um perito; e o prazo do laudo é de 10 dias, prorrogáveis em casos excepcionais.",
    ),
    (
        "Quanto à cadeia de custódia (arts. 158-A a 158-F, CPP), assinale a alternativa correta:",
        [
            "A cadeia de custódia tem início apenas com a chegada do vestígio à central de custódia, não alcançando o momento de sua coleta no local do crime.",
            "Vestígio, segundo a lei, é apenas o objeto visível e já identificado como relacionado à infração, excluindo-se materiais latentes.",
            "O início da cadeia de custódia dá-se com a preservação do local de crime ou com procedimentos policiais/periciais em que se detecte a existência de vestígio.",
            "A etapa de \"reconhecimento\" consiste no armazenamento final do vestígio após o processamento pericial.",
            "A entrada em locais isolados ou a remoção de vestígios antes da liberação pelo perito responsável é conduta lícita, desde que autorizada por qualquer autoridade policial.",
        ],
        2,
        ASSUNTO,
        "Correto o item C. O art. 158-A, §1º, CPP estabelece que a cadeia de custódia tem início com a preservação do local de crime ou com procedimentos policiais/periciais em que se detecte vestígio. Vestígio é todo objeto ou material BRUTO, visível OU LATENTE; \"reconhecimento\" é a PRIMEIRA etapa (distinguir um elemento de potencial interesse), não a última; e a entrada em locais isolados/remoção de vestígios antes da liberação pelo perito é tipificada como FRAUDE PROCESSUAL (art. 158-C, §2º, CPP, c/c art. 347, CP).",
    ),
    (
        "Assinale a alternativa que apresenta corretamente a ordem das etapas da cadeia de custódia previstas no art. 158-B do CPP:",
        [
            "Descarte, processamento, coleta, reconhecimento.",
            "Reconhecimento, isolamento, fixação, coleta, acondicionamento, transporte, recebimento, processamento, armazenamento, descarte.",
            "Armazenamento, transporte, isolamento, reconhecimento, descarte.",
            "Processamento, reconhecimento, descarte, fixação.",
            "Coleta, descarte, reconhecimento, isolamento, processamento.",
        ],
        1,
        ASSUNTO,
        "Correto o item B. É a ordem literal do art. 158-B, CPP: reconhecimento (I), isolamento (II), fixação (III), coleta (IV), acondicionamento (V), transporte (VI), recebimento (VII), processamento (VIII), armazenamento (IX) e descarte (X).",
    ),
    (
        "Sobre a autópsia e a exumação, assinale a alternativa correta:",
        [
            "O exame interno (visceral) da autópsia é sempre obrigatório, mesmo na carbonização cadavérica.",
            "O exame interno pode ser dispensado na morte violenta sem crime a apurar (ex.: suicídio) ou quando a análise externa for suficiente para precisar a causa da morte, sem circunstância relevante a esclarecer.",
            "A exumação consiste exclusivamente no exame externo do cadáver ainda sepultado, sem necessidade de desenterramento.",
            "A recusa do administrador do cemitério em contribuir para o encontro da sepultura não gera qualquer consequência penal.",
            "A autópsia é incompatível com o conceito de fato axiomático ou intuitivo previsto no art. 162 do CPP.",
        ],
        1,
        ASSUNTO,
        "Correto o item B. O exame interno pode ser dispensado em duas hipóteses: morte violenta sem crime a apurar (ex.: suicídio) e quando a análise externa já é suficiente para precisar a causa da morte, sem circunstância relevante pendente de esclarecimento (ex.: carbonização). A exumação é o ato de DESENTERRAR o cadáver; e a recusa do administrador do cemitério configura crime de DESOBEDIÊNCIA (art. 330, CP).",
    ),
    (
        "No crime de lesão corporal grave por incapacidade para as ocupações habituais por mais de 30 dias (art. 129, §1º, I, CP), o laudo pericial complementar previsto no art. 168 do CPP:",
        [
            "Deve ser realizado imediatamente após o fato, antes de decorridos 30 dias.",
            "É dispensado sempre que o primeiro exame pericial for completo.",
            "Deve ser realizado tão logo decorra o prazo de 30 dias contado da data do crime, quando se busca a exata classificação do delito.",
            "Só pode ser requerido pelo Ministério Público, sendo vedada a iniciativa de ofício da autoridade.",
            "Substitui integralmente o primeiro exame de corpo de delito, que se torna dispensável.",
        ],
        2,
        ASSUNTO,
        "Correto o item C. O exame complementar deve ser realizado tão logo decorra o prazo de 30 dias da data do crime, para aferir se a incapacidade persiste e classificar corretamente o delito (art. 168, §2º, CPP). Pode ser determinado de ofício pela autoridade policial/judiciária, ou a requerimento do MP, do ofendido, do acusado ou de seu defensor — e não dispensa o primeiro exame.",
    ),
    (
        "No crime de furto qualificado por destruição/rompimento de obstáculo ou por escalada (art. 155, §4º, I e II, CP), é correto afirmar que:",
        [
            "A destruição ou rompimento de obstáculo dispensa sempre o exame pericial, por não deixar vestígios.",
            "A escalada sempre deixa vestígios, exigindo perícia obrigatória em todos os casos.",
            "A destruição/rompimento de obstáculo sempre deixa vestígios, exigindo corpo de delito (suprido pela prova testemunhal se os vestígios desaparecerem); já a escalada pode ou não deixar vestígios, admitindo-se outros meios de prova quando não os deixar.",
            "Ambas as qualificadoras dependem exclusivamente de confissão do acusado para sua comprovação.",
            "Nenhuma das duas qualificadoras admite prova testemunhal em qualquer hipótese.",
        ],
        2,
        ASSUNTO,
        "Correto o item C. A destruição/rompimento de obstáculo SEMPRE deixa vestígios (exigindo corpo de delito, suprido por prova testemunhal se os vestígios desaparecerem, art. 167, CPP); já a escalada PODE ou não deixar vestígios — se não deixar, admitem-se outros meios de prova (monitoramento, filmagem, testemunhas).",
    ),
    (
        "Sobre o interrogatório judicial, assinale a alternativa correta:",
        [
            "Desde a reforma de 2008, o interrogatório passou a ser o primeiro ato da instrução processual, antes da oitiva de testemunhas.",
            "O silêncio do acusado durante o interrogatório pode ser utilizado pelo juiz como fundamento para a condenação.",
            "Desde a reforma de 2008, o interrogatório é o último ato da instrução processual (art. 400, CPP), e o silêncio é direito do acusado, não podendo fundamentar condenação.",
            "O interrogatório é ato sigiloso por natureza, incompatível com o princípio da publicidade.",
            "O interrogatório pode ser delegado a terceiros, dispensando a presença do magistrado.",
        ],
        2,
        ASSUNTO,
        "Correto o item C. Com a reforma de 2008, o interrogatório passou a ser o ÚLTIMO ato da instrução processual (art. 400, CPP) — e não o primeiro. O silêncio é direito do acusado e jamais pode ser usado para fundamentar condenação. O interrogatório é, ao contrário, ato de PUBLICIDADE, e deve ser realizado pelo próprio magistrado (ato personalíssimo quanto ao julgador).",
    ),
    (
        "Quanto à natureza jurídica do interrogatório, segundo as correntes doutrinárias, assinale a alternativa correta:",
        [
            "A corrente que defende ser o interrogatório exclusivamente meio de prova se baseia no fato de estar inserido topograficamente no capítulo do CPP que trata das provas.",
            "Não há divergência doutrinária quanto à natureza jurídica do interrogatório, sendo pacífico tratar-se apenas de meio de defesa.",
            "A posição majoritária nega qualquer natureza de meio de prova ao interrogatório, considerando-o exclusivamente meio de defesa.",
            "A corrente da natureza mista ou híbrida é minoritária, prevalecendo a tese de que o interrogatório é só meio de prova.",
            "O interrogatório nunca pode ser considerado meio de prova, ainda que o réu deseje falar sobre os fatos.",
        ],
        0,
        ASSUNTO,
        "Correto o item A. Uma das 4 correntes doutrinárias sustenta que o interrogatório é meio de prova justamente por sua posição TOPOGRÁFICA no CPP (Capítulo III, Título VII — Da Prova). Há sim divergência doutrinária (4 correntes); a posição MAJORITÁRIA é a de natureza MISTA/HÍBRIDA (meio de prova E de defesa), não exclusivamente uma ou outra.",
    ),
    (
        "Sobre o local de realização do interrogatório do réu preso e a videoconferência, assinale a alternativa correta:",
        [
            "O réu preso só pode ser interrogado pessoalmente dentro do presídio, sendo vedada qualquer outra forma.",
            "A videoconferência é vedada em qualquer hipótese no processo penal brasileiro, por violar a publicidade.",
            "Entre as finalidades da videoconferência está impedir a influência do réu no ânimo da testemunha ou da vítima, quando não for possível colher o depoimento destas por videoconferência.",
            "A apresentação do réu preso no fórum é a única forma admitida de interrogatório, excluindo-se o presídio e a videoconferência.",
            "A videoconferência só pode ser utilizada a pedido exclusivo da defesa, nunca por iniciativa do juízo.",
        ],
        2,
        ASSUNTO,
        "Correto o item C. É uma das 4 finalidades da videoconferência (art. 185, §2º, CPP): impedir a influência do réu no ânimo da testemunha ou da vítima, quando não for possível colher o depoimento delas por videoconferência. O réu preso pode ser interrogado de 3 formas: no presídio, por videoconferência, ou no fórum (quando as duas primeiras não forem possíveis).",
    ),
    (
        "Sobre a confissão no processo penal, assinale a alternativa correta:",
        [
            "A confissão é indivisível, devendo o juiz considerá-la integralmente ou rejeitá-la por completo.",
            "A confissão é divisível e retratável; a retratação, contudo, não vincula o juiz, que pode se valer da confissão anterior ao sentenciar.",
            "Uma vez retratada, a confissão anterior não pode, em nenhuma hipótese, ser utilizada pelo juiz no momento da sentença.",
            "A confissão recai sobre o direito aplicável ao caso, e não sobre os fatos.",
            "A retratação da confissão dispensa a realização de novo interrogatório do acusado.",
        ],
        1,
        ASSUNTO,
        "Correto o item B. A confissão é DIVISÍVEL (o juiz pode considerar só parte dela) e RETRATÁVEL (o réu pode voltar atrás) — mas a retratação não vincula o juiz, que pode utilizar a confissão anterior ao sentenciar (art. 200, CPP), por força do livre convencimento motivado. A retratação exige, inclusive, novo interrogatório.",
    ),
    (
        "Em relação às perguntas ao ofendido (art. 201, CPP), é correto afirmar que:",
        [
            "O ofendido é considerado testemunha para todos os efeitos, respondendo por falso testemunho se mentir.",
            "O ofendido não é considerado testemunha, não respondendo por falso testemunho, mas podendo responder por denunciação caluniosa.",
            "O ofendido não tem qualquer obrigação de comparecer aos atos processuais, ainda que devidamente intimado.",
            "A ausência injustificada do ofendido jamais pode ensejar condução coercitiva.",
            "O ofendido só pode comparecer aos atos processuais se representado por advogado.",
        ],
        1,
        ASSUNTO,
        "Correto o item B. O ofendido NÃO é testemunha (não presta compromisso de dizer a verdade, não cometendo falso testemunho), mas pode responder por denunciação caluniosa. É obrigado a comparecer quando intimado, sob pena de condução coercitiva e, eventualmente, responsabilização por desobediência.",
    ),
    (
        "Quanto à dispensa do dever de depor e à dispensa do dever de prestar compromisso das testemunhas, assinale a alternativa correta:",
        [
            "Ambas as dispensas produzem exatamente os mesmos efeitos jurídicos, sendo termos sinônimos no CPP.",
            "A dispensa do dever de depor (art. 206, CPP) alcança o cônjuge, ainda que separado, e os ascendentes/descendentes do réu, podendo estes se recusar a depor, salvo quando for o único meio de prova disponível.",
            "Menores de 14 anos têm o dever de depor e de prestar compromisso, nos mesmos termos de qualquer outra testemunha adulta.",
            "A dispensa do dever de prestar compromisso (art. 208, CPP) exime a testemunha do próprio dever de comparecer e depor.",
            "A testemunha, assim como o réu, tem direito ao silêncio quanto aos fatos.",
        ],
        1,
        ASSUNTO,
        "Correto o item B. O art. 206, parte final, do CPP dispensa do DEVER DE DEPOR o cônjuge (ainda que separado), ascendente, descendente, afim em linha reta, irmão, pai, mãe e filho adotivo do réu — podendo se recusar a depor, salvo quando o testemunho for o único meio de prova disponível (hipótese em que depõem sem compromisso). Já o art. 208 dispensa apenas o DEVER DE PRESTAR COMPROMISSO (não o dever de depor) de doentes, deficientes mentais, menores de 14 anos e das pessoas do art. 206. A testemunha, diferente do réu, NÃO tem direito ao silêncio.",
    ),
    (
        "Sobre o reconhecimento de pessoas e coisas, assinale a alternativa correta:",
        [
            "O reconhecimento por fotografia é prova nominada, expressamente prevista no art. 226 do CPP, e pode, por si só, embasar uma condenação.",
            "O retrato falado é meio de prova idôneo para, isoladamente, fundamentar uma condenação penal.",
            "O reconhecimento por fotografia é prova inominada, devendo seguir o mesmo procedimento do reconhecimento pessoal, servindo apenas como etapa antecedente a eventual reconhecimento pessoal, não bastando, isoladamente, para embasar a condenação.",
            "Havendo risco de intimidação, a cautela de evitar que o reconhecido veja o reconhecedor (art. 226, III, CPP) também se aplica normalmente em plenário do júri.",
            "Se várias pessoas forem chamadas a reconhecer o mesmo indivíduo, devem fazê-lo em conjunto, para fins de confirmação mútua.",
        ],
        2,
        ASSUNTO,
        "Correto o item C. O reconhecimento por fotografia é prova INOMINADA (o art. 226 fala em pessoas e coisas, não em fotografia), devendo seguir o mesmo procedimento do reconhecimento pessoal e servindo como etapa antecedente — não serve, sozinho, como prova em ação penal (STJ, HC 598.886-SC). O retrato falado NÃO é meio de prova, só auxilia investigações. A cautela do inciso III do art. 226 NÃO se aplica na instrução criminal ou em plenário de julgamento (parágrafo único). E cada reconhecedor deve atuar em SEPARADO, sem comunicação entre si (art. 228, CPP).",
    ),
    (
        "Sobre a acareação (arts. 229 e 230, CPP), assinale a alternativa correta:",
        [
            "A acareação só pode ser realizada na fase processual, sendo vedada durante o inquérito policial.",
            "A acareação pode ocorrer tanto na fase investigatória (art. 6º, VI, CPP) quanto na fase processual, e pode envolver, entre outras combinações, acusado com ofendido e testemunha com ofendido.",
            "Somente acusados podem ser acareados entre si, sendo vedada a acareação entre testemunhas.",
            "A acareação é sinônimo do reconhecimento de pessoas e coisas, previsto no mesmo dispositivo legal.",
            "A acareação exige sempre a presença de um perito oficial para sua validade.",
        ],
        1,
        ASSUNTO,
        "Correto o item B. A acareação pode ocorrer na fase investigatória (art. 6º, VI, CPP) ou na processual, admitindo diversas combinações: acusado-acusado, acusado-testemunha, testemunha-testemunha, acusado-ofendido, testemunha-ofendido e ofendido-ofendido.",
    ),
    (
        "Sobre documentos e indícios no processo penal, assinale a alternativa correta:",
        [
            "O CPP adotou conceito amplo de documento, abrangendo qualquer suporte de informação, inclusive gravações e fotografias, sob o mesmo regime dos arts. 213 a 238.",
            "As cartas particulares interceptadas ou obtidas por meios criminosos são admitidas em juízo, desde que relevantes para a elucidação do fato.",
            "Indício, segundo o art. 239 do CPP, é a circunstância conhecida e provada que, tendo relação com o fato, autorize, por indução, concluir-se a existência de outra circunstância — tendo valor probatório relativo.",
            "Indícios têm valor probatório absoluto, vinculando necessariamente o juiz a uma condenação.",
            "A prova documental não pode ser produzida a qualquer tempo, estando sempre sujeita a prazo preclusivo rígido.",
        ],
        2,
        ASSUNTO,
        "Correto o item C. É a definição literal do art. 239, CPP, com o indício tendo valor RELATIVO (pode embasar absolvição ou condenação, conforme o restante da instrução). O CPP adotou conceito RESTRITO de documento (escritos, instrumentos ou papéis); as cartas particulares interceptadas ilicitamente NÃO são admitidas (art. 233, CPP); e a prova documental pode, em regra, ser produzida a qualquer tempo, salvo vedação legal expressa.",
    ),
    (
        "Sobre a busca e apreensão, assinale a alternativa correta quanto à sua natureza jurídica e ao horário de cumprimento do mandado:",
        [
            "A busca e apreensão, apesar de topograficamente inserida no capítulo da prova, tem natureza jurídica de meio de OBTENÇÃO de prova, e não de meio de prova em si.",
            "O art. 241 do CPP, que permite à autoridade policial realizar busca domiciliar sem mandado judicial, foi integralmente recepcionado pela CF/88.",
            "A busca domiciliar pode ser cumprida a qualquer hora, inclusive à noite, independentemente do consentimento do morador, em qualquer situação.",
            "Em crimes permanentes como o tráfico de drogas, não é possível o ingresso em residência sem mandado, mesmo diante de flagrante delito.",
            "O mandado de busca pode ser genérico quanto ao local, desde que indique a autoridade responsável pelo cumprimento.",
        ],
        0,
        ASSUNTO,
        "Correto o item A. Embora inserida topograficamente no capítulo da prova, a busca e apreensão tem natureza jurídica de meio de OBTENÇÃO de prova. O art. 241 do CPP, na parte que dispensa mandado judicial, NÃO foi recepcionado pela CF/88; a busca domiciliar deve ser cumprida de DIA, salvo consentimento do morador para a noite (art. 5º, XI, CF); em crimes PERMANENTES com flagrante delito, o ingresso é possível a qualquer hora, SEM mandado; e o mandado não pode ser genérico (art. 243, CPP).",
    ),
    (
        "Sobre a busca pessoal e a apreensão de smartphones, assinale a alternativa correta:",
        [
            "A busca pessoal sempre depende de prévia autorização judicial, sendo vedada a abordagem policial por fundada suspeita.",
            "A busca em mulher deve, em regra, ser feita por outra mulher, admitindo-se a realização por homem se a espera por agente feminino importar retardamento ou prejuízo da diligência.",
            "O acesso ao WhatsApp de investigado preso em flagrante, sem qualquer autorização judicial, é considerado prova lícita pela jurisprudência.",
            "A apreensão do celular com mandado de busca e apreensão válido impede, em qualquer hipótese futura, o acesso ao seu conteúdo.",
            "O acesso ao WhatsApp da vítima morta, mesmo com autorização do cônjuge sobrevivente, é sempre considerado prova ilícita, por ausência de autorização judicial.",
        ],
        1,
        ASSUNTO,
        "Correto o item B. O art. 249, CPP determina que a busca em mulher seja feita por outra mulher, admitindo-se exceção (busca por homem) quando a espera por agente feminino importar retardamento ou prejuízo da diligência. A busca pessoal INDEPENDE de autorização judicial quando há fundada suspeita; acessar o WhatsApp do investigado sem autorização é PROVA ILÍCITA; já acessar o WhatsApp de vítima morta com autorização do cônjuge é considerado PROVA VÁLIDA pela jurisprudência indicada no material.",
    ),
]


def main():
    with open('questions.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    max_id = max(q['id'] for q in data)

    new_objs = []
    for i, (enun, alts, resp, assunto, exp) in enumerate(MC_QUESTIONS, start=1):
        new_objs.append({
            "id": max_id + i,
            "corp": "PCPE",
            "disc": "Direito Processual Penal",
            "tipo": "MC",
            "enun": enun,
            "alts": alts,
            "resp": resp,
            "exp": exp,
            "assunto": assunto,
        })

    with open('questions.json', 'w', encoding='utf-8', newline='') as f:
        f.write('[' + json.dumps(data[0], ensure_ascii=False))
        for q in data[1:]:
            f.write('\r\n, ' + json.dumps(q, ensure_ascii=False))
        for q in new_objs:
            f.write('\r\n, ' + json.dumps(q, ensure_ascii=False))
        f.write(']')

    print(f"Added {len(new_objs)} new questions, ids {max_id+1}..{max_id+len(new_objs)}")

    with open('app-template.html', 'r', encoding='utf-8') as f:
        template = f.read()
    with open('questions.json', 'r', encoding='utf-8') as f:
        questions_json = f.read()
    final_html = template.replace('__QUESTIONS_JSON__', questions_json)
    with open('estudo-cebraspe-ma.html', 'w', encoding='utf-8', newline='') as f:
        f.write(final_html)
    print("Regenerated estudo-cebraspe-ma.html")


if __name__ == '__main__':
    main()
