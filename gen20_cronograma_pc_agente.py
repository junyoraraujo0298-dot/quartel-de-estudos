# -*- coding: utf-8 -*-
# Adiciona uma nova trilha de Teoria, especifica do corp PC, com o
# resumo do edital (estrutura da prova objetiva do cargo de Agente de
# Policia) e o cronograma/ciclo de estudos semanal fornecido pelo
# usuario.
import re

with open('app-template.html', encoding='utf-8') as f:
    html = f.read()

ITEMS = [
    {"t": "tit", "x": "EDITAL E CRONOGRAMA DE ESTUDOS — PCMA: CARGO DE AGENTE DE POLÍCIA"},
    {"t": "cap", "x": "O Que o Edital Informa (Estrutura da Prova Objetiva)"},
    {"t": "art", "n": "Distribuição oficial por prova",
     "x": "O edital divide a prova objetiva em apenas duas provas, sem detalhar por disciplina: "
          "P1 — Noções de Direito: 20 questões (33,3% da prova); P2 — Conhecimentos Específicos: "
          "40 questões (66,7% da prova). Total: 60 questões (100%).",
     "s": "Os Conhecimentos Específicos valem o DOBRO do Direito. Juntas, Português, Informática, "
          "Raciocínio Lógico, Contabilidade e Estatística pesam mais que todo o bloco de Direito — não "
          "subestime essas matérias só porque não soam \"jurídicas\"."},
    {"t": "cap", "x": "Estimativa de Questões por Disciplina (Não É Oficial)"},
    {"t": "art", "n": "Tabela estimada",
     "x": "Estimativa baseada em editais anteriores da banca, a confirmar quando sair o edital de "
          "convocação ou a prova anterior: Língua Portuguesa — 14 questões (23,3% da prova / 20% do "
          "tempo de estudo sugerido); Raciocínio Lógico — 9 (15,0% / 12%); Informática — 7 (11,7% / "
          "8%); Contabilidade Geral — 6 (10,0% / 7%); Estatística — 4 (6,7% / 4%); Direito Penal — 4 "
          "(6,7% / 10%); Direito Processual Penal — 4 (6,7% / 9%); Direito Constitucional — 4 (6,7% / "
          "9%); Direito Administrativo — 4 (6,7% / 8%); Legislação Estadual — 4 (6,7% / 8%); Redação e "
          "Atualidades — 30 pontos à parte (5% do tempo). Total: 60 questões (100% da prova / 100% do "
          "tempo).",
     "s": "Repare que o % de TEMPO DE ESTUDO não é igual ao % de QUESTÕES: Direito recebe mais tempo "
          "do que peso em questões (exige lei seca e memorização, além de ser base do cargo); "
          "Estatística e Informática recebem menos tempo (rendem rápido com treino de questões); "
          "Português fica no topo por ter mais questões e ser a mais \"garantida\" pra quem treina; "
          "Redação tem peso próprio (30 pontos, mínimo de 15 pra não ser eliminado)."},
    {"t": "cap", "x": "Notas de Corte"},
    {"t": "art", "n": "Pontuações mínimas",
     "x": "Objetivas: mínimo de 30 de 60 pontos (50%) — mas a classificação final é pela nota, então "
          "só atingir o mínimo não garante a aprovação. Redação: mínimo de 15 de 30 pontos. Só os "
          "candidatos mais bem colocados avançam para a prova discursiva (estimativa de 4.680 vagas na "
          "ampla concorrência) — por isso o alvo deve ser bem acima do mínimo, não só \"passar\".",
     "s": "Mínimo não é meta — é só o corte de eliminação. Para classificar entre os convocados pra "
          "discursiva, é preciso pontuar bem acima de 30/60."},
    {"t": "cap", "x": "Ciclo Semanal de Estudos (16h por semana)"},
    {"t": "art", "n": "Premissas do ciclo",
     "x": "Tempo disponível: 5 dias úteis × 2h = 10h, mais 6h no fim de semana (3h por dia), "
          "totalizando 16h por semana. Prazo: de 19/10/2026 até a prova em 7/3/2027 são cerca de 20 "
          "semanas, ou aproximadamente 320h de estudo. Os pesos usados seguem a estimativa de "
          "disciplinas do tópico anterior.",
     "s": "Se o fim de semana virar 6h POR DIA (12h no total), o ciclo semanal sobe pra 22h e a tabela "
          "de horas por disciplina precisa ser refeita proporcionalmente."},
    {"t": "art", "n": "Horas por disciplina no ciclo (16h)",
     "x": "Língua Portuguesa: 3h (18,8%). Raciocínio Lógico: 2h (12,5%). Informática: 1h30 (9,4%). "
          "Direito Penal: 1h30 (9,4%). Direito Processual Penal: 1h30 (9,4%). Direito Constitucional: "
          "1h30 (9,4%). Legislação Estadual: 1h30 (9,4%). Contabilidade Geral: 1h (6,3%). Direito "
          "Administrativo: 1h (6,3%). Redação e Atualidades: 1h (6,3%). Estatística: 0h30 (3,1%). "
          "Total: 16h (100%)."},
    {"t": "art", "n": "Distribuição por dia da semana",
     "x": "Segunda (2h): Português (1h) + Constitucional (1h). Terça (2h): Raciocínio Lógico (1h) + "
          "Penal (1h). Quarta (2h): Português (1h) + Legislação Estadual (1h). Quinta (2h): Processual "
          "Penal (1h) + Informática (1h). Sexta (2h): Raciocínio Lógico (1h) + Administrativo (1h). "
          "Sábado (3h): Português (1h) + Contabilidade (1h) + Estatística (30min) + Informática "
          "(30min). Domingo (3h): Redação (1h) + Penal (30min) + Processual Penal (30min) + "
          "Constitucional (30min) + Legislação Estadual (30min).",
     "s": "Se a rotina atrapalhar e um dia não der pra estudar, NÃO pule a matéria do dia — passe pro "
          "próximo bloco do ciclo e mantenha a ordem, sem tentar \"compensar\" tudo de uma vez depois."},
    {"t": "cap", "x": "Fases Até a Prova (19/10/2026 a 7/3/2027)"},
    {"t": "art", "n": "Fase 1 — Base (semanas 1 a 10, 19/10 a 27/12)",
     "x": "Foco: 60% teoria e 40% questões. Primeira passada em todo o edital, com resumos curtos de "
          "cada disciplina."},
    {"t": "art", "n": "Fase 2 — Questões (semanas 11 a 17, 28/12 a 14/2)",
     "x": "Foco: 30% teoria e 70% questões no estilo CEBRASPE. Revisão dos erros cometidos e "
          "aprofundamento na lei seca estadual."},
    {"t": "art", "n": "Fase 3 — Reta Final (semanas 18 a 20, 15/2 a 6/3)",
     "x": "Foco: simulados completos de 4 horas, revisão do caderno de erros e prática de redação."},
]

import json as _json
array_literal = '[\n' + ',\n'.join(_json.dumps(it, ensure_ascii=False) for it in ITEMS) + '\n]'

m = re.search(r'const TEORIA_COMBATE_INCENDIO\s*=\s*\[[\s\S]*?\n\];', html)
assert m, "bloco TEORIA_COMBATE_INCENDIO nao encontrado"
insertion_point = m.end()

new_block = '\n\nconst TEORIA_CRONOGRAMA_PC = ' + array_literal + ';'
new_html = html[:insertion_point] + new_block + html[insertion_point:]

old_teoria_decks_tail = '  hist: { label: "História do Maranhão", data: HIST_MA_LESSON, corp: null }\n};'
new_teoria_decks_tail = ('  hist: { label: "História do Maranhão", data: HIST_MA_LESSON, corp: null },\n'
                          '  cronograma_pc: { label: "Edital e Cronograma — PC Agente de Polícia", '
                          'data: TEORIA_CRONOGRAMA_PC, corp: "PC" }\n};')
assert old_teoria_decks_tail in new_html, "final de TEORIA_DECKS nao encontrado como esperado"
new_html = new_html.replace(old_teoria_decks_tail, new_teoria_decks_tail)

with open('app-template.html', 'w', encoding='utf-8', newline='') as f:
    f.write(new_html)
print('TEORIA_CRONOGRAMA_PC adicionada com', len(ITEMS), 'itens; registrada em TEORIA_DECKS (corp PC).')

with open('questions.json', encoding='utf-8') as f:
    qdata = f.read()
with open('app-template.html', encoding='utf-8') as f:
    html2 = f.read()
html2 = html2.replace('__QUESTIONS_JSON__', qdata)
with open('estudo-cebraspe-ma.html', 'w', encoding='utf-8') as f:
    f.write(html2)
print('estudo-cebraspe-ma.html regenerado com sucesso')
