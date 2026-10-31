# -*- coding: utf-8 -*-
"""
Primeiro conteudo de Direito Administrativo do app (PC-PE) -- a partir do
PDF "Fontes do Direito Administrativo" (Focus Concursos), que cobre o item
2 ("Direito administrativo") do edital.

As mudancas estruturais em app-template.html ja foram feitas via Edit antes
deste script rodar: criacao do const TEORIA_DIREITO_ADMINISTRATIVO_PCPE
(teoria resumida de fontes do Direito Administrativo -- lei, jurisprudencia,
doutrina, costumes/praxe, classificacoes formais/materiais, analogia,
sumula vinculante, fontes primarias/secundarias e objeto do Direito
Administrativo), e registro do deck em TEORIA_DECKS / TEORIA_DECK_TO_DISC
com o disc "Direito Administrativo".

O PDF trazia questoes prontas em dois formatos: multipla escolha (ja no
formato usado pelo PC-PE) e Certo/Errado (formato que o PC-PE NAO usa --
ver feedback salvo em memoria). As questoes MC prontas, com gabarito e
comentario, foram transcritas quase integralmente (apenas reformatando pra
nosso schema). As questoes Certo/Errado foram reescritas como questoes de
multipla escolha originais, mantendo o mesmo fato juridico testado e o
mesmo gabarito (a assertiva do item, certa ou errada, vira uma das 5
alternativas; as demais sao distratores plausiveis construidos a partir do
proprio texto do PDF), em vez de serem simplesmente descartadas.

Este script cuida so de: (1) acrescentar as 20 questoes a questions.json,
(2) regenerar estudo-cebraspe-ma.html a partir do app-template.html ja
editado.
"""
import json

MC_QUESTIONS = [
    (
        "Considerando as fontes do direito administrativo como sendo aquelas regras ou aqueles comportamentos que provocam o surgimento de uma norma posta, assinale a opção correta.",
        ["A lei é uma fonte primária e deve ser considerada em seu sentido amplo para abranger inclusive os regulamentos administrativos.", "O acordo é uma importante fonte do direito administrativo por ser forma de regulamentar a convivência mediante a harmonização de pensamentos.", "Os costumes, pela falta de norma escrita, não podem ser considerados como fonte do direito administrativo.", "A jurisprudência é compreendida como sendo aquela emanada por estudiosos ao publicarem suas pesquisas acerca de determinada questão jurídica.", "Uma doutrina se consolida com reiteradas decisões judiciais sobre o mesmo tema."],
        0,
        "2 — Direito Administrativo: Fontes do Direito Administrativo",
        "Correto o item A. A lei é fonte primária do Direito Administrativo e deve ser compreendida em sentido amplo, o que inclui a Constituição Federal, as normas supralegais, as leis e também os atos normativos da própria administração pública (regulamentos). O item B erra porque acordo não é fonte do Direito Administrativo; o C erra porque costumes são fonte secundária, apesar de não escrita; o D confunde jurisprudência com doutrina; o E confunde doutrina com jurisprudência."
    ),
    (
        "Acerca do direito administrativo, assinale a alternativa correta quanto aos costumes como fonte do direito administrativo, conforme a doutrina majoritária.",
        ["Os costumes não constituem fonte do direito administrativo, em razão do princípio da legalidade estrita.", "Os costumes constituem fonte secundária do direito administrativo, ao lado da doutrina e da jurisprudência.", "Os costumes constituem fonte primária do direito administrativo, equiparados à lei.", "Os costumes só são considerados fonte quando positivados em lei.", "Os costumes não são reconhecidos como fonte em nenhum ramo do direito brasileiro."],
        1,
        "2 — Direito Administrativo: Fontes do Direito Administrativo",
        "Correto o item B. A doutrina diferencia as fontes do Direito em primárias e secundárias. No âmbito do Direito Administrativo, apenas a lei constitui fonte primária; dentre as fontes secundárias, encontram-se a doutrina, a jurisprudência e também os costumes — diferentemente do que ocorre no âmbito privado, onde os costumes têm papel mais relevante, eles continuam sendo fonte também no Direito Administrativo, apenas secundária."
    ),
    (
        "Assinale a alternativa correta a respeito da codificação do direito administrativo brasileiro:",
        ["O direito administrativo é codificado, estando suas normas reunidas em um único corpo de leis, assim como ocorre no direito penal e no direito civil.", "O direito administrativo não é codificado; embora a lei seja sua fonte primária, não existe um código administrativo único reunindo todas as normas da matéria.", "O direito administrativo passou a ser codificado somente após a Constituição Federal de 1988.", "A codificação do direito administrativo é parcial, abrangendo apenas a disciplina dos contratos administrativos.", "A ausência de codificação retira da lei o status de fonte primária do direito administrativo."],
        1,
        "2 — Direito Administrativo: Fontes do Direito Administrativo",
        "Correto o item B. Diferentemente do direito penal, civil e processual penal, o direito administrativo não é codificado — não existe um código administrativo único reunindo todas as suas normas; isso não retira da lei, porém, a condição de fonte primária, apenas significa que ela se espalha por diversos diplomas normativos."
    ),
    (
        "Em relação à origem e às fontes do direito administrativo, aos sistemas administrativos e à administração pública em geral, assinale a alternativa correta:",
        ["Um dos aspectos da constitucionalização do direito administrativo se refere à elevação, ao nível constitucional, de matérias antes tratadas por legislação infraconstitucional.", "A constitucionalização do direito administrativo significa a substituição integral da lei ordinária pela Constituição como única fonte da matéria.", "A constitucionalização retirou da jurisprudência qualquer papel como fonte do direito administrativo.", "A constitucionalização do direito administrativo é incompatível com a existência de normas infraconstitucionais.", "A constitucionalização do direito administrativo extinguiu o princípio da legalidade."],
        0,
        "2 — Direito Administrativo: Fontes do Direito Administrativo",
        "Correto o item A. A constitucionalização do direito administrativo é fenômeno pelo qual matérias antes tratadas apenas por lei infraconstitucional passam a ter assento constitucional (ex.: princípios da administração pública, art. 37, CF/88) — isso não exclui a lei nem a jurisprudência como fontes, nem extingue o princípio da legalidade."
    ),
    (
        "Sobre o costume como fonte do direito administrativo brasileiro, assinale a alternativa correta:",
        ["No Brasil, assim como no sistema de common law, o costume é fonte principal (primária) do direito administrativo.", "No Brasil, diferentemente do sistema de common law, o costume é fonte apenas secundária do direito administrativo, prevalecendo a lei como fonte primária.", "O costume é fonte primária do direito administrativo brasileiro, equiparado à lei.", "O costume não é, em nenhuma hipótese, considerado fonte do direito administrativo brasileiro.", "O Brasil adota o sistema de common law para fins de direito administrativo."],
        1,
        "2 — Direito Administrativo: Fontes do Direito Administrativo",
        "Correto o item B. O Brasil adota a tradição de civil law, na qual a lei é a fonte primária; o costume, embora seja fonte do direito administrativo, é apenas secundário — diferente do que ocorre em sistemas de common law, nos quais o costume e o precedente têm peso muito maior."
    ),
    (
        "As principais fontes formais do direito administrativo, segundo a doutrina majoritária, são:",
        ["Os princípios gerais de direito, a jurisprudência, a lei e os atos normativos da administração.", "Os costumes, a lei e os atos normativos da administração.", "A Constituição, a lei e os costumes.", "A doutrina, a jurisprudência e a Constituição.", "A Constituição, a lei e os atos normativos da administração pública."],
        4,
        "2 — Direito Administrativo: Fontes do Direito Administrativo",
        "Correto o item E. São fontes FORMAIS as criações do Estado por processo formal específico — Constituição, leis e atos normativos da administração pública (regulamentos, portarias etc.). Doutrina, jurisprudência (não vinculante), costumes e princípios gerais do direito são, em regra, fontes MATERIAIS."
    ),
    (
        "Assinale a alternativa correta sobre o costume e a praxe administrativa como fontes do direito administrativo:",
        ["O costume e a praxe administrativa são fontes organizadas, pois resultam de processo formal específico de cada Poder.", "O costume e a praxe administrativa são fontes inorganizadas do direito administrativo, que só indiretamente influenciam a produção do direito positivo.", "Apenas o costume, e não a praxe administrativa, é considerado fonte inorganizada do direito administrativo.", "O costume e a praxe administrativa equivalem-se, sendo tratados como sinônimos pela doutrina administrativista.", "A praxe administrativa prevalece sobre a lei quando esta apresenta lacuna."],
        1,
        "2 — Direito Administrativo: Fontes do Direito Administrativo",
        "Correto o item B. Tanto o costume quanto a praxe administrativa são fontes NÃO ESCRITAS/INORGANIZADAS (ao lado dos princípios gerais do direito), e sua influência sobre o direito positivo é indireta — não criam, por si só, norma jurídica vinculante como a lei."
    ),
    (
        "Em decorrência de qual princípio a lei é considerada a mais importante das fontes do direito administrativo?",
        ["Princípio da supremacia do interesse público.", "Princípio da legalidade.", "Princípio da eficiência.", "Princípio da moralidade administrativa.", "Princípio da autotutela."],
        1,
        "2 — Direito Administrativo: Fontes do Direito Administrativo",
        "Correto o item B. A primazia da lei como fonte do Direito Administrativo decorre diretamente do princípio da legalidade, que orienta toda a atuação da Administração Pública — só a lei vincula, por si só, de forma imediata e direta, a conduta do administrador."
    ),
    (
        "Assinale a alternativa correta quanto à hierarquia das fontes do direito administrativo:",
        ["Costumes, jurisprudência, doutrina e lei têm, todos, a mesma hierarquia, sendo considerados fontes primárias do direito administrativo.", "Somente a lei é fonte primária; costumes, jurisprudência e doutrina são fontes secundárias.", "Somente os costumes e a doutrina são fontes do direito administrativo; a jurisprudência não é fonte.", "A jurisprudência é sempre fonte primária, independentemente de ter ou não efeito vinculante.", "A doutrina é fonte primária, por sistematizar o conhecimento jurídico."],
        1,
        "2 — Direito Administrativo: Fontes do Direito Administrativo",
        "Correto o item B. A hierarquia das fontes do Direito Administrativo não é igualitária: apenas a lei é fonte primária (originária/direta); costumes, jurisprudência (não vinculante) e doutrina são fontes secundárias (derivadas/indiretas)."
    ),
    (
        "Os costumes sociais, quando considerados fonte do direito administrativo, classificam-se como:",
        ["Fonte direta (primária), pois criam imediatamente obrigações para a Administração Pública.", "Fonte indireta (secundária), pois apenas influenciam, sem vincular por si só, a produção legislativa ou jurisprudencial.", "Fonte formal, equiparada à lei em sentido amplo.", "Fonte escrita e organizada.", "Fonte exclusiva do direito administrativo, sem equivalente em outros ramos do direito."],
        1,
        "2 — Direito Administrativo: Fontes do Direito Administrativo",
        "Correto o item B. Os costumes são fonte secundária (indireta/mediata): não criam, por si só, obrigação jurídica vinculante — apenas influenciam a produção de normas e a formação da jurisprudência, suprindo lacunas da legislação."
    ),
    (
        "Sobre a diferença entre costume e praxe administrativa, assinale a alternativa correta:",
        ["O costume exige apenas o requisito objetivo (uso continuado); a praxe administrativa exige, cumulativamente, os requisitos objetivo e subjetivo (convicção de obrigatoriedade).", "O costume exige cumulativamente os requisitos objetivo (uso continuado) e subjetivo (convicção de obrigatoriedade), ao passo que a praxe administrativa conta apenas com o requisito objetivo; nenhum dos dois, porém, é reconhecido como fonte formal do direito administrativo.", "Costume e praxe administrativa são sinônimos para a doutrina administrativista majoritária.", "A praxe administrativa é sempre conhecida pelo público em geral, diferentemente do costume.", "O costume contra legem prevalece sobre a lei quando reiteradamente praticado pela Administração."],
        1,
        "2 — Direito Administrativo: Fontes do Direito Administrativo",
        "Correto o item B. O costume exige os dois requisitos cumulativamente (objetivo + subjetivo) e é conhecido por todos (agentes e administrados); já a praxe administrativa só tem o requisito objetivo e é interna/desconhecida do grande público. Ambos, porém, são fontes materiais e inorganizadas — não fontes formais, categoria reservada às criações do Estado por processo formal específico (leis)."
    ),
    (
        "Assinale a alternativa correta sobre jurisprudência e costumes como fontes do direito administrativo:",
        ["A jurisprudência, em regra, não vincula a atuação de outros julgadores, e os costumes têm sua influência relacionada à deficiência ou lacuna da legislação.", "A jurisprudência sempre vincula a atuação da Administração Pública, independentemente de ter ou não efeito vinculante.", "Os costumes substituem a lei sempre que esta for omissa quanto a determinada matéria.", "A jurisprudência é fonte primária do direito administrativo em toda e qualquer hipótese.", "Os costumes não guardam qualquer relação com lacunas da legislação."],
        0,
        "2 — Direito Administrativo: Fontes do Direito Administrativo",
        "Correto o item A. Em regra, a jurisprudência não vincula a atuação de outros juízes, servindo apenas como orientação (ressalvada a súmula vinculante); os costumes, por sua vez, suprem o texto escrito justamente onde a legislação é deficiente ou lacunosa — não a substituem de forma plena, mas atuam como elemento informativo da prática administrativa."
    ),
    (
        "Em relação ao objeto e às fontes do direito administrativo, assinale a opção correta.",
        ["O Poder Executivo exerce, além da função administrativa, a denominada função política de governo — como, por exemplo, a elaboração de políticas públicas, que também constituem objeto de estudo do direito administrativo.", "As decisões judiciais com efeitos vinculantes ou eficácia erga omnes são consideradas fontes secundárias de direito administrativo, e não fontes principais.", "São exemplos de manifestação do princípio da especialidade o exercício do poder de polícia e as chamadas cláusulas exorbitantes dos contratos administrativos.", "Decorrem do princípio da indisponibilidade do interesse público a necessidade de realizar concurso público para admissão de pessoal permanente e as restrições impostas à alienação de bens públicos.", "Dizer que o direito administrativo é um ramo do direito público significa o mesmo que dizer que seu objeto está restrito a relações jurídicas regidas pelo direito público."],
        3,
        "2 — Direito Administrativo: Fontes do Direito Administrativo",
        "Correto o item D. A indisponibilidade do interesse público impõe restrições à atuação do administrador em nome da coletividade — daí decorrem, por exemplo, a exigência de concurso público (que impede escolha pessoal/discricionária de servidores efetivos) e as restrições à alienação de bens públicos (que impedem o gestor de dispor livremente do patrimônio estatal)."
    ),
    (
        "De acordo com a classificação das fontes do direito administrativo quanto à origem, são consideradas fontes MATERIAIS:",
        ["As leis em sentido genérico (CF/88, leis complementares, ordinárias, decretos).", "A doutrina, a jurisprudência, os costumes e os princípios gerais do direito.", "Somente a lei e a jurisprudência vinculante.", "Somente os atos normativos internos da Administração Pública.", "A Constituição Federal e os tratados internacionais de direitos humanos."],
        1,
        "2 — Direito Administrativo: Fontes do Direito Administrativo",
        "Correto o item B. Fontes MATERIAIS são as que advêm de fora do processo formal de criação de normas, estando muitas vezes fora da própria estrutura do Estado: doutrina, jurisprudência, costumes e princípios gerais do direito. As leis em sentido genérico são exemplo de fonte FORMAL."
    ),
    (
        "Quanto à forma, são consideradas fontes ESCRITAS ou ORGANIZADAS do direito administrativo:",
        ["Os costumes e os princípios gerais do direito.", "A lei, em sentido amplo, abrangendo desde a Constituição Federal até os regulamentos internos de órgãos e entidades.", "Apenas os princípios gerais do direito.", "A doutrina e a jurisprudência não vinculante.", "Somente os regulamentos internos, excluída a Constituição Federal."],
        1,
        "2 — Direito Administrativo: Fontes do Direito Administrativo",
        "Correto o item B. A lei é a principal fonte escrita e organizada do Direito Administrativo, abrangendo, em sentido amplo, desde a Constituição Federal até os regulamentos internos de órgãos e entidades. Costumes e princípios gerais do direito são as fontes NÃO escritas/inorganizadas por excelência."
    ),
    (
        "Sobre a analogia no âmbito do direito administrativo, assinale a alternativa correta:",
        ["Para a doutrina administrativista majoritária, a analogia é expressamente reconhecida como fonte do direito administrativo.", "Para a doutrina administrativista majoritária, a analogia não é citada como fonte do direito administrativo; já a jurisprudência, inclusive do STF e do STJ, vem utilizando essa técnica para solucionar casos concretos.", "A analogia é fonte formal e primária do direito administrativo, equiparada à lei.", "A analogia é vedada em qualquer hipótese no âmbito do direito administrativo, inclusive pela jurisprudência.", "A analogia é fonte exclusivamente legislativa, não podendo ser utilizada pelo Poder Judiciário."],
        1,
        "2 — Direito Administrativo: Fontes do Direito Administrativo",
        "Correto o item B. A maioria dos doutrinadores não cita a analogia como fonte autônoma do Direito Administrativo; contudo, na prática, a jurisprudência — inclusive do STF e do STJ — vem utilizando a técnica da analogia (mesma razão de fato, mesma razão de direito) para solucionar casos concretos não expressamente regulados."
    ),
    (
        "Em regra, a jurisprudência constitui fonte MATERIAL do direito administrativo. Assinale a alternativa que indica corretamente a exceção a essa regra:",
        ["Quando a decisão tiver efeito erga omnes ou a súmula possuir efeito vinculante, caso em que se está diante de uma fonte FORMAL.", "Quando a decisão for proferida por tribunal de segunda instância, caso em que se torna fonte formal.", "Não há exceção: a jurisprudência é sempre fonte material, independentemente do efeito da decisão.", "Quando a decisão for unânime, independentemente do órgão julgador.", "Quando a decisão envolver matéria tributária, caso em que se torna automaticamente fonte formal."],
        0,
        "2 — Direito Administrativo: Fontes do Direito Administrativo",
        "Correto o item A. A regra é que a jurisprudência seja fonte material; porém, quando a decisão tiver efeito erga omnes (ex.: controle concentrado de constitucionalidade) ou a súmula possuir efeito vinculante (súmula vinculante do STF), ela passa a ser FONTE FORMAL, por produzir efeitos jurídicos diretos e obrigatórios, equiparáveis aos da lei."
    ),
    (
        "Para fins de prova, são consideradas fontes PRIMÁRIAS ou FORMAIS do direito administrativo, ainda que sejam derivações da fonte jurisprudencial:",
        ["Quaisquer decisões monocráticas de relator em tribunais superiores.", "As súmulas vinculantes do STF, as decisões em recursos extraordinários com repercussão geral e as decisões em ações de controle de constitucionalidade (ADI, ADC, ADPF).", "Súmulas meramente orientadoras de qualquer tribunal, inclusive de primeira instância.", "Pareceres da Advocacia-Geral da União, ainda que não aprovados pelo Presidente da República.", "Enunciados de jornadas de direito administrativo promovidas por universidades."],
        1,
        "2 — Direito Administrativo: Fontes do Direito Administrativo",
        "Correto o item B. São tratadas como fontes primárias/formais — mesmo derivando da fonte jurisprudencial — as súmulas vinculantes do STF, as decisões de recursos extraordinários com repercussão geral e as decisões tomadas em ações de controle concentrado de constitucionalidade (ADI, ADC, ADPF), por seu efeito vinculante/erga omnes."
    ),
    (
        "Nos termos do art. 103-A da Constituição Federal de 1988, a súmula vinculante editada pelo Supremo Tribunal Federal:",
        ["Tem caráter meramente orientador, podendo ser livremente afastada pela Administração Pública mediante justificativa.", "É de cumprimento obrigatório pela Administração Pública, direta e indireta, nas esferas federal, estadual e municipal.", "Vincula apenas o Poder Judiciário, não alcançando a Administração Pública.", "Depende de regulamentação por lei ordinária para produzir efeitos.", "Tem eficácia limitada ao órgão que suscitou sua edição."],
        1,
        "2 — Direito Administrativo: Fontes do Direito Administrativo",
        "Correto o item B. O art. 103-A da CF/88 estabelece que a súmula vinculante, a partir de sua publicação na imprensa oficial, terá efeito vinculante em relação aos demais órgãos do Poder Judiciário e à administração pública direta e indireta, nas esferas federal, estadual e municipal — sendo, portanto, de cumprimento obrigatório."
    ),
    (
        "Quanto ao objeto do direito administrativo, assinale a alternativa correta:",
        ["O direito administrativo tem por objeto exclusivamente as relações entre órgãos e entidades de um mesmo Estado.", "O direito administrativo tem por objeto afirmar as relações entre os Estados (órgãos e entidades) e entre as pessoas (físicas e jurídicas) e o próprio Estado, além de ser responsável pelo regime jurídico administrativo (normas, princípios e regras).", "O direito administrativo tem por objeto apenas a disciplina dos contratos administrativos.", "O direito administrativo, por ser ramo do direito privado, regula exclusivamente relações entre particulares.", "O direito administrativo não possui objeto próprio, limitando-se a complementar o direito constitucional."],
        1,
        "2 — Direito Administrativo: Fontes do Direito Administrativo",
        "Correto o item B. O Direito Administrativo tem por objeto afirmar as relações entre os Estados — órgãos e entidades — e entre as pessoas (físicas e jurídicas) e o próprio Estado, sendo responsável pelo regime jurídico administrativo (normas administrativas, princípios e regras). É ramo do direito PÚBLICO, não codificado, autônomo e independente."
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
