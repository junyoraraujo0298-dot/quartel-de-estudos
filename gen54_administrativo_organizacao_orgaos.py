# -*- coding: utf-8 -*-
"""
Quarto conteudo de Direito Administrativo do app (PC-PE) -- a partir do PDF
"Organizacao da Administracao Publica | Administracao Publica Direta"
(Focus Concursos), cobrindo o item 8 do programa oficial ("8. Organizacao
administrativa: 8.1 Centralizacao, descentralizacao, concentracao e
desconcentracao; 8.2 Administracao direta e indireta").

Diferente do PDF da Lei 8.112/90 (que e federal e so serviu de base
doutrinaria generica pros itens 12/13), este PDF cai direto no item 8 do
edital -- organizacao administrativa e administracao direta sao conceitos
de Direito Administrativo puro, sem vinculo com nenhuma esfera federativa
especifica, entao nao ha ressalva de escopo aqui.

A mudanca estrutural em app-template.html ja foi feita via Edit antes deste
script rodar: nova secao "Organizacao Administrativa -- Administracao
Publica Direta e Teoria do Orgao (item 8)" no deck
TEORIA_DIREITO_ADMINISTRATIVO_PCPE ja existente (que ja tinha Fontes,
Principios LIMPE e Agente Publico/Cargo), com 11 itens: conceito de
administracao direta/centralizada; as 4 teorias sobre a relacao Estado x
agente (mandato, representacao, identidade/subjetiva e orgao/imputacao --
essa ultima e a adotada); conceito legal (Lei 9.784/99, art. 1 par. 2 I)
e doutrinario (Hely Lopes Meirelles) de orgao publico; caracteristicas dos
orgaos (rol de 8 pontos, incluindo a excecao de criacao/extincao por
decreto quando nao ha aumento de despesa); capacidade processual/judiciaria
como excecao restrita a independentes e autonomos (Sumula 525 STJ sobre
Camara de Vereadores); e as 5 classificacoes dos orgaos (quanto a posicao
estatal, estrutura, atuacao funcional, funcoes exercidas e esfera de acao
-- essa ultima de Di Pietro). Dois diagramas SVG novos (orgaoPosicao:
piramide Independentes > Autonomos > Superiores > Subalternos; orgaoNaoTem:
esquema do que o orgao NAO tem x o que ele TEM, reproduzindo o
"ESQUEMATIZANDO" do PDF).

18 questoes novas (MC, originais, nao sao transcricao literal do PDF, que
traz questoes Certo/Errado -- convertidas pro formato MC ja padrao do app
pro PC-PE), cada uma testando um fato novo do item 8. Varias exploram a
pegadinha classica de trocar a definicao de "independentes" pela de
"superiores" (e vice-versa), que e o erro mais comum cobrado pelo
CEBRASPE nesse assunto (inclusive aparece registrado no proprio PDF-fonte,
nas questoes 01 e 02 da secao "Questao Comentada").

Este script cuida so de: (1) acrescentar as questoes a questions.json,
(2) regenerar estudo-cebraspe-ma.html a partir do app-template.html ja
editado.
"""
import json

MC_QUESTIONS = [
    (
        "A Administração Pública Direta, também chamada de Administração Pública Centralizada, pode ser corretamente definida como:",
        ["O conjunto de órgãos públicos que integram as pessoas jurídicas políticas (União, Estados, DF e Municípios), para a execução de atividades administrativas de forma centralizada.", "O conjunto de pessoas jurídicas com personalidade própria, criadas por lei para descentralizar a execução de serviços públicos.", "Apenas o Poder Executivo, excluindo-se os órgãos do Legislativo e do Judiciário.", "O conjunto de empresas públicas e sociedades de economia mista vinculadas a cada ente federativo.", "Uma categoria exclusiva da esfera federal, não existente nos Estados, no DF ou nos Municípios."],
        0,
        "8.2 — Administração Pública Direta: conceito",
        "Correto o item A. A Administração Direta (ou Centralizada) é o conjunto de órgãos públicos (sem personalidade jurídica própria) que integram diretamente as pessoas jurídicas políticas, existindo em todos os níveis de governo e em todos os Poderes."
    ),
    (
        "Um servidor lotado no Ministério da Justiça, órgão que integra a Administração Pública Direta da União, é, juridicamente falando:",
        ["Servidor da própria União, já que o Ministério não possui personalidade jurídica independente, sendo o comando sempre exercido por um único centro de poder.", "Servidor do Ministério da Justiça, pessoa jurídica de direito público distinta da União.", "Servidor de uma autarquia federal vinculada à União.", "Servidor de uma entidade da Administração Indireta, por força da descentralização.", "Servidor sem vínculo definido, já que Ministérios não possuem natureza jurídica própria para fins trabalhistas."],
        0,
        "8.2 — Administração Pública Direta: conceito",
        "Correto o item A. Órgãos da Administração Direta, como os Ministérios, não têm personalidade jurídica própria — o servidor neles lotado é, tecnicamente, servidor da própria pessoa jurídica política (no caso, a União)."
    ),
    (
        "Em relação às teorias que buscam explicar a relação entre o Estado e seus agentes, é correto afirmar que, pela teoria do MANDATO:",
        ["O agente é considerado mandatário do Estado, de forma semelhante ao que ocorre no Direito Civil quando uma pessoa outorga a outra uma procuração — teoria criticada, entre outros motivos, por não acarretar qualquer responsabilidade ao Estado caso o ato do mandatário fosse ilícito.", "O agente é equiparado a um tutor ou curador de um incapaz.", "Órgão e agente formam uma unidade inseparável, de modo que o órgão é o próprio agente.", "A conduta do agente é diretamente imputada ao órgão, que responde perante a pessoa jurídica a que pertence.", "É a teoria atualmente adotada pela doutrina brasileira majoritária."],
        0,
        "8.2 — Teorias sobre a relação Estado x agente público",
        "Correto o item A. A teoria do mandato (hoje superada) via o agente como mandatário do Estado; uma das críticas centrais é justamente a ausência de responsabilização do Estado por atos ilícitos do mandatário, já que o Estado, como pessoa jurídica abstrata, não teria existência concreta para efetivamente outorgar esse mandato."
    ),
    (
        "A teoria da IDENTIDADE (ou subjetiva), uma das primeiras a tentar explicar a relação entre Estado e agente público, sofre a seguinte crítica, segundo a doutrina:",
        ["Como o órgão público é, nessa teoria, o próprio agente, levada a lógica às últimas consequências, a morte do agente público causaria a extinção do órgão — o que é evidentemente equivocado.", "Ela atribui ao Estado a condição de incapaz, que deveria ser representado por um tutor ou curador.", "Ela não reconhece qualquer vínculo entre o agente e o Estado.", "Ela é a teoria atualmente adotada e, por isso, não é mais objeto de críticas doutrinárias.", "Ela pressupõe a existência de um contrato de mandato entre agente e Estado."],
        0,
        "8.2 — Teorias sobre a relação Estado x agente público",
        "Correto o item A. Pela teoria da identidade, órgão e agente formam uma unidade inseparável — o equívoco, apontado pela doutrina (Alexandre Mazza), é que essa lógica levaria à conclusão de que a morte do agente extinguiria o órgão, o que não condiz com a realidade (o órgão permanece, e outro agente assume)."
    ),
    (
        "A teoria atualmente adotada pela doutrina moderna para explicar a relação entre o Estado e os agentes públicos é a teoria:",
        ["Do órgão, também chamada de teoria da imputação, segundo a qual toda conduta praticada pelo agente é imputada ao órgão, que está ligado à entidade dotada de personalidade jurídica, sendo esta, ao final, quem responde juridicamente.", "Do mandato, segundo a qual o agente atua como mandatário do Estado.", "Da representação, segundo a qual o agente representa o Estado à semelhança do tutor do incapaz.", "Da identidade, segundo a qual o órgão se confunde com a pessoa do próprio agente.", "Contratualista, segundo a qual a relação entre agente e Estado é de natureza puramente contratual privada."],
        0,
        "8.2 — Teoria do Órgão (Teoria da Imputação)",
        "Correto o item A. A teoria do órgão (ou da imputação) é a atualmente adotada: o agente é um veículo de expressão da vontade estatal, e sua conduta é imputada ao órgão a que pertence, que por sua vez se vincula à pessoa jurídica dotada de personalidade."
    ),
    (
        "Segundo a doutrina de Alexandre Mazza sobre a teoria do órgão, é correto afirmar que:",
        ["Os órgãos públicos não são pessoas, mas partes integrantes da pessoa estatal — a personalidade, no corpo como no Estado, é atributo do todo, e não das partes.", "Os órgãos públicos possuem personalidade jurídica própria, distinta da pessoa jurídica a que pertencem.", "A personalidade jurídica é atributo de cada órgão isoladamente considerado, e não da entidade estatal como um todo.", "A teoria do órgão rejeita qualquer analogia entre a estrutura do Estado e a estrutura do corpo humano.", "Pela teoria do órgão, cada repartição estatal possui vontade própria, independente da pessoa jurídica a que se vincula."],
        0,
        "8.2 — Teoria do Órgão (Teoria da Imputação)",
        "Correto o item A, conforme a lição de Alexandre Mazza citada no material: a personalidade é atributo do todo (a pessoa jurídica estatal), não das partes (os órgãos) — por isso os órgãos não são pessoas."
    ),
    (
        "Nos termos do art. 1º, §2º, inciso I, da Lei nº 9.784/1999, que disciplina o processo administrativo no âmbito da Administração Pública Federal, órgão é definido como:",
        ["A unidade de atuação integrante da estrutura da Administração direta e da estrutura da Administração indireta.", "A pessoa jurídica de direito público criada por lei específica para descentralizar serviços públicos.", "O conjunto de agentes públicos hierarquicamente organizados dentro de uma entidade.", "A unidade de atuação exclusiva da Administração direta, não se aplicando à Administração indireta.", "Qualquer entidade pública ou privada que preste serviço público mediante delegação."],
        0,
        "8.2 — Conceito legal e doutrinário de órgão público",
        "Correto o item A, nos termos literais do art. 1º, §2º, I, da Lei nº 9.784/1999 — a definição legal deixa claro que órgão existe tanto na Administração direta quanto na indireta, não sendo exclusividade de nenhuma delas."
    ),
    (
        "Em relação às características dos órgãos públicos, é correto afirmar que:",
        ["No âmbito da Administração Direta, a criação e a extinção de órgãos dependem de lei; contudo, a mera disciplina da organização e do funcionamento do órgão, desde que não implique aumento de despesa, pode ser veiculada por decreto do chefe do Poder Executivo.", "A criação e a extinção de órgãos públicos sempre podem ser feitas por simples decreto do chefe do Poder Executivo, independentemente de aumento de despesa.", "Os órgãos públicos possuem personalidade jurídica própria, distinta da entidade a que pertencem.", "A divisão em órgãos é fenômeno exclusivo da Administração Direta, não existindo na estrutura da Administração Indireta.", "Os órgãos públicos, em regra, possuem plena capacidade processual para defesa de seus próprios interesses."],
        0,
        "8.2 — Características dos Órgãos Públicos",
        "Correto o item A. A regra geral é a exigência de lei para criar/extinguir órgãos; a exceção (decreto) só vale para a mera organização/funcionamento interno, sem aumento de despesa."
    ),
    (
        "Embora o órgão público possa, para fins orçamentários, possuir CNPJ próprio, é correto afirmar que:",
        ["Isso não lhe confere personalidade jurídica — o cadastramento do órgão é mera exigência orçamentária, para organização de finanças e orçamento público, e o órgão continua sem personalidade jurídica, patrimônio, vida ou direitos próprios.", "O órgão passa a ter personalidade jurídica própria a partir do momento em que obtém CNPJ.", "A posse de CNPJ equivale, para todos os efeitos, ao reconhecimento de capacidade processual plena ao órgão.", "Apenas os órgãos da Administração Indireta podem possuir CNPJ, nunca os da Administração Direta.", "O CNPJ do órgão substitui o CNPJ da pessoa jurídica a que ele pertence, para todos os efeitos legais."],
        0,
        "8.2 — Características dos Órgãos Públicos",
        "Correto o item A. CNPJ de órgão é mera formalidade orçamentária/contábil; não se confunde com personalidade jurídica, que o órgão nunca possui — o órgão é apenas uma parcela da pessoa jurídica (o todo)."
    ),
    (
        "Em relação à capacidade processual (ou judiciária) dos órgãos públicos, é correto afirmar que:",
        ["Trata-se de exceção excepcionalíssima, reconhecida pela doutrina e jurisprudência apenas aos órgãos independentes e autônomos, para a defesa de suas competências e prerrogativas funcionais violadas por outro órgão.", "Todo e qualquer órgão público possui, em regra, capacidade processual plena para a defesa de seus interesses em juízo.", "A capacidade processual é reconhecida apenas aos órgãos subalternos, que resolvem seus conflitos exclusivamente por via judicial.", "A capacidade processual pressupõe, necessariamente, o reconhecimento prévio de personalidade jurídica ao órgão.", "Órgãos superiores podem demandar judicialmente contra órgãos independentes em caso de conflito de atribuições."],
        0,
        "8.2 — Capacidade Processual (Judiciária) do Órgão: Exceção",
        "Correto o item A. A capacidade processual/judiciária é exceção raríssima, restrita aos órgãos independentes e autônomos; órgãos superiores e subalternos resolvem seus conflitos por via administrativa/hierárquica, sem poder demandar em juízo."
    ),
    (
        "Segundo a Súmula 525 do STJ, é correto afirmar que a Câmara de Vereadores:",
        ["Não possui personalidade jurídica, mas possui personalidade judiciária, somente podendo demandar em juízo para defender os seus direitos institucionais.", "Possui plena personalidade jurídica, podendo demandar em juízo para a defesa de quaisquer interesses do Município.", "Não possui personalidade jurídica nem personalidade judiciária, jamais podendo demandar em juízo.", "Possui personalidade jurídica apenas para fins orçamentários, mas não para fins processuais.", "É equiparada, para todos os fins, a uma autarquia municipal."],
        0,
        "8.2 — Capacidade Processual (Judiciária) do Órgão: Exceção",
        "Correto o item A, nos termos literais da Súmula 525 do STJ — exemplo clássico de órgão (a Câmara de Vereadores é órgão do Poder Legislativo municipal, sem personalidade jurídica) com personalidade judiciária excepcional, restrita à defesa de seus direitos institucionais."
    ),
    (
        "Quanto à classificação dos órgãos públicos pela posição estatal, é correto afirmar que os órgãos INDEPENDENTES:",
        ["São originários da Constituição, representativos dos Poderes Legislativo, Executivo e Judiciário, sem subordinação hierárquica ou funcional, sujeitando-se exclusivamente aos controles constitucionais entre os Poderes.", "Encontram-se subordinados hierarquicamente aos órgãos autônomos, formando a cúpula intermediária da Administração.", "Têm liberdade funcional restrita ao planejamento e a soluções técnicas, sendo a execução feita, em regra, por órgãos subalternos.", "Representam o último escalão da Administração, com reduzido poder decisório.", "São exemplificados por Inspetorias-Gerais, Coordenadorias e Divisões."],
        0,
        "8.2 — Classificação quanto à Posição Estatal: Independentes",
        "Correto o item A. Órgãos independentes (Casas Legislativas, Chefias do Executivo, Ministério Público, Defensorias, Tribunais de Contas, Tribunais e juízes) são os únicos sem qualquer subordinação hierárquica — a alternativa C descreve órgãos superiores, e a D e E descrevem subalternos."
    ),
    (
        "Em relação aos órgãos AUTÔNOMOS, é correto afirmar que:",
        ["Encontram-se na cúpula da Administração, logo abaixo dos órgãos independentes, a eles subordinados, gozando de autonomia administrativa, financeira e técnica — são exemplos os Ministérios, as Secretarias estaduais e municipais e a Advocacia-Geral da União.", "São originários diretamente da Constituição, representando os três Poderes do Estado, sem qualquer subordinação.", "Não gozam de autonomia administrativa nem financeira, atributos exclusivos dos órgãos independentes.", "Representam o último escalão hierárquico da Administração Pública.", "São exemplificados pelas Inspetorias-Gerais e pelos Gabinetes."],
        0,
        "8.2 — Classificação quanto à Posição Estatal: Autônomos",
        "Correto o item A. Diferentemente dos independentes, os autônomos não são originários da Constituição — estão subordinados aos independentes, mas gozam de ampla autonomia administrativa, financeira e técnica, sendo responsáveis por planejamento, supervisão, coordenação e controle."
    ),
    (
        "Assinale a alternativa que descreve corretamente os órgãos SUPERIORES, segundo a classificação quanto à posição estatal:",
        ["Detêm poder de direção, controle, decisão e comando em assuntos de sua competência específica, mas não gozam de autonomia administrativa nem financeira, atributos dos órgãos independentes e autônomos a que pertencem.", "São originários da Constituição e representativos dos Poderes de Estado, sem qualquer subordinação hierárquica ou funcional.", "Representam o último escalão da Administração, com atribuições predominantemente de execução.", "Gozam de autonomia administrativa, financeira e técnica, caracterizando-se como órgãos diretivos subordinados apenas aos independentes.", "São exemplificados pelo Congresso Nacional e pelo Senado Federal."],
        0,
        "8.2 — Classificação quanto à Posição Estatal: Superiores",
        "Correto o item A. Órgãos superiores (Gabinetes, Inspetorias-Gerais, Coordenadorias, Departamentos, Divisões) têm poder de direção/controle/decisão/comando em sua área, mas sem autonomia administrativa ou financeira — essa é exatamente a troca de definição que o CEBRASPE usa como pegadinha, atribuindo aos superiores a definição dos independentes (ou vice-versa)."
    ),
    (
        "Os órgãos SUBALTERNOS, última categoria da classificação quanto à posição estatal, caracterizam-se por:",
        ["Representarem o último escalão da Administração, com reduzido poder decisório e predominância de atribuições de execução, a exemplo das atividades-meio e do atendimento ao público (portarias, protocolos, seções de expediente).", "Serem originários da Constituição, sem qualquer subordinação hierárquica.", "Gozarem de autonomia administrativa, financeira e técnica, equiparando-se aos órgãos autônomos.", "Deterem poder de direção, controle, decisão e comando em assuntos de sua competência específica.", "Resolverem seus conflitos de atribuições exclusivamente por via judicial, por possuírem capacidade processual."],
        0,
        "8.2 — Classificação quanto à Posição Estatal: Subalternos",
        "Correto o item A. Subalternos são o último escalão, com atribuições essencialmente de execução e reduzido (ou nenhum) poder decisório — exatamente o oposto da descrição dos órgãos independentes."
    ),
    (
        "Quanto à sua estrutura, os órgãos públicos classificam-se em simples (ou unitários) e compostos. É correto afirmar que:",
        ["Órgãos compostos reúnem em sua estrutura outros órgãos menores, uns exercendo atividade-fim (idêntica à principal) e outros exercendo atividade-meio (função auxiliar diferente da principal) — são exemplos as Secretarias e os Ministérios.", "Órgãos simples são aqueles que reúnem em sua estrutura diversos órgãos menores, com funções auxiliares diversificadas.", "A classificação quanto à estrutura do órgão determina, por si só, a classificação do ato administrativo que ele venha a praticar.", "Órgãos compostos são, necessariamente, os mesmos que os órgãos colegiados ou pluripessoais.", "Presidência da República e Portarias são exemplos clássicos de órgãos compostos."],
        0,
        "8.2 — Classificação quanto à Estrutura: Simples x Compostos",
        "Correto o item A. Órgãos simples (unitários) têm um único centro de competência (ex.: Presidência da República); compostos reúnem órgãos menores de atividade-fim e atividade-meio (ex.: Secretarias, Ministérios). A estrutura do órgão NÃO determina a classificação do ato que ele pratica."
    ),
    (
        "Em relação à classificação dos órgãos quanto à atuação funcional, é correto afirmar que os órgãos COLEGIADOS (ou pluripessoais):",
        ["Atuam e decidem pela manifestação conjunta e majoritária da vontade de seus membros, não prevalecendo a vontade pessoal do chefe ou de qualquer outro integrante isoladamente — são exemplos as Corporações Legislativas, os Tribunais e as Comissões.", "Apresentam um só titular, chefe e representante, que desempenha a função principal individualmente.", "Têm sua manifestação de vontade dependente exclusivamente da decisão pessoal do seu presidente.", "São sinônimos de órgãos compostos, classificação relativa à estrutura do órgão.", "São exemplificados pela Presidência da República e pelas Prefeituras."],
        0,
        "8.2 — Classificação quanto à Atuação Funcional: Singulares x Colegiados",
        "Correto o item A. Órgãos colegiados decidem pela vontade conjunta e majoritária dos membros (ex.: Tribunais, Comissões, Corporações Legislativas) — diferente dos singulares/unipessoais (ex.: Presidência da República), cuja vontade é formada por um único titular, sem depender do acordo de outra autoridade."
    ),
    (
        "Quanto às funções exercidas, os órgãos públicos podem ser classificados em ativos, de consulta e de controle. É correto afirmar que os órgãos DE CONSULTA:",
        ["Produzem pareceres e opiniões necessários para a tomada de decisão por parte dos órgãos ativos — são exemplo as assessorias jurídicas integrantes das estruturas dos Ministérios.", "Produzem ações e atos necessários ao cumprimento direto dos fins da pessoa jurídica da qual fazem parte.", "São responsáveis por acompanhar e fiscalizar outros órgãos, a exemplo do Tribunal de Contas da União.", "Detêm poder de decisão final sobre as matérias de competência dos órgãos ativos, substituindo-os.", "Correspondem, na classificação quanto à posição estatal, aos órgãos autônomos."],
        0,
        "8.2 — Classificação quanto às Funções Exercidas",
        "Correto o item A. Órgãos de consulta (como assessorias jurídicas) produzem pareceres/opiniões que subsidiam a decisão dos órgãos ativos (que produzem os atos finalísticos, como Ministérios e Secretarias); os órgãos de controle (como o TCU) fiscalizam outros órgãos."
    ),
    (
        "A classificação dos órgãos públicos quanto à esfera de ação, apresentada pela doutrinadora Maria Sylvia Zanella Di Pietro, divide os órgãos em centrais e locais. É correto afirmar que os órgãos LOCAIS:",
        ["Atuam apenas sobre uma parte do território, em atuação localizada — são exemplo as Delegacias Regionais da Receita Federal, as Delegacias de Polícia e os Postos de Saúde.", "Exercem atribuições em todo o território nacional, estadual ou municipal, a exemplo dos Ministérios e das Secretarias de Estado.", "Correspondem, na classificação quanto à posição estatal, aos órgãos independentes.", "São sinônimos de órgãos colegiados, na classificação quanto à atuação funcional.", "Não podem, em nenhuma hipótese, integrar a estrutura da Administração Direta."],
        0,
        "8.2 — Classificação quanto à Esfera de Ação (Di Pietro)",
        "Correto o item A. Órgãos locais (Delegacias Regionais, Delegacias de Polícia, Postos de Saúde) atuam sobre parte do território; os órgãos centrais (Ministérios, Secretarias) exercem atribuições em todo o território do ente a que pertencem."
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
