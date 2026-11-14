# -*- coding: utf-8 -*-
"""
Setimo conteudo de Contabilidade Geral do app (PC-PE) -- a partir do PDF
"Atributos Fundamentais" (Focus Concursos), que cobre o item 4 do edital
(Contas: conceitos, contas de debitos, contas de creditos e saldos) --
topico ate entao SEM NENHUMA cobertura no app.

Fatos novos trazidos pelo PDF: o conceito de CONTA (aspecto qualitativo =
nome; aspecto quantitativo = valor); os 6 elementos de identificacao da
conta no livro Razao (titulo, data, historico, debito, credito, saldo); a
classificacao da conta em 5 criterios (tipo, natureza, impacto, funcao,
estrutura), com foco no criterio TIPO; a distincao entre contas
PATRIMONIAIS (estaticas, compoe o Balanco Patrimonial, saldo nao se
encerra no fim do exercicio) e contas de RESULTADO (dinamicas, compoe a
DRE, se encerram/zeram no fim do exercicio -- por isso chamadas de contas
transitorias); e exemplos extensos de contas de Ativo, Passivo exigivel e
Patrimonio Liquido, incluindo a pegadinha classica de que "Banco conta
corrente" e tratado pela banca como BEM, nao como direito.

A mudanca estrutural em app-template.html ja foi feita via Edit antes
deste script rodar: foram acrescentadas 4 novas secoes ao final do
TEORIA_CONTABILIDADE_PCPE ja existente (mesma materia, nao um deck novo):
"Contas -- Conceito e Elementos de Identificacao", "Classificacao das
Contas -- 5 criterios", "Contas Patrimoniais x Contas de Resultado -- o
criterio Tipo" e "Contas Patrimoniais -- Exemplos (Ativo, Passivo, PL)".

O PDF trazia uma Maratona de 10 questoes (Certo/Errado e multipla
escolha), com bastante repeticao da mesma pegadinha central (contas de
resultado NAO sao patrimoniais, por serem encerradas no fim do exercicio).
Essa repeticao foi consolidada em questoes originais de multipla escolha,
usando a capacidade liberada para cobrir os elementos de identificacao da
conta, os 5 criterios de classificacao, e exemplos especificos de
ativo/passivo/PL que o banco do PDF testava apenas de raspao.

Este script cuida so de: (1) acrescentar as questoes a questions.json,
(2) regenerar estudo-cebraspe-ma.html a partir do app-template.html ja
editado.
"""
import json

ASSUNTO = "4 — Contabilidade Geral: Contas (Conceito, Elementos e Classificação)"

MC_QUESTIONS = [
    (
        "Acerca do conceito de conta em Contabilidade, assinale a alternativa correta:",
        ["Conta é apenas o valor monetário de um elemento patrimonial, sem relação com sua identificação qualitativa.", "Conta é o item que representa, qualitativa e quantitativamente, os componentes patrimoniais e a evolução do patrimônio, sendo considerada a base da Contabilidade.", "Conta é sinônimo de Balanço Patrimonial.", "Conta é um sinônimo de Plano de Contas, documento que reúne todas as contas de uma entidade.", "Conta só pode representar bens, nunca direitos, obrigações, receitas ou despesas."],
        1,
        ASSUNTO,
        "Correto o item B. Conta é o item que representa, qualitativa (o nome, que item está sendo representado) e quantitativamente (o valor), os componentes patrimoniais e a evolução do patrimônio. É por meio das contas que a Contabilidade registra e controla as transações que modificam o patrimônio da entidade — por isso é considerada a base da Contabilidade."
    ),
    (
        "São elementos de identificação de uma conta no Livro Razão, EXCETO:",
        ["Título — o nome da conta.", "Data — dia, mês e ano do fato.", "Histórico — descrição do que aconteceu.", "Débito e Crédito — valores debitados e creditados.", "Plano de contas — elenco de todas as contas utilizadas pela entidade."],
        4,
        ASSUNTO,
        "Correto o item E, por ser o único que NÃO é um elemento de identificação da conta no livro Razão. Os seis elementos são: título, data, histórico, débito, crédito e saldo. O plano de contas é um instrumento diferente — o elenco organizado de todas as contas da entidade, e não um elemento de identificação de uma conta individual."
    ),
    (
        "Quanto à classificação das contas contábeis, são considerados critérios de classificação, EXCETO:",
        ["Tipo — patrimonial ou de resultado.", "Natureza — devedora ou credora.", "Impacto — aplicação ou origem de recursos.", "Função — unilateral ou bilateral.", "Finalidade — econômica ou social, conforme a azienda."],
        4,
        ASSUNTO,
        "Correto o item E. Os cinco critérios de classificação da conta são: Tipo (patrimonial ou de resultado), Natureza (devedora ou credora), Impacto (aplicação ou origem), Função (unilateral ou bilateral) e Estrutura (sintética ou analítica). 'Finalidade econômica ou social' é critério de classificação das AZIENDAS (entidades), não das contas."
    ),
    (
        "Em relação às contas patrimoniais, é correto afirmar que:",
        ["São contas dinâmicas, pois alteram a situação líquida da empresa a cada período.", "Têm seu saldo encerrado (zerado) ao final de cada exercício social.", "São contas estáticas, que demonstram a situação do patrimônio em determinado momento, e seu saldo não se encerra ao final do exercício — o saldo de 31/12 é transferido como saldo inicial de 01/01.", "Compreendem exclusivamente as contas de receita e despesa.", "Não compõem o Balanço Patrimonial."],
        2,
        ASSUNTO,
        "Correto o item C. As contas patrimoniais (Ativo, Passivo exigível e Patrimônio Líquido) são estáticas — retratam o patrimônio em determinado momento — e compõem o Balanço Patrimonial. Diferentemente das contas de resultado, seu saldo NÃO se encerra ao final do exercício: o saldo apurado em 31/12 é transferido como saldo inicial de 01/01 do ano seguinte."
    ),
    (
        "Sobre as contas de resultado, assinale a alternativa correta:",
        ["São contas estáticas, que retratam a posição do patrimônio em determinado momento.", "São compostas pelas receitas e despesas, são contas dinâmicas e são encerradas (zeradas) ao final do exercício social, por isso denominadas contas transitórias.", "Compõem o Balanço Patrimonial, ao lado do Ativo e do Passivo.", "Seu saldo final de um exercício é transferido como saldo inicial do exercício seguinte, da mesma forma que as contas patrimoniais.", "Representam exclusivamente bens e direitos da entidade."],
        1,
        ASSUNTO,
        "Correto o item B. As contas de resultado (receitas e despesas) são dinâmicas, pois alteram a situação líquida da empresa, e são apresentadas na Demonstração do Resultado do Exercício (DRE) — não no Balanço Patrimonial. Ao final do exercício social, são encerradas (zeradas) para a apuração do resultado (lucro ou prejuízo), por isso são chamadas de contas TRANSITÓRIAS, ao contrário das patrimoniais."
    ),
    (
        "Toda receita, sob a ótica patrimonial, é classificada como:",
        ["Perda econômica, que diminui o Patrimônio Líquido.", "Ganho econômico, que deixa a empresa mais rica.", "Uma conta patrimonial do grupo Passivo.", "Uma obrigação da entidade perante terceiros.", "Um resíduo patrimonial, assim como o Patrimônio Líquido."],
        1,
        ASSUNTO,
        "Correto o item B. Toda RECEITA representa um ganho econômico, que deixa a empresa mais rica (aumenta o Patrimônio Líquido); toda DESPESA representa uma perda econômica, que deixa a empresa mais pobre (diminui o Patrimônio Líquido). Nenhuma das duas é conta patrimonial — ambas são contas de resultado."
    ),
    (
        "O Passivo exigível de uma entidade é conceituado como:",
        ["O conjunto dos recursos que representam bens e direitos sob o controle da empresa.", "O conjunto de obrigações perante terceiros — o capital alheio aplicado na empresa.", "A diferença entre o Ativo e o Passivo, representando a riqueza dos sócios aplicada na empresa.", "Uma conta de resultado, encerrada ao final do exercício social.", "Sinônimo de Patrimônio Líquido, por ambos representarem capital de terceiros."],
        1,
        ASSUNTO,
        "Correto o item B. O Passivo exigível representa o conjunto de obrigações da entidade perante terceiros — é o capital ALHEIO aplicado na empresa (ex.: contas a pagar, financiamentos, empréstimos, impostos a recolher). Já o Ativo é o conjunto de bens e direitos, e o Patrimônio Líquido é o capital PRÓPRIO (riqueza dos sócios)."
    ),
    (
        "Acerca do Patrimônio Líquido, é correto afirmar que:",
        ["É conceituado como a soma do Ativo com o Passivo exigível da entidade.", "Representa uma dívida exigível da empresa junto aos sócios, equiparável às obrigações com terceiros.", "É a diferença entre o valor do Ativo e do Passivo em determinado momento — o resíduo patrimonial que, legalmente, representa uma dívida NÃO exigível da empresa junto aos sócios.", "Compõe a Demonstração do Resultado do Exercício, ao lado das receitas e despesas.", "É uma conta de resultado, pois seu saldo é encerrado ao final do exercício social."],
        2,
        ASSUNTO,
        "Correto o item C. O Patrimônio Líquido é a diferença entre o valor do Ativo e do Passivo de uma entidade em determinado momento — é o resíduo patrimonial, que legalmente representa uma dívida NÃO EXIGÍVEL da empresa junto aos sócios, representando a riqueza destes aplicada na empresa (capital próprio)."
    ),
    (
        "Considerando-se a tradicional classificação adotada pelas bancas de concurso, assinale a alternativa que apresenta corretamente a natureza patrimonial de cada conta a seguir: Duplicatas a receber; Banco conta corrente; Impostos a recolher.",
        ["Direito; Bem; Obrigação.", "Bem; Direito; Obrigação.", "Obrigação; Bem; Direito.", "Direito; Obrigação; Bem.", "Bem; Obrigação; Direito."],
        0,
        ASSUNTO,
        "Correto o item A. 'Duplicatas a receber' é um DIREITO (contas que terminam em '... a receber' tipicamente representam direitos da entidade). 'Banco conta corrente', tradicionalmente para as bancas, é classificado como um BEM da empresa (ao lado de Caixa, Estoque, Móveis e utensílios) — ainda que parte da doutrina o considere um direito. 'Impostos a recolher' é uma OBRIGAÇÃO (contas que terminam em '... a pagar/recolher' representam obrigações perante terceiros)."
    ),
    (
        "Com relação ao critério de classificação das contas quanto ao TIPO, é correto afirmar que:",
        ["As contas se dividem em patrimoniais e de resultado; as patrimoniais compõem o Ativo, o Passivo e o Patrimônio Líquido, enquanto as de resultado compreendem as receitas e despesas, apresentadas na DRE.", "As contas se dividem exclusivamente em devedoras e credoras.", "Contas patrimoniais e contas de resultado são sinônimos, apenas com denominações distintas.", "O critério Tipo classifica as contas quanto à sua estrutura, em sintéticas ou analíticas.", "Contas de resultado compõem o Balanço Patrimonial, enquanto as patrimoniais compõem a DRE."],
        0,
        ASSUNTO,
        "Correto o item A. Quanto ao TIPO, as contas se dividem em patrimoniais (Ativo = bens e direitos; Passivo = obrigações; Patrimônio Líquido = resíduo patrimonial — todas compõem o Balanço Patrimonial) e de resultado (Receita = ganho econômico; Despesa = perda econômica — ambas compõem a Demonstração do Resultado do Exercício). 'Devedora ou credora' é o critério Natureza; 'sintética ou analítica' é o critério Estrutura."
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
