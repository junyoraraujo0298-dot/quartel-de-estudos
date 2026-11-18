# -*- coding: utf-8 -*-
"""
Quinto conteudo de Direito Administrativo do app (PC-PE) -- a partir do PDF
"Organizacao da Administracao Publica | Administracao Publica Indireta --
Parte I" (Focus Concursos), cobrindo o restante do item 8.2 do programa
oficial ("Administracao direta e indireta").

Mesmo caso do PDF anterior (Administracao Direta/Teoria do Orgao): e
Direito Administrativo puro, sem vinculo com nenhuma esfera federativa
especifica, entao nao ha ressalva de escopo.

A mudanca estrutural em app-template.html ja foi feita via Edit antes deste
script rodar: duas novas secoes no deck TEORIA_DIREITO_ADMINISTRATIVO_PCPE
ja existente -- "Administracao Publica Indireta -- Conceito e
Caracteristicas Comuns (item 8.2)" (conceito e entes da indireta; consorcios
e associacoes publicas; as 5 caracteristicas comuns: personalidade juridica
propria, criacao/extincao pelo paralelismo das formas, sem fins lucrativos,
finalidade especifica, ausencia de hierarquia/controle finalistico) e
"Autarquias, Fundacoes Publicas e Empresas Estatais (item 8.2)" (autarquia
conceito/privilegios/bens; fundacao publica direito publico x privado;
empresas estatais conceito geral; empresa publica x sociedade de economia
mista -- tabela Lei 13.303/2016; prestadoras de servico publico x
exploradoras de atividade economica; Decreto-Lei 200/67 e a pegadinha
entidade politica x administrativa). Um diagrama SVG novo em TEORIA_SCENES
(entesIndiretaTree: arvore "Administracao Indireta" branching pras 4
entidades, no mesmo estilo do provimentoTree ja usado no deck).

19 questoes novas (MC, originais, nao sao transcricao literal do PDF, que
traz questoes Certo/Errado -- convertidas pro formato MC ja padrao do app
pro PC-PE). A questao 03 explora a mesma pegadinha ja cobrada no PDF-fonte
(secretarias municipais NAO integram a administracao indireta --
desconcentracao, nao descentralizacao).

Este script cuida so de: (1) acrescentar as questoes a questions.json,
(2) regenerar estudo-cebraspe-ma.html a partir do app-template.html ja
editado.
"""
import json

MC_QUESTIONS = [
    (
        "Nos termos do art. 37, XIX, da Constituição Federal, a Administração Pública Indireta é composta pelas seguintes entidades:",
        ["Autarquias, fundações públicas, empresas públicas e sociedades de economia mista.", "Apenas autarquias e fundações públicas, com personalidade jurídica de direito público.", "Secretarias, Ministérios e demais órgãos integrantes da estrutura da Administração Direta.", "Organizações sociais, serviços sociais autônomos e entidades paraestatais.", "Somente as empresas públicas e sociedades de economia mista, com personalidade de direito privado."],
        0,
        "8.2 — Administração Indireta: conceito e entes",
        "Correto o item A. A Administração Indireta, fruto do processo de descentralização, é composta por autarquias, fundações públicas, empresas públicas e sociedades de economia mista (CF, art. 37, XIX), todas dotadas de personalidade jurídica própria."
    ),
    (
        "A respeito da relação entre as entidades da Administração Indireta e o ente político que as criou, é correto afirmar que:",
        ["Não há subordinação hierárquica entre elas, mas apenas vinculação, sujeitando-se a Administração Indireta a controle e fiscalização (também chamado de controle finalístico) por parte da Administração Direta.", "As entidades da Administração Indireta são subordinadas hierarquicamente ao ente que as instituiu, podendo este revogar livremente seus atos.", "A Administração Indireta integra, para todos os efeitos, a mesma pessoa jurídica do ente instituidor.", "Inexiste qualquer forma de controle ou fiscalização sobre as entidades da Administração Indireta, em razão de sua autonomia plena.", "O controle sobre a Administração Indireta é exercido exclusivamente pelo Poder Judiciário."],
        0,
        "8.2 — Administração Indireta: conceito e entes",
        "Correto o item A. Não existe hierarquia entre a Administração Direta e a Indireta — o que existe é vinculação e controle finalístico (supervisão ministerial), exercido pelos três Poderes, nunca subordinação."
    ),
    (
        "Julgando a situação em que determinado município criou, por meio de lei, diversas secretarias municipais para a execução especializada de suas atividades administrativas, é correto afirmar que:",
        ["As secretarias municipais não constituem nova pessoa jurídica, de modo que integram a Administração Direta do município, por força da desconcentração administrativa, e não da descentralização.", "As secretarias municipais passam a integrar a Administração Indireta do município, por serem dotadas de personalidade jurídica própria.", "A criação de secretarias é exemplo clássico de descentralização por outorga.", "As secretarias municipais equivalem, para fins jurídicos, a autarquias municipais.", "A criação de secretarias depende de autorização legislativa, nos mesmos moldes exigidos para a criação de empresas públicas."],
        0,
        "8.2 — Consórcios públicos e associações públicas",
        "Correto o item A. Secretarias (municipais, estaduais ou Ministérios) são órgãos, não pessoas jurídicas novas — resultam de desconcentração dentro da própria Administração Direta, jamais integrando a Administração Indireta, que pressupõe descentralização (criação de nova pessoa jurídica)."
    ),
    (
        "Os consórcios públicos, disciplinados pela Lei nº 11.107/2005, podem dar origem às chamadas associações públicas. A respeito delas, é correto afirmar que:",
        ["A associação pública de direito público constitui espécie do gênero autarquia, por vezes chamada de autarquia interfederativa, enquanto a associação de direito privado segue o regime das empresas estatais.", "Toda associação resultante de consórcio público tem, obrigatoriamente, personalidade jurídica de direito privado.", "O consórcio público não gera nova pessoa jurídica, mas apenas um acordo de cooperação entre os entes consorciados.", "As associações públicas confundem-se, para todos os efeitos, com os próprios entes políticos que as instituíram.", "Associações públicas somente podem ser instituídas pela União, sendo vedada a participação de Estados e Municípios."],
        0,
        "8.2 — Consórcios públicos e associações públicas",
        "Correto o item A. O consórcio público (Lei nº 11.107/2005) é contrato entre entes políticos que pode gerar associação pública de direito público (espécie de autarquia, também chamada interfederativa/multifederada) ou, se de direito privado, seguirá o regime das empresas estatais."
    ),
    (
        "As entidades da Administração Indireta gozam de autonomia técnica, administrativa e financeira. Sobre esse ponto, é correto afirmar que:",
        ["Tais entidades não possuem autonomia política, isto é, não têm aptidão para legislar — nem mesmo as agências reguladoras, cuja competência normativa se restringe à edição de normas técnicas complementares à lei.", "A autonomia técnica, administrativa e financeira equivale, na prática, à autonomia política dos entes federativos.", "Somente as autarquias gozam de autonomia administrativa e financeira, sendo esta vedada às empresas públicas e sociedades de economia mista.", "As agências reguladoras, por serem autarquias de regime especial, possuem autonomia política plena, podendo editar normas com força de lei.", "A ausência de autonomia política impede que as entidades da Administração Indireta tenham patrimônio e receitas próprios."],
        0,
        "8.2 — Características comuns: personalidade jurídica e patrimônio próprios",
        "Correto o item A. Autonomia técnica/administrativa/financeira não se confunde com autonomia política (aptidão para legislar) — esta inexiste mesmo nas agências reguladoras, cuja regulamentação técnica é sempre complementar à lei, nunca substitutiva dela."
    ),
    (
        "A respeito da criação e extinção das entidades da Administração Indireta, de acordo com o princípio do paralelismo das formas, é correto afirmar que:",
        ["Se a regra para determinada entidade é que a lei a cria diretamente, somente outra lei poderá extingui-la; se a regra é que a lei apenas autoriza a criação, somente a lei poderá autorizar a extinção.", "Toda entidade da Administração Indireta, uma vez criada por lei, somente pode ser extinta por decreto do chefe do Poder Executivo.", "A extinção de qualquer entidade da Administração Indireta pode ser feita por simples ato administrativo, independentemente da forma usada para sua criação.", "Autarquias e empresas públicas seguem, em todos os aspectos, a mesma regra de criação e extinção.", "A regra do paralelismo das formas aplica-se apenas às fundações públicas, não se estendendo às demais entidades."],
        0,
        "8.2 — Criação e extinção: o paralelismo das formas",
        "Correto o item A. Pelo paralelismo das formas, o instrumento usado para extinguir deve espelhar o usado para criar: lei cria → só lei extingue; lei autoriza a criação → só lei autoriza a extinção."
    ),
    (
        "Quanto à criação da autarquia e da fundação pública de direito público, é correto afirmar que:",
        ["Ambas são criadas diretamente por lei específica, sendo a fundação pública de direito público também chamada de autarquia fundacional, por constituir espécie do gênero autarquia.", "Ambas dependem de lei que apenas autorize sua criação, com posterior registro dos atos constitutivos em cartório ou junta comercial.", "A fundação pública de direito público é criada por decreto do chefe do Poder Executivo, dispensada lei específica.", "A autarquia, diferentemente da fundação pública de direito público, depende de registro de atos constitutivos para passar a existir.", "Apenas a autarquia é criada por lei; a fundação pública de direito público é sempre criada por lei complementar que define sua área de atuação."],
        0,
        "8.2 — Criação e extinção: o paralelismo das formas",
        "Correto o item A. Autarquia e fundação pública de direito público (espécie de autarquia, também chamada de autarquia fundacional) são as únicas entidades criadas diretamente pela lei — basta a lei para que existam, sem necessidade de registro posterior."
    ),
    (
        "A fundação pública de direito privado, também chamada de fundação governamental, segue regime distinto do aplicável à fundação pública de direito público. A respeito dela, é correto afirmar que:",
        ["Sua criação depende de lei ordinária específica que apenas autorize a instituição, cabendo à lei complementar definir as possíveis áreas de atuação da fundação.", "É criada diretamente por lei específica, dispensando qualquer ato de registro posterior.", "Constitui espécie do gênero autarquia, sendo chamada de autarquia fundacional.", "Segue regime jurídico integralmente público, idêntico ao das autarquias.", "Pode ter sua finalidade alterada livremente pelo administrador, sem necessidade de lei."],
        0,
        "8.2 — Fundação pública: direito público x direito privado",
        "Correto o item A. A fundação pública de direito privado (fundação governamental) segue o regime das empresas estatais: lei ordinária específica autoriza sua criação, e lei complementar define as áreas em que pode atuar — exatamente o entendimento já considerado correto pelo CEBRASPE."
    ),
    (
        "Em relação à finalidade lucrativa das entidades da Administração Indireta, é correto afirmar que:",
        ["Nenhuma delas é criada com finalidade lucrativa, podendo até auferir lucro no exercício de suas atividades, mas sem que esse seja o objetivo da sua criação — inclusive as empresas públicas e sociedades de economia mista exploradoras de atividade econômica.", "As empresas públicas e sociedades de economia mista que exploram atividade econômica têm, por definição legal, finalidade exclusivamente lucrativa.", "Somente as autarquias e fundações públicas não podem ter fins lucrativos; empresas estatais podem ser criadas livremente com esse objetivo.", "A obtenção de lucro, ainda que eventual, descaracteriza a natureza jurídica da entidade como integrante da Administração Indireta.", "A exploração de atividade econômica pelo Estado é a regra geral, prevista no art. 173 da CF como forma ordinária de atuação estatal."],
        0,
        "8.2 — Sem fins lucrativos e finalidade específica",
        "Correto o item A. Nenhuma entidade da Administração Indireta — nem mesmo as exploradoras de atividade econômica, que existem apenas excepcionalmente por relevante interesse coletivo ou segurança nacional (CF, art. 173) — é criada com finalidade lucrativa, ainda que o lucro possa ocorrer como consequência."
    ),
    (
        "O princípio da especialidade, aplicado às entidades da Administração Indireta, implica dizer que:",
        ["A finalidade específica de cada entidade é definida já na lei que autoriza ou determina sua criação, não podendo ser alterada por simples ato do administrador, mas somente por nova lei.", "Cada entidade da Administração Indireta pode livremente redefinir sua própria finalidade, conforme a conveniência da sua direção.", "A finalidade específica é fixada por decreto do chefe do Poder Executivo, independentemente do instrumento usado para a criação da entidade.", "O princípio da especialidade aplica-se somente às autarquias, não alcançando empresas públicas ou sociedades de economia mista.", "A mudança de finalidade de uma entidade da Administração Indireta prescinde de qualquer formalidade legal."],
        0,
        "8.2 — Sem fins lucrativos e finalidade específica",
        "Correto o item A. Pelo princípio da especialidade, a finalidade de cada entidade é definida na própria lei de criação/autorização, e sua alteração exige nova lei — nunca ato discricionário do administrador."
    ),
    (
        "Quanto às formas de controle exercidas sobre as entidades da Administração Indireta, é correto afirmar que:",
        ["O Poder Executivo exerce a supervisão ministerial (controle finalístico, de receitas e despesas, podendo nomear dirigentes); o Legislativo controla por meio do Tribunal de Contas e de CPIs; e o Judiciário controla a legalidade dos atos por meio de ações judiciais.", "Apenas o Poder Executivo exerce controle sobre a Administração Indireta, excluídos o Legislativo e o Judiciário.", "O controle exercido sobre a Administração Indireta é sempre hierárquico, da mesma natureza do controle interno dentro da Administração Direta.", "O Tribunal de Contas não possui competência para fiscalizar entidades da Administração Indireta dotadas de personalidade jurídica de direito privado.", "As entidades da Administração Indireta, por gozarem de autonomia plena, estão imunes a qualquer forma de controle externo."],
        0,
        "8.2 — Ausência de hierarquia: controle finalístico e supervisão ministerial",
        "Correto o item A. Os três Poderes exercem controle sobre a Administração Indireta: Executivo (supervisão ministerial/controle finalístico), Legislativo (Tribunal de Contas e CPIs) e Judiciário (controle de legalidade via ações judiciais) — nunca controle hierárquico, que pressuporia subordinação inexistente."
    ),
    (
        "A autarquia, dentre todas as entidades da Administração Indireta, apresenta a seguinte peculiaridade:",
        ["É a única que possui personalidade jurídica de direito público sempre, submetendo-se, por isso, a regime jurídico integralmente público, sendo criada por lei específica para exercer atividade típica do Estado.", "Pode ter personalidade jurídica de direito público ou de direito privado, a critério do administrador no momento da criação.", "É a única entidade da Administração Indireta que pode explorar atividade econômica com finalidade lucrativa.", "Depende de registro de seus atos constitutivos em cartório para passar a existir, assim como as empresas estatais.", "Submete-se a regime jurídico predominantemente privado, equiparando-se às sociedades de economia mista."],
        0,
        "8.2 — Autarquia: conceito e natureza jurídica",
        "Correto o item A. A autarquia é a única entidade da Administração Indireta com personalidade de direito público sempre — diferentemente da fundação pública, que pode ter regime público ou privado, e das empresas estatais, sempre de direito privado."
    ),
    (
        "Em relação aos privilégios processuais das autarquias, previstos no art. 183 do Código de Processo Civil, é correto afirmar que:",
        ["As autarquias possuem prazo em dobro para se manifestar em processos judiciais, além de se sujeitarem à remessa necessária quando sucumbentes, tornando obrigatório o duplo grau de jurisdição.", "As autarquias não gozam de qualquer prazo diferenciado em relação aos particulares, equiparando-se a estes em juízo.", "A remessa necessária é vedada às autarquias, por se tratar de prerrogativa exclusiva dos entes políticos.", "O prazo em dobro previsto no CPC aplica-se apenas às autarquias federais, não alcançando as estaduais e municipais.", "As autarquias, por gozarem de imunidade tributária, estão dispensadas de qualquer prazo processual."],
        0,
        "8.2 — Autarquia: privilégios e características",
        "Correto o item A. O art. 183 do CPC garante às autarquias prazo em dobro e sujeição à remessa necessária (reexame obrigatório) quando a decisão lhes for desfavorável — prerrogativas decorrentes da sua personalidade de direito público, sem distinção entre esferas federativas."
    ),
    (
        "A respeito dos bens das autarquias, é correto afirmar que:",
        ["São considerados bens públicos, sendo impenhoráveis e imprescritíveis (não sujeitos a usucapião), com inalienabilidade apenas condicionada, já que os bens dominicais podem ser alienados, desde que atendidas as exigências legais.", "São sempre bens privados, por força da autonomia patrimonial conferida à autarquia em relação ao ente que a instituiu.", "São absolutamente inalienáveis, não podendo ser alienados em nenhuma hipótese, ainda que se trate de bens dominicais.", "Podem ser livremente penhorados para satisfação de dívidas da autarquia perante terceiros.", "Estão sujeitos a usucapião, desde que o particular comprove posse mansa e pacífica por prazo superior a 15 anos."],
        0,
        "8.2 — Autarquia: privilégios e características",
        "Correto o item A. Os bens das autarquias, por serem pessoas jurídicas de direito público, são bens públicos: impenhoráveis, imprescritíveis, e com inalienabilidade apenas condicionada (não absoluta) quanto aos bens dominicais."
    ),
    (
        "Sobre as empresas estatais (gênero que abrange empresa pública e sociedade de economia mista), é correto afirmar que:",
        ["Possuem personalidade jurídica de direito privado, são criadas por lei que apenas autoriza sua instituição, com posterior registro, mas somente se extinguem por lei específica, sendo a maioria do capital votante sempre detida pelo poder público.", "Possuem personalidade jurídica de direito público, equiparando-se, nesse aspecto, às autarquias.", "Podem ser extintas por simples decreto do chefe do Poder Executivo, independentemente de lei.", "São sempre criadas diretamente por lei, dispensando qualquer ato de registro posterior à sua instituição.", "O poder público pode deter capital minoritário nessas entidades, desde que mantenha o controle administrativo por outros meios."],
        0,
        "8.2 — Empresas estatais: conceito e traços comuns",
        "Correto o item A. As empresas estatais (empresa pública e SEM) têm personalidade privada, nascem de lei autorizativa seguida de registro, só se extinguem por lei específica, e pressupõem sempre a maioria do capital votante nas mãos do poder público."
    ),
    (
        "Comparando empresa pública e sociedade de economia mista, nos termos da Lei nº 13.303/2016, é correto afirmar que:",
        ["A empresa pública admite capital 100% público, podendo ser constituída sob qualquer modalidade societária; já a sociedade de economia mista tem capital misto (majoritariamente público) e somente pode ser constituída sob a forma de sociedade anônima.", "Ambas somente podem ser constituídas sob a forma de sociedade anônima, sendo essa a única distinção relevante entre elas.", "A sociedade de economia mista admite capital 100% público, ao passo que a empresa pública exige, obrigatoriamente, capital misto.", "Apenas a sociedade de economia mista pode ter mais de um sócio; a empresa pública é sempre unipessoal.", "Não há qualquer distinção quanto à forma societária admitida para cada uma dessas entidades."],
        0,
        "8.2 — Empresa Pública x Sociedade de Economia Mista",
        "Correto o item A, nos termos dos arts. 3º e 4º da Lei nº 13.303/2016: empresa pública tem capital exclusivamente público e pode adotar qualquer forma societária; a SEM tem capital misto (maioria pública) e só pode ser S/A."
    ),
    (
        "Quanto à competência para processar e julgar ações envolvendo empresas públicas e sociedades de economia mista federais, é correto afirmar que:",
        ["Compete à Justiça Federal processar e julgar causas em que a empresa pública federal seja parte, nos termos do art. 109, I, da CF, ao passo que a sociedade de economia mista federal se submete, em regra, à Justiça comum estadual.", "Ambas se submetem, invariavelmente, à Justiça Federal, independentemente da esfera federativa a que pertençam.", "Ambas se submetem, invariavelmente, à Justiça comum estadual, ainda que sejam federais.", "A competência depende exclusivamente do objeto social da entidade (prestação de serviço público ou exploração de atividade econômica), e não da sua natureza jurídica.", "Compete à Justiça do Trabalho processar e julgar toda e qualquer causa envolvendo empresas estatais federais, inclusive as de natureza cível."],
        0,
        "8.2 — Empresa Pública x Sociedade de Economia Mista",
        "Correto o item A. Por expressa disposição do art. 109, I, da CF, a Justiça Federal julga causas de interesse de empresa pública federal; a sociedade de economia mista (mesmo federal) não está nesse rol, submetendo-se à Justiça comum estadual — entendimento pacífico do STF (Súmula 517, STF, por analogia)."
    ),
    (
        "A respeito do regime jurídico das empresas públicas e sociedades de economia mista conforme o objeto para o qual foram criadas, é correto afirmar que:",
        ["As prestadoras de serviço público recebem imunidade tributária, têm bens impenhoráveis, respondem objetivamente e se submetem a execução por precatório, enquanto as exploradoras de atividade econômica não gozam dessas prerrogativas, respondendo subjetivamente e sujeitando-se a execução comum.", "Tanto as prestadoras de serviço público quanto as exploradoras de atividade econômica gozam, em igual medida, de imunidade tributária e execução por precatório.", "As exploradoras de atividade econômica é que gozam de imunidade tributária, justamente para equipará-las à iniciativa privada.", "A responsabilidade civil é sempre objetiva para ambas as categorias, independentemente do objeto social.", "O regime jurídico é idêntico para as duas categorias, não havendo qualquer distinção relevante quanto a bens, tributação ou responsabilidade."],
        0,
        "8.2 — Prestadoras de serviço público x exploradoras de atividade econômica",
        "Correto o item A. O regime varia conforme o objeto: prestadoras de serviço público têm regime mais próximo do direito público (imunidade tributária, bens impenhoráveis, responsabilidade objetiva, precatório); exploradoras de atividade econômica se aproximam do regime privado comum (sem essas prerrogativas, responsabilidade subjetiva)."
    ),
    (
        "De acordo com o Decreto-Lei nº 200/67 e a classificação usual da Administração Pública brasileira, é correto afirmar que:",
        ["As entidades da Administração Indireta são classificadas como entidades administrativas, enquanto a Administração Direta (União, Estados, DF e Municípios) é classificada como entidade política.", "As entidades da Administração Indireta são classificadas como entidades políticas, por deterem personalidade jurídica própria.", "A Administração Direta é classificada como entidade administrativa, por integrar a estrutura da Presidência da República e dos Ministérios.", "Não há distinção entre entidade política e entidade administrativa no direito brasileiro, sendo ambos os termos sinônimos.", "Apenas as autarquias são classificadas como entidades administrativas; as demais entidades da Administração Indireta são classificadas como entidades políticas."],
        0,
        "8.2 — Administração Pública no Brasil: Decreto-Lei nº 200/67",
        "Correto o item A. Trata-se de pegadinha recorrente: entidades da Administração Indireta = entidades administrativas; a Administração Direta (entes federativos) = entidades políticas, dotadas de autonomia e capacidade de autodeterminação legislativa."
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
