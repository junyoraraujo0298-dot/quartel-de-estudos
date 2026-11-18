# -*- coding: utf-8 -*-
"""
Terceiro conteudo de Direito Administrativo do app (PC-PE) -- a partir do
PDF "Lei n. 8.112/1990" (apostila completa, Focus Concursos), que cobre os
itens 12 ("Agente publico: legislacao pertinente; disposicoes
constitucionais aplicaveis") e 13 ("Cargo, emprego e funcao publica") do
PROGRAMA_PCPE_AGENTE oficial.

Contexto importante: a Lei 8.112/1990 e o Regime Juridico dos Servidores
Publicos Civis da UNIAO (federal) -- nao se aplica literalmente ao PC-PE,
que e cargo ESTADUAL regido pela Lei 6.123/1968 e pela Lei 6.425/1972. Por
isso, este round NAO trata o PDF como "legislacao estadual" (que e item
separado do edital, ja coberto por outro deck), mas sim como doutrina
generica do item 12/13 de Direito Administrativo -- CEBRASPE historicamente
usa a 8.112/90 como lei-modelo para testar esses conceitos (agente
publico, cargo/emprego/funcao, provimento, vacancia, estagio probatorio x
estabilidade, acumulacao, regime disciplinar, PAD) mesmo em certames
estaduais, justamente por ser a lei mais didatica e mais cobrada do genero.

A mudanca estrutural em app-template.html ja foi feita via Edit antes deste
script rodar: foi acrescentada uma nova secao "Agente Publico -- Cargo,
Emprego e Funcao Publica (Lei no 8.112/1990)" ao const
TEORIA_DIREITO_ADMINISTRATIVO_PCPE ja existente (mesma materia, nao um
deck novo), com 17 itens cobrindo: conceito de agente publico e suas
especies; conceito e criacao de cargo publico; cargo efetivo x em comissao
x funcao de confianca; distincao cargo x emprego x funcao publica;
investidura/provimento (originario x derivado); formas de provimento e
Sumula Vinculante 43; prazos de posse e exercicio; estagio probatorio
(ACADIPRORE, 24 meses) x estabilidade (36 meses, EC 19/98); vacancia;
remocao x redistribuicao x substituicao; acumulacao de cargos (regra e
excecoes constitucionais); deveres (art. 116); proibicoes (art. 117);
penalidades disciplinares (rol taxativo); prescricao da acao disciplinar;
e sindicancia x PAD.

O deck TEORIA_DIREITO_ADMINISTRATIVO_PCPE ja tinha as secoes "Fontes do
Direito Administrativo" (item 2 do edital) e "Principios Expressos LIMPE"
(item 5.2) -- esta e a terceira secao, cobrindo os itens 12 e 13. O label
do deck no seletor tambem foi atualizado de "Direito Administrativo --
Fontes do Direito Administrativo (PC-PE)" para apenas "Direito
Administrativo (PC-PE)", ja que o deck deixou de ser so sobre fontes.

As 20 questoes deste round foram escritas originalmente (nao sao
transcricao literal do PDF, que nao traz citacao de banca/orgao/ano real),
cada uma testando um fato novo sobre os itens 12/13. Conteudo do PDF fora
do escopo desses dois itens (direitos e vantagens pecuniarias --
vencimento, ferias, licencas remuneradas, seguridade social, pensoes,
aposentadoria -- que sao tipicamente testados sob a otica da legislacao
ESTADUAL especifica de PE, nao da 8.112 federal) foi deliberadamente
deixado de fora deste round, para nao cobrar fato fora do que realmente
cai no PC-PE.

Este script cuida so de: (1) acrescentar as questoes a questions.json,
(2) regenerar estudo-cebraspe-ma.html a partir do app-template.html ja
editado.
"""
import json

MC_QUESTIONS = [
    (
        "Em relação ao conceito de agente público, é correto afirmar que:",
        ["Agente público é gênero, do qual servidor público é espécie — nem todo agente público ocupa cargo público (ex.: agentes políticos e particulares em colaboração com o Poder Público, como jurados e mesários).", "Agente público e servidor público são sinônimos perfeitos, sem qualquer distinção técnica.", "Somente ocupantes de cargo efetivo, aprovados em concurso público, podem ser considerados agentes públicos.", "Particulares que colaboram transitoriamente com o Poder Público, como mesários, não são considerados agentes públicos.", "Agentes políticos são espécie de servidor público, sujeitos ao mesmo regime estatutário destes."],
        0,
        "12 — Agente Público: conceito e espécies",
        "Correto o item A. Agente público é o gênero (toda pessoa que exerce função pública, ainda que transitória e não remunerada); servidor público — definido no art. 2º da Lei nº 8.112/1990 como \"a pessoa legalmente investida em cargo público\" — é apenas uma das espécies, ao lado dos agentes políticos e dos particulares em colaboração com o Poder Público."
    ),
    (
        "Nos termos do art. 3º da Lei nº 8.112/1990, o cargo público:",
        ["É o conjunto de atribuições e responsabilidades previstas na estrutura organizacional, criado por lei, com denominação própria e vencimento pago pelos cofres públicos, para provimento em caráter efetivo ou em comissão.", "Pode ser criado por decreto do Presidente da República, dispensada lei em sentido estrito.", "Somente pode ser provido em caráter efetivo, nunca em comissão.", "Tem denominação genérica, não sendo necessária denominação própria para cada cargo.", "É financiado, em regra, por recursos privados, complementados pelo erário apenas excepcionalmente."],
        0,
        "12 — Cargo Público: conceito e criação",
        "Correto o item A, nos termos literais do art. 3º, caput e parágrafo único, da Lei nº 8.112/1990."
    ),
    (
        "Quanto à extinção de cargos públicos, é correto afirmar que:",
        ["Cargos públicos ocupados somente podem ser extintos por lei, ao passo que cargos públicos vagos podem ser extintos por decreto do Presidente da República.", "Tanto cargos ocupados quanto vagos só podem ser extintos por lei.", "Tanto cargos ocupados quanto vagos podem ser extintos por simples decreto.", "Cargos ocupados podem ser extintos por decreto, desde que o ocupante seja previamente indenizado.", "A extinção de cargos públicos independe de qualquer previsão normativa específica."],
        0,
        "12 — Cargo Público: conceito e criação",
        "Correto o item A. Como os cargos públicos só podem ser CRIADOS por lei, a regra simétrica é que cargos OCUPADOS só podem ser extintos por lei; já os cargos VAGOS, por não gerarem direito subjetivo de terceiro, podem ser extintos por decreto do Presidente da República."
    ),
    (
        "Em relação às espécies de cargo público, é correto afirmar que:",
        ["O cargo em comissão é de livre nomeação e livre exoneração (ad nutum), submetendo seu ocupante ao regime geral de previdência social, ao passo que o cargo efetivo depende de aprovação em concurso público e submete seu ocupante ao regime próprio de previdência social.", "Tanto o cargo efetivo quanto o em comissão dependem de aprovação prévia em concurso público.", "A função de confiança pode ser exercida por qualquer pessoa, ainda que não ocupe cargo efetivo.", "O cargo em comissão submete seu ocupante a estágio probatório, da mesma forma que o cargo efetivo.", "O cargo efetivo é de livre exoneração, assim como o cargo em comissão."],
        0,
        "13 — Cargo Efetivo x Cargo em Comissão x Função de Confiança",
        "Correto o item A. Cargo em comissão: livre nomeação e exoneração, regime geral de previdência (RGPS). Cargo efetivo: depende de concurso público, estágio probatório e estabilidade, com regime próprio de previdência (RPPS). A função de confiança, diferentemente do cargo em comissão, somente pode ser exercida por quem já ocupa cargo efetivo."
    ),
    (
        "Quanto à distinção entre cargo público, emprego público e função pública, é correto afirmar que:",
        ["O cargo público é regido por vínculo estatutário (unilateral, podendo ser alterado por lei independentemente da concordância do servidor), ao passo que o emprego público é regido por vínculo contratual celetista, próprio de empresas públicas e sociedades de economia mista.", "Cargo público e emprego público são sinônimos, ambos regidos pela CLT.", "A função pública sempre pressupõe a existência de um cargo público correspondente e específico.", "O emprego público é regido pelo mesmo regime estatutário do cargo público.", "A função de confiança, por ser uma função pública, pode ser atribuída a qualquer pessoa, servidor ou não."],
        0,
        "13 — Cargo, Emprego e Função Pública: distinção",
        "Correto o item A. Regime estatutário (cargo) é unilateral e pode ser alterado por lei sem necessidade de concordância do servidor; regime celetista (emprego) é contratual. A função pública, ao contrário do cargo, não tem correspondência necessária na estrutura organizacional — é atribuída a quem já ocupa cargo efetivo (função de confiança) ou, excepcionalmente, a contratado temporário."
    ),
    (
        "A investidura em cargo público, segundo a Lei nº 8.112/1990:",
        ["Ocorre com a posse, não se confundindo com o provimento, que é o ato de preenchimento do cargo praticado pela autoridade competente.", "Ocorre com a nomeação, sendo sinônimo de posse.", "Ocorre com o exercício, não com a posse.", "Independe de qualquer ato formal da Administração Pública.", "É sinônimo de provimento derivado."],
        0,
        "12 — Investidura, Provimento e suas Categorias",
        "Correto o item A, nos termos do art. 7º da Lei nº 8.112/1990: \"A investidura em cargo público ocorrerá com a posse.\" Provimento é conceito distinto — o ato de preenchimento do cargo."
    ),
    (
        "Em relação às categorias de provimento de cargo público, é correto afirmar que:",
        ["Provimento originário é aquele em que a pessoa é designada ao cargo independentemente de vínculo anterior com a Administração Pública, tendo como única forma a nomeação; as demais formas de provimento são todas derivadas.", "Todas as formas de provimento previstas na Lei nº 8.112/1990 são originárias.", "Provimento derivado pressupõe sempre a aprovação em novo concurso público.", "A promoção é forma de provimento originário.", "Readaptação e reversão são formas de provimento originário, por não dependerem de concurso."],
        0,
        "12 — Investidura, Provimento e suas Categorias",
        "Correto o item A. A nomeação é a única forma de provimento ORIGINÁRIO (independe de vínculo anterior com a Administração); promoção, readaptação, reversão, aproveitamento, reintegração e recondução são formas de provimento DERIVADO, pois pressupõem vínculo anterior do servidor com a Administração Pública."
    ),
    (
        "Segundo a Súmula Vinculante 43 do STF, é inconstitucional toda modalidade de provimento que:",
        ["Propicie ao servidor investir-se, sem prévia aprovação em concurso público destinado ao seu provimento, em cargo que não integra a carreira na qual anteriormente investido — por isso, transferência, ascensão, acesso e readmissão não são formas de provimento válidas.", "Exija do servidor qualquer tipo de avaliação de desempenho prévia.", "Dependa de ato da autoridade competente de cada Poder.", "Seja utilizada para o preenchimento de cargo efetivo mediante concurso público regular.", "Envolva a promoção do servidor dentro da própria carreira, mediante critérios de antiguidade e merecimento."],
        0,
        "12 — Formas de Provimento e Súmula Vinculante 43",
        "Correto o item A, nos termos literais da Súmula Vinculante 43 do STF — veda-se qualquer forma de \"burlar\" o concurso público, permitindo que o servidor mude de carreira sem nova aprovação."
    ),
    (
        "Quanto aos prazos de posse e exercício previstos na Lei nº 8.112/1990, é correto afirmar que:",
        ["A posse deve ocorrer no prazo de 30 dias contados da publicação do ato de provimento, e só é cabível nos casos de provimento por nomeação; o exercício, por sua vez, deve ter início em até 15 dias improrrogáveis contados da posse.", "A posse deve ocorrer em até 15 dias, e o exercício, em até 30 dias.", "Tanto a posse quanto o exercício têm prazo de 30 dias, prorrogáveis por igual período.", "A posse é cabível em qualquer forma de provimento, inclusive na promoção.", "O prazo de exercício, diferentemente do de posse, pode ser prorrogado a critério da autoridade."],
        0,
        "12 — Posse e Exercício: prazos",
        "Correto o item A, nos termos dos arts. 13, §1º, e 15, §1º, da Lei nº 8.112/1990. A posse só é cabível em caso de NOMEAÇÃO (art. 13, §4º); o prazo de 15 dias para entrar em exercício é IMPRORROGÁVEL."
    ),
    (
        "Se o servidor empossado em cargo público não entrar em exercício no prazo legal de 15 dias, é correto afirmar que ele será:",
        ["Exonerado de ofício, não se tratando essa exoneração de penalidade disciplinar.", "Demitido, por se tratar de penalidade disciplinar por abandono de cargo.", "Suspenso por até 90 dias.", "Advertido por escrito, apenas.", "Automaticamente reconduzido ao cargo anteriormente ocupado."],
        0,
        "12 — Posse e Exercício: prazos",
        "Correto o item A, nos termos do art. 15, §2º, c/c art. 34, parágrafo único, II, da Lei nº 8.112/1990 — a perda do prazo de exercício gera exoneração de ofício, que NÃO é penalidade (diferente de demissão, que pressupõe PAD)."
    ),
    (
        "Em relação ao estágio probatório do servidor público, é correto afirmar que:",
        ["Embora o art. 20 da Lei nº 8.112/1990 preveja literalmente o prazo de 24 meses, o STF e o STJ pacificaram entendimento de que esse prazo deve acompanhar o da estabilidade prevista no art. 41 da CF/88 (com redação da EC nº 19/1998), de 3 anos (36 meses).", "O prazo de estágio probatório é de 24 meses, sem qualquer controvérsia doutrinária ou jurisprudencial.", "A estabilidade é adquirida automaticamente com a posse, independentemente de prazo de efetivo exercício.", "O estágio probatório aplica-se igualmente a ocupantes de cargo em comissão.", "O mnemônico ACADIPRORE refere-se aos requisitos para promoção, não para avaliação do estágio probatório."],
        0,
        "12 — Estágio Probatório x Estabilidade",
        "Correto o item A. Há dissonância entre a literalidade da Lei nº 8.112/1990 (24 meses) e a CF/88 após a EC nº 19/1998 (36 meses) — prevalece, segundo STF e STJ, o prazo constitucional de 36 meses tanto para a estabilidade quanto para o estágio probatório."
    ),
    (
        "O mnemônico ACADIPRORE, utilizado para memorizar os fatores de avaliação do estágio probatório previstos no art. 20 da Lei nº 8.112/1990, refere-se a:",
        ["Assiduidade, CApacidade de iniciativa, DIsciplina, PROdutividade e REsponsabilidade.", "Assiduidade, Capacidade técnica, Disciplina, Produtividade e Retidão.", "Autonomia, Capacidade, Disciplina, Probidade e Responsabilidade.", "Assiduidade, Cordialidade, Disciplina, Pontualidade e Responsabilidade.", "Aptidão, Capacidade, Discrição, Produtividade e Retidão."],
        0,
        "12 — Estágio Probatório x Estabilidade",
        "Correto o item A. Os cinco fatores do art. 20 da Lei nº 8.112/1990 são: assiduidade, disciplina, capacidade de iniciativa, produtividade e responsabilidade — organizados no mnemônico ACADIPRORE."
    ),
    (
        "Assinale a alternativa que NÃO corresponde a uma das hipóteses de vacância do cargo público previstas no art. 33 da Lei nº 8.112/1990:",
        ["Advertência.", "Exoneração.", "Demissão.", "Aposentadoria.", "Falecimento."],
        0,
        "12 — Vacância",
        "Correto o item A (é a exceção pedida). O art. 33 traz como hipóteses de vacância: exoneração, demissão, promoção, readaptação, aposentadoria, posse em outro cargo inacumulável e falecimento. Advertência é penalidade disciplinar, não hipótese de vacância."
    ),
    (
        "Em relação à demissão e à exoneração no regime da Lei nº 8.112/1990, é correto afirmar que:",
        ["A demissão é penalidade disciplinar, precedida de processo administrativo disciplinar, ao passo que a exoneração não possui natureza punitiva, podendo se dar a pedido do servidor ou de ofício.", "Exoneração e demissão são sinônimos, ambas penalidades disciplinares.", "A exoneração sempre pressupõe a prática de infração disciplinar pelo servidor.", "A demissão pode se dar a pedido do próprio servidor, sem necessidade de processo disciplinar.", "Apenas a exoneração gera vacância do cargo público; a demissão não."],
        0,
        "12 — Vacância",
        "Correto o item A. A demissão é a PENALIDADE máxima do regime disciplinar, exigindo PAD prévio; a exoneração não tem caráter punitivo — ambas, porém, geram vacância do cargo (art. 33, I e II)."
    ),
    (
        "Em relação à remoção e à redistribuição, previstas na Lei nº 8.112/1990, é correto afirmar que:",
        ["A remoção desloca o SERVIDOR (pessoa física), a pedido ou de ofício, no âmbito do mesmo quadro; já a redistribuição desloca o CARGO (ocupado ou vago), entre órgãos ou entidades do mesmo Poder.", "Tanto a remoção quanto a redistribuição deslocam exclusivamente o cargo, nunca o servidor.", "A redistribuição pode ocorrer entre órgãos de Poderes distintos, como do Executivo para o Legislativo.", "A remoção e a redistribuição são formas de provimento de cargo público.", "A substituição, assim como a remoção, desloca definitivamente o servidor de seu cargo de origem."],
        0,
        "12 — Remoção, Redistribuição e Substituição",
        "Correto o item A, nos termos dos arts. 36 e 37 da Lei nº 8.112/1990. A redistribuição, diferentemente da remoção, só pode ocorrer dentro do MESMO Poder (Executivo, Legislativo ou Judiciário). Nenhuma das duas é forma de provimento ou de vacância."
    ),
    (
        "Quanto à acumulação remunerada de cargos públicos, é correto afirmar que:",
        ["A regra geral é a vedação, ressalvadas as hipóteses constitucionalmente previstas — como a de dois cargos de professor, ou de um cargo de professor com outro técnico ou científico — sempre condicionadas à comprovação de compatibilidade de horários.", "A acumulação de cargos públicos é sempre permitida, desde que o servidor cumpra integralmente a carga horária de cada um.", "A compatibilidade de horários é exigida apenas nas acumulações consideradas ilícitas.", "A acumulação de dois cargos privativos de profissionais de saúde é sempre vedada, mesmo havendo compatibilidade de horário.", "A proibição de acumular cargos não se estende às empresas públicas e sociedades de economia mista."],
        0,
        "13 — Acumulação de Cargos Públicos",
        "Correto o item A, nos termos do art. 118 da Lei nº 8.112/1990 c/c art. 37, XVI, da CF. As exceções constitucionais (dois cargos de professor; um de professor com outro técnico/científico; dois privativos de profissionais de saúde) exigem, em qualquer caso, compatibilidade de horários."
    ),
    (
        "A acumulação ilícita de cargos, empregos ou funções públicas, uma vez caracterizada e comprovada a má-fé, sujeita o servidor à penalidade de:",
        ["Demissão.", "Advertência.", "Suspensão de até 30 dias.", "Multa, sem outras consequências.", "Afastamento preventivo, apenas."],
        0,
        "13 — Acumulação de Cargos Públicos",
        "Correto o item A, nos termos do art. 132, XII, da Lei nº 8.112/1990, que arrola a acumulação ilegal de cargos, empregos ou funções públicas entre as hipóteses de demissão."
    ),
    (
        "Em relação aos deveres do servidor público previstos no art. 116 da Lei nº 8.112/1990, é correto afirmar que o dever de cumprir as ordens superiores:",
        ["Comporta exceção quando a ordem for manifestamente ilegal, caso em que o servidor não deve cumpri-la.", "É absoluto, devendo o servidor cumprir qualquer ordem superior, ainda que manifestamente ilegal.", "Só se aplica a servidores ocupantes de cargo em comissão.", "Pode ser descumprido sempre que o servidor discordar do mérito da ordem recebida.", "Não está previsto expressamente entre os deveres do servidor na Lei nº 8.112/1990."],
        0,
        "12 — Regime Disciplinar: Deveres do Servidor",
        "Correto o item A, nos termos literais do art. 116, IV, da Lei nº 8.112/1990: \"cumprir as ordens superiores, exceto quando manifestamente ilegais\" — não há dever de obediência cega a ordens flagrantemente contrárias à lei."
    ),
    (
        "Em relação às proibições previstas no art. 117 da Lei nº 8.112/1990, é correto afirmar que:",
        ["É vedado ao servidor participar da gerência ou administração de sociedade privada, EXCETO na qualidade de acionista, cotista ou comanditário.", "É absolutamente vedado ao servidor ser acionista, cotista ou comanditário de qualquer sociedade privada.", "É permitido ao servidor manter, sob sua chefia imediata, cônjuge ou parente até o segundo grau civil em cargo de confiança.", "A proibição de participar de gerência de sociedade privada se aplica apenas a servidores em estágio probatório.", "Receber vantagem em razão das atribuições do cargo é conduta permitida, desde que não configure crime."],
        0,
        "12 — Regime Disciplinar: Proibições do Servidor",
        "Correto o item A, nos termos do art. 117, X, da Lei nº 8.112/1990. Ser mero acionista, cotista ou comanditário é a exceção expressamente ressalvada pela lei — o que se veda é a participação ativa na GERÊNCIA ou ADMINISTRAÇÃO da sociedade."
    ),
    (
        "Assinale a alternativa que apresenta apenas penalidades disciplinares efetivamente previstas, em rol taxativo, no art. 127 da Lei nº 8.112/1990:",
        ["Advertência, suspensão, demissão, cassação de aposentadoria ou disponibilidade, destituição de cargo em comissão e destituição de função comissionada.", "Advertência, suspensão, demissão, exoneração e remoção.", "Advertência, censura, multa, suspensão e afastamento preventivo.", "Suspensão, demissão, remoção de ofício e cassação de aposentadoria.", "Advertência, suspensão, demissão e afastamento preventivo."],
        0,
        "12 — Penalidades Disciplinares",
        "Correto o item A, nos termos literais do art. 127 da Lei nº 8.112/1990. Exoneração, remoção, censura, multa (isolada) e afastamento preventivo NÃO constam desse rol taxativo — afastamento preventivo é mera medida cautelar, sem natureza punitiva."
    ),
    (
        "Em relação à prescrição da ação disciplinar prevista no art. 142 da Lei nº 8.112/1990, é correto afirmar que ela ocorre em:",
        ["5 anos, quanto às infrações puníveis com demissão, cassação de aposentadoria ou disponibilidade e destituição de cargo em comissão; 2 anos, quanto à suspensão; e 180 dias, quanto à advertência.", "2 anos, para todas as infrações disciplinares, sem distinção quanto à penalidade cabível.", "180 dias, para toda e qualquer infração disciplinar.", "5 anos, exclusivamente para a advertência, e 180 dias para a demissão.", "10 anos, quanto às infrações puníveis com demissão, e 5 anos, quanto à suspensão."],
        0,
        "12 — Prescrição da Ação Disciplinar",
        "Correto o item A, nos termos literais do art. 142, I a III, da Lei nº 8.112/1990."
    ),
    (
        "Em relação à sindicância e ao processo administrativo disciplinar (PAD), é correto afirmar que:",
        ["A instauração do PAD é obrigatória sempre que o ilícito praticado pelo servidor ensejar a imposição de suspensão por mais de 30 dias, demissão, cassação de aposentadoria ou disponibilidade, ou destituição de cargo em comissão.", "A sindicância é sempre obrigatória antes da instauração de qualquer PAD.", "O PAD pode ser conduzido por um único servidor, dispensada a formação de comissão.", "A sindicância pode, por si só, resultar na aplicação da penalidade de demissão.", "O PAD é conduzido por comissão composta por servidores ocupantes de cargo em comissão, ainda que não estáveis."],
        0,
        "12 — Sindicância x Processo Administrativo Disciplinar (PAD)",
        "Correto o item A, nos termos do art. 146 da Lei nº 8.112/1990. A sindicância, por si só, só pode resultar em arquivamento, advertência ou suspensão de até 30 dias (art. 145) — nunca em demissão, que exige PAD conduzido por comissão de servidores ESTÁVEIS (art. 149)."
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
