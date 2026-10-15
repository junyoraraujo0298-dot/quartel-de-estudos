# -*- coding: utf-8 -*-
# Troca o campo "assunto" (criado pelo gen12) das questoes de legislacao
# pelo TITULO OFICIAL COMPLETO da lei, no mesmo formato em que aparece no
# proprio texto legal (campo "tit" dos arrays LAW_6513/LEI_12896/
# LAW_14751/LAW_10230) -- em vez do nome curto usado antes. Isso permite
# filtrar por "Assunto" usando a identificacao exata e oficial da lei.
import json

with open('questions.json', encoding='utf-8') as f:
    data = json.load(f)

DISC_TO_ASSUNTO = {
    # as 4 leis totalmente transcritas no app -- titulo oficial EXATO,
    # copiado do campo "tit" de LAW_6513 / LEI_12896 / LAW_14751 / LAW_10230
    "Estatuto da PM/MA (Lei 6.513/95)":
        "LEI Nº 6.513, DE 30 DE NOVEMBRO DE 1995 — Estatuto dos Policiais-Militares da Polícia "
        "Militar do Maranhão",
    "Lei 12.896/2026 (Organização Básica da PMMA)":
        "LEI Nº 12.896, DE 1º DE JUNHO DE 2026 — Dispõe sobre a organização básica da Polícia "
        "Militar do Maranhão, e dá outras providências",
    "Lei 14.751/2023 (Nacional — PM e BM)":
        "LEI Nº 14.751, DE 12 DE DEZEMBRO DE 2023 — Lei Orgânica Nacional das Polícias Militares e "
        "dos Corpos de Bombeiros Militares dos Estados, do Distrito Federal e dos Territórios",
    "Lei 10.230/2015 (Organização Básica do CBMMA)":
        "LEI Nº 10.230, DE 23 DE ABRIL DE 2015 — Organização Básica do Corpo de Bombeiros Militar "
        "do Maranhão (CBMMA)",

    # demais leis/codigos citados em questoes, no mesmo padrao de citacao oficial
    "Código Penal Militar (Decreto-Lei nº 1.001/1969)":
        "DECRETO-LEI Nº 1.001, DE 21 DE OUTUBRO DE 1969 — Código Penal Militar",
    "Estatuto da Criança e do Adolescente (Lei nº 8.069/1990)":
        "LEI Nº 8.069, DE 13 DE JULHO DE 1990 — Dispõe sobre o Estatuto da Criança e do Adolescente "
        "e dá outras providências",
    "Estatuto do Desarmamento (Lei nº 10.826/2003)":
        "LEI Nº 10.826, DE 22 DE DEZEMBRO DE 2003 — Dispõe sobre registro, posse e comercialização "
        "de armas de fogo e munição, define crimes e dá outras providências (Estatuto do "
        "Desarmamento)",
    "Estatuto do Idoso (Lei nº 10.741/2003)":
        "LEI Nº 10.741, DE 1º DE OUTUBRO DE 2003 — Dispõe sobre o Estatuto do Idoso e dá outras "
        "providências",
    "Lei de Abuso de Autoridade (Lei nº 13.869/2019)":
        "LEI Nº 13.869, DE 5 DE SETEMBRO DE 2019 — Dispõe sobre os crimes de abuso de autoridade",
    "Lei de Drogas (Lei nº 11.343/2006)":
        "LEI Nº 11.343, DE 23 DE AGOSTO DE 2006 — Institui o Sistema Nacional de Políticas Públicas "
        "sobre Drogas (Sisnad) e dá outras providências",
    "Lei de Execução Penal (Lei nº 7.210/1984)":
        "LEI Nº 7.210, DE 11 DE JULHO DE 1984 — Institui a Lei de Execução Penal",
    "Lei de Organização Criminosa (Lei nº 12.850/2013)":
        "LEI Nº 12.850, DE 2 DE AGOSTO DE 2013 — Define organização criminosa e dispõe sobre a "
        "investigação criminal, os meios de obtenção de prova, infrações penais correlatas e o "
        "procedimento criminal",
    "Lei Maria da Penha (Lei nº 11.340/2006)":
        "LEI Nº 11.340, DE 7 DE AGOSTO DE 2006 — Lei Maria da Penha: cria mecanismos para coibir a "
        "violência doméstica e familiar contra a mulher",
    "Direito Constitucional": "CONSTITUIÇÃO DA REPÚBLICA FEDERATIVA DO BRASIL DE 1988",
    "Direito Penal": "DECRETO-LEI Nº 2.848, DE 7 DE DEZEMBRO DE 1940 — Código Penal",
    "Direito Processual Penal": "DECRETO-LEI Nº 3.689, DE 3 DE OUTUBRO DE 1941 — Código de Processo "
        "Penal",

    # disciplinas sem lei/codigo especifico -- mantem o assunto = disciplina
    "Criminologia": "Criminologia",
    "Direito Administrativo": "Direito Administrativo",
    "Direitos Humanos": "Direitos Humanos",
    "Geografia do Brasil": "Geografia do Brasil",
    "Geografia do Maranhão": "Geografia do Maranhão",
    "História do Brasil": "História do Brasil",
    "História do Maranhão": "História do Maranhão",
    "Língua Estrangeira (Inglês)": "Língua Estrangeira (Inglês)",
    "Língua Portuguesa": "Língua Portuguesa",
    "Medicina Legal": "Medicina Legal",
    "Noções de Combate a Incêndio": "Noções de Combate a Incêndio",
    "Noções de Informática": "Noções de Informática",
    "Noções de Primeiros Socorros": "Noções de Primeiros Socorros",
    "Raciocínio Lógico": "Raciocínio Lógico",
    "Segurança Contra Incêndio e Pânico": "Segurança Contra Incêndio e Pânico",
}

discs_in_data = set(q['disc'] for q in data)
missing = discs_in_data - set(DISC_TO_ASSUNTO)
assert not missing, f"discs sem mapeamento de assunto: {missing}"

changed = 0
for q in data:
    novo = DISC_TO_ASSUNTO[q['disc']]
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
print('OK -- total de questoes:', len(check))
print('questoes com assunto atualizado:', changed)
from collections import Counter
for assunto, n in sorted(Counter(q['assunto'] for q in check).items()):
    print(f'  {n:4d}  {assunto}')

with open('questions.json', encoding='utf-8') as f:
    qdata = f.read()
with open('app-template.html', encoding='utf-8') as f:
    html = f.read()
html = html.replace('__QUESTIONS_JSON__', qdata)
with open('estudo-cebraspe-ma.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('estudo-cebraspe-ma.html regenerado com sucesso')
