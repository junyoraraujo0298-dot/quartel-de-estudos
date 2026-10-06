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

# PM — Legislação Institucional (mais)
ce("PM","Legislação Institucional PM","O militar estadual, ao ingressar na corporação, assume deveres éticos e funcionais que orientam sua conduta, tanto na vida profissional quanto, em certa medida, na vida particular, dada a natureza da função.",True,"Correto. Os estatutos militares costumam prever deveres éticos que extrapolam o mero ambiente de trabalho, refletindo a natureza especial da função policial-militar, inclusive quanto à conduta na vida particular, na medida em que afete o decoro da classe.")
ce("PM","Legislação Institucional PM","A Polícia Militar do Maranhão, assim como as demais polícias militares estaduais, subordina-se administrativamente ao Governador do Estado, conforme previsto na Constituição Federal.",True,"Correto, conforme art. 144, §6º, da CF: as polícias militares e corpos de bombeiros militares subordinam-se, juntamente com as polícias civis, aos Governadores dos Estados, do Distrito Federal e dos Territórios.")
ce("PM","Legislação Institucional PM","O regulamento disciplinar de uma corporação militar estadual tem por finalidade estabelecer as transgressões disciplinares e as respectivas sanções, distintas do regime de crimes militares.",True,"Correto. O regulamento disciplinar disciplina as transgressões (infrações de natureza administrativa) e as sanções correspondentes, em contraposição ao regime de crimes militares, apurado pela Justiça Militar.")
ce("PM","Legislação Institucional PM","A sindicância e o processo administrativo disciplinar são exemplos de procedimentos utilizados para apuração de transgressões disciplinares no âmbito militar, assegurados o contraditório e a ampla defesa.",True,"Correto. Tanto a sindicância quanto o processo administrativo disciplinar (PAD) são instrumentos de apuração de transgressões no âmbito da corporação, devendo respeitar o contraditório e a ampla defesa.")
ce("PM","Legislação Institucional PM","O militar estadual em atividade não pode filiar-se a partido político, sendo essa vedação uma decorrência da necessidade de preservar a neutralidade política das corporações militares.",True,"Correto. De modo geral, os estatutos militares vedam a filiação partidária do militar da ativa, em consonância com o princípio da subordinação das Forças Militares aos poderes constituídos, de forma apartidária.")
ce("PM","Legislação Institucional PM","O militar estadual, mesmo na condição de policial, não possui o dever de resguardar o sigilo de informações obtidas em razão do exercício da função, podendo divulgá-las livremente.",False,"Errado. O militar, no exercício da função policial, possui o dever de resguardar o sigilo de informações obtidas em razão do serviço, sob pena de responsabilização disciplinar e, conforme o caso, penal.")
ce("PM","Legislação Institucional PM","O uso do uniforme e das insígnias da corporação por pessoa não autorizada pode configurar ilícito, tendo em vista a proteção da identidade visual e da autoridade representada pela farda militar.",True,"Correto. O uso indevido de uniforme, distintivos ou insígnias de corporação militar por pessoa não autorizada é, em regra, vedado e pode configurar ilícito administrativo ou penal, conforme a legislação aplicável.")
ce("PM","Legislação Institucional PM","O militar estadual que se afasta do serviço sem autorização por período superior ao estabelecido em lei pode incorrer no crime militar de deserção.",True,"Correto. A deserção é crime militar próprio, caracterizado pelo afastamento não autorizado do militar de suas funções por prazo superior ao estabelecido na legislação penal militar.")
ce("PM","Legislação Institucional PM","O princípio da disciplina militar não admite qualquer flexibilização, mesmo diante de ordens manifestamente ilegais.",False,"Errado. A disciplina militar não se confunde com obediência cega: o subordinado não deve cumprir ordens manifestamente ilegais, respondendo, nesse caso, apenas o superior que as expediu.")
ce("PM","Legislação Institucional PM","Compete às polícias militares estaduais, no âmbito de suas atribuições constitucionais, o policiamento de trânsito nas vias urbanas, quando previsto em lei estadual ou convênio específico.",True,"Correto. Embora o trânsito seja, em regra, atribuição de órgãos específicos, é comum que a legislação estadual ou convênios atribuam às polícias militares o policiamento de trânsito, sobretudo em municípios sem órgão próprio estruturado.")

# PM — Geografia do Brasil (mais)
ce("PM","Geografia do Brasil","O bioma Cerrado, o segundo maior bioma brasileiro em extensão, caracteriza-se por vegetação predominantemente arbustiva e herbácea, com árvores de troncos tortuosos e casca grossa.",True,"Correto. O Cerrado é o segundo maior bioma do Brasil, com vegetação típica de savana tropical, marcada por árvores de troncos tortuosos, casca grossa e vegetação rasteira predominante.")
ce("PM","Geografia do Brasil","A Mata Atlântica, bioma que se estende por parte considerável do litoral brasileiro, encontra-se, atualmente, com a maior parte de sua cobertura original preservada e intacta.",False,"Errado. A Mata Atlântica é um dos biomas brasileiros mais devastados, restando atualmente apenas uma pequena fração de sua cobertura vegetal original, em razão da intensa ocupação humana ao longo de sua área de distribuição.")
ce("PM","Geografia do Brasil","O regime de chuvas no Brasil apresenta grande variação regional, sendo o semiárido nordestino uma das áreas de menor índice pluviométrico do país.",True,"Correto. O semiárido nordestino caracteriza-se por baixos índices pluviométricos e irregularidade nas chuvas, sendo uma das regiões mais secas do território brasileiro.")
ce("PM","Geografia do Brasil","O relevo brasileiro é classificado, segundo modelos geomorfológicos clássicos, principalmente em planaltos, planícies e depressões, havendo predominância de áreas de planalto no território nacional.",True,"Correto. O território brasileiro é formado majoritariamente por planaltos, seguidos por planícies e depressões, com predominância de altitudes moderadas.")
ce("PM","Geografia do Brasil","A hidrografia brasileira é caracterizada pela existência de grandes bacias hidrográficas, sendo a Bacia do Prata uma das mais importantes, ao lado da Bacia Amazônica e da Bacia do São Francisco.",True,"Correto. Além da Bacia Amazônica, o Brasil possui outras bacias relevantes, como a do Prata (que inclui o rio Paraná) e a do São Francisco, fundamentais para diferentes regiões do país.")
ce("PM","Geografia do Brasil","O fenômeno do êxodo rural no Brasil, ocorrido principalmente a partir de meados do século XX, contribuiu para o aumento da população nas cidades e para o crescimento das periferias urbanas.",True,"Correto. O êxodo rural, impulsionado pela industrialização e pela mecanização do campo, contribuiu significativamente para o crescimento das cidades brasileiras e, muitas vezes, para a expansão desordenada de suas periferias.")
ce("PM","Geografia do Brasil","O Brasil, por sua extensão territorial, está localizado integralmente dentro da zona climática temperada, não havendo qualquer área de clima tropical ou equatorial em seu território.",False,"Errado. A maior parte do território brasileiro está situada na zona intertropical, com predominância de climas tropicais e equatorial, havendo apenas pequena porção do Sul do país sob influência de clima subtropical.")
ce("PM","Geografia do Brasil","A industrialização brasileira, historicamente concentrada na região Sudeste, contribuiu para consolidar essa região como o principal polo econômico do país.",True,"Correto. A industrialização brasileira concentrou-se, sobretudo, na região Sudeste, especialmente em São Paulo e Rio de Janeiro, consolidando-a como o principal polo econômico e populacional do país.")

# PM — Historia do Brasil (mais)
ce("PM","História do Brasil","O Brasil Colônia foi marcado pela predominância de uma economia agroexportadora, voltada para a produção de gêneros destinados ao mercado europeu, como o açúcar e, posteriormente, o ouro.",True,"Correto. A economia colonial brasileira caracterizou-se pela produção agroexportadora, com destaque inicial para o açúcar e, a partir do século XVIII, para a exploração do ouro nas Minas Gerais.")
ce("PM","História do Brasil","A abolição da escravidão no Brasil, em 1888, ocorreu de forma simultânea e imediata à concessão do direito de voto universal a todos os ex-escravizados.",False,"Errado. A abolição da escravidão em 1888 não veio acompanhada de medidas de inclusão social, política ou econômica dos ex-escravizados, que permaneceram, em grande parte, à margem da sociedade e sem acesso imediato a direitos políticos plenos.")
ce("PM","História do Brasil","O golpe militar de 1964 foi justificado, pelos seus articuladores, sob o argumento de combate a uma suposta ameaça comunista ao país.",True,"Correto. Os articuladores do golpe de 1964 alegaram a necessidade de conter uma suposta ameaça comunista, associada ao governo de João Goulart, como justificativa para a deposição do presidente.")
ce("PM","História do Brasil","A Constituição de 1988 restabeleceu a eleição direta para presidente da República já em seu texto original, tendo sido a primeira eleição direta realizada logo após a promulgação da Constituição, em 1988.",False,"Errado. Embora a Constituição de 1988 tenha restabelecido a eleição direta para presidente, a primeira eleição direta após o regime militar ocorreu apenas em 1989, e não no ano da promulgação da Constituição.")
ce("PM","História do Brasil","O processo de industrialização brasileira intensificou-se, sobretudo, a partir da década de 1930, associado às políticas desenvolvimentistas adotadas por Getúlio Vargas.",True,"Correto. A partir da Era Vargas, o Brasil intensificou seu processo de industrialização, com políticas voltadas ao desenvolvimento de indústrias de base e à substituição de importações.")
ce("PM","História do Brasil","A ditadura militar brasileira (1964-1985) foi marcada, entre outros aspectos, pela criação de órgãos de repressão política e pela censura aos meios de comunicação.",True,"Correto. O período do regime militar caracterizou-se pela criação de órgãos de repressão política e pela censura à imprensa, sobretudo após a edição do AI-5, em 1968.")
ce("PM","História do Brasil","A redemocratização brasileira culminou com a promulgação de uma nova Constituição Federal em 1988, marco jurídico do retorno ao Estado Democrático de Direito.",True,"Correto. A Constituição de 1988, elaborada por uma Assembleia Nacional Constituinte, é considerada o marco jurídico da redemocratização brasileira e da consolidação do Estado Democrático de Direito.")

# PM — Portugues (mais)
ce("PM","Língua Portuguesa","O uso do plural 'menas' é aceito pela norma-padrão como variação livre da palavra invariável 'menos'.",False,"Errado. 'Menos' é palavra invariável em português; a forma 'menas' não é aceita pela norma-padrão, sendo considerada desvio próprio da linguagem coloquial ou regional.")
ce("PM","Língua Portuguesa","O verbo 'obedecer' é transitivo indireto, regendo-se com a preposição 'a': 'obedecer às ordens do superior'.",True,"Correto. 'Obedecer' é transitivo indireto na norma-padrão, exigindo a preposição 'a': obedecer a alguém ou a algo.")
ce("PM","Língua Portuguesa","Na frase 'Assisti ao filme sobre a corporação', o verbo 'assistir' está corretamente empregado com a preposição 'a', no sentido de 'presenciar' ou 'ver'.",True,"Correto. 'Assistir' no sentido de ver/presenciar é transitivo indireto, regendo-se corretamente com a preposição 'a'.")
ce("PM","Língua Portuguesa","O emprego do hífen na palavra 'auto-escola' está de acordo com o Acordo Ortográfico atualmente vigente.",False,"Errado. Pelo Acordo Ortográfico vigente, a forma correta é 'autoescola', sem hífen, uma vez que o prefixo 'auto' seguido de vogal diferente não exige hífen.")
ce("PM","Língua Portuguesa","Em 'Precisamos de mais policiais para o policiamento ostensivo', o verbo 'precisar', no sentido de necessitar, é transitivo indireto, regendo-se com a preposição 'de'.",True,"Correto. 'Precisar', no sentido de necessitar, é transitivo indireto e exige a preposição 'de': precisar de algo ou de alguém.")
ce("PM","Língua Portuguesa","A palavra 'porque' deve ser sempre grafada separadamente e sem acento, independentemente do contexto sintático em que for empregada.",False,"Errado. A grafia de 'porque/por que/porquê/por quê' varia conforme a função sintática: 'porque' (junto, sem acento) é usado, tipicamente, como conjunção explicativa ou causal; as demais formas têm empregos distintos.")
ce("PM","Língua Portuguesa","Em 'Trata-se de questões relevantes para a corporação', o pronome 'se' integra uma construção de sentido genérico, comum em textos de caráter técnico ou formal.",True,"Correto. A construção 'trata-se de' é comumente empregada em textos técnicos e formais para introduzir um tema, sendo o 'se' parte integrante dessa construção verbal.")
ce("PM","Língua Portuguesa","O uso da conjunção 'mas' dispensa, em qualquer hipótese, o emprego de vírgula antes dela, por se tratar de conectivo de valor aditivo.",False,"Errado. 'Mas' é conjunção adversativa (não aditiva) e deve, como regra, ser antecedida de vírgula, por introduzir uma ideia de contraste em relação à oração anterior.")
ce("PM","Língua Portuguesa","Na frase 'Ele próprio resolveu o problema', a palavra 'próprio' funciona como reforço do sujeito, concordando em gênero e número com ele.",True,"Correto. 'Próprio' (e também 'mesmo'), quando usado como reforço, concorda em gênero e número com o termo a que se refere: 'ele próprio', 'ela própria'.")
ce("PM","Língua Portuguesa","O pronome relativo 'onde' deve ser empregado exclusivamente para retomar lugares físicos, sendo inadequado seu uso para retomar ideias abstratas.",True,"Correto. A norma-padrão recomenda o uso de 'onde' apenas para retomar lugar físico; para ideias abstratas, recomenda-se o uso de 'em que' ou 'no qual', entre outras formas.")

# BM — Portugues (mais)
mc("BM","Língua Portuguesa","Assinale a alternativa em que a regência do verbo 'obedecer' está de acordo com a norma-padrão.",
   ["Obedecemos o comandante.","Obedecemos ao comandante.","Obedecemos com o comandante.","Obedecemos para o comandante.","Obedecemos de o comandante."],
   1,"'Obedecer' é transitivo indireto, regendo-se com a preposição 'a': 'Obedecemos ao comandante' está correto.")
mc("BM","Língua Portuguesa","Assinale a alternativa que apresenta a grafia correta, segundo o Acordo Ortográfico vigente.",
   ["Autoescola","Auto-escola","Autoesscola","Auto escola","Auto-Escola"],
   0,"A forma correta, sem hífen, é 'autoescola', conforme as regras do Acordo Ortográfico vigente para prefixos como 'auto' seguidos de vogal diferente.")
mc("BM","Língua Portuguesa","Assinale a alternativa correta quanto ao uso do porquê nas suas diferentes formas.",
   ["Não sei por que ele faltou.","Não sei por quê ele faltou.","Não sei porque ele faltou, sem qualquer regra.","Não sei o por que ele faltou.","Não sei o porquê, disso, sem contexto."],
   0,"'Por que' (separado, sem acento) é usado em perguntas diretas ou indiretas, equivalendo a 'por qual razão': 'Não sei por que ele faltou' está correto.")
mc("BM","Língua Portuguesa","Assinale a alternativa que respeita a concordância nominal na frase.",
   ["Segue anexos o relatório e a planilha.","Seguem anexo o relatório e a planilha.","Seguem anexos o relatório e a planilha.","Segue anexo os relatório e planilha.","Anexos, segue o relatório e planilha, sem concordância."],
   2,"'Seguem anexos o relatório e a planilha' está correto: o verbo concorda com o sujeito composto no plural, e 'anexos' concorda em número com os substantivos a que se refere.")
mc("BM","Língua Portuguesa","Assinale a alternativa em que o pronome relativo está empregado corretamente.",
   ["A cidade onde ele nasceu fica no Maranhão.","A ideia onde ele defendeu foi debatida.","O motivo onde ele faltou não foi esclarecido.","A situação onde ele descreveu era grave.","O projeto onde ele apresentou foi aprovado."],
   0,"'Onde' deve ser usado para retomar lugar físico: 'A cidade onde ele nasceu' está correto; nas demais alternativas, o pronome retoma ideias abstratas, o que é inadequado, cabendo o uso de 'em que' ou 'no qual'."),

# BM — Historia do Maranhao (mais)
mc("BM","História do Maranhão","O ciclo econômico do algodão no Maranhão colonial teve como um dos fatores impulsionadores:",
   ["A descoberta de ouro nas proximidades de São Luís.","A atuação da Companhia de Comércio do Grão-Pará e Maranhão, no século XVIII.","A chegada da Família Real portuguesa a São Luís, em 1808.","A construção da Estrada de Ferro Carajás.","A instalação de indústrias têxteis inglesas na região."],
   1,"A Companhia de Comércio do Grão-Pará e Maranhão, criada no século XVIII, teve papel relevante no fomento à produção e exportação de algodão, impulsionando a economia da região."),
mc("BM","História do Maranhão","Assinale a alternativa correta sobre a adesão do Maranhão ao processo de independência do Brasil.",
   ["Ocorreu de forma imediata e sem qualquer resistência, em 1822.","Não ocorreu de forma imediata, havendo resistência de setores ligados a Portugal antes da efetiva adesão da província, em 1823.","Nunca chegou a se efetivar, permanecendo o Maranhão sob domínio português até o fim do Império.","Foi liderada exclusivamente por tropas espanholas.","Ocorreu antes mesmo da Proclamação da Independência do Brasil."],
   1,"A adesão maranhense à independência somente se consolidou em 1823, após enfrentamentos com setores de resistência portuguesa em São Luís."),

# BM — Geografia do Maranhao (mais)
mc("BM","Geografia do Maranhão","Assinale a alternativa que descreve corretamente a localização do Maranhão no território brasileiro.",
   ["Região Sul do Brasil, na fronteira com o Uruguai.","Região Nordeste do Brasil, também integrando a Amazônia Legal.","Região Centro-Oeste do Brasil, na fronteira com a Bolívia.","Região Sudeste do Brasil, no litoral do Rio de Janeiro.","Região Norte do Brasil, exclusivamente, sem qualquer vínculo com o Nordeste."],
   1,"O Maranhão integra oficialmente a região Nordeste do Brasil, mas também faz parte da Amazônia Legal, sendo frequentemente descrito como estado de transição entre essas duas grandes regiões."),
mc("BM","Geografia do Maranhão","Em relação aos principais rios que cortam o Maranhão, assinale a alternativa correta.",
   ["Tietê, Piracicaba e Grande.","Itapecuru, Mearim, Pindaré e Grajaú.","Tocantins, Xingu e Tapajós, exclusivamente.","São Francisco e Paraná, apenas.","Uruguai e Iguaçu, apenas."],
   1,"Itapecuru, Mearim, Pindaré e Grajaú estão entre os principais rios do território maranhense, relevantes para o abastecimento e a economia regional."),

# BM — Ingles (mais)
mc("BM","Língua Estrangeira (Inglês)","Assinale a alternativa que apresenta o correto significado da expressão 'call for help'.",
   ["Pedir ajuda","Ligar para casa","Chamar a atenção","Fazer uma denúncia anônima","Cancelar o chamado"],
   0,"'Call for help' significa 'pedir ajuda', expressão comum em contextos de emergência."),
mc("BM","Língua Estrangeira (Inglês)","Choose the correct sentence using the present continuous tense.",
   ["The firefighters is fighting the fire now.","The firefighters are fighting the fire now.","The firefighters fights the fire now.","The firefighters fighting the fire now.","The firefighters was fighting the fire now."],
   1,"A forma correta no presente contínuo, com sujeito no plural, é 'are fighting': 'The firefighters are fighting the fire now.'"),

# BM — Legislacao Institucional (mais)
mc("BM","Legislação Institucional","Assinale a alternativa correta sobre o requisito de idade para ingresso no cargo de Praça Combatente Bombeiro Militar, segundo os parâmetros usualmente exigidos em editais desse tipo de concurso.",
   ["Apenas candidatos com até 21 anos podem concorrer.","Em regra, exige-se idade mínima de 18 anos e idade máxima em torno de 35 anos, na data de referência estabelecida em edital.","Não há qualquer limite de idade para o cargo.","Somente candidatos com mais de 40 anos podem concorrer.","A idade mínima exigida é de 25 anos completos."],
   1,"Editais desse tipo de concurso para ingresso em corporações militares estaduais costumam exigir idade mínima de 18 anos e idade máxima em torno de 35 anos, na data de referência prevista no próprio edital."),
mc("BM","Legislação Institucional","No que se refere às atribuições do Corpo de Bombeiros Militar, além do combate a incêndios, compete-lhe também, de modo geral:",
   ["Atividades exclusivamente de policiamento ostensivo urbano.","Ações de defesa civil, busca e salvamento, e atendimento pré-hospitalar em situações de emergência.","Investigação de infrações penais comuns.","Fiscalização tributária estadual.","Expedição de carteira de identidade civil."],
   1,"Além do combate a incêndios, os corpos de bombeiros militares atuam, de modo geral, em ações de defesa civil, busca e salvamento, e atendimento pré-hospitalar em situações de emergência."),

# PC — Direito Constitucional (mais)
mc("PC","Direito Constitucional","Assinale a alternativa correta acerca do controle de constitucionalidade no ordenamento jurídico brasileiro.",
   ["Somente pode ser exercido pelo Supremo Tribunal Federal, de forma concentrada.","Pode ser exercido de forma difusa, por qualquer juiz ou tribunal, e de forma concentrada, perante o Supremo Tribunal Federal, nas hipóteses previstas na Constituição.","É vedado a qualquer órgão do Poder Judiciário brasileiro.","Aplica-se exclusivamente a leis municipais.","Depende sempre de manifestação prévia do Poder Legislativo."],
   1,"O Brasil adota um sistema misto de controle de constitucionalidade, admitindo tanto o controle difuso (exercido por qualquer juiz ou tribunal, incidentalmente) quanto o controle concentrado (perante o STF, nas hipóteses constitucionais específicas).")
mc("PC","Direito Constitucional","Sobre os direitos sociais previstos na Constituição Federal, é correto afirmar que incluem, entre outros:",
   ["Apenas o direito de propriedade.","Educação, saúde, alimentação, trabalho, moradia, transporte, lazer, segurança e previdência social, conforme o art. 6º da CF.","Exclusivamente o direito à livre iniciativa.","Somente direitos de natureza eleitoral.","Apenas o direito à liberdade de expressão."],
   1,"O art. 6º da CF elenca, entre os direitos sociais, a educação, a saúde, a alimentação, o trabalho, a moradia, o transporte, o lazer, a segurança, a previdência social, a proteção à maternidade e à infância e a assistência aos desamparados.")
mc("PC","Direito Constitucional","Em relação à competência dos entes federativos para legislar sobre segurança pública, é correto afirmar que:",
   ["É matéria de competência exclusiva dos Municípios.","A União possui competência para legislar sobre normas gerais de organização, efetivos, material bélico, garantias e convocação das polícias militares e corpos de bombeiros militares.","Os Estados não possuem qualquer competência sobre a matéria.","É matéria de competência exclusiva do Distrito Federal.","Não há previsão constitucional sobre essa competência."],
   1,"Conforme art. 22, XXI, da CF, compete privativamente à União legislar sobre normas gerais de organização, efetivos, material bélico, garantias, convocação e mobilização das polícias militares e corpos de bombeiros militares.")
mc("PC","Direito Constitucional","Assinale a alternativa correta a respeito das cláusulas pétreas previstas na Constituição Federal.",
   ["Podem ser livremente abolidas por emenda constitucional aprovada por maioria simples.","Não podem ser objeto de deliberação de proposta de emenda tendente a aboli-las, conforme o art. 60, §4º, da CF.","Aplicam-se apenas às normas de direito tributário.","Foram todas revogadas pela Emenda Constitucional nº 45.","Referem-se exclusivamente à forma republicana de governo."],
   1,"Conforme art. 60, §4º, da CF, não será objeto de deliberação a proposta de emenda tendente a abolir a forma federativa de Estado, o voto direto, secreto, universal e periódico, a separação dos Poderes, e os direitos e garantias individuais."),

# PC — Direito Administrativo (mais)
mc("PC","Direito Administrativo","Assinale a alternativa correta acerca das formas de provimento de cargos públicos.",
   ["A nomeação é a única forma de provimento prevista em lei.","A nomeação, a promoção, a readaptação e a reintegração são exemplos de formas de provimento de cargos públicos.","O provimento de cargos públicos independe de concurso público, em qualquer hipótese.","A exoneração é uma forma de provimento de cargo público.","Todo provimento de cargo público exige aprovação prévia do Poder Legislativo."],
   1,"São exemplos de formas de provimento de cargo público a nomeação, a promoção, a readaptação e a reintegração, entre outras previstas na legislação estatutária de cada ente federativo.")
mc("PC","Direito Administrativo","Em relação à licitação, é correto afirmar que ela tem por finalidade principal:",
   ["Beneficiar diretamente um fornecedor previamente escolhido pelo administrador.","Selecionar a proposta mais vantajosa para a Administração, garantindo isonomia entre os licitantes.","Dispensar, em qualquer hipótese, a observância de princípios como legalidade e impessoalidade.","Eliminar totalmente a necessidade de fiscalização dos contratos administrativos.","Aplicar-se exclusivamente a contratos de valor elevado, sem qualquer outro critério."],
   1,"A licitação tem por finalidade selecionar a proposta mais vantajosa para a Administração Pública, assegurando a isonomia entre os licitantes e a observância dos princípios que regem a atividade administrativa.")
mc("PC","Direito Administrativo","Assinale a alternativa que apresenta corretamente uma das modalidades de intervenção do Estado na propriedade privada.",
   ["Anulação","Revogação","Desapropriação","Convalidação","Ratificação"],
   2,"A desapropriação é uma das formas de intervenção do Estado na propriedade privada, mediante indenização, em regra, prévia, justa e em dinheiro, nos casos de necessidade ou utilidade pública, ou interesse social."),
mc("PC","Direito Administrativo","Sobre a prescrição da pretensão punitiva da Administração em processos administrativos disciplinares, é correto afirmar que:",
   ["Não existe prazo prescricional para a Administração apurar infrações disciplinares.","A legislação costuma prever prazos prescricionais, variáveis conforme a gravidade da infração, para a apuração e punição administrativa.","O prazo prescricional é sempre de cem anos, independentemente da infração.","A prescrição administrativa é idêntica, em todos os casos, à prescrição penal.","Não há qualquer relação entre prescrição e o poder disciplinar da Administração."],
   1,"A legislação estatutária costuma prever prazos prescricionais distintos para a apuração e punição administrativa, a depender da gravidade da infração, de modo a assegurar segurança jurídica ao servidor."),

# PC — Direito Penal (mais)
mc("PC","Direito Penal","Assinale a alternativa correta acerca do conceito de crime, sob o aspecto formal e material.",
   ["Crime é toda conduta considerada imoral pela sociedade, independentemente de previsão legal.","Sob o aspecto formal, crime é a conduta prevista em lei como infração penal, sujeita a pena; sob o aspecto material, é a conduta que lesiona ou expõe a perigo bem jurídico penalmente tutelado.","Crime é sinônimo de contravenção penal em qualquer hipótese.","O conceito de crime independe de previsão legal.","Toda conduta ilícita configura, necessariamente, crime."],
   1,"Sob o aspecto formal, crime é a conduta prevista em lei como infração penal sujeita a pena; sob o aspecto material, é a conduta que lesiona ou expõe a perigo de lesão um bem jurídico penalmente relevante.")
mc("PC","Direito Penal","Sobre as espécies de pena previstas no Código Penal, assinale a alternativa correta.",
   ["Apenas a pena privativa de liberdade é prevista no Código Penal.","O Código Penal prevê penas privativas de liberdade, restritivas de direitos e de multa.","A pena de multa foi extinta do ordenamento jurídico brasileiro.","As penas restritivas de direitos são sempre cumuladas com a pena privativa de liberdade, nunca a substituindo.","Não há qualquer previsão de substituição da pena privativa de liberdade por restritiva de direitos."],
   1,"O Código Penal prevê, como espécies de pena, a privativa de liberdade, a restritiva de direitos e a de multa, podendo, em determinadas hipóteses, a pena privativa de liberdade ser substituída pela restritiva de direitos.")
mc("PC","Direito Penal","Em relação à reincidência, prevista no Código Penal, é correto afirmar que ela se configura quando:",
   ["O agente comete o primeiro crime de sua vida.","O agente comete novo crime depois de transitar em julgado sentença que o tenha condenado por crime anterior, no Brasil ou no exterior.","O agente é apenas investigado por um segundo crime, sem condenação.","A reincidência é sempre presumida, independentemente de condenação anterior.","Refere-se apenas à reiteração de contravenções penais."],
   1,"Conforme art. 63 do CP, a reincidência configura-se quando o agente comete novo crime depois de transitar em julgado sentença que, no Brasil ou no exterior, o tenha condenado por crime anterior."),
mc("PC","Direito Penal","Sobre a diferença entre imputabilidade e inimputabilidade penal, é correto afirmar que:",
   ["Todo agente imputável está isento de pena.","O inimputável, em regra, não é penalmente responsável, podendo, contudo, sujeitar-se à aplicação de medida de segurança.","A inimputabilidade é sinônimo de ausência de conduta.","Menores de 18 anos são considerados imputáveis para fins penais, sujeitando-se ao Código Penal comum.","Não há qualquer consequência jurídica para o agente inimputável que pratica fato típico e ilícito."],
   1,"O agente inimputável, em regra, não é penalmente responsável (isento de pena), podendo, contudo, sujeitar-se à aplicação de medida de segurança, conforme previsto no Código Penal."),

# PC — Direito Processual Penal (mais)
mc("PC","Direito Processual Penal","Assinale a alternativa correta acerca da competência para julgamento dos crimes dolosos contra a vida no Brasil.",
   ["Compete ao juiz singular, sem qualquer participação popular.","Compete, em regra, ao Tribunal do Júri, conforme previsão constitucional.","Compete exclusivamente ao Supremo Tribunal Federal.","Compete ao delegado de polícia, com força de decisão final.","Compete ao Ministério Público, sem qualquer participação do Poder Judiciário."],
   1,"Conforme art. 5º, XXXVIII, 'd', da CF, compete, em regra, ao Tribunal do Júri o julgamento dos crimes dolosos contra a vida.")
mc("PC","Direito Processual Penal","Sobre o princípio do juiz natural, previsto implicitamente na Constituição Federal, é correto afirmar que ele veda:",
   ["A existência de tribunais ou juízos de exceção.","A existência de qualquer especialização de varas ou tribunais.","A distribuição de processos por sorteio entre os juízos competentes.","A existência do Tribunal do Júri.","A criação de varas especializadas em crimes financeiros."],
   0,"O princípio do juiz natural veda a instituição de tribunais ou juízos de exceção, assegurando que o processo seja julgado por autoridade competente, previamente estabelecida, e não designada posteriormente ao fato.")
mc("PC","Direito Processual Penal","Em relação à busca e apreensão domiciliar, prevista constitucionalmente, é correto afirmar que, em regra, ela depende de:",
   ["Autorização verbal de qualquer autoridade policial, sem necessidade de mandado.","Determinação judicial, ressalvadas as hipóteses constitucionais de flagrante delito, desastre, prestação de socorro, ou, durante o dia, mediante consentimento do morador.","Consentimento exclusivamente do proprietário do imóvel, ainda que este não seja o morador.","Autorização do Ministério Público, dispensada qualquer participação judicial.","Prévia notificação por edital ao morador, com trinta dias de antecedência."],
   1,"Conforme art. 5º, XI, da CF, a casa é asilo inviolável, sendo a entrada sem consentimento do morador possível apenas em caso de flagrante delito, desastre, para prestar socorro, ou, durante o dia, por determinação judicial."),

# PC — Direitos Humanos (mais)
mc("PC","Direitos Humanos","Assinale a alternativa correta sobre a proteção internacional dos direitos humanos e sua relação com a soberania estatal.",
   ["A proteção internacional dos direitos humanos elimina completamente a soberania dos Estados.","A proteção internacional dos direitos humanos convive com a soberania estatal, estabelecendo padrões mínimos de respeito a esses direitos que os Estados se comprometem a observar.","Não existe qualquer sistema internacional de proteção aos direitos humanos.","A soberania estatal impede qualquer responsabilização internacional por violações de direitos humanos.","Apenas tratados aprovados por todos os países do mundo têm validade em matéria de direitos humanos."],
   1,"A proteção internacional dos direitos humanos convive com a soberania dos Estados, estabelecendo padrões mínimos que os países signatários de tratados se comprometem a respeitar, sujeitando-se, em certas hipóteses, a mecanismos de responsabilização internacional."),
mc("PC","Direitos Humanos","No âmbito da atuação policial, o respeito aos direitos humanos das pessoas sob custódia estatal implica, entre outros deveres, o de:",
   ["Utilizar qualquer meio para obtenção de confissão, inclusive violência.","Assegurar condições dignas de custódia, integridade física e psicológica, e acesso à assistência jurídica.","Restringir, sem qualquer critério legal, o direito de comunicação da pessoa presa com seus familiares.","Dispensar qualquer registro formal da prisão efetuada.","Presumir automaticamente a culpa da pessoa sob custódia."],
   1,"O respeito aos direitos humanos das pessoas sob custódia estatal implica assegurar condições dignas de custódia, a integridade física e psicológica do preso, e o acesso à assistência jurídica, entre outras garantias."),

# PC — Medicina Legal (mais)
mc("PC","Medicina Legal","Assinale a alternativa que descreve corretamente o conceito de 'livor cadavérico' (livores de hipóstase).",
   ["Enrijecimento da musculatura corporal após a morte.","Manchas arroxeadas que surgem no corpo devido ao acúmulo de sangue nas partes mais baixas, por ação da gravidade, após a cessação da circulação.","Processo de decomposição avançada do corpo.","Fenômeno exclusivo de mortes por afogamento.","Sinal de vida presente em vítimas ainda socorrível."],
   1,"Os livores cadavéricos (de hipóstase) são manchas arroxeadas que surgem devido ao acúmulo de sangue nas regiões mais baixas do corpo, por ação da gravidade, após a cessação da circulação sanguínea decorrente da morte."),
mc("PC","Medicina Legal","Em relação à classificação das lesões corporais no Código Penal, a lesão corporal seguida de morte, sem que o agente tenha desejado ou assumido o risco desse resultado, é classificada como:",
   ["Lesão corporal leve","Lesão corporal grave","Lesão corporal gravíssima","Lesão corporal seguida de morte (preterdolosa)","Homicídio doloso"],
   3,"A lesão corporal seguida de morte, prevista no art. 129, §3º, do CP, é uma hipótese de crime preterdoloso: há dolo na conduta que causa a lesão, mas apenas culpa quanto ao resultado morte, que não foi desejado nem assumido pelo agente."),

# PC — Criminologia (mais)
mc("PC","Criminologia","Assinale a alternativa que apresenta corretamente o conceito de 'criminalidade de colarinho branco' (white collar crime), formulado por Edwin Sutherland.",
   ["Refere-se exclusivamente a crimes violentos cometidos por pessoas de baixa renda.","Refere-se a crimes cometidos por pessoas de elevado status social, geralmente no exercício de sua atividade profissional, como fraudes e desvios financeiros.","É sinônimo de crime organizado violento.","Aplica-se apenas a crimes cometidos por menores de idade.","Refere-se exclusivamente a crimes contra a vida."],
   1,"O conceito de 'criminalidade de colarinho branco', formulado por Edwin Sutherland, refere-se a crimes cometidos por pessoas de elevado status social, geralmente no exercício de sua profissão, como fraudes, corrupção e desvios financeiros."),
mc("PC","Criminologia","No estudo da criminologia, o conceito de 'anomia', desenvolvido por autores como Émile Durkheim e Robert Merton, refere-se a:",
   ["Uma situação de ausência ou enfraquecimento de normas sociais reguladoras da conduta, associada ao aumento de comportamentos desviantes.","Uma teoria exclusivamente biológica sobre o crime.","Um tipo específico de pena prevista no Código Penal.","Sinônimo de reincidência criminal.","Um procedimento de perícia criminal."],
   0,"A anomia refere-se a uma situação de ausência ou enfraquecimento das normas sociais reguladoras da conduta, podendo estar associada ao aumento de comportamentos desviantes e criminosos, segundo teorias sociológicas clássicas da criminologia."),

# PC — Legislacao Especial (mais)
mc("PC","Legislação Especial","Segundo a Lei de Abuso de Autoridade (Lei nº 13.869/2019), é correto afirmar que a ação penal por crimes nela previstos é, em regra:",
   ["Privada, exclusiva da vítima.","Pública incondicionada.","Pública condicionada à representação do ofendido, sempre.","Inexistente, tratando-se apenas de infração administrativa.","Dependente exclusivamente de requisição ministerial."],
   1,"A ação penal relativa aos crimes de abuso de autoridade previstos na Lei nº 13.869/2019 é, em regra, pública incondicionada."),
mc("PC","Legislação Especial","Sobre o Estatuto do Idoso (Lei nº 10.741/2003), é correto afirmar que ele assegura à pessoa idosa, entre outros direitos:",
   ["Apenas o direito à assistência médica gratuita, sem qualquer outra garantia.","Prioridade no atendimento, proteção à vida e à saúde, e direitos específicos em diversas áreas, como educação, trabalho e previdência social.","Nenhum direito diferenciado em relação aos demais cidadãos.","Apenas benefícios de natureza tributária.","Direitos exclusivamente relacionados à moradia."],
   1,"O Estatuto do Idoso assegura à pessoa idosa prioridade no atendimento, proteção à vida e à saúde, além de direitos específicos em áreas como educação, cultura, esporte, lazer, trabalho, previdência social, entre outras.")

with open("/home/claude/qbank/questions.json","w",encoding="utf-8") as f:
    json.dump(BANK, f, ensure_ascii=False, indent=None)

print("total:", len(BANK))
from collections import Counter
c = Counter(q["corp"] for q in BANK)
print(c)
c2 = Counter((q["corp"],q["disc"]) for q in BANK)
for k,v in sorted(c2.items()):
    print(k,v)
