# -*- coding: utf-8 -*-
# Adapta os itens 51-58 da Prova CEBRASPE - PMMA 2026 (ja adicionados como
# CE no corp PM pelo gen10) para o corp BM, em formato MC. Esses itens
# tratam do Estatuto da PM/MA (Lei 6.513/95), que se aplica tambem ao
# CBMMA por forca do art. 167 dessa mesma lei -- por isso "tambem caem"
# para quem estuda pra BMMA, do mesmo jeito que os itens 66-75 (Lei
# 14.751/2023) ja foram adaptados no gen10.
import json

with open('questions.json', encoding='utf-8') as f:
    raw = f.read()

data_check = json.loads(raw)
max_id = max(q['id'] for q in data_check)
assert max_id == 956, max_id

DISC = "Estatuto da PM/MA (Lei 6.513/95)"
FONTE = (" (Adaptação, em múltipla escolha, de item da Prova CEBRASPE – PMMA, Edital 2026, sobre o "
         "Estatuto da PM/MA, aplicável ao CBMMA por força do art. 167 da Lei nº 6.513/95.)")

BM_MC = [
    {"enun": "Acerca da promoção em ressarcimento de preterição, nos termos do Estatuto da PM/MA "
             "(Lei nº 6.513/95), aplicável também ao CBMMA por força do art. 167, é correto afirmar "
             "que ela:",
     "alts": ["é admitida em casos extraordinários, nos termos do art. 78, §1º.",
              "é vedada, independentemente do caso, não havendo qualquer exceção legal.",
              "somente pode ocorrer após o trânsito em julgado de decisão judicial específica.",
              "depende de aprovação prévia da Assembleia Legislativa.",
              "é concedida automaticamente a cada cinco anos de serviço, independentemente de "
              "preterição."],
     "resp": 0,
     "exp": "Correto, nos termos do art. 78, §1º, da Lei nº 6.513/95 — a promoção em ressarcimento de "
            "preterição é admitida em casos extraordinários, não sendo vedada de forma absoluta."},

    {"enun": "Quanto ao ingresso no Quadro de Oficiais de Administração (QOA) e no Quadro de Oficiais "
             "Especialistas (QOE), nos termos do Estatuto da PM/MA (Lei nº 6.513/95), é correto "
             "afirmar que ele:",
     "alts": ["é aberto a qualquer praça, independentemente da graduação ou do tempo de serviço.",
              "exige exclusivamente diploma de nível superior em Direito.",
              "é restrito a subtenentes com, no mínimo, 18 anos de efetivo serviço e diploma de curso "
              "de nível superior, além de aprovação no CHOA/CHOE.",
              "é restrito a subtenentes com, no mínimo, 10 anos de efetivo serviço e certificado de "
              "conclusão de ensino médio.",
              "é vedado a subtenentes, sendo restrito a sargentos com curso superior."],
     "resp": 2,
     "exp": "Correto, nos termos do art. 11 da Lei nº 6.513/95: subtenentes, 18 anos de efetivo "
            "serviço, diploma de nível superior e aprovação no CHOA/CHOE — não 10 anos nem ensino "
            "médio."},

    {"enun": "Segundo o art. 39 do Estatuto da PM/MA (Lei nº 6.513/95), aplicável também ao CBMMA, o "
             "aprimoramento técnico-profissional é:",
     "alts": ["uma das manifestações essenciais do valor policial militar.",
              "uma faculdade do militar, sem relação com o valor policial militar.",
              "exigido apenas dos oficiais, não das praças.",
              "incompatível com o espírito de corpo e o civismo.",
              "uma atribuição exclusiva da Corregedoria-Geral."],
     "resp": 0,
     "exp": "Correto, nos termos do art. 39, VI, da Lei nº 6.513/95."},

    {"enun": "Constitui prerrogativa dos policiais e bombeiros militares, nos crimes militares:",
     "alts": ["a imunidade total a qualquer responsabilização penal.",
              "o julgamento em foro especial (Justiça Militar Estadual).",
              "o julgamento exclusivo pelo Tribunal do Júri.",
              "a vedação a qualquer recurso às instâncias superiores.",
              "o julgamento direto pelo Supremo Tribunal Federal."],
     "resp": 1,
     "exp": "Correto — o foro especial da Justiça Militar Estadual é prerrogativa assegurada aos "
            "militares estaduais para o julgamento de crimes militares."},

    {"enun": "Sobre a requisição ou cessão de militar estadual da ativa para a Defensoria Pública do "
             "Maranhão, é correto afirmar que:",
     "alts": ["é possível, mediante decisão indelegável do chefe do Poder Executivo.",
              "é vedada em qualquer hipótese.",
              "pode ser decidida livremente pelo Comandante-Geral, sem participação do Governador.",
              "depende exclusivamente de requerimento do próprio militar, sem análise da autoridade "
              "superior.",
              "somente é possível após 20 anos de efetivo serviço."],
     "resp": 0,
     "exp": "Correto — a Defensoria Pública consta do rol de órgãos aos quais o militar pode ser posto "
            "à disposição (art. 35 da Lei nº 6.513/95), mediante decisão reservada ao chefe do Poder "
            "Executivo."},

    {"enun": "A precedência hierárquica no âmbito das corporações militares estaduais é regulada, nos "
             "termos do art. 20 da Lei nº 6.513/95, de forma a:",
     "alts": ["prestigiar a precedência funcional, em detrimento da antiguidade no posto ou "
              "graduação.",
              "depender exclusivamente da idade do militar, independentemente do posto.",
              "ser definida por sorteio entre militares do mesmo posto.",
              "prestigiar a antiguidade no posto ou graduação, em vez da precedência funcional.",
              "não admitir qualquer critério de precedência entre militares de mesmo posto."],
     "resp": 3,
     "exp": "Correto, nos termos do art. 20 da Lei nº 6.513/95 — a antiguidade no posto/graduação é o "
            "critério padrão, cedendo à precedência funcional apenas quando esta for expressamente "
            "estabelecida em lei."},

    {"enun": "O exame toxicológico exigido dos candidatos aos cursos de formação das corporações "
             "militares estaduais do Maranhão:",
     "alts": ["é obrigatório e possui caráter eliminatório.",
              "é facultativo, a critério do candidato.",
              "é obrigatório, mas não tem caráter eliminatório.",
              "só é exigido dos candidatos a oficial, não das praças.",
              "foi abolido pela legislação vigente."],
     "resp": 0,
     "exp": "Correto, nos termos do art. 9º, parágrafo único, da Lei nº 6.513/95."},

    {"enun": "Em caso de concurso de crime militar e de transgressão disciplinar cometidos pelo mesmo "
             "militar estadual, nos termos do art. 55, §2º, da Lei nº 6.513/95:",
     "alts": ["aplicam-se cumulativamente a sanção disciplinar e a pena relativa ao crime.",
              "aplica-se somente a sanção disciplinar, afastando-se a pena criminal.",
              "aplica-se somente a pena relativa ao crime.",
              "cabe ao militar escolher qual das duas punições prefere cumprir.",
              "nenhuma das duas sanções é aplicável, por bis in idem."],
     "resp": 2,
     "exp": "Correto, nos termos do art. 55, §2º, da Lei nº 6.513/95 — aplica-se SOMENTE a pena "
            "relativa ao crime, e não ambas cumulativamente."},
]

assert len(BM_MC) == 8

next_id = 957
new_questions = []
for item in BM_MC:
    new_questions.append({
        "id": next_id, "corp": "BM", "disc": DISC, "tipo": "MC",
        "enun": item["enun"], "alts": item["alts"], "resp": item["resp"],
        "exp": item["exp"] + FONTE,
    })
    next_id += 1

assert new_questions[-1]['id'] == 964

body = raw[:-1]
for q in new_questions:
    body += '\r\n, ' + json.dumps(q, ensure_ascii=False)
body += ']'

with open('questions.json', 'w', encoding='utf-8', newline='') as f:
    f.write(body)

with open('questions.json', encoding='utf-8') as f:
    data = json.load(f)
assert len(data) == len(data_check) + len(new_questions)
print('OK -- total de questoes agora:', len(data))
print('novo total BM:', sum(1 for q in data if q['corp'] == 'BM'))

with open('questions.json', encoding='utf-8') as f:
    qdata = f.read()
with open('app-template.html', encoding='utf-8') as f:
    html = f.read()
html = html.replace('__QUESTIONS_JSON__', qdata)
with open('estudo-cebraspe-ma.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('estudo-cebraspe-ma.html regenerado com sucesso')
