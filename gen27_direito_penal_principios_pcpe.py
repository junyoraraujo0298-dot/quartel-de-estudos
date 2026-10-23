# -*- coding: utf-8 -*-
# Adiciona conteudo de Direito Penal (Principios do Direito Penal) pra
# PC-PE: um deck de teoria na aba Teoria (corp PCPE) resumindo os
# principios cobrados no edital, e um lote de questoes Certo/Errado
# (formato CEBRASPE) extraidas do material da Focus Concursos,
# cobrindo os mesmos principios. Fonte: PDF Focado "Direito Penal -
# Principios do Direito Penal", Prof. Lucas Favero, Focus Concursos.
import re
import json

with open('app-template.html', encoding='utf-8') as f:
    html = f.read()

TEORIA_ITEMS = [
    {"t": "tit", "x": "DIREITO PENAL — PRINCÍPIOS DO DIREITO PENAL (PC-PE)"},
    {"t": "art", "n": "Conceito",
     "x": "Princípios são valores fundamentais que inspiram a criação, aplicação e manutenção do "
          "ordenamento jurídico. No Direito Penal, orientam o legislador e o aplicador da lei penal, com "
          "a finalidade de limitar o poder punitivo estatal mediante a imposição de garantias aos "
          "cidadãos. Podem ser explícitos (previstos em texto de lei/Constituição) ou implícitos "
          "(decorrentes de interpretação)."},
    {"t": "art", "n": "Princípio da Legalidade",
     "x": "Nullum crimen, nulla poena sine lege — não há crime sem lei anterior que o defina, nem pena "
          "sem prévia cominação legal (art. 5º, XXXIX, CF; art. 1º, CP). É o princípio mais cobrado em "
          "prova, pois se desdobra em quatro funções/subprincípios.",
     "s": "O princípio da legalidade é o 'guarda-chuva' que contém os outros quatro abaixo — toda questão "
          "sobre reserva legal, anterioridade, taxatividade ou proibição de analogia está, no fundo, "
          "testando o princípio da legalidade."},
    {"t": "art", "n": "1ª função: Princípio da Reserva Legal",
     "x": "Proíbe a criação de crimes e penas pelos costumes — a lei penal deve ser escrita. Compete "
          "privativamente à União legislar sobre Direito Penal (art. 22, I, CF). É vedada a edição de "
          "medida provisória sobre matéria penal (art. 62, §1º, I, 'b', CF) — mas o STF admite MP em "
          "matéria penal quando benéfica ao agente."},
    {"t": "art", "n": "2ª função: Princípio da Anterioridade (ou Irretroatividade)",
     "x": "Proíbe a retroatividade da lei penal gravosa — a lei deve ser anterior ao fato que se pretende "
          "punir (art. 5º, XXXIX, CF). Exceção: a lei penal benéfica ao réu pode retroagir (retroatividade "
          "da lei benéfica) — a esse movimento de leis no tempo dá-se o nome de extratividade."},
    {"t": "art", "n": "3ª função: Princípio da Taxatividade",
     "x": "Proíbe incriminações vagas e indeterminadas — a lei penal deve descrever a conduta criminosa "
          "de maneira clara e precisa. Um tipo penal vago ou impreciso é considerado inconstitucional por "
          "violar a taxatividade."},
    {"t": "art", "n": "4ª função: Proibição da Analogia 'in malam partem'",
     "x": "Não se pode aplicar a um caso omisso a lei maléfica ao réu que disciplina caso semelhante — a "
          "lei penal deve ser estrita. Permite-se, contudo, a analogia 'in bonam partem' (em benefício do "
          "réu).",
     "s": "Pegadinha clássica: a vedação de analogia só vale 'in malam partem' — contra o réu. Analogia "
          "'in bonam partem', que beneficia o réu, é permitida no Direito Penal."},
    {"t": "art", "n": "Princípio da Humanidade / Dignidade da Pessoa Humana",
     "x": "Visa evitar tratamento cruel ou desrespeito às premissas básicas do cidadão (art. 1º, III, CF). "
          "Penas proibidas (art. 5º, XLVII, CF): de morte (salvo guerra declarada), de caráter perpétuo, "
          "de trabalhos forçados, de banimento, e cruéis."},
    {"t": "art", "n": "Princípio da Ofensividade / Lesividade",
     "x": "Nullum crimen sine injuria — só há crime se a conduta provocar lesão ao bem jurídico ou, ao "
          "menos, perigo concreto de lesão. Consequência: são questionáveis os crimes de perigo abstrato "
          "(presumido). A autolesão não configura crime (princípio da alteridade). Não se pune, como "
          "regra, atos preparatórios ou simples cogitação. O princípio da exclusiva proteção ao bem "
          "jurídico veda a criminalização de pensamentos, ideias e teses."},
    {"t": "art", "n": "Princípio da Intervenção Mínima",
     "x": "O Direito Penal é a 'ultima ratio' — só deve intervir quando os demais ramos do direito forem "
          "insuficientes. Divide-se em dois: Fragmentariedade (dirigida ao LEGISLADOR — só se tipificam "
          "como crime as ofensas mais graves aos bens jurídicos mais importantes) e Subsidiariedade "
          "(dirigida ao JUIZ — o Direito Penal só é aplicado no caso concreto quando os demais ramos se "
          "mostrarem ineficazes, funcionando como 'soldado de reserva').",
     "s": "Fragmentariedade = legislador (abstrato, na hora de criar a lei). Subsidiariedade = juiz "
          "(concreto, na hora de aplicar a lei ao caso)."},
    {"t": "art", "n": "Princípio da Insignificância / Bagatela",
     "x": "Evita punir crimes de bagatela (ninharia) — a conduta já nasce atípica (exclusão da tipicidade "
          "material). Requisitos do STF/STJ: mínima ofensividade da conduta, ausência de periculosidade "
          "social da ação, reduzido grau de reprovabilidade do comportamento, e inexpressividade da lesão "
          "jurídica (mnemônico MARI). Súmula 589/STJ: inaplicável nos crimes contra a mulher no âmbito "
          "doméstico. Súmula 599/STJ: inaplicável aos crimes contra a administração pública. Súmula "
          "606/STJ: inaplicável à transmissão clandestina de sinal de internet. Também inaplicável, por "
          "jurisprudência, a: tráfico de drogas, roubo, moeda falsa, reincidente contumaz e furto "
          "qualificado. Não se confunde com a insignificância IMPRÓPRIA (bagatela imprópria): nela o fato "
          "nasce relevante, mas depois se constata a desnecessidade da pena (ex.: colaboração com a "
          "justiça) — funciona como 'perdão judicial', causa SUPRALEGAL de extinção da punibilidade."},
    {"t": "art", "n": "Princípio da Individualização da Pena",
     "x": "A pena deve ser individualizada ao infrator, considerando aspectos subjetivos e objetivos do "
          "crime (art. 5º, XLVI, CF). Ocorre em três fases: legislativa (cominação — escolha das espécies "
          "de pena), judiciária (aplicação — fixação da pena pelo juiz) e administrativa (execução — "
          "cumprimento da pena após o trânsito em julgado, na forma da LEP)."},
    {"t": "art", "n": "Princípio da Culpabilidade / Responsabilidade Penal",
     "x": "Não tem previsão expressa na Constituição (é implícito). O sujeito só pode ser responsabilizado "
          "se sua conduta for dolosa ou culposa — não se admite responsabilidade penal objetiva. Possui "
          "dois sentidos: culpabilidade como elemento do conceito analítico de crime, e culpabilidade como "
          "princípio medidor da pena."},
    {"t": "art", "n": "Princípio da Pessoalidade / Intranscendência da Pena",
     "x": "Nenhuma pena passará da pessoa do condenado (art. 5º, XLV, CF) — mas a obrigação de reparar o "
          "dano e a decretação de perdimento de bens podem, nos termos da lei, ser estendidas aos "
          "sucessores e contra eles executadas, ATÉ O LIMITE do valor do patrimônio transferido (não "
          "ilimitadamente).",
     "s": "Pegadinha recorrente: a responsabilidade civil dos sucessores é limitada ao patrimônio "
          "transferido — nunca 'ilimitadamente'."},
    {"t": "art", "n": "Princípio da Materialização do Fato / Responsabilidade do Fato",
     "x": "A pena deve se basear em um fato lesivo concreto, e não no modo de ser do sujeito (direito "
          "penal do fato, não do autor). Vedada incriminação fundada exclusivamente nas condições "
          "pessoais do agente ou em mera cogitação."},
    {"t": "art", "n": "Princípio do 'Ne Bis In Idem'",
     "x": "Não se pode punir ou processar o indivíduo mais de uma vez pelo mesmo fato — litispendência se "
          "ainda em curso, coisa julgada se já decidido. Proíbe também que um fato configure mais de uma "
          "norma incriminadora (ex.: 6 tiros que matam = 1 homicídio, não 5 lesões + 1 homicídio). "
          "Exceção: extraterritorialidade incondicionada da lei penal brasileira (art. 7º, I e §1º, c/c "
          "art. 8º, CP). O STF admite excepcionar o princípio quando o julgamento no exterior não foi "
          "justo e legítimo."},
    {"t": "art", "n": "Princípio da Presunção de Inocência",
     "x": "Ninguém será considerado culpado até o trânsito em julgado de sentença penal condenatória "
          "(art. 5º, LVII, CF). Regra probatória: cabe à acusação provar, não ao réu provar sua inocência "
          "(in dubio pro reo). O STF (ADCs 43, 44 e 54) entende que a execução provisória de pena antes do "
          "trânsito em julgado viola esse princípio."},
    {"t": "art", "n": "Adequação Social",
     "x": "Afasta a reprovação penal de condutas que a sociedade não reprova socialmente, mesmo que "
          "formalmente típicas. Exemplos de debate: jogo do bicho, bigamia. NÃO se aplica, segundo "
          "jurisprudência do STJ (Súmula 502), à venda de CDs/DVDs piratas — mera leniência social não "
          "equivale a adequação social."},
    {"t": "art", "n": "Princípio da Proporcionalidade",
     "x": "Deve haver equilíbrio entre a gravidade do crime e a resposta estatal (pena), observado em "
          "dois planos: proibição do excesso e proteção insuficiente de bens jurídicos. Tem três "
          "destinatários: legislador, juiz e órgãos de execução penal."},
    {"t": "art", "n": "Princípio da Isonomia (Igualdade)",
     "x": "Tratamento igual aos iguais e desigual aos desiguais, na medida de suas desigualdades (art. 5º, "
          "caput, CF)."},
]

CE_QUESTIONS = [
    ("O princípio da legalidade veda a existência de crime sem lei que o defina e impede a existência de "
     "pena sem cominação legal.", True, "Princípio da Legalidade",
     "Correto — é a própria redação do art. 5º, XXXIX, da CF e do art. 1º do CP."),
    ("O princípio da legalidade ou da reserva legal impede a criação de crimes e a cominação de penas "
     "por medidas provisórias.", True, "Princípio da Reserva Legal",
     "Correto — o art. 62, §1º, I, 'b', da CF veda expressamente a edição de medida provisória sobre "
     "matéria de direito penal."),
    ("O princípio da legalidade é conhecido pela seguinte expressão latina: nullum crimen, nulla poena "
     "sine lege.", True, "Princípio da Legalidade", "Correto — é a expressão latina clássica do princípio."),
    ("NÃO constitui situação de violação do princípio de legalidade: Incriminação com base em analogia.",
     False, "Princípio da Legalidade",
     "Errado — incriminar por analogia (in malam partem) É uma das formas clássicas de violação do "
     "princípio da legalidade."),
    ("NÃO constitui situação de violação do princípio de legalidade: Uso de norma penal em branco em "
     "sentido estrito.", True, "Princípio da Legalidade",
     "Correto — a norma penal em branco em sentido estrito (complementada por outra norma, não por ato "
     "do próprio órgão que a editou) é admitida e não viola a legalidade, desde que o núcleo essencial "
     "da conduta esteja na lei."),
    ("NÃO constitui situação de violação do princípio de legalidade: Retroatividade de lei incriminadora "
     "desfavorável ao réu.", False, "Princípio da Anterioridade",
     "Errado — a retroatividade de lei incriminadora desfavorável ao réu é justamente o que o princípio "
     "da anterioridade/irretroatividade proíbe."),
    ("NÃO constitui situação de violação do princípio de legalidade: Incriminação em casos dos chamados "
     "delitos de acumulação.", False, "Princípio da Legalidade",
     "Errado — delitos de acumulação (em que a conduta isolada é inofensiva, mas a acumulação de "
     "condutas semelhantes gera dano relevante) são criticados na doutrina justamente por tensionarem o "
     "princípio da ofensividade/legalidade."),
    ("Reza o princípio da reserva legal que não há crime sem lei anterior que o defina, nem pena sem "
     "prévia cominação legal.", True, "Princípio da Reserva Legal",
     "Correto — é a formulação clássica do princípio, compartilhada com a legalidade em sentido amplo."),
    ("O princípio da legalidade, que é desdobrado nos princípios da reserva legal e da anterioridade, não "
     "se aplica às medidas de segurança, que não possuem natureza de pena, pois a parte geral do Código "
     "Penal apenas se refere aos crimes e contravenções penais.", False, "Princípio da Legalidade",
     "Errado — o princípio da legalidade também se aplica às medidas de segurança, que exigem previsão "
     "legal prévia."),
    ("O princípio da legalidade penal, do qual decorre o princípio da reserva legal, impede o uso dos "
     "costumes e analogia para criar tipos penais incriminadores ou agravar as infrações existentes.",
     True, "Princípio da Reserva Legal",
     "Correto — costumes e analogia não podem criar ou agravar tipos penais, apenas a lei em sentido "
     "estrito."),
    ("Em 8/11/2021, Almir, visando conseguir dinheiro, utilizou uma arma de fogo para restringir a "
     "liberdade da empresária Emília, colocando-a em cativeiro e exigindo resgate; a polícia libertou a "
     "vítima dias depois. A partir dessa situação hipotética e considerando o direito penal vigente, "
     "julgue: o emprego da analogia in bonam partem não é admitido no direito penal, devido ao princípio "
     "da legalidade.", False, "Princípio da Legalidade",
     "Errado — a analogia in bonam partem (em benefício do réu) é admitida no direito penal; a legalidade "
     "veda apenas a analogia in malam partem."),
    ("A norma penal deve ser instituída por lei em sentido estrito, razão por que é proibida, em caráter "
     "absoluto, a analogia no direito penal, seja para criar tipo penal incriminador, seja para "
     "fundamentar ou alterar a pena.", False, "Princípio da Legalidade",
     "Errado — a proibição não é absoluta: a analogia in bonam partem (favorável ao réu) é permitida."),
    ("Em razão do princípio da legalidade penal, a tipificação de conduta como crime deve ser feita por "
     "meio de lei em sentido material, não se exigindo, em regra, a lei em sentido formal.", False,
     "Princípio da Legalidade",
     "Errado — exige-se lei em sentido ESTRITO (formal e material: aprovada pelo processo legislativo "
     "regular), não bastando o sentido meramente material."),
    ("O objetivo do direito penal moderno é exclusivamente a proteção de bens jurídicos, de modo que é "
     "vedada a criminalização de intenções, de pensamentos e de maneiras de viver, salvo se "
     "exteriorizadas de modo a, no mínimo, colocar em risco os referidos bens jurídicos, especialmente "
     "aqueles consagrados na própria Constituição Federal, como a saúde pública, o patrimônio e o meio "
     "ambiente.", True, "Princípio da Ofensividade/Exclusiva Proteção de Bens Jurídicos",
     "Correto — resume exatamente os princípios da ofensividade e da exclusiva proteção de bens "
     "jurídicos: só se pune a exteriorização que ao menos coloque em risco o bem jurídico."),
    ("Nenhum dos princípios que regem o direito penal veda a criminalização, pelo legislador, da "
     "tentativa de suicídio, embora, no momento, esta conduta não esteja tipificada.", False,
     "Princípio da Ofensividade/Exclusiva Proteção de Bens Jurídicos",
     "Errado — o princípio da ofensividade/alteridade veda a criminalização de autolesão (a conduta não "
     "lesiona bem jurídico de terceiro), o que impede tipificar a tentativa de suicídio como crime."),
    ("Pelo princípio da fragmentariedade, o direito penal só deve intervir em ofensas realmente graves "
     "aos bens jurídicos mais relevantes.", True, "Princípio da Intervenção Mínima/Fragmentariedade",
     "Correto — a fragmentariedade (voltada ao legislador) reserva a tipificação penal só às ofensas mais "
     "graves aos bens jurídicos mais importantes."),
    ("O princípio da insignificância ou bagatela própria é uma causa supralegal de exclusão da tipicidade "
     "material.", True, "Princípio da Insignificância/Bagatela",
     "Correto — a insignificância própria exclui a tipicidade material (não há previsão legal expressa "
     "desse efeito, daí ser 'supralegal' — construção doutrinária/jurisprudencial)."),
    ("Para o STF, de acordo com o princípio da culpabilidade, somente é possível imputar crime a pessoa "
     "jurídica se, simultaneamente, o ilícito penal for imputado à pessoa física que tenha sido o autor "
     "material da conduta.", False, "Princípio da Culpabilidade",
     "Errado — o STF admite a responsabilização penal da pessoa jurídica (em crimes ambientais) de forma "
     "autônoma, não exigindo imputação simultânea obrigatória de pessoa física específica."),
    ("O princípio da vedação à dupla persecução (ne bis in idem processual) poderá ser excepcionado "
     "quando o julgamento no exterior não se realizar de modo justo e legítimo.", True,
     "Princípio do Ne Bis In Idem",
     "Correto — é o entendimento do STF (2ª Turma, HC 171118/SP), permitindo persecução interna "
     "complementar se o julgamento estrangeiro não foi justo/legítimo."),
    ("A regra que veda a interpretação extensiva das normas penais incriminadoras decorre do princípio "
     "constitucional da legalidade.", True, "Princípio da Legalidade",
     "Correto — a taxatividade (desdobramento da legalidade) exige interpretação restrita das normas "
     "incriminadoras, vedando a extensão por interpretação."),
    ("A lesividade do bem jurídico protegido pela lei penal é critério de legalidade material ou "
     "substancial e depende da existência da lei para caracterizar o delito.", False,
     "Princípio da Ofensividade/Exclusiva Proteção de Bens Jurídicos",
     "Errado — a lesividade/ofensividade é critério MATERIAL que existe independentemente da mera "
     "existência formal da lei; o bem jurídico deve ser efetivamente lesado ou exposto a perigo concreto, "
     "não bastando a tipificação formal."),
    ("O princípio da legalidade exige, além da previsão legal do crime e da pena anteriores ao fato "
     "praticado, definição de conduta e cominação balizada de punição.", True, "Princípio da Legalidade",
     "Correto — combina a reserva legal/anterioridade com a taxatividade (definição clara da conduta) e a "
     "proporcionalidade na cominação da pena."),
    ("Pelo princípio da legalidade compreende-se que ninguém responderá por um fato que a lei penal "
     "preveja como crime e, pelo princípio da anterioridade compreende-se que alguém somente responderá "
     "por crime devidamente previsto em lei que tenha entrado em vigor um ano anteriormente à prática da "
     "conduta.", False, "Princípio da Anterioridade",
     "Errado — o princípio da legalidade é o oposto do descrito (só responde por fato que a lei PREVEJA "
     "como crime), e a anterioridade não exige prazo mínimo de 'um ano' — basta a lei ser anterior ao "
     "fato, por qualquer intervalo de tempo."),
    ("Os princípios da legalidade e da anterioridade pressupõem a existência de lei anterior à prática de "
     "uma determinada conduta para que esta possa ser considerada como crime.", True,
     "Princípio da Anterioridade",
     "Correto — ambos convergem na exigência de lei prévia ao fato."),
    ("Os princípios da legalidade e da anterioridade são sinônimos e significam a necessidade da "
     "existência de lei para que uma conduta seja considerada crime.", False, "Princípio da Anterioridade",
     "Errado — não são sinônimos: a legalidade exige lei que defina o crime; a anterioridade exige que "
     "essa lei seja ANTERIOR ao fato — são aspectos complementares, não idênticos."),
    ("Os princípios da legalidade e da anterioridade são incompatíveis um com o outro, já que pressupõem "
     "circunstâncias diversas.", False, "Princípio da Anterioridade",
     "Errado — são complementares (a anterioridade é um desdobramento da legalidade), não incompatíveis."),
    ("Pelo princípio da anterioridade compreende-se a previsão anterior de determinada conduta como "
     "criminosa independentemente de definição por lei em sentido estrito.", False,
     "Princípio da Anterioridade",
     "Errado — a anterioridade exige que a previsão seja feita justamente por LEI em sentido estrito, não "
     "'independentemente' dela."),
    ("O princípio da legalidade dos crimes e das penas, sob a perspectiva do nullum crimen sine lege "
     "scricta, repudia o emprego da interpretação extensiva in malam partem.", True,
     "Princípio da Legalidade",
     "Correto — a legalidade estrita ('lex stricta') veda a interpretação extensiva que prejudique o "
     "réu."),
    ("O princípio da reserva legal é mitigado no âmbito do direito da infância e da juventude, dada a "
     "inimputabilidade absoluta do menor de 18 anos de idade.", False, "Princípio da Reserva Legal",
     "Errado — a reserva legal não é mitigada para menores; pelo contrário, o Estatuto da Criança e do "
     "Adolescente também exige tipificação prévia e específica dos atos infracionais."),
    ("É materialmente atípica, pela aplicação do Princípio da Insignificância, a conduta de portar ou "
     "possuir ínfima quantidade de munição, aliada à ausência do artefato capaz de disparar o projétil, "
     "que denote a incapacidade de gerar perigo à incolumidade pública.", False,
     "Princípio da Insignificância/Bagatela",
     "Errado — a jurisprudência majoritária do STJ/STF considera os crimes do Estatuto do Desarmamento "
     "como de perigo abstrato, não admitindo, em regra, a aplicação do princípio da insignificância, "
     "mesmo para ínfima quantidade de munição."),
    ("O princípio da individualização da pena determina que nenhuma pena passará da pessoa do condenado, "
     "razão pela qual as sanções relativas à restrição de liberdade não alcançarão parentes do autor do "
     "delito.", False, "Princípio da Pessoalidade/Intranscendência da Pena",
     "Errado — essa é a descrição do princípio da PESSOALIDADE/INTRANSCENDÊNCIA da pena (art. 5º, XLV, "
     "CF), não do princípio da individualização da pena (que trata de adequar a pena ao perfil do "
     "infrator, em três fases: legislativa, judiciária e administrativa)."),
    ("Princípio da Individualização da Pena: Qualquer que seja a pena aplicada, ela estará restrita à "
     "liberdade, ao patrimônio e à pessoa do condenado. A exceção é o uso do patrimônio transferido em "
     "herança para quitar obrigação de decretação de perdimento de bens e de reparação de dano.", True,
     "Princípio da Pessoalidade/Intranscendência da Pena",
     "Correto — a obrigação de reparar o dano e a decretação de perdimento de bens podem ser estendidas "
     "aos sucessores, até o limite do patrimônio transferido (art. 5º, XLV, CF)."),
    ("É possível a aplicação do princípio da insignificância nos crimes contra a administração pública, "
     "desde que o prejuízo seja em valor inferior a um salário-mínimo.", False,
     "Princípio da Insignificância/Bagatela",
     "Errado — Súmula 599/STJ: 'O princípio da insignificância é inaplicável aos crimes contra a "
     "administração pública', independentemente do valor do prejuízo, pois protegem também a moral "
     "administrativa."),
    ("Conforme jurisprudência assente do STF, o princípio da insignificância descaracteriza a tipicidade "
     "penal em seu caráter material.", True, "Princípio da Insignificância/Bagatela",
     "Correto — a insignificância não afasta a tipicidade formal (a conduta se amolda à descrição legal), "
     "mas afasta a tipicidade MATERIAL (a relevância do dano/perigo ao bem jurídico)."),
    ("O princípio da fragmentariedade ou o caráter fragmentário do direito penal quer dizer que a pessoa "
     "cometerá o crime se sua conduta coincidir com qualquer verbo da descrição desse crime, ou seja, com "
     "qualquer fragmento de seu tipo penal.", False, "Princípio da Intervenção Mínima/Fragmentariedade",
     "Errado — fragmentariedade significa que o direito penal só protege FRAGMENTOS (uma pequena parte) "
     "dos bens jurídicos e condutas lesivas existentes — os mais graves — e não que qualquer coincidência "
     "parcial com um verbo do tipo já configura o crime."),
    ("O princípio da anterioridade, no direito penal, informa que ninguém será punido sem lei anterior "
     "que defina a conduta como crime e que a pena também deve ser prevista previamente, ou seja, a lei "
     "nunca poderá retroagir.", False, "Princípio da Anterioridade",
     "Errado — a lei penal PODE retroagir quando beneficia o réu (retroatividade da lei benéfica); a "
     "irretroatividade só é absoluta para a lei prejudicial ao réu."),
    ("É possível que uma lei penal mais benigna alcance condutas anteriores à sua vigência, seja para "
     "possibilitar a aplicação de pena menos severa, seja para contemplar situação em que a conduta "
     "tipificada passe a não mais ser crime.", True, "Princípio da Anterioridade",
     "Correto — é a retroatividade da lei penal benéfica (abolitio criminis ou lei mais branda), prevista "
     "no art. 5º, XL, da CF."),
    ("O princípio da insignificância no direito penal dispõe que nenhuma vida humana será considerada "
     "insignificante, sendo que todas deverão ser protegidas.", False, "Princípio da Insignificância/Bagatela",
     "Errado — essa descrição não corresponde ao princípio da insignificância, que trata da exclusão da "
     "tipicidade material em condutas de reduzidíssima lesividade a bens jurídicos em geral (patrimoniais, "
     "por exemplo), não sendo um enunciado sobre o valor da vida humana."),
    ("O princípio da ultima ratio ou da intervenção mínima do direito penal significa que a pessoa só "
     "cometerá um crime se a pessoa a ser prejudicada por esse crime o permitir.", False,
     "Princípio da Intervenção Mínima/Fragmentariedade",
     "Errado — a intervenção mínima/subsidiariedade significa que o direito penal só deve atuar quando os "
     "demais ramos do direito se mostrarem insuficientes para proteger o bem jurídico, e não depende de "
     "'permissão' da potencial vítima."),
    ("O princípio da legalidade é parâmetro fixador do conteúdo das normas penais incriminadoras, ou "
     "seja, os tipos penais de tal natureza somente podem ser criados por meio de lei em sentido "
     "estrito.", True, "Princípio da Legalidade",
     "Correto — somente lei ordinária ou complementar (lei em sentido estrito) pode criar tipo penal "
     "incriminador."),
    ("Em caso de urgência, a definição do que é crime pode ser realizada por meio de medida provisória.",
     False, "Princípio da Reserva Legal",
     "Errado — o art. 62, §1º, I, 'b', da CF veda expressamente medida provisória sobre direito penal, "
     "mesmo em caso de urgência."),
    ("Prevê a Constituição Federal que nenhuma pena passará da pessoa do condenado, podendo a obrigação "
     "de reparar o dano e a decretação de perdimento de bens ser, nos termos da lei, estendidas aos "
     "sucessores e contra eles executadas, até o limite do valor do patrimônio transferido. Referido "
     "dispositivo constitucional traduz o princípio da intranscendência.", True,
     "Princípio da Pessoalidade/Intranscendência da Pena",
     "Correto — é a transcrição literal do art. 5º, XLV, da CF, base do princípio da "
     "pessoalidade/intranscendência da pena."),
    ("João, aproveitando-se de distração de Marcos, juiz de direito, subtraiu para si uma sacola de "
     "roupas usadas a ele pertencentes, avaliadas em valor ínfimo, que Marcos pretendia doar a instituição "
     "de caridade. O fato de a vítima ser juiz de direito demonstra maior reprovabilidade da conduta de "
     "João, o que impede o reconhecimento do princípio da insignificância.", False,
     "Princípio da Insignificância/Bagatela",
     "Errado — a condição pessoal da vítima (ser juiz, ter renda alta) não impede, por si só, a "
     "insignificância; ao contrário, como as roupas já seriam doadas, o dano patrimonial é ainda mais "
     "irrelevante, reforçando a aplicação do princípio."),
    ("Do princípio da individualização da pena decorre a exigência de que a dosimetria obedeça ao perfil "
     "do sentenciado, não havendo correlação do referido princípio com a atividade legislativa "
     "incriminadora, isto é, com a feitura de normas penais incriminadoras.", False,
     "Princípio da Individualização da Pena",
     "Errado — a individualização da pena também se manifesta na fase LEGISLATIVA (cominação), quando o "
     "legislador gradua os limites mínimo e máximo da pena conforme a gravidade de cada infração — há, "
     "sim, correlação com a atividade legislativa."),
    ("Quando do envio do Código de Defesa do Consumidor à sanção presidencial, um de seus dispositivos "
     "foi vetado em sua integralidade, por descrever como crime 'colocar no mercado, fornecer ou expor "
     "para fornecimento produtos ou serviços impróprios'. Com base nos princípios que norteiam o direito "
     "penal, é correto afirmar que a razão invocada no veto foi a inobservância do princípio da "
     "legalidade.", True, "Princípio da Legalidade",
     "Correto — o conceito vago de 'produtos impróprios' viola a taxatividade, um dos desdobramentos do "
     "princípio da legalidade."),
    ("Ao se referir ao princípio da lesividade ou ofensividade, a doutrina majoritária aponta que somente "
     "haverá infração penal se houver efetiva lesão ao bem jurídico tutelado.", False,
     "Princípio da Ofensividade/Exclusiva Proteção de Bens Jurídicos",
     "Errado — basta a LESÃO OU O PERIGO CONCRETO de lesão ao bem jurídico, não sendo necessária lesão "
     "efetiva em todos os casos (ex.: crimes de perigo concreto)."),
    ("Dado o princípio da intranscendência da pena, o condenado não pode permanecer mais tempo preso do "
     "que aquele estipulado pela sentença transitada em julgado.", False,
     "Princípio da Pessoalidade/Intranscendência da Pena",
     "Errado — essa garantia decorre do devido processo legal/individualização da pena e do cumprimento "
     "regular da execução penal, não do princípio da intranscendência, que trata da impossibilidade de a "
     "pena ultrapassar a pessoa do condenado para atingir terceiros."),
    ("Em consequência da fragmentaridade do direito penal, ainda que haja outras formas de sanção ou "
     "outros meios de controle social para a tutela de determinado bem jurídico, a criminalização, pelo "
     "direito penal, de condutas que invistam contra esse bem será adequada e recomendável.", False,
     "Princípio da Intervenção Mínima/Fragmentariedade",
     "Errado — é exatamente o oposto: pela subsidiariedade, se outros ramos do direito já protegem "
     "eficazmente o bem jurídico, a criminalização penal NÃO é recomendável nem necessária."),
    ("É legítima a criação de tipos penais por meio de decreto.", False, "Princípio da Reserva Legal",
     "Errado — só lei em sentido estrito (ordinária ou complementar) pode criar tipo penal; decreto é ato "
     "infralegal do Poder Executivo."),
    ("Conforme o STF, para que incida o princípio da insignificância e, consequentemente, seja afastada a "
     "recriminação penal, é indispensável que a conduta do agente seja marcada por ofensividade mínima ao "
     "bem jurídico tutelado, reduzido grau de reprovabilidade, inexpressividade da lesão, e nenhuma "
     "periculosidade social.", True, "Princípio da Insignificância/Bagatela",
     "Correto — são os quatro vetores fixados pelo STF (mnemônico MARI: Mínima ofensividade, Ausência de "
     "periculosidade social, Reduzido grau de reprovabilidade, Inexpressividade da lesão jurídica)."),
    ("Um dos princípios basilares do direito penal diz respeito à não transcendência da pena, que "
     "significa que a pena deve estar expressamente prevista no tipo penal, não havendo possibilidade de "
     "aplicar pena cominada a outro crime.", False, "Princípio da Pessoalidade/Intranscendência da Pena",
     "Errado — a não transcendência/intranscendência trata da impossibilidade de a pena ultrapassar a "
     "pessoa do condenado, e não da vedação de aplicar pena de outro tipo penal (isso seria uma violação "
     "à legalidade/taxatividade, não à intranscendência)."),
    ("O princípio da reserva legal aplica-se, de forma absoluta, às normas penais incriminadoras, "
     "excluindo-se de sua incidência as normas penais não incriminadoras. (questão CESPE, Câmara dos "
     "Deputados, 2014)", True, "Princípio da Reserva Legal",
     "Correto — a reserva legal estrita só se aplica às normas que definem crimes/penas (incriminadoras); "
     "normas penais não incriminadoras (ex.: causas de justificação) podem decorrer de outras fontes."),
    ("A venda de cópias não autorizadas de CDs e DVDs — cópias piratas — por vendedores ambulantes que "
     "não possuam outra renda além da advinda dessa atividade, apesar de ser conduta tipificada, não "
     "possui, segundo a jurisprudência do STJ, tipicidade material, aplicando-se ao caso o princípio da "
     "adequação social.", False, "Princípio da Adequação Social",
     "Errado — Súmula 502/STJ: a conduta de expor à venda CDs e DVDs piratas é TÍPICA; mera tolerância "
     "social (leniência) não equivale à adequação social, que exige a conduta deixar de ser reprovada "
     "pela sociedade, o que não é o caso."),
    ("A pena não passará da pessoa do condenado, mas a obrigação de reparar o dano e a decretação do "
     "perdimento de bens poderá ser, nos termos da lei, estendidas aos sucessores e contra eles "
     "executadas ilimitadamente.", False, "Princípio da Pessoalidade/Intranscendência da Pena",
     "Errado — a extensão aos sucessores é LIMITADA ao valor do patrimônio transferido, não é "
     "ilimitada (art. 5º, XLV, CF)."),
]

# -------------------- insere o deck de teoria --------------------
array_literal = '[\n' + ',\n'.join(json.dumps(it, ensure_ascii=False) for it in TEORIA_ITEMS) + '\n]'

m = re.search(r'const TEORIA_COMBATE_INCENDIO\s*=\s*\[[\s\S]*?\n\];', html)
assert m, "bloco TEORIA_COMBATE_INCENDIO nao encontrado"
insertion_point = m.end()
new_block = '\n\nconst TEORIA_DIREITO_PENAL_PCPE = ' + array_literal + ';'
html = html[:insertion_point] + new_block + html[insertion_point:]

old_teoria_tail = '  hist: { label: "História do Maranhão", data: HIST_MA_LESSON, corp: null }\n};'
assert old_teoria_tail in html, "final de TEORIA_DECKS nao encontrado como esperado"
new_teoria_tail = ('  hist: { label: "História do Maranhão", data: HIST_MA_LESSON, corp: null },\n'
                   '  direito_penal_pcpe: { label: "Direito Penal — Princípios (PC-PE)", '
                   'data: TEORIA_DIREITO_PENAL_PCPE, corp: "PCPE" }\n};')
html = html.replace(old_teoria_tail, new_teoria_tail, 1)

with open('app-template.html', 'w', encoding='utf-8', newline='') as f:
    f.write(html)
print('TEORIA_DIREITO_PENAL_PCPE adicionada com', len(TEORIA_ITEMS), 'itens; registrada em TEORIA_DECKS.')

# -------------------- insere as questoes --------------------
with open('questions.json', encoding='utf-8') as f:
    qdata = json.load(f)

next_id = max(q['id'] for q in qdata) + 1
added = 0
for enun, resp, assunto, exp in CE_QUESTIONS:
    qdata.append({
        "id": next_id,
        "corp": "PCPE",
        "disc": "Direito Penal",
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
print('OK --', added, 'questoes de Direito Penal (PC-PE) adicionadas. Total no banco:', len(check))

# -------------------- regenera o HTML final --------------------
with open('questions.json', encoding='utf-8') as f:
    qdata_raw = f.read()
with open('app-template.html', encoding='utf-8') as f:
    html2 = f.read()
html2 = html2.replace('__QUESTIONS_JSON__', qdata_raw)
with open('estudo-cebraspe-ma.html', 'w', encoding='utf-8') as f:
    f.write(html2)
print('estudo-cebraspe-ma.html regenerado com sucesso')
