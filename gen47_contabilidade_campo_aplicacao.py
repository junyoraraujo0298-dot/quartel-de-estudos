# -*- coding: utf-8 -*-
"""
Quinto conteudo de Contabilidade Geral do app (PC-PE) -- a partir do PDF
"Campo de Aplicacao da Contabilidade" (Focus Concursos), que aprofunda o
item 1 ("Conceitos, objetivos e finalidades da contabilidade") do
PROGRAMA_PCPE_AGENTE oficial.

Ate aqui, o deck TEORIA_CONTABILIDADE_PCPE so mencionava o campo de
aplicacao de forma muito resumida, dentro de uma tabela comparativa
objeto/objetivo/finalidade/campo de aplicacao/principio basico ("Campo de
aplicacao: Qualquer pessoa fisica ou juridica"). O conceito de AZIENDA --
o termo tecnico/sintetico que a banca usa para "campo de aplicacao" --,
seus 3 elementos (patrimonio, administracao, atividade) e sua
classificacao (quanto ao tipo: PF/PJ, publica/privada, capital aberto/
fechado; quanto a finalidade: sociais, economico-sociais, economicas) sao
conteudo genuinamente novo.

A mudanca estrutural em app-template.html ja foi feita via Edit antes deste
script rodar: foi acrescentada uma nova secao "Campo de Aplicacao da
Contabilidade -- Azienda" ao const TEORIA_CONTABILIDADE_PCPE ja existente
(mesma materia, nao um deck novo), logo apos a tabela que ja mencionava o
campo de aplicacao resumidamente.

O PDF trazia uma "Maratona de Questoes" com 10 itens, a maioria Certo/
Errado, testando repetidamente o MESMO fato (o campo de aplicacao abrange
qualquer entidade com patrimonio, com ou sem fins lucrativos, publica ou
privada -- itens 1, 3, 5, 7 e 9 do PDF sao, em essencia, a mesma pegadinha
reformulada). Em vez de transcrever as 10 questoes 1:1, essa pegadinha
central foi consolidada em uma unica questao de multipla escolha bem
elaborada, e a capacidade liberada foi usada para questoes originais
cobrindo os fatos novos (elementos da azienda, classificacao por tipo e
por finalidade) que o banco de questoes do PDF nao chegou a testar
diretamente.

Este script cuida so de: (1) acrescentar as questoes a questions.json,
(2) regenerar estudo-cebraspe-ma.html a partir do app-template.html ja
editado.
"""
import json

ASSUNTO = "1 — Contabilidade Geral: Campo de Aplicação (Azienda)"

MC_QUESTIONS = [
    (
        "Acerca do campo de aplicação da contabilidade, assinale a alternativa correta:",
        ["O campo de aplicação da contabilidade abrange todas as entidades, sejam elas pessoas físicas ou jurídicas, com ou sem finalidade lucrativa, de direito público ou privado, desde que possuam patrimônio.", "A contabilidade e seus conceitos aplicam-se apenas às entidades com finalidade lucrativa, visto que sua função é quantificar o resultado.", "Os conceitos relativos à ciência contábil não se aplicam aos microempreendedores individuais, haja vista sua condição de pessoa física.", "O campo de aplicação da contabilidade não abrange as microempresas, haja vista a limitada movimentação econômico-financeira que efetuam no exercício.", "O campo de aplicação da contabilidade não abrange as entidades sem fins lucrativos, haja vista a apuração do lucro ser o propósito último de sua existência."],
        0,
        ASSUNTO,
        "Correto o item A. O campo de aplicação da contabilidade abrange qualquer entidade (azienda) que possua patrimônio — pessoa física ou jurídica, com ou sem fins lucrativos, pública ou privada —, o que inclui microempreendedores individuais, microempresas e entidades sem fins lucrativos (desde que tenham patrimônio a controlar)."
    ),
    (
        "O campo de atuação da Contabilidade é denominado, de forma sintetizada, de AZIENDA — termo de origem italiana. A classificação de uma azienda (entidade) exige a existência de três elementos principais, que são:",
        ["Patrimônio, administração e atividade.", "Ativo, passivo e patrimônio líquido.", "Objeto, objetivo e finalidade.", "Bens, direitos e obrigações.", "Escrituração, demonstração e divulgação."],
        0,
        ASSUNTO,
        "Correto o item A. Azienda define a relação entre um PATRIMÔNIO, a ação ADMINISTRATIVA do homem sobre esse patrimônio e a execução de uma ATIVIDADE, praticando atos de natureza econômica — esses são os três elementos exigidos para a classificação de uma entidade como azienda."
    ),
    (
        "Quanto à sua finalidade, as aziendas que têm fim puramente social, não visam ao lucro e são denominadas de instituições (como ONGs, igrejas, clubes e sindicatos) são classificadas como aziendas:",
        ["Sociais.", "Econômico-sociais.", "Econômicas.", "Mistas.", "Públicas."],
        0,
        ASSUNTO,
        "Correto o item A. As aziendas SOCIAIS têm fim puramente social, não visam ao lucro, e são denominadas de instituições — exemplos: ONGs, igrejas, clubes e sindicatos."
    ),
    (
        "As aziendas que são entidades sociais que operam atividades com características econômicas, cujo resultado é um superávit ou déficit (sempre reaplicado na própria entidade) — como cooperativas, fundos de investimento e fundos de pensão —, são classificadas, quanto à finalidade, como aziendas:",
        ["Econômico-sociais.", "Sociais.", "Econômicas.", "Públicas.", "Mistas."],
        0,
        ASSUNTO,
        "Correto o item A. As aziendas ECONÔMICO-SOCIAIS são entidades sociais que operam com características econômicas; todo resultado positivo (superávit) é reaplicado na própria entidade, nunca distribuído — exemplos: cooperativas, fundos de investimento e fundos de pensão."
    ),
    (
        "As aziendas que visam ao lucro, podendo este ser destinado aos sócios na forma de dividendos, e que são denominadas de empresas, são classificadas, quanto à finalidade, como aziendas:",
        ["Econômicas.", "Sociais.", "Econômico-sociais.", "Mistas.", "Associativas."],
        0,
        ASSUNTO,
        "Correto o item A. As aziendas ECONÔMICAS visam ao lucro, que pode ser destinado aos sócios como dividendos — são denominadas de empresas, ao contrário das aziendas sociais (sem fins lucrativos) e econômico-sociais (resultado sempre reaplicado)."
    ),
    (
        "Quanto ao tipo, as aziendas podem ser classificadas em pessoas físicas ou jurídicas, empresas públicas ou privadas, e, ainda, em:",
        ["Sociedades de capital aberto ou fechado.", "Sociedades de pequeno e de grande porte, exclusivamente.", "Microempresas e empresas de grande porte, exclusivamente.", "Entidades nacionais e multinacionais, exclusivamente.", "Entidades lucrativas e deficitárias, exclusivamente."],
        0,
        ASSUNTO,
        "Correto o item A. Quanto ao tipo, as aziendas se classificam em: pessoas físicas ou jurídicas; empresas públicas ou privadas; e sociedades de capital aberto ou fechado."
    ),
    (
        "Para atingir seu objetivo fundamental, a contabilidade deve:",
        ["Priorizar a evidenciação de todas as informações que possibilitem o controle e a tomada de decisões por parte de seus usuários internos e externos.", "Restringir-se a atender aos requisitos da legislação referente aos impostos diretos e indiretos incidentes sobre as operações da entidade.", "Priorizar exclusivamente a apuração do lucro tributável da entidade.", "Restringir-se à elaboração do Balanço Patrimonial, único documento relevante para os usuários.", "Priorizar exclusivamente o controle da folha de pagamento da entidade."],
        0,
        ASSUNTO,
        "Correto o item A. O objetivo da contabilidade é fornecer informações aos usuários internos e externos, de forma que consigam controlar a entidade e tomar suas decisões operacionais e de investimento — e não se restringir a questões tributárias, de lucro ou de um único demonstrativo."
    ),
    (
        "Se uma entidade for capaz de atender aos requisitos da legislação referente aos impostos diretos e indiretos incidentes sobre suas operações, é correto afirmar que, com isso, a contabilidade dessa entidade:",
        ["Ainda não terá atingido seus objetivos finais, já que o objetivo final da contabilidade é fornecer informação de natureza econômica, financeira, operacional e social, útil aos usuários internos e externos — não apenas tributária.", "Terá atingido plenamente seus objetivos finais, pois o cumprimento da legislação tributária é o objetivo central da contabilidade.", "Terá atingido seus objetivos finais apenas se a entidade for de direito público.", "Terá atingido seus objetivos finais apenas se a entidade tiver finalidade lucrativa.", "Não há relação alguma entre o cumprimento da legislação tributária e os objetivos da contabilidade."],
        0,
        ASSUNTO,
        "Correto o item A. O objetivo final da contabilidade vai muito além do cumprimento de obrigações tributárias — abrange informação econômica, financeira, operacional e social, útil a todos os usuários, internos e externos."
    ),
    (
        "Julgue os itens a seguir, relativos à Contabilidade: I) A Contabilidade é uma ciência exata; II) A Contabilidade tem funções administrativa (controlar o patrimônio) e econômica (apurar o resultado do exercício); III) O principal campo de aplicação da Contabilidade são as aziendas. Está(ão) correto(s):",
        ["Apenas os itens II e III.", "Apenas o item I.", "Apenas o item III.", "Apenas os itens I e II.", "Os itens I, II e III."],
        0,
        ASSUNTO,
        "Correto o item A. A Contabilidade é ciência SOCIAL aplicada, não ciência exata (item I está errado); tem função administrativa (controlar o patrimônio) e econômica (apurar o resultado do exercício) — item II correto; e seu campo de aplicação são, de fato, as aziendas — item III correto."
    ),
    (
        "Pode-se afirmar que o campo de aplicação da contabilidade é onde ela é ________ e abrange todas as entidades ________.",
        ["utilizada / econômico-administrativas", "estudada / financeiras", "fiscalizada / fechadas", "regulamentada / públicas", "auditada / multinacionais"],
        0,
        ASSUNTO,
        "Correto o item A. O campo de aplicação da contabilidade é onde ela é UTILIZADA, abrangendo todas as entidades ECONÔMICO-ADMINISTRATIVAS (aziendas) — pessoas físicas ou jurídicas, com ou sem fins lucrativos, públicas ou privadas."
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
