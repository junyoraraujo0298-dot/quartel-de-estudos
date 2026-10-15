# -*- coding: utf-8 -*-
# Corrige o rotulo "disc" (e complementa o "exp" com o artigo exato, quando
# identificavel) das questoes que hoje estao sob rotulos genericos demais
# para uma categoria de legislacao: "Legislacao Institucional PM" (PM),
# "Legislacao Institucional" (BM) e "Legislacao Especial" (PC).
#
# Cada questao foi conferida manualmente contra o texto das leis ja
# presentes no app (LAW_6513, LAW_14751, LAW_10230) ou contra a lei citada
# no proprio enunciado (caso da antiga "Legislacao Especial"). Onde o
# artigo exato foi identificado, ele e acrescentado ao campo "exp".
#
# Para nao reformatar o restante do arquivo (que mistura uma linha unica
# gigante -- ids 1..~610 -- com uma questao por linha para ids maiores),
# este script localiza cada objeto pelo id, usando json.JSONDecoder
# .raw_decode para achar o span exato do objeto no texto bruto, e
# substitui SOMENTE esse trecho, preservando tudo o mais.
import json
import re

with open('questions.json', encoding='utf-8') as f:
    raw = f.read()

# id -> (disc_esperado_atual, novo_disc, sufixo_exp_ou_None, (old_enun_substr, new_enun_substr)_ou_None)
FIXES = {
    # --- PM: "Legislação Institucional PM" ---
    87:  ("Legislação Institucional PM", "Estatuto da PM/MA (Lei 6.513/95)", " (art. 17, §§1º e 2º, da Lei nº 6.513/95).", None),
    88:  ("Legislação Institucional PM", "Direito Constitucional", " (art. 144, §6º, c/c art. 42, CF).", None),
    89:  ("Legislação Institucional PM", "Estatuto da PM/MA (Lei 6.513/95)", " (arts. 55 e 58-59 da Lei nº 6.513/95).", None),
    90:  ("Legislação Institucional PM", "Estatuto da PM/MA (Lei 6.513/95)", " (art. 19 da Lei nº 6.513/95).", None),
    91:  ("Legislação Institucional PM", "Direito Constitucional", None, None),  # ja cita art. 37, XVI/XVII, CF
    92:  ("Legislação Institucional PM", "Estatuto da PM/MA (Lei 6.513/95)", " (art. 78 da Lei nº 6.513/95).", None),
    93:  ("Legislação Institucional PM", "Estatuto da PM/MA (Lei 6.513/95)", " (art. 56 da Lei nº 6.513/95).", None),
    94:  ("Legislação Institucional PM", "Direitos Humanos", None, None),
    95:  ("Legislação Institucional PM", "Estatuto da PM/MA (Lei 6.513/95)", " (art. 59 da Lei nº 6.513/95).", None),
    96:  ("Legislação Institucional PM", "Estatuto da PM/MA (Lei 6.513/95)", " (art. 17, §2º, da Lei nº 6.513/95).", None),
    97:  ("Legislação Institucional PM", "Direito Constitucional", None, None),  # ja cita art. 144, §5º e §6º, CF
    98:  ("Legislação Institucional PM", "Estatuto da PM/MA (Lei 6.513/95)", " (art. 17, §3º, da Lei nº 6.513/95).", None),
    99:  ("Legislação Institucional PM", "Estatuto da PM/MA (Lei 6.513/95)", " (arts. 20 e 21 da Lei nº 6.513/95).", None),
    100: ("Legislação Institucional PM", "Estatuto da PM/MA (Lei 6.513/95)", " (art. 9º da Lei nº 6.513/95).",
          ("idade entre 18 e 35 anos", "idade máxima de 30 anos")),
    101: ("Legislação Institucional PM", "Lei 14.751/2023 (Nacional — PM e BM)", " (art. 13, VI, da Lei nº 14.751/2023).", None),
    407: ("Legislação Institucional PM", "Estatuto da PM/MA (Lei 6.513/95)", " (art. 40 da Lei nº 6.513/95).", None),
    408: ("Legislação Institucional PM", "Direito Constitucional", None, None),  # ja cita art. 144, §6º, CF
    409: ("Legislação Institucional PM", "Estatuto da PM/MA (Lei 6.513/95)", " (arts. 55 e 59 da Lei nº 6.513/95).", None),
    410: ("Legislação Institucional PM", "Estatuto da PM/MA (Lei 6.513/95)", " (art. 59 da Lei nº 6.513/95).", None),
    411: ("Legislação Institucional PM", "Estatuto da PM/MA (Lei 6.513/95)", " (art. 64, §2º, da Lei nº 6.513/95).", None),
    412: ("Legislação Institucional PM", "Estatuto da PM/MA (Lei 6.513/95)", " (art. 40 da Lei nº 6.513/95).", None),
    413: ("Legislação Institucional PM", "Estatuto da PM/MA (Lei 6.513/95)", " (art. 102, parágrafo único, da Lei nº 6.513/95).", None),
    414: ("Legislação Institucional PM", "Código Penal Militar (Decreto-Lei nº 1.001/1969)", " (Decreto-Lei nº 1.001/1969 — Código Penal Militar).", None),
    415: ("Legislação Institucional PM", "Estatuto da PM/MA (Lei 6.513/95)", " (art. 17, §2º, da Lei nº 6.513/95).", None),
    416: ("Legislação Institucional PM", "Lei 14.751/2023 (Nacional — PM e BM)", " (art. 5º, V e VI, da Lei nº 14.751/2023).", None),
    492: ("Legislação Institucional PM", "Estatuto da PM/MA (Lei 6.513/95)", " (art. 116 da Lei nº 6.513/95).", None),

    # --- BM: "Legislação Institucional" ---
    145: ("Legislação Institucional", "Direito Constitucional", None, None),  # ja cita art. 42 c/c art. 144, §6º, CF
    146: ("Legislação Institucional", "Estatuto da PM/MA (Lei 6.513/95)", " (arts. 55 e 58-59 da Lei nº 6.513/95, aplicável ao CBMMA por força do art. 167).", None),
    147: ("Legislação Institucional", "Estatuto da PM/MA (Lei 6.513/95)", " (art. 17, §2º, da Lei nº 6.513/95, aplicável ao CBMMA por força do art. 167).", None),
    148: ("Legislação Institucional", "Direito Constitucional", None, None),  # ja cita art. 144, §5º, CF
    149: ("Legislação Institucional", "Direito Constitucional", None, None),  # ja cita art. 37, XVI/XVII, CF
    356: ("Legislação Institucional", "Lei 14.751/2023 (Nacional — PM e BM)", " (art. 13 da Lei nº 14.751/2023).", None),
    357: ("Legislação Institucional", "Estatuto da PM/MA (Lei 6.513/95)", " (art. 59 da Lei nº 6.513/95, aplicável ao CBMMA por força do art. 167).", None),
    358: ("Legislação Institucional", "Lei 14.751/2023 (Nacional — PM e BM)", " (art. 14 da Lei nº 14.751/2023).", None),
    359: ("Legislação Institucional", "Estatuto da PM/MA (Lei 6.513/95)", " (art. 16 da Lei nº 6.513/95, aplicável ao CBMMA por força do art. 167).", None),
    360: ("Legislação Institucional", "Estatuto da PM/MA (Lei 6.513/95)", " (art. 17 da Lei nº 6.513/95, aplicável ao CBMMA por força do art. 167).", None),
    453: ("Legislação Institucional", "Estatuto da PM/MA (Lei 6.513/95)", " (art. 9º da Lei nº 6.513/95, aplicável ao CBMMA por força do art. 56 da Lei nº 10.230/2015).",
          ("idade mínima de 18 anos e idade máxima em torno de 35 anos", "idade mínima de 18 anos e idade máxima de 30 anos")),  # ocorre em exp E em alts[1]
    454: ("Legislação Institucional", "Lei 10.230/2015 (Organização Básica do CBMMA)", " (art. 2º da Lei nº 10.230/2015).", None),
    481: ("Legislação Institucional", "Lei 14.751/2023 (Nacional — PM e BM)", " (art. 13, VII, da Lei nº 14.751/2023).", None),

    # --- PC: "Legislação Especial" (a lei ja e citada no proprio enunciado) ---
    205: ("Legislação Especial", "Lei de Abuso de Autoridade (Lei nº 13.869/2019)", None, None),
    206: ("Legislação Especial", "Lei Maria da Penha (Lei nº 11.340/2006)", None, None),
    207: ("Legislação Especial", "Estatuto da Criança e do Adolescente (Lei nº 8.069/1990)", None, None),
    403: ("Legislação Especial", "Lei de Drogas (Lei nº 11.343/2006)", None, None),
    404: ("Legislação Especial", "Lei de Organização Criminosa (Lei nº 12.850/2013)", None, None),
    405: ("Legislação Especial", "Estatuto do Desarmamento (Lei nº 10.826/2003)", None, None),
    406: ("Legislação Especial", "Lei Maria da Penha (Lei nº 11.340/2006)", None, None),
    476: ("Legislação Especial", "Lei de Abuso de Autoridade (Lei nº 13.869/2019)", None, None),
    477: ("Legislação Especial", "Estatuto do Idoso (Lei nº 10.741/2003)", None, None),
    499: ("Legislação Especial", "Lei de Execução Penal (Lei nº 7.210/1984)", None, None),
}

assert len(FIXES) == 49, len(FIXES)

decoder = json.JSONDecoder()
replacements = []  # (start, end, new_text)

for qid, (old_disc, new_disc, exp_suffix, enun_fix) in FIXES.items():
    m = re.search(r'\{"id":\s*%d,' % qid, raw)
    if not m:
        raise SystemExit(f"id {qid} nao encontrado no questions.json")
    start = m.start()
    obj, end = decoder.raw_decode(raw, start)  # end = indice absoluto logo apos o "}"

    assert obj['id'] == qid
    assert obj['disc'] == old_disc, f"id {qid}: disc atual é {obj['disc']!r}, esperado {old_disc!r}"

    if enun_fix:
        old_sub, new_sub = enun_fix
        found = False
        if old_sub in obj.get('enun', ''):
            obj['enun'] = obj['enun'].replace(old_sub, new_sub)
            found = True
        if old_sub in obj.get('exp', ''):
            obj['exp'] = obj['exp'].replace(old_sub, new_sub)
            found = True
        if 'alts' in obj:
            for i, alt in enumerate(obj['alts']):
                if old_sub in alt:
                    obj['alts'][i] = alt.replace(old_sub, new_sub)
                    found = True
        assert found, f"id {qid}: trecho {old_sub!r} nao encontrado em enun/exp/alts"

    obj['disc'] = new_disc
    if exp_suffix and not exp_suffix.strip('.() ') in obj['exp']:
        obj['exp'] = obj['exp'].rstrip() + exp_suffix

    new_text = json.dumps(obj, ensure_ascii=False)
    replacements.append((start, end, new_text))

# aplica de tras pra frente para nao invalidar os indices anteriores
replacements.sort(key=lambda t: t[0], reverse=True)
new_raw = raw
for start, end, new_text in replacements:
    new_raw = new_raw[:start] + new_text + new_raw[end:]

with open('questions.json', 'w', encoding='utf-8', newline='') as f:
    f.write(new_raw)

# validacao final
with open('questions.json', encoding='utf-8') as f:
    data = json.load(f)
print('OK -- total de questoes:', len(data))
remaining = [q['id'] for q in data if q['disc'] in ('Legislação Institucional PM', 'Legislação Institucional', 'Legislação Especial')]
print('ids ainda com disc generico (deveria ser vazio):', remaining)
from collections import Counter
print(Counter(q['disc'] for q in data if q['id'] in FIXES))

# regenera o html final
with open('questions.json', encoding='utf-8') as f:
    qdata = f.read()
with open('app-template.html', encoding='utf-8') as f:
    html = f.read()
html = html.replace('__QUESTIONS_JSON__', qdata)
with open('estudo-cebraspe-ma.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('estudo-cebraspe-ma.html regenerado com sucesso')
