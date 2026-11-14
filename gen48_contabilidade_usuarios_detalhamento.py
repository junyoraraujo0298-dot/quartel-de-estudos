# -*- coding: utf-8 -*-
"""
Sexto conteudo de Contabilidade Geral do app (PC-PE) -- a partir do PDF
"Usuarios da Contabilidade" (Focus Concursos), que aprofunda o item 1 do
edital (conceitos, objetivos e finalidades da contabilidade).

O app ja cobria a divisao basica internos x externos (gen43). Este PDF traz
fatos genuinamente novos, ainda nao cobertos: o conceito de usuario segundo
o CPC 00; a divisao dos usuarios EXTERNOS em primarios (investidores,
credores por emprestimo) e secundarios (fornecedores, clientes, governo,
sindicatos, sociedade); a pegadinha classica dos acionistas ORDINARIOS
(internos, com poder de voto) x PREFERENCIAIS (externos primarios, sem
poder de voto); o fato de o CONTADOR ser usuario interno (poder decisorio
tecnico na elaboracao das demonstracoes); e as necessidades especificas de
cada usuario externo (investidores, empregados, credores, fornecedores,
clientes, governo/agencias reguladoras, publico).

A mudanca estrutural em app-template.html ja foi feita via Edit antes deste
script rodar: a secao "Principio da Entidade, Usuarios e Tecnicas
Contabeis" do TEORIA_CONTABILIDADE_PCPE foi expandida com 6 novos itens
detalhando usuarios (substituindo o item unico anterior).

O PDF trazia uma Maratona de 20 questoes Certo/Errado, com bastante
repeticao da mesma ideia central (primarios x secundarios, quem e usuario
interno x externo). Essas repeticoes foram consolidadas em questoes
originais de multipla escolha, usando a capacidade liberada para cobrir os
fatos novos que o banco testava apenas de raspao (ex.: acionistas
ordinarios x preferenciais; contador como usuario interno; a pegadinha da
ANEEL como usuaria externa SECUNDARIA mesmo sendo agencia reguladora
especifica do setor).

Este script cuida so de: (1) acrescentar as questoes a questions.json,
(2) regenerar estudo-cebraspe-ma.html a partir do app-template.html ja
editado.
"""
import json

ASSUNTO = "1 — Contabilidade Geral: Usuários da Contabilidade (Detalhamento, CPC 00)"

MC_QUESTIONS = [
    (
        "Segundo o Pronunciamento Conceitual Básico (CPC 00), são usuários das informações contábeis:",
        ["Apenas os investidores do mercado de capitais.", "As pessoas físicas ou jurídicas com interesse na entidade, que utilizam as informações contábeis para seus próprios fins, de forma permanente ou transitória.", "Somente os administradores da própria entidade.", "Apenas os órgãos governamentais de fiscalização tributária.", "Apenas os sócios que integram o quadro societário da entidade."],
        1,
        ASSUNTO,
        "Correto o item B. O CPC 00 define como usuários as pessoas físicas ou jurídicas com interesse na entidade, que utilizam as informações contábeis para seus próprios fins, de forma permanente ou transitória — conceito amplo, que não se restringe a investidores, administradores ou órgãos fiscais isoladamente."
    ),
    (
        "Em relação ao acesso à informação contábil, é correto afirmar que os usuários internos:",
        ["Dependem exclusivamente da divulgação das demonstrações contábeis, assim como os externos.", "Têm acesso tempestivo às informações e podem solicitar a elaboração de relatórios específicos para suas próprias análises, não dependendo das demonstrações contábeis.", "Só podem obter informações após a publicação do relatório de auditoria.", "São sempre pessoas estranhas ao quadro de administração da entidade.", "Têm interesse apenas nos aspectos genéricos expressos nas demonstrações contábeis."],
        1,
        ASSUNTO,
        "Correto o item B. Os usuários internos (assembleia dos sócios, conselho de administração, presidente e gestores) têm facilidade de acesso às informações contábeis, obtendo-as de forma tempestiva e podendo solicitar relatórios específicos — ao contrário dos externos, que recebem a informação apenas pela divulgação das demonstrações contábeis."
    ),
    (
        "Quanto à classificação dos usuários externos da informação contábil, são considerados usuários externos PRIMÁRIOS:",
        ["Os fornecedores e os clientes da entidade.", "Os sindicatos e a sociedade em geral.", "As entidades governamentais de fiscalização.", "Os acionistas preferenciais, os investidores (atuais e potenciais) e os financiadores da empresa.", "Os empregados que não ocupam cargo de gestão."],
        3,
        ASSUNTO,
        "Correto o item D. Os usuários externos primários são aqueles que aplicam dinheiro na empresa, vinculados ao mercado de capitais: acionistas preferenciais, investidores atuais/potenciais e financiadores. Fornecedores, clientes, entidades de fiscalização, sindicatos e a sociedade em geral são usuários externos SECUNDÁRIOS."
    ),
    (
        "Acerca da classificação dos acionistas de uma sociedade anônima como usuários da informação contábil, é correto afirmar que:",
        ["Todos os acionistas, ordinários ou preferenciais, são sempre classificados como usuários externos.", "Os acionistas ordinários, por terem poder de voto nas assembleias e acesso tempestivo às informações, são usuários internos; os preferenciais, sem poder de voto, são usuários externos.", "Os acionistas preferenciais são usuários internos, por buscarem vantagens no recebimento de dividendos.", "Nenhum acionista pode ser considerado usuário interno da informação contábil.", "A classificação de um acionista como interno ou externo depende exclusivamente do valor de suas ações."],
        1,
        ASSUNTO,
        "Correto o item B. Os acionistas ordinários têm poder de voto nas assembleias, tomam decisões sobre a vida da empresa e têm acesso tempestivo às informações, sem depender dos relatórios da administração — por isso são usuários INTERNOS. Já os acionistas preferenciais, sem poder de voto e sem poder decisório nas políticas da empresa, são usuários EXTERNOS."
    ),
    (
        "O contabilista que elabora as demonstrações contábeis de determinada entidade deve ser classificado como:",
        ["Usuário externo secundário, por não ter vínculo societário com a entidade.", "Usuário interno, pois, devido ao seu conhecimento técnico, tem poder decisório na elaboração das demonstrações contábeis que serão divulgadas.", "Usuário externo primário, equiparado aos investidores.", "Não usuário da contabilidade, por ser apenas um prestador de serviço técnico.", "Usuário externo secundário, equiparado aos órgãos de fiscalização."],
        1,
        ASSUNTO,
        "Correto o item B. O contador faz parte da administração da entidade, pois, em razão de seu conhecimento técnico, tem poder decisório na elaboração das demonstrações contábeis a serem divulgadas — sendo, portanto, usuário INTERNO das informações, e não um terceiro alheio ao processo decisório."
    ),
    (
        "As demonstrações contábeis (relatórios contábeis de propósitos gerais), segundo o CPC 00, são destinadas, de forma prioritária, a(aos):",
        ["Usuários internos, especialmente à alta administração.", "Órgãos de fiscalização tributária, com exclusividade.", "Usuários externos, especialmente aos usuários externos primários.", "Empregados da entidade, com exclusividade.", "Sociedade em geral, de forma indiferenciada em relação aos demais usuários."],
        2,
        ASSUNTO,
        "Correto o item C. As demonstrações contábeis de propósitos gerais são destinadas aos usuários EXTERNOS, especialmente aos externos PRIMÁRIOS (investidores e credores por empréstimos) — os usuários internos não dependem delas, pois têm acesso direto e tempestivo às informações."
    ),
    (
        "Em relação às necessidades específicas de cada categoria de usuário externo da informação contábil, é correto afirmar que:",
        ["Os credores por empréstimos interessam-se, principalmente, por informações que lhes permitam determinar se os empréstimos e os juros correspondentes serão pagos no vencimento.", "Os empregados não têm qualquer interesse na estabilidade e na lucratividade de seus empregadores.", "Os fornecedores, em regra, têm interesse em uma entidade por período mais longo do que os credores por empréstimos.", "Os clientes não possuem interesse na continuidade operacional de seus fornecedores.", "O público em geral não é considerado usuário das informações contábeis de uma entidade."],
        0,
        ASSUNTO,
        "Correto o item A. Os credores por empréstimos interessam-se, principalmente, em determinar se os valores emprestados e os respectivos juros serão pagos no vencimento. Já os empregados interessam-se pela estabilidade/lucratividade do empregador; os fornecedores, em regra, têm interesse por período menor do que os credores por empréstimos (salvo dependência da entidade como cliente importante); clientes se interessam pela continuidade operacional de fornecedores de quem dependam; e o público em geral também é usuário externo secundário."
    ),
    (
        "Considere que uma companhia brasileira de capital aberto explore serviços de energia elétrica, estando sujeita à fiscalização da Agência Nacional de Energia Elétrica (ANEEL). Nessa situação, a ANEEL deve ser classificada como:",
        ["Usuária interna da informação contábil dessa companhia.", "Usuária externa primária, por aplicar recursos financeiros na companhia.", "Usuária externa secundária, ainda que seja um dos principais usuários da informação apresentada por aquela companhia específica.", "Não usuária da informação contábil, por se tratar de órgão público.", "Acionista ordinária da companhia, com poder de voto em assembleia."],
        2,
        ASSUNTO,
        "Correto o item C. Mesmo sendo um usuário de grande importância para aquela companhia específica (por regulamentar o setor de energia elétrica), a ANEEL é uma agência reguladora/governamental, logo usuária externa SECUNDÁRIA — os usuários externos primários são os que aplicam dinheiro na empresa (investidores e credores por empréstimos)."
    ),
    (
        "Com relação aos usuários internos e externos da informação contábil, assinale a alternativa correta:",
        ["Os usuários externos podem requerer diretamente da entidade as informações específicas de que necessitam, assim como os internos.", "Os usuários internos utilizam as informações para decidir a vida da empresa, enquanto os usuários externos as utilizam para tomar decisões próprias em relação a ela (investir, conceder crédito, vender, comprar).", "Usuários internos e externos têm exatamente o mesmo grau de acesso às informações contábeis da entidade.", "Somente os usuários externos primários podem ser classificados como usuários da informação contábil.", "A classificação em internos e externos não tem relação com o nível de acesso às informações contábeis."],
        1,
        ASSUNTO,
        "Correto o item B. Os usuários internos utilizam as informações para decidir a vida da empresa (gestão, planejamento, controle); os usuários externos as utilizam para tomar decisões a respeito de seu próprio relacionamento com a entidade, como investir, conceder crédito, comprar ou vender. Os externos, diferentemente dos internos, normalmente não podem requerer informações diretamente da entidade."
    ),
    (
        "Sobre a divisão dos usuários externos da informação contábil, é correto afirmar que os usuários externos SECUNDÁRIOS compreendem:",
        ["Os investidores atuais e potenciais e os financiadores da entidade.", "Exclusivamente os acionistas ordinários da entidade.", "Os fornecedores, os credores, os clientes, as entidades governamentais de fiscalização, os sindicatos e a sociedade em geral.", "Apenas a alta administração e os gestores da entidade.", "Exclusivamente o contabilista responsável pela elaboração das demonstrações contábeis."],
        2,
        ASSUNTO,
        "Correto o item C. Os usuários externos secundários são os fornecedores, credores, clientes, entidades governamentais de fiscalização, sindicatos e a sociedade em geral, que têm interesses diversos na entidade, normalmente ligados às suas atividades operacionais — diferentemente dos primários, que aplicam dinheiro na empresa."
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
