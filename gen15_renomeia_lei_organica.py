# -*- coding: utf-8 -*-
# Renomeia o disc "Lei 14.751/2023 (Nacional - PM e BM)" para incluir
# explicitamente "Lei Organica", pois o usuario procurou por "lei
# organica" e nao achou -- a lei ja estava no app (LAW_14751 +
# questoes), so faltava esse termo no rotulo exibido.
import json

with open('questions.json', encoding='utf-8') as f:
    data = json.load(f)

OLD = "Lei 14.751/2023 (Nacional — PM e BM)"
NEW = "Lei 14.751/2023 (Lei Orgânica Nacional — PM e BM)"

changed = 0
for q in data:
    if q['disc'] == OLD:
        q['disc'] = NEW
        changed += 1

assert changed == 25, changed

lines = [json.dumps(q, ensure_ascii=False) for q in data]
body = '[' + lines[0]
for line in lines[1:]:
    body += '\r\n, ' + line
body += ']'

with open('questions.json', 'w', encoding='utf-8', newline='') as f:
    f.write(body)

with open('questions.json', encoding='utf-8') as f:
    check = json.load(f)
assert len(check) == len(data)
print('OK -- disc renomeado em', changed, 'questoes')

with open('questions.json', encoding='utf-8') as f:
    qdata = f.read()
with open('app-template.html', encoding='utf-8') as f:
    html = f.read()
html = html.replace('__QUESTIONS_JSON__', qdata)
with open('estudo-cebraspe-ma.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('estudo-cebraspe-ma.html regenerado com sucesso')
