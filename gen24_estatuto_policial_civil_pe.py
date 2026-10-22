# -*- coding: utf-8 -*-
# Adiciona um novo deck na aba Estrategia com o resumo, ja filtrado
# para a redacao VIGENTE (descartando paragrafos/incisos revogados ou
# substituidos por leis posteriores -- principalmente a Lei n 6.657/1974,
# que trocou "Escola de Policia" por "Academia de Policia Civil" e
# renumerou varios dispositivos, e a Lei n 10.466/1990, que reescreveu
# as regras de concurso), da Lei n 6.425/1972 -- Estatuto do Policial
# Civil da Secretaria de Seguranca Publica de Pernambuco. Essa e a lei
# organica da propria carreira que o usuario esta estudando para
# ingressar (Agente de Policia da PC-PE), entao o deck cobre a lei
# inteira (provimento, vencimento e vantagens, deveres, transgressoes
# disciplinares, penas, processo disciplinar, merito policial e
# Conselho Superior de Policia), nao so um recorte.
import re
import json

with open('app-template.html', encoding='utf-8') as f:
    html = f.read()

ITEMS = [
    {"t": "tit", "x": "LEI Nº 6.425/1972 — ESTATUTO DO POLICIAL CIVIL DE PERNAMBUCO (trechos vigentes)"},
    {"t": "art", "n": "Sobre este resumo",
     "x": "Resumo da Lei nº 6.425, de 29/9/1972 (Estatuto dos Funcionários Policiais Civis da Secretaria "
          "da Segurança Pública de Pernambuco), já filtrado para trazer só a redação vigente — a lei foi "
          "bastante alterada pela Lei nº 6.657/1974 (que trocou 'Escola de Polícia' por 'Academia de "
          "Polícia Civil' e renumerou quase todos os incisos) e pela Lei nº 10.466/1990 (que reescreveu as "
          "regras de concurso público). Esta é a lei orgânica da própria carreira de Agente de Polícia da "
          "PC-PE — cai bastante em prova, principalmente a parte de deveres, transgressões disciplinares e "
          "penas."},

    {"t": "cap", "x": "TÍTULO I — DISPOSIÇÕES PRELIMINARES (Art. 1º a 4º)"},
    {"t": "art", "n": "Art. 1º a 3º",
     "x": "A lei institui o regime jurídico dos policiais civis ocupantes de cargos de atividade policial "
          "do Quadro de Pessoal Policial da Secretaria da Segurança Pública (SSP). Só nos casos "
          "expressamente previstos nesta lei o tratamento é diferente dos demais servidores — nos demais "
          "casos, o policial civil segue o regime jurídico geral dos servidores civis do Estado (hoje "
          "substituído pela Constituição e pelo estatuto geral vigente, à época a Lei nº 6.123/1968). São "
          "abrangidos os brasileiros investidos em cargos privativos do Quadro de Pessoal Policial, e "
          "também os ocupantes de cargo em comissão ou função gratificada com atribuição e responsabilidade "
          "de natureza policial."},
    {"t": "art", "n": "Art. 4º",
     "x": "A função policial se fundamenta na hierarquia e na disciplina, e é incompatível com qualquer "
          "outra atividade pública ou privada, ressalvadas: exigência da Segurança Nacional; e, havendo "
          "compatibilidade de horários, as hipóteses de acumulação remunerada de cargos públicos previstas "
          "no art. 37, XVI, da Constituição Federal, além de atividades de magistério e empregos privativos "
          "de profissionais de saúde — em qualquer caso, limitado a 2 (dois) vínculos (redação da Lei "
          "Complementar nº 490/2022). § 1º Para efeito de acumulação, é técnico o cargo de natureza "
          "policial que exige diploma de curso universitário ou equivalente. § 2º É vedada a acumulação de "
          "dois cargos de natureza policial entre si. § 3º A exigência da Segurança Nacional depende de "
          "autorização expressa do Secretário da Segurança Pública.",
     "s": "O limite de 2 vínculos é recente (LC 490/2022) — antes disso a lei não fixava esse teto "
          "numérico. E repare: é vedado acumular DOIS CARGOS POLICIAIS entre si, mesmo com a acumulação "
          "geral liberada em outros casos."},

    {"t": "cap", "x": "TÍTULO II, CAPÍTULO I — DO PROVIMENTO (Art. 5º)"},
    {"t": "art", "n": "Art. 5º",
     "x": "Os cargos de natureza policial serão preenchidos por: I - Nomeação; II - Acesso; III - "
          "Promoção; IV - Reintegração; V - Aproveitamento; VI - Reversão; VII - Transferência (redação da "
          "Lei nº 6.657/1974, que acrescentou 'Acesso' como forma própria, distinta de 'Promoção', e "
          "acrescentou 'Transferência' como sétima forma — na redação original de 1972 eram só 6 formas e "
          "não existia 'Acesso' separado)."},

    {"t": "cap", "x": "TÍTULO II, CAPÍTULO II — DA NOMEAÇÃO (Art. 6º a 11)"},
    {"t": "art", "n": "Art. 6º e 7º",
     "x": "A nomeação far-se-á exclusivamente: I - em caráter efetivo, para cargo de classe inicial de "
          "série de classes; II - em comissão, para cargo isolado que a lei assim exigir. Os cargos vagos "
          "em classe inicial de série de classes — tanto do Quadro de Autoridades Policiais Civis quanto do "
          "Quadro de Pessoal Policial da SSP — são providos por nomeação e por acesso, na proporção de 50% "
          "das vagas para cada forma (redação da Lei nº 10.466/1990).",
     "s": "Metade das vagas é para quem entra de fora (concurso externo/nomeação) e metade para quem já é "
          "do quadro e sobe por concurso interno (acesso) — proporção 50/50."},
    {"t": "art", "n": "Art. 7º, § 1º a § 3º",
     "x": "§ 1º O provimento por nomeação e por acesso depende de aprovação em processo de seleção: "
          "concurso público de provas (ou de provas e títulos, quando exigida escolaridade de nível "
          "superior) e frequência/aproveitamento em curso de formação profissional específico. § 2º O "
          "processo de seleção começa no edital do concurso e termina com a nomeação do candidato. § 3º O "
          "concurso é exclusivamente para admissão ao curso de formação a que se refere (redação acrescida "
          "pela Lei nº 10.466/1990)."},
    {"t": "art", "n": "Art. 8º, requisitos I a X",
     "x": "A Academia de Polícia Civil disciplina em edital o processo de realização, inscrição, prazo de "
          "validade, critérios de classificação, recursos, e os seguintes requisitos que os candidatos "
          "devem atender (redação da Lei nº 10.466/1990): I - ser brasileiro; II - ter entre 21 e 35 anos "
          "na data do pedido de inscrição, salvo se já for funcionário público estadual; III - não ter sido "
          "condenado criminalmente, nem estar respondendo a processo penal ou inquérito policial; IV - não "
          "ter sofrido demissão ou punição por falta grave nos últimos 12 meses, nem estar respondendo a "
          "processo disciplinar, se já foi/é servidor público; V - estar no gozo dos direitos políticos; VI "
          "- estar em dia com o serviço militar e as obrigações eleitorais; VII - ter aptidão física "
          "(testes específicos, tabela de avaliação e altura mínima do edital); VIII - ser aprovado em "
          "exame psicotécnico específico do concurso; IX - possuir a qualificação técnico-profissional ou "
          "escolaridade exigida para o cargo; X - ter boa conduta moral e social."},
    {"t": "art", "n": "Art. 8º, § 1º a § 4º",
     "x": "§ 1º O exame psicotécnico é feito por entidade credenciada, estranha ao serviço público, com no "
          "mínimo 5 anos de experiência em recrutamento de pessoal; as provas de conhecimento são "
          "elaboradas/corrigidas por comissão designada pelo Secretário da Segurança Pública e aplicadas "
          "pela Academia de Polícia Civil. § 2º A conduta moral e social é investigada — o Conselho "
          "Superior de Polícia pode, em sessão secreta, impugnar pedido ou cancelar inscrição, ou excluir o "
          "candidato em qualquer fase até a nomeação, declarando as razões quando solicitado pelo "
          "interessado. § 3º Os aprovados na prova de conhecimentos são admitidos no curso de formação por "
          "ordem de classificação, em número igual ao de vagas do curso. § 4º Até ser nomeado — mesmo tendo "
          "a inscrição deferida ou o curso concluído — é excluído do processo quem infringir normas da "
          "Academia, tiver omitido fato impeditivo da inscrição, ou vier a contrariar os incisos III, IV ou "
          "X (condenação/processo penal, falta grave, má conduta)."},
    {"t": "art", "n": "Art. 9º",
     "x": "Os candidatos aprovados são nomeados por ordem de classificação, considerada em ordem "
          "decrescente pela média aritmética da soma da nota/pontos do concurso público com a média global "
          "obtida no curso de formação (redação da Lei nº 10.466/1990).",
     "s": "A redação original de 1989/1990 deste artigo tinha uma lista enorme de requisitos de inscrição "
          "(I a XI) e vários parágrafos — tudo isso foi suprimido/revogado pela Lei nº 10.466/1990 e "
          "substituído só por esta regra de classificação final. Não confundir com os requisitos do art. 8º, "
          "que são os que valem hoje."},
    {"t": "art", "n": "Art. 10",
     "x": "Só toma posse quem: I - for brasileiro; II - tiver completado 18 anos; III - estiver em gozo dos "
          "direitos políticos; IV - estiver quite com as obrigações militares; V - estiver quite com as "
          "obrigações eleitorais; VI - gozar de boa saúde física e psíquica, comprovada em inspeção médica. "
          "Para cargo de provimento efetivo, exige-se ainda (redação da Lei nº 6.657/1974): ter "
          "temperamento adequado à função policial, apurado em exame psicotécnico pela Academia de Polícia "
          "Civil; e ter sido habilitado em concurso de provas e aprovado no curso de formação, ambos pela "
          "Academia de Polícia Civil."},
    {"t": "art", "n": "Art. 11",
     "x": "Dão posse (redação da Lei nº 6.657/1974): o Secretário da Segurança Pública, ao seu Chefe de "
          "Gabinete, aos Diretores de Departamentos e órgãos equivalentes, Diretores Executivos, Titulares "
          "de Delegacias, Delegados em geral, Médicos Legistas e Peritos Criminais; e o Diretor do "
          "Departamento de Pessoal, nos demais casos."},

    {"t": "cap", "x": "TÍTULO II, CAPÍTULO III — DA REMOÇÃO (Art. 12 a 15)"},
    {"t": "art", "n": "Art. 12 a 15",
     "x": "A remoção se dá de um para outro órgão da SSP, ou de uma para outra localidade com serviço da "
          "mesma — sendo vedada a remoção do policial civil para outro órgão da administração fora da SSP. "
          "Formas: de ofício (interesse da Administração), a pedido do funcionário (atendida a conveniência "
          "do serviço), ou por conveniência da disciplina. A remoção por conveniência da disciplina precisa "
          "ser expressamente justificada pelo chefe do serviço e acarreta a perda dos direitos/vantagens "
          "das outras formas de remoção. Em qualquer caso a remoção depende de vaga (claro de lotação), "
          "exceto a remoção por disciplina."},

    {"t": "cap", "x": "TÍTULO II, CAPÍTULO IV — DO VENCIMENTO E DAS VANTAGENS (Art. 16 a 29)"},
    {"t": "art", "n": "Art. 16 e 17",
     "x": "Vencimento é a retribuição pelo efetivo exercício do cargo, no nível fixado em lei. Além do "
          "vencimento, o policial civil pode ter: ajuda de custo, diárias, salário-família, "
          "auxílio-acidente, auxílio-moradia, transporte e gratificações."},
    {"t": "art", "n": "Art. 18 a 21",
     "x": "Ajuda de custo: concedida quando o policial passa a ter exercício em nova sede, ou é designado "
          "para missão/estudo fora da sede (inclusive no exterior); ressarce despesas de viagem e nova "
          "instalação (exceto transporte), até o limite de 1 mês de vencimento, pago adiantadamente. "
          "Diárias: devidas quando o policial se desloca a serviço, missão oficial ou estudo, indenizando "
          "alimentação e pousada, arbitradas com base no maior salário mínimo do local de destino. "
          "Salário-família: nos termos da regulamentação em vigor. Auxílio-acidente: concedido ao ferido ou "
          "acidentado em serviço, cobrindo despesas médico-hospitalares, condicionado a atestado do chefe "
          "do órgão e homologação do Secretário."},
    {"t": "art", "n": "Art. 22",
     "x": "O auxílio-moradia é concedido ao Policial Civil pelo efetivo exercício de suas funções (redação "
          "da Lei nº 10.278/1989). É calculado sobre o vencimento-base do cargo somado à gratificação por "
          "tempo de serviço, à base de 20% para quem é lotado no interior do Estado, e 15% para quem é "
          "lotado na Área Metropolitana (inclusive a Capital)."},
    {"t": "art", "n": "Art. 23 e 24",
     "x": "Transporte: quando removido de ofício, o policial tem direito a transporte domicílio a "
          "domicílio por conta da Administração (passagem + bagagem), estendido a dependentes e 1 serviçal. "
          "Gratificações possíveis: de função; de função policial; por serviço extraordinário; de "
          "representação de Gabinete; por exercício em zonas/locais determinados; por participação em "
          "órgão de deliberação coletiva da SSP; por cursos de formação/treinamento/especialização/"
          "aperfeiçoamento em estabelecimento de ensino policial; por exercício de encargo de auxiliar, "
          "professor ou instrutor em curso da Academia de Polícia Civil; por participação em banca/comissão "
          "de concurso de natureza policial; por trabalho relevante técnico ou científico de natureza "
          "policial; adicional por tempo de serviço; e outros encargos previstos em lei ou regulamento."},
    {"t": "art", "n": "Art. 25 e 26",
     "x": "A gratificação de função policial compensa a incompatibilização compulsória do policial com "
          "qualquer outra atividade, e os riscos da função. § 1º Ela sujeita o policial ao regime de "
          "dedicação integral, com no mínimo 200 horas mensais de trabalho. § 2º Esse regime é específico "
          "do policial civil e o exclui dos regimes gerais de jornada do estatuto comum. § 3º Não pode "
          "acumular com outra gratificação de risco de vida. A gratificação é calculada sobre o vencimento "
          "do cargo efetivo, entre 100% (mínimo) e 150% (máximo) desse valor — para chefia/assessoramento "
          "policial, calcula-se sobre o vencimento do símbolo do cargo em comissão/função gratificada, com "
          "a mesma percentagem.",
     "s": "As 200 horas mensais de dedicação integral são um número clássico de prova — não confundir com a "
          "jornada comum de 8h/dia e 44h/semana dos demais servidores (art. 98, VII, da Constituição de "
          "PE)."},
    {"t": "art", "n": "Art. 27 a 29",
     "x": "O policial efetivo que, nos 2 anos imediatamente anteriores à aposentadoria, estava recebendo em "
          "regime de dedicação integral a gratificação de função policial, tem direito a incorporá-la aos "
          "proventos da aposentadoria (redação da Lei nº 6.657/1974). Os limites dessa gratificação só "
          "podem mudar por legislação específica. Há ainda gratificações por cursos de formação/"
          "treinamento/especialização/aperfeiçoamento na Academia de Polícia Civil ou em outros "
          "estabelecimentos de ensino policial/de informações: valoradas de 5% a 20% sobre o vencimento "
          "conforme importância e duração do curso, limitadas à soma de 30%, e só se aplicam a cursos com "
          "carga horária igual ou superior a 350 horas-aula."},

    {"t": "cap", "x": "TÍTULO III, CAPÍTULO I — DOS DEVERES (Art. 30)"},
    {"t": "art", "n": "Art. 30",
     "x": "Além dos deveres comuns aos demais servidores civis, o policial deve: dedicação e fidelidade à "
          "Pátria, cuja honra, segurança e integridade deve defender mesmo com sacrifício da própria vida; "
          "disciplina e respeito à hierarquia; frequentar com assiduidade os cursos instituídos "
          "periodicamente pela Academia de Polícia Civil ou estabelecimentos congêneres em que tenha sido "
          "compulsoriamente matriculado; zelar pela dignidade da função policial; e ter conduta pública "
          "irrepreensível."},

    {"t": "cap", "x": "TÍTULO III, CAPÍTULO II — DAS TRANSGRESSÕES DISCIPLINARES (Art. 31, I a XLVIII)"},
    {"t": "art", "n": "Art. 31, I a XVI",
     "x": "São transgressões disciplinares: I - exercer cumulativamente 2+ cargos/funções públicas sem "
          "exceção legal; II - divulgar fatos da repartição por qualquer veículo, ou facilitar seu "
          "conhecimento a não autorizados; III - referir-se desrespeitosa/depreciativamente a autoridades e "
          "atos da Administração; IV - promover/participar de manifestações de apreço ou desapreço a "
          "autoridades; V - manifestar-se/participar de manifestações contra atos da Administração; VI - "
          "indispor funcionários contra superiores ou provocar animosidade entre colegas; VII - valer-se do "
          "cargo para proveito pessoal em detrimento da dignidade da função policial; VIII - praticar ato "
          "que importe escândalo ou comprometa a dignidade da função; IX - retirar sem autorização "
          "documento/objeto da repartição; X - cometer a pessoa estranha à repartição encargo que competia "
          "ao servidor ou a subordinado; XI - pleitear como procurador/intermediário junto a repartições "
          "públicas (salvo vencimentos de parentes até 2º grau); XII - participar de gerência/administração "
          "de empresas; XIII - exercer comércio ou participar de sociedade comercial (salvo como acionista/"
          "cotista/comanditário); XIV - deixar de pagar pensão devida por decisão judicial; XV - deixar "
          "habitualmente de saldar dívidas legítimas; XVI - utilizar-se do anonimato para qualquer fim."},
    {"t": "art", "n": "Art. 31, XVII a XXXII",
     "x": "XVII - praticar usura; XVIII - manter amizade ou exibir-se em público com pessoas de notórios "
          "antecedentes criminais, sem razão de serviço; XIX - faltar à verdade no exercício das funções, "
          "por malícia/má-fé; XX - deixar de comunicar imediatamente faltas/irregularidades presenciadas; "
          "XXI - deixar de comunicar fato que ameace instituições civis/militares ou a Segurança Nacional; "
          "XXII - apresentar maliciosamente parte/queixa/representação; XXIII - provocar ou participar de "
          "paralisação do serviço policial; XXIV - negligenciar/descumprir ordem legítima; XXV - trabalhar "
          "incorretamente de modo intencional para prejudicar o serviço, ou negligenciar deveres; XXVI - "
          "simular doença para esquivar-se de obrigações; XXVII - faltar/atrasar ao serviço sem avisar com "
          "antecedência, sem motivo justo; XXVIII - não se apresentar sem motivo justo ao fim de férias/"
          "licença/dispensa; XXIX - abandonar o serviço designado, ou permutá-lo sem permissão; XXX - "
          "atribuir-se representação de sua repartição ou de outra sem autorização; XXXI - frequentar sem "
          "razão de serviço lugares incompatíveis com o decoro da função policial; XXXII - dar conhecimento "
          "ao público de informações sobre investigações/serviços de interesse policial, sem autorização "
          "expressa da autoridade competente."},
    {"t": "art", "n": "Art. 31, XXXIII a XLVIII",
     "x": "XXXIII - negligenciar a guarda de objetos da repartição, possibilitando dano/extravio, ou "
          "danificá-los intencionalmente; XXXIV - valer-se do cargo para participar de atividade "
          "político-partidária ou obter proveito próprio/alheio; XXXV - coagir/aliciar subordinados com "
          "objetivo político-partidário; XXXVI - entregar-se a jogos/vícios/atos atentatórios à moral ou "
          "aos bons costumes, puníveis em lei; XXXVII - comparecer embriagado ao serviço ou embriagar-se "
          "nele; XXXVIII - dirigir-se a superior hierárquico de modo ofensivo/desrespeitoso; XXXIX - tratar "
          "colegas e público sem urbanidade; XL - maltratar preso sob guarda ou usar violência "
          "desnecessária no exercício da função; XLI - omitir-se/negligenciar a guarda de presos; XLII - "
          "permitir que presos conservem instrumentos/objetos que possam danificar instalações ou produzir "
          "lesões; XLIII - facilitar o uso, por presos, de substâncias proibidas, ou participar do tráfico; "
          "XLIV - desrespeitar/procrastinar o cumprimento de decisão/ordem judicial, ou criticá-las; XLV - "
          "deixar sem justa causa de se submeter à inspeção médica determinada; XLVI - prevalecer-se "
          "abusivamente da condição de policial; XLVII - atentar, com abuso de autoridade evidente, contra "
          "a liberdade de pessoa ou a inviolabilidade de domicílio; XLVIII - cometer infração penal "
          "infamante que incompatibilize o servidor para o exercício da função policial.",
     "s": "A lista do art. 31 é a base de referência para duas outras listas importantes: o art. 37 diz "
          "quais desses itens são considerados GRAVES (geram suspensão), e o art. 49, XII, diz quais geram "
          "DEMISSÃO diretamente — vale a pena cruzar os três artigos ao estudar."},
    {"t": "art", "n": "Art. 32 e 33",
     "x": "O policial responde civil, penal e administrativamente pelo exercício regular de suas "
          "atribuições. As comunicações nessas três esferas podem se cumular, sendo as instâncias civil, "
          "penal e administrativa independentes entre si."},

    {"t": "cap", "x": "TÍTULO III, CAPÍTULO IV — DAS PENAS DISCIPLINARES (Art. 34 a 52)"},
    {"t": "art", "n": "Art. 34 a 36",
     "x": "São penas disciplinares: repreensão, multa, suspensão, detenção disciplinar, destituição de "
          "função, demissão, e cassação de aposentadoria ou disponibilidade. Na aplicação, considera-se a "
          "natureza/gravidade/circunstâncias da transgressão, os danos ao serviço público, a repercussão do "
          "fato, os antecedentes do funcionário e a reincidência — é agravante a falta cometida em concurso "
          "com 2 ou mais funcionários. A repreensão é sempre aplicada por escrito, consta do assentamento "
          "individual, e se destina a faltas consideradas leves (sem sanção específica prevista)."},
    {"t": "art", "n": "Art. 37",
     "x": "A suspensão não excede 30 dias, aplicada em caso de falta grave ou reincidência em falta de "
          "qualquer natureza. São consideradas de natureza grave (redação da Lei nº 6.657/1974) as "
          "transgressões dos itens II, III, IV, V, IX, X, XI, XV, XVI, XVII, XVIII, XIX, XXII, XXIV, XXV, "
          "XXVI, XXVII, XXVIII, XXIX, XXX, XXXII, XXXIII, XXXVII, XXXVIII, XXXIX, XLI, XLII, XLIV, XLV, "
          "XLVI e XLVII do art. 31."},
    {"t": "art", "n": "Art. 38 a 47",
     "x": "A suspensão pode ser convertida em detenção disciplinar por ordem escrita do Secretário da SSP "
          "ou do Governador, respeitando o mesmo limite de 30 dias; não acarreta perda de vencimentos, e é "
          "cumprida na residência (se até 48h) ou em sala especial na sede da SSP. A ordem informa motivo, "
          "prazo e local; o funcionário assina ciente com data/hora/local do recebimento; o prazo corre a "
          "partir do recolhimento. Durante a detenção, o funcionário não pode se ausentar nem ser incumbido "
          "de atividade. O Secretário pode interromper ou suspender a detenção por necessidade de serviço, "
          "emergência, segurança nacional ou saúde (se suspensa, é considerada cumprida integralmente; se "
          "interrompida, retoma depois até o final). Recusar cumprir a detenção, descumprir suas normas, ou "
          "cometer nova falta durante o recolhimento configura insubordinação grave em serviço, sujeita a "
          "demissão. O tempo de detenção não é computado nos assentamentos funcionais. O funcionário pode "
          "receber visitas de familiares em horário determinado pelo Secretário. A suspensão pode, por "
          "conveniência do serviço, ser convertida em multa de 50% do vencimento/remuneração por dia, "
          "permanecendo o funcionário no serviço."},
    {"t": "art", "n": "Art. 48 a 50",
     "x": "A destituição de função tem por fundamento a falta de exação (zelo/cuidado) no cumprimento do "
          "dever. A demissão é aplicada nos casos de: I - crime contra a Segurança Nacional; II - crime "
          "contra a Administração Pública; III - abandono do cargo; IV - insubordinação grave em serviço; "
          "V - ofensa física a pessoa em serviço, salvo legítima defesa ou estrito cumprimento do dever "
          "legal; VI - aplicação irregular de dinheiros públicos; VII - revelação de segredo conhecido em "
          "razão do cargo/função; VIII - lesão aos cofres públicos/dilapidação do patrimônio estadual; IX - "
          "falta ao serviço por 60 dias interpolados sem causa justificada em 12 meses; X - reincidência em "
          "falta que gerou suspensão de 30 dias ou detenção disciplinar; XI - contumácia na prática de "
          "transgressões disciplinares; XII - prática das transgressões dos itens I, VI, VII, VIII, XII, "
          "XIII, XXI, XXIII, XXXI, XXXIV, XXXV, XXXVI, XL, XLIII e XLVIII do art. 31 (redação da Lei nº "
          "6.657/1974). O ato de demissão sempre menciona a causa."},
    {"t": "art", "n": "Art. 51 e 52",
     "x": "A cassação de aposentadoria/disponibilidade segue a legislação em vigor sobre o tema. São "
          "competentes para aplicar as penalidades (redação da Lei nº 6.657/1974): o Governador, em "
          "qualquer caso, e privativamente nos casos de demissão e cassação de aposentadoria/"
          "disponibilidade; o Secretário da Segurança Pública, em todos os demais casos; o Chefe de "
          "Gabinete da SSP, repreensão e suspensão até 20 dias; os Diretores de Departamentos e órgãos "
          "equivalentes, Diretores Executivos e o Corregedor, repreensão e suspensão até 15 dias; os "
          "Titulares de Delegacias, Delegados de Polícia, Médicos Legistas e Peritos Criminais, repreensão "
          "e suspensão até 10 dias."},

    {"t": "cap", "x": "TÍTULO III, CAPÍTULO V — DAS PENAS PREVENTIVAS (Art. 53 a 55)"},
    {"t": "art", "n": "Art. 53 a 55",
     "x": "Quando a presença do policial puder influir na apuração de falta, pode ser imposta suspensão "
          "preventiva de até 30 dias pelas autoridades competentes para punir (art. 52, I a IV). A "
          "suspensão preventiva pode ser convertida em detenção disciplinar preventiva nas hipóteses do "
          "art. 38, só por ordem escrita do Secretário ou do Governador. A detenção preventiva não excede o "
          "limite da suspensão preventiva, mas ambas podem ser prorrogadas até 90 dias no total, após o que "
          "cessam seus efeitos mesmo que o processo ainda não esteja concluído."},

    {"t": "cap", "x": "TÍTULO IV — DO PROCESSO DISCIPLINAR E SUA REVISÃO (Art. 56 a 71)"},
    {"t": "art", "n": "Art. 56 a 60",
     "x": "A apuração de irregularidades se dá por processo disciplinar, que compreende sindicância e "
          "inquérito disciplinar. São competentes para instaurar: o Governador, o Secretário da SSP, o "
          "Chefe de seu Gabinete e as autoridades do art. 52, IV. O processo disciplinar precede a "
          "aplicação de: suspensão por mais de 15 dias, destituição de função, demissão e cassação de "
          "disponibilidade — e também apura responsabilidade por dano à Fazenda Estadual por dolo ou culpa. "
          "A sindicância é instaurada quando as irregularidades não são evidentes ou a autoria é incerta, "
          "sendo procedida por 2 policiais civis designados pela autoridade instauradora."},
    {"t": "art", "n": "Art. 61 a 70",
     "x": "O inquérito é promovido por uma Comissão Permanente de Disciplina, de 3 membros (de preferência "
          "bacharéis em Direito), designada pelo Secretário da SSP, podendo haver até 2 Comissões "
          "Permanentes (Primeira e Segunda). Quando o indiciado for hierarquicamente superior aos membros "
          "da Comissão Permanente, o Secretário constitui uma Comissão Especial de Inquérito com membros de "
          "hierarquia igual ou superior. O mandato dos membros é de 12 meses, prorrogável até a conclusão "
          "dos processos já em fase de indiciação. O presidente é indicado pelo Secretário entre os "
          "membros, com nível equivalente a Diretor de Departamento; os demais membros, nível de Chefe de "
          "Divisão. Membros podem ser redesignados para o mandato seguinte, salvo quem perder o mandato por "
          "conduta desidiosa, punição ou indiciamento, ou por perda dos prazos processuais (que também "
          "impede recondução no mandato imediatamente seguinte)."},
    {"t": "art", "n": "Art. 71",
     "x": "A simples alegação de injustiça da penalidade, ou a arguição de nulidade não suscitada no "
          "processo (ou suscitada e não acolhida), não é fundamento para revisão do processo disciplinar."},

    {"t": "cap", "x": "TÍTULO V — DO MÉRITO POLICIAL (Art. 72)"},
    {"t": "art", "n": "Art. 72",
     "x": "Fica instituída a Medalha do Mérito Policial, nas classes ouro, prata e bronze (redação da Lei "
          "nº 6.657/1974, que trocou a antiga 'Ordem do Mérito Policial' por essa medalha única), para "
          "agraciar policiais civis que se distinguiram no serviço, bem como outras personalidades que "
          "prestaram serviços relevantes à causa policial. O processamento da concessão é regulamentado por "
          "Decreto do Poder Executivo."},

    {"t": "cap", "x": "DO CONSELHO SUPERIOR DE POLÍCIA (Art. 73 a 80)"},
    {"t": "art", "n": "Art. 73 e 74",
     "x": "O Conselho Superior de Polícia (criado pelo Decreto nº 1.395/1967) é integrado, na redação "
          "vigente (Lei nº 6.657/1974), por: o Secretário da Segurança Pública; o Chefe do Gabinete; o "
          "Diretor do Departamento de Polícia Judiciária; o Diretor de Departamento de Ordem Política e "
          "Social; o Diretor do Departamento de Operações; o Diretor do Centro de Informações; o Diretor do "
          "Departamento de Polícia Científica; o Diretor da Academia de Polícia Civil; e o Diretor do "
          "Departamento de Administração. O Secretário da SSP e seu Chefe de Gabinete são, respectivamente, "
          "Presidente e Vice-Presidente natos."},
    {"t": "art", "n": "Art. 75 a 80",
     "x": "O Conselho é órgão consultivo, normativo e opinativo para assuntos de polícia em geral "
          "(administração, polícia judiciária, emprego operacional). Examina, julga e aprova a concessão "
          "aos policiais civis e a outras personalidades da Medalha do Mérito Policial, e as classes "
          "concedidas. Reúne-se por convocação do Presidente (ou do Vice, se autorizado), com maioria "
          "absoluta dos membros, decidindo em caráter secreto por maioria. Extraordinariamente, reúne-se "
          "como 'Tribunal de Ética', a pedido de Comissão Permanente de Disciplina, para dar parecer sobre "
          "conduta/atos de policial em processos que apuram as transgressões dos itens VII, VIII, XVIII, "
          "XXXI, XXXIV, XXXV, XXXVI, XXXVII, XXXVIII, XXXIX, XLIII, XLIV, XLVI, XLVII e XLVIII do art. 31, "
          "e os casos de demissão dos itens IV, VII, X e XI do art. 49. Pode elaborar seu próprio Regimento "
          "Interno."},

    {"t": "cap", "x": "TÍTULO VII — DISPOSIÇÕES FINAIS (Art. 81 a 88)"},
    {"t": "art", "n": "Art. 82",
     "x": "O policial civil que se invalidar definitivamente em razão de serviço é promovido ao padrão "
          "imediatamente superior por merecimento, aposentando-se com os vencimentos e vantagens do novo "
          "cargo — essa promoção não conta para efeito de alternância dos critérios de promoção. Desde a "
          "Lei nº 15.093/2013, o Policial Civil com incapacidade definitiva para a atividade-fim decorrente "
          "de deficiência pode, mediante requerimento, permanecer no serviço em atividade administrativa, "
          "sendo readaptado em função compatível, desde que julgado apto por Junta Médica do Estado e "
          "atendida a conveniência do serviço — nesse caso, não faz jus à promoção do caput."},
    {"t": "art", "n": "Art. 83 a 86",
     "x": "O Estado concede pensão especial (reajustada como a remuneração dos policiais em atividade, sem "
          "prejuízo da pensão previdenciária) aos beneficiários do policial civil falecido em consequência "
          "de ferimentos em luta contra malfeitores, acidente em serviço, ou moléstia decorrente desses "
          "casos (redação da Lei nº 11.423/1996). Essa pensão equivale à remuneração do padrão imediatamente "
          "superior ao do policial falecido, e se estende também aos beneficiários do art. 82 (invalidez "
          "definitiva) quando a morte decorrer dos mesmos motivos da invalidez — nesse caso, calculada na "
          "base do vencimento em que o policial foi aposentado. O policial civil só pode ser posto à "
          "disposição de órgão da administração direta/indireta (federal, estadual ou municipal), a "
          "critério do Governador, a prazo certo, para exercer atividades de natureza policial."},
    {"t": "art", "n": "Art. 87 e 88",
     "x": "A lei é denominada Estatuto dos Funcionários Policiais Civis da Secretaria da Segurança Pública "
          "do Estado de Pernambuco, em vigor desde a publicação em 29/9/1972. Revogam-se as disposições em "
          "contrário."},
]

array_literal = '[\n' + ',\n'.join(json.dumps(it, ensure_ascii=False) for it in ITEMS) + '\n]'

m = re.search(r'const LAW_PE_CONSTITUICAO\s*=\s*\[[\s\S]*?\n\];', html)
assert m, "bloco LAW_PE_CONSTITUICAO nao encontrado"
insertion_point = m.end()

new_block = '\n\nconst LAW_PE_ESTATUTO_POLICIAL = ' + array_literal + ';'
new_html = html[:insertion_point] + new_block + html[insertion_point:]

old_deck_block = ('const ESTRATEGIA_DECKS = {\n'
                   '  cronograma_pcpe: { label: "Edital e Cronograma — PC-PE (Pernambuco), Agente de '
                   'Polícia", data: CRONOGRAMA_PCPE, corp: null },\n'
                   '  constituicao_pe: { label: "Constituição de PE (trechos) — Segurança Pública e '
                   'Administração", data: LAW_PE_CONSTITUICAO, corp: null }\n'
                   '};')
assert old_deck_block in new_html, "bloco ESTRATEGIA_DECKS nao encontrado como esperado"
new_deck_block = ('const ESTRATEGIA_DECKS = {\n'
                   '  cronograma_pcpe: { label: "Edital e Cronograma — PC-PE (Pernambuco), Agente de '
                   'Polícia", data: CRONOGRAMA_PCPE, corp: null },\n'
                   '  constituicao_pe: { label: "Constituição de PE (trechos) — Segurança Pública e '
                   'Administração", data: LAW_PE_CONSTITUICAO, corp: null },\n'
                   '  estatuto_policial_pe: { label: "Estatuto do Policial Civil de PE (Lei 6.425/1972)", '
                   'data: LAW_PE_ESTATUTO_POLICIAL, corp: null }\n'
                   '};')
new_html = new_html.replace(old_deck_block, new_deck_block, 1)

with open('app-template.html', 'w', encoding='utf-8', newline='') as f:
    f.write(new_html)
print('LAW_PE_ESTATUTO_POLICIAL adicionada com', len(ITEMS), 'itens; registrada em ESTRATEGIA_DECKS.')

with open('questions.json', encoding='utf-8') as f:
    qdata = f.read()
with open('app-template.html', encoding='utf-8') as f:
    html2 = f.read()
html2 = html2.replace('__QUESTIONS_JSON__', qdata)
with open('estudo-cebraspe-ma.html', 'w', encoding='utf-8') as f:
    f.write(html2)
print('estudo-cebraspe-ma.html regenerado com sucesso')
