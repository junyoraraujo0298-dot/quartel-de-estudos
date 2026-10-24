# -*- coding: utf-8 -*-
# Regenera estudo-cebraspe-ma.html a partir do app-template.html apos a
# adicao do botao "Praticar questoes deste assunto" na aba Teoria (faltava
# so na Teoria; na Legislacao ja existia via lawPracticeBtn).
with open('questions.json', encoding='utf-8') as f:
    qdata_raw = f.read()
with open('app-template.html', encoding='utf-8') as f:
    html = f.read()
html = html.replace('__QUESTIONS_JSON__', qdata_raw)
with open('estudo-cebraspe-ma.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('estudo-cebraspe-ma.html regenerado com sucesso')
