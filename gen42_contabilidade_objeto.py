# -*- coding: utf-8 -*-
"""
Segundo conteudo de Contabilidade Geral do app (PC-PE) -- a partir do PDF
"Objeto da Contabilidade" (Focus Concursos), que cobre o item 2
("Patrimonio: componentes, equacao fundamental do patrimonio, situacao
liquida, representacao grafica") do PROGRAMA_PCPE_AGENTE oficial.

A mudanca estrutural em app-template.html ja foi feita via Edit antes deste
script rodar: foram acrescentados itens ao const TEORIA_CONTABILIDADE_PCPE
ja existente (nao um novo deck -- e a mesma materia, Contabilidade Geral),
numa nova secao "Objeto da Contabilidade - Patrimonio": o objeto sempre e
o patrimonio; qualidades do patrimonio (tangivel/intangivel, onerado/nao
onerado, adquirido/formado/produzido/recebido/mantido/utilizado); conceitos
de bens, direitos e obrigacoes; teoria personalista (Primeiro = empresa,
Segundo = socios, Terceiros = credores/devedores); estrutura do Balanco
Patrimonial (Ativo, Passivo, PL); Patrimonio Liquido como "sobra" e Capital
Proprio (teoria da propriedade); art. 178 da Lei 6.404/1976 (estrutura do
Ativo e Passivo, com a pegadinha do PL "dentro" do Passivo pela lei
societaria); sinonimos de Ativo/Passivo/PL; a equacao patrimonial e suas
variacoes; e o patrimonio sob o olhar de outras ciencias (Direito).

O PDF trazia uma "Maratona de Questoes" com 22 itens prontos, misturando
Certo/Errado (1 a 7) e multipla escolha (8 a 22, 4 delas com so 4
alternativas no original -- foi acrescentada uma 5a alternativa so pra
manter o schema do app, sem mudar o gabarito). Boa parte dos itens (sobretudo
os C/E 1, 2, 3, 5 e varias das MC 9, 13, 14, 19, 20, 21) testava
repetidamente o MESMO fato ("o objeto da contabilidade e sempre o
patrimonio"), entao nao foram todos transcritos/convertidos 1 a 1: o espaco
liberado pela consolidacao foi usado pra cobrir, com questoes originais, os
fatos ricos do PDF que so apareciam no texto corrido e ainda nao tinham
questao nenhuma (teoria personalista, estrutura do Balanco segundo a Lei
6.404/1976 -- incluindo a pegadinha do PL dentro do Passivo --, sinonimos de
Ativo/Passivo/PL, a equacao patrimonial e suas variacoes, as qualidades do
patrimonio do conceito do CFC, e a distincao Direitos x Obrigacoes).

Este script cuida so de: (1) acrescentar as questoes a questions.json,
(2) regenerar estudo-cebraspe-ma.html a partir do app-template.html ja
editado.
"""
import json

ASSUNTO = "2 — Contabilidade Geral: Objeto da Contabilidade (Patrimônio)"

MC_QUESTIONS = [
    (
        "O conjunto de bens, direitos e obrigações pertencentes a uma pessoa física ou jurídica ou a um conjunto de pessoas, susceptíveis de avaliação econômica, é o conceito de:",
        ["passivo.", "ativo.", "situação líquida.", "obrigações exigíveis.", "patrimônio."],
        4,
        ASSUNTO,
        "Correto o item E. PATRIMÔNIO é o conjunto de recursos próprios e de terceiros representados pelos bens, direitos e obrigações de uma empresa."
    ),
    (
        "O patrimônio é definido como sendo:",
        ["O conjunto de bens tangíveis e intangíveis de propriedade de uma empresa.", "Os bens da empresa utilizados para atingimento de seus objetivos.", "Bens, valores e as obrigações com sócios e terceiros.", "Conjunto de bens, direitos e obrigações pertencentes a uma determinada entidade.", "Conjunto de ativos circulantes e não circulantes de uma entidade."],
        3,
        ASSUNTO,
        "Correto o item D. O patrimônio é o conjunto dos bens, direitos e obrigações de uma entidade. O item C erra porque 'valores' não é o mesmo que 'direitos' — lembre-se de que as obrigações podem ser junto a terceiros (passivo exigível) ou junto aos sócios (patrimônio líquido)."
    ),
    (
        "O conceito de patrimônio de uma empresa abrange:",
        ["bens e direitos mais obrigações.", "bens e direitos menos obrigações.", "bens e direitos apenas.", "bens tangíveis e direitos.", "bens tangíveis e bens intangíveis."],
        0,
        ASSUNTO,
        "Correto o item A. Patrimônio é o conjunto de bens, direitos e obrigações vinculado a uma pessoa ou entidade — representa a soma dos bens mais direitos mais obrigações (não a diferença entre eles, que seria o Patrimônio Líquido)."
    ),
    (
        "Assinale a alternativa que representa o conceito de Bens sob a ótica da contabilidade.",
        ["São itens corpóreos mensuráveis em dinheiro que podem integrar o patrimônio das entidades para utilização futura, tais como marcas e patentes.", "São os itens que estão em poder de terceiros que podem ser utilizados de forma imediata.", "São itens incorpóreos que são mensuráveis em dinheiro que podem ser tocados, tais como máquinas e veículos.", "São os direitos de terceiros em poder da entidade.", "São itens tangíveis e intangíveis quantificáveis em dinheiro e que integrarão o patrimônio da entidade para utilização imediata."],
        4,
        ASSUNTO,
        "Correto o item E. Os bens representam os ativos tangíveis (máquinas, equipamentos, estoques etc.) e intangíveis (marca, fórmulas, softwares etc.) que podem ser mensurados economicamente e serão utilizados pela empresa em suas atividades."
    ),
    (
        "Na bibliografia, Ribeiro (2017) afirma que 'o patrimônio é um conjunto de Bens, Direitos e Obrigações de uma pessoa, avaliado em moeda'. Considerando os elementos que compõem o Patrimônio, marque a alternativa INCORRETA:",
        ["Os Bens são as coisas capazes de satisfazer as necessidades humanas e suscetíveis de avaliação econômica.", "Constituem Direitos para a empresa todos os valores que ela tem a receber de terceiros (clientes, inquilinos, etc.).", "Constituem Obrigações para a empresa todos os valores que ela tem a pagar para terceiros (fornecedores, proprietários de imóveis, empregados, Governo, bancos, etc.).", "As Obrigações geralmente aparecem registradas nos livros contábeis das empresas, com o nome do elemento representativo seguido da expressão 'a pagar'.", "Os Direitos geralmente aparecem registrados nos livros contábeis da empresa, com o nome do elemento representativo seguido da expressão 'a pagar'."],
        4,
        ASSUNTO,
        "Correto o item E — é a assertiva INCORRETA, portanto o gabarito. Os Direitos são contas contábeis registradas com o nome do item complementado pelo termo 'A RECEBER', e não 'a pagar'; essa expressão é característica das contas de Obrigações."
    ),
    (
        "Indique a alternativa incorreta.",
        ["Patrimônio é um conjunto de bens, direitos e obrigações vinculado a uma pessoa física ou jurídica ou a uma entidade.", "O objeto da contabilidade é o patrimônio da entidade.", "O campo de aplicação da contabilidade são as aziendas.", "Direitos são dívidas ou compromissos de qualquer espécie ou natureza assumidos perante terceiros, ou bens de terceiros que se encontram em posse (uso) da entidade.", "As obrigações podem ser junto a terceiros (passivo exigível) ou junto aos sócios (patrimônio líquido)."],
        3,
        ASSUNTO,
        "Correto o item D — é a assertiva INCORRETA, portanto o gabarito —, pois Direitos NÃO são dívidas. Os direitos representam os créditos que a empresa possui, especialmente junto a seus clientes; também podem decorrer de despesas pagas antecipadamente (ex.: aluguel) ou de impostos a recuperar junto ao poder público."
    ),
    (
        "Segundo a teoria personalista da Contabilidade, ao se falar em 'terceiros' em relação a uma entidade, está-se referindo a:",
        ["Os sócios da entidade, que têm responsabilidade indireta pelas negociações da empresa.", "A própria entidade, enquanto personalidade jurídica.", "Os credores e devedores da entidade — ou seja, suas obrigações (fornecedores) e seus direitos (clientes).", "Exclusivamente os clientes da entidade, que representam direitos a receber.", "Exclusivamente os fornecedores da entidade, que representam obrigações a pagar."],
        2,
        ASSUNTO,
        "Correto o item C. Na teoria personalista: Primeiro é a empresa (a personalidade jurídica); Segundo são os sócios, com responsabilidade indireta pelas negociações do primeiro — o patrimônio da empresa é diferente do patrimônio do sócio; Terceiros são os credores e devedores em relação ao primeiro, ou seja, as obrigações (fornecedores) e os direitos (clientes) da empresa."
    ),
    (
        "No Balanço Patrimonial, os bens e direitos formam o lado:",
        ["Ativo, onde está o potencial econômico da empresa.", "Passivo, onde estão as exigibilidades da empresa.", "Patrimônio Líquido, como capital próprio da empresa.", "Resultado, como lucro ou prejuízo apurado.", "Nenhum grupo específico — ficam fora do Balanço Patrimonial."],
        0,
        ASSUNTO,
        "Correto o item A. Os bens e direitos formam o lado ATIVO do patrimônio, onde está o potencial econômico da empresa; já as obrigações apresentam o lado PASSIVO, com as exigibilidades junto a terceiros e as obrigações não exigíveis junto aos sócios."
    ),
    (
        "Assinale a alternativa correta sobre o Patrimônio Líquido (PL):",
        ["PL = bens + direitos – obrigações, representando o valor residual dos ativos da entidade depois de deduzidos os passivos exigíveis.", "PL = bens + direitos + obrigações, somando todo o patrimônio bruto da entidade.", "PL é sinônimo de Patrimônio, podendo ser usado indistintamente.", "PL representa exclusivamente as obrigações da empresa junto a terceiros.", "PL é calculado antes de se apurar o total do Ativo da entidade."],
        0,
        ASSUNTO,
        "Correto o item A. PL = bens + direitos – obrigações; estruturalmente, é uma SOBRA, por isso também chamado de Capital Próprio — pela teoria da propriedade, o sócio não empresta dinheiro à empresa, ele aplica no capital social dela, esperando a valorização do investimento. Patrimônio e Patrimônio Líquido NÃO são sinônimos: o primeiro é o total (bens + direitos + obrigações)."
    ),
    (
        "Patrimônio Bruto é sinônimo de:",
        ["Capital Aplicado (Ativo).", "Capital Fixo.", "Capital Próprio.", "Capital de Terceiros.", "Capital Alheio."],
        0,
        ASSUNTO,
        "Correto o item A. Patrimônio Bruto é outra denominação para o ATIVO, também chamado de Capital Total ou Capital Aplicado ou Realizável. Capital Próprio é sinônimo de Patrimônio Líquido; Capital de Terceiros/Capital Alheio são sinônimos de Passivo."
    ),
    (
        "Assinale a alternativa que reúne corretamente sinônimos usados pela banca para os componentes do patrimônio:",
        ["Ativo = Patrimônio de terceiros; Passivo = Capital aplicado; PL = Capital alheio.", "Ativo = Patrimônio bruto ou Capital aplicado; Passivo = Patrimônio de terceiros ou Capital alheio ou Exigível; PL = Capital próprio ou resíduo patrimonial ou passivo não exigível.", "Ativo = Exigível; Passivo = Realizável; PL = Capital total.", "Ativo, Passivo e PL são sinônimos entre si, usados apenas por preferência estilística do autor.", "Ativo = Capital próprio; Passivo = Capital aplicado; PL = Patrimônio bruto."],
        1,
        ASSUNTO,
        "Correto o item B. Ativo = Patrimônio bruto, Capital total, Capital aplicado ou Realizável. Passivo = Patrimônio de terceiros, Capital alheio ou Exigível. Patrimônio Líquido = Capital próprio, Resíduo patrimonial ou Passivo não exigível."
    ),
    (
        "A equação patrimonial fundamental, da qual decorrem outras denominações equivalentes (como 'patrimônio bruto = patrimônio alheio + patrimônio líquido'), é corretamente expressa por:",
        ["Ativo = Passivo + Patrimônio Líquido.", "Ativo = Passivo – Patrimônio Líquido.", "Passivo = Ativo + Patrimônio Líquido.", "Patrimônio Líquido = Ativo + Passivo.", "Ativo + Passivo = Patrimônio Líquido."],
        0,
        ASSUNTO,
        "Correto o item A. A equação patrimonial fundamental é Ativo = Passivo + Patrimônio Líquido — também apresentada como Bens + Direitos = Obrigações + Capital Próprio, ou Patrimônio bruto = Patrimônio alheio + Patrimônio líquido, ou Capital total aplicado = Capital de terceiros + Capital próprio."
    ),
    (
        "Nos termos do art. 178 da Lei nº 6.404/1976, o Ativo, no Balanço Patrimonial, é disposto nos seguintes grupos:",
        ["Ativo circulante e ativo não circulante (este composto por realizável a longo prazo, investimentos, imobilizado e intangível).", "Ativo circulante, ativo fixo e ativo diferido.", "Ativo exigível e ativo não exigível.", "Ativo operacional e ativo financeiro.", "Ativo próprio e ativo de terceiros."],
        0,
        ASSUNTO,
        "Correto o item A. O art. 178, §1º, da Lei nº 6.404/1976 dispõe que, no ativo, as contas serão classificadas em ativo circulante e ativo não circulante — este último composto por ativo realizável a longo prazo, investimentos, imobilizado e intangível."
    ),
    (
        "Segundo o art. 178, §2º, da Lei nº 6.404/1976 ('Lei das Sociedades Anônimas'), o Passivo é classificado nos seguintes grupos:",
        ["Passivo circulante, passivo não circulante e patrimônio líquido.", "Passivo circulante e passivo não circulante, apenas — o patrimônio líquido fica fora do Balanço.", "Passivo exigível e patrimônio bruto.", "Passivo operacional, passivo financeiro e ativo intangível.", "Passivo de terceiros e passivo de sócios, apenas."],
        0,
        ASSUNTO,
        "Correto o item A. O art. 178, §2º, classifica o passivo em passivo circulante, passivo não circulante e patrimônio líquido — pela Lei das S/A, o PL fica formalmente DENTRO do passivo, como uma obrigação da empresa junto aos sócios (teoria da propriedade), mesmo sendo, contabilmente, uma obrigação NÃO EXIGÍVEL, diferente das dívidas exigíveis com terceiros."
    ),
    (
        "Para o Direito, o patrimônio é definido como:",
        ["O complexo de direitos e obrigações pecuniariamente apreciáveis inerentes a uma pessoa — uma universalidade de direitos e obrigações.", "Exclusivamente os bens tangíveis de uma pessoa, excluindo direitos e obrigações.", "O mesmo conceito contábil de patrimônio, sem qualquer distinção de enfoque.", "Apenas o ativo circulante de uma pessoa jurídica.", "A soma do capital social e das reservas de lucro de uma companhia."],
        0,
        ASSUNTO,
        "Correto o item A. Para o Direito, patrimônio é a representação econômica da pessoa, com natureza jurídica de universalidade de direitos e obrigações — o complexo de direitos e obrigações pecuniariamente apreciáveis inerentes a uma pessoa. A Contabilidade, por sua vez, estuda o patrimônio em seus aspectos quantitativos (valores) e qualitativos (composição) — um enfoque diferente do jurídico, ainda que o objeto seja o mesmo."
    ),
    (
        "Assinale a alternativa correta sobre a relação entre os conceitos de patrimônio e capital:",
        ["Patrimônio é formado pelo ativo e passivo da entidade; capital é a origem do patrimônio — o capital de terceiros forma o passivo e o capital próprio forma o patrimônio líquido.", "Capital é constituído pelo patrimônio líquido, e patrimônio é formado apenas pelo ativo total das entidades.", "Patrimônio e capital são sinônimos perfeitos, intercambiáveis em qualquer contexto contábil.", "Capital é sempre maior que o patrimônio, pois inclui ativos que ainda não foram incorporados à entidade.", "Patrimônio é exclusivamente o capital próprio da entidade, sem relação com o capital de terceiros."],
        0,
        ASSUNTO,
        "Correto o item A. Patrimônio é o conjunto dos bens, direitos e obrigações (formado pelo ativo e pelo passivo); capital é a origem do patrimônio — alguém aplicou seu capital para que o patrimônio existisse. O capital total aplicado (ativo/patrimônio bruto) é originado pelo capital de terceiros (passivo) e pelo capital próprio (patrimônio líquido)."
    ),
    (
        "De acordo com a Resolução CFC nº 774, de 16 de dezembro de 1994, do Conselho Federal de Contabilidade, o objeto de estudo da contabilidade, em seus aspectos qualitativos e quantitativos, denomina-se:",
        ["Aziendas.", "Patrimônio Líquido.", "Controle do Patrimônio.", "Ação Administrativa.", "Patrimônio."],
        4,
        ASSUNTO,
        "Correto o item E. Segundo a Resolução CFC nº 774/1994, na Contabilidade o objeto é sempre o PATRIMÔNIO de uma Entidade, definido como um conjunto de bens, direitos e de obrigações para com terceiros, pertencente a uma pessoa física, a um conjunto de pessoas (sociedades informais) ou a uma sociedade/instituição de qualquer natureza, com ou sem fins lucrativos."
    ),
    (
        "De acordo com Max Weber, a moderna organização racional da empresa capitalista foi viabilizada pela contabilidade racional. Esse pensamento foi corroborado, na ciência contábil, por Vicenzo Masi, que identificou como objeto da contabilidade:",
        ["as contas.", "a azienda.", "os réditos.", "o patrimônio.", "o lucro."],
        3,
        ASSUNTO,
        "Correto o item D. Vicenzo Masi foi o criador da teoria patrimonialista, que divide as contas em patrimoniais e de resultado; segundo essa teoria, o objeto da contabilidade é o PATRIMÔNIO, o objetivo é fornecer informações, e a finalidade é controlar o patrimônio e sua evolução."
    ),
    (
        "Segundo o conceito de Patrimônio do Conselho Federal de Contabilidade, um bem 'onerado' é aquele que:",
        ["Pode ser dado como garantia ou exige um pagamento.", "Possui corpo, matéria (é tangível).", "Foi recebido como doação.", "Não pode ser utilizado como garantia e não exige pagamento.", "É incorpóreo, sem existência física."],
        0,
        ASSUNTO,
        "Correto o item A. Onerados são os bens e direitos que podem ser dados como garantia ou exigem um pagamento; o oposto — não onerados — são os que não podem ser usados como garantia nem exigem pagamento."
    ),
    (
        "No conceito de Patrimônio do CFC, bens e direitos 'formados' são aqueles que:",
        ["Foram comprados, à vista ou a prazo.", "Foram criados pela própria empresa (ex.: uma marca desenvolvida internamente).", "São bens industrializados, resultantes da transformação de insumos em produto.", "Foram recebidos como doação.", "Estão sob o domínio da empresa em regime de usufruto."],
        1,
        ASSUNTO,
        "Correto o item B. 'Formados' são os bens e direitos criados pela própria empresa, como uma marca. 'Adquiridos' são os comprados (item A); 'produzidos' são os industrializados (item C); 'recebidos' vêm de doação (item D); 'mantidos' estão sob domínio/usufruto da empresa (item E)."
    ),
    (
        "Na contabilidade, os 'Direitos' representam:",
        ["Os recursos que a empresa tem a receber ou a recuperar junto a terceiros — seus créditos (ex.: duplicatas a receber, impostos a recuperar).", "As dívidas da empresa junto a terceiros ou sócios.", "Os bens tangíveis de propriedade da empresa.", "O patrimônio líquido da empresa.", "A soma de todos os ativos e passivos da empresa."],
        0,
        ASSUNTO,
        "Correto o item A. Direitos são os recursos que a empresa tem a receber ou a recuperar junto a terceiros, representando seus créditos — só existe direito porque alguém deve algo à empresa."
    ),
    (
        "Na contabilidade, as 'Obrigações' representam:",
        ["Os créditos que a empresa tem a receber de terceiros.", "As dívidas e valores que a empresa deve pagar a terceiros ou aos sócios — um exigível.", "Os bens intangíveis da empresa.", "O conjunto de bens tangíveis e intangíveis da empresa.", "O valor de mercado das ações da empresa."],
        1,
        ASSUNTO,
        "Correto o item B. Obrigações representam as dívidas, os valores que devem ser pagos pela empresa junto a terceiros ou aos sócios — representam os débitos, um exigível, aquilo que a empresa terá de pagar para alguém."
    ),
    (
        "A contabilidade é uma ciência social que se caracteriza por estudar objetos, fenômenos e atos decorrentes de ações humanas (fatos contábeis), que afetam diretamente o respectivo objeto de estudo, que é o(a):",
        ["patrimônio de uma pessoa física ou jurídica.", "produtividade dos insumos utilizados no processo de produção.", "eficiência na alocação de recursos de uma sociedade de qualquer natureza.", "resultado financeiro de qualquer tipo de sociedade em determinado período.", "eficácia da gestão de recursos financeiros, humanos e tecnológicos de uma organização."],
        0,
        ASSUNTO,
        "Correto o item A. O objeto de estudo da Contabilidade é o patrimônio de qualquer pessoa, seja física ou jurídica."
    ),
    (
        "Os registros de operações realizadas em uma empresa têm o objetivo de gerar informações úteis para a gestão organizacional. Embora seja fornecida uma diversidade de informações nos relatórios contábeis, o objeto da contabilidade é o:",
        ["controle de receitas e despesas.", "fluxo de caixa das entidades.", "lucro das entidades.", "patrimônio das entidades.", "valor de mercado das entidades."],
        3,
        ASSUNTO,
        "Correto o item D. O objeto da contabilidade é o PATRIMÔNIO das entidades; o objetivo é o fornecimento de informações úteis — não confundir objeto com objetivo."
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
            "disc": "Contabilidade Geral",
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
