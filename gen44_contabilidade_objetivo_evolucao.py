# -*- coding: utf-8 -*-
"""
Quarto conteudo de Contabilidade Geral do app (PC-PE) -- a partir do PDF
"Objetivo da contabilidade" (Prof. Claudio Zorzo, Tema 1 - aula 3), que
aprofunda o item 1 ("Conceitos, objetivos e finalidades da contabilidade")
do PROGRAMA_PCPE_AGENTE oficial com a evolucao historica do conceito.

A mudanca estrutural em app-template.html ja foi feita via Edit antes deste
script rodar: foi acrescentada uma nova secao "Objetivo da Contabilidade -
Evolucao Historica" ao const TEORIA_CONTABILIDADE_PCPE ja existente (mesma
materia, nao um deck novo): a linha do tempo das normas (Decreto-Lei
2.627/1940, Lei 6.404/1976, Lei 11.638/07, Lei 11.941/09); a escola
italiana (objetivo=controlar, finalidade=informar); a escola americana,
que INVERTE objetivo e finalidade (objetivo=informar, finalidade=
controlar) e divide a contabilidade em Financeira (usuarios externos) e
Gerencial (usuarios internos); a escola internacional do IASB (Lei
11.638/07), que acrescenta a "primazia da essencia economica sobre a
forma juridica"; a Resolucao CFC 774/94 (objetivo cientifico x
pragmatico); e o objetivo atual consolidado (informacao economica,
financeira, OPERACIONAL e SOCIAL).

O PDF trazia 10 questoes reais de banca (Quadrix, CESPE, VUNESP, FGV),
misturando Certo/Errado (itens 1 a 5) e multipla escolha (itens 6 a 10,
uma delas -- item 8, CESPE/APEX/2024 -- com so 4 alternativas no
original, recebendo uma 5a soh pra manter o schema do app, sem mudar o
gabarito). As citacoes de banca/orgao/cargo/ano das questoes originais
foram preservadas no enunciado, entre parenteses, por serem questoes reais
e recentes (ha itens de 2023 e 2024) -- isso da credibilidade extra ao
material. Os 5 itens de Certo/Errado foram reescritos como questoes de
multipla escolha originais, mantendo o mesmo fato juridico/conceitual
testado e o mesmo gabarito da assertiva original.

Este script cuida so de: (1) acrescentar as questoes a questions.json,
(2) regenerar estudo-cebraspe-ma.html a partir do app-template.html ja
editado.
"""
import json

ASSUNTO = "1 — Contabilidade Geral: Objetivo da Contabilidade (evolução histórica)"

MC_QUESTIONS = [
    (
        "(QUADRIX/CREA-TO/Contador/2021 — adaptada) Assinale a alternativa correta sobre o alcance do objetivo da contabilidade:",
        ["O objetivo da contabilidade não se restringe a demonstrar o resultado operacional de uma entidade e a forma como foi obtido; a contabilidade tem por objetivo fornecer informações úteis sobre o patrimônio a usuários internos e externos.", "O objetivo da contabilidade restringe-se a demonstrar o resultado operacional de determinada entidade e a forma como esse resultado foi obtido.", "O objetivo da contabilidade restringe-se ao controle dos tributos devidos pela entidade.", "O objetivo da contabilidade restringe-se à elaboração do Balanço Patrimonial.", "O objetivo da contabilidade restringe-se à auditoria das demonstrações contábeis."],
        0,
        ASSUNTO,
        "Correto o item A. A banca considerou ERRADA a assertiva que restringia o objetivo da contabilidade a demonstrar apenas o resultado operacional e como ele foi obtido — o objetivo é mais amplo: fornecer informações úteis sobre o patrimônio da entidade a usuários internos e externos, para finalidades diversas."
    ),
    (
        "(CESPE/EBSERH/Técnico contábil/2018) Assinale a alternativa correta sobre o principal objetivo da contabilidade:",
        ["O principal objetivo da contabilidade é fornecer informações úteis sobre o patrimônio da entidade para finalidades diversas, entre as quais planejamento, controle e auxílio no processo decisório.", "O principal objetivo da contabilidade é exclusivamente calcular o lucro tributável da entidade.", "O principal objetivo da contabilidade é fiscalizar o cumprimento de obrigações trabalhistas.", "O principal objetivo da contabilidade é avaliar unicamente o desempenho dos gestores da entidade.", "O principal objetivo da contabilidade é elaborar o orçamento anual da entidade."],
        0,
        ASSUNTO,
        "Correto o item A — gabarito CERTO na prova original. O principal objetivo da contabilidade é fornecer informações úteis sobre o patrimônio da entidade para finalidades diversas: planejamento, controle e auxílio no processo decisório, tanto de usuários internos quanto externos."
    ),
    (
        "(CESPE/ANTT/Contador/2024 — adaptada) Se um trabalhador controla rigorosamente, em um caderno, todos os seus gastos e as suas rendas, e, com base nesse controle, decide o que lhe convém e o que não lhe convém fazer com seus recursos, então, agindo assim, ele:",
        ["Reafirma o objetivo fundamental da contabilidade, que é fornecer informações úteis para a tomada de decisão sobre o patrimônio.", "Não pratica contabilidade, pois a ciência contábil só se aplica a pessoas jurídicas.", "Pratica apenas escrituração, sem qualquer relação com o objetivo da contabilidade.", "Exerce atividade de auditoria, e não de contabilidade.", "Pratica controle tributário, não contábil."],
        0,
        ASSUNTO,
        "Correto o item A — gabarito CERTO na prova original. Mesmo sem ser um profissional contábil, ao controlar sistematicamente seu patrimônio (gastos e rendas) para decidir o que fazer com seus recursos, o trabalhador reafirma o objetivo fundamental da contabilidade: fornecer informações úteis para a tomada de decisão — o patrimônio é objeto da contabilidade de QUALQUER pessoa, física ou jurídica."
    ),
    (
        "(CESPE/CAU/Assistente técnico/2024) Assinale a alternativa correta sobre o papel da contabilidade no processo decisório:",
        ["A contabilidade estuda o patrimônio em seus aspectos quantitativo e qualitativo, fornecendo subsídios ao processo de tomada de decisões econômico-financeiras por usuários internos e externos.", "A contabilidade estuda o patrimônio apenas em seu aspecto quantitativo, sendo o aspecto qualitativo objeto exclusivo da administração.", "A contabilidade fornece subsídios à tomada de decisão apenas para usuários externos, já que usuários internos têm acesso direto à entidade.", "A contabilidade não fornece subsídios a decisões econômico-financeiras, apenas ao cumprimento de obrigações legais.", "A contabilidade estuda exclusivamente o aspecto qualitativo do patrimônio, delegando o quantitativo à área financeira."],
        0,
        ASSUNTO,
        "Correto o item A — gabarito CERTO na prova original. A contabilidade estuda o patrimônio em seus aspectos quantitativo (valores) e qualitativo (composição), fornecendo subsídios ao processo de tomada de decisões econômico-financeiras tanto a usuários internos quanto externos."
    ),
    (
        "(CESPE/PETROBRAS/Administração/2023) Assinale a alternativa correta sobre as finalidades da ciência contábil:",
        ["O fornecimento de informações úteis para a tomada de decisão pelos agentes econômicos é uma das finalidades da ciência contábil.", "O fornecimento de informações úteis para a tomada de decisão não é finalidade da ciência contábil, mas apenas de suas técnicas acessórias.", "A ciência contábil tem finalidade exclusivamente fiscal, voltada à apuração de tributos.", "A ciência contábil tem finalidade exclusivamente de controle interno, sem relação com a tomada de decisão de agentes econômicos.", "A ciência contábil não possui finalidade própria, apenas instrumentaliza decisões de outras ciências sociais."],
        0,
        ASSUNTO,
        "Correto o item A — gabarito CERTO na prova original. O fornecimento de informações úteis para a tomada de decisão pelos agentes econômicos é, de fato, uma das finalidades da ciência contábil."
    ),
    (
        "(CESPE/TRE-BA/Contador/2017) A contabilidade tem como principal objetivo a(o):",
        ["fornecimento de informações que proporcionem aos seus mais diversos usuários — seja internos, seja externos — utilidade no processo de tomada de decisões.", "elaboração de guias de recolhimento de tributos a fim de manter a entidade em conformidade com os ditames legais.", "elaboração de demonstrações contábeis que atendam às finalidades específicas de determinado grupo de usuários.", "avaliação da capacidade das entidades comerciais em arcar com suas obrigações financeiras.", "mensuração de bens patrimoniais a fim de elaborar corretamente as demonstrações contábeis."],
        0,
        ASSUNTO,
        "Correto o item A. O principal objetivo da contabilidade é fornecer informações que proporcionem utilidade, no processo de tomada de decisões, aos mais diversos usuários — internos e externos —, e não apenas servir a um grupo específico (item C) ou a finalidades estritamente tributárias (item B)."
    ),
    (
        "(VUNESP/IPSM/Contador/2018) Assinale, dentre as alternativas apresentadas a seguir, aquela que apresenta adequadamente o objetivo da Contabilidade.",
        ["A Contabilidade tem por objetivo o controle dos impostos a pagar.", "A Contabilidade tem por objetivo gerar informações para o controle dos estoques das indústrias.", "A Contabilidade tem por objetivo controlar as dívidas e os impostos a serem pagos.", "A Contabilidade tem por objetivo o controle das obrigações trabalhistas e tributárias.", "A Contabilidade tem por objetivo gerar informações para o apoio das decisões econômico-financeiras."],
        4,
        ASSUNTO,
        "Correto o item E. As alternativas A a D restringem indevidamente o objetivo da contabilidade a áreas específicas de controle (tributos, estoques, dívidas, obrigações trabalhistas); o objetivo correto e abrangente é gerar informações para apoiar as decisões econômico-financeiras dos usuários."
    ),
    (
        "(CESPE/APEX/Contador/2024) A ciência contábil tem múltiplas finalidades e ramos de atuação, mas, independentemente do enfoque, a contabilidade tem por objetivo fundamental:",
        ["registrar, estimar, organizar e sintetizar as informações geradas pelas sociedades.", "fornecer informações úteis aos usuários para a tomada de decisão.", "controlar o patrimônio do ente contábil.", "mensurar o resultado do empreendimento societário.", "elaborar exclusivamente o Balanço Patrimonial e a Demonstração do Resultado do Exercício."],
        1,
        ASSUNTO,
        "Correto o item B. Independentemente do enfoque ou ramo de atuação (financeira, gerencial, de custos, pública etc.), o objetivo fundamental da contabilidade é fornecer informações úteis aos usuários para a tomada de decisão — os demais itens descrevem técnicas, meios ou finalidades específicas, não o objetivo fundamental em si."
    ),
    (
        "(QUADRIX/PRODAM-AM/Contador/2022) A contabilidade é a ciência social que tem por objeto de estudo o patrimônio, o qual compreende o(s):",
        ["bens e direitos, tangíveis ou não, sob o controle da entidade.", "bens e direitos, deduzidas as obrigações.", "bens, os direitos e as obrigações de uma entidade.", "total das propriedades, monetárias ou não, de uma entidade.", "passivo exigível e o passivo não exigível."],
        2,
        ASSUNTO,
        "Correto o item C. O patrimônio compreende os bens, os direitos e as obrigações de uma entidade — não apenas bens e direitos (item A), nem a diferença entre eles (item B, que seria o Patrimônio Líquido), nem apenas o passivo (item E)."
    ),
    (
        "(FGV/TAUBATÉ-SP/Contador/2022) A Contabilidade pode ser segmentada em Contabilidade Financeira e Contabilidade Gerencial. Um objetivo da Contabilidade Gerencial é:",
        ["fornecer informações aos investidores.", "auxiliar a tomada de decisão dos gestores.", "elaborar a declaração do imposto de renda.", "evidenciar a saúde financeira da entidade ao público em geral.", "constituir a base de informação para elaboração das demonstrações contábeis pelos contadores."],
        1,
        ASSUNTO,
        "Correto o item B. A Contabilidade Gerencial volta-se aos usuários INTERNOS (gestores), auxiliando sua tomada de decisão por meio de relatórios gerenciais; já a Contabilidade Financeira volta-se aos usuários EXTERNOS (como investidores, item A), produzindo as demonstrações contábeis (item D)."
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
