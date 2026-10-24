# -*- coding: utf-8 -*-
# Converte os itens de Homonimos e Paronimos (deck Lingua Portuguesa
# PC-PE) de paragrafo corrido pra tabela (campo "tbl"), igual ja foi
# feito pra outras tabelas do app -- fica bem mais facil de ler uma
# lista de pares palavra/significado em tabela do que num paragrafo.
import json

with open('app-template.html', encoding='utf-8') as f:
    html = f.read()

OLD_HOMONIMOS = ('{"t": "art", "n": "Homônimos — grafia ou fonética iguais, significados diferentes", '
                  '"x": "Principais pares: acender (atear fogo)/ascender (subir); bucho (estômago de '
                  'animal)/buxo (arbusto); caçar (perseguir)/cassar (anular); cela (compartimento)/sela '
                  '(arreio); censo (recenseamento)/senso (juízo); cerração (nevoeiro)/serração (ato de '
                  'serrar); cidra (fruto)/sidra (vinho de maçã); concertar (harmonizar)/consertar '
                  '(reparar); insipiente (ignorante)/incipiente (iniciante); laço (nó)/lasso (frouxo); '
                  'paço (palácio)/passo (andar); seção (divisão, parte)/sessão (reunião); tacha '
                  '(prego)/taxa (imposto)."}')
assert OLD_HOMONIMOS in html, "item Homonimos nao encontrado como esperado"

OLD_PARONIMOS_1 = ('{"t": "art", "n": "Parônimos — grafia e pronúncia parecidas, significados '
                    'diferentes", "x": "Principais pares: absolver (perdoar)/absorver (consumir); '
                    'aprender (instruir-se)/apreender (assimilar); área (medida)/ária (peça musical); '
                    'arrear (pôr arreios)/arriar (abaixar); comprimento (extensão)/cumprimento '
                    '(saudação); costear (navegar junto à costa)/custear (financiar); deferir '
                    '(conceder)/diferir (adiar); degredado (exilado)/degradado (rebaixado); delatar '
                    '(denunciar)/dilatar (ampliar); descrição (descrever)/discrição (ser discreto); '
                    'descriminar (inocentar)/discriminar (distinguir); despensa (mantimentos)/dispensa '
                    '(isenção); despercebido (não percebido)/desapercebido (desprovido); discente '
                    '(aluno)/docente (professor); emergir (vir à tona)/imergir (mergulhar); emigrar '
                    '(sair do país)/imigrar (entrar no país); eminente (ilustre)/iminente (prestes a '
                    'acontecer)."}')
assert OLD_PARONIMOS_1 in html, "item Paronimos 1 nao encontrado como esperado"

OLD_PARONIMOS_2 = ('{"t": "art", "n": "Parônimos (continuação)", "x": "Mais pares: estufar '
                    '(aquecer)/estofar (encher); flagrante (evidente)/fragrante (perfumado); fluir '
                    '(correr)/fruir (desfrutar); imoral (contrário à moral)/amoral (nem a favor nem '
                    'contra a moral); indefeso (sem defesa)/indefesso (incansável); infligir '
                    '(aplicar)/infringir (transgredir); intimorato (corajoso)/intemerato (íntegro, '
                    'puro); mandato (procuração)/mandado (ordem judicial); pleito (demanda, '
                    'eleição)/preito (homenagem); precedente (antecedente)/procedente (proveniente); '
                    'prescrever (ordenar)/proscrever (condenar); recreação (diversão)/recriação (ato de '
                    'recriar); retificar (corrigir)/ratificar (confirmar); soar (produzir som)/suar '
                    '(transpirar); sortir (abastecer)/surtir (resultar); tráfego (trânsito)/tráfico '
                    '(comércio ilícito); vadear (atravessar o rio a pé)/vadiar (viver no ócio); vultoso '
                    '(de grande vulto)/vultuoso (inchado)."}')
assert OLD_PARONIMOS_2 in html, "item Paronimos 2 nao encontrado como esperado"

HOMONIMOS_PAIRS = [
    ("Acender", "atear fogo", "Ascender", "subir"),
    ("Bucho", "estômago de animal", "Buxo", "arbusto"),
    ("Caçar", "perseguir animais", "Cassar", "anular"),
    ("Cela", "compartimento", "Sela", "arreio para montar"),
    ("Censo", "recenseamento", "Senso", "raciocínio, juízo"),
    ("Cerração", "nevoeiro denso", "Serração", "ato de serrar"),
    ("Cidra", "fruto", "Sidra", "vinho de maçã"),
    ("Concertar", "harmonizar", "Consertar", "reparar"),
    ("Insipiente", "ignorante", "Incipiente", "iniciante"),
    ("Laço", "nó", "Lasso", "cansado, frouxo"),
    ("Paço", "palácio", "Passo", "andar"),
    ("Seção", "divisão, parte", "Sessão", "reunião"),
    ("Tacha", "pequeno prego", "Taxa", "imposto, tributo"),
]

PARONIMOS_PAIRS_1 = [
    ("Absolver", "perdoar, inocentar", "Absorver", "sorver, consumir"),
    ("Aprender", "instruir-se", "Apreender", "assimilar"),
    ("Área", "medida de superfície", "Ária", "peça musical"),
    ("Arrear", "pôr arreios", "Arriar", "abaixar"),
    ("Comprimento", "extensão", "Cumprimento", "saudação"),
    ("Costear", "navegar junto à costa", "Custear", "financiar"),
    ("Deferir", "conceder", "Diferir", "diferenciar, adiar"),
    ("Degredado", "desterrado, exilado", "Degradado", "rebaixado"),
    ("Delatar", "denunciar", "Dilatar", "alargar, ampliar"),
    ("Descrição", "ato de descrever", "Discrição", "qualidade de discreto"),
    ("Descriminar", "inocentar", "Discriminar", "distinguir"),
    ("Despensa", "lugar dos mantimentos", "Dispensa", "isenção"),
    ("Despercebido", "não percebido", "Desapercebido", "desprovido"),
    ("Discente", "relativo aos alunos", "Docente", "relativo aos professores"),
    ("Emergir", "vir à tona", "Imergir", "mergulhar"),
    ("Emigrar", "sair do país", "Imigrar", "entrar no país"),
    ("Eminente", "ilustre", "Iminente", "prestes a acontecer"),
]

PARONIMOS_PAIRS_2 = [
    ("Estufar", "aquecer com estufa", "Estofar", "encher"),
    ("Flagrante", "evidente", "Fragrante", "perfumado"),
    ("Fluir", "correr", "Fruir", "desfrutar"),
    ("Imoral", "contrário à moral", "Amoral", "nem a favor nem contra a moral"),
    ("Indefeso", "sem defesa", "Indefesso", "incansável"),
    ("Infligir", "aplicar", "Infringir", "transgredir, violar"),
    ("Intimorato", "corajoso, valente", "Intemerato", "íntegro, puro"),
    ("Mandato", "procuração", "Mandado", "ordem judicial"),
    ("Pleito", "demanda, eleição", "Preito", "homenagem, sujeição"),
    ("Precedente", "antecedente", "Procedente", "proveniente"),
    ("Prescrever", "ordenar, aconselhar", "Proscrever", "condenar, eliminar"),
    ("Recreação", "diversão", "Recriação", "ato de recriar"),
    ("Retificar", "corrigir", "Ratificar", "confirmar"),
    ("Soar", "produzir som", "Suar", "transpirar"),
    ("Sortir", "prover, abastecer", "Surtir", "resultar"),
    ("Tráfego", "trânsito, fluxo", "Tráfico", "comércio ilícito"),
    ("Vadear", "atravessar o rio a pé", "Vadiar", "viver no ócio"),
    ("Vultoso", "de grande vulto", "Vultuoso", "inchado"),
]

def build_item(n, search_x, pairs):
    header = ["Palavra", "Significado", "Palavra", "Significado"]
    rows = [[p[0], p[1], p[2], p[3]] for p in pairs]
    return {"t": "art", "n": n, "x": search_x, "tbl": [header] + rows}

NEW_HOMONIMOS = build_item(
    "Homônimos — grafia ou fonética iguais, significados diferentes",
    "Homônimos: acender/ascender, bucho/buxo, caçar/cassar, cela/sela, censo/senso, cerração/serração, "
    "cidra/sidra, concertar/consertar, insipiente/incipiente, laço/lasso, paço/passo, seção/sessão, "
    "tacha/taxa.",
    HOMONIMOS_PAIRS,
)
NEW_PARONIMOS_1 = build_item(
    "Parônimos — grafia e pronúncia parecidas, significados diferentes",
    "Parônimos: absolver/absorver, aprender/apreender, área/ária, arrear/arriar, "
    "comprimento/cumprimento, costear/custear, deferir/diferir, degredado/degradado, delatar/dilatar, "
    "descrição/discrição, descriminar/discriminar, despensa/dispensa, despercebido/desapercebido, "
    "discente/docente, emergir/imergir, emigrar/imigrar, eminente/iminente.",
    PARONIMOS_PAIRS_1,
)
NEW_PARONIMOS_2 = build_item(
    "Parônimos (continuação)",
    "Parônimos: estufar/estofar, flagrante/fragrante, fluir/fruir, imoral/amoral, indefeso/indefesso, "
    "infligir/infringir, intimorato/intemerato, mandato/mandado, pleito/preito, precedente/procedente, "
    "prescrever/proscrever, recreação/recriação, retificar/ratificar, soar/suar, sortir/surtir, "
    "tráfego/tráfico, vadear/vadiar, vultoso/vultuoso.",
    PARONIMOS_PAIRS_2,
)

html = html.replace(OLD_HOMONIMOS, json.dumps(NEW_HOMONIMOS, ensure_ascii=False), 1)
html = html.replace(OLD_PARONIMOS_1, json.dumps(NEW_PARONIMOS_1, ensure_ascii=False), 1)
html = html.replace(OLD_PARONIMOS_2, json.dumps(NEW_PARONIMOS_2, ensure_ascii=False), 1)

with open('app-template.html', 'w', encoding='utf-8', newline='') as f:
    f.write(html)
print('Homonimos e Paronimos convertidos pra tabela.')

with open('questions.json', encoding='utf-8') as f:
    qdata_raw = f.read()
with open('app-template.html', encoding='utf-8') as f:
    html2 = f.read()
html2 = html2.replace('__QUESTIONS_JSON__', qdata_raw)
with open('estudo-cebraspe-ma.html', 'w', encoding='utf-8') as f:
    f.write(html2)
print('estudo-cebraspe-ma.html regenerado com sucesso')
