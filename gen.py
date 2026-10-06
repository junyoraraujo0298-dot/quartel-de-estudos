# -*- coding: utf-8 -*-
import json

qid = [0]
def nid():
    qid[0]+=1
    return qid[0]

BANK = []

def ce(corp, disc, enun, resp, exp):
    BANK.append({"id":nid(),"corp":corp,"disc":disc,"tipo":"CE","enun":enun,"resp":resp,"exp":exp})

def mc(corp, disc, enun, alts, correct, exp):
    assert len(alts)==5
    BANK.append({"id":nid(),"corp":corp,"disc":disc,"tipo":"MC","enun":enun,"alts":alts,"resp":correct,"exp":exp})

# =====================================================================
# PMMA — CERTO/ERRADO (P1 Conhecimentos Gerais + P2 Conhecimentos Especificos)
# =====================================================================

# ---- Português (PM) ----
ce("PM","Língua Portuguesa","Na frase 'Assiste-se, hoje, a um aumento da criminalidade', o verbo 'assistir', no sentido de 'presenciar', é transitivo indireto e exige a preposição 'a'.",True,"Correto. 'Assistir' no sentido de presenciar/testemunhar é transitivo indireto, regendo-se com a preposição 'a': assiste-se a um aumento.")
ce("PM","Língua Portuguesa","O verbo 'chegar', quando indica destino, deve ser regido pela preposição 'em', sendo condenado pela norma-padrão o uso da preposição 'a' nesse contexto.",False,"Errado. A norma-padrão recomenda o uso da preposição 'a' com o verbo 'chegar' (chegar a algum lugar), e não 'em', embora este último seja frequente na língua coloquial.")
ce("PM","Língua Portuguesa","Em 'Fazem cinco anos que o policial ingressou na corporação', há desvio da norma-padrão, pois o verbo 'fazer', indicando tempo decorrido, deveria permanecer na terceira pessoa do singular.",True,"Correto. O verbo 'fazer' indicando tempo é impessoal e deve ficar sempre no singular: 'Faz cinco anos'.")
ce("PM","Língua Portuguesa","Na oração 'Houveram muitas ocorrências durante o plantão', o verbo 'haver', no sentido de existir, é impessoal e não deveria ter sido flexionado no plural.",True,"Correto. O verbo 'haver', no sentido de existir, é impessoal e permanece invariável na 3ª pessoa do singular: 'Houve muitas ocorrências'.")
ce("PM","Língua Portuguesa","O uso da crase é obrigatório na expressão 'à paisana', por se tratar de locução adverbial feminina.",True,"Correto. Locuções adverbiais femininas formadas por 'a + substantivo/adjetivo feminino' recebem o acento indicativo de crase, como em 'à paisana', 'às pressas'.")
ce("PM","Língua Portuguesa","É correto o emprego da crase em 'Entreguei o documento à ele', uma vez que pronomes pessoais do caso reto também podem receber o acento grave.",False,"Errado. Não se usa crase antes de pronomes pessoais retos ('ele', 'ela'), pois estes não admitem o artigo feminino 'a' que a crase representa. O correto é 'Entreguei o documento a ele'.")
ce("PM","Língua Portuguesa","Na frase 'Vendem-se casas naquele bairro', o 'se' funciona como partícula apassivadora, e o sujeito da oração é 'casas'.",True,"Correto. Trata-se de voz passiva sintética: 'se' é partícula apassivadora e 'casas' é o sujeito paciente, concordando com o verbo no plural.")
ce("PM","Língua Portuguesa","Em 'Precisa-se de policiais para a nova unidade', o 'se' é índice de indeterminação do sujeito, uma vez que o verbo 'precisar' é transitivo indireto e não admite voz passiva sintética nessa construção.",True,"Correto. Como 'precisar de' é transitivo indireto, o 'se' não pode ser apassivador; funciona como índice de indeterminação do sujeito, e o verbo permanece no singular.")
ce("PM","Língua Portuguesa","A vírgula deve ser empregada para isolar o aposto explicativo, sendo seu uso, nesse caso, uma exigência da norma-padrão, e não mera opção estilística.",True,"Correto. O aposto explicativo é isolado por vírgulas, travessões ou parênteses, sendo essa pontuação obrigatória para marcar seu caráter de explicação adicional.")
ce("PM","Língua Portuguesa","É facultativo o uso de vírgula antes da conjunção 'mas', já que essa conjunção adversativa dispensa qualquer separação do restante do período.",False,"Errado. A conjunção adversativa 'mas' deve, como regra, ser antecedida de vírgula, pois introduz uma oração que contrasta com a anterior.")
ce("PM","Língua Portuguesa","Na frase 'Ele mesmo confirmou a ocorrência', a palavra 'mesmo' concorda em gênero e número com o termo a que se refere, funcionando como reforço do pronome.",True,"Correto. Quando usado como reforço de pronome ou substantivo (equivalente a 'próprio'), 'mesmo' varia: 'ele mesmo', 'ela mesma', 'eles mesmos'.")
ce("PM","Língua Portuguesa","O pronome relativo 'cujo' deve concordar em gênero e número com o substantivo que o antecede, e não com o que o sucede.",False,"Errado. 'Cujo' concorda com o substantivo que vem depois dele (o possuído), e não com o antecedente que vem antes.")
ce("PM","Língua Portuguesa","Em 'Entre eu e você não deve haver segredos', há desvio da norma-padrão, pois após preposição os pronomes pessoais retos devem ser substituídos pelos oblíquos tônicos.",True,"Correto. Após preposição, usam-se os pronomes oblíquos tônicos: 'entre mim e você', e não os pronomes retos 'eu' e 'você'.")
ce("PM","Língua Portuguesa","Na frase 'Vi ela na viatura ontem', o emprego do pronome 'ela' como objeto direto está de acordo com a norma-padrão da língua portuguesa.",False,"Errado. Como objeto direto de verbos transitivos diretos, a norma-padrão recomenda o uso do pronome oblíquo átono: 'Vi-a na viatura ontem'.")
ce("PM","Língua Portuguesa","A palavra 'menos' é invariável em português, sendo incorreta a forma 'menas', ainda que empregada, por vezes, na linguagem coloquial.",True,"Correto. 'Menos' não possui flexão de gênero ou número; a forma 'menas' não existe na norma-padrão.")
ce("PM","Língua Portuguesa","O plural de 'cidadão' pode ser 'cidadãos', 'cidadães' ou 'cidadões', sendo as três formas igualmente aceitas pela norma-padrão.",False,"Errado. Apenas 'cidadãos' é a forma de plural aceita pela norma-padrão para 'cidadão'.")
ce("PM","Língua Portuguesa","Em 'Meio-dia e meia', a palavra 'meia' concorda com 'hora' (subentendida), e não com 'meio-dia', razão pela qual permanece no feminino.",True,"Correto. Em 'meio-dia e meia', 'meia' refere-se a 'meia hora' subentendida, daí a concordância no feminino.")
ce("PM","Língua Portuguesa","O verbo 'implicar', no sentido de 'acarretar', é transitivo direto e dispensa a preposição 'em' antes do complemento, conforme a norma-padrão.",True,"Correto. Nesse sentido, 'implicar' é transitivo direto: 'A conduta implica sanção disciplinar', sem a preposição 'em'.")
ce("PM","Língua Portuguesa","Na frase 'Eram quase seis horas quando a viatura chegou ao local', o verbo 'ser', indicando horas, concorda com o numeral que expressa a hora, e não fica invariável.",True,"Correto. O verbo 'ser' na indicação de horas concorda com o numeral: 'era uma hora', 'eram seis horas'.")
ce("PM","Língua Portuguesa","O uso do hífen em 'guarda-noturno' segue a mesma regra aplicável a substantivos compostos por dois substantivos ou substantivo e adjetivo que formam uma unidade de sentido.",True,"Correto. 'Guarda-noturno' é substantivo composto (substantivo + adjetivo) que designa uma função, mantendo o hífen conforme o Acordo Ortográfico.")
ce("PM","Língua Portuguesa","Segundo a norma-padrão, é obrigatório o emprego da próclise em início absoluto de período, como em 'Se apresentou à autoridade imediatamente'.",False,"Errado. Em início absoluto de período, a norma-padrão exige a ênclise, e não a próclise: 'Apresentou-se à autoridade imediatamente'.")

# ---- História do Brasil (PM) ----
ce("PM","História do Brasil","A Proclamação da República, em 15 de novembro de 1889, foi liderada pelo Marechal Deodoro da Fonseca, que se tornou o primeiro presidente do Brasil.",True,"Correto. O golpe militar de 15 de novembro de 1889 depôs o imperador Dom Pedro II e instituiu a República, tendo Deodoro da Fonseca como primeiro presidente.")
ce("PM","História do Brasil","A Lei Áurea, sancionada em 1888 pela Princesa Isabel, aboliu a escravidão no Brasil sem prever qualquer indenização aos ex-senhores de escravos.",True,"Correto. A Lei Áurea, de 13 de maio de 1888, extinguiu a escravidão no Brasil de forma direta, sem indenização aos senhores, embora o tema tenha sido debatido à época.")
ce("PM","História do Brasil","A Revolução de 1930 levou Getúlio Vargas ao poder e encerrou o período da chamada República Velha, marcada pela política do café com leite.",True,"Correto. A Revolução de 1930 pôs fim à hegemonia política de São Paulo e Minas Gerais (café com leite) e iniciou a chamada Era Vargas.")
ce("PM","História do Brasil","O Estado Novo, período ditatorial implantado por Getúlio Vargas em 1937, caracterizou-se pela ampliação das liberdades democráticas e pelo fortalecimento do Poder Legislativo.",False,"Errado. O Estado Novo (1937-1945) foi um período ditatorial marcado justamente pelo fechamento do Congresso Nacional e pela restrição de liberdades democráticas, concentrando poder no Executivo.")
ce("PM","História do Brasil","O regime militar brasileiro teve início em 1964, com a deposição do presidente João Goulart, e se estendeu até 1985, quando ocorreu a redemocratização.",True,"Correto. O golpe de 1964 depôs João Goulart e instaurou o regime militar, que perdurou até 1985, com a eleição indireta de Tancredo Neves marcando a redemocratização.")
ce("PM","História do Brasil","A Constituição Federal de 1988, conhecida como Constituição Cidadã, ampliou significativamente os direitos e garantias fundamentais em comparação às constituições anteriores.",True,"Correto. A Constituição de 1988 é chamada de 'Cidadã' justamente por ampliar os direitos individuais, sociais e coletivos, consolidando o Estado Democrático de Direito.")
ce("PM","História do Brasil","O Descobrimento do Brasil, em 1500, é tradicionalmente associado à chegada da esquadra portuguesa comandada por Pedro Álvares Cabral.",True,"Correto. A esquadra de Pedro Álvares Cabral aportou no litoral da atual Bahia em abril de 1500, episódio tradicionalmente associado ao descobrimento do Brasil pelos portugueses.")
ce("PM","História do Brasil","O período colonial brasileiro caracterizou-se pelo chamado 'pacto colonial', segundo o qual a colônia deveria manter relações comerciais exclusivas com a metrópole portuguesa.",True,"Correto. O pacto colonial (exclusivo metropolitano) determinava que o comércio da colônia fosse monopolizado pela metrópole, restringindo trocas com outras nações.")
ce("PM","História do Brasil","A Inconfidência Mineira, ocorrida no final do século XVIII, foi um movimento de caráter separatista que teve êxito imediato, resultando na independência de Minas Gerais em relação a Portugal.",False,"Errado. A Inconfidência Mineira (1789) foi descoberta antes de sua execução e reprimida pela Coroa portuguesa, não resultando em independência; Tiradentes foi condenado e executado.")
ce("PM","História do Brasil","A vinda da Família Real portuguesa para o Brasil, em 1808, ocorreu em razão das invasões napoleônicas em Portugal e teve como consequência a abertura dos portos brasileiros às nações amigas.",True,"Correto. Fugindo das tropas de Napoleão, a Corte portuguesa transferiu-se para o Brasil em 1808, e Dom João VI decretou a Abertura dos Portos às Nações Amigas.")
ce("PM","História do Brasil","A independência do Brasil, proclamada por Dom Pedro I em 1822, resultou imediatamente em uma ruptura completa e pacífica com Portugal, sem qualquer conflito armado subsequente.",False,"Errado. Apesar da Proclamação em 1822, houve resistência de tropas portuguesas em diversas províncias, gerando conflitos armados até a efetiva consolidação da independência em algumas regiões.")
ce("PM","História do Brasil","O Brasil Império foi marcado por três períodos distintos: o Primeiro Reinado, o Período Regencial e o Segundo Reinado.",True,"Correto. Essa é a divisão clássica do período imperial brasileiro (1822-1889): Primeiro Reinado (Dom Pedro I), Período Regencial e Segundo Reinado (Dom Pedro II).")
ce("PM","História do Brasil","A Guerra do Paraguai (1864-1870) envolveu o Brasil, a Argentina e o Uruguai, unidos na Tríplice Aliança contra o Paraguai, governado por Solano López.",True,"Correto. A Guerra do Paraguai opôs a Tríplice Aliança (Brasil, Argentina e Uruguai) ao Paraguai, sendo o maior conflito armado da história da América do Sul.")
ce("PM","História do Brasil","A ditadura militar brasileira (1964-1985) teve como um de seus instrumentos de repressão o Ato Institucional nº 5 (AI-5), editado em 1968, que suspendeu diversas garantias constitucionais.",True,"Correto. O AI-5, de dezembro de 1968, foi um dos atos mais duros do regime militar, suspendendo garantias como o habeas corpus para crimes políticos e fechando o Congresso Nacional.")
ce("PM","História do Brasil","O processo de redemocratização brasileira culminou com a eleição direta para presidente em 1989, vencida por Fernando Collor de Mello.",True,"Correto. Em 1989 ocorreu a primeira eleição presidencial direta desde 1960, vencida por Fernando Collor de Mello sobre Luiz Inácio Lula da Silva no segundo turno.")
ce("PM","História do Brasil","A escravidão indígena foi a única forma de trabalho compulsório utilizada durante todo o período colonial brasileiro, não havendo registro de tráfico de africanos escravizados.",False,"Errado. Além da escravização indígena, o Brasil colonial recorreu maciçamente ao tráfico transatlântico de africanos escravizados, sobretudo a partir do século XVI, para o trabalho nos engenhos e, depois, nas minas.")
ce("PM","História do Brasil","O Tratado de Tordesilhas, de 1494, dividiu as terras recém-descobertas entre Portugal e Espanha antes mesmo da chegada oficial de Cabral ao Brasil.",True,"Correto. O Tratado de Tordesilhas, assinado em 1494, estabeleceu uma linha de divisão territorial entre os domínios portugueses e espanhóis, anos antes da chegada de Cabral em 1500.")
ce("PM","História do Brasil","O ciclo do ouro, no século XVIII, teve como principal região produtora as Minas Gerais, contribuindo para o deslocamento do eixo econômico da colônia para o Sudeste.",True,"Correto. A descoberta de ouro em Minas Gerais no final do século XVII e ao longo do XVIII deslocou o eixo econômico e populacional da colônia para essa região.")
ce("PM","História do Brasil","A Semana de Arte Moderna de 1922, ocorrida em São Paulo, é considerada um marco do modernismo artístico e cultural brasileiro.",True,"Correto. A Semana de Arte Moderna, realizada no Theatro Municipal de São Paulo em 1922, é considerada o marco inaugural do modernismo no Brasil.")
ce("PM","História do Brasil","O Plano Real, implementado em 1994, no governo de Itamar Franco, teve como principal objetivo o controle da hiperinflação que assolava a economia brasileira.",True,"Correto. O Plano Real, lançado em 1994, teve como principal meta estabilizar a moeda e controlar a hiperinflação crônica que afetava o país havia décadas.")

# ---- História do Maranhão (PM) ----
ce("PM","História do Maranhão","A cidade de São Luís, capital do Maranhão, foi fundada por colonizadores franceses em 1612, sendo a única capital brasileira de origem francesa.",True,"Correto. São Luís foi fundada em 1612 pelos franceses, liderados por Daniel de La Touche, sendo até hoje a única capital de estado brasileira fundada por colonizadores franceses.")
ce("PM","História do Maranhão","Após a fundação francesa, o Maranhão foi definitivamente incorporado ao domínio português somente após a expulsão dos holandeses, que nunca chegaram a ocupar a região.",False,"Errado. Após expulsarem os franceses em 1615, os portugueses também precisaram enfrentar e expulsar os holandeses, que ocuparam São Luís entre 1641 e 1644, antes da definitiva consolidação portuguesa na região.")
ce("PM","História do Maranhão","O Maranhão integrou, no período colonial, o Estado do Maranhão e Grão-Pará, administrativamente separado do Estado do Brasil, com sede em São Luís.",True,"Correto. Criado em 1621, o Estado do Maranhão (depois Maranhão e Grão-Pará) era administrativamente distinto do Estado do Brasil, subordinando-se diretamente à Coroa portuguesa.")
ce("PM","História do Maranhão","A Balaiada, revolta popular ocorrida no Maranhão entre 1838 e 1841, teve entre suas lideranças figuras como Raimundo Gomes e Cosme Bento das Chagas, o 'Negro Cosme'.",True,"Correto. A Balaiada foi uma das maiores revoltas do período regencial, com lideranças como Raimundo Gomes, Cosme Bento das Chagas (líder de um grupo de escravizados) e Manuel dos Anjos Ferreira.")
ce("PM","História do Maranhão","A Balaiada foi um movimento de apoio incondicional às elites agrárias maranhenses, sem qualquer participação popular ou de escravizados.",False,"Errado. A Balaiada teve ampla participação popular, incluindo sertanejos, vaqueiros e escravizados fugidos, contrapondo-se, em parte, aos interesses das elites locais então no poder.")
ce("PM","História do Maranhão","O ciclo econômico do algodão, no século XVIII, foi um dos fatores que impulsionou o desenvolvimento econômico do Maranhão colonial, associado à atuação da Companhia de Comércio do Grão-Pará e Maranhão.",True,"Correto. A Companhia de Comércio do Grão-Pará e Maranhão, criada no século XVIII, fomentou a produção e exportação de algodão e outros produtos, impulsionando a economia da região.")
ce("PM","História do Maranhão","O Maranhão participou ativamente da Confederação do Equador, movimento separatista de 1824, sendo uma das províncias que a lideraram desde o início.",False,"Errado. A Confederação do Equador teve como epicentro Pernambuco; o Maranhão não foi uma província protagonista do movimento, mantendo posição majoritariamente distinta desse levante.")
ce("PM","História do Maranhão","A adesão do Maranhão à independência do Brasil, em 1823, não ocorreu de forma imediata, havendo resistência de setores ligados a Portugal antes da efetiva adesão da província.",True,"Correto. A adesão maranhense à independência somente se consolidou em 1823, após enfrentamentos, com destaque para a atuação de Lord Cochrane, que ajudou a reprimir a resistência lusitana em São Luís.")
ce("PM","História do Maranhão","O Maranhão é reconhecido nacionalmente pela tradição cultural do Bumba Meu Boi, manifestação popular que mescla elementos indígenas, africanos e europeus.",True,"Correto. O Bumba Meu Boi maranhense é uma das mais importantes manifestações culturais do estado, reconhecida como Patrimônio Cultural Imaterial do Brasil, com forte mescla de influências indígenas, africanas e europeias.")
ce("PM","História do Maranhão","O centro histórico de São Luís foi declarado Patrimônio Cultural da Humanidade pela UNESCO, em razão de seu conjunto arquitetônico colonial preservado, com destaque para os azulejos portugueses.",True,"Correto. O Centro Histórico de São Luís foi reconhecido pela UNESCO como Patrimônio Mundial em 1997, sobretudo por seu conjunto arquitetônico colonial português, incluindo o uso característico de azulejos nas fachadas.")
ce("PM","História do Maranhão","Após a independência do Brasil, o Maranhão manteve grande importância econômica devido à produção de açúcar e, principalmente, de algodão, exportado através do porto de São Luís.",True,"Correto. Durante boa parte do século XIX, o Maranhão figurou entre os grandes produtores e exportadores de algodão e açúcar do Império, escoados pelo porto de São Luís.")

# ---- Geografia do Brasil (PM) ----
ce("PM","Geografia do Brasil","O Brasil é dividido oficialmente pelo IBGE em cinco grandes regiões: Norte, Nordeste, Centro-Oeste, Sudeste e Sul.",True,"Correto. A divisão regional oficial do IBGE separa o território brasileiro em cinco macrorregiões: Norte, Nordeste, Centro-Oeste, Sudeste e Sul.")
ce("PM","Geografia do Brasil","O Maranhão é considerado, por diferentes classificações geográficas, um estado de transição entre as regiões Nordeste e Norte do Brasil, situação relacionada à presença da Amazônia Legal em seu território.",True,"Correto. Embora integre oficialmente a região Nordeste, o Maranhão também faz parte da Amazônia Legal, sendo frequentemente descrito como um estado de transição entre as paisagens amazônicas e nordestinas.")
ce("PM","Geografia do Brasil","O bioma predominante em todo o território brasileiro é exclusivamente a Floresta Amazônica, não havendo outros biomas relevantes no país.",False,"Errado. O Brasil possui diversos biomas, entre eles Amazônia, Cerrado, Caatinga, Mata Atlântica, Pampa e Pantanal, cada um com características e distribuição geográfica distintas.")
ce("PM","Geografia do Brasil","O clima equatorial, quente e úmido, com pouca variação de temperatura ao longo do ano, é característico da região amazônica.",True,"Correto. O clima equatorial, marcado por altas temperaturas e umidade constante, é típico da região amazônica, com pequena amplitude térmica anual.")
ce("PM","Geografia do Brasil","O semiárido nordestino caracteriza-se por clima tropical semiárido, com baixos índices pluviométricos e chuvas irregulares concentradas em curto período do ano.",True,"Correto. O clima semiárido do sertão nordestino é marcado por escassez e irregularidade de chuvas, associado à vegetação de caatinga.")
ce("PM","Geografia do Brasil","O relevo brasileiro é predominantemente montanhoso, com a maior parte do território situada acima de 2.000 metros de altitude.",False,"Errado. O relevo brasileiro é predominantemente formado por planaltos e planícies de baixa e média altitude; áreas acima de 2.000 metros são exceções pontuais, como picos na Serra da Mantiqueira e no Sistema do Espinhaço.")
ce("PM","Geografia do Brasil","A Bacia Amazônica é a maior bacia hidrográfica do mundo em extensão e volume de água, sendo o rio Amazonas seu principal curso d'água.",True,"Correto. A Bacia Amazônica é reconhecida como a maior bacia hidrográfica do planeta, tanto em área de drenagem quanto em volume de água transportado pelo rio Amazonas.")
ce("PM","Geografia do Brasil","A Zona Franca de Manaus é um exemplo de política de incentivo fiscal voltada ao desenvolvimento econômico da região Norte do país.",True,"Correto. Criada em 1967, a Zona Franca de Manaus concede incentivos fiscais para atrair indústrias e promover o desenvolvimento econômico da região amazônica.")
ce("PM","Geografia do Brasil","O fenômeno da urbanização brasileira intensificou-se sobretudo a partir da segunda metade do século XX, associado ao êxodo rural e à industrialização.",True,"Correto. A partir de meados do século XX, o Brasil passou por intensa urbanização, impulsionada pela industrialização e pelo consequente êxodo rural.")

# ---- Geografia do Maranhão (PM) ----
ce("PM","Geografia do Maranhão","O Maranhão é considerado o maior estado da região Nordeste em extensão territorial.",True,"Correto. Com pouco mais de 331 mil km², o Maranhão é o maior estado em área territorial entre os que compõem a região Nordeste do Brasil.")
ce("PM","Geografia do Maranhão","O Parque Nacional dos Lençóis Maranhenses, um dos principais cartões-postais do estado, é formado por extensas dunas de areia branca entremeadas por lagoas de água doce, que se formam principalmente no período chuvoso.",True,"Correto. Os Lençóis Maranhenses são formados por dunas de areia branca e lagoas de água da chuva, que se acumulam entre as dunas principalmente entre os meses chuvosos (aproximadamente de janeiro a junho).")
ce("PM","Geografia do Maranhão","O Delta do Parnaíba, um dos poucos deltas em mar aberto do mundo, está localizado inteiramente em território maranhense, sem qualquer extensão para o Piauí.",False,"Errado. O Delta do Parnaíba está localizado na divisa entre os estados do Maranhão e do Piauí, sendo compartilhado por ambos, e não situado exclusivamente em território maranhense.")
ce("PM","Geografia do Maranhão","Entre os principais rios que cortam o território maranhense estão o Itapecuru, o Mearim, o Pindaré e o Grajaú.",True,"Correto. Esses são alguns dos principais rios maranhenses, importantes tanto para o abastecimento quanto para a economia regional, sobretudo ligados à bacia hidrográfica do estado.")
ce("PM","Geografia do Maranhão","O clima predominante no Maranhão é o tropical, com estações bem definidas de chuva e estiagem, havendo, contudo, variações regionais, sobretudo no leste do estado, com tendência a maior semiaridez.",True,"Correto. O Maranhão apresenta clima tropical, com um período mais chuvoso e outro mais seco; a porção leste do estado tende a apresentar características mais próximas do semiárido nordestino.")
ce("PM","Geografia do Maranhão","A economia maranhense é baseada exclusivamente na atividade industrial, não havendo relevância da agropecuária ou do extrativismo mineral em seu território.",False,"Errado. A economia do Maranhão é diversificada, com relevante participação da agropecuária (como soja e pecuária), do extrativismo mineral (como ferro, escoado pela Estrada de Ferro Carajás) e também de atividades industriais e de serviços.")
ce("PM","Geografia do Maranhão","O município de São Luís está localizado em uma ilha, formada entre as baías de São Marcos e de São José.",True,"Correto. A capital maranhense está situada na Ilha do Maranhão (também chamada Ilha de São Luís), banhada pelas baías de São Marcos e de São José.")
ce("PM","Geografia do Maranhão","A vegetação maranhense caracteriza-se por uma transição entre formações amazônicas, de cerrado e de caatinga, o que reflete a posição geográfica do estado entre diferentes domínios naturais brasileiros.",True,"Correto. Justamente por sua localização de transição, o Maranhão apresenta uma vegetação diversificada, com influências da Floresta Amazônica, do Cerrado e, em menor grau, da Caatinga.")
ce("PM","Geografia do Maranhão","A Estrada de Ferro Carajás, que conecta a região de mineração no Pará ao Porto do Itaqui, em São Luís, é fundamental para o escoamento de minério de ferro pelo território maranhense.",True,"Correto. A Estrada de Ferro Carajás liga a mina de Carajás (PA) ao Porto do Itaqui, em São Luís (MA), sendo estratégica para o escoamento da produção mineral brasileira.")
ce("PM","Geografia do Maranhão","O Golfão Maranhense é uma extensa reentrância litorânea, formada por baías e rios, que caracteriza parte significativa do litoral do estado.",True,"Correto. O chamado Golfão Maranhense é uma área de recortes litorâneos com diversas baías (como as de São Marcos e São José) e desembocaduras de rios, sendo uma feição marcante da costa maranhense.")

# ---- Raciocínio Lógico (PM) ----
ce("PM","Raciocínio Lógico","A negação da proposição 'Alguns policiais estão de folga' é 'Nenhum policial está de folga'.",True,"Correto. A negação de uma proposição existencial ('algum...') é uma proposição universal com o predicado negado: 'nenhum policial está de folga'.")
ce("PM","Raciocínio Lógico","Em lógica proposicional, a disjunção 'p ou q' é falsa apenas quando ambas as proposições p e q forem falsas.",True,"Correto. Na disjunção inclusiva, o resultado só é falso quando as duas proposições envolvidas forem falsas; em qualquer outro caso, é verdadeiro.")
ce("PM","Raciocínio Lógico","A condicional 'Se p, então q' é falsa apenas quando p for verdadeiro e q for falso.",True,"Correto. Esta é exatamente a definição da condicional material: ela só é falsa quando o antecedente é verdadeiro e o consequente é falso; em todos os demais casos, é verdadeira.")
ce("PM","Raciocínio Lógico","A negação de 'Se chove, então a rua fica molhada' equivale a 'Chove e a rua não fica molhada'.",True,"Correto. A negação da condicional 'se p então q' é 'p e não q', ou seja, afirma-se o antecedente e nega-se o consequente.")
ce("PM","Raciocínio Lógico","Duas proposições são equivalentes quando possuem, em todas as linhas da tabela-verdade, valores lógicos (V ou F) idênticos.",True,"Correto. A equivalência lógica entre duas proposições ocorre justamente quando elas assumem os mesmos valores de verdade em todas as combinações possíveis das proposições simples envolvidas.")
ce("PM","Raciocínio Lógico","Pela Lei de De Morgan, a negação de 'p e q' é equivalente a 'não p e não q'.",False,"Errado. Pela Lei de De Morgan, a negação de 'p e q' é equivalente a 'não p ou não q' (troca-se o conectivo 'e' pelo 'ou' ao negar).")
ce("PM","Raciocínio Lógico","Pela Lei de De Morgan, a negação de 'p ou q' é equivalente a 'não p e não q'.",True,"Correto. Ao negar uma disjunção, trocam-se os conectivos: 'não (p ou q)' equivale a 'não p e não q'.")
ce("PM","Raciocínio Lógico","O argumento 'Se todo soldado é disciplinado, e Marcos é soldado, logo Marcos é disciplinado' constitui uma inferência válida, conhecida como modus ponens.",True,"Correto. Trata-se de aplicação clássica do modus ponens: de 'todo P é Q' e 'Marcos é P', conclui-se validamente que 'Marcos é Q'.")
ce("PM","Raciocínio Lógico","Na sequência numérica 3, 6, 12, 24, 48, cada termo é obtido pela soma de 3 unidades ao termo anterior.",False,"Errado. Cada termo é obtido pela multiplicação do anterior por 2 (progressão geométrica de razão 2), e não pela soma de 3 unidades.")
ce("PM","Raciocínio Lógico","Na sequência 1, 4, 9, 16, 25, cada termo corresponde ao quadrado de um número natural em ordem crescente.",True,"Correto. Trata-se da sequência dos quadrados perfeitos: 1², 2², 3², 4², 5², ou seja, 1, 4, 9, 16, 25.")
ce("PM","Raciocínio Lógico","Se a proposição 'p' é verdadeira, então a proposição 'não p' também será necessariamente verdadeira.",False,"Errado. Se 'p' é verdadeira, sua negação 'não p' é necessariamente falsa, e não verdadeira, pois ambas possuem valores lógicos sempre opostos.")
ce("PM","Raciocínio Lógico","Um argumento é considerado válido quando, sendo as premissas verdadeiras, a conclusão é necessariamente verdadeira.",True,"Correto. A validade lógica de um argumento está relacionada à estrutura: se as premissas forem verdadeiras, a conclusão deve, obrigatoriamente, também ser verdadeira.")
ce("PM","Raciocínio Lógico","Na tabela-verdade da bicondicional 'p se, e somente se, q', o resultado é verdadeiro sempre que p e q tiverem o mesmo valor lógico.",True,"Correto. A bicondicional é verdadeira quando ambas as proposições possuem o mesmo valor lógico (ambas verdadeiras ou ambas falsas), e falsa quando os valores divergem.")
ce("PM","Raciocínio Lógico","Considerando que 'todo A é B' seja uma proposição verdadeira, é correto concluir, de forma logicamente válida, que 'todo B é A'.",False,"Errado. A proposição universal afirmativa 'todo A é B' não pode ser convertida simplesmente em 'todo B é A'; essa conversão constitui falácia lógica, pois a relação de inclusão não é simétrica.")
ce("PM","Raciocínio Lógico","Considerando um conjunto de 30 policiais, em que 18 atuam no policiamento ostensivo e 15 atuam no trânsito, havendo 8 que atuam em ambas as atividades, o número de policiais que atuam em pelo menos uma das duas atividades é 25.",True,"Correto. Pelo princípio da inclusão-exclusão: 18 + 15 − 8 = 25 policiais atuam em pelo menos uma das duas atividades.")

# ---- Legislação Institucional PM (PM) ----
ce("PM","Legislação Institucional PM","A hierarquia militar é a ordenação da autoridade em níveis diferentes dentro da estrutura da corporação, e a disciplina consiste na rigorosa observância das leis, regulamentos e normas.",True,"Correto. Essa é a definição clássica de hierarquia e disciplina adotada pelos estatutos e regulamentos militares, aplicável, por simetria, às polícias militares estaduais.")
ce("PM","Legislação Institucional PM","Nos termos da Constituição Federal, as polícias militares e os corpos de bombeiros militares dos estados são organizados com base na hierarquia e na disciplina, subordinando-se aos respectivos Governadores de Estado.",True,"Correto, conforme art. 42, caput, c/c art. 144, §6º, da Constituição Federal: os militares dos Estados são organizados com base na hierarquia e disciplina, e as polícias militares e corpos de bombeiros militares subordinam-se aos Governadores dos Estados.")
ce("PM","Legislação Institucional PM","A transgressão disciplinar militar é apurada por meio de processo judicial perante a Justiça Militar, da mesma forma que ocorre com o crime militar.",False,"Errado. A transgressão disciplinar é apurada em âmbito administrativo (sindicância ou processo administrativo disciplinar), no interior da própria corporação, diferentemente do crime militar, que é apurado e julgado pela Justiça Militar.")
ce("PM","Legislação Institucional PM","Os postos e graduações da carreira militar estadual seguem uma ordem hierárquica que vai, de modo geral, do soldado ao coronel, passando por graduações intermediárias como cabo, sargento e subtenente, e por postos de oficiais.",True,"Correto. A estrutura hierárquica típica das polícias militares brasileiras contempla, entre as praças, graduações como soldado, cabo, sargento e subtenente, e entre os oficiais, postos que vão de segundo-tenente a coronel.")
ce("PM","Legislação Institucional PM","O militar estadual, em regra, não pode acumular cargo público, ressalvadas as exceções constitucionalmente previstas, como a de um cargo de professor combinado com outro técnico ou científico.",True,"Correto. Aplica-se, por simetria, a vedação constitucional de acumulação de cargos públicos (art. 37, XVI e XVII, CF), ressalvadas as hipóteses de exceção nela previstas.")
ce("PM","Legislação Institucional PM","A promoção na carreira militar estadual pode ocorrer, entre outros critérios, por antiguidade e por merecimento, conforme os critérios estabelecidos na legislação e nos regulamentos específicos de cada corporação.",True,"Correto. Antiguidade e merecimento são critérios clássicos de promoção nas carreiras militares, previstos de forma geral nos estatutos e regulamentos de promoções das corporações.")
ce("PM","Legislação Institucional PM","O policial militar, quando no exercício de suas funções, está isento de responsabilização civil e administrativa por seus atos, respondendo unicamente na esfera penal.",False,"Errado. O agente público, incluindo o militar estadual, pode responder cumulativamente nas esferas civil, administrativa (disciplinar) e penal por seus atos, não havendo isenção das duas primeiras.")
ce("PM","Legislação Institucional PM","O uso da força pela Polícia Militar deve observar os princípios da legalidade, necessidade, proporcionalidade e moderação, conforme diretrizes amplamente reconhecidas na atuação policial.",True,"Correto. Esses são os critérios centrais reconhecidos para o uso da força por agentes de segurança pública, tanto pela doutrina de direitos humanos quanto pela normatização interna das corporações.")
ce("PM","Legislação Institucional PM","O poder disciplinar da administração militar permite a aplicação de sanções aos integrantes da corporação em razão de transgressões, assegurados o contraditório e a ampla defesa.",True,"Correto. O poder disciplinar autoriza a apuração e a punição de transgressões no âmbito da corporação, sempre respeitando as garantias constitucionais do contraditório e da ampla defesa.")
ce("PM","Legislação Institucional PM","O dever de obediência do militar às ordens superiores é absoluto, não comportando qualquer exceção, ainda que a ordem seja manifestamente ilegal ou configure crime.",False,"Errado. O dever de obediência hierárquica não é absoluto: o subordinado não deve cumprir ordens manifestamente ilegais ou que configurem crime, respondendo o superior que as expediu.")
ce("PM","Legislação Institucional PM","Compete à Polícia Militar, nos termos constitucionais, o policiamento ostensivo e a preservação da ordem pública, sendo considerada força auxiliar e reserva do Exército.",True,"Correto, conforme art. 144, §5º e §6º da CF: cabe à PM a polícia ostensiva e a preservação da ordem pública, sendo as polícias militares consideradas forças auxiliares e reserva do Exército.")
ce("PM","Legislação Institucional PM","O policial militar em situação de inatividade (reserva ou reforma) deixa de estar sujeito a qualquer norma de conduta ou disciplina da corporação.",False,"Errado. Ainda que na inatividade, o militar permanece vinculado a determinadas normas de conduta e disciplina compatíveis com sua condição, conforme previsto nos estatutos militares.")
ce("PM","Legislação Institucional PM","O princípio da hierarquia impõe uma relação de subordinação entre postos e graduações, sendo a antiguidade, dentro de um mesmo posto ou graduação, um dos critérios para o estabelecimento de precedência.",True,"Correto. Dentro de um mesmo posto ou graduação, a antiguidade (tempo de permanência naquele nível) costuma ser critério relevante para fins de precedência hierárquica.")
ce("PM","Legislação Institucional PM","O ingresso na Polícia Militar do Maranhão, no cargo de Soldado do Quadro de Praças, exige, entre outros requisitos, idade entre 18 e 35 anos e altura mínima diferenciada conforme o sexo do candidato.",True,"Correto. Segundo os requisitos usualmente estabelecidos em editais desse tipo de concurso, exige-se idade entre 18 e 35 anos e altura mínima distinta para candidatos do sexo masculino e feminino.")
ce("PM","Legislação Institucional PM","A investigação social é uma das fases do concurso público para ingresso na Polícia Militar, tendo por finalidade verificar a idoneidade moral e social do candidato.",True,"Correto. A investigação social integra as fases eliminatórias típicas de concursos para ingresso em corporações militares estaduais, com o objetivo de avaliar a idoneidade do candidato.")

# ---- Informática (PM) ----
ce("PM","Noções de Informática","O protocolo HTTPS utiliza criptografia para proteger a comunicação entre o navegador e o servidor, sendo amplamente utilizado em sistemas que exigem segurança de dados.",True,"Correto. O HTTPS emprega criptografia via TLS/SSL para proteger a confidencialidade e a integridade dos dados trafegados entre cliente e servidor.")
ce("PM","Noções de Informática","Um firewall tem como função exclusiva remover vírus já instalados no computador, não atuando na filtragem de tráfego de rede.",False,"Errado. O firewall atua controlando e filtrando o tráfego de rede (entrada e saída); a remoção de vírus já instalados é função do antivírus, não do firewall.")
ce("PM","Noções de Informática","O backup do tipo incremental copia apenas os arquivos alterados desde o último backup realizado, seja ele completo ou incremental.",True,"Correto. O backup incremental copia somente os dados modificados desde o último backup de qualquer tipo, tornando o processo mais rápido e econômico em espaço.")
ce("PM","Noções de Informática","O atalho Ctrl+Z, na maioria dos softwares de edição de texto, é utilizado para refazer (redo) a última ação desfeita.",False,"Errado. Ctrl+Z é o atalho para desfazer (undo) a última ação; o atalho para refazer (redo) costuma ser Ctrl+Y ou Ctrl+Shift+Z, dependendo do programa.")
ce("PM","Noções de Informática","A memória RAM é um tipo de memória volátil, ou seja, seu conteúdo é perdido quando o computador é desligado.",True,"Correto. A memória RAM (Random Access Memory) é volátil e perde as informações armazenadas assim que o equipamento é desligado, ao contrário de dispositivos de armazenamento permanente, como o HD ou SSD.")
ce("PM","Noções de Informática","O termo 'phishing' designa uma técnica utilizada para enganar usuários e obter informações sigilosas, como senhas e dados bancários, geralmente por meio de mensagens ou sites falsos.",True,"Correto. Phishing é uma fraude eletrônica em que o golpista se passa por uma instituição confiável para induzir a vítima a fornecer dados sigilosos.")
ce("PM","Noções de Informática","Um antivírus atualizado garante proteção total contra qualquer tipo de ameaça digital, tornando desnecessárias outras práticas de segurança, como o uso de senhas fortes.",False,"Errado. Nenhum antivírus garante proteção absoluta; boas práticas de segurança, como senhas fortes, atualizações do sistema e cautela com links suspeitos, continuam sendo necessárias.")
ce("PM","Noções de Informática","O termo 'nuvem' (cloud computing) refere-se ao armazenamento e processamento de dados por meio da internet, em servidores remotos, em vez de no próprio computador do usuário.",True,"Correto. A computação em nuvem permite armazenar e processar dados remotamente, acessando-os pela internet, sem depender exclusivamente do armazenamento local do dispositivo.")
ce("PM","Noções de Informática","No Microsoft Word, o recurso de 'Localizar e Substituir' permite encontrar um termo específico no documento e substituí-lo, de forma automática, por outro termo definido pelo usuário.",True,"Correto. A ferramenta 'Localizar e Substituir' (geralmente acessada por Ctrl+U ou pelo menu correspondente) permite buscar e trocar termos automaticamente ao longo de todo o documento.")
ce("PM","Noções de Informática","Uma rede local (LAN) conecta computadores em uma área geograficamente ampla, como diferentes países, sendo equivalente, em alcance, a uma rede de longa distância (WAN).",False,"Errado. A LAN (Local Area Network) conecta dispositivos em uma área geográfica restrita, como um escritório ou residência; já a WAN (Wide Area Network) é que abrange áreas geograficamente extensas, como países ou continentes.")
ce("PM","Noções de Informática","No Microsoft Excel, a função SOMA é utilizada para somar os valores contidos em um intervalo de células selecionado.",True,"Correto. A função SOMA (=SOMA(intervalo)) é uma das funções básicas do Excel, utilizada para somar os valores numéricos de um conjunto de células.")
ce("PM","Noções de Informática","O uso de senhas idênticas em múltiplos sites e serviços é uma prática recomendada de segurança da informação, pois facilita a memorização e reduz o risco de esquecimento.",False,"Errado. Reutilizar a mesma senha em vários serviços é uma prática de risco: se um deles for comprometido, todos os demais ficam vulneráveis; recomenda-se o uso de senhas distintas e fortes para cada serviço.")
ce("PM","Noções de Informática","O termo 'malware' é um termo genérico que abrange diferentes tipos de softwares maliciosos, como vírus, worms, trojans e ransomware.",True,"Correto. 'Malware' é o termo abrangente para qualquer software malicioso, incluindo vírus, worms, cavalos de troia (trojans), ransomware, spyware, entre outros.")
ce("PM","Noções de Informática","O ransomware é um tipo de malware que sequestra o acesso aos dados da vítima, geralmente criptografando-os, e exige pagamento de resgate para restabelecer o acesso.",True,"Correto. O ransomware criptografa (ou bloqueia o acesso a) os arquivos da vítima e exige pagamento, geralmente em criptomoedas, para a suposta liberação dos dados.")
ce("PM","Noções de Informática","A autenticação em dois fatores (2FA) aumenta a segurança de uma conta ao exigir, além da senha, uma segunda forma de verificação, como um código enviado ao celular do usuário.",True,"Correto. A autenticação em dois fatores acrescenta uma camada extra de segurança, exigindo, além da senha, uma segunda verificação, como um código temporário ou biometria.")


# =====================================================================
# BMMA — MULTIPLA ESCOLHA (5 alternativas)
# =====================================================================

# ---- Português (BM) ----
mc("BM","Língua Portuguesa","Assinale a alternativa em que o emprego da crase está de acordo com a norma-padrão da língua portuguesa.",
   ["Cheguei à uma hora da tarde no quartel.","Refiro-me à você, soldado.","O bombeiro saiu à procura de vítimas.","Estava à espera dele desde cedo, à noite.","Voltarei à essa cidade em breve."],
   3,"O correto é 'Estava à espera dele desde cedo, à noite', pois há crase antes de 'espera' (locução feminina) e antes de 'noite' (locução adverbial feminina de tempo). Não há crase antes de pronomes como 'você' ou 'essa', nem antes de numeral indicando 'uma hora' no sentido de hora exata sem determinação de lugar específico.")
mc("BM","Língua Portuguesa","Em qual das frases a seguir o verbo 'haver' está empregado de acordo com a norma-padrão, no sentido de existir?",
   ["Haviam muitas vítimas no local do incêndio.","Deve haver, no plantão, ao menos dois bombeiros de prontidão.","Houveram vários chamados durante a noite.","Vão haver novos concursos em breve.","Existe para haver mais equipamentos na unidade."],
   1,"O verbo 'haver', no sentido de existir, é impessoal e deve permanecer sempre na 3ª pessoa do singular: 'Deve haver... dois bombeiros de prontidão' está correto. As demais opções cometem o erro de flexionar 'haver' no plural.")
mc("BM","Língua Portuguesa","Assinale a opção em que a concordância verbal está de acordo com a norma-padrão.",
   ["Fazem dois anos que o bombeiro se formou.","Faz dois anos que o bombeiro se formou.","Fazem-se dois anos desde a formatura.","Houve-se dois anos de formatura.","Vai fazer dois anos, contando com hoje, que se formaram."],
   1,"'Faz dois anos que o bombeiro se formou' está correto, pois o verbo 'fazer', ao indicar tempo decorrido, é impessoal e permanece na 3ª pessoa do singular.")
mc("BM","Língua Portuguesa","Assinale a alternativa em que a vírgula foi empregada corretamente para isolar o aposto explicativo.",
   ["O comandante, Coronel Silva chegou ao local.","O comandante Coronel Silva, chegou ao local.","O comandante, Coronel Silva, chegou ao local.","O, comandante Coronel Silva chegou, ao local.","O comandante Coronel, Silva chegou ao local."],
   2,"O correto é isolar o aposto explicativo entre vírgulas: 'O comandante, Coronel Silva, chegou ao local.'")
mc("BM","Língua Portuguesa","Assinale a alternativa em que o uso do pronome está de acordo com a norma-padrão após preposição.",
   ["Entre eu e ele, não há dúvidas.","Entre mim e ele, não há dúvidas.","Entre mim e ele mesmo, existe dúvida entre nós dois.","Para eu fazer o trabalho, preciso de ajuda.","Isso é para mim fazer."],
   1,"Após preposição, usam-se os pronomes oblíquos tônicos: 'Entre mim e ele' está correto. 'Entre eu' é incorreto, pois pronomes retos não devem ser usados após preposição nessa função.")
mc("BM","Língua Portuguesa","Assinale a opção que apresenta erro de regência verbal em relação à norma-padrão.",
   ["Assistimos ao treinamento com atenção.","Preferimos o treinamento teórico ao prático.","Obedecemos às ordens do comandante.","Chegamos no quartel antes do previsto.","Aspiramos a uma promoção justa."],
   3,"'Chegamos no quartel' apresenta desvio, pois a norma-padrão recomenda a preposição 'a' com o verbo 'chegar', e não 'em': o correto seria 'Chegamos ao quartel'.")
mc("BM","Língua Portuguesa","Assinale a alternativa cuja grafia está correta segundo o Acordo Ortográfico vigente.",
   ["Guarda-noturno","Auto-escola","Ante-sala","Sub-solo","Pre-fixado"],
   0,"'Guarda-noturno' mantém o hífen corretamente, por se tratar de substantivo composto. As demais palavras tiveram o hífen suprimido pelo Acordo Ortográfico: autoescola, antessala, subsolo e pré-fixado (com acento, sem hífen).")
mc("BM","Língua Portuguesa","Assinale a alternativa em que o plural está correto segundo a norma-padrão.",
   ["Os cidadões votaram na eleição.","Os cidadães participaram do evento.","Os cidadãos compareceram ao local.","Os cidadão se reuniram.","Os cidadã se manifestaram."],
   2,"O plural correto de 'cidadão' é 'cidadãos'. As demais formas ('cidadões', 'cidadães') não existem na norma-padrão.")

# ---- História do Maranhão (BM) ----
mc("BM","História do Maranhão","A cidade de São Luís, capital do Maranhão, foi fundada, em 1612, por colonizadores de qual nacionalidade?",
   ["Espanhóis","Holandeses","Franceses","Ingleses","Italianos"],
   2,"São Luís foi fundada em 1612 por colonizadores franceses, liderados por Daniel de La Touche, sendo até hoje a única capital brasileira de origem francesa.")
mc("BM","História do Maranhão","A Balaiada, importante revolta popular ocorrida no Maranhão durante o período regencial, teve início aproximadamente em que ano?",
   ["1808","1822","1838","1889","1930"],
   2,"A Balaiada teve início em 1838, estendendo-se até 1841, sendo uma das maiores revoltas do período regencial brasileiro.")
mc("BM","História do Maranhão","Antes de sua definitiva incorporação ao domínio português, o território do Maranhão também foi disputado por qual outra potência europeia, que chegou a ocupar São Luís entre 1641 e 1644?",
   ["Espanha","Holanda","Inglaterra","Suécia","Bélgica"],
   1,"Os holandeses ocuparam São Luís entre 1641 e 1644, antes de serem expulsos pelos portugueses, que consolidaram definitivamente o domínio lusitano na região.")
mc("BM","História do Maranhão","O Centro Histórico de São Luís é reconhecido internacionalmente por qual título concedido pela UNESCO?",
   ["Reserva da Biosfera","Patrimônio Cultural Imaterial","Patrimônio Mundial (Patrimônio Cultural da Humanidade)","Geoparque Mundial","Cidade Criativa"],
   2,"O Centro Histórico de São Luís foi declarado Patrimônio Cultural da Humanidade (Patrimônio Mundial) pela UNESCO em 1997, principalmente em razão de seu conjunto arquitetônico colonial preservado.")
mc("BM","História do Maranhão","Qual manifestação cultural popular, típica do Maranhão, mescla elementos indígenas, africanos e europeus, sendo reconhecida como Patrimônio Cultural Imaterial do Brasil?",
   ["Boi de Mamão","Bumba Meu Boi","Frevo","Maracatu","Congada"],
   1,"O Bumba Meu Boi é a manifestação cultural popular mais representativa do Maranhão, reconhecida como Patrimônio Cultural Imaterial do Brasil pelo IPHAN."),

# ---- Geografia do Maranhão (BM) ----
mc("BM","Geografia do Maranhão","O Parque Nacional dos Lençóis Maranhenses é caracterizado principalmente pela presença de:",
   ["Cavernas calcárias e rios subterrâneos","Dunas de areia branca entremeadas por lagoas de água doce","Formações de manguezal isoladas do mar","Vulcões extintos e crateras","Florestas de araucária"],
   1,"Os Lençóis Maranhenses são formados por extensas dunas de areia branca, entre as quais se formam lagoas de água da chuva, sobretudo no período chuvoso.")
mc("BM","Geografia do Maranhão","O Delta do Parnaíba, um dos poucos deltas em mar aberto do mundo, está localizado na divisa do Maranhão com qual outro estado?",
   ["Ceará","Pará","Piauí","Tocantins","Bahia"],
   2,"O Delta do Parnaíba está situado na divisa entre os estados do Maranhão e do Piauí, sendo compartilhado por ambos.")
mc("BM","Geografia do Maranhão","Assinale a alternativa que apresenta corretamente rios importantes do território maranhense.",
   ["Amazonas, Negro e Solimões","Itapecuru, Mearim e Pindaré","São Francisco, Parnaíba e Doce","Paraná, Paraguai e Uruguai","Tietê, Piracicaba e Grande"],
   1,"Itapecuru, Mearim e Pindaré estão entre os principais rios que cortam o território do Maranhão, relevantes para o abastecimento e a economia regional.")
mc("BM","Geografia do Maranhão","A capital do Maranhão, São Luís, está localizada:",
   ["No interior do estado, sem acesso direto ao mar","Em uma ilha, banhada pelas baías de São Marcos e de São José","Na fronteira com o estado do Piauí","Às margens exclusivas do rio Amazonas","No topo da Serra da Ibiapaba"],
   1,"São Luís está situada na Ilha do Maranhão, banhada pelas baías de São Marcos e de São José.")
mc("BM","Geografia do Maranhão","Em relação à posição geográfica, o Maranhão é frequentemente descrito como um estado de transição entre quais domínios naturais brasileiros?",
   ["Pampa e Mata Atlântica","Amazônia e Nordeste (Cerrado/Caatinga)","Pantanal e Cerrado","Mata Atlântica e Pampa","Caatinga e Pantanal"],
   1,"Por sua localização, o Maranhão apresenta características de transição entre a paisagem amazônica, ao qual pertence pela Amazônia Legal, e as paisagens do Nordeste, com influências de cerrado e caatinga."),

# ---- Inglês (BM) ----
mc("BM","Língua Estrangeira (Inglês)","Choose the correct translation for: 'The firefighter rescued the child from the burning building.'",
   ["O bombeiro resgatou a criança do prédio em chamas.","O bombeiro apagou o incêndio da criança.","A criança resgatou o bombeiro do prédio.","O prédio resgatou o bombeiro e a criança.","O bombeiro construiu o prédio para a criança."],
   0,"A tradução correta é 'O bombeiro resgatou a criança do prédio em chamas', pois 'rescued' significa 'resgatou' e 'burning building' significa 'prédio em chamas'.")
mc("BM","Língua Estrangeira (Inglês)","Fill in the blank: 'If there ______ a fire, call the emergency number immediately.'",
   ["is","are","was","were","be"],
   0,"A forma correta é 'is', concordando com o sujeito singular 'a fire' em uma oração condicional no presente: 'If there is a fire...'.")
mc("BM","Língua Estrangeira (Inglês)","Assinale a alternativa que apresenta o correto significado da palavra 'emergency' em português.",
   ["Emergência","Emigração","Emprego","Empréstimo","Empenho"],
   0,"'Emergency' significa 'emergência' em português, um falso cognato comum é confundi-la com outras palavras semelhantes, mas seu significado é direto neste caso.")
mc("BM","Língua Estrangeira (Inglês)","Choose the correct form: 'Firefighters ______ trained to respond quickly to emergencies.'",
   ["is","am","are","was","be"],
   2,"O sujeito 'firefighters' está no plural, exigindo o verbo 'to be' na forma 'are': 'Firefighters are trained...'.")
mc("BM","Língua Estrangeira (Inglês)","Qual é o significado da expressão 'first aid' em português?",
   ["Primeira ajuda financeira","Primeiros socorros","Primeira reunião","Primeiro auxílio jurídico","Primeira chamada telefônica"],
   1,"'First aid' significa 'primeiros socorros', a assistência inicial prestada a uma vítima antes do atendimento médico especializado."),

# ---- Raciocínio Lógico (BM) ----
mc("BM","Raciocínio Lógico","A negação da proposição 'Todos os bombeiros usam capacete' é:",
   ["Nenhum bombeiro usa capacete.","Todos os bombeiros não usam capacete.","Algum bombeiro não usa capacete.","Alguns bombeiros usam capacete.","Nenhum bombeiro deixa de usar capacete."],
   2,"A negação de uma proposição universal ('todos...') é uma proposição existencial com o predicado negado: 'algum bombeiro não usa capacete'.")
mc("BM","Raciocínio Lógico","Assinale a alternativa que apresenta a negação correta de 'Se houver incêndio, então a equipe será acionada.'",
   ["Se não houver incêndio, a equipe não será acionada.","Houve incêndio e a equipe não foi acionada.","Não houve incêndio ou a equipe foi acionada.","A equipe será acionada mesmo sem incêndio.","Houve incêndio ou a equipe foi acionada."],
   1,"A negação da condicional 'se p então q' é 'p e não q': 'houve incêndio e a equipe não foi acionada'.")
mc("BM","Raciocínio Lógico","Em uma tabela-verdade, quando a disjunção 'p ou q' é falsa, pode-se concluir corretamente que:",
   ["p é verdadeira e q é falsa.","p é falsa e q é verdadeira.","p e q são ambas verdadeiras.","p e q são ambas falsas.","é impossível determinar os valores de p e q."],
   3,"A disjunção inclusiva 'p ou q' só é falsa quando ambas as proposições, p e q, forem falsas simultaneamente.")
mc("BM","Raciocínio Lógico","Considere a sequência: 5, 10, 20, 40, 80. O próximo número da sequência é:",
   ["100","120","140","160","200"],
   3,"A sequência é uma progressão geométrica de razão 2 (cada termo é o dobro do anterior): 80 × 2 = 160.")
mc("BM","Raciocínio Lógico","Em um grupo de 40 bombeiros, 25 sabem realizar reanimação cardiopulmonar (RCP) e 20 sabem operar motobomba, havendo 10 que sabem realizar ambas as atividades. Quantos bombeiros sabem realizar pelo menos uma dessas atividades?",
   ["25","30","35","40","45"],
   2,"Pelo princípio da inclusão-exclusão: 25 + 20 − 10 = 35 bombeiros sabem realizar pelo menos uma das duas atividades."),

# ---- Legislação Institucional BM (BM) ----
mc("BM","Legislação Institucional","A hierarquia e a disciplina, no âmbito dos corpos de bombeiros militares estaduais, constituem, segundo a Constituição Federal, a base institucional da corporação, da mesma forma como ocorre em relação:",
   ["Apenas às polícias civis","Às Forças Armadas e às polícias militares","Exclusivamente à Marinha do Brasil","Às guardas municipais","Aos órgãos do Poder Judiciário"],
   1,"Nos termos do art. 42 c/c art. 144, §6º, da Constituição Federal, os militares dos Estados (polícias militares e corpos de bombeiros militares) organizam-se com base na hierarquia e disciplina, nos mesmos moldes das Forças Armadas.")
mc("BM","Legislação Institucional","Assinale a alternativa correta acerca da diferença entre crime militar e transgressão disciplinar.",
   ["Ambos são apurados exclusivamente pela Justiça Militar.","O crime militar é apurado pela Justiça Militar; a transgressão disciplinar, em âmbito administrativo interno da corporação.","A transgressão disciplinar é sempre mais grave que o crime militar.","Não existe distinção entre os dois institutos no direito militar.","Somente o crime militar exige respeito ao contraditório e à ampla defesa."],
   1,"O crime militar é apurado e julgado pela Justiça Militar, enquanto a transgressão disciplinar é apurada por procedimento administrativo (sindicância ou PAD) no âmbito da própria corporação, respeitados o contraditório e a ampla defesa em ambos os casos.")
mc("BM","Legislação Institucional","Em relação ao dever de obediência hierárquica no âmbito militar, é correto afirmar que:",
   ["É absoluto, não comportando qualquer exceção.","Não existe, cabendo ao subordinado decidir livremente se cumpre ou não as ordens recebidas.","Não se aplica a ordens manifestamente ilegais ou que configurem crime.","Aplica-se apenas às ordens escritas.","Só vincula os oficiais, e não as praças."],
   2,"O dever de obediência não é absoluto: o subordinado não deve cumprir ordens manifestamente ilegais ou que configurem crime, hipótese em que o superior responderá pelo ato ordenado.")
mc("BM","Legislação Institucional","Segundo a Constituição Federal, compete aos corpos de bombeiros militares, além de outras atribuições definidas em lei, principalmente:",
   ["A execução de atividades de defesa civil, prevenção e combate a incêndios","O policiamento ostensivo e a preservação da ordem pública, com exclusividade","A investigação de infrações penais comuns","A fiscalização eleitoral","A guarda externa de estabelecimentos penais, com exclusividade"],
   0,"Conforme o art. 144, §5º, da CF, cabe aos corpos de bombeiros militares, além das atribuições definidas em lei, a execução de atividades de defesa civil, prevenção e combate a incêndios.")
mc("BM","Legislação Institucional","No que se refere à acumulação de cargos públicos pelo militar estadual em atividade, é correto afirmar que:",
   ["É livremente permitida, sem qualquer restrição.","É vedada, em regra, ressalvadas as exceções constitucionalmente previstas, como a de um cargo de professor combinado com outro técnico ou científico.","É permitida apenas para cargos de natureza militar.","É vedada de forma absoluta, sem qualquer exceção.","Depende exclusivamente de autorização do comandante imediato, independentemente da Constituição."],
   1,"Aplica-se, por simetria, a regra geral de vedação à acumulação de cargos públicos (art. 37, XVI e XVII, CF), ressalvadas as exceções nela previstas."),

# ---- Primeiros Socorros (BM) ----
mc("BM","Noções de Primeiros Socorros","Na avaliação inicial de uma vítima inconsciente, a sequência do suporte básico de vida (ABC) prioriza, nessa ordem:",
   ["Circulação, respiração, vias aéreas","Vias aéreas, respiração, circulação","Respiração, circulação, vias aéreas","Circulação, vias aéreas, respiração","Vias aéreas, circulação, respiração"],
   1,"A sequência clássica do ABC do suporte básico de vida prioriza: A (vias Aéreas), B (Boa respiração) e C (Circulação), nessa ordem.")
mc("BM","Noções de Primeiros Socorros","Em caso de hemorragia externa intensa em um membro, a primeira conduta recomendada é:",
   ["Aplicar torniquete imediatamente, antes de qualquer outra medida","Aplicar pressão direta firme sobre o ferimento com um pano limpo","Elevar o membro sem realizar qualquer outra medida","Aguardar a chegada do socorro sem intervir","Aplicar gelo diretamente sobre o ferimento aberto"],
   1,"A conduta inicial recomendada em hemorragias externas é a aplicação de pressão direta firme sobre o ferimento, reservando-se o torniquete para casos de hemorragia grave não controlada por outros meios.")
mc("BM","Noções de Primeiros Socorros","Em uma parada cardiorrespiratória em adulto, a proporção recomendada de compressões torácicas para ventilações, durante a reanimação cardiopulmonar (RCP) realizada por um único socorrista leigo, é geralmente de:",
   ["15 compressões para 2 ventilações","30 compressões para 2 ventilações","5 compressões para 1 ventilação","10 compressões para 1 ventilação","50 compressões para 5 ventilações"],
   1,"A proporção amplamente recomendada em diretrizes de RCP para socorristas é de 30 compressões torácicas para 2 ventilações, em ciclos sucessivos.")
mc("BM","Noções de Primeiros Socorros","Diante de uma vítima com suspeita de fratura em membro, a conduta correta de primeiros socorros é:",
   ["Tentar recolocar o osso na posição normal antes de imobilizar","Imobilizar o membro na posição em que foi encontrado, sem tentar realinhá-lo","Massagear a região para aliviar a dor","Movimentar bastante o membro para verificar a extensão da lesão","Aplicar calor intenso diretamente sobre a fratura"],
   1,"A conduta correta é imobilizar o membro na posição encontrada, evitando movimentações desnecessárias e tentativas de realinhamento, que podem agravar a lesão.")
mc("BM","Noções de Primeiros Socorros","Em vítimas de queimaduras, uma das condutas iniciais recomendadas é:",
   ["Aplicar pasta de dente ou manteiga sobre a área queimada","Resfriar a área queimada com água corrente em temperatura ambiente, por alguns minutos","Estourar imediatamente todas as bolhas formadas","Remover a pele já destacada com as mãos","Aplicar gelo diretamente sobre a queimadura"],
   1,"Resfriar a área queimada com água corrente em temperatura ambiente por alguns minutos é uma conduta inicial recomendada; substâncias caseiras como pasta de dente ou manteiga são contraindicadas."),

# ---- Combate a Incêndio (BM) ----
mc("BM","Noções de Combate a Incêndio","O chamado 'triângulo do fogo' é formado pelos seguintes elementos essenciais para a ocorrência da combustão:",
   ["Água, oxigênio e calor","Combustível, comburente (oxigênio) e calor","Fumaça, calor e combustível","Comburente, água e fumaça","Calor, fumaça e vento"],
   1,"O triângulo do fogo é formado por combustível, comburente (geralmente o oxigênio) e calor; a ausência de qualquer um desses elementos impede ou extingue a combustão.")
mc("BM","Noções de Combate a Incêndio","Segundo a classificação usual de incêndios, o incêndio classe B refere-se a fogo envolvendo:",
   ["Materiais combustíveis comuns, como madeira e papel","Líquidos e gases inflamáveis","Equipamentos elétricos energizados","Metais combustíveis, como magnésio e sódio","Óleos e gorduras de cozinha em equipamentos de cocção"],
   1,"O incêndio classe B envolve líquidos e gases inflamáveis, como gasolina, óleo e GLP.")
mc("BM","Noções de Combate a Incêndio","Em incêndios envolvendo equipamentos elétricos energizados (classe C), deve-se evitar, sobretudo, o uso de:",
   ["Extintor de CO2 (gás carbônico)","Extintor de pó químico seco","Água em jato direto sobre o equipamento energizado","Extintor à base de espuma mecânica de água","Cobertor corta-fogo, quando aplicável"],
   2,"Deve-se evitar água em jato direto sobre equipamentos elétricos energizados, pela condutividade elétrica da água, que pode causar choque; recomenda-se, nesses casos, o uso de extintores como CO2 ou pó químico seco.")
mc("BM","Noções de Combate a Incêndio","Assinale a alternativa que indica corretamente a classe de incêndio associada a metais combustíveis, como magnésio, titânio e sódio.",
   ["Classe A","Classe B","Classe C","Classe D","Classe K"],
   3,"A classe D de incêndio refere-se a metais combustíveis, como magnésio, titânio, sódio e potássio, que exigem agentes extintores específicos.")
mc("BM","Noções de Combate a Incêndio","O extintor de incêndio à base de água pressurizada é indicado, principalmente, para incêndios da classe:",
   ["Classe A (materiais combustíveis comuns)","Classe B (líquidos inflamáveis)","Classe C (equipamentos elétricos energizados)","Classe D (metais combustíveis)","Classe K (óleos e gorduras de cozinha)"],
   0,"O extintor de água pressurizada é indicado, principalmente, para incêndios classe A (materiais combustíveis comuns, como madeira, papel e tecido), não sendo indicado para incêndios elétricos ou com líquidos inflamáveis."),

# ---- Segurança Contra Incêndio e Pânico (BM) ----
mc("BM","Segurança Contra Incêndio e Pânico","As rotas de fuga em edificações devem ser projetadas, entre outros critérios, para garantir:",
   ["O menor número possível de saídas, para facilitar o controle de acesso","Caminhos desobstruídos e sinalizados até um local seguro, em tempo hábil","Passagem exclusiva pelos elevadores do prédio","Uso obrigatório de escadas rolantes como via de escape","Concentração de todas as saídas em um único ponto do edifício"],
   1,"As rotas de fuga devem proporcionar caminhos desobstruídos, sinalizados e dimensionados adequadamente, permitindo que os ocupantes alcancem um local seguro em tempo hábil, em caso de emergência.")
mc("BM","Segurança Contra Incêndio e Pânico","Os sistemas de detecção e alarme de incêndio têm como finalidade principal:",
   ["Extinguir automaticamente o fogo assim que detectado","Detectar precocemente princípios de incêndio e alertar os ocupantes da edificação","Substituir integralmente a necessidade de rotas de fuga","Servir apenas como item decorativo em edificações antigas","Funcionar exclusivamente durante inspeções do Corpo de Bombeiros"],
   1,"Os sistemas de detecção e alarme têm por finalidade identificar precocemente um princípio de incêndio e alertar os ocupantes, permitindo o acionamento tempestivo da evacuação e do combate ao fogo.")
mc("BM","Segurança Contra Incêndio e Pânico","Em edificações, o Auto de Vistoria do Corpo de Bombeiros (AVCB), ou documento equivalente, tem por finalidade principal:",
   ["Substituir o alvará de funcionamento municipal","Atestar que a edificação atende às exigências de segurança contra incêndio e pânico previstas na legislação","Autorizar exclusivamente a instalação elétrica do imóvel","Certificar a qualidade estrutural do concreto utilizado na construção","Dispensar a edificação de manutenção de extintores"],
   1,"O AVCB (ou documento equivalente) atesta que a edificação atende às normas e exigências de segurança contra incêndio e pânico estabelecidas pela legislação e pelo Corpo de Bombeiros.")
mc("BM","Segurança Contra Incêndio e Pânico","A sinalização de emergência (placas indicativas de saída, extintores, entre outras) deve, de modo geral, seguir um padrão de cores; a cor predominantemente associada a extintores e equipamentos de combate a incêndio é:",
   ["Azul","Amarelo","Vermelho","Verde","Branco"],
   2,"A cor vermelha é tradicionalmente associada a equipamentos de combate a incêndio, como extintores e hidrantes, na sinalização de segurança.")
mc("BM","Segurança Contra Incêndio e Pânico","A carga de incêndio de uma edificação está relacionada, principalmente:",
   ["À quantidade de energia térmica que pode ser liberada pela combustão dos materiais existentes na edificação","Ao número de extintores instalados no local","À cor da fachada do edifício","Ao número de pavimentos da edificação, exclusivamente","À quantidade de janelas existentes no prédio"],
   0,"A carga de incêndio refere-se à quantidade de energia térmica (calor) que pode ser liberada pela combustão de todos os materiais combustíveis existentes em determinado ambiente ou edificação, sendo um parâmetro relevante para o dimensionamento de medidas de segurança.")

# =====================================================================
# PCMA — MULTIPLA ESCOLHA (5 alternativas)
# =====================================================================

# ---- Português (PC) ----
mc("PC","Língua Portuguesa","Assinale a alternativa em que a regência verbal está de acordo com a norma-padrão.",
   ["O delegado assistiu ao interrogatório com atenção.","O investigador chegou no local do crime rapidamente.","A vítima aspirava ser ouvida em juízo, sem citar a preposição adequada.","O escrivão implicou em atraso na entrega do laudo.","O perito preferiu mais a perícia do que o depoimento."],
   0,"'Assistiu ao interrogatório' está correto, pois 'assistir' no sentido de presenciar é transitivo indireto, regendo-se com a preposição 'a'.")
mc("PC","Língua Portuguesa","Assinale a alternativa em que o uso da crase está correto.",
   ["Entreguei o laudo à ela.","Vou às 14 horas à delegacia.","Refiro-me à Vossa Excelência, sem o artigo.","Cheguei à uma hora exata da madrugada.","Estava à disposição desde cedo."],
   4,"'Estava à disposição desde cedo' está correto, pois há crase diante de locução feminina ('à disposição'). Não há crase antes de pronomes pessoais ('ela') nem, em regra, antes de 'Vossa Excelência'.")
mc("PC","Língua Portuguesa","No que se refere à concordância verbal, assinale a alternativa correta.",
   ["Fazem cinco anos que o inquérito foi arquivado.","Faz cinco anos que o inquérito foi arquivado.","Houveram cinco anos de investigação.","Devem haver novos indícios no processo.","Vão fazer cinco anos, apurados de forma plural."],
   1,"'Faz cinco anos que o inquérito foi arquivado' está correto, pois 'fazer', indicando tempo decorrido, é impessoal e permanece no singular.")
mc("PC","Língua Portuguesa","Assinale a alternativa em que o emprego da vírgula está de acordo com a norma-padrão para isolar o aposto explicativo.",
   ["O delegado, Doutor Marcos conduziu o interrogatório.","O delegado Doutor Marcos, conduziu o interrogatório.","O delegado, Doutor Marcos, conduziu o interrogatório.","O, delegado Doutor Marcos conduziu, o interrogatório.","O delegado Doutor, Marcos conduziu o interrogatório."],
   2,"O aposto explicativo deve ser isolado por vírgulas: 'O delegado, Doutor Marcos, conduziu o interrogatório.'"),

# ---- Informática (PC) ----
mc("PC","Noções de Informática","Assinale a alternativa correta a respeito do protocolo HTTPS.",
   ["Não utiliza qualquer tipo de criptografia na comunicação.","Utiliza criptografia (via TLS/SSL) para proteger a comunicação entre navegador e servidor.","É utilizado exclusivamente para transferência de arquivos por FTP.","Substitui integralmente a necessidade de firewall em qualquer rede.","É um protocolo de correio eletrônico."],
   1,"O HTTPS utiliza criptografia via TLS/SSL para proteger a confidencialidade e integridade da comunicação entre navegador e servidor.")
mc("PC","Noções de Informática","Em relação a backups, assinale a alternativa correta sobre o backup incremental.",
   ["Copia sempre todos os arquivos do sistema, independentemente de alterações.","Copia apenas os arquivos alterados desde o último backup, seja completo ou incremental.","É sempre mais lento que o backup completo.","Não pode ser usado em conjunto com backups completos.","Elimina a necessidade de qualquer outro tipo de backup."],
   1,"O backup incremental copia apenas os dados alterados desde o último backup de qualquer tipo, tornando o processo mais rápido e econômico em espaço de armazenamento.")
mc("PC","Noções de Informática","Assinale a alternativa que descreve corretamente o conceito de phishing.",
   ["Técnica de criptografia utilizada para proteger senhas.","Fraude eletrônica que busca enganar o usuário para obter dados sigilosos, geralmente por mensagens ou sites falsos.","Tipo de backup incremental de dados.","Protocolo de segurança utilizado em redes corporativas.","Sistema de arquivos utilizado por servidores Linux."],
   1,"Phishing é uma fraude eletrônica em que o golpista se passa por uma instituição confiável para induzir a vítima a fornecer dados sigilosos, como senhas e dados bancários.")
mc("PC","Noções de Informática","Assinale a alternativa correta a respeito de um firewall.",
   ["Tem como função exclusiva remover vírus já instalados no sistema.","Atua controlando e filtrando o tráfego de entrada e saída de uma rede.","É sinônimo de antivírus.","Substitui integralmente a necessidade de senhas de acesso.","É utilizado apenas em redes sem fio (Wi-Fi)."],
   1,"O firewall atua controlando e filtrando o tráfego de rede (entrada e saída), sendo distinto do antivírus, que tem a função de detectar e remover softwares maliciosos."),

# ---- Raciocínio Lógico (PC) ----
mc("PC","Raciocínio Lógico","A negação da proposição 'Todos os inquéritos foram concluídos no prazo' é:",
   ["Nenhum inquérito foi concluído no prazo.","Algum inquérito não foi concluído no prazo.","Todos os inquéritos não foram concluídos no prazo.","Alguns inquéritos foram concluídos no prazo.","Nenhum inquérito deixou de ser concluído no prazo."],
   1,"A negação de uma proposição universal é uma proposição existencial com o predicado negado: 'algum inquérito não foi concluído no prazo'.")
mc("PC","Raciocínio Lógico","Considerando a condicional 'Se houver indícios suficientes, então o inquérito será instaurado', assinale a negação correta dessa proposição.",
   ["Não há indícios suficientes e o inquérito não será instaurado.","Há indícios suficientes e o inquérito não será instaurado.","Não há indícios suficientes ou o inquérito será instaurado.","O inquérito será instaurado, mesmo sem indícios suficientes.","Há indícios suficientes ou o inquérito será instaurado."],
   1,"A negação da condicional 'se p então q' é 'p e não q': 'há indícios suficientes e o inquérito não será instaurado'.")
mc("PC","Raciocínio Lógico","Pela Lei de De Morgan, a negação da proposição composta 'p e q' equivale a:",
   ["não p e não q","não p ou não q","p ou q","p e não q","não p e q"],
   1,"Pela Lei de De Morgan, 'não (p e q)' equivale a 'não p ou não q', trocando-se o conectivo 'e' pelo 'ou' ao negar.")
mc("PC","Raciocínio Lógico","Em um grupo de 50 policiais civis, 30 atuam em investigação e 25 atuam em atendimento ao público, havendo 12 que atuam em ambas as atividades. O número de policiais que atuam em pelo menos uma dessas atividades é:",
   ["30","37","43","45","50"],
   2,"Pelo princípio da inclusão-exclusão: 30 + 25 − 12 = 43 policiais atuam em pelo menos uma das duas atividades."),

# ---- Direito Constitucional (PC) ----
mc("PC","Direito Constitucional","Nos termos da Constituição Federal, compete às polícias civis, dirigidas por delegados de polícia de carreira, ressalvada a competência da União:",
   ["O policiamento ostensivo e a preservação da ordem pública.","As funções de polícia judiciária e a apuração de infrações penais, exceto as militares.","A segurança viária, com exclusividade sobre as demais forças.","A defesa civil e o combate a incêndios.","A guarda externa de estabelecimentos penais, com exclusividade."],
   1,"Conforme o art. 144, §4º, da CF, às polícias civis cabem as funções de polícia judiciária e a apuração de infrações penais, exceto as militares, ressalvada a competência da União.")
mc("PC","Direito Constitucional","Assinale a alternativa correta a respeito do remédio constitucional cabível para proteger a liberdade de locomoção contra ilegalidade ou abuso de poder.",
   ["Mandado de segurança","Habeas data","Habeas corpus","Ação popular","Mandado de injunção"],
   2,"O habeas corpus, previsto no art. 5º, LXVIII, da CF, é o remédio constitucional cabível sempre que alguém sofrer ou se achar ameaçado de sofrer violência ou coação em sua liberdade de locomoção.")
mc("PC","Direito Constitucional","Em relação ao mandado de segurança, é correto afirmar que se trata de instrumento residual, cabível para proteger direito líquido e certo:",
   ["Ainda que amparável por habeas corpus ou habeas data.","Não amparado por habeas corpus nem por habeas data.","Exclusivamente em matéria eleitoral.","Apenas contra atos de particulares.","Somente após o trânsito em julgado da ação principal."],
   1,"O mandado de segurança é residual: protege direito líquido e certo não amparado por habeas corpus (liberdade de locomoção) nem por habeas data (acesso/retificação de dados), conforme art. 5º, LXIX, da CF.")
mc("PC","Direito Constitucional","O direito de reunião pacífica, sem armas, previsto na Constituição Federal, exige do interessado, em regra:",
   ["Autorização prévia da autoridade competente.","Apenas prévio aviso à autoridade competente, sem necessidade de autorização.","Autorização judicial específica para cada reunião.","Anuência da maioria dos moradores do local.","Registro em cartório com trinta dias de antecedência."],
   1,"Conforme o art. 5º, XVI, da CF, o direito de reunião pacífica e sem armas independe de autorização, exigindo-se apenas prévio aviso à autoridade competente.")
mc("PC","Direito Constitucional","Assinale a alternativa correta acerca dos direitos fundamentais previstos na Constituição Federal de 1988.",
   ["São normas de eficácia limitada, sem qualquer aplicabilidade imediata.","Possuem, em regra, aplicabilidade imediata, conforme o §1º do art. 5º da CF.","Podem ser suprimidos por simples lei ordinária.","Aplicam-se exclusivamente a cidadãos brasileiros natos.","Não podem ser objeto de restrições, ainda que proporcionais e previstas em lei."],
   1,"Nos termos do art. 5º, §1º, da CF, as normas definidoras de direitos e garantias fundamentais têm aplicação imediata, muito embora, em certos casos, admitam restrições proporcionais previstas na própria Constituição ou em lei."),

# ---- Direito Administrativo (PC) ----
mc("PC","Direito Administrativo","O princípio da autotutela administrativa permite que a Administração Pública:",
   ["Anule seus próprios atos ilegais e revogue os inconvenientes ou inoportunos, sem necessidade de intervenção judicial.","Aja livremente, sem qualquer controle, inclusive quanto à legalidade de seus atos.","Delegue integralmente suas funções fiscalizatórias a particulares.","Anule atos de outros entes federativos sem processo específico.","Revogue atos legais praticados por particulares, independentemente de qualquer procedimento."],
   0,"Pela autotutela, a Administração pode anular seus atos ilegais (Súmula 473 do STF) e revogar os inconvenientes ou inoportunos, respeitados direitos adquiridos, sem necessidade de intervenção judicial.")
mc("PC","Direito Administrativo","Em relação ao controle judicial dos atos administrativos discricionários, é correto afirmar que o Poder Judiciário:",
   ["Pode substituir livremente o juízo de conveniência e oportunidade do administrador.","Não pode controlar a legalidade desses atos em hipótese alguma.","Pode controlar a legalidade do ato, mas não o mérito administrativo (conveniência e oportunidade).","Somente pode atuar mediante prévia autorização do Poder Executivo.","Está impedido de analisar desvio de finalidade em atos discricionários."],
   2,"O Judiciário não pode substituir o juízo de conveniência e oportunidade (mérito) do administrador, mas pode controlar a legalidade do ato discricionário, inclusive quanto a competência, forma, finalidade e limites da discricionariedade.")
mc("PC","Direito Administrativo","Segundo o princípio da continuidade do serviço público, é correto afirmar que a interrupção do serviço:",
   ["É absolutamente vedada em qualquer hipótese.","Pode ocorrer em situações de emergência, por razões técnicas ou de segurança das instalações, ou por inadimplemento do usuário após aviso prévio.","Somente pode ocorrer por decisão do Poder Legislativo.","É permitida exclusivamente para empresas privadas concessionárias.","Depende sempre de autorização judicial prévia."],
   1,"A legislação (como a Lei 8.987/1995) admite a interrupção do serviço em situações de emergência, por razões técnicas, de segurança das instalações, ou por inadimplemento do usuário, após aviso prévio, não se tratando de vedação absoluta.")
mc("PC","Direito Administrativo","Assinale a alternativa que apresenta corretamente um dos atributos dos atos administrativos.",
   ["Irretratabilidade absoluta, mesmo diante de vícios de legalidade.","Autoexecutoriedade, que permite a execução do ato pela própria Administração, sem necessidade de prévia intervenção judicial, nos casos previstos em lei.","Impossibilidade de revogação em qualquer hipótese.","Necessidade de aprovação do Poder Judiciário antes de sua produção de efeitos.","Vinculação obrigatória à vontade do particular destinatário do ato."],
   1,"A autoexecutoriedade é um dos atributos dos atos administrativos, permitindo, nos casos previstos em lei, que a própria Administração execute suas decisões sem necessidade de prévia intervenção do Poder Judiciário.")
mc("PC","Direito Administrativo","Em relação aos princípios expressos da Administração Pública previstos no art. 37, caput, da Constituição Federal, assinale a alternativa que os enumera corretamente.",
   ["Legalidade, impessoalidade, moralidade, publicidade e eficiência.","Legalidade, hierarquia, moralidade, publicidade e razoabilidade.","Impessoalidade, proporcionalidade, publicidade, eficiência e segurança jurídica.","Legalidade, moralidade, eficiência, continuidade e supremacia.","Publicidade, eficiência, hierarquia, disciplina e moralidade."],
   0,"O art. 37, caput, da CF elenca expressamente os princípios da legalidade, impessoalidade, moralidade, publicidade e eficiência (conhecidos pelo mnemônico LIMPE)."),

# ---- Direito Penal (PC) ----
mc("PC","Direito Penal","Em relação ao tempo do crime, o Código Penal brasileiro adotou a teoria:",
   ["Do resultado, considerando praticado o crime no momento da consumação.","Da atividade, considerando praticado o crime no momento da ação ou omissão, ainda que outro seja o momento do resultado.","Mista, sem critério definido.","Da ubiquidade, exclusivamente.","Da territorialidade absoluta."],
   1,"O art. 4º do Código Penal adota a teoria da atividade: reputa-se praticado o crime no momento da conduta (ação ou omissão), ainda que outro seja o momento do resultado.")
mc("PC","Direito Penal","Quanto à aplicação da lei penal no espaço, o Brasil adotou, como regra geral, a teoria da:",
   ["Territorialidade absoluta, sem qualquer exceção.","Territorialidade temperada (mitigada), com hipóteses de extraterritorialidade previstas em lei.","Extraterritorialidade absoluta.","Personalidade ativa exclusiva.","Universalidade irrestrita."],
   1,"O Brasil adota a territorialidade temperada: aplica-se a lei brasileira aos crimes no território nacional, sem prejuízo de convenções, tratados e hipóteses de extraterritorialidade previstas no art. 7º do CP.")
mc("PC","Direito Penal","Assinale a alternativa que define corretamente a legítima defesa, segundo o Código Penal.",
   ["Uso de qualquer meio para repelir agressão futura e incerta.","Repelir, usando moderadamente os meios necessários, agressão injusta, atual ou iminente, a direito próprio ou alheio.","Reação desproporcional a qualquer ofensa, ainda que já cessada.","Excludente aplicável apenas a agentes públicos.","Conduta que exige autorização judicial prévia para sua configuração."],
   1,"Segundo o art. 25 do CP, considera-se em legítima defesa quem, usando moderadamente dos meios necessários, repele injusta agressão, atual ou iminente, a direito seu ou de outrem.")
mc("PC","Direito Penal","Em relação ao erro de tipo, é correto afirmar que:",
   ["Quando inevitável, exclui o dolo e a culpa.","Quando evitável, exclui tanto o dolo quanto a culpa.","Sempre isenta o agente de qualquer responsabilidade penal, seja evitável ou não.","Aplica-se apenas a crimes culposos.","Não é previsto no ordenamento jurídico brasileiro."],
   0,"Conforme o art. 20 do CP, o erro de tipo essencial inevitável exclui dolo e culpa; se evitável, exclui apenas o dolo, permitindo a punição por culpa, se prevista em lei.")
mc("PC","Direito Penal","Assinale a alternativa correta sobre a diferença entre dolo direto e dolo eventual.",
   ["No dolo direto, o agente quer o resultado; no dolo eventual, assume o risco de produzi-lo.","No dolo eventual, o agente sempre deseja o resultado.","Dolo direto e dolo eventual são sinônimos no Código Penal.","O dolo eventual exclui a responsabilidade penal do agente.","O dolo direto somente se aplica a crimes culposos."],
   0,"No dolo direto, o agente quer diretamente o resultado; no dolo eventual, ele não deseja diretamente o resultado, mas assume o risco de produzi-lo, conforme a teoria adotada pelo Código Penal (art. 18, I)."),

# ---- Processo Penal (PC) ----
mc("PC","Direito Processual Penal","Em relação à natureza do inquérito policial, é correto afirmar que:",
   ["É procedimento judicial, sujeito a contraditório pleno desde o início.","É procedimento administrativo, de natureza inquisitorial, que dispensa, em regra, o contraditório pleno em sua fase investigativa.","Substitui integralmente a ação penal.","É de responsabilidade exclusiva do Ministério Público.","Não pode ser instaurado de ofício pela autoridade policial."],
   1,"O inquérito policial é procedimento administrativo preparatório da ação penal, de natureza predominantemente inquisitorial, não se exigindo, como regra, o contraditório pleno nessa fase.")
mc("PC","Direito Processual Penal","Segundo o Código de Processo Penal, a prisão em flagrante delito, no que se refere às pessoas que podem efetuá-la, é classificada como:",
   ["Facultativa para qualquer pessoa do povo e obrigatória para as autoridades policiais e seus agentes.","Obrigatória apenas para o Ministério Público.","Facultativa apenas para autoridades policiais.","Vedada a qualquer pessoa que não seja policial.","Exclusiva de autoridade judiciária."],
   0,"Conforme art. 301 do CPP, qualquer do povo poderá (flagrante facultativo) e as autoridades policiais e seus agentes deverão (flagrante obrigatório) prender quem for encontrado em flagrante delito.")
mc("PC","Direito Processual Penal","Desde a entrada em vigor da Lei nº 13.964/2019 (Pacote Anticrime), é correto afirmar, quanto à prisão preventiva, que:",
   ["Pode ser decretada de ofício pelo juiz, a qualquer tempo.","Somente pode ser decretada mediante requerimento das partes ou representação da autoridade policial, sendo vedada a decretação de ofício.","Foi extinta do ordenamento jurídico brasileiro.","Depende exclusivamente de decisão do Ministério Público, sem participação do juiz.","Pode ser decretada sem qualquer fundamentação, a critério do julgador."],
   1,"Desde a Lei 13.964/2019, o juiz não pode mais decretar a prisão preventiva de ofício, dependendo de requerimento do Ministério Público, do querelante, do assistente, ou de representação da autoridade policial (art. 311 do CPP).")
mc("PC","Direito Processual Penal","Assinale a alternativa que indica corretamente o remédio constitucional cabível contra ilegalidade ou abuso de poder que restrinja a liberdade de locomoção de alguém.",
   ["Mandado de segurança","Habeas data","Habeas corpus","Recurso ordinário constitucional, exclusivamente","Ação civil pública"],
   2,"O habeas corpus é o remédio constitucional cabível sempre que alguém sofrer ou se achar ameaçado de sofrer violência ou coação em sua liberdade de locomoção, por ilegalidade ou abuso de poder (art. 5º, LXVIII, CF)."),

# ---- Direitos Humanos (PC) ----
mc("PC","Direitos Humanos","Assinale a alternativa correta acerca da Declaração Universal dos Direitos Humanos, de 1948.",
   ["Tem força de tratado internacional vinculante por si só, com aplicação obrigatória imediata em todos os países.","Tem caráter de recomendação (resolução da Assembleia Geral da ONU), embora tenha inspirado diversos tratados internacionais posteriores.","Foi revogada pela Convenção Americana de Direitos Humanos.","Aplica-se exclusivamente aos Estados membros do Conselho de Segurança da ONU.","Não trata de direitos civis e políticos, apenas de direitos sociais."],
   1,"A Declaração de 1948 foi aprovada como resolução da Assembleia Geral da ONU, com força moral e política, servindo de base para tratados internacionais posteriores, que geram, esses sim, obrigações jurídicas vinculantes.")
mc("PC","Direitos Humanos","Em relação ao uso da força por agentes de segurança pública, segundo princípios amplamente reconhecidos de direitos humanos, deve-se observar, entre outros, os critérios de:",
   ["Discricionariedade irrestrita e sigilo absoluto.","Legalidade, necessidade, proporcionalidade e moderação.","Celeridade, sem necessidade de qualquer proporcionalidade.","Exclusividade da força letal em qualquer abordagem.","Ausência de qualquer controle posterior sobre o uso da força."],
   1,"Esses são os critérios centrais reconhecidos por diretrizes internacionais (como os Princípios Básicos da ONU sobre o Uso da Força) e pela doutrina nacional sobre a atuação de agentes de segurança pública.")
mc("PC","Direitos Humanos","Sobre a proibição da tortura no ordenamento jurídico brasileiro e nos tratados internacionais, é correto afirmar que se trata de:",
   ["Proibição relativa, admitindo exceções em situações de guerra ou emergência.","Proibição absoluta, sem qualquer relativização, mesmo em situações excepcionais.","Conduta permitida quando autorizada por autoridade judicial.","Prática permitida em investigações de crimes graves, mediante autorização do Ministério Público.","Vedação aplicável apenas a agentes públicos civis, não a militares."],
   1,"A proibição da tortura é considerada norma de caráter absoluto (jus cogens), sem exceções, conforme a Convenção contra a Tortura da ONU, a Convenção Americana de Direitos Humanos e a Constituição Federal (art. 5º, III)."),

# ---- Medicina Legal (PC) ----
mc("PC","Medicina Legal","Na tanatologia forense, o conjunto de fenômenos que ocorrem no corpo após a morte, como o resfriamento cadavérico, a rigidez cadavérica e a livididade, é conhecido como:",
   ["Fenômenos vitais","Fenômenos cadavéricos (ou tanatognomônicos)","Fenômenos transformativos exclusivamente","Fenômenos de sobrevivência","Fenômenos agônicos"],
   1,"Os fenômenos cadavéricos (também chamados abióticos ou tanatognomônicos) incluem o resfriamento, a rigidez e a livididade cadavérica, entre outros sinais que se manifestam após a morte.")
mc("PC","Medicina Legal","A rigidez cadavérica, um dos fenômenos abióticos consecutivos à morte, caracteriza-se por:",
   ["Amolecimento progressivo da musculatura logo após a morte.","Enrijecimento da musculatura do corpo, que se instala e depois se dissipa em um período determinado.","Fenômeno que ocorre apenas em mortes violentas.","Ausência total de alterações musculares após a morte.","Processo que ocorre exclusivamente em climas frios."],
   1,"A rigidez cadavérica (rigor mortis) é caracterizada pelo enrijecimento progressivo da musculatura corporal após a morte, instalando-se e posteriormente se dissipando dentro de um período relativamente previsível.")
mc("PC","Medicina Legal","Na classificação das lesões corporais previstas no Código Penal, a lesão corporal é considerada grave quando, entre outras hipóteses, resulta em:",
   ["Simples dor sem qualquer outra consequência.","Incapacidade para as ocupações habituais por mais de trinta dias.","Equimose de pequena extensão.","Mero desconforto emocional passageiro.","Qualquer arranhão superficial na pele."],
   1,"Entre as hipóteses de lesão corporal grave previstas no art. 129, §1º, do Código Penal, está a incapacidade para as ocupações habituais por mais de trinta dias."),

# ---- Criminologia (PC) ----
mc("PC","Criminologia","A Escola Clássica da Criminologia, influenciada pelo Iluminismo, caracteriza-se, entre outros aspectos, por:",
   ["Defender o livre-arbítrio do indivíduo e a proporcionalidade entre crime e pena.","Considerar o crime resultado exclusivo de fatores biológicos hereditários.","Negar qualquer responsabilidade individual pelo ato criminoso.","Defender penas arbitrárias, sem qualquer critério de proporcionalidade.","Ser posterior, cronologicamente, à Escola Positiva."],
   0,"A Escola Clássica, de base iluminista (com autores como Beccaria), defendia o livre-arbítrio do indivíduo e a necessidade de proporcionalidade entre a gravidade do crime e a pena aplicada.")
mc("PC","Criminologia","A Escola Positiva da Criminologia, tendo Cesare Lombroso como um de seus principais expoentes, caracterizou-se por:",
   ["Rejeitar completamente qualquer estudo científico sobre o criminoso.","Buscar explicações científicas (biológicas, psicológicas e sociais) para o comportamento criminoso, relativizando o livre-arbítrio absoluto.","Defender exclusivamente o livre-arbítrio absoluto do indivíduo.","Ser anterior, cronologicamente, à Escola Clássica.","Negar a existência de qualquer fator biológico relacionado ao crime."],
   1,"A Escola Positiva buscou explicações científicas para o crime, considerando fatores biológicos, psicológicos e sociais, relativizando a ideia de livre-arbítrio absoluto defendida pela Escola Clássica.")
mc("PC","Criminologia","Assinale a alternativa que descreve corretamente o conceito de 'cifra negra' (ou cifra oculta) na criminologia.",
   ["O total de crimes registrados oficialmente pelas autoridades.","A diferença entre a criminalidade real e a criminalidade oficialmente registrada pelas estatísticas.","O nome de uma teoria sobre a pena de morte.","Um tipo específico de perícia criminal.","Sinônimo de reincidência criminal."],
   1,"A cifra negra (ou oculta) representa a diferença entre a criminalidade real (todos os crimes efetivamente ocorridos) e a criminalidade aparente, oficialmente registrada pelas estatísticas policiais e judiciais."),

# ---- Legislação Especial (PC) ----
mc("PC","Legislação Especial","No que se refere à Lei de Abuso de Autoridade (Lei nº 13.869/2019), é correto afirmar que ela tem como finalidade:",
   ["Ampliar, sem qualquer limite, os poderes de agentes públicos no exercício da função.","Definir e sancionar condutas que configurem abuso de autoridade por agente público, no exercício de suas funções.","Extinguir a responsabilidade civil de agentes públicos por atos de ofício.","Aplicar-se exclusivamente a agentes do Poder Judiciário.","Revogar integralmente o Código Penal em matéria de crimes funcionais."],
   1,"A Lei nº 13.869/2019 tem como finalidade definir e sancionar condutas que configurem abuso de autoridade cometido por agente público no exercício de suas funções ou a pretexto de exercê-las.")
mc("PC","Legislação Especial","Segundo a Lei Maria da Penha (Lei nº 11.340/2006), a violência doméstica e familiar contra a mulher pode se manifestar, entre outras formas, como:",
   ["Apenas violência física, excluídas as demais formas de violência.","Violência física, psicológica, sexual, patrimonial e moral.","Exclusivamente violência patrimonial.","Somente violência ocorrida dentro do ambiente doméstico, excluído o âmbito familiar mais amplo.","Apenas condutas already tipificadas como crime no Código Penal."],
   1,"A Lei Maria da Penha prevê expressamente, em seu art. 7º, diversas formas de violência doméstica e familiar contra a mulher: física, psicológica, sexual, patrimonial e moral.")
mc("PC","Legislação Especial","Em relação ao Estatuto da Criança e do Adolescente (Lei nº 8.069/1990), é correto afirmar que ele adota, como princípio norteador, a:",
   ["Doutrina da situação irregular, típica de legislações anteriores ao Estatuto.","Doutrina da proteção integral, reconhecendo crianças e adolescentes como sujeitos de direitos.","Ausência de qualquer prioridade legal para crianças e adolescentes.","Equiparação plena entre menores de idade e adultos para fins penais.","Exclusão de qualquer medida socioeducativa para adolescentes em conflito com a lei."],
   1,"O ECA adota a doutrina da proteção integral, superando a antiga doutrina da situação irregular, reconhecendo crianças e adolescentes como sujeitos de direitos que devem ter prioridade absoluta.")


# =====================================================================
print(len(BANK))
with open("/home/claude/qbank/questions.json","w",encoding="utf-8") as f:
    json.dump(BANK, f, ensure_ascii=False, indent=None)
