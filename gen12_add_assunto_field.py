# -*- coding: utf-8 -*-
# Adiciona o campo "assunto" a TODAS as questoes do banco, habilitando o
# filtro "Assunto" (ate agora desabilitado na interface). Para disciplinas
# baseadas numa lei/codigo especifico, o assunto e o nome exato dessa
# norma; para disciplinas sem lei associada (Portugues, Historia,
# Geografia, Raciocinio Logico, Informatica, Direitos Humanos etc.), o
# assunto repete o nome da disciplina.
#
# Como TODA questao e alterada (novo campo em cada uma), este script
# recarrega e regrava o arquivo inteiro -- diferente dos scripts
# anteriores, que editavam so um subconjunto cirurgicamente. Para manter
# o arquivo legivel e facil de diferenciar (diff) no futuro, o formato de
# saida passa a ser uma questao por linha de forma consistente em todo o
# arquivo (hoje e uma linha gigante com as ~610 primeiras + uma questao
# por linha dai em diante).
import json

with open('questions.json', encoding='utf-8') as f:
    data = json.load(f)

DISC_TO_ASSUNTO = {
    # legislacao especifica -> nome exato da lei/codigo
    "Código Penal Militar (Decreto-Lei nº 1.001/1969)": "Código Penal Militar (Decreto-Lei nº 1.001/1969)",
    "Estatuto da Criança e do Adolescente (Lei nº 8.069/1990)": "Lei nº 8.069/1990 (Estatuto da Criança e do Adolescente)",
    "Estatuto da PM/MA (Lei 6.513/95)": "Lei nº 6.513/1995 (Estatuto da PM/MA)",
    "Estatuto do Desarmamento (Lei nº 10.826/2003)": "Lei nº 10.826/2003 (Estatuto do Desarmamento)",
    "Estatuto do Idoso (Lei nº 10.741/2003)": "Lei nº 10.741/2003 (Estatuto do Idoso)",
    "Lei 10.230/2015 (Organização Básica do CBMMA)": "Lei nº 10.230/2015 (Organização Básica do CBMMA)",
    "Lei 12.896/2026 (Organização Básica da PMMA)": "Lei nº 12.896/2026 (Organização Básica da PMMA)",
    "Lei 14.751/2023 (Nacional — PM e BM)": "Lei nº 14.751/2023 (Lei Orgânica Nacional das PMs e CBMs)",
    "Lei de Abuso de Autoridade (Lei nº 13.869/2019)": "Lei nº 13.869/2019 (Lei de Abuso de Autoridade)",
    "Lei de Drogas (Lei nº 11.343/2006)": "Lei nº 11.343/2006 (Lei de Drogas)",
    "Lei de Execução Penal (Lei nº 7.210/1984)": "Lei nº 7.210/1984 (Lei de Execução Penal)",
    "Lei de Organização Criminosa (Lei nº 12.850/2013)": "Lei nº 12.850/2013 (Lei das Organizações Criminosas)",
    "Lei Maria da Penha (Lei nº 11.340/2006)": "Lei nº 11.340/2006 (Lei Maria da Penha)",
    "Direito Constitucional": "Constituição Federal de 1988",
    "Direito Penal": "Código Penal (Decreto-Lei nº 2.848/1940)",
    "Direito Processual Penal": "Código de Processo Penal (Decreto-Lei nº 3.689/1941)",
    # disciplinas sem lei/codigo especifico -> repete a disciplina
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

for q in data:
    q['assunto'] = DISC_TO_ASSUNTO[q['disc']]

# reconstroi o arquivo, uma questao por linha, no mesmo estilo visual ja
# usado (", " antes de cada objeto, exceto o primeiro)
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
assert all('assunto' in q for q in check)
print('OK -- total de questoes:', len(check))
from collections import Counter
print(Counter(q['assunto'] for q in check))

with open('questions.json', encoding='utf-8') as f:
    qdata = f.read()
with open('app-template.html', encoding='utf-8') as f:
    html = f.read()
html = html.replace('__QUESTIONS_JSON__', qdata)
with open('estudo-cebraspe-ma.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('estudo-cebraspe-ma.html regenerado com sucesso')
