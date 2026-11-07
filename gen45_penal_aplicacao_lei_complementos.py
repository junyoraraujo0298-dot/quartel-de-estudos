# -*- coding: utf-8 -*-
"""
Quinto round de Direito Penal (PC-PE) -- a partir do PDF "Aplicacao da lei
penal" (Focus Concursos, PDF FOCADO), que cobre tempo e lugar do crime,
territorialidade/extraterritorialidade, eficacia da sentenca estrangeira,
contagem de prazo e conflito aparente de leis penais.

O PDF e extremamente extenso (dezenas de paginas de teoria + 150+ questoes
de treino), mas, ao comparar com o conteudo ja existente em
TEORIA_DIREITO_PENAL_PCPE (adicionado no gen37, antes desta sessao), quase
todo o escopo teorico principal ja estava coberto: tempus regit actum, os
4 conflitos de leis no tempo, teoria da atividade x ubiquidade (com Sumula
711), lei excepcional/temporaria, combinacao de leis/Lex Tertia (Sumula
501 STJ), continuidade normativo-tipica, territorialidade e
extraterritorialidade (tabela completa do art. 7, incondicionada/
condicionada/hipercondicionada), pena cumprida no estrangeiro, eficacia de
sentenca estrangeira (STJ, Sumula 420 STF), contagem de prazo penal x
processual, fracoes nao computaveis, legislacao especial, interpretacao da
lei penal (analogia x extensiva x analogica) e conflito aparente de leis
(mnemonico CASE) -- ou seja, o PDF e, em grande parte, material duplicado
do que ja estava no app.

A mudanca estrutural em app-template.html ja foi feita via Edit antes deste
script rodar: foi acrescentada uma nova secao "Aplicacao da Lei Penal --
Complementos (vacatio legis, lei penal em branco, sentenca estrangeira)" ao
const TEORIA_DIREITO_PENAL_PCPE ja existente (mesma materia, nao um deck
novo), cobrindo so os pontos genuinamente novos identificados no PDF:
vacatio legis padrao de 45 dias (LINDB, art. 1); a impossibilidade de
aplicar novatio legis in mellius durante a propria vacatio legis; abolitio
criminis temporaria / atipicidade momentanea (STJ, REsp 1.311.408, exemplo
do art. 30 da Lei 10.826/2003); extincao da reincidencia em caso de
abolitio criminis; distincao diplomata (imunidade absoluta) x consul
(imunidade relativa); embaixada nao ser territorio estrangeiro; distincao
crimes a distancia x crimes plurilocais; os 5 requisitos do art. 788 do
CPP para homologacao de sentenca penal estrangeira; a nova hipotese de
homologacao criada pela Lei de Migracao (13.445/2017) para transferencia
de execucao de pena, incluindo o caso real do STJ sobre perdimento de
imovel por lavagem de dinheiro (Convencao de Palermo); retroatividade do
complemento de normas penais em branco homogeneas x heterogeneas (com e
sem carater transitorio, incluindo o caso real do lanca-perfume, HC 94.397
STF); o conceito de lei intermediaria; e a pegadinha classica de trocar
teoria da atividade (tempo) por teoria da ubiquidade (lugar) na Sumula 711.

Como o PDF e majoritariamente duplicado, as 20 questoes deste round NAO
sao uma transcricao mecanica das (muitas) questoes Certo/Errado do PDF --
foram escritas originalmente (no formato MC exigido para PC-PE), cada uma
testando um dos fatos novos acima, para nao repetir o que ja e cobrado
pelas questoes do gen37.

Este script cuida so de: (1) acrescentar as questoes a questions.json,
(2) regenerar estudo-cebraspe-ma.html a partir do app-template.html ja
editado.
"""
import json

MC_QUESTIONS = [
    (
        "Salvo disposição contrária, de acordo com a Lei de Introdução às Normas do Direito Brasileiro (LINDB), a lei brasileira, quando não fixa seu próprio prazo de vigência, começa a vigorar em todo o país:",
        ["Imediatamente após sua publicação.", "45 (quarenta e cinco) dias depois de oficialmente publicada.", "90 (noventa) dias depois de oficialmente publicada.", "6 (seis) meses depois de oficialmente publicada, em qualquer hipótese.", "30 (trinta) dias depois de oficialmente publicada."],
        1,
        "3.1 — Aplicação da Lei Penal no Tempo: Vacatio Legis",
        "Correto o item B. Nos termos do art. 1º da LINDB, salvo disposição contrária, a lei começa a vigorar em todo o país 45 dias depois de oficialmente publicada — é a regra residual, usada quando a própria lei não fixa sua data de entrada em vigor. A própria lei pode fixar prazo diferente (maior ou menor), como fez o próprio Código Penal de 1940."
    ),
    (
        "Durante o período de vacatio legis de uma nova lei penal, é correto afirmar que:",
        ["A nova lei já pode ser aplicada, desde que seja para beneficiar o réu.", "A nova lei não pode ser aplicada em nenhuma hipótese, nem mesmo para beneficiar o réu, pois seus efeitos só se iniciam com a entrada em vigor.", "A nova lei pode ser aplicada apenas aos crimes permanentes.", "A nova lei pode ser aplicada se o réu expressamente concordar.", "A nova lei já revoga tacitamente a lei anterior desde a publicação."],
        1,
        "3.1 — Aplicação da Lei Penal no Tempo: Vacatio Legis",
        "Correto o item B. A doutrina majoritária rejeita a aplicação de lei nova (ainda que mais benéfica) durante sua vacatio legis, por não fazer sentido admitir uma \"vacatio sem vacatio\" — os efeitos da norma só começam no dia em que ela efetivamente entra em vigor."
    ),
    (
        "O fenômeno jurídico pelo qual uma conduta, em determinado período, deixa de ser considerada típica em razão da suspensão temporária dos efeitos de uma norma incriminadora — também chamado de atipicidade momentânea — denomina-se:",
        ["Novatio legis in mellius.", "Abolitio criminis temporária (vacatio legis indireta).", "Lei penal excepcional.", "Continuidade normativo-típica.", "Extra-atividade maléfica."],
        1,
        "3.1 — Aplicação da Lei Penal no Tempo: Abolitio Criminis Temporária",
        "Correto o item B. O STJ (REsp 1.311.408) reconhece a abolitio criminis temporária (ou vacatio legis indireta) como a atipicidade momentânea de uma conduta, com efeitos erga omnes. Exemplo clássico: o art. 30 da Lei nº 10.826/2003 (Estatuto do Desarmamento), que deu prazo para os possuidores de arma de fogo não registrada regularizarem o registro — durante esse prazo, a posse irregular não configurava crime."
    ),
    (
        "Em caso de abolitio criminis, a reincidência decorrente do crime abolido:",
        ["Subsiste integralmente, como efeito secundário da condenação.", "É extinta, já que a abolitio criminis extingue todos os efeitos penais da sentença condenatória.", "Subsiste, mas apenas para fins de maus antecedentes.", "Depende de requerimento expresso do condenado para ser extinta.", "Subsiste até o trânsito em julgado de nova sentença."],
        1,
        "3.1 — Aplicação da Lei Penal no Tempo: Abolitio Criminis",
        "Correto o item B, nos termos do art. 2º, caput, do CP. A abolitio criminis extingue TODOS os efeitos penais decorrentes da sentença condenatória — inclusive a reincidência e os maus antecedentes —, mas não afasta os efeitos civis (ex.: dever de reparar o dano)."
    ),
    (
        "Quanto à imunidade de agentes diplomáticos e consulares em relação à lei penal brasileira, é correto afirmar que:",
        ["O diplomata goza de imunidade absoluta, independentemente do crime cometido; o cônsul goza de imunidade apenas relativa, restrita aos crimes relacionados à sua atividade consular.", "Tanto o diplomata quanto o cônsul gozam de imunidade absoluta, para qualquer crime.", "Tanto o diplomata quanto o cônsul gozam apenas de imunidade relativa.", "O cônsul goza de imunidade absoluta; o diplomata, apenas relativa.", "Nenhum dos dois goza de qualquer imunidade perante a lei brasileira."],
        0,
        "3.4 — Territorialidade e Extraterritorialidade: Imunidades Diplomática e Consular",
        "Correto o item A. O diplomata tem imunidade ABSOLUTA perante a lei brasileira (Convenção de Viena), independentemente do crime cometido; já o cônsul tem imunidade apenas RELATIVA, restrita aos crimes ligados à sua atividade consular/administrativa."
    ),
    (
        "Em relação ao território nacional para fins penais, é correto afirmar que a embaixada de um país estrangeiro localizada no Brasil:",
        ["É considerada extensão do território do país que ela representa.", "É considerada território brasileiro comum, não configurando extensão do território estrangeiro, ressalvada a imunidade pessoal do diplomata.", "É considerada território neutro, sem soberania de nenhum país.", "Submete-se exclusivamente às regras de direito internacional, nunca à lei brasileira.", "É equiparada a embarcação ou aeronave estrangeira de propriedade privada."],
        1,
        "3.4 — Territorialidade e Extraterritorialidade: Embaixada",
        "Correto o item B. A embaixada estrangeira situada no Brasil continua sendo território brasileiro comum — o que afasta a aplicação da lei brasileira, nesses casos, é a imunidade pessoal do diplomata, não o \"espaço físico\" da embaixada."
    ),
    (
        "Assinale a alternativa correta sobre crimes à distância e crimes plurilocais:",
        ["Crimes à distância são aqueles em que a conduta ocorre em um país e o resultado em outro, resolvidos pela teoria da ubiquidade (art. 6º do CP); crimes plurilocais ocorrem dentro de um único país, mas em comarcas diferentes, resolvidos por regras processuais.", "Crimes à distância e crimes plurilocais são sinônimos e seguem exatamente a mesma regra do art. 6º do CP.", "Crimes plurilocais são resolvidos pela teoria da atividade; crimes à distância, pela teoria do resultado.", "O art. 6º do CP regula tanto os crimes à distância quanto os plurilocais, de forma idêntica.", "Crimes à distância só existem quando praticados por meio de aeronaves ou embarcações."],
        0,
        "3.4 — Territorialidade e Extraterritorialidade: Crimes à Distância x Plurilocais",
        "Correto o item A. Crimes à distância (espaço máximo) envolvem dois países e são resolvidos pela teoria da ubiquidade (art. 6º, CP); crimes plurilocais ocorrem dentro do mesmo país, em comarcas diferentes, e são resolvidos por regras processuais (ex.: art. 70 do CPP)."
    ),
    (
        "São requisitos para a homologação de sentença penal estrangeira, nos termos do art. 788 do Código de Processo Penal, EXCETO:",
        ["Estar revestida das formalidades externas necessárias, segundo a legislação do país de origem.", "Haver sido proferida por juiz competente, mediante citação regular, segundo a legislação de origem.", "Ter passado em julgado.", "Estar devidamente autenticada por cônsul brasileiro e acompanhada de tradução por tradutor público.", "Ter sido previamente registrada em cartório de títulos e documentos no Brasil."],
        4,
        "3.4 — Eficácia de Sentença Estrangeira: Requisitos do Art. 788, CPP",
        "Correto o item E (é a exceção pedida). Os requisitos reais do art. 788 do CPP são os das alternativas A a D; não existe exigência de prévio registro em cartório de títulos e documentos como condição para a homologação."
    ),
    (
        "A Lei nº 13.445/2017 (Lei de Migração) criou uma nova hipótese de homologação de sentença penal estrangeira, consistente em:",
        ["Sujeitar o condenado a medida de segurança no Brasil.", "Obrigar o condenado à reparação do dano causado no exterior.", "Transferir para o Brasil a execução da pena de pessoa condenada em território estrangeiro que seja nacional ou tenha residência habitual ou vínculo pessoal no Brasil.", "Permitir a extradição automática do condenado, independentemente de tratado.", "Dispensar a competência do STJ para homologação de sentenças penais estrangeiras."],
        2,
        "3.4 — Eficácia de Sentença Estrangeira: Lei de Migração",
        "Correto o item C. Além das hipóteses do art. 9º do CP (medida de segurança e reparação do dano), a Lei de Migração (art. 100) criou a hipótese de transferência para o Brasil da execução de pena de condenado no exterior que seja nacional ou tenha vínculo pessoal com o Brasil, também sujeita à homologação do STJ."
    ),
    (
        "Segundo entendimento do STJ, é possível a homologação de sentença penal estrangeira que determine o perdimento de imóvel situado no Brasil, quando:",
        ["O bem for produto de crime de lavagem de dinheiro, por força do art. 9º, I, do Código Penal e da Convenção das Nações Unidas contra o Crime Organizado Transnacional (Convenção de Palermo).", "O condenado for brasileiro nato.", "Houver pedido expresso do Ministério Público brasileiro, independentemente de homologação.", "O imóvel estiver localizado em zona rural.", "Jamais é possível, por violar a soberania nacional sobre bens imóveis."],
        0,
        "3.4 — Eficácia de Sentença Estrangeira: Perdimento de Bens",
        "Correto o item A. O STJ já homologou sentença penal estrangeira determinando o perdimento de imóvel situado no Brasil por ser produto de lavagem de dinheiro, com fundamento no art. 9º, I, do CP e na Convenção de Palermo."
    ),
    (
        "Quanto à retroatividade do complemento de uma norma penal em branco HOMOGÊNEA (complementada por outra lei), é correto afirmar que:",
        ["A alteração do complemento, quando benéfica ao réu, retroage, pois a norma complementar, como lei ordinária que é, também se sujeita às regras de retroatividade e irretroatividade.", "A alteração do complemento jamais retroage, por se tratar de norma penal em branco.", "A alteração do complemento só retroage se o complemento for um ato administrativo.", "A alteração do complemento retroage apenas quando se tratar de lei temporária.", "A alteração do complemento nunca produz efeitos sobre fatos já praticados."],
        0,
        "3.1 — Aplicação da Lei Penal no Tempo: Normas Penais em Branco",
        "Correto o item A. Na norma penal em branco homogênea, o complemento é outra lei — e, como lei, também se sujeita à retroatividade benéfica, podendo gerar abolitio criminis ou novatio legis in mellius."
    ),
    (
        "No caso concreto em que a ANVISA, por meio de Resolução, retirou temporariamente o cloreto de etila (lança-perfume) da lista de substâncias psicotrópicas de uso proscrito, o STF entendeu configurada:",
        ["Uma irrelevância penal absoluta, sem qualquer efeito sobre processos em curso.", "Uma abolitio criminis, tornando atípicos o uso e o tráfico da substância durante o período em que vigorou a retirada, com retroatividade da norma complementar benéfica.", "Uma hipótese de ultratividade obrigatória da norma incriminadora anterior.", "Uma novatio legis incriminadora.", "A manutenção da tipicidade, por se tratar de ato administrativo e não de lei em sentido estrito."],
        1,
        "3.1 — Aplicação da Lei Penal no Tempo: Normas Penais em Branco",
        "Correto o item B (STF, HC 94.397). Na norma penal em branco heterogênea com complemento NÃO transitório, a alteração benéfica do ato administrativo retroage normalmente — no caso do lança-perfume, configurou abolitio criminis."
    ),
    (
        "Quando a norma penal em branco heterogênea for complementada por um ato administrativo de caráter transitório (ex.: tabela oficial de preços), a alteração benéfica desse complemento:",
        ["Retroage normalmente, como qualquer lei penal benéfica.", "Não retroage em favor do réu, pelos mesmos fundamentos que justificam a ultratividade das leis penais temporárias e excepcionais.", "Retroage apenas se o réu for primário.", "Retroage apenas após homologação do STJ.", "Torna o fato atípico desde a prática da conduta, independentemente de qualquer outro requisito."],
        1,
        "3.1 — Aplicação da Lei Penal no Tempo: Normas Penais em Branco",
        "Correto o item B. Quando o complemento é transitório, sua alteração benéfica NÃO retroage, pelos mesmos fundamentos da ultratividade das leis temporárias e excepcionais — do contrário, essas normas perderiam toda a eficácia dissuasória."
    ),
    (
        "Denomina-se lei intermediária aquela que:",
        ["Não estava em vigor nem no momento da prática do fato nem no momento da prolação da sentença, mas vigorou em momento intermediário entre esses dois marcos — e, se for a mais favorável de todas, será retroativa em relação ao fato e ultrativa em relação à sentença.", "É a lei vigente exclusivamente no momento da prática do crime.", "É a lei vigente exclusivamente no momento da sentença.", "É sinônimo de lei excepcional ou temporária.", "Nunca pode ser aplicada, por não ter vigorado em nenhum dos dois marcos temporais relevantes."],
        0,
        "3.1 — Aplicação da Lei Penal no Tempo: Lei Intermediária",
        "Correto o item A. A lei intermediária, se for a mais benéfica entre as que se sucederam no tempo, é aplicada mesmo não tendo vigorado nem no momento do fato nem no da sentença — sendo retroativa quanto ao fato e ultrativa quanto à sentença."
    ),
    (
        "Segundo a doutrina majoritária, uma lei penal nova mais benéfica ao réu:",
        ["Pode ser aplicada imediatamente após sua publicação, independentemente do decurso do prazo de vacatio legis.", "Não pode ser aplicada antes do decurso de sua vacatio legis, sob pena de se admitir a existência de uma \"vacatio sem vacatio\".", "Só pode ser aplicada após dois anos de sua publicação.", "Deve ser aplicada retroativamente mesmo durante sua vacatio, por força do princípio da retroatividade benéfica.", "Nunca poderá retroagir, ainda que seja mais benéfica."],
        1,
        "3.1 — Aplicação da Lei Penal no Tempo: Vacatio Legis",
        "Correto o item B. A doutrina majoritária entende que nem mesmo a lei mais benéfica pode ser aplicada antes do fim de sua própria vacatio legis."
    ),
    (
        "É correto afirmar que o Código Penal brasileiro adota, para determinar o TEMPO do crime, a:",
        ["Teoria da ubiquidade, prevista no art. 6º do CP.", "Teoria do resultado.", "Teoria da atividade, prevista no art. 4º do CP — considera-se praticado o crime no momento da ação ou omissão, ainda que outro seja o momento do resultado.", "Teoria mista, aplicável tanto ao tempo quanto ao lugar do crime.", "Teoria da ubiquidade temperada."],
        2,
        "3.2 — Tempo do Crime: Teoria da Atividade",
        "Correto o item C. O tempo do crime é determinado pela teoria da ATIVIDADE (art. 4º, CP); a teoria da ubiquidade (art. 6º) é usada para o LUGAR do crime — pegadinha clássica de banca trocar uma pela outra."
    ),
    (
        "Um crime permanente teve início sob a vigência de uma lei penal menos grave, mas sua execução se prolongou até a entrada em vigor de nova lei, mais severa, antes de cessar a permanência. Nessa hipótese, nos termos da Súmula 711 do STF:",
        ["Aplica-se sempre a lei mais branda, vigente no início da execução, por força da irretroatividade da lei penal maléfica.", "Aplica-se a lei mais grave, vigente no momento em que cessou a permanência, pois sua vigência era anterior à cessação da continuidade/permanência.", "Aplica-se a lei intermediária que porventura tenha vigorado durante a execução.", "O agente não pode ser responsabilizado, por conflito insolúvel de leis no tempo.", "Aplica-se a lei mais branda, por analogia in bonam partem."],
        1,
        "3.2 — Tempo do Crime: Súmula 711 STF",
        "Correto o item B. A Súmula 711 do STF determina que a lei penal mais grave aplica-se ao crime continuado ou permanente se sua vigência for anterior à cessação da continuidade ou permanência — ainda se trata de aplicação da teoria da atividade, apenas com o marco temporal deslocado para a cessação da conduta."
    ),
    (
        "Considerando que o Código Penal adota a teoria da atividade para determinar o tempo do crime, se um agente desfere um disparo de arma de fogo contra a vítima em um dia sob a vigência da Lei 'A', e a vítima vem a falecer dias depois, já sob a vigência de uma Lei 'B' mais severa, deverá ser aplicada ao fato:",
        ["A Lei 'B', vigente no momento do resultado morte.", "A Lei 'A', vigente no momento da ação (o disparo), ainda que o resultado tenha ocorrido sob a vigência de outra lei.", "Ambas as leis, cumulativamente.", "A lei mais branda entre as duas, independentemente do momento da ação.", "Nenhuma das duas, por tratar-se de crime impossível."],
        1,
        "3.2 — Tempo do Crime: Teoria da Atividade",
        "Correto o item B. Pela teoria da atividade (art. 4º, CP), considera-se praticado o crime no momento da ação ou omissão, ainda que outro seja o momento do resultado — aplica-se, portanto, a Lei 'A', vigente no momento do disparo."
    ),
    (
        "Para que seja cabível o emprego da analogia em matéria penal, é necessário, EXCETO:",
        ["Que inexista um ato normativo que regule especificamente a situação.", "Que exista uma norma legal que regulamente um caso semelhante.", "Que o fundamento da norma existente também possa ser aplicado ao caso que carece de regulamentação.", "Que o emprego da analogia beneficie o réu.", "Que o juiz identifique uma lacuna proposital do legislador, e não uma omissão involuntária."],
        4,
        "3.6 — Interpretação da Lei Penal: Analogia",
        "Correto o item E (é a exceção pedida). A analogia pressupõe uma lacuna INVOLUNTÁRIA do legislador — se a omissão for proposital (silêncio eloquente), não cabe analogia."
    ),
    (
        "Em relação ao crime de bigamia (art. 235, CP), que criminaliza contrair novo casamento estando o agente ainda casado, a prática de um terceiro ou quarto casamento simultâneo (poligamia) é alcançada pela norma por meio de:",
        ["Analogia in malam partem, vedada no Direito Penal.", "Interpretação extensiva, pelo argumento a minori ad maius (o que é proibido para o menos deve ser proibido para o mais).", "Abolitio criminis.", "Novatio legis incriminadora.", "Interpretação analógica, por haver fórmula casuística seguida de fórmula genérica no tipo penal."],
        1,
        "3.6 — Interpretação da Lei Penal: Interpretação Extensiva",
        "Correto o item B. Trata-se de interpretação extensiva (amplia o alcance da própria norma, sem criar norma nova), justificada pelo argumento a minori ad maius — se contrair um segundo casamento já configura bigamia, contrair um terceiro ou quarto com maior razão também configura."
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
            "disc": "Direito Penal",
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
