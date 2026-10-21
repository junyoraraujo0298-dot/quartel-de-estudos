# -*- coding: utf-8 -*-
# Troca o item "Distribuicao por dia da semana" do cronograma PC Agente
# de Policia (aba Estrategia) de um paragrafo corrido pra uma tabela
# (campo opcional "tbl": [cabecalho, ...linhas]), que o renderizador
# generico de deck (renderTeoria/renderEstrategia) agora sabe desenhar.
import json
import re

with open('app-template.html', encoding='utf-8') as f:
    html = f.read()

m = re.search(r'\{"t": "art", "n": "Distribuição por dia da semana"', html)
assert m, "item 'Distribuicao por dia da semana' nao encontrado"
start = m.start()
decoder = json.JSONDecoder()
obj, end = decoder.raw_decode(html, start)

assert obj['n'] == 'Distribuição por dia da semana'

obj['tbl'] = [
    ["Dia", "Horas", "Blocos de estudo"],
    ["Segunda", "2h", "Português (1h) + Constitucional (1h)"],
    ["Terça", "2h", "Raciocínio Lógico (1h) + Penal (1h)"],
    ["Quarta", "2h", "Português (1h) + Legislação Estadual (1h)"],
    ["Quinta", "2h", "Processual Penal (1h) + Informática (1h)"],
    ["Sexta", "2h", "Raciocínio Lógico (1h) + Administrativo (1h)"],
    ["Sábado", "3h", "Português (1h) + Contabilidade (1h) + Estatística (30min) + Informática (30min)"],
    ["Domingo", "3h", "Redação (1h) + Penal (30min) + Processual Penal (30min) + Constitucional (30min) + Legislação Estadual (30min)"],
]

new_obj_text = json.dumps(obj, ensure_ascii=False)
new_html = html[:start] + new_obj_text + html[end:]

with open('app-template.html', 'w', encoding='utf-8', newline='') as f:
    f.write(new_html)
print('OK -- campo tbl adicionado ao item Distribuicao por dia da semana')

with open('questions.json', encoding='utf-8') as f:
    qdata = f.read()
with open('app-template.html', encoding='utf-8') as f:
    html2 = f.read()
html2 = html2.replace('__QUESTIONS_JSON__', qdata)
with open('estudo-cebraspe-ma.html', 'w', encoding='utf-8') as f:
    f.write(html2)
print('estudo-cebraspe-ma.html regenerado com sucesso')
