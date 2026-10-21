# -*- coding: utf-8 -*-
# O conteudo de edital/cronograma que foi adicionado na aba Estrategia
# na verdade descreve a estrutura da PC-PE (Pernambuco), nao da PCMA
# (Maranhao) -- o usuario corrigiu isso explicitamente. Este script:
#   1) renomeia a const TEORIA_CRONOGRAMA_PC -> CRONOGRAMA_PCPE;
#   2) corrige o titulo do deck pra deixar claro que e PC-PE, com uma
#      nota explicando que serve so de referencia/modelo de metodo de
#      estudo, ja que os pesos/disciplinas da PCMA podem ser diferentes;
#   3) atualiza o label do deck em ESTRATEGIA_DECKS e solta o corp (nao
#      fica mais amarrado ao filtro corp=PC da MA, ja que o conteudo nao
#      e da MA).
import re

with open('app-template.html', encoding='utf-8') as f:
    html = f.read()

assert 'const TEORIA_CRONOGRAMA_PC = [' in html
html = html.replace('const TEORIA_CRONOGRAMA_PC = [', 'const CRONOGRAMA_PCPE = [', 1)

old_title = '{"t": "tit", "x": "EDITAL E CRONOGRAMA DE ESTUDOS — PCMA: CARGO DE AGENTE DE POLÍCIA"},'
new_title = ('{"t": "tit", "x": "EDITAL E CRONOGRAMA DE ESTUDOS — PC-PE (PERNAMBUCO): CARGO DE AGENTE DE '
             'POLÍCIA"},\n'
             '{"t": "art", "n": "Atenção: isto é da PC-PE, não da PCMA", '
             '"x": "Este cronograma usa como base o edital e a estrutura de prova da PC-PE (Pernambuco), '
             'não da PCMA (Maranhão) — está aqui como referência de método de estudo (como organizar um '
             'ciclo semanal, como interpretar peso de disciplina x tempo de estudo). As disciplinas, pesos '
             'e notas de corte da PCMA podem ser diferentes quando o edital de Maranhão sair.", '
             '"s": "Quando sair o edital oficial da PCMA, os números de questões por disciplina e as notas '
             'de corte devem ser ajustados — o que vale como modelo aqui é o MÉTODO (ciclo semanal, fases '
             'de estudo), não os números específicos da PE."},'
             )
assert old_title in html, "titulo antigo nao encontrado"
html = html.replace(old_title, new_title, 1)

old_deck_entry = ('  cronograma_pc: { label: "Edital e Cronograma — PC Agente de Polícia", '
                   'data: TEORIA_CRONOGRAMA_PC, corp: "PC" }')
new_deck_entry = ('  cronograma_pcpe: { label: "Edital e Cronograma — PC-PE (Pernambuco), Agente de '
                   'Polícia", data: CRONOGRAMA_PCPE, corp: null }')
assert old_deck_entry in html, "entrada antiga de ESTRATEGIA_DECKS nao encontrada"
html = html.replace(old_deck_entry, new_deck_entry, 1)

assert 'state.estrategiaDeck = "cronograma_pc";' in html
html = html.replace('state.estrategiaDeck = "cronograma_pc";', 'state.estrategiaDeck = "cronograma_pcpe";', 1)

with open('app-template.html', 'w', encoding='utf-8', newline='') as f:
    f.write(html)
print('OK -- deck renomeado pra cronograma_pcpe, titulo e nota de alerta corrigidos')

with open('questions.json', encoding='utf-8') as f:
    qdata = f.read()
with open('app-template.html', encoding='utf-8') as f:
    html2 = f.read()
html2 = html2.replace('__QUESTIONS_JSON__', qdata)
with open('estudo-cebraspe-ma.html', 'w', encoding='utf-8') as f:
    f.write(html2)
print('estudo-cebraspe-ma.html regenerado com sucesso')
