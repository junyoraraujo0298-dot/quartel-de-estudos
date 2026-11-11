# -*- coding: utf-8 -*-
"""
Segundo conteudo de Direito Administrativo do app (PC-PE) -- a partir do PDF
"Principios Explicitos - Parte I e II" (Focus Concursos, prof. Kaique
Balbuena), que aprofunda o item 5.2 ("Principios expressos e implicitos da
administracao publica") do PROGRAMA_PCPE_AGENTE oficial.

Ao contrario do PDF anterior de Direito Administrativo (Fontes do Direito
Administrativo, gen40), que ja estava integralmente coberto, este PDF traz
conteudo GENUINAMENTE NOVO: o deck TEORIA_DIREITO_ADMINISTRATIVO_PCPE so
tinha, ate aqui, a secao sobre fontes do direito administrativo -- nao
havia nada sobre os principios constitucionais expressos (LIMPE).

A mudanca estrutural em app-template.html ja foi feita via Edit antes deste
script rodar: foi acrescentada uma nova secao "Principios Expressos da
Administracao Publica (LIMPE)" ao const TEORIA_DIREITO_ADMINISTRATIVO_PCPE
ja existente (mesma materia, nao um deck novo), cobrindo: o mnemonico LIMPE
e a distincao entre principios originarios (Legalidade, Impessoalidade,
Moralidade, Publicidade) e o principio incorporado pela EC 19/98
(Eficiencia); Legalidade (conceito, duas vertentes particular x
administracao, legalidade em sentido amplo, atuacao vinculada x
discricionaria, excecoes/constricoes segundo Celso Antonio Bandeira de
Mello, legalidade x legitimidade segundo Hely Lopes Meirelles, legalidade
x reserva legal, Sumula 636 STF); Impessoalidade (duas vertentes --
isonomia e vedacao a promocao pessoal --, art. 37 §1º CF, nepotismo pela
Sumula Vinculante 13 do STF e a excecao para agentes politicos, agente de
fato e teoria da aparencia); Moralidade (moralidade administrativa x moral
comum, dever de probidade, moralidade objetiva segundo o STF); Publicidade
(eficacia x validade do ato, publicidade mitigada -- nao excecao --, nos
casos de seguranca do Estado/sociedade/privacidade); e Eficiencia
(principio incorporado pela EC 19/98, consequencias constitucionais --
contratos de gestao, avaliacao de desempenho, exoneracao por insuficiencia
de desempenho ou por excesso de despesa com pessoal --, e a distincao
entre eficiencia, eficacia e efetividade).

O PDF e majoritariamente dedicado aos principios EXPRESSOS (LIMPE) -- o
amplo banco de questoes do PDF (22 "Questoes para Treinar" + 7 "Questoes
de Sala") tambem testa bastante os principios IMPLICITOS (autotutela,
supremacia do interesse publico, indisponibilidade, protecao a confianca),
que nao sao o foco deste PDF e ainda nao tem teoria propria no app --
essas questoes foram deliberadamente DEIXADAS DE FORA deste round, para
nao cobrar fato que nao tem teoria correspondente ainda (ficam para um
proximo PDF/round especifico de principios implicitos). As 20 questoes
deste round foram escritas originalmente (nao sao transcricao literal das
questoes do PDF, que nao trazem citacao de banca/orgao/ano real), cada uma
testando um fato genuinamente novo sobre os principios expressos LIMPE.

Este script cuida so de: (1) acrescentar as questoes a questions.json,
(2) regenerar estudo-cebraspe-ma.html a partir do app-template.html ja
editado.
"""
import json

MC_QUESTIONS = [
    (
        "Em relação ao princípio da legalidade, é correto afirmar que:",
        ["O particular pode fazer tudo o que a lei não proíbe (autonomia da vontade), ao passo que a Administração Pública só pode fazer o que a lei autoriza ou determina (restrição da vontade).", "Tanto o particular quanto a Administração Pública podem fazer tudo o que a lei não proíbe.", "Tanto o particular quanto a Administração Pública só podem fazer o que a lei expressamente autoriza.", "O particular só pode fazer o que a lei autoriza; a Administração Pública pode fazer tudo o que a lei não proíbe.", "A legalidade não distingue particular de Administração Pública, aplicando-se de forma idêntica a ambos."],
        0,
        "5.2 — Princípios Expressos: Legalidade",
        "Correto o item A. O particular é caracterizado pela autonomia da vontade (faz tudo que a lei não proíba); já a Administração Pública somente pode atuar segundo o que a lei autoriza ou determina (restrição da vontade) — art. 5º, II, c/c art. 37, caput, da CF."
    ),
    (
        "O princípio da legalidade, previsto no art. 37, caput, da Constituição Federal:",
        ["Aplica-se à Administração Pública direta e indireta de todos os Poderes (Executivo, Legislativo e Judiciário) e de todas as esferas da Federação, não se restringindo ao Poder Executivo federal.", "Aplica-se apenas ao Poder Executivo federal.", "Aplica-se apenas à Administração Pública direta, não alcançando a indireta.", "Aplica-se apenas aos Estados e ao Distrito Federal, não à União nem aos Municípios.", "Aplica-se apenas ao Poder Judiciário, no exercício de sua função atípica administrativa."],
        0,
        "5.2 — Princípios Expressos: Legalidade",
        "Correto o item A, nos termos literais do art. 37, caput, da CF: a legalidade vincula a Administração Pública direta e indireta de qualquer dos Poderes da União, dos Estados, do DF e dos Municípios."
    ),
    (
        "A legalidade e a reserva legal, em Direito Administrativo:",
        ["Não podem ser equiparadas: a legalidade engloba medidas provisórias, resoluções, decretos e todas as medidas de reserva legal (sentido amplo), ao passo que a reserva legal inclui somente as medidas de lei em sentido estrito (leis ordinárias, complementares e delegadas).", "São sinônimos, podendo os termos ser usados indistintamente.", "A reserva legal é mais ampla que a legalidade, abrangendo também atos infralegais.", "A legalidade se restringe à lei em sentido estrito; a reserva legal abrange também os decretos regulamentares.", "Nenhuma das duas abrange medidas provisórias."],
        0,
        "5.2 — Princípios Expressos: Legalidade x Reserva Legal",
        "Correto o item A. A legalidade é o conceito mais amplo, incluindo toda a reserva legal mais os demais atos normativos (decretos, resoluções, medidas provisórias); a reserva legal é mais restrita, abrangendo apenas a lei em sentido estrito."
    ),
    (
        "Segundo o professor Celso Antônio Bandeira de Mello, o princípio da legalidade pode sofrer \"constrições\" (restrições), em função de circunstâncias excepcionais expressamente previstas no texto constitucional, tais como:",
        ["A edição de medida provisória, a decretação de estado de defesa e a decretação de estado de sítio pelo Presidente da República.", "A edição de decretos regulamentares por qualquer autoridade administrativa.", "A edição de portarias internas de órgãos públicos.", "A celebração de contratos administrativos em geral.", "A prática de qualquer ato discricionário pela Administração Pública."],
        0,
        "5.2 — Princípios Expressos: Legalidade",
        "Correto o item A. O CEBRASPE já considerou correta a assertiva de que a medida provisória, o estado de defesa e o estado de sítio constituem exceção (constrição) ao princípio da legalidade na administração pública."
    ),
    (
        "Segundo o professor Hely Lopes Meirelles, a diferença entre legalidade e legitimidade está em que:",
        ["Cumprir simplesmente a lei na frieza do seu texto é legalidade; atendê-la na letra e no espírito, respeitando também os demais princípios administrativos (moralidade, honestidade, probidade, interesse público), é legitimidade.", "Legalidade e legitimidade são sinônimos perfeitos, sem qualquer distinção doutrinária.", "Legitimidade é conceito exclusivo do direito eleitoral, sem aplicação ao Direito Administrativo.", "Legalidade se refere ao espírito da lei; legitimidade, apenas à sua letra.", "Legitimidade é requisito de validade apenas dos atos discricionários, nunca dos vinculados."],
        0,
        "5.2 — Princípios Expressos: Legalidade x Legitimidade",
        "Correto o item A, segundo a doutrina de Hely Lopes Meirelles: a legalidade atende aos ditames da lei em sentido amplo; a legitimidade vai além, exigindo também a observância dos demais princípios administrativos."
    ),
    (
        "Segundo a Súmula 636 do STF, não cabe recurso extraordinário por contrariedade ao princípio constitucional da legalidade quando:",
        ["A sua verificação pressuponha rever a interpretação dada a normas infraconstitucionais pela decisão recorrida.", "A decisão recorrida tiver sido proferida por tribunal estadual.", "O recorrente for a própria Fazenda Pública.", "O valor da causa for inferior a determinado teto legal.", "A matéria já tiver sido pacificada por súmula vinculante do STF."],
        0,
        "5.2 — Princípios Expressos: Legalidade",
        "Correto o item A, nos termos literais da Súmula 636 do STF — quando a alegada ofensa à legalidade depender de reexame de normas infraconstitucionais, não há questão constitucional autônoma apta a ensejar recurso extraordinário."
    ),
    (
        "\"Esse princípio acaba completando a ideia de que o administrador é um executor do ato, que serve de veículo de manifestação da vontade estatal e, portanto, as realizações administrativo-governamentais não são do agente político, mas da entidade pública em nome da qual atuou\" (José Afonso da Silva, adaptado). O autor está tratando do princípio constitucional da:",
        ["Impessoalidade.", "Eficiência.", "Moralidade.", "Legalidade.", "Publicidade."],
        0,
        "5.2 — Princípios Expressos: Impessoalidade",
        "Correto o item A. A impessoalidade impõe que o agente público atue sempre em nome do Estado, nunca em nome próprio — as realizações administrativas pertencem à entidade pública, não ao agente político que as executou."
    ),
    (
        "Situação hipotética: o prefeito de determinado município promoveu campanha publicitária para combate ao mosquito da dengue; nos panfletos, constava sua imagem, além do símbolo de sua campanha eleitoral. Nesse caso:",
        ["Há ofensa ao princípio da impessoalidade, na vertente de vedação à promoção pessoal, por força do art. 37, § 1º, da CF.", "Não há qualquer ofensa a princípio constitucional, por se tratar de campanha de saúde pública.", "Há ofensa apenas ao princípio da eficiência, não ao da impessoalidade.", "Há ofensa ao princípio da legalidade, mas não ao da impessoalidade.", "A conduta é plenamente lícita, desde que a campanha tenha sido aprovada pela Câmara Municipal."],
        0,
        "5.2 — Princípios Expressos: Impessoalidade",
        "Correto o item A. O art. 37, § 1º, da CF veda que a publicidade de atos, obras e campanhas dos órgãos públicos contenha nomes, símbolos ou imagens que caracterizem promoção pessoal de autoridades — a presença da imagem do prefeito e do símbolo de sua campanha eleitoral configura clara violação à impessoalidade."
    ),
    (
        "Nos termos da Súmula Vinculante 13 do STF, é vedada, em qualquer dos Poderes e esferas da Federação, a nomeação de:",
        ["Cônjuge, companheiro ou parente em linha reta, colateral ou por afinidade, até o terceiro grau, inclusive, da autoridade nomeante ou de servidor da mesma pessoa jurídica investido em cargo de direção, chefia ou assessoramento, para cargo em comissão, função de confiança ou função gratificada — inclusive mediante designações recíprocas.", "Qualquer pessoa que tenha grau de parentesco com servidor público, mesmo que este não ocupe cargo de direção, chefia ou assessoramento.", "Pessoas aprovadas em concurso público que sejam parentes de autoridades.", "Servidores efetivos para cargos de mesma natureza de seu cargo de origem.", "Apenas parentes em linha reta até o segundo grau."],
        0,
        "5.2 — Princípios Expressos: Impessoalidade — Nepotismo",
        "Correto o item A, nos termos literais da Súmula Vinculante 13. A vedação inclui, ainda, o nepotismo cruzado (ajuste mediante designações recíprocas entre autoridades de órgãos diferentes)."
    ),
    (
        "Segundo o entendimento majoritário do Supremo Tribunal Federal, a vedação ao nepotismo prevista na Súmula Vinculante 13:",
        ["Não alcança os agentes políticos, como secretários municipais nomeados pelo prefeito.", "Alcança igualmente agentes políticos e servidores ocupantes de cargo em comissão, sem qualquer distinção.", "Aplica-se apenas à esfera federal, não aos Estados e Municípios.", "Foi revogada por emenda constitucional posterior.", "Aplica-se apenas a cargos de natureza técnica, nunca a cargos de chefia."],
        0,
        "5.2 — Princípios Expressos: Impessoalidade — Nepotismo",
        "Correto o item A (STF, Rcl 28.449 AgR). O entendimento majoritário do STF é de que a vedação da Súmula Vinculante 13 não alcança os agentes políticos (como secretários municipais), por não se tratar de cargo em comissão ou função comissionada no sentido técnico da súmula."
    ),
    (
        "Um indivíduo tomou posse em cargo público efetivo utilizando-se de diploma falso para comprovar escolaridade, tendo desempenhado efetivamente as funções do cargo por determinado período até a descoberta da fraude. Quanto aos atos por ele praticados nesse período, é correto afirmar, com base na impessoalidade e na boa-fé, que:",
        ["Os atos regulares por ele praticados, em princípio, não devem ser anulados, ainda que o agente tivesse ciência da própria condição irregular — aplica-se a teoria da aparência, pois, para os administrados, o agente parecia legítimo.", "Todos os atos por ele praticados são automaticamente nulos, independentemente de qualquer outra consideração.", "Os atos só são válidos se o agente desconhecia sua própria condição de irregularidade.", "A nulidade do ato de investidura contamina automaticamente todos os atos posteriores por ele praticados.", "Apenas atos praticados após a descoberta da fraude podem ser considerados válidos."],
        0,
        "5.2 — Princípios Expressos: Impessoalidade — Agente de Fato",
        "Correto o item A. É a hipótese do \"funcionário/agente de fato\": o ato de investidura é nulo, mas os atos regulares por ele praticados não devem ser anulados — pela impessoalidade, quem praticou o ato foi a Administração, não o agente; pela boa-fé/teoria da aparência, não se pode lesar terceiros que confiaram na aparente legitimidade do agente."
    ),
    (
        "Na análise da moralidade administrativa, pressuposto de validade de todo ato da Administração Pública, é correto afirmar que:",
        ["A moralidade administrativa é um valor objetivo, não sendo imprescindível avaliar a intenção subjetiva do agente para aferi-la.", "É sempre imprescindível avaliar a intenção subjetiva do agente público para se aferir a moralidade de um ato.", "A moralidade administrativa se confunde integralmente com a moral comum, formada no âmbito familiar e religioso.", "A moralidade administrativa é conceito estritamente subjetivo, variando conforme a interpretação pessoal de cada agente.", "A moralidade administrativa não possui qualquer relação com a legalidade do ato."],
        0,
        "5.2 — Princípios Expressos: Moralidade",
        "Correto o item A (STF, ADI 2.661 MC). A moralidade administrativa deve ser vista como valor objetivo, extraído do próprio ordenamento jurídico, independente das intenções ou noções pessoais (subjetivas) do agente público — avaliar a \"intenção\" do agente não é imprescindível."
    ),
    (
        "O princípio da moralidade, em relação ao princípio da legalidade, é entendido pela doutrina como:",
        ["Um complemento à legalidade, pois nem tudo que é legal é moral — o desrespeito à moralidade afeta a própria legalidade do ato, podendo gerar sua nulidade e, ainda, responsabilização por improbidade administrativa.", "Um princípio totalmente independente e sem qualquer relação com a legalidade.", "Um princípio subordinado e menos importante que a legalidade, sem capacidade de gerar nulidade de atos.", "Um sinônimo perfeito de legalidade, sem distinção prática entre os dois.", "Um princípio aplicável apenas a atos discricionários, nunca a atos vinculados."],
        0,
        "5.2 — Princípios Expressos: Moralidade",
        "Correto o item A. A moralidade complementa a legalidade: o dever de probidade (ética, decoro, honestidade e boa-fé) deve acompanhar o cumprimento da lei — um ato formalmente legal, mas imoral, é nulo."
    ),
    (
        "A publicação de um ato administrativo praticado com cumprimento de todas as formalidades legais, em órgão oficial de imprensa (como o Diário Oficial da União, na esfera federal):",
        ["Não é condição de validade ou de forma do ato, mas sim condição de sua eficácia — o ato já válido permanece ineficaz até a publicação.", "É condição de validade do ato, de modo que o ato praticado sem publicação é nulo desde a origem.", "É mera formalidade dispensável, sem qualquer efeito jurídico sobre o ato.", "É condição de existência do ato, e não de validade nem de eficácia.", "Só é exigida para atos normativos, nunca para atos administrativos individuais."],
        0,
        "5.2 — Princípios Expressos: Publicidade",
        "Correto o item A. Um ato administrativo regularmente praticado é válido desde logo, mas permanece INEFICAZ até sua publicação em órgão oficial de imprensa — a publicação é condição de eficácia, não de validade ou forma."
    ),
    (
        "Em relação ao princípio da publicidade, é correto afirmar que:",
        ["Não existe exceção ao princípio da publicidade, mas sim situações em que a publicidade é mitigada (reduzida), como nos casos de segurança do Estado, segurança da sociedade e privacidade do indivíduo.", "Existem diversas exceções ao princípio da publicidade, que dispensam totalmente a Administração de publicar atos em determinadas hipóteses legais.", "A publicidade é absoluta, não comportando qualquer espécie de restrição, ainda que em defesa da intimidade do cidadão.", "A publicidade só se aplica a atos da Administração direta, não alcançando a indireta.", "A publicidade pode ser substituída, em qualquer caso, pela mera divulgação em redes sociais oficiais."],
        0,
        "5.2 — Princípios Expressos: Publicidade",
        "Correto o item A. A regra é a publicidade; não há exceção a ela, mas apenas mitigação (restrição) em hipóteses expressamente previstas (art. 5º, XXXIII, CF): segurança do Estado, segurança da sociedade e privacidade/intimidade do indivíduo."
    ),
    (
        "Como um dos princípios da administração pública brasileira, a publicidade destina-se, entre outras finalidades, a:",
        ["Garantir a transparência dos atos dos agentes públicos, permitindo um controle popular mais eficiente da atuação administrativa do Estado.", "Garantir exclusivamente a validade formal dos atos administrativos, sem qualquer relação com transparência.", "Autorizar a promoção pessoal de autoridades em atos, obras e campanhas públicas.", "Substituir integralmente o controle judicial sobre os atos da Administração Pública.", "Dispensar a Administração de prestar contas aos órgãos de controle externo."],
        0,
        "5.2 — Princípios Expressos: Publicidade",
        "Correto o item A. Além de condição de eficácia do ato, a publicidade exige transparência da atuação administrativa, permitindo um controle popular mais eficiente — inclusive em casos como a exigência de votações abertas em processos de grande repercussão institucional."
    ),
    (
        "O princípio da eficiência, também chamado de \"dever de boa administração\", foi inserido no art. 37, caput, da Constituição Federal:",
        ["Pela Emenda Constitucional nº 19/1998, sendo, por isso, classificado como princípio incorporado (e não originário, como a legalidade, a impessoalidade, a moralidade e a publicidade).", "Desde a redação originária da Constituição Federal de 1988, junto com os demais princípios do LIMPE.", "Por lei ordinária federal, podendo ser revogado por lei de igual hierarquia.", "Pela Emenda Constitucional nº 45/2004 (Reforma do Judiciário).", "Por entendimento meramente doutrinário, sem previsão constitucional expressa."],
        0,
        "5.2 — Princípios Expressos: Eficiência",
        "Correto o item A. A Eficiência foi acrescentada ao art. 37, caput, da CF pela EC nº 19/1998 — diferentemente de Legalidade, Impessoalidade, Moralidade e Publicidade, que já constavam da redação originária da CF/88 (por isso são chamados de originários, e a Eficiência, de incorporada)."
    ),
    (
        "A obrigação do agente público de fazer somente o que a lei permite corresponde, mais precisamente, ao princípio da:",
        ["Legalidade, e não ao da eficiência, que se relaciona à busca do melhor custo-benefício e da qualidade na prestação dos serviços públicos.", "Eficiência, pois esse princípio abrange toda e qualquer limitação da atuação do agente público pela lei.", "Moralidade, por se tratar de limite ético à atuação do agente.", "Publicidade, já que a transparência pressupõe atuação estritamente legal.", "Impessoalidade, por vedar que o agente atue além do que a lei permite."],
        0,
        "5.2 — Princípios Expressos: Eficiência x Legalidade",
        "Correto o item A. Fazer somente o que a lei permite é, tecnicamente, a definição do princípio da LEGALIDADE, não da eficiência — pegadinha clássica de banca, que tenta atribuir à eficiência um conceito que pertence a outro princípio do LIMPE."
    ),
    (
        "Em razão do princípio da eficiência, a Constituição Federal prevê, EXCETO:",
        ["A celebração de contratos de gestão entre órgãos/entidades públicos, com fixação de metas de desempenho (art. 37, § 8º).", "A avaliação especial de desempenho do servidor público como condição obrigatória para aquisição da estabilidade (art. 41, § 4º).", "A possibilidade de exoneração de servidor estável com base em avaliação periódica de desempenho insuficiente (art. 41, III).", "A possibilidade de exoneração de servidores, estáveis ou não, em razão de excesso de despesa com pessoal (art. 169, §§ 3º e 4º).", "A vedação absoluta e permanente à exoneração de qualquer servidor público estável, mesmo em caso de insuficiência de desempenho comprovada."],
        4,
        "5.2 — Princípios Expressos: Eficiência",
        "Correto o item E (é a exceção pedida — a única alternativa falsa). As demais (A a D) são consequências constitucionais reais do princípio da eficiência; a exoneração de servidor estável por insuficiência de desempenho (art. 41, III) e por excesso de despesa com pessoal (art. 169) são, justamente, hipóteses constitucionalmente previstas, não vedadas."
    ),
    (
        "Em relação aos conceitos de eficiência, eficácia e efetividade na Administração Pública, é correto afirmar que:",
        ["Eficiência diz respeito à relação custo-benefício (utilização mais adequada dos recursos); eficácia refere-se ao sucesso da atuação administrativa (exame dos resultados em si); e efetividade compara o que foi efetivamente alcançado com as metas planejadas.", "Os três termos são sinônimos perfeitos, podendo ser usados indistintamente em qualquer contexto.", "Eficácia é sinônimo de custo-benefício; eficiência mede apenas o cumprimento de metas planejadas.", "Efetividade é sinônimo de legalidade; eficiência, de moralidade.", "Eficiência mede exclusivamente o tempo de duração de um processo administrativo."],
        0,
        "5.2 — Princípios Expressos: Eficiência x Eficácia x Efetividade",
        "Correto o item A. São três conceitos distintos e frequentemente confundidos: eficiência (meio — custo-benefício), eficácia (resultado em si — sucesso da atuação) e efetividade (comparação entre o planejado e o realmente cumprido)."
    ),
    (
        "Assinale a alternativa que apresenta APENAS princípios expressamente previstos no art. 37, caput, da Constituição Federal de 1988:",
        ["Legalidade, impessoalidade, moralidade, publicidade e eficiência.", "Legalidade, moralidade, eficiência, continuidade dos serviços públicos e supremacia do interesse público.", "Legalidade, moralidade, impessoalidade, eficiência e supremacia do interesse público.", "Legalidade, moralidade, impessoalidade, publicidade, proporcionalidade e autotutela.", "Legalidade, moralidade, eficiência e continuidade dos serviços públicos."],
        0,
        "5.2 — Princípios Expressos: LIMPE",
        "Correto o item A. Apenas Legalidade, Impessoalidade, Moralidade, Publicidade e Eficiência (LIMPE) são EXPRESSOS no art. 37, caput, da CF; supremacia do interesse público, indisponibilidade, autotutela, continuidade dos serviços públicos e proporcionalidade são princípios IMPLÍCITOS, reconhecidos pela doutrina e jurisprudência, mas não positivados nesse dispositivo."
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
            "disc": "Direito Administrativo",
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
