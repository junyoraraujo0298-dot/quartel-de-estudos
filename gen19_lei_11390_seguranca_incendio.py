# -*- coding: utf-8 -*-
# Adiciona a Lei n. 11.390/2020 (Regulamento de Seguranca Contra
# Incendios das edificacoes e areas de risco no Estado do Maranhao) como
# nova lei de leitura (LAW_11390), registrada em LAW_DECKS e no atalho
# "Praticar questoes desta lei". Corrige a questao id 162, que usava o
# termo AVCB (terminologia de Sao Paulo, nao se aplica ao Maranhao -- o
# termo correto e Certificacao do Corpo de Bombeiros Militar). Adiciona
# 10 novas questoes de multipla escolha (BM) baseadas no texto real da
# lei.
import json
import re

with open('questions.json', encoding='utf-8') as f:
    raw = f.read()

data_check = json.loads(raw)
max_id = max(q['id'] for q in data_check)
assert max_id == 984, max_id

with open('app-template.html', encoding='utf-8') as f:
    html = f.read()

LAW_11390_ITEMS = [
    {"t": "tit", "x": "LEI Nº 11.390, DE 21 DE DEZEMBRO DE 2020 — Institui o Regulamento de Segurança "
                      "Contra Incêndios das edificações e áreas de risco no Estado do Maranhão"},
    {"t": "cap", "x": "CAPÍTULO I — DAS DISPOSIÇÕES PRELIMINARES"},
    {"t": "art", "n": "Art. 1º",
     "x": "Fica instituído o Regulamento de Segurança Contra Incêndios das edificações e áreas de "
          "risco no Estado do Maranhão.",
     "s": "É a lei estadual \"irmã\" da Lei 10.230/2015 (organização do CBMMA) — só que esta trata "
          "especificamente das exigências técnicas de segurança contra incêndio em edificações."},
    {"t": "art", "n": "Art. 2º",
     "x": "Objetivos do Regulamento: I- proteger prioritariamente a vida dos ocupantes; II- restringir "
          "o surgimento e dificultar a propagação de incêndios, reduzindo danos ao meio ambiente e ao "
          "patrimônio; III- proporcionar meios ao controle e à extinção de incêndios; IV- viabilizar "
          "operações de atendimento de emergências; V- proporcionar continuidade dos serviços nas "
          "edificações; VI- atribuir competências para o cumprimento das medidas; VII- fomentar uma "
          "cultura prevencionista de segurança contra incêndios.",
     "s": "Decore o inciso I: a PRIORIDADE é a vida dos ocupantes, não o patrimônio — pegadinha comum "
          "inverter essa ordem de prioridade."},
    {"t": "cap", "x": "CAPÍTULO II — DAS DEFINIÇÕES (Art. 3º)"},
    {"t": "art", "n": "Altura da edificação",
     "x": "Duas medidas distintas: a) para EXIGÊNCIAS de segurança contra incêndio — do piso mais "
          "baixo ocupado ao piso do último pavimento; b) para SAÍDA DE EMERGÊNCIA — do ponto que "
          "caracteriza a saída do nível de descarga ao piso do último pavimento habitável (podendo ser "
          "ascendente ou descendente).",
     "s": "PEGADINHA clássica: são DUAS alturas diferentes conforme a finalidade (exigências x saída "
          "de emergência) — não existe uma única \"altura da edificação\" no Regulamento."},
    {"t": "art", "n": "Agente fiscalizador / Carga de incêndio",
     "x": "Agente fiscalizador: integrante do CBMMA que exerce fiscalização das edificações e áreas de "
          "risco. Carga de incêndio: soma das energias caloríficas possíveis de serem liberadas pela "
          "combustão completa de todos os materiais combustíveis de um espaço, inclusive revestimento "
          "de paredes, divisórias, pisos e tetos.",
     "s": "Carga de incêndio inclui até o REVESTIMENTO (paredes/pisos/teto), não só o mobiliário/"
          "conteúdo do ambiente."},
    {"t": "art", "n": "Certificação do Corpo de Bombeiros Militar",
     "x": "Ato administrativo pelo qual o CBMMA, verificando que o interessado atendeu a todas as "
          "exigências legais do processo de segurança contra incêndios e emergências, autoriza a "
          "ocupação e o funcionamento das edificações ou áreas de risco.",
     "s": "Esse é o termo CORRETO no Maranhão — \"AVCB\" (Auto de Vistoria do Corpo de Bombeiros) é "
          "nomenclatura de SÃO PAULO, não da legislação maranhense; aqui o nome oficial é Certificação "
          "do Corpo de Bombeiros Militar."},
    {"t": "art", "n": "Compartimentação / Isolamento de risco",
     "x": "Compartimentação: medida de proteção incorporada ao sistema construtivo, com elementos "
          "resistentes ao fogo, para evitar ou minimizar a propagação do fogo, calor e gases, interna "
          "ou externamente, no mesmo pavimento ou a pavimentos elevados consecutivos. Isolamento de "
          "risco: medida de proteção passiva por parede de compartimentação sem aberturas ou "
          "afastamento ENTRE edificações, para evitar propagação entre blocos isolados.",
     "s": "Compartimentação = dentro da MESMA edificação; isolamento de risco = ENTRE edificações "
          "distintas. Não confundir os dois conceitos."},
    {"t": "art", "n": "Edificação existente / Edificação térrea",
     "x": "Edificação existente: área construída ou regularizada, com documentação comprobatória, "
          "anterior à edição do Regulamento, desde que não contrarie seus dispositivos. Edificação "
          "térrea: construção de um único pavimento, podendo possuir mezanino.",
     "s": "Edificação térrea PODE ter mezanino e continuar sendo \"térrea\" — mezanino não conta como "
          "pavimento adicional para esse fim, desde que dentro dos limites do art. 3º, XXV."},
    {"t": "art", "n": "Instalações temporárias",
     "x": "Abrigam ocupação com duração de até 6 (seis) meses, prorrogável uma vez por igual período, "
          "podendo ou não estar no interior de edificação permanente (ex.: circos, parques de "
          "diversões, feiras, rodeios, shows).",
     "s": "Decore o prazo: até 6 meses + 1 prorrogação de 6 meses = no máximo 12 meses."},
    {"t": "art", "n": "Mezanino",
     "x": "Pavimento que subdivide parcialmente um andar e cujas áreas somadas, limitadas a 250 m², "
          "não ultrapassem 1/3 (um terço) do pavimento subdividido.",
     "s": "Dois limites CUMULATIVOS: até 250 m² E até 1/3 do pavimento — ultrapassando qualquer um dos "
          "dois, deixa de ser mezanino para fins do Regulamento."},
    {"t": "art", "n": "Ocupação mista, predominante e subsidiária",
     "x": "Ocupação mista: há mais de um tipo de ocupação na edificação/área de risco. Ocupação "
          "predominante: atividade/uso principal. Ocupação subsidiária: atividade de apoio ou suporte, "
          "vinculada à principal.",
     "s": "Não se caracteriza ocupação mista (art. 4º, §5º) quando a subsidiária não ultrapassar 750 m² "
          "OU 10% da área total — nesse caso, aplicam-se só as exigências da ocupação predominante."},
    {"t": "art", "n": "Perícia de incêndio / Processo infracional",
     "x": "Perícia de incêndio: apuração das causas, do desenvolvimento e das consequências dos "
          "incêndios atendidos pelo CBMMA, mediante exame técnico das edificações, materiais e "
          "equipamentos, no local ou em laboratório, visando o aprimoramento técnico da segurança "
          "contra incêndios e da atividade operacional. Processo infracional: processo de fiscalização "
          "do CBMMA que resulta na autuação do infrator, assegurados contraditório e ampla defesa.",
     "s": "A perícia de incêndio é atribuição técnica do PRÓPRIO Corpo de Bombeiros (não é só a "
          "polícia científica que periciai incêndio) — serve também para aprimorar a própria atividade "
          "operacional do CBMMA."},
    {"t": "art", "n": "Risco específico / Subsolo",
     "x": "Risco específico: situação com maior probabilidade de perigo à edificação (caldeira, casa "
          "de máquinas, incinerador, central de gás combustível, transformador, fonte de ignição, "
          "entre outros). Subsolo: pavimento situado abaixo do perfil do terreno; NÃO será considerado "
          "subsolo o pavimento com ventilação natural para o exterior (área total superior a 0,006 m² "
          "por metro cúbico de ar do compartimento) e laje de cobertura acima de 1,20 m do perfil do "
          "terreno.",
     "s": "PEGADINHA: nem todo pavimento abaixo do nível do solo é \"subsolo\" para o Regulamento — "
          "se tiver ventilação natural suficiente e a laje de cobertura acima de 1,20 m, deixa de ser "
          "classificado como subsolo."},
    {"t": "art", "n": "Vistoria técnica de fiscalização x de regularização",
     "x": "Vistoria técnica de fiscalização: o CBMMA verifica, a qualquer momento, se a edificação "
          "atende à legislação vigente. Vistoria técnica de regularização: o CBMMA verifica, mediante "
          "SOLICITAÇÃO do proprietário/responsável, se as medidas de segurança foram atendidas.",
     "s": "Fiscalização = iniciativa do CBMMA, a qualquer momento (ex officio). Regularização = "
          "mediante solicitação do interessado. Mesma lógica do art. 32 (dois tipos de fiscalização: "
          "a pedido ou ex officio)."},
    {"t": "cap", "x": "CAPÍTULO III — DA APLICAÇÃO"},
    {"t": "art", "n": "Art. 4º",
     "x": "As medidas de segurança aplicam-se a edificações e áreas de risco em todo o território "
          "estadual, em especial por ocasião de: construção, reforma com alteração de leiaute, "
          "mudança de ocupação/uso, ampliação de área construída, aumento de altura, ou regularização. "
          "§1º Excluem-se: edificações de uso residencial exclusivamente unifamiliares; residência "
          "exclusivamente unifamiliar no pavimento superior. §4º/§5º: em ocupação mista, aplicam-se as "
          "medidas de MAIOR RIGOR para toda a edificação (salvo exceções de compartimentação em "
          "edificações térreas, ou subsidiária até 750 m²/10%, caso em que vale só a predominante).",
     "s": "Residência unifamiliar é a GRANDE exceção do Regulamento — o resto (inclusive multifamiliar) "
          "entra na regra geral."},
    {"t": "cap", "x": "CAPÍTULO IV — DAS COMPETÊNCIAS E ATRIBUIÇÕES"},
    {"t": "art", "n": "Arts. 5º a 7º",
     "x": "Compete ao CBMMA: estudo, análise, planejamento e elaboração das normas de segurança contra "
          "incêndios e emergências, a fiscalização de seu cumprimento e a promoção de programas de "
          "educação pública nesse campo (art. 5º). Nas vistorias, o CBMMA verifica a funcionalidade "
          "dos sistemas de forma VISUAL e POR AMOSTRAGEM, NÃO se responsabilizando pela instalação, "
          "comissionamento, inspeção, ensaio, manutenção ou utilização indevida dos sistemas (art. 6º). "
          "Compete ao RESPONSÁVEL TÉCNICO o dimensionamento das medidas e sua correta instalação "
          "(art. 7º).",
     "s": "PEGADINHA do art. 6º: o CBMMA fiscaliza por amostragem visual, mas quem RESPONDE pela "
          "correta instalação/manutenção dos sistemas é o responsável técnico/proprietário, não o "
          "CBMMA."},
    {"t": "cap", "x": "CAPÍTULO V — DAS RESPONSABILIDADES"},
    {"t": "art", "n": "Art. 8º",
     "x": "É de inteira responsabilidade do proprietário ou usuário: utilizar a edificação conforme a "
          "Certificação outorgada; realizar manutenção e testes periódicos das medidas de segurança, "
          "com emissão de relatórios comprobatórios; efetuar treinamento periódico dos ocupantes e "
          "manter atualizada a brigada e os planos de emergência; providenciar a adequação da "
          "edificação às exigências do art. 4º.",
     "s": "Reforça o art. 6º: a manutenção periódica dos sistemas é responsabilidade do proprietário/"
          "usuário, não do CBMMA."},
    {"t": "cap", "x": "CAPÍTULO VI — DO SERVIÇO DE SEGURANÇA CONTRA INCÊNDIOS E EMERGÊNCIAS"},
    {"t": "art", "n": "Arts. 9º e 10",
     "x": "O Serviço de Segurança Contra Incêndios e Emergências é constituído pelo conjunto de "
          "Organizações Bombeiro Militar com essa finalidade. Compete aos seus órgãos, entre outras "
          "atribuições: realizar investigações em casos de incêndio/explosão; estabelecer normas "
          "complementares; habilitar os militares do serviço; analisar projetos e realizar vistorias; "
          "expedir, anular, cassar ou revogar certificações do CBMMA; embargar ou interditar "
          "edificações/áreas de risco; notificar, autuar e sancionar; emitir Consultas e Pareceres "
          "Técnicos; credenciar escolas/empresas de formação, empresas de brigada profissional, "
          "bombeiros civis e empresas instaladoras/conservadoras/revendedoras de material de segurança "
          "contra incêndio; cadastrar responsáveis técnicos.",
     "s": "Lista extensa — o essencial é saber que CASSAR certificação, EMBARGAR/INTERDITAR e "
          "CREDENCIAR bombeiros civis são todas atribuições do próprio Serviço de Segurança do CBMMA."},
    {"t": "cap", "x": "CAPÍTULO VII — DO PROCESSO DE SEGURANÇA CONTRA INCÊNDIOS E EMERGÊNCIAS"},
    {"t": "art", "n": "Arts. 11 a 15",
     "x": "O Processo de Segurança Contra Incêndio e Emergências é o conjunto de procedimentos para o "
          "licenciamento de edificações/áreas de risco (art. 11). A Certificação do CBMMA é emitida "
          "quando as medidas estiverem de acordo com o processo aprovado, com prazo de validade "
          "predeterminado em Norma Técnica (art. 12); constatadas irregularidades após a emissão, "
          "inicia-se de ofício processo para CASSAÇÃO (art. 13, parágrafo único). O Termo de "
          "Autorização para Adequação (TAACBM) é emitido EXCEPCIONALMENTE, mediante avaliação de "
          "Comissão Técnica, para edificações que precisem de prazo para ajustar as medidas (art. 14). "
          "Casos com soluções técnicas diversas das previstas são analisados por Comissão Técnica "
          "(art. 15).",
     "s": "O TAACBM é EXCEÇÃO, não regra — exige avaliação de Comissão Técnica e cronograma físico de "
          "adequação."},
    {"t": "cap", "x": "CAPÍTULO VIII — DA ALTURA E ÁREA DAS EDIFICAÇÕES"},
    {"t": "art", "n": "Art. 16 — O que NÃO entra no cálculo da altura",
     "x": "Não são considerados, na mensuração da altura: subsolos destinados a estacionamento, "
          "vestiários, instalações sanitárias e áreas técnicas sem permanência de pessoas; pavimentos "
          "superiores destinados exclusivamente a áticos, casas de máquinas, barriletes e "
          "reservatórios; mezaninos dentro dos limites do art. 3º, XXV; o pavimento superior de "
          "unidade dúplex/triplex do último piso de edificação residencial multifamiliar.",
     "s": "Casa de máquinas, ático e reservatório no topo do prédio NÃO contam como \"mais um "
          "pavimento\" para fins de altura."},
    {"t": "art", "n": "Art. 18 — O que NÃO entra no cálculo da área",
     "x": "Não são computados no cálculo da área a proteger: telheiros com laterais abertas e até "
          "10 m² (proteção de utensílios/caixas d'água/tanques); platibandas e beirais de telhado com "
          "até 3 m de projeção; passagens cobertas de até 3 m de largura, com laterais abertas, para "
          "circulação; cobertura de bombas de combustível/pedágio aberta lateralmente em ao menos 50% "
          "do perímetro; reservatórios de água; piscinas/banheiros/vestiários (quanto a sistemas "
          "hidráulicos, alarme de incêndio e compartimentação).",
     "s": "Decore os números: telheiro até 10 m², beiral até 3 m, passagem coberta até 3 m de largura, "
          "bomba de combustível aberta em pelo menos 50% do perímetro."},
    {"t": "cap", "x": "CAPÍTULO IX — DAS MEDIDAS DE SEGURANÇA CONTRA INCÊNDIOS E EMERGÊNCIAS"},
    {"t": "art", "n": "Art. 19 — Parâmetros para determinar as medidas",
     "x": "Devem ser considerados: ocupação/uso; altura; carga de incêndio; área construída; "
          "capacidade de lotação; riscos específicos.",
     "s": "6 parâmetros — repare que \"localização geográfica\" ou \"idade da edificação\" NÃO estão "
          "na lista."},
    {"t": "art", "n": "Art. 20 — As 22 medidas de segurança",
     "x": "Acesso de viatura; isolamento de risco; segurança estrutural contra incêndio; "
          "compartimentação; controle de materiais de acabamento/revestimento; saídas de emergência; "
          "elevador de emergência; controle de fumaça; gerenciamento de risco de incêndio (incluindo "
          "plano de emergência); brigada de incêndio; iluminação de emergência; detecção automática de "
          "incêndio; alarme de incêndio; sinalização de emergência; extintores; hidrantes e "
          "mangotinhos; chuveiros automáticos; sistema de resfriamento; sistema de espuma; sistema "
          "fixo de gases limpos e CO₂; Sistema de Proteção contra Descargas Atmosféricas (SPDA); "
          "controle de fontes de ignição.",
     "s": "Lista grande — não precisa decorar as 22 em ordem, mas saiba reconhecer cada uma como "
          "MEDIDA DE SEGURANÇA (ex.: SPDA e controle de fontes de ignição também são medidas de "
          "segurança contra incêndio, não só extintor/hidrante)."},
    {"t": "cap", "x": "CAPÍTULO X — DO CUMPRIMENTO DAS MEDIDAS"},
    {"t": "art", "n": "Arts. 22 a 25",
     "x": "São obrigatórias as medidas assinaladas com \"X\" nas tabelas de exigências da Norma "
          "Técnica, conforme a classificação da edificação (art. 22, §1º). Pavimentos ocupados devem "
          "ter aberturas para o exterior (janelas/painéis de vidro) ou controle de fumaça (art. 23). "
          "Áreas descobertas de armazenamento de materiais sólidos combustíveis são consideradas áreas "
          "de risco, devendo os materiais ser fracionados em lotes, afastados dos limites da "
          "propriedade, com corredores internos (art. 25).",
     "s": "Área descoberta com material combustível armazenado também é \"área de risco\" — não "
          "precisa ser uma edificação fechada para se enquadrar no Regulamento."},
    {"t": "cap", "x": "CAPÍTULO XI — DAS INSTALAÇÕES TEMPORÁRIAS"},
    {"t": "art", "n": "Arts. 26 a 28",
     "x": "Instalações temporárias com área delimitada (art. 26) e sem delimitação de área, mas com "
          "acesso ao público (art. 27), devem ter controle de acesso e ser regularizadas junto ao "
          "CBMMA ANTES do início do evento. Instalações temporárias dentro de edificação permanente "
          "precisam de controle próprio de acesso, além da regularização prévia da própria edificação "
          "permanente (art. 28).",
     "s": "Regularizar a instalação temporária NÃO dispensa a regularização da edificação permanente "
          "onde ela estiver instalada (art. 28) — são exigências cumulativas."},
    {"t": "cap", "x": "CAPÍTULO XII — DO TRATAMENTO ÀS ME, EPP E MEI"},
    {"t": "art", "n": "Arts. 29 a 31",
     "x": "Microempresas, empresas de pequeno porte e MEIs têm tratamento SIMPLIFICADO para "
          "regularização, visando à celeridade (art. 29). A fiscalização nesses casos deve ser "
          "PRIORITARIAMENTE ORIENTADORA, quando o grau de risco da atividade comportar esse "
          "procedimento (art. 30). O CBMMA pode, a qualquer tempo, verificar as informações/documentos "
          "prestados, sob pena de cassação da certificação, independentemente de responsabilidades "
          "civis e penais (art. 31).",
     "s": "\"Prioritariamente orientadora\" não significa \"sem fiscalização\" — o CBMMA pode verificar "
          "e cassar a certificação a qualquer tempo, mesmo pra ME/EPP/MEI."},
    {"t": "cap", "x": "CAPÍTULO XIII — DA FISCALIZAÇÃO"},
    {"t": "art", "n": "Art. 32",
     "x": "A fiscalização pode se dar por solicitação do proprietário/responsável/procurador, ou EX "
          "OFFICIO pelo CBMMA. No exercício da fiscalização, o CBMMA pode adentrar o local, obter "
          "relatórios e informações verbais. A fiscalização NÃO pode interromper as atividades do "
          "estabelecimento — não se considera interrupção a verificação durante o horário normal de "
          "funcionamento.",
     "s": "PEGADINHA: fiscalizar durante o horário normal de funcionamento NÃO é considerado "
          "\"interrupção das atividades\", mesmo que atrapalhe um pouco a rotina do local."},
    {"t": "cap", "x": "CAPÍTULO XIV — DAS INFRAÇÕES E PENALIDADES"},
    {"t": "art", "n": "Arts. 33 a 38 — Sanções e procedimento",
     "x": "Sanções administrativas (art. 34): advertência, multa, interdição, embargo — a multa PODE "
          "ser cumulada com as demais (§2º), e sanções aplicadas conjuntamente são INDEPENDENTES entre "
          "si (art. 35, parágrafo único). O pagamento de multa NÃO isenta das exigências nem de outras "
          "sanções cíveis/penais (art. 37, §2º). Interdição/embargo são imediatamente exigíveis em "
          "caso de risco de dano irreparável ou grave (art. 37, §1º). Cabe recurso administrativo "
          "contra qualquer penalidade (art. 38).",
     "s": "Multa não substitui nem dispensa interdição/embargo quando necessário — e pagar a multa não "
          "livra o infrator de corrigir a irregularidade."},
    {"t": "art", "n": "Anexo B — Classificação das infrações: Deficiente, Inoperante, Inexistente",
     "x": "Deficiente: sistema instalado (total ou parcialmente) e utilizável, mas que não atende "
          "totalmente às especificações técnicas. Inoperante: sistema instalado, mas que NÃO funciona. "
          "Inexistente: sistema que NÃO está instalado. Para a infração, usa-se a tipificação mais "
          "específica para a irregularidade.",
     "s": "Ordem de gravidade crescente para a MESMA medida de segurança: deficiente (Grupo I, leve) < "
          "inoperante (Grupo II, média) < inexistente (Grupo III, grave) — quanto pior o estado do "
          "sistema, mais grave o grupo da infração."},
    {"t": "art", "n": "Anexo B — Grupos I a IV de infrações",
     "x": "Grupo I (leves): medidas DEFICIENTES (ex.: saída de emergência deficiente, extintores "
          "deficientes). Grupo II (médias): medidas INOPERANTES (ex.: sistema de alarme inoperante) e "
          "outras situações específicas (ex.: armazenamento de GLP/GN em desconformidade). Grupo III "
          "(graves): medidas INEXISTENTES (ex.: saída de emergência inexistente, SPDA inexistente) e "
          "uso indevido de símbolos do Corpo de Bombeiros. Grupo IV (gravíssimas): evento temporário "
          "sem licença do CBMMA; armazenamento/comércio/manipulação irregular de explosivos; "
          "edificação sem Certificação do CBMMA; lotação acima do permitido; saída de emergência "
          "insuficiente, obstruída ou trancada em local de reunião de público.",
     "s": "Saída de emergência TRANCADA ou OBSTRUÍDA em local de reunião de público é infração "
          "GRAVÍSSIMA (Grupo IV) — não apenas grave."},
    {"t": "cap", "x": "CAPÍTULO XV — DO CADASTRAMENTO E CREDENCIAMENTO"},
    {"t": "art", "n": "Arts. 39 e 40",
     "x": "Empresas formadoras de bombeiro civil, brigada de incêndio e guarda-vidas (e seus centros, "
          "instrutores e avaliadores) devem estar cadastradas e credenciadas junto ao CBMMA, com "
          "periodicidade ANUAL, de forma específica para cada endereço, intransferível, temporária e "
          "renovável (art. 39). Bombeiros civis, brigadistas e guarda-vidas também devem estar "
          "credenciados/cadastrados, com periodicidade anual e SEM COBRANÇA DE TAXA (art. 40). Seus "
          "uniformes NÃO podem se confundir com os do CBMMA.",
     "s": "PEGADINHA: o credenciamento do PROFISSIONAL (bombeiro civil/brigadista/guarda-vidas) não tem "
          "taxa, diferente do credenciamento das EMPRESAS (que têm taxa de credenciamento anual, "
          "conforme o Anexo A)."},
    {"t": "cap", "x": "CAPÍTULO XVI — DAS DISPOSIÇÕES FINAIS E TRANSITÓRIAS"},
    {"t": "art", "n": "Arts. 44 e 46",
     "x": "A instalação e manutenção de hidrantes em logradouros públicos compete ao CBMMA, com auxílio "
          "do órgão/entidade de abastecimento de água local, mediante convênio (art. 44). Durante o "
          "atendimento a sinistros, havendo real necessidade, o CBMMA pode utilizar água armazenada em "
          "reservatórios privativos de edificações particulares ou públicas, devendo depois informar o "
          "consumo ao responsável e à concessionária (art. 46).",
     "s": "O CBMMA pode \"invadir\" a caixa d'água de um prédio particular em caso de emergência real "
          "— mas depois precisa prestar contas do volume usado."},
    {"t": "art", "n": "Arts. 47 a 49",
     "x": "Altera a Tabela \"E\" da Lei nº 7.799/2002 (taxas). Revoga a Lei nº 6.546/1995 e disposições "
          "contrárias. Vigência: data da publicação.",
     "s": "Esta lei de 2020 REVOGA a antiga Lei 6.546/1995, que tratava do tema antes dela."},
    {"t": "cap", "x": "ANEXO C — Fórmula de Cálculo da Multa"},
    {"t": "art", "n": "A fórmula",
     "x": "Multa (R$) = [(2,5 × I) + (3,5 × II) + (5 × III) + (7 × IV)] × R × K × VBBM, onde I, II, "
          "III e IV são as quantidades de infrações de cada grupo (I, II e III: de 0 a 4; IV: de 0 a "
          "2); R é o fator de risco (Tabela 1: baixo=1,0 / médio=1,1 / alto=1,2, conforme a carga de "
          "incêndio); K é o fator de área (Tabela 2, crescente conforme a área total, de 4 até 200 m² "
          "até 100 pontos acima de 100.000 m²); e VBBM é o Valor Básico Bombeiro Militar.",
     "s": "Decore os PESOS por grupo: leve=2,5 / média=3,5 / grave=5 / gravíssima=7 — crescem conforme "
          "a gravidade, e o Grupo IV tem o maior peso individual (7), mas o menor limite de "
          "quantidade (máximo 2, contra 4 dos demais grupos)."},
]

m = re.search(r'const LAW_10230\s*=\s*\[', html)
assert m, "LAW_10230 nao encontrada"
array_start = m.end() - 1
decoder = json.JSONDecoder()
_arr, array_end = decoder.raw_decode(html, array_start)
insertion_point = array_end  # logo apos o ";" implicito -- vamos inserir depois do "];" da LAW_10230
# array_end aponta logo apos o "]"; o proximo caractere deve ser ";"
assert html[array_end] == ';', html[array_end:array_end+20]
insertion_point = array_end + 1

new_law_block = ('\n\nconst LAW_11390 = [\n' +
                  ',\n'.join(json.dumps(item, ensure_ascii=False) for item in LAW_11390_ITEMS) +
                  '\n];')

new_html = html[:insertion_point] + new_law_block + html[insertion_point:]

# registra no LAW_DECKS e no atalho LEITURA_DECK_TO_DISC
old_law_decks = '  comparativo: { label: "Comparativo das 3 Leis (PMMA)", data: LAW_COMPARISON, corp: "PM" }\n};'
new_law_decks = ('  comparativo: { label: "Comparativo das 3 Leis (PMMA)", data: LAW_COMPARISON, corp: "PM" },\n'
                  '  lei11390: { label: "Lei 11.390/2020 (Segurança Contra Incêndio)", data: LAW_11390, '
                  'corp: "BM" }\n};')
assert old_law_decks in new_html, "bloco LAW_DECKS nao encontrado como esperado"
new_html = new_html.replace(old_law_decks, new_law_decks)

old_map = '''const LEITURA_DECK_TO_DISC = {
  lei: "Estatuto da PM/MA (Lei 6.513/95)",
  lei12896: "Lei 12.896/2026 (Organização Básica da PMMA)",
  lei10230: "Lei 10.230/2015 (Organização Básica do CBMMA)",
  lei14751: "Lei 14.751/2023 (Lei Orgânica Nacional — PM e BM)"
};'''
new_map = '''const LEITURA_DECK_TO_DISC = {
  lei: "Estatuto da PM/MA (Lei 6.513/95)",
  lei12896: "Lei 12.896/2026 (Organização Básica da PMMA)",
  lei10230: "Lei 10.230/2015 (Organização Básica do CBMMA)",
  lei14751: "Lei 14.751/2023 (Lei Orgânica Nacional — PM e BM)",
  lei11390: "Segurança Contra Incêndio e Pânico"
};'''
assert old_map in new_html, "LEITURA_DECK_TO_DISC nao encontrado como esperado"
new_html = new_html.replace(old_map, new_map)

with open('app-template.html', 'w', encoding='utf-8', newline='') as f:
    f.write(new_html)
print('LAW_11390 adicionada com', len(LAW_11390_ITEMS), 'itens; registrada em LAW_DECKS e no atalho.')

# ---------------- corrige a questao 162 (AVCB) e adiciona 10 novas ----------------
DISC = "Segurança Contra Incêndio e Pânico"
ASSUNTO_LEI = ("LEI Nº 11.390, DE 21 DE DEZEMBRO DE 2020 — Institui o Regulamento de Segurança Contra "
               "Incêndios das edificações e áreas de risco no Estado do Maranhão")
FONTE = " (Lei nº 11.390/2020 — Regulamento de Segurança Contra Incêndios do Maranhão.)"

data_list = json.loads(raw)
q162 = next(q for q in data_list if q['id'] == 162)
assert 'AVCB' in q162['enun']
q162['enun'] = ("Em edificações no Estado do Maranhão, a Certificação do Corpo de Bombeiros Militar do "
                "Maranhão (CBMMA) tem por finalidade principal:")
q162['alts'] = [
    "autorizar a ocupação e o funcionamento da edificação ou área de risco, por atestar o atendimento "
    "a todas as exigências legais de segurança contra incêndios e emergências.",
    "substituir integralmente o alvará de funcionamento municipal, para todos os fins.",
    "dispensar o proprietário de qualquer manutenção futura dos sistemas de segurança instalados.",
    "ser exigida apenas de edificações públicas, não de edificações privadas.",
    "ter validade permanente, sem necessidade de renovação."
]
q162['resp'] = 0
q162['exp'] = ("Correto. No Maranhão, o documento correto é a Certificação do Corpo de Bombeiros Militar "
               "(e não o AVCB, terminologia usada em São Paulo), nos termos do art. 3º, XII, e do art. "
               "12 da Lei nº 11.390/2020 — ato que autoriza a ocupação e o funcionamento da edificação. "
               "Sua validade é predeterminada em Norma Técnica (não é permanente), e ela não dispensa a "
               "manutenção periódica dos sistemas, que é responsabilidade do proprietário/usuário "
               "(art. 8º)." + FONTE)
q162['assunto'] = ASSUNTO_LEI
print('Questao 162 corrigida (AVCB -> Certificacao do CBMMA)')

NEW_QUESTIONS = [
    {"enun": "Nos termos da Lei nº 11.390/2020, a altura da edificação, para fins de aplicação do "
             "Regulamento de Segurança Contra Incêndios do Maranhão, é definida:",
     "alts": ["por uma única medida, aplicável tanto às exigências de segurança quanto ao "
              "dimensionamento das saídas de emergência.",
              "por duas medidas distintas: uma para fins de exigências de segurança contra incêndios "
              "(do piso mais baixo ocupado ao piso do último pavimento) e outra, independente, para "
              "fins de saída de emergência (do nível de descarga ao piso do último pavimento "
              "habitável).",
              "exclusivamente em função do número de subsolos da edificação.",
              "apenas para edificações com mais de 12 metros de altura.",
              "pela soma da altura de todos os pavimentos, incluindo áticos e casas de máquinas."],
     "resp": 1,
     "exp": "Correto, nos termos do art. 3º, I, e do art. 17 e parágrafo único da Lei nº 11.390/2020: "
            "há duas alturas diferentes, conforme a finalidade."},

    {"enun": "De acordo com a Lei nº 11.390/2020, um pavimento mezanino, para ser assim classificado, "
             "deve atender cumulativamente aos seguintes limites:",
     "alts": ["área de até 500 m², independentemente da proporção em relação ao pavimento subdividido.",
              "área de até 250 m² e, ao mesmo tempo, não ultrapassar 1/3 (um terço) da área do "
              "pavimento que subdivide.",
              "ocupar, no mínimo, metade da área do pavimento subdividido.",
              "estar localizado exclusivamente no último pavimento da edificação.",
              "não haver limite de área, desde que a edificação seja térrea."],
     "resp": 1,
     "exp": "Correto, nos termos do art. 3º, XXV, da Lei nº 11.390/2020 — os dois limites (250 m² e "
            "1/3 do pavimento) são cumulativos."},

    {"enun": "Segundo a Lei nº 11.390/2020, um pavimento situado abaixo do perfil do terreno:",
     "alts": ["será sempre classificado como subsolo, independentemente de sua ventilação.",
              "não será considerado subsolo se possuir ventilação natural para o exterior em área "
              "suficiente e tiver a laje de cobertura acima de 1,20 m do perfil do terreno.",
              "só poderá ser classificado como subsolo se for destinado a estacionamento de veículos.",
              "será automaticamente excluído do cálculo de altura da edificação, em qualquer "
              "hipótese.",
              "é sempre considerado área de risco, independentemente de sua ocupação."],
     "resp": 1,
     "exp": "Correto, nos termos do art. 3º, XLVIII, da Lei nº 11.390/2020 — a definição de subsolo "
            "admite exceção quando há ventilação natural suficiente e a laje de cobertura está acima "
            "de 1,20 m do perfil do terreno."},

    {"enun": "Em relação às instalações temporárias disciplinadas pela Lei nº 11.390/2020, assinale a "
             "alternativa correta.",
     "alts": ["Podem abrigar ocupação por prazo indeterminado, sem necessidade de prorrogação formal.",
              "Devem abrigar ocupação de até 6 meses, prorrogável uma única vez por igual período, "
              "podendo ou não estar no interior de edificação permanente.",
              "Estão sempre dispensadas de controle de acesso de público.",
              "Dispensam a regularização da edificação permanente em que estiverem instaladas, quando "
              "houver.",
              "Só podem ser instaladas em áreas públicas, nunca em edificações privadas."],
     "resp": 1,
     "exp": "Correto, nos termos do art. 3º, XXII, c/c art. 28, da Lei nº 11.390/2020. Quando situadas "
            "no interior de edificação permanente, é obrigatória também a regularização prévia dessa "
            "edificação."},

    {"enun": "No exercício da fiscalização prevista na Lei nº 11.390/2020, é correto afirmar que o "
             "Corpo de Bombeiros Militar do Maranhão:",
     "alts": ["não pode realizar fiscalização de ofício, dependendo sempre de solicitação do "
              "proprietário.",
              "pode agir tanto mediante solicitação do interessado quanto de ofício, podendo adentrar o "
              "local e obter relatórios e informações, sem que a verificação durante o horário normal "
              "de funcionamento seja considerada interrupção das atividades.",
              "deve obrigatoriamente interromper o funcionamento do estabelecimento durante toda "
              "vistoria técnica.",
              "está impedido de exigir documentos relativos aos materiais e equipamentos de segurança "
              "contra incêndio.",
              "só pode fiscalizar edificações públicas, nunca estabelecimentos privados."],
     "resp": 1,
     "exp": "Correto, nos termos do art. 32 da Lei nº 11.390/2020."},

    {"enun": "Segundo o Anexo B da Lei nº 11.390/2020, um sistema de extintores de incêndio "
             "INSTALADO na edificação, mas que NÃO FUNCIONA, deve ser classificado como:",
     "alts": ["deficiente, por não atender totalmente às especificações técnicas.",
              "inoperante, por estar instalado mas não funcionar, enquadrando-se, nesse caso, em "
              "infração do Grupo II (média).",
              "inexistente, pois a ausência de funcionamento equivale à falta de instalação.",
              "irrelevante para fins de fiscalização, desde que o sistema esteja fisicamente presente.",
              "gravíssimo, independentemente do tipo de edificação."],
     "resp": 1,
     "exp": "Correto. Um sistema instalado, mas que não funciona, é \"inoperante\" (Anexo B, item b), "
            "enquadrando-se no Grupo II de infrações — diferente de \"deficiente\" (instalado mas fora "
            "da especificação técnica) e de \"inexistente\" (não instalado)."},

    {"enun": "Em um local destinado à reunião de público, a saída de emergência encontrada obstruída e "
             "trancada, no dia de uma fiscalização do CBMMA, deve ser enquadrada, segundo o Anexo B da "
             "Lei nº 11.390/2020, como infração:",
     "alts": ["leve, por se tratar de mera questão de manutenção predial.",
              "média, equivalente a um sistema meramente inoperante.",
              "grave, pela ausência completa do dispositivo de segurança.",
              "gravíssima, por se tratar expressamente de hipótese do Grupo IV.",
              "não enquadrável em nenhum grupo, por não constar do Anexo B."],
     "resp": 3,
     "exp": "Correto. O Anexo B, Grupo IV (infrações gravíssimas), prevê expressamente \"local "
            "destinado à reunião de público com saída de emergência insuficiente, obstruída ou "
            "trancada\" como infração gravíssima."},

    {"enun": "Quanto às sanções administrativas previstas na Lei nº 11.390/2020 para infrações ao "
             "Regulamento de Segurança Contra Incêndios, é correto afirmar que:",
     "alts": ["a pena de multa é sempre aplicada isoladamente, sendo incompatível com qualquer outra "
              "sanção.",
              "a pena de multa pode ser cumulada com as demais sanções (advertência, interdição ou "
              "embargo), e, havendo mais de uma sanção aplicada, estas são consideradas independentes "
              "entre si.",
              "o pagamento da multa isenta automaticamente o responsável do cumprimento das exigências "
              "pendentes.",
              "a interdição e o embargo somente podem ser aplicados após o trânsito em julgado de "
              "processo judicial.",
              "não cabe recurso administrativo contra a aplicação de penalidades previstas no "
              "Regulamento."],
     "resp": 1,
     "exp": "Correto, nos termos do art. 34, §2º, e do art. 35 e parágrafo único, da Lei nº 11.390/2020."},

    {"enun": "Considerando a fórmula de cálculo de multas do Anexo C da Lei nº 11.390/2020 — Multa "
             "(R$) = [(2,5 × I) + (3,5 × II) + (5 × III) + (7 × IV)] × R × K × VBBM —, é correto "
             "afirmar que:",
     "alts": ["o peso atribuído às infrações do Grupo IV (gravíssimas) é o maior entre os quatro "
              "grupos, ainda que esse grupo comporte, no máximo, apenas 2 infrações na fórmula, contra "
              "até 4 dos demais grupos.",
              "todos os grupos de infração têm o mesmo peso multiplicador na fórmula.",
              "o fator de risco (R) independe da carga de incêndio da edificação.",
              "o fator de área (K) diminui à medida que a área total da edificação aumenta.",
              "o Valor Básico Bombeiro Militar (VBBM) é fixado em lei, sem possibilidade de correção "
              "monetária."],
     "resp": 0,
     "exp": "Correto. O Grupo IV tem o maior peso (7), mas está limitado a, no máximo, 2 infrações "
            "inseridas na fórmula, enquanto os Grupos I, II e III (pesos 2,5, 3,5 e 5, respectivamente) "
            "comportam até 4 infrações cada."},

    {"enun": "Em relação ao credenciamento de profissionais e empresas previsto na Lei nº 11.390/2020, "
             "é correto afirmar que:",
     "alts": ["tanto as empresas quanto os profissionais (bombeiros civis, brigadistas e guarda-vidas) "
              "pagam taxa de credenciamento anual ao CBMMA.",
              "o credenciamento dos profissionais (bombeiros civis, brigadistas e guarda-vidas) junto "
              "ao CBMMA é anual e não há cobrança de taxa, diferentemente do credenciamento das "
              "empresas, sujeito a taxa específica.",
              "o credenciamento, uma vez obtido, tem validade permanente, sem necessidade de renovação "
              "anual.",
              "os uniformes dos bombeiros civis podem ser idênticos aos do Corpo de Bombeiros Militar, "
              "desde que autorizados pelo empregador.",
              "apenas as empresas formadoras precisam de credenciamento; os profissionais formados "
              "estão automaticamente habilitados, sem necessidade de credenciamento individual."],
     "resp": 1,
     "exp": "Correto, nos termos dos arts. 39 e 40 da Lei nº 11.390/2020 — o credenciamento dos "
            "profissionais é anual e gratuito; já as empresas pagam taxa de credenciamento anual "
            "(Anexo A); os uniformes dos profissionais civis não podem se confundir com os do CBMMA."},
]

assert len(NEW_QUESTIONS) == 10
next_id = 985
built = []
for item in NEW_QUESTIONS:
    built.append({
        "id": next_id, "corp": "BM", "disc": DISC, "assunto": ASSUNTO_LEI, "tipo": "MC",
        "enun": item["enun"], "alts": item["alts"], "resp": item["resp"],
        "exp": item["exp"] + FONTE,
    })
    next_id += 1

data_list.extend(built)

lines = [json.dumps(q, ensure_ascii=False) for q in data_list]
body = '[' + lines[0]
for line in lines[1:]:
    body += '\r\n, ' + line
body += ']'

with open('questions.json', 'w', encoding='utf-8', newline='') as f:
    f.write(body)

with open('questions.json', encoding='utf-8') as f:
    check = json.load(f)
assert len(check) == len(data_check) + len(built)
print('OK -- total de questoes agora:', len(check))

with open('questions.json', encoding='utf-8') as f:
    qdata = f.read()
with open('app-template.html', encoding='utf-8') as f:
    html2 = f.read()
html2 = html2.replace('__QUESTIONS_JSON__', qdata)
with open('estudo-cebraspe-ma.html', 'w', encoding='utf-8') as f:
    f.write(html2)
print('estudo-cebraspe-ma.html regenerado com sucesso')
