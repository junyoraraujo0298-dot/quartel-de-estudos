# -*- coding: utf-8 -*-
import json

with open("/home/claude/qbank/questions.json","r",encoding="utf-8") as f:
    BANK = json.load(f)

qid = [max(q["id"] for q in BANK)]
def nid():
    qid[0]+=1
    return qid[0]

def ce(corp, disc, enun, resp, exp):
    BANK.append({"id":nid(),"corp":corp,"disc":disc,"tipo":"CE","enun":enun,"resp":resp,"exp":exp})

def mc(corp, disc, enun, alts, correct, exp):
    assert len(alts)==5
    BANK.append({"id":nid(),"corp":corp,"disc":disc,"tipo":"MC","enun":enun,"alts":alts,"resp":correct,"exp":exp})

# =====================================================================
# BM — mais Portugues
# =====================================================================
mc("BM","Língua Portuguesa","Assinale a alternativa em que o verbo 'haver', no sentido de existir, está corretamente flexionado.",
   ["Haviam muitas ocorrências no plantão.","Devem haver mais equipamentos na base.","Houve muitas ocorrências no plantão.","Vão haver novos cursos em breve.","Houveram vários chamados noturnos."],
   2,"'Houve muitas ocorrências' está correto, pois o verbo 'haver', no sentido de existir, é impessoal e permanece sempre na 3ª pessoa do singular.")
mc("BM","Língua Portuguesa","Assinale a alternativa em que o emprego do pronome está de acordo com a norma-padrão.",
   ["Vi ele na base ontem.","Vi-o na base ontem.","Encontrei ele na base.","Chamei ele para o serviço.","Levei ele até a viatura."],
   1,"'Vi-o na base ontem' está correto, pois, como objeto direto, deve-se usar o pronome oblíquo átono 'o', e não o pronome reto 'ele'.")
mc("BM","Língua Portuguesa","Assinale a alternativa que apresenta a forma verbal correta na frase indicativa de tempo decorrido.",
   ["Fazem dez anos que ele ingressou na corporação.","Faz dez anos que ele ingressou na corporação.","Houveram dez anos de serviço.","Vão fazer, no plural, dez anos.","Fazem-se dez anos de serviço, no plural."],
   1,"'Faz dez anos' está correto, pois o verbo 'fazer', indicando tempo decorrido, é impessoal e permanece sempre no singular.")
mc("BM","Língua Portuguesa","Assinale a alternativa em que a concordância nominal está de acordo com a norma-padrão.",
   ["Seguem anexo os documentos solicitados.","Seguem anexos os documentos solicitados.","Segue anexos o documento solicitado.","Anexo, seguem os documento.","Os documento seguem anexo."],
   1,"'Seguem anexos os documentos' está correto, pois 'anexo', quando usado como adjetivo, concorda em gênero e número com o substantivo a que se refere.")
mc("BM","Língua Portuguesa","Assinale a alternativa que respeita a regra de colocação pronominal (próclise) em início de oração.",
   ["Se apresentou imediatamente à autoridade.","Apresentou-se imediatamente à autoridade.","Se-apresentou imediatamente à autoridade.","Imediatamente se apresentou, é facultativo, à autoridade, sem regra.","Apresentou se imediatamente à autoridade."],
   1,"Em início absoluto de período, a norma-padrão exige a ênclise: 'Apresentou-se imediatamente à autoridade', e não a próclise ('Se apresentou...')."),

# =====================================================================
# BM — mais Historia do Maranhao
# =====================================================================
mc("BM","História do Maranhão","O Estado do Maranhão e Grão-Pará, criado no período colonial, caracterizava-se por:",
   ["Ser administrativamente subordinado diretamente ao Estado do Brasil, sem qualquer autonomia.","Ser administrativamente distinto do Estado do Brasil, subordinando-se diretamente à Coroa portuguesa.","Não ter qualquer ligação com Portugal.","Ser governado exclusivamente por autoridades eclesiásticas.","Ter sido extinto antes da chegada dos franceses a São Luís."],
   1,"O Estado do Maranhão (depois Maranhão e Grão-Pará), criado em 1621, era administrativamente distinto do Estado do Brasil, subordinando-se diretamente à Coroa portuguesa.")
mc("BM","História do Maranhão","Assinale a alternativa que apresenta corretamente uma das lideranças da Balaiada, revolta ocorrida no Maranhão entre 1838 e 1841.",
   ["Tiradentes","Zumbi dos Palmares","Cosme Bento das Chagas, o 'Negro Cosme'","Frei Caneca","Padre Cícero"],
   2,"Cosme Bento das Chagas, conhecido como 'Negro Cosme', foi uma das principais lideranças da Balaiada, liderando um contingente de escravizados fugidos durante o conflito.")
mc("BM","História do Maranhão","A economia do Maranhão, ao longo do século XVIII, foi impulsionada, entre outros fatores, pela atuação de qual companhia de comércio, criada pela Coroa portuguesa?",
   ["Companhia das Índias Orientais","Companhia de Comércio do Grão-Pará e Maranhão","Companhia Holandesa das Índias Ocidentais","Companhia de Jesus","Companhia Geral do Brasil"],
   1,"A Companhia de Comércio do Grão-Pará e Maranhão, criada no século XVIII, teve papel relevante no fomento à produção e exportação de produtos como o algodão na região.")
mc("BM","História do Maranhão","A adesão do Maranhão ao processo de independência do Brasil, em 1823, teve destacada participação militar de qual figura histórica na repressão à resistência portuguesa em São Luís?",
   ["Duque de Caxias","Lord Cochrane","Marquês de Tamandaré","Barão do Rio Branco","Duque de Bragança"],
   1,"Lord Cochrane, contratado pelo governo brasileiro, teve papel destacado na repressão à resistência portuguesa em São Luís, contribuindo para a efetiva adesão do Maranhão à independência em 1823.")
mc("BM","História do Maranhão","O reconhecimento do Centro Histórico de São Luís como Patrimônio Mundial pela UNESCO, em 1997, deveu-se, principalmente, a:",
   ["Seu conjunto arquitetônico colonial preservado, com destaque para o uso de azulejos portugueses nas fachadas.","Sua localização na foz do rio Amazonas.","A presença de vulcões ativos na região.","Ser o único destino turístico do Nordeste brasileiro.","Abrigar a maior floresta urbana do mundo."],
   0,"O reconhecimento se deu, sobretudo, em razão do conjunto arquitetônico colonial português preservado no centro da cidade, com destaque para o uso característico de azulejos nas fachadas."),

# =====================================================================
# BM — mais Geografia do Maranhao
# =====================================================================
mc("BM","Geografia do Maranhão","Em relação à extensão territorial, o Maranhão pode ser corretamente descrito como:",
   ["O menor estado da região Nordeste.","O maior estado da região Nordeste em área territorial.","Um estado sem litoral.","O único estado nordestino sem municípios costeiros.","Um estado com território menor que o do Sergipe."],
   1,"Com pouco mais de 331 mil km², o Maranhão é o maior estado em área territorial entre os que compõem a região Nordeste do Brasil.")
mc("BM","Geografia do Maranhão","A Estrada de Ferro Carajás, de grande relevância econômica para o Maranhão, tem como função principal:",
   ["Transportar passageiros entre São Luís e Teresina.","Escoar a produção de minério de ferro da mina de Carajás (PA) até o Porto do Itaqui, em São Luís (MA).","Conectar exclusivamente polos turísticos do litoral maranhense.","Servir apenas ao transporte de cargas agrícolas do sul do estado.","Ligar o Maranhão ao Distrito Federal."],
   1,"A Estrada de Ferro Carajás liga a mina de Carajás, no Pará, ao Porto do Itaqui, em São Luís, sendo estratégica para o escoamento de minério de ferro produzido na região.")
mc("BM","Geografia do Maranhão","Assinale a alternativa que descreve corretamente o clima predominante no território maranhense.",
   ["Frio, com neve frequente no inverno.","Tropical, com estações de chuva e estiagem bem definidas, havendo variações regionais.","Desértico, sem qualquer período chuvoso.","Subpolar, com baixas temperaturas o ano todo.","Mediterrâneo, com verões secos e invernos chuvosos."],
   1,"O Maranhão apresenta clima tropical, com um período mais chuvoso e outro mais seco, havendo variações regionais, sobretudo no leste do estado, com tendência a maior semiaridez.")
mc("BM","Geografia do Maranhão","O chamado 'Golfão Maranhense', feição marcante do litoral do estado, caracteriza-se por:",
   ["Uma extensa cordilheira montanhosa.","Uma reentrância litorânea formada por baías e desembocaduras de rios.","Um deserto de dunas sem qualquer vegetação.","Uma região exclusivamente urbana, sem cobertura vegetal.","Um platô de altitude elevada, acima de 2.000 metros."],
   1,"O Golfão Maranhense é uma extensa reentrância litorânea, formada por baías (como as de São Marcos e São José) e desembocaduras de rios, sendo característica marcante da costa maranhense.")
mc("BM","Geografia do Maranhão","A vegetação do território maranhense caracteriza-se por:",
   ["Ser uniforme em todo o estado, sem qualquer variação.","Apresentar transição entre formações amazônicas, de cerrado e, em menor grau, de caatinga.","Ser composta exclusivamente por vegetação de restinga.","Não apresentar qualquer influência amazônica.","Ser idêntica à vegetação da região Sul do Brasil."],
   1,"Por sua posição de transição, o Maranhão apresenta vegetação diversificada, com influências da Amazônia, do Cerrado e, em menor grau, da Caatinga."),

# =====================================================================
# BM — mais Ingles
# =====================================================================
mc("BM","Língua Estrangeira (Inglês)","Choose the correct translation for: 'The fire department responded quickly to the emergency call.'",
   ["O corpo de bombeiros respondeu rapidamente à chamada de emergência.","O corpo de bombeiros ignorou a chamada de emergência.","A chamada de emergência respondeu ao corpo de bombeiros.","O corpo de bombeiros ligou para a emergência.","A emergência chamou o corpo de bombeiros rapidamente, sem resposta."],
   0,"A tradução correta é 'O corpo de bombeiros respondeu rapidamente à chamada de emergência', pois 'responded' significa 'respondeu' e 'emergency call' significa 'chamada de emergência'.")
mc("BM","Língua Estrangeira (Inglês)","Assinale a alternativa que apresenta o correto significado da palavra 'rescue' em português.",
   ["Resgate","Descanso","Registro","Reserva","Recusa"],
   0,"'Rescue' significa 'resgate' em português, geralmente associado a operações de salvamento de vítimas.")
mc("BM","Língua Estrangeira (Inglês)","Fill in the blank: 'The victim ______ trapped inside the vehicle when the firefighters arrived.'",
   ["was","were","is","are","be"],
   0,"O sujeito 'the victim' está no singular, exigindo o verbo 'to be' no passado na forma 'was': 'The victim was trapped...'.")
mc("BM","Língua Estrangeira (Inglês)","Assinale a alternativa que apresenta o correto significado da palavra 'smoke' em português.",
   ["Chama","Fumaça","Calor","Cinza","Fogo"],
   1,"'Smoke' significa 'fumaça' em português.")
mc("BM","Língua Estrangeira (Inglês)","Choose the correct sentence in the simple past tense.",
   ["The firefighters extinguish the fire yesterday.","The firefighters extinguished the fire yesterday.","The firefighters extinguishing the fire yesterday.","The firefighters will extinguish the fire yesterday.","The firefighters extinguishes the fire yesterday."],
   1,"A forma correta no passado simples é 'extinguished': 'The firefighters extinguished the fire yesterday.'"),

# =====================================================================
# BM — mais Legislacao Institucional
# =====================================================================
mc("BM","Legislação Institucional","Assinale a alternativa correta acerca das fases previstas em concursos públicos para ingresso em corporações militares estaduais.",
   ["Apenas a prova objetiva é exigida, sem outras etapas.","Além da prova objetiva, costumam ser exigidas, entre outras, avaliação de saúde, teste de aptidão física, avaliação psicológica e investigação social.","Somente a avaliação psicológica é etapa eliminatória.","O teste de aptidão física é etapa meramente classificatória, nunca eliminatória.","A investigação social é etapa exclusiva de cargos de nível superior."],
   1,"Concursos para ingresso em corporações militares estaduais costumam prever, além da prova objetiva, fases como avaliação de saúde, teste de aptidão física, avaliação psicológica e investigação social, todas de caráter eliminatório.")
mc("BM","Legislação Institucional","No que se refere ao poder disciplinar no âmbito militar, é correto afirmar que:",
   ["Permite a aplicação de sanções por transgressões, assegurados o contraditório e a ampla defesa.","Dispensa qualquer forma de defesa do acusado.","Aplica-se apenas a oficiais, nunca a praças.","É exercido exclusivamente pelo Poder Judiciário.","Não pode resultar em qualquer tipo de punição administrativa."],
   0,"O poder disciplinar autoriza a apuração e a aplicação de sanções por transgressões no âmbito da corporação, sempre respeitando as garantias constitucionais do contraditório e da ampla defesa.")
mc("BM","Legislação Institucional","Em relação às promoções na carreira militar estadual, os critérios comumente adotados incluem:",
   ["Apenas sorteio entre os candidatos.","Antiguidade e merecimento, conforme critérios estabelecidos em regulamentos específicos.","Exclusivamente indicação política.","Somente escolaridade em nível superior.","Apenas tempo de afastamento por licença."],
   1,"Antiguidade e merecimento são critérios clássicos de promoção nas carreiras militares, previstos de forma geral nos estatutos e regulamentos de promoções das corporações.")
mc("BM","Legislação Institucional","Assinale a alternativa correta sobre a natureza do vínculo do militar estadual durante o curso de formação.",
   ["O candidato aprovado ingressa imediatamente como oficial superior.","O candidato aprovado ingressa na corporação como aluno, por período correspondente à duração do curso de formação.","Não há qualquer vínculo até a conclusão de toda a carreira.","O vínculo somente se inicia após dez anos de serviço.","O candidato aprovado já ingressa na reserva remunerada."],
   1,"Conforme previsto em editais desse tipo de concurso, os candidatos aprovados ingressam na corporação na condição de aluno, durante o período correspondente à duração do curso de formação.")
mc("BM","Legislação Institucional","Assinale a alternativa que descreve corretamente a relação entre hierarquia e disciplina no âmbito militar.",
   ["São conceitos equivalentes e intercambiáveis.","A hierarquia é a ordenação da autoridade em níveis; a disciplina é a observância das leis, regulamentos e normas.","A disciplina só se aplica a oficiais; a hierarquia, apenas a praças.","A hierarquia é opcional, dependendo da vontade do comandante.","A disciplina é aplicável exclusivamente durante o período de guerra."],
   1,"A hierarquia é a ordenação da autoridade em diferentes níveis dentro da estrutura militar, e a disciplina consiste na rigorosa observância das leis, regulamentos e normas, sendo ambas a base institucional das corporações militares."),

# =====================================================================
# BM — mais Primeiros Socorros
# =====================================================================
mc("BM","Noções de Primeiros Socorros","Diante de uma vítima consciente que está engasgada e não consegue tossir, falar ou respirar, a manobra recomendada como primeiro socorro é:",
   ["Dar tapas fortes nas costas exclusivamente, sem outra manobra.","Realizar a manobra de Heimlich (compressões abdominais).","Oferecer água imediatamente à vítima.","Induzir o vômito da vítima.","Aguardar a vítima se recuperar sozinha, sem qualquer intervenção."],
   1,"A manobra de Heimlich, com compressões abdominais, é a técnica recomendada para desobstrução de vias aéreas em vítimas conscientes engasgadas que não conseguem tossir, falar ou respirar.")
mc("BM","Noções de Primeiros Socorros","Em relação a uma vítima com suspeita de lesão na coluna vertebral, a conduta correta de primeiros socorros é:",
   ["Movimentar a vítima livremente para verificar a extensão da lesão.","Evitar ao máximo a movimentação da vítima, estabilizando a região até a chegada do socorro especializado.","Sentar a vítima imediatamente, independentemente do quadro.","Fazer a vítima caminhar para avaliar se sente dor.","Aplicar calor intenso na região suspeita."],
   1,"Diante de suspeita de lesão na coluna, deve-se evitar ao máximo a movimentação da vítima, estabilizando a região e aguardando o atendimento especializado, para não agravar eventual lesão medular.")
mc("BM","Noções de Primeiros Socorros","Os sinais vitais comumente avaliados em uma vítima incluem:",
   ["Apenas a temperatura corporal.","Frequência cardíaca, frequência respiratória, temperatura corporal e pressão arterial.","Somente o nível de consciência.","Apenas a cor da pele.","Somente o tamanho da pupila."],
   1,"Os sinais vitais clássicos avaliados incluem frequência cardíaca, frequência respiratória, temperatura corporal e pressão arterial, entre outros parâmetros relevantes para a avaliação inicial da vítima.")
mc("BM","Noções de Primeiros Socorros","Em caso de suspeita de infarto agudo do miocárdio, um dos sinais e sintomas mais característicos é:",
   ["Dor ou aperto no peito, podendo irradiar para o braço esquerdo, mandíbula ou costas.","Coceira intensa na pele, exclusivamente.","Melhora imediata da dor ao repouso, sem qualquer outro sintoma.","Ausência total de qualquer desconforto físico.","Aumento da acuidade visual repentino."],
   0,"A dor ou aperto no peito, que pode irradiar para o braço esquerdo, mandíbula ou costas, é um dos sinais mais característicos de um possível infarto agudo do miocárdio, exigindo atendimento de urgência.")
mc("BM","Noções de Primeiros Socorros","Um dos sinais de alerta para um possível Acidente Vascular Cerebral (AVC), segundo protocolos de reconhecimento rápido, é:",
   ["Melhora súbita da força muscular em um dos lados do corpo.","Fraqueza ou paralisia súbita em um dos lados do rosto, braço ou perna.","Aumento da temperatura corporal exclusivamente.","Dor intensa e localizada no joelho.","Melhora repentina da fala, sem qualquer outro sintoma."],
   1,"A fraqueza ou paralisia súbita em um dos lados do corpo (rosto, braço ou perna), muitas vezes acompanhada de dificuldade na fala, é um dos sinais de alerta mais reconhecidos para um possível AVC."),

# =====================================================================
# BM — mais Combate a Incendio
# =====================================================================
mc("BM","Noções de Combate a Incêndio","Assinale a alternativa que indica corretamente a classe de incêndio relacionada a materiais combustíveis comuns, como madeira, papel e tecido.",
   ["Classe A","Classe B","Classe C","Classe D","Classe K"],
   0,"A classe A de incêndio refere-se a materiais combustíveis comuns, como madeira, papel, tecido e a maioria dos plásticos, que deixam resíduos (cinzas) após a queima.")
mc("BM","Noções de Combate a Incêndio","O incêndio classe K está relacionado a:",
   ["Materiais combustíveis comuns.","Líquidos inflamáveis.","Equipamentos elétricos energizados.","Óleos e gorduras utilizados em equipamentos de cocção.","Metais combustíveis."],
   3,"A classe K refere-se a incêndios envolvendo óleos e gorduras utilizados em equipamentos de cocção, comuns em cozinhas industriais, exigindo agentes extintores específicos.")
mc("BM","Noções de Combate a Incêndio","Assinale a alternativa que apresenta corretamente os três elementos que compõem o chamado 'triângulo do fogo'.",
   ["Água, fumaça e calor.","Combustível, comburente e calor.","Combustível, fumaça e vento.","Comburente, água e cinza.","Calor, cinza e fumaça."],
   1,"O triângulo do fogo é formado por combustível, comburente (geralmente oxigênio) e calor; a ausência de qualquer um desses elementos impede ou extingue a combustão.")
mc("BM","Noções de Combate a Incêndio","Em relação aos métodos de extinção do fogo, o chamado 'abafamento' consiste em:",
   ["Retirar o calor da reação de combustão.","Eliminar ou reduzir o comburente (oxigênio) disponível para a combustão.","Retirar o material combustível do local do incêndio.","Aumentar a quantidade de oxigênio disponível.","Aplicar exclusivamente água sobre o fogo."],
   1,"O abafamento consiste em eliminar ou reduzir a disponibilidade de comburente (oxigênio) para a combustão, interrompendo a reação em cadeia do fogo.")
mc("BM","Noções de Combate a Incêndio","O método de extinção conhecido como 'resfriamento' atua, principalmente, sobre qual elemento do triângulo do fogo?",
   ["Combustível","Comburente","Calor","Vento","Fumaça"],
   2,"O resfriamento consiste em retirar o calor da reação de combustão, geralmente por meio da aplicação de água, reduzindo a temperatura abaixo do ponto necessário para a manutenção do fogo."),

# =====================================================================
# BM — mais Seguranca Contra Incendio e Panico
# =====================================================================
mc("BM","Segurança Contra Incêndio e Pânico","Os extintores de incêndio devem passar por inspeções e manutenções periódicas, de responsabilidade do proprietário ou responsável pela edificação, com a finalidade principal de:",
   ["Garantir apenas a estética do equipamento.","Assegurar que o equipamento esteja em condições adequadas de funcionamento em caso de necessidade.","Evitar exclusivamente furtos do equipamento.","Substituir a necessidade de treinamento dos ocupantes.","Aumentar o valor de revenda do imóvel."],
   1,"As inspeções e manutenções periódicas dos extintores visam garantir que o equipamento esteja em plenas condições de uso, assegurando sua eficácia em uma eventual situação de incêndio.")
mc("BM","Segurança Contra Incêndio e Pânico","Em relação à sinalização de emergência em edificações, as placas indicativas de rota de fuga e saída de emergência costumam utilizar predominantemente qual cor de fundo?",
   ["Vermelho","Amarelo","Verde","Azul","Preto"],
   2,"A cor verde é tradicionalmente utilizada na sinalização de rotas de fuga e saídas de emergência, indicando segurança e orientação para escape.")
mc("BM","Segurança Contra Incêndio e Pânico","O sistema de hidrantes em uma edificação tem como principal finalidade:",
   ["Fornecer água potável aos ocupantes do prédio.","Disponibilizar água sob pressão para o combate a incêndios de maior porte.","Substituir integralmente os extintores portáteis.","Servir apenas como reserva técnica para limpeza.","Realizar a climatização do ambiente."],
   1,"O sistema de hidrantes fornece água sob pressão suficiente para o combate a incêndios de maior porte, complementando o uso de extintores portáteis, que são indicados para princípios de incêndio.")
mc("BM","Segurança Contra Incêndio e Pânico","No dimensionamento da segurança contra incêndio de uma edificação, a 'população' considerada corresponde:",
   ["Apenas ao número de funcionários da administração do prédio.","À estimativa do número de pessoas que podem ocupar simultaneamente a edificação, conforme seu uso.","Ao número de veículos estacionados no local.","À quantidade de equipamentos elétricos instalados.","Ao número de pavimentos da edificação."],
   1,"A população de uma edificação, para fins de segurança contra incêndio, corresponde à estimativa do número de pessoas que podem ocupá-la simultaneamente, considerando a área e o tipo de uso, parâmetro relevante para o dimensionamento de saídas e demais medidas de segurança.")
mc("BM","Segurança Contra Incêndio e Pânico","Em uma situação de princípio de incêndio em ambiente com grande concentração de pessoas, uma medida fundamental de segurança contra pânico é:",
   ["Manter todas as saídas trancadas até a chegada do Corpo de Bombeiros.","Orientar a evacuação ordenada, utilizando rotas de fuga previamente sinalizadas e desobstruídas.","Aglomerar todas as pessoas em um único ponto do ambiente.","Desligar toda a iluminação do ambiente, mesmo a de emergência.","Aguardar instruções sem qualquer ação imediata."],
   1,"A orientação para uma evacuação ordenada, utilizando rotas de fuga sinalizadas e desobstruídas, é medida fundamental para reduzir o risco de pânico e acidentes durante a evacuação de um ambiente com grande concentração de pessoas."),

# =====================================================================
# PC — mais Direito Constitucional
# =====================================================================
mc("PC","Direito Constitucional","Assinale a alternativa correta acerca do princípio da separação dos poderes previsto na Constituição Federal.",
   ["Os poderes Executivo, Legislativo e Judiciário são absolutamente independentes entre si, sem qualquer mecanismo de controle recíproco.","Os poderes são independentes e harmônicos entre si, havendo mecanismos de controle recíproco (freios e contrapesos).","Apenas o Poder Executivo exerce função legislativa no Brasil.","O Poder Judiciário está subordinado hierarquicamente ao Poder Executivo.","A separação dos poderes foi abolida pela Constituição de 1988."],
   1,"O art. 2º da CF estabelece que os Poderes Executivo, Legislativo e Judiciário são independentes e harmônicos entre si, havendo mecanismos de controle recíproco (freios e contrapesos) entre eles.")
mc("PC","Direito Constitucional","Em relação aos remédios constitucionais, o mandado de injunção é cabível quando:",
   ["Há violação da liberdade de locomoção.","Falta norma regulamentadora que inviabilize o exercício de direitos e liberdades constitucionais.","Se busca acesso a informações pessoais constantes de banco de dados públicos.","Há necessidade de proteger direito líquido e certo não amparado por habeas corpus ou habeas data.","Se pretende a anulação de ato lesivo ao patrimônio público."],
   1,"O mandado de injunção, previsto no art. 5º, LXXI, da CF, é cabível quando a falta de norma regulamentadora torna inviável o exercício de direitos e liberdades constitucionais e das prerrogativas inerentes à nacionalidade, à soberania e à cidadania.")
mc("PC","Direito Constitucional","Assinale a alternativa correta sobre o instituto do habeas data, previsto na Constituição Federal.",
   ["Destina-se a proteger a liberdade de locomoção.","Destina-se a assegurar o conhecimento ou a retificação de informações relativas à pessoa do impetrante, constantes de registros ou bancos de dados de entidades governamentais ou de caráter público.","Cabe exclusivamente contra atos de particulares.","Substitui o mandado de segurança em qualquer hipótese.","Aplica-se apenas a informações de natureza penal."],
   1,"O habeas data, previsto no art. 5º, LXXII, da CF, destina-se a assegurar o conhecimento ou a retificação de informações relativas à pessoa do impetrante, constantes de registros ou bancos de dados de entidades governamentais ou de caráter público.")
mc("PC","Direito Constitucional","Sobre os remédios constitucionais e a legitimidade para propor ação popular, é correto afirmar que:",
   ["Qualquer cidadão é parte legítima para propor ação popular que vise anular ato lesivo ao patrimônio público, à moralidade administrativa, ao meio ambiente ou ao patrimônio histórico e cultural.","Somente o Ministério Público pode propor ação popular.","A ação popular é cabível apenas contra atos de particulares.","A ação popular substitui integralmente o mandado de segurança coletivo.","Estrangeiros não residentes podem propor ação popular livremente."],
   0,"Conforme art. 5º, LXXIII, da CF, qualquer cidadão é parte legítima para propor ação popular que vise anular ato lesivo ao patrimônio público, à moralidade administrativa, ao meio ambiente e ao patrimônio histórico e cultural.")
mc("PC","Direito Constitucional","Em relação à organização dos poderes no âmbito estadual, é correto afirmar que:",
   ["Os Estados-membros não possuem autonomia para organizar seus próprios poderes.","Os Estados-membros organizam-se e regem-se pelas Constituições e leis que adotarem, observados os princípios da Constituição Federal.","Somente a União pode legislar sobre organização administrativa estadual.","Os Estados-membros estão subordinados hierarquicamente à União em todas as matérias.","Não existe repartição de competências entre União, Estados e Municípios."],
   1,"Conforme art. 25 da CF, os Estados organizam-se e regem-se pelas Constituições e leis que adotarem, observados os princípios da Constituição Federal, no exercício de sua autonomia federativa."),

# =====================================================================
# PC — mais Direito Administrativo
# =====================================================================
mc("PC","Direito Administrativo","Assinale a alternativa correta acerca dos poderes administrativos.",
   ["O poder de polícia permite à Administração restringir e condicionar o exercício de direitos individuais em benefício do interesse coletivo, observados os limites legais.","O poder hierárquico permite ao superior delegar responsabilidade penal a seus subordinados.","O poder disciplinar aplica-se exclusivamente a particulares contratados pela Administração.","O poder regulamentar permite ao chefe do Executivo criar obrigações não previstas em lei, livremente.","O poder vinculado é sinônimo de poder discricionário."],
   0,"O poder de polícia é a prerrogativa que permite à Administração restringir e condicionar o exercício de direitos e atividades individuais em prol do interesse coletivo, sempre observados os limites legais.")
mc("PC","Direito Administrativo","No que se refere aos contratos administrativos, é correto afirmar que a Administração Pública possui, entre outras, a prerrogativa de:",
   ["Modificar unilateralmente as cláusulas contratuais, respeitados os limites legais e o equilíbrio econômico-financeiro do contrato.","Descumprir integralmente o contrato sem qualquer consequência.","Transferir a terceiros, livremente, a execução do contrato, sem anuência da Administração.","Extinguir o contrato sem qualquer motivação.","Aplicar sanções sem observância do contraditório e da ampla defesa."],
   0,"Entre as chamadas cláusulas exorbitantes dos contratos administrativos, está a possibilidade de a Administração modificar unilateralmente as cláusulas contratuais, respeitados os limites legais e o equilíbrio econômico-financeiro do contrato.")
mc("PC","Direito Administrativo","Assinale a alternativa correta acerca da improbidade administrativa.",
   ["A Lei de Improbidade Administrativa não prevê sanções de natureza civil ou política, apenas penal.","Atos de improbidade administrativa podem resultar em sanções como ressarcimento ao erário, perda da função pública e suspensão dos direitos políticos, conforme previsto em lei.","A improbidade administrativa somente pode ser praticada por agentes de nível superior.","Não há distinção legal entre os diferentes tipos de atos de improbidade administrativa.","A ação de improbidade administrativa prescreve em prazo idêntico ao da prescrição penal, em qualquer hipótese."],
   1,"A Lei de Improbidade Administrativa (Lei nº 8.429/1992, com alterações) prevê sanções como o ressarcimento ao erário, a perda da função pública e a suspensão dos direitos políticos, entre outras, a depender do tipo de ato de improbidade praticado.")
mc("PC","Direito Administrativo","Em relação à responsabilidade civil do Estado, a Constituição Federal adota, como regra geral, a teoria:",
   ["Da culpa subjetiva, exigindo prova de dolo ou culpa do agente público.","Da responsabilidade objetiva, sob a modalidade do risco administrativo, admitindo excludentes como caso fortuito, força maior e culpa exclusiva da vítima.","Da irresponsabilidade estatal absoluta.","Da responsabilidade subjetiva exclusiva para atos comissivos.","Da responsabilidade solidária automática entre Estado e agente, sem direito de regresso."],
   1,"Conforme art. 37, §6º, da CF, o Estado responde objetivamente pelos danos causados por seus agentes a terceiros, na modalidade do risco administrativo, admitindo-se excludentes como caso fortuito, força maior e culpa exclusiva da vítima."),

# =====================================================================
# PC — mais Direito Penal
# =====================================================================
mc("PC","Direito Penal","Assinale a alternativa correta acerca do concurso de pessoas no Direito Penal.",
   ["Somente é possível em crimes culposos.","Ocorre quando duas ou mais pessoas concorrem para a prática do mesmo crime, respondendo cada uma na medida de sua culpabilidade.","Exclui automaticamente a responsabilidade penal de todos os envolvidos.","Aplica-se apenas a crimes contra o patrimônio.","Impede a diferenciação entre autor e partícipe."],
   1,"O concurso de pessoas ocorre quando duas ou mais pessoas concorrem para a prática do mesmo crime, respondendo cada uma na medida de sua culpabilidade, distinguindo-se, conforme o caso, autores e partícipes.")
mc("PC","Direito Penal","Sobre as causas excludentes de ilicitude previstas no Código Penal, assinale a alternativa correta.",
   ["Incluem apenas a legítima defesa.","Incluem o estado de necessidade, a legítima defesa, o estrito cumprimento do dever legal e o exercício regular de direito.","Excluem sempre a existência do próprio fato típico.","Aplicam-se somente a agentes públicos.","Não podem ser reconhecidas de ofício pelo juiz."],
   1,"O art. 23 do Código Penal prevê como causas excludentes de ilicitude o estado de necessidade, a legítima defesa, o estrito cumprimento do dever legal e o exercício regular de direito.")
mc("PC","Direito Penal","Em relação à tentativa, prevista no Código Penal, é correto afirmar que:",
   ["Ocorre quando o crime é consumado integralmente.","Ocorre quando, iniciada a execução, o crime não se consuma por circunstâncias alheias à vontade do agente.","É sempre punida com a mesma pena do crime consumado, sem qualquer redução.","Não é prevista no ordenamento jurídico brasileiro.","Aplica-se apenas a contravenções penais."],
   1,"Conforme art. 14, II, do CP, há tentativa quando, iniciada a execução do crime, este não se consuma por circunstâncias alheias à vontade do agente, sendo a pena, em regra, reduzida em relação ao crime consumado.")
mc("PC","Direito Penal","Assinale a alternativa correta a respeito da diferença entre crime e contravenção penal no ordenamento jurídico brasileiro.",
   ["Não há qualquer distinção entre esses institutos.","Crimes são sempre julgados por júri popular; contravenções, nunca.","Às contravenções penais são cominadas penas de prisão simples ou multa, enquanto aos crimes podem ser cominadas penas de reclusão ou detenção, além de multa.","Contravenções penais são mais graves que crimes, em regra.","Apenas crimes admitem a aplicação de medidas de segurança."],
   2,"Segundo a Lei de Introdução ao Código Penal, às contravenções penais cominam-se penas de prisão simples ou multa, enquanto aos crimes podem ser cominadas penas de reclusão ou detenção, isolada, alternativa ou cumulativamente com multa.")
mc("PC","Direito Penal","Sobre a culpabilidade como elemento do crime, assinale a alternativa correta.",
   ["É sinônimo de tipicidade.","É composta, segundo a teoria finalista predominante, pela imputabilidade, potencial consciência da ilicitude e exigibilidade de conduta diversa.","Não é considerada elemento do crime pela doutrina majoritária.","Aplica-se apenas a pessoas jurídicas.","Independe da imputabilidade do agente."],
   1,"Segundo a teoria finalista da ação, majoritariamente adotada, a culpabilidade é composta pela imputabilidade, pela potencial consciência da ilicitude e pela exigibilidade de conduta diversa."),

# =====================================================================
# PC — mais Processo Penal
# =====================================================================
mc("PC","Direito Processual Penal","Assinale a alternativa correta acerca dos sujeitos processuais no processo penal.",
   ["O Ministério Público não pode atuar como parte no processo penal.","O juiz, o Ministério Público, o acusado e seu defensor são exemplos de sujeitos processuais.","Somente o acusado é considerado sujeito processual.","O defensor não integra o processo penal.","A vítima nunca pode participar do processo penal, em qualquer hipótese."],
   1,"São exemplos de sujeitos processuais no processo penal o juiz, o Ministério Público (titular da ação penal pública), o acusado e seu defensor, entre outros, a depender da hipótese.")
mc("PC","Direito Processual Penal","Em relação às provas no processo penal, é correto afirmar que:",
   ["São inadmissíveis as provas obtidas por meios ilícitos, conforme previsão constitucional.","Todas as provas, ainda que ilícitas, devem ser admitidas pelo juiz.","O ônus da prova compete exclusivamente ao acusado.","A confissão do acusado é prova plena e absoluta, dispensando qualquer outra análise.","Não existe qualquer critério de valoração das provas no processo penal brasileiro."],
   0,"Conforme art. 5º, LVI, da CF, são inadmissíveis, no processo, as provas obtidas por meios ilícitos, sendo esse um dos princípios centrais do processo penal brasileiro.")
mc("PC","Direito Processual Penal","No que se refere às medidas cautelares diversas da prisão, previstas no Código de Processo Penal, é correto afirmar que:",
   ["Somente podem ser aplicadas cumulativamente com a prisão preventiva.","Podem ser aplicadas isoladamente ou cumulativamente, como alternativas à prisão preventiva, quando adequadas e suficientes ao caso concreto.","Substituem, em qualquer caso, a necessidade de comparecimento a atos processuais.","Não podem ser fiscalizadas pelo juiz.","Não têm qualquer previsão no ordenamento jurídico brasileiro."],
   1,"O art. 319 do CPP prevê diversas medidas cautelares alternativas à prisão preventiva, que podem ser aplicadas isolada ou cumulativamente, sempre que se mostrarem adequadas e suficientes para a hipótese concreta.")
mc("PC","Direito Processual Penal","Assinale a alternativa correta sobre a ação penal pública incondicionada.",
   ["Depende de representação da vítima para ser iniciada.","É promovida pelo Ministério Público independentemente de qualquer condição de procedibilidade, sendo regida pelo princípio da obrigatoriedade.","Somente pode ser proposta pela própria vítima.","Extingue-se automaticamente com a morte do agressor, mesmo antes da denúncia.","Depende de autorização do Poder Judiciário para sua propositura pelo Ministério Público."],
   1,"A ação penal pública incondicionada é promovida pelo Ministério Público, independentemente de representação da vítima ou de qualquer outra condição de procedibilidade, sendo regida pelo princípio da obrigatoriedade."),

# =====================================================================
# PC — mais Direitos Humanos
# =====================================================================
mc("PC","Direitos Humanos","Assinale a alternativa correta a respeito do Sistema Interamericano de Proteção dos Direitos Humanos.",
   ["É composto exclusivamente pela Corte Interamericana de Direitos Humanos.","É composto pela Comissão Interamericana de Direitos Humanos e pela Corte Interamericana de Direitos Humanos, no âmbito da Organização dos Estados Americanos (OEA).","Não possui qualquer relação com a Organização dos Estados Americanos.","Aplica-se apenas a países europeus.","Substitui integralmente o sistema global da ONU."],
   1,"O Sistema Interamericano é composto pela Comissão Interamericana de Direitos Humanos e pela Corte Interamericana de Direitos Humanos, ambas vinculadas à Organização dos Estados Americanos (OEA).")
mc("PC","Direitos Humanos","Sobre a dignidade da pessoa humana, fundamento da República Federativa do Brasil previsto no art. 1º, III, da Constituição Federal, é correto afirmar que:",
   ["É um valor meramente programático, sem qualquer aplicabilidade prática.","Constitui fundamento estruturante do ordenamento jurídico brasileiro, orientando a interpretação de todo o sistema de direitos fundamentais.","Aplica-se exclusivamente a cidadãos brasileiros natos.","Foi introduzida apenas por emenda constitucional posterior a 1988.","Não possui qualquer relação com os direitos fundamentais previstos no art. 5º da CF."],
   1,"A dignidade da pessoa humana é fundamento estruturante da República e do ordenamento jurídico brasileiro, orientando a interpretação e a aplicação de todo o sistema de direitos fundamentais.")
mc("PC","Direitos Humanos","Em relação ao princípio da não discriminação em direitos humanos, é correto afirmar que ele veda, entre outras formas de discriminação, distinções fundadas em:",
   ["Mérito profissional comprovado.","Raça, cor, sexo, orientação sexual, religião, origem ou condição social, entre outros fatores arbitrários.","Idade mínima exigida para determinados cargos públicos, quando prevista em lei e proporcional.","Habilitação técnica exigida para o exercício de profissão regulamentada.","Critérios objetivos de aprovação em concurso público."],
   1,"O princípio da não discriminação veda distinções arbitrárias fundadas em características como raça, cor, sexo, orientação sexual, religião, origem ou condição social, entre outros fatores que não se relacionem a critérios legítimos e proporcionais."),

# =====================================================================
# PC — mais Medicina Legal
# =====================================================================
mc("PC","Medicina Legal","Assinale a alternativa que descreve corretamente o exame de corpo de delito.",
   ["É facultativo em crimes que deixam vestígios, podendo ser substituído livremente por prova testemunhal.","É indispensável nas infrações que deixarem vestígios, não podendo supri-lo a confissão do acusado.","Aplica-se apenas em crimes contra a vida.","É realizado exclusivamente por autoridade policial, sem participação de perito.","Não é regulamentado pelo Código de Processo Penal."],
   1,"Conforme art. 158 do CPP, quando a infração deixar vestígios, será indispensável o exame de corpo de delito, direto ou indireto, não podendo supri-lo a confissão do acusado.")
mc("PC","Medicina Legal","Em relação aos fenômenos cadavéricos transformativos (como a putrefação), é correto afirmar que:",
   ["Ocorrem imediatamente após a morte, antes dos fenômenos abióticos.","Correspondem a processos de decomposição do corpo que se seguem aos fenômenos abióticos imediatos (como resfriamento e rigidez).","Não têm qualquer relevância para a estimativa do tempo de morte.","São idênticos aos fenômenos vitais.","Ocorrem apenas em ambientes aquáticos."],
   1,"Os fenômenos transformativos, como a putrefação, correspondem aos processos de decomposição do corpo que se seguem aos fenômenos abióticos imediatos (como resfriamento, rigidez e livores cadavéricos), sendo relevantes para a estimativa da data da morte.")
mc("PC","Medicina Legal","Assinale a alternativa que apresenta corretamente um dos objetivos da traumatologia forense.",
   ["Estudar exclusivamente doenças infecciosas.","Estudar as lesões corporais resultantes de energias de diferentes naturezas (mecânica, física, química), estabelecendo nexo causal e classificação médico-legal.","Analisar apenas fenômenos cadavéricos tardios.","Substituir integralmente a perícia criminal em locais de crime.","Aplicar-se exclusivamente a mortes por causas naturais."],
   1,"A traumatologia forense estuda as lesões corporais decorrentes de diferentes energias (mecânica, física, química, entre outras), estabelecendo o nexo causal e a classificação médico-legal das lesões, relevante para a tipificação penal."),

# =====================================================================
# PC — mais Criminologia
# =====================================================================
mc("PC","Criminologia","Assinale a alternativa que descreve corretamente a teoria da associação diferencial, no âmbito da criminologia.",
   ["Defende que o comportamento criminoso é exclusivamente hereditário.","Sustenta que o comportamento criminoso é aprendido por meio da interação social com outras pessoas, incluindo técnicas, motivações e justificativas para o crime.","Nega qualquer influência do ambiente social sobre o comportamento criminoso.","É sinônimo da Escola Clássica de Criminologia.","Defende que apenas fatores biológicos explicam o crime."],
   1,"A teoria da associação diferencial, formulada por Edwin Sutherland, sustenta que o comportamento criminoso é aprendido por meio da interação social, incluindo técnicas, motivações, racionalizações e atitudes favoráveis à prática de crimes.")
mc("PC","Criminologia","Sobre a vitimologia, ramo da criminologia voltado ao estudo da vítima, é correto afirmar que ela analisa, entre outros aspectos:",
   ["Apenas o perfil psicológico do autor do crime.","A relação entre vítima e autor, o papel da vítima na dinâmica criminal e as consequências da vitimização.","Exclusivamente questões de direito processual civil.","Somente crimes patrimoniais.","Apenas a reincidência criminal do autor."],
   1,"A vitimologia estuda a vítima do delito, analisando sua relação com o autor, seu eventual papel na dinâmica criminal e as consequências (físicas, psicológicas e sociais) decorrentes da vitimização.")
mc("PC","Criminologia","Assinale a alternativa que descreve corretamente o conceito de prevenção criminal terciária.",
   ["Atua antes da ocorrência do delito, sobre a população em geral.","Atua sobre grupos identificados como de maior risco de envolvimento em atividades criminosas.","Atua após a ocorrência do delito, voltada à reintegração social do autor e à prevenção da reincidência.","Refere-se exclusivamente a medidas de segurança pública ostensiva.","É sinônimo de prevenção primária."],
   2,"A prevenção terciária atua após a ocorrência do delito, voltada especialmente à reintegração social do autor do crime e à prevenção de novos episódios de reincidência criminal."),

# =====================================================================
# PC — mais Legislacao Especial
# =====================================================================
mc("PC","Legislação Especial","Segundo a Lei de Drogas (Lei nº 11.343/2006), a diferenciação entre usuário e traficante de drogas leva em consideração, entre outros critérios, previstos em lei:",
   ["Apenas a quantidade de droga apreendida, isoladamente.","A natureza e a quantidade da substância apreendida, o local e as condições em que se desenvolveu a ação, as circunstâncias sociais e pessoais, bem como a conduta e os antecedentes do agente.","Exclusivamente a confissão do agente.","Somente o valor de mercado da substância apreendida.","Apenas a existência de antecedentes criminais do agente, isoladamente."],
   1,"Conforme art. 28, §2º, da Lei nº 11.343/2006, para a diferenciação entre usuário e traficante, o juiz deve considerar a natureza e a quantidade da substância, o local e as condições da ação, as circunstâncias sociais e pessoais, bem como a conduta e os antecedentes do agente.")
mc("PC","Legislação Especial","Assinale a alternativa correta a respeito da Lei de Organização Criminosa (Lei nº 12.850/2013).",
   ["Não prevê qualquer definição legal de organização criminosa.","Define organização criminosa como a associação de quatro ou mais pessoas, estruturalmente ordenada e caracterizada pela divisão de tarefas, para a obtenção de vantagem por meio da prática de infrações penais com penas superiores a quatro anos ou de caráter transnacional.","Aplica-se exclusivamente a crimes de menor potencial ofensivo.","Exige, obrigatoriamente, mais de cem integrantes para sua configuração.","Foi revogada integralmente pelo Código Penal em 2015."],
   1,"A Lei nº 12.850/2013 define organização criminosa como a associação de quatro ou mais pessoas estruturalmente ordenada e caracterizada pela divisão de tarefas, ainda que informalmente, com objetivo de obter vantagem por meio da prática de infrações penais cujas penas máximas sejam superiores a quatro anos, ou que sejam de caráter transnacional.")
mc("PC","Legislação Especial","Segundo o Estatuto do Desarmamento (Lei nº 10.826/2003), o porte de arma de fogo, em regra, no território nacional:",
   ["É livre a qualquer cidadão, independentemente de autorização.","Depende de autorização do órgão competente, sendo vedado, em regra, sem essa autorização.","Aplica-se apenas a armas de uso restrito das Forças Armadas.","Independe de qualquer registro da arma de fogo.","Não é regulamentado por lei federal."],
   1,"O Estatuto do Desarmamento estabelece que o porte de arma de fogo depende, em regra, de autorização de órgão competente, sendo vedado o porte irregular, sem a devida autorização legal.")
mc("PC","Legislação Especial","Sobre a Lei Maria da Penha, é correto afirmar que a medida protetiva de urgência, prevista nessa lei, pode ser deferida:",
   ["Somente após o trânsito em julgado de ação penal.","Pelo juiz, inclusive de forma imediata, para proteger a mulher em situação de violência doméstica e familiar, independentemente do resultado final do processo criminal.","Exclusivamente pelo delegado de polícia, sem qualquer participação judicial.","Apenas em casos de violência patrimonial.","Somente mediante requerimento do agressor."],
   1,"A Lei Maria da Penha prevê que medidas protetivas de urgência podem ser deferidas pelo juiz, inclusive de forma célere, para proteger a mulher em situação de violência doméstica e familiar, independentemente do desfecho final do eventual processo criminal.")

with open("/home/claude/qbank/questions.json","w",encoding="utf-8") as f:
    json.dump(BANK, f, ensure_ascii=False, indent=None)

print("total:", len(BANK))
from collections import Counter
c = Counter(q["corp"] for q in BANK)
print(c)
