# -*- coding: utf-8 -*-
"""
Primeiro conteudo de Contabilidade Geral do app (PC-PE) -- a partir do PDF
"Conceitos da Contabilidade" (Focus Concursos), que cobre o item 1
("Conceitos, objetivos e finalidades da contabilidade") do
PROGRAMA_PCPE_AGENTE oficial.

As mudancas estruturais em app-template.html ja foram feitas via Edit antes
deste script rodar: criacao do const TEORIA_CONTABILIDADE_PCPE (conceito
oficial de 1924, conceito atual de Hilario Franco, conceitos correlatos --
escrituracao/contabilista/contabilizar/digrafia --, distincao contabilidade
x escrituracao, classificacao como ciencia social aplicada, metodologia
racional, objeto/objetivo/finalidade/campo de aplicacao/principio basico, e
a influencia norte-americana na Lei 6.404/1976), e registro do deck em
TEORIA_DECKS / TEORIA_DECK_TO_DISC com o disc "Contabilidade Geral".

O PDF trazia uma "Maratona de Questoes" com 19 itens numerados, misturando
Certo/Errado (itens 1 a 10) e multipla escolha (itens 11 a 19), todos com
gabarito e comentario prontos. Como o PC-PE so usa multipla escolha:
- Os 9 itens de MC (11 a 19) foram aproveitados quase que diretamente;
  3 deles (12, 15, 16) so traziam 4 alternativas no PDF, entao foi
  acrescentada uma 5a alternativa (distrator claramente incorreto) so pra
  manter o schema de 5 alternativas do app -- sem alterar a logica nem o
  gabarito original.
- Os 10 itens de Certo/Errado (1 a 10) nao foram convertidos um a um de
  forma mecanica: tres deles (3, 4 e 6) testavam exatamente o mesmo fato
  ("contabilidade nao e ciencia exata, e social aplicada"), entao foram
  consolidados em menos questoes originais de multipla escolha, usando o
  espaco liberado pra cobrir fatos do PDF que ainda nao tinham questao
  nenhuma (os conceitos correlatos -- escrituracao/contabilista/
  contabilizar/digrafia --, a distincao contabilidade x escrituracao, e os
  5 elementos objeto/objetivo/finalidade/campo de aplicacao/principio
  basico, que o PDF so trazia no texto corrido).

Este script cuida so de: (1) acrescentar as questoes a questions.json,
(2) regenerar estudo-cebraspe-ma.html a partir do app-template.html ja
editado.
"""
import json

MC_QUESTIONS = [
    # ---- originais, a partir dos fatos testados pelos itens Certo/Errado 1-10 ----
    (
        "Quanto à área de conhecimento, a Contabilidade é classificada, pela doutrina majoritária, como:",
        ["Ciência Humana.", "Ciência Social Aplicada.", "Ciência Exata.", "Ciência Biológica.", "Ciência Formal."],
        1,
        "1 — Contabilidade Geral: Conceitos da Contabilidade",
        "Correto o item B. A Contabilidade é ciência social aplicada: social porque envolve relacionamento entre pessoas (na contabilidade, as contas contábeis representam essas pessoas/entidades dentro de uma sociedade); aplicada porque seu conhecimento é voltado à prática. Não é ciência humana nem exata."
    ),
    (
        "Segundo o entendimento consolidado sobre o objeto de estudo da Contabilidade, assinale a alternativa correta:",
        ["A Contabilidade estuda, interpreta e registra as variações expressas na equação fundamental do patrimônio que afetam a situação líquida patrimonial.", "A Contabilidade estuda exclusivamente as variações do passivo que não afetam a situação líquida.", "A Contabilidade não possui a equação fundamental do patrimônio como objeto de análise.", "A Contabilidade estuda apenas as variações patrimoniais quantitativas, nunca as qualitativas.", "A Contabilidade estuda a equação fundamental do patrimônio apenas em entidades sem fins lucrativos."],
        0,
        "1 — Contabilidade Geral: Conceitos da Contabilidade",
        "Correto o item A. A Contabilidade, como ciência, estuda as variações patrimoniais que afetam a situação líquida — leitura consolidada em cima da equação fundamental do patrimônio (Ativo = Passivo + Patrimônio Líquido)."
    ),
    (
        "São as três condições da metodologia racional por meio da qual a Contabilidade, como ciência social, trata do patrimônio:",
        ["Generalidade, certeza e busca das causas.", "Objetividade, neutralidade e comparabilidade.", "Relevância, materialidade e tempestividade.", "Uniformidade, consistência e prudência.", "Legalidade, moralidade e eficiência."],
        0,
        "1 — Contabilidade Geral: Conceitos da Contabilidade",
        "Correto o item A. A Contabilidade trata do patrimônio por meio de conhecimentos obtidos por metodologia racional, com as condições de Generalidade (vale para qualquer patrimônio e qualquer pessoa, sem usuário específico), Certeza (informação fidedigna e factual, embasada em fatos ocorridos) e Busca das causas (todo fato deve ser comprovado por documento que lhe deu origem)."
    ),
    (
        "Na ciência contábil, a 'finalidade' corresponde a:",
        ["O patrimônio das entidades.", "Fornecer informações úteis.", "Controlar o patrimônio das entidades.", "Qualquer pessoa física ou jurídica.", "As partidas dobradas."],
        2,
        "1 — Contabilidade Geral: Conceitos da Contabilidade",
        "Correto o item C. Objeto = patrimônio das entidades; Objetivo = fornecer informações úteis; Finalidade = controlar o patrimônio das entidades; Campo de aplicação = qualquer pessoa física ou jurídica; Princípio básico = partidas dobradas. A pegadinha clássica é trocar 'objetivo' por 'finalidade' — são conceitos distintos nessa classificação."
    ),
    (
        "Na ciência contábil, o 'objetivo' corresponde a:",
        ["O patrimônio das entidades.", "Fornecer informações úteis.", "Controlar o patrimônio das entidades.", "Qualquer pessoa física ou jurídica.", "As partidas dobradas."],
        1,
        "1 — Contabilidade Geral: Conceitos da Contabilidade",
        "Correto o item B. Objeto = patrimônio das entidades; Objetivo = fornecer informações úteis (B, correto); Finalidade = controlar o patrimônio das entidades; Campo de aplicação = qualquer pessoa física ou jurídica; Princípio básico = partidas dobradas. Cuidado para não trocar 'objetivo' por 'finalidade'."
    ),
    (
        "Assinale a alternativa que expressa corretamente a diferença entre a Contabilidade (como ciência) e a Escrituração:",
        ["Não há diferença: Contabilidade e Escrituração são sinônimos.", "A Escrituração é um meio técnico e disciplinado para registrar e evidenciar a movimentação dos fatos patrimoniais, enquanto a ciência contábil se ocupa da explicação do fenômeno patrimonial, com lastro em teorias e conceitos.", "A Escrituração é mais abrangente que a ciência contábil, pois engloba toda a Contabilidade.", "A ciência contábil só existe depois de finalizada a Escrituração de um exercício social.", "A Escrituração é exclusiva do setor público; a ciência contábil, do setor privado."],
        1,
        "1 — Contabilidade Geral: Conceitos da Contabilidade",
        "Correto o item B. A Escrituração é um meio técnico e disciplinado para registrar a movimentação dos fatos patrimoniais e evidenciá-los; já a ciência contábil se ocupa do fenômeno patrimonial e da explicação do que ocorre com o patrimônio em suas transformações, com lastro em teorias, teoremas e um conjunto de conceitos."
    ),
    (
        "No I Congresso Brasileiro de Contabilistas (1924) e nos conceitos a ele associados, 'Digrafia' significa:",
        ["O registro metódico dos fatos administrativos de ordem econômica.", "O profissional versado nos estudos de Contabilidade.", "Organizar o patrimônio e as informações de acordo com as normas contábeis.", "Afirmar que a escrituração dos fatos será feita por partidas dobradas.", "A ciência social que estuda as funções de orientação, controle e registro."],
        3,
        "1 — Contabilidade Geral: Conceitos da Contabilidade",
        "Correto o item D. Escrituração = registro metódico dos fatos administrativos de ordem econômica (item A). Contabilista = profissional versado em Contabilidade (item B). Contabilizar = organizar o patrimônio conforme as normas contábeis (item C). Digrafia = afirmar que a escrituração será feita por partidas dobradas (item D, correto). O item E descreve o próprio conceito de Contabilidade."
    ),
    (
        "Quanto à definição atual de Contabilidade como 'ciência do patrimônio', assinale a alternativa correta sobre o seu objetivo:",
        ["Captar os elementos sensíveis, perceptíveis e habituais de transações que afetem a riqueza das organizações.", "Fornecer informações úteis aos usuários internos e externos sobre o patrimônio.", "Arrecadar tributos em nome do Estado sobre as variações patrimoniais.", "Avaliar exclusivamente o desempenho individual dos funcionários da entidade.", "Substituir integralmente a função do controle interno das organizações."],
        1,
        "1 — Contabilidade Geral: Conceitos da Contabilidade",
        "Correto o item B. A Contabilidade pode, sim, ser definida como a ciência do patrimônio (seu objeto), mas seu OBJETIVO é fornecer informações úteis aos usuários — e não 'captar elementos sensíveis, perceptíveis e habituais de transações', formulação que a banca considerou incorreta."
    ),
    (
        "Assinale a alternativa que apresenta uma afirmação CORRETA sobre a Contabilidade:",
        ["Os princípios contábeis relacionam-se à Contabilidade como ciência do patrimônio, destacando que o patrimônio é o objeto da Contabilidade.", "Os princípios contábeis aplicam-se apenas às entidades sem fins lucrativos.", "A Contabilidade, por ser uma ciência do patrimônio, não necessita de princípios para sua sistematização.", "Os princípios contábeis substituem a necessidade de normas emitidas pelo Comitê de Pronunciamentos Contábeis (CPC).", "Os princípios contábeis só se aplicam a partir da vigência da Lei nº 6.404/1976."],
        0,
        "1 — Contabilidade Geral: Conceitos da Contabilidade",
        "Correto o item A. A Contabilidade é ciência social aplicada que tem como objeto o patrimônio de qualquer pessoa, podendo ser denominada ciência do patrimônio. Os princípios contábeis dão arcabouço científico à Contabilidade, destacando justamente que o patrimônio é o seu objeto."
    ),
    (
        "Segundo um enfoque amplamente aceito na literatura contábil, a Contabilidade consiste em:",
        ["Um sistema de informações financeiras destinado a identificar, registrar e comunicar os eventos econômicos de uma organização.", "Um sistema de controle de estoques destinado exclusivamente a entidades comerciais.", "Um conjunto de normas tributárias voltado à arrecadação de impostos.", "Uma técnica de auditoria destinada a fiscalizar atos de gestores públicos.", "Um ramo do Direito Administrativo voltado ao controle do patrimônio público."],
        0,
        "1 — Contabilidade Geral: Conceitos da Contabilidade",
        "Correto o item A. Esse enfoque está alinhado ao conceito atual de Contabilidade como ciência social que estuda, controla e interpreta os fatos ocorridos no patrimônio das entidades — o controle contábil é feito por meio de um sistema de informações diretamente relacionado ao controle interno da entidade e a seu processo contábil."
    ),
    # ---- transcritas/adaptadas das questoes de multipla escolha prontas 11-19 ----
    (
        "A contabilidade está ligada à administração, ao direito e à economia, desempenhando função administrativa e econômica ao manter controle sobre o patrimônio da organização e apurando os respectivos resultados econômicos. Considerando essa informação, é correto afirmar que a contabilidade:",
        ["é um sistema de informação e avaliação que fornece demonstrações e análises de natureza econômica, financeira, física e de produtividade, com relação à entidade objeto de contabilização.", "estuda o passivo à disposição das aziendas, em seus aspectos estáticos e em suas variações, para enunciar, por meio de fórmulas racionalmente deduzidas, os efeitos da administração sobre a formação e a distribuição dos créditos.", "é uma ciência que permite manter um controle permanente do passivo da empresa, usando técnicas de cunho financeiro e fiscal.", "sobrepõe-se, como ciência, à administração e ao direito, pois não há como administrar sem números e sem referência contábil e financeira.", "é uma ciência concebida para coletar, registrar, resumir e interpretar dados e fenômenos que afetam as situações administrativas de uma organização."],
        0,
        "1 — Contabilidade Geral: Conceitos da Contabilidade",
        "Correto o item A. A contabilidade é a ciência social que estuda, controla e interpreta os fatos ocorridos no patrimônio das entidades, mediante o registro, a demonstração e a divulgação desses fatos, com o fim de oferecer informações sobre a composição do patrimônio, suas variações e o resultado econômico decorrente da gestão da riqueza patrimonial aos usuários — para isso, a entidade precisa de um sistema de controle interno que capture e trate as informações, apresentando-as por meio de relatórios e demonstrações."
    ),
    (
        "Como ramo do conhecimento, a Contabilidade deve ser classificada dentre:",
        ["As Ciências Exatas.", "As Ciências Humanas.", "As Ciências Patrimoniais.", "As Ciências Sociais.", "As Ciências Biológicas."],
        3,
        "1 — Contabilidade Geral: Conceitos da Contabilidade",
        "Correto o item D. A contabilidade é uma ciência social que trata dos relacionamentos, por meio de débitos e créditos, das contas."
    ),
    (
        "Existe um conceito oficial de contabilidade formulado no Primeiro Congresso Brasileiro de Contabilidade. Assinale a opção que corrobora com esse conceito oficial.",
        ["Contabilidade é uma ciência aplicada que estuda e pratica as funções de orientação, de controle e de registro relativas à Administração Econômica.", "Contabilidade estuda o patrimônio do ponto de vista econômico e financeiro, observando seus aspectos quantitativo e específico e as variações por ele sofridas.", "Contabilidade é a ciência que controla o patrimônio das empresas, mediante registro, demonstração expositiva, confirmação, análise e interpretação dos fatos nele ocorridos.", "Contabilidade é a técnica especial concebida para registrar, reunir e interpretar os fenômenos que afetam as situações patrimoniais, financeiras e econômicas de qualquer empresa.", "Contabilidade é a técnica de registrar todas as transações de uma companhia, que possam ser expressas em termos monetários, e de informar os reflexos dessas transações na situação dessa companhia."],
        0,
        "1 — Contabilidade Geral: Conceitos da Contabilidade",
        "Correto o item A. O primeiro Congresso Brasileiro de Contabilistas (Rio de Janeiro, agosto de 1924) estabeleceu que Contabilidade é 'a ciência social que estuda a prática e as funções de orientação, de controle e de registro, relativos aos atos e aos fatos de administração econômica' — redação mais próxima da alternativa A; as demais trocam 'ciência social' por 'técnica' ou mudam o objeto para 'patrimônio' em vez de 'administração econômica'."
    ),
    (
        "Muitas são as definições de Contabilidade apresentadas pelos autores contábeis, variando, ligeiramente, de acordo com sua corrente doutrinária. Entretanto, todos os conceitos, de uma forma ou de outra, convergem para a definição cunhada no I Congresso Brasileiro de Contabilidade. Nesse Congresso, a Contabilidade foi definida como sendo a ciência que, em relação aos atos e fatos da administração econômica, pratica as funções de:",
        ["anotação, mensuração e contagem.", "comprovação, verificação e acompanhamento.", "informação, medição e evidenciação.", "levantamento, marcação e apropriação.", "orientação, controle e registro."],
        4,
        "1 — Contabilidade Geral: Conceitos da Contabilidade",
        "Correto o item E. O primeiro Congresso Brasileiro de Contabilistas (1924) estabeleceu que a Contabilidade é a ciência social que estuda a prática e as funções de ORIENTAÇÃO, de CONTROLE e de REGISTRO, relativos aos atos e aos fatos de administração econômica."
    ),
    (
        "Em 16 de agosto de 1924, foi aprovado o Regulamento do Congresso que teve como objetivo estudar e regularizar todos os assuntos relacionados a contabilidade. Sabendo que, neste Congresso, foram delimitadas definições para a contabilidade, qual o conceito CORRETO de contabilidade:",
        ["Contabilidade: é a metodologia que estuda a prática e as funções de orientação, de controle e de registro, relativos aos atos e aos fatos de administração econômica.", "Contabilidade: é o registro metódico dos fatos administrativos de ordem econômica.", "Contabilidade: é a ciência que estuda e executa fatos administrativos de ordem econômica.", "Contabilidade: é a ciência que estuda a prática e as funções de orientação, de controle e de registro, relativos aos atos e aos fatos de administração econômica.", "Contabilidade: é a técnica que estuda e disciplina os fatos administrativos de ordem econômica."],
        3,
        "1 — Contabilidade Geral: Conceitos da Contabilidade",
        "Correto o item D. O primeiro Congresso Brasileiro de Contabilistas (1924) estabeleceu que Contabilidade é 'a ciência social que estuda a prática e as funções de orientação, de controle e de registro, relativos aos atos e aos fatos de administração econômica'. O item B, de propósito, descreve o conceito de ESCRITURAÇÃO, não o de Contabilidade."
    ),
    (
        "A contabilidade foi definida no I Congresso Brasileiro de Contabilidade como: 'a ciência que estuda e pratica as funções de orientação, controle e registro relativo aos atos e fatos da administração econômica.' São objetivos da contabilidade, EXCETO:",
        ["Fornecer informações sobre a posição patrimonial e financeira, o desempenho e as mudanças na posição financeira da entidade.", "Auxiliar o maior número de usuários em suas avaliações e tomadas de decisão financeira.", "Apresentar os resultados da atuação da administração na gestão da entidade quanto aos recursos que lhe foram confiados.", "Auxiliar os acionistas a avaliar a produtividade de cada funcionário da empresa e o desempenho dos gerentes.", "Fornecer subsídios para a tomada de decisão de investidores e credores sobre a entidade."],
        3,
        "1 — Contabilidade Geral: Conceitos da Contabilidade",
        "Correto o item D, por ser o único que NÃO é objetivo da contabilidade. Conceitualmente, a contabilidade é uma ciência social que estuda, controla o patrimônio de qualquer pessoa a fim de fornecer informações a seus usuários — não se encaixa nesses objetivos auxiliar os acionistas a avaliar a produtividade individual de funcionários, isso foge do escopo da ciência contábil."
    ),
    (
        "Segundo a teoria contábil contemporânea, a contabilidade é mais adequadamente classificada como uma:",
        ["metodologia.", "técnica.", "arte.", "prática.", "ciência."],
        4,
        "1 — Contabilidade Geral: Conceitos da Contabilidade",
        "Correto o item E. Atualmente, a contabilidade é considerada uma ciência social aplicada, que tem por objeto o patrimônio de qualquer entidade."
    ),
    (
        "A inspiração para a Lei nº 6.404/1976, que representou uma transição no sistema contábil brasileiro e alinhou o país a um novo cenário que começou a se desenhar na década de 1950, foi:",
        ["alemã.", "italiana.", "francesa.", "norte-americana.", "portuguesa."],
        3,
        "1 — Contabilidade Geral: Conceitos da Contabilidade",
        "Correto o item D. No processo de evolução legal da contabilidade no Brasil, a Lei nº 6.404/1976 abarcou os ditames da escola norte-americana, que se afastou da escola italiana, mudando o objetivo da contabilidade para o fornecimento de informações, e não mais o mero controle patrimonial."
    ),
    (
        "Assinale a alternativa que define corretamente a Contabilidade.",
        ["É uma ciência que se desenvolve com o objetivo de controlar o caixa de uma entidade financeira. São entidades financeiras todas aquelas que possuam uma conta caixa.", "É uma ciência que define na empresa um sistema de informações contábil que tem por objetivo subsidiar a tomada de decisões sobre entidades econômicas. São entidades econômicas pessoas físicas ou jurídicas que tomem decisões sobre recursos econômicos.", "Corresponde ao registro dos itens do ativo e do passivo que tenham ou não valor econômico. O valor econômico de um ativo é definido como sendo o seu custo histórico de aquisição.", "É uma ciência exata que permite mensurar objetivamente o patrimônio líquido das entidades econômicas. O patrimônio líquido corresponde à diferença entre os grupos ativo intangível e passivo intangível.", "É uma ciência histórica que tem por finalidade a evidenciação das operações de uma entidade com o objetivo principal de possibilitar ao estado o exercício da tributação e a cobrança do cumprimento das obrigações acessórias."],
        1,
        "1 — Contabilidade Geral: Conceitos da Contabilidade",
        "Correto o item B. A contabilidade é uma ciência social que estuda, controla e interpreta os fatos ocorridos no patrimônio das entidades, oferecendo informações sobre sua composição, variações e resultado econômico — ela se utiliza de um sistema de informações para subsidiar a tomada de decisão de usuários (pessoas físicas ou jurídicas) sobre recursos econômicos."
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
