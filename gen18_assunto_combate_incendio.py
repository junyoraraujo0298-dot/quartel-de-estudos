# -*- coding: utf-8 -*-
# Torna o campo "assunto" das questoes de Nocoes de Combate a Incendio
# especifico por topico (igual ao padrao "DISCIPLINA: Combate a Incendio
# / ASSUNTO-TOPICO: 2. Processos de Combustao" usado nos PDFs Focados da
# Focus Concursos), em vez de repetir o nome da disciplina.
#
# Os topicos com PDF confirmado pelo usuario levam o numero oficial do
# PDF (2. Processos de Combustao; 3. Fases do Incendio). Os demais
# topicos (Teoria do Fogo, Classes de Incendio, Metodos de Extincao,
# Agentes Extintores) nao tiveram PDF fornecido ainda, entao ficam sem
# numero, so com o nome do topico -- pra nao inventar uma numeracao
# oficial que eu nao confirmei.
import json

with open('questions.json', encoding='utf-8') as f:
    data = json.load(f)

ASSUNTO_POR_ID = {
    155: "Teoria do Fogo",
    156: "Classes de Incêndio",
    157: "Classes de Incêndio",
    158: "Classes de Incêndio",
    159: "Agentes Extintores",
    366: "Classes de Incêndio",
    367: "Classes de Incêndio",
    368: "Teoria do Fogo",
    369: "Métodos de Extinção",
    370: "Métodos de Extinção",
    479: "Agentes Extintores",
    965: "2. Processos de Combustão",
    966: "2. Processos de Combustão",
    967: "2. Processos de Combustão",
    968: "2. Processos de Combustão",
    969: "2. Processos de Combustão",
    970: "2. Processos de Combustão",
    971: "2. Processos de Combustão",
    972: "2. Processos de Combustão",
    973: "2. Processos de Combustão",
    974: "2. Processos de Combustão",
    975: "3. Fases do Incêndio",
    976: "3. Fases do Incêndio",
    977: "3. Fases do Incêndio",
    978: "3. Fases do Incêndio",
    979: "3. Fases do Incêndio",
    980: "3. Fases do Incêndio",
    981: "3. Fases do Incêndio",
    982: "3. Fases do Incêndio",
    983: "3. Fases do Incêndio",
    984: "3. Fases do Incêndio",
}

disc_ids = set(q['id'] for q in data if q['disc'] == 'Noções de Combate a Incêndio')
assert disc_ids == set(ASSUNTO_POR_ID), disc_ids.symmetric_difference(set(ASSUNTO_POR_ID))

changed = 0
for q in data:
    if q['id'] in ASSUNTO_POR_ID:
        novo = ASSUNTO_POR_ID[q['id']]
        if q.get('assunto') != novo:
            q['assunto'] = novo
            changed += 1

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
print('OK -- assunto atualizado em', changed, 'questoes de Combate a Incendio')
from collections import Counter
for a, n in sorted(Counter(q['assunto'] for q in check if q['disc'] == 'Noções de Combate a Incêndio').items()):
    print(f'  {n:3d}  {a}')

with open('questions.json', encoding='utf-8') as f:
    qdata = f.read()
with open('app-template.html', encoding='utf-8') as f:
    html = f.read()
html = html.replace('__QUESTIONS_JSON__', qdata)
with open('estudo-cebraspe-ma.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('estudo-cebraspe-ma.html regenerado com sucesso')
