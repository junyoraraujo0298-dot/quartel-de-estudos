# -*- coding: utf-8 -*-
"""
Move os decks "Constituicao de PE" e "Estatuto do Policial Civil de PE"
(Lei 6.425/1972) da aba Estrategia para a aba Legislacao, alinhando com o
item 2 (e 1) da "Legislacao Estadual" do PROGRAMA_PCPE_AGENTE oficial, e
acrescenta 18 questoes de multipla escolha (regra atual pro PC-PE) sobre o
Estatuto do Policial Civil -- a lei organica da propria carreira de Agente
de Policia da PC-PE.

As mudancas estruturais em app-template.html (mover os decks de
ESTRATEGIA_DECKS para LAW_DECKS, registrar o disc "Legislacao Estadual" em
LEITURA_DECK_TO_DISC, atualizar o texto do PROGRAMA_PCPE_AGENTE e corrigir a
nota desatualizada "este app ainda nao tem banco de questoes propria da
PC-PE") ja foram feitas via Edit antes deste script rodar. Este script cuida
só de: (1) acrescentar as questoes a questions.json, (2) regenerar
estudo-cebraspe-ma.html a partir do app-template.html ja editado.
"""
import json

MC_QUESTIONS = [
    (
        "Segundo o art. 4º do Estatuto do Policial Civil de PE (Lei nº 6.425/1972), na redação dada pela Lei Complementar nº 490/2022, havendo compatibilidade de horários, as hipóteses de acumulação remunerada de cargos públicos previstas no art. 37, XVI, da Constituição Federal, além das atividades de magistério e empregos privativos de profissionais de saúde, ficam limitadas, em qualquer caso, a:",
        ["1 (um) vínculo.", "2 (dois) vínculos.", "3 (três) vínculos.", "Não há limite numérico, desde que haja compatibilidade de horários.", "2 (dois) vínculos, exceto para o magistério, que não se submete a limite."],
        1,
        "2 — Lei nº 6.425/1972, art. 4º (acumulação de cargos)",
        "Correto o item B. O art. 4º, caput, na redação dada pelo art. 1º da Lei Complementar nº 490/2022, fixa o limite de 2 (dois) vínculos em qualquer caso de acumulação remunerada de cargos públicos."
    ),
    (
        "Em relação à acumulação de cargos pelo funcionário policial civil de Pernambuco, assinale a alternativa correta, conforme o art. 4º, §2º, do Estatuto do Policial Civil (Lei nº 6.425/1972):",
        ["É permitida a acumulação de dois cargos de natureza policial, desde que haja compatibilidade de horários.", "É vedada, em qualquer hipótese, a acumulação de cargo de natureza policial com cargo técnico que exija diploma de curso superior.", "É vedada ao funcionário policial a acumulação de cargos de natureza policial.", "É permitida a acumulação de até três cargos de natureza policial, nos termos da Lei Complementar nº 490/2022.", "Toda acumulação de cargos depende de prévia autorização do Conselho Superior de Polícia."],
        2,
        "2 — Lei nº 6.425/1972, art. 4º, §2º (vedação de acumulação policial)",
        "Correto o item C. O art. 4º, §2º, é categórico: 'É vedada ao funcionário policial a acumulação de cargos de natureza policial.' Essa vedação é específica e não se confunde com o limite geral de 2 vínculos do caput, que trata de outras hipóteses de acumulação (magistério, saúde)."
    ),
    (
        "De acordo com o art. 5º do Estatuto do Policial Civil de PE, na redação dada pelo inciso I do art. 52 da Lei nº 6.657/1974, os cargos com atribuições e responsabilidade de natureza policial são providos por quantas formas?",
        ["6 formas, conforme a redação original de 1972.", "7 formas: nomeação, acesso, promoção, reintegração, aproveitamento, reversão e transferência.", "5 formas, pois a reversão foi suprimida pela Lei nº 6.657/1974.", "8 formas, incluindo a remoção como forma de provimento.", "4 formas, restritas a nomeação, promoção, reintegração e aproveitamento."],
        1,
        "2 — Lei nº 6.425/1972, art. 5º (formas de provimento)",
        "Correto o item B. A redação original de 1972 trazia 6 formas e não havia 'Acesso' como forma distinta de 'Promoção'. A Lei nº 6.657/1974 acrescentou 'Acesso' (separado de 'Promoção') e 'Transferência', totalizando as 7 formas vigentes: nomeação, acesso, promoção, reintegração, aproveitamento, reversão e transferência."
    ),
    (
        "Consoante a redação dada pelo art. 3º da Lei nº 10.466/1990 ao art. 7º do Estatuto do Policial Civil de PE, os cargos vagos em classe inicial de série de classes, do Quadro de Autoridades Policiais Civis e do Quadro de Pessoal Policial da Secretaria da Segurança Pública, são providos por nomeação e por acesso em qual proporção?",
        ["70% por nomeação e 30% por acesso.", "100% por acesso, salvo inexistência de candidato habilitado.", "50% das vagas para cada uma das duas formas, respectivamente.", "30% por nomeação e 70% por acesso.", "A proporção é livremente definida em cada edital de concurso."],
        2,
        "2 — Lei nº 6.425/1972, art. 7º (proporção nomeação/acesso)",
        "Correto o item C. O art. 7º, na redação da Lei nº 10.466/1990, fixa que o provimento se dá 'por nomeação e acesso, na proporção, respectivamente, de 50% das vagas a preencher' — ou seja, metade para quem entra de fora (nomeação/concurso externo) e metade para quem já é do quadro (acesso/concurso interno)."
    ),
    (
        "Segundo o art. 8º, inciso II, do Estatuto do Policial Civil de PE (redação da Lei nº 10.466/1990), qual é a faixa etária exigida para a inscrição no concurso público, na data do pedido de inscrição, salvo se o candidato já for funcionário público estadual?",
        ["18 a 30 anos.", "21 a 35 anos.", "18 a 35 anos.", "21 a 40 anos.", "Não há exigência de idade mínima ou máxima, apenas de maioridade civil."],
        1,
        "2 — Lei nº 6.425/1972, art. 8º (requisitos de inscrição)",
        "Correto o item B. O art. 8º, II, exige idade mínima de 21 e máxima de 35 anos na data do pedido de inscrição, ressalvado o candidato que já seja funcionário público estadual."
    ),
    (
        "De acordo com o §1º do art. 22 do Estatuto do Policial Civil de PE (redação da Lei nº 10.278/1989), o auxílio-moradia, calculado sobre o vencimento-base do cargo somado à gratificação por tempo de serviço, é atribuído em quais percentuais aos funcionários lotados, respectivamente, no interior do Estado e na Área Metropolitana (inclusive a Capital)?",
        ["20% no interior e 15% na Área Metropolitana.", "15% no interior e 20% na Área Metropolitana.", "10% no interior e 20% na Área Metropolitana.", "25% no interior e 15% na Área Metropolitana.", "O percentual é único, de 20%, independentemente da lotação."],
        0,
        "2 — Lei nº 6.425/1972, art. 22, §1º (auxílio-moradia)",
        "Correto o item A. O §1º do art. 22 fixa 20% para os lotados em unidades do interior do Estado e 15% para os lotados na Área Metropolitana, inclusive a Capital."
    ),
    (
        "Pelo art. 25, §1º, do Estatuto do Policial Civil de PE, a gratificação de função policial sujeita o funcionário policial ao regime de dedicação integral, obrigando-o à prestação de, no mínimo, quantas horas mensais de trabalho?",
        ["150 horas.", "180 horas.", "200 horas.", "220 horas.", "240 horas."],
        2,
        "2 — Lei nº 6.425/1972, art. 25, §1º (dedicação integral)",
        "Correto o item C. O §1º do art. 25 exige, no mínimo, 200 (duzentas) horas mensais de trabalho como contrapartida do regime de dedicação integral ligado à gratificação de função policial."
    ),
    (
        "Nos termos do art. 26 do Estatuto do Policial Civil de PE, a gratificação de função policial, calculada sobre o vencimento do cargo efetivo, é fixada entre quais limites percentuais?",
        ["Entre 50% (mínimo) e 100% (máximo).", "Entre 100% (mínimo) e 150% (máximo).", "Entre 80% (mínimo) e 120% (máximo).", "Entre 100% (mínimo) e 200% (máximo).", "É fixa em 100%, sem variação entre mínimo e máximo."],
        1,
        "2 — Lei nº 6.425/1972, art. 26 (percentual da gratificação de função policial)",
        "Correto o item B. O art. 26, caput, fixa a gratificação de função policial entre os limites mínimo de 100% e máximo de 150% sobre o vencimento do cargo efetivo."
    ),
    (
        "São penas disciplinares expressamente previstas no art. 34 do Estatuto do Policial Civil de PE, EXCETO:",
        ["Repreensão.", "Multa.", "Detenção disciplinar.", "Advertência verbal.", "Cassação de aposentadoria ou disponibilidade."],
        3,
        "2 — Lei nº 6.425/1972, art. 34 (rol de penas disciplinares)",
        "Correto o item D, por ser a única pena NÃO prevista no rol taxativo do art. 34: repreensão, multa, suspensão, detenção disciplinar, destituição de função, demissão e cassação de aposentadoria ou disponibilidade. 'Advertência verbal' não consta dessa lista."
    ),
    (
        "Consoante o art. 37 do Estatuto do Policial Civil de PE, a pena de suspensão, aplicada em caso de falta grave ou de reincidência em falta de qualquer natureza, não poderá exceder a quantos dias?",
        ["15 dias.", "20 dias.", "30 dias.", "45 dias.", "60 dias."],
        2,
        "2 — Lei nº 6.425/1972, art. 37 (limite da suspensão)",
        "Correto o item C. O art. 37, caput, estabelece que a suspensão não excederá a 30 (trinta) dias."
    ),
    (
        "Segundo o art. 44 do Estatuto do Policial Civil de PE, o funcionário que, recebendo ordem de detenção disciplinar, se recusar a cumpri-la, ou, durante o cumprimento, desatender às normas da penalidade ou praticar outra falta de qualquer natureza, comete transgressão configuradora de:",
        ["falta leve, sujeita apenas a repreensão por escrito.", "insubordinação grave em serviço, sujeita à pena de demissão.", "abandono de cargo, sujeito à cassação de aposentadoria.", "reincidência simples, sujeita apenas à prorrogação do prazo de detenção.", "crime contra a Administração Pública, de apuração exclusivamente judicial."],
        1,
        "2 — Lei nº 6.425/1972, art. 44 (insubordinação grave em serviço)",
        "Correto o item B. O art. 44 tipifica essa conduta como 'transgressão configuradora de insubordinação grave em serviço, sujeita a pena de demissão' — uma das hipóteses que dispensam o enquadramento comum do art. 31 e vão direto para a pena mais grave."
    ),
    (
        "Pelo art. 49, inciso IX, do Estatuto do Policial Civil de PE, a pena de demissão é aplicada ao funcionário que faltar ao serviço por quantos dias interpolados, sem causa justificada, no período de doze meses?",
        ["30 dias.", "45 dias.", "60 dias.", "90 dias.", "120 dias."],
        2,
        "2 — Lei nº 6.425/1972, art. 49, IX (demissão por faltas interpoladas)",
        "Correto o item C. O art. 49, IX, prevê demissão para a falta ao serviço por 60 (sessenta) dias interpolados, sem causa justificada, durante o período de doze meses."
    ),
    (
        "Segundo o art. 52, inciso I, do Estatuto do Policial Civil de PE, a aplicação das penas de demissão e de cassação de aposentadoria ou disponibilidade é de competência:",
        ["concorrente entre o Governador e o Secretário da Segurança Pública.", "privativa do Governador do Estado.", "do Secretário da Segurança Pública, com recurso ao Governador.", "do Corregedor-Geral de Polícia.", "do Conselho Superior de Polícia, em sessão secreta."],
        1,
        "2 — Lei nº 6.425/1972, art. 52, I (competência privativa do Governador)",
        "Correto o item B. O art. 52, I, atribui ao Governador competência para aplicar penalidades em qualquer caso e, privativamente, nos casos de demissão e de cassação de aposentadoria ou disponibilidade — nos demais casos, quem aplica é o Secretário da Segurança Pública (inciso II)."
    ),
    (
        "De acordo com o art. 56, parágrafo único, do Estatuto do Policial Civil de PE, o processo disciplinar, instrumento de apuração de irregularidades cometidas por funcionário policial, compreende:",
        ["somente o inquérito disciplinar.", "somente a sindicância.", "a sindicância e o inquérito disciplinar.", "a sindicância, o inquérito disciplinar e o processo judicial.", "exclusivamente a apuração realizada pelo Conselho Superior de Polícia."],
        2,
        "2 — Lei nº 6.425/1972, art. 56 (sindicância e inquérito disciplinar)",
        "Correto o item C. O parágrafo único do art. 56 define que 'o processo disciplinar compreenderá a sindicância e o inquérito disciplinar'."
    ),
    (
        "A Comissão Permanente de Disciplina, responsável por promover o inquérito disciplinar no âmbito da Polícia Civil de Pernambuco, é composta, segundo o art. 61 do Estatuto do Policial Civil, por quantos membros, de preferência bacharéis em Direito?",
        ["2 membros.", "3 membros.", "5 membros.", "1 membro, auxiliado por um secretário.", "Número variável, a critério exclusivo do Secretário da Segurança Pública."],
        1,
        "2 — Lei nº 6.425/1972, art. 61 (Comissão Permanente de Disciplina)",
        "Correto o item B. O art. 61, caput, prevê que a Comissão Permanente de Disciplina é composta de 3 (três) membros, de preferência bacharéis em Direito, funcionários policiais ou não, designada pelo Secretário da Segurança Pública."
    ),
    (
        "Na redação vigente, dada pelo art. 54 da Lei nº 6.657/1974, o art. 72 do Estatuto do Policial Civil de PE instituiu:",
        ["a Ordem do Mérito Policial, com medalhas em ouro, prata e bronze.", "a Medalha do Mérito Policial, nas classes ouro, prata e bronze.", "a Comenda do Mérito Policial Civil, em classe única.", "o Diploma de Honra ao Mérito Policial, sem distinção de classes.", "a Medalha do Mérito Policial, exclusivamente na classe ouro."],
        1,
        "2 — Lei nº 6.425/1972, art. 72 (Medalha do Mérito Policial)",
        "Correto o item B. A redação original de 1972 instituía a 'Ordem do Mérito Policial, com as medalhas respectivas em ouro, prata e bronze' — essa redação foi substituída pela Lei nº 6.657/1974, que passou a instituir diretamente a 'Medalha do Mérito Policial, nas classes ouro, prata e bronze', sem a antiga 'Ordem'."
    ),
    (
        "Segundo o art. 82, §2º, do Estatuto do Policial Civil de PE (acrescido pela Lei nº 15.093/2013), o Policial Civil do Estado que incorrer em incapacidade definitiva para o exercício da atividade-fim, decorrente de deficiência, pode:",
        ["ser automaticamente aposentado, sem possibilidade de permanência no serviço.", "mediante requerimento, permanecer no serviço em atividade administrativa, sendo readaptado em função compatível com sua capacidade física e intelectual, desde que julgado apto por Junta Médica do Estado.", "ser promovido ao padrão imediatamente superior, mantendo as atribuições da atividade-fim.", "optar pela readaptação e, cumulativamente, pela promoção prevista no caput do art. 82.", "ser posto à disposição de órgão federal, a critério do Governador, pelo prazo de 90 dias."],
        1,
        "2 — Lei nº 6.425/1972, art. 82, §2º (readaptação por incapacidade)",
        "Correto o item B. O §2º permite a permanência no serviço em atividade administrativa, mediante readaptação em função compatível, condicionada à aptidão julgada por Junta Médica do Estado e à conveniência do serviço. Pelo §3º, quem opta pela readaptação NÃO faz jus à promoção prevista no caput do art. 82 — por isso o item D está errado."
    ),
    (
        "Além dos deveres comuns aos demais funcionários públicos civis, é dever do funcionário policial civil de Pernambuco, segundo o art. 30 do Estatuto do Policial Civil (Lei nº 6.425/1972):",
        ["exercer atividade de magistério eventual, ainda que incompatível com o serviço.", "a dedicação e a fidelidade à Pátria, cuja honra, segurança e integridade deve defender mesmo com sacrifício da própria vida.", "participar de manifestações de apreço às autoridades superiores, como forma de disciplina.", "divulgar, por qualquer veículo de comunicação, fatos ocorridos na repartição, quando de interesse público.", "exercer comércio ou participar de sociedade comercial como forma de complementação de renda."],
        1,
        "2 — Lei nº 6.425/1972, art. 30 (deveres do funcionário policial)",
        "Correto o item B, que reproduz o art. 30, I. Os demais itens descrevem, na verdade, TRANSGRESSÕES DISCIPLINARES previstas no art. 31 (incisos IV, II e XIII, respectivamente) — o contrário de um dever."
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
            "disc": "Legislação Estadual",
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
