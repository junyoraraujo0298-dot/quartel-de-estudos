# -*- coding: utf-8 -*-
"""
Terceiro conteudo de Contabilidade Geral do app (PC-PE) -- a partir de um
infografico "Introducao a Contabilidade" (QConcursos) enviado pelo usuario.
O infografico resume tudo que ja estava no app (ciencia social aplicada,
objeto = patrimonio) e traz 3 pontos genuinamente novos, ainda nao cobertos:
o PRINCIPIO DA ENTIDADE (patrimonio autonomo, distinto do patrimonio dos
socios), os USUARIOS da informacao contabil (internos x externos) e as 4
TECNICAS/etapas do processo contabil (escrituracao, demonstracoes
contabeis, analise das demonstracoes, auditoria).

A mudanca estrutural em app-template.html ja foi feita via Edit antes deste
script rodar: foi acrescentada uma nova secao "Principio da Entidade,
Usuarios e Tecnicas Contabeis" ao const TEORIA_CONTABILIDADE_PCPE ja
existente (mesma materia, nao um deck novo).

Como o infografico e um resumo visual, sem questoes prontas (nao e um PDF
FOCADO com Maratona de Questoes), as 10 questoes abaixo foram escritas
originalmente, cobrindo cada um dos 3 pontos novos (principio da entidade,
usuarios internos/externos, e as 4 tecnicas contabeis na ordem correta e
uma por uma).

Este script cuida so de: (1) acrescentar as questoes a questions.json,
(2) regenerar estudo-cebraspe-ma.html a partir do app-template.html ja
editado.
"""
import json

ASSUNTO = "1 — Contabilidade Geral: Princípio da Entidade, Usuários e Técnicas Contábeis"

MC_QUESTIONS = [
    (
        "O patrimônio estudado pela Contabilidade deve ser, necessariamente:",
        ["Autônomo, distinto do patrimônio de seus sócios ou proprietários, ainda que pertença a uma pessoa física.", "Pertencente exclusivamente a uma pessoa jurídica com fins lucrativos.", "Confundido com o patrimônio pessoal dos sócios, para fins de simplificação contábil.", "De propriedade exclusiva do Estado, quando se tratar de entidade com fins sociais.", "Vinculado apenas a sociedades anônimas de capital aberto."],
        0,
        ASSUNTO,
        "Correto o item A. Pelo princípio da entidade (autonomia patrimonial), o patrimônio estudado pela Contabilidade é autônomo, distinto do patrimônio de seus sócios, proprietários ou administradores — pode pertencer a pessoa física ou jurídica, com ou sem fins lucrativos."
    ),
    (
        "Os usuários da informação contábil classificam-se, quanto à sua relação com a entidade, em:",
        ["Primários e secundários.", "Internos e externos.", "Diretos e indiretos.", "Societários e não societários.", "Patrimoniais e extrapatrimoniais."],
        1,
        ASSUNTO,
        "Correto o item B. Os usuários da informação contábil dividem-se em internos (a administração/gestores da entidade) e externos (investidores, credores, empregados e o Governo)."
    ),
    (
        "São exemplos de usuários INTERNOS da informação contábil:",
        ["Investidores e acionistas minoritários.", "Credores e instituições financeiras.", "A administração/gestores da entidade, que utilizam a informação para planejamento, controle e tomada de decisão.", "O Governo, por meio da fiscalização tributária.", "Empregados que não ocupam cargo de gestão."],
        2,
        ASSUNTO,
        "Correto o item C. Os usuários internos são a administração/gestores da entidade, que usam a informação contábil para planejamento, controle e apoio ao processo decisório. Investidores, credores, empregados e o Governo são usuários EXTERNOS."
    ),
    (
        "São exemplos de usuários EXTERNOS da informação contábil, EXCETO:",
        ["Investidores.", "Credores.", "Empregados.", "Governo.", "A administração da própria entidade."],
        4,
        ASSUNTO,
        "Correto o item E, por ser o único usuário INTERNO da lista. Investidores, credores, empregados e o Governo são usuários externos da informação contábil; a administração/gestores da entidade são usuários internos."
    ),
    (
        "A finalidade da Contabilidade é:",
        ["Controlar o patrimônio e apoiar o planejamento, o controle e o processo decisório.", "Arrecadar tributos em nome do Estado.", "Fiscalizar exclusivamente as obrigações trabalhistas da entidade.", "Substituir a função do controle interno da entidade.", "Avaliar o desempenho individual de cada funcionário da entidade."],
        0,
        ASSUNTO,
        "Correto o item A. A finalidade da Contabilidade é controlar o patrimônio das entidades e apoiar o planejamento, o controle e o processo decisório — tanto dos usuários internos quanto dos externos."
    ),
    (
        "São técnicas (etapas) do processo contábil, na ordem lógica de execução:",
        ["Auditoria, Análise das Demonstrações, Demonstrações Contábeis e Escrituração.", "Escrituração, Demonstrações Contábeis, Análise das Demonstrações e Auditoria.", "Demonstrações Contábeis, Escrituração, Auditoria e Análise das Demonstrações.", "Análise das Demonstrações, Auditoria, Escrituração e Demonstrações Contábeis.", "Escrituração, Auditoria, Demonstrações Contábeis e Análise das Demonstrações."],
        1,
        ASSUNTO,
        "Correto o item B. A ordem lógica do processo contábil é: Escrituração (registro dos fatos) → Demonstrações Contábeis (relatórios a partir do registrado) → Análise das Demonstrações (avaliação da situação patrimonial/econômica/financeira) → Auditoria (verificação da adequação e veracidade das informações)."
    ),
    (
        "A técnica contábil que registra os fatos contábeis em livros próprios, como o Diário e o Razão, denomina-se:",
        ["Escrituração.", "Demonstração Contábil.", "Análise das Demonstrações.", "Auditoria.", "Contabilização societária."],
        0,
        ASSUNTO,
        "Correto o item A. A Escrituração é a técnica que registra, de forma metódica, os fatos contábeis em livros próprios, como o Diário e o Razão — é a primeira etapa do processo contábil."
    ),
    (
        "Os relatórios periódicos que reúnem as informações da entidade, elaborados a partir dos registros da escrituração, denominam-se:",
        ["Escrituração.", "Demonstrações Contábeis.", "Pareceres de Auditoria.", "Plano de Contas.", "Balancete de Verificação Preliminar."],
        1,
        ASSUNTO,
        "Correto o item B. As Demonstrações Contábeis são os relatórios periódicos elaborados a partir da escrituração, reunindo as informações patrimoniais, econômicas e financeiras da entidade."
    ),
    (
        "A técnica contábil que avalia a situação patrimonial, econômica e financeira de uma entidade, a partir de suas demonstrações contábeis, denomina-se:",
        ["Escrituração.", "Auditoria.", "Análise das Demonstrações Contábeis.", "Perícia Contábil.", "Consolidação de Balanços."],
        2,
        ASSUNTO,
        "Correto o item C. A Análise das Demonstrações Contábeis é a técnica que avalia a situação patrimonial, econômica e financeira da entidade, a partir das demonstrações já elaboradas — a etapa seguinte à elaboração dos relatórios."
    ),
    (
        "A técnica contábil que verifica a adequação e a veracidade das informações contábeis denomina-se:",
        ["Escrituração.", "Demonstração Contábil.", "Análise das Demonstrações.", "Auditoria.", "Perícia Patrimonial."],
        3,
        ASSUNTO,
        "Correto o item D. A Auditoria verifica a adequação e a veracidade das informações contábeis — é a última das quatro técnicas do processo contábil (escrituração, demonstrações contábeis, análise das demonstrações e auditoria)."
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
