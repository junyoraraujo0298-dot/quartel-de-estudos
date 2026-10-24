# -*- coding: utf-8 -*-
# Adiciona conteudo de Lingua Portuguesa (Dominio da ortografia
# oficial/acentuacao) pra PC-PE: um deck de teoria na aba Teoria
# (corp PCPE) resumindo as regras de acentuacao grafica, e as 6
# questoes Certo/Errado do material da Focus Concursos sobre o tema.
# Fonte: "Slides-Lingua-Portuguesa-Maria-Augusta-Material-Dominio-da-
# Ortografia.pdf", Profa. Maria Augusta G. Almeida, Focus Concursos.
#
# OBS: por decisao explicita do usuario (confirmada via pergunta), as
# questoes de PC-PE continuam no formato Certo/Errado (tipo "CE"),
# igual ao Direito Penal ja adicionado -- nao convertidas pra MC.
import re
import json

with open('app-template.html', encoding='utf-8') as f:
    html = f.read()

TEORIA_ITEMS = [
    {"t": "tit", "x": "LÍNGUA PORTUGUESA — DOMÍNIO DA ORTOGRAFIA OFICIAL / ACENTUAÇÃO (PC-PE)"},
    {"t": "art", "n": "Regra 1 — Oxítonas",
     "x": "Acentuam-se as OXÍTONAS terminadas em A(S), E(S), O(S), EM, ENS.",
     "s": "Ex.: sabiás, também, revês, compôs, ninguém, intervéns, atrás, até."},
    {"t": "art", "n": "Regra 2 — Paroxítonas",
     "x": "Acentuam-se as PAROXÍTONAS terminadas em: R, N, L, X, I(S), US, UM(S), ON(S), Ã(S), PS, DITONGOS.",
     "s": "Ex.: éter, pólen, móvel, tórax, júri, bônus, álbuns, nêutrons, bíceps, mídia."},
    {"t": "art", "n": "Paroxítonas terminadas em ditongo crescente — atenção",
     "x": "As paroxítonas terminadas em ditongo crescente podem ser consideradas proparoxítonas eventuais, "
          "dependendo de como se separa a sílaba: frequência = fre-quên-cia (paroxítona terminada em "
          "ditongo) OU fre-quên-ci-a (proparoxítona). Mesma lógica para história = his-tó-ria OU "
          "his-tó-ri-a. De qualquer forma, o acento é obrigatório nos dois casos."},
    {"t": "art", "n": "Regra 3 — Proparoxítonas",
     "x": "Acentuam-se TODAS as PROPAROXÍTONAS, sem exceção.",
     "s": "Ex.: página, tímido, médico, trânsito, córrego, pedíssemos, lâmpada."},
    {"t": "art", "n": "Regra 4 — Monossílabos tônicos",
     "x": "Acentuam-se os MONOSSÍLABOS TÔNICOS terminados em A(S), E(S), O(S).",
     "s": "Ex.: sós, nós, vês, lá, pás, nó, prós."},
    {"t": "art", "n": "Regra 5 — Ditongos abertos ÉI, ÓI, ÉU",
     "x": "Acentuam-se os ditongos abertos ÉI(S), ÓI(S), ÉU(S) quando estão na sílaba tônica de uma "
          "OXÍTONA ou de um MONOSSÍLABO TÔNICO. Ex.: carretéis, troféu, lençóis, papéis, destrói, sóis, "
          "véu. Atenção: quando esses mesmos ditongos abertos estão na sílaba tônica de uma PAROXÍTONA, "
          "NÃO recebem mais acento (reforma ortográfica).",
     "s": "Ex. de paroxítonas que perderam o acento: ideia, apoio (verbo), joia, apneia, assembleia, boia."},
    {"t": "art", "n": "Regra 6 — Hiato tônico com I e U",
     "x": "Acentuam-se o I e o U, quando TÔNICOS, formando hiato com a vogal anterior, desde que estejam "
          "sozinhos na sílaba ou seguidos apenas de S. Ex.: saída, moído, prejuízo, cairmos, faísca, "
          "saúde, baú, caju, caindo, moinho, bainha, egoísta. ATENÇÃO: quando esse I ou U tônico é "
          "seguido de NH, não recebe acento (moinho, bainha). Nas OXÍTONAS, o acento no i/u tônico "
          "permanece mesmo havendo ditongo antes dele — por isso se escreve Piauí, tuiuiú."},
    {"t": "art", "n": "Hiatos EEM e OO — sem acento",
     "x": "Desde o Novo Acordo Ortográfico, os hiatos EEM e OO não recebem mais acento. Ex.: magoo, "
          "enjoo, abençoo, perdoo, leem, creem, veem."},
    {"t": "art", "n": "Fim do trema",
     "x": "O trema foi extinto na ortografia oficial — não se usa mais em nenhuma palavra. Ex.: "
          "linguiça, frequente, consequência, aguentar (antes: lingüiça, freqüente, conseqüência, "
          "agüentar)."},
    {"t": "art", "n": "Acentos diferenciais",
     "x": "PÔDE (pretérito perfeito, passado) × PODE (presente do indicativo). PÔR (verbo) × POR "
          "(preposição)."},
    {"t": "art", "n": "Verbos TER e VIR (3ª pessoa)",
     "x": "Verbo TER: ele tem (singular, sem acento) / eles têm (plural, com acento circunflexo). Verbo "
          "VIR: ele vem (singular, sem acento) / eles vêm (plural, com acento circunflexo)."},
    {"t": "art", "n": "Derivados de TER e VIR",
     "x": "O mesmo padrão (singular sem acento / plural com acento) vale para os verbos derivados de TER "
          "e VIR. Ex.: OBTER — ele obtém / eles obtêm. INTERVIR — ele intervém / eles intervêm. Outros "
          "exemplos comuns: manter (ele mantém/eles mantêm), conter (contém/contêm), convir "
          "(convém/convêm)."},
]

CE_QUESTIONS = [
    ("A eliminação do acento gráfico na palavra “hieróglifos” não geraria incorreção no texto.",
     False, "Regra 3 — Proparoxítonas",
     "Errado — “hieróglifos” é proparoxítona (hi-e-RÓ-gli-fos, sílaba tônica antepenúltima), "
     "e todas as proparoxítonas são obrigatoriamente acentuadas (Regra 3). Remover o acento tornaria a "
     "grafia incorreta."),
    ("No trecho “A inteligência artificial (IA) tem desempenhado papel cada vez mais importante nos "
     "últimos anos”, a flexão da forma verbal “tem” no plural — têm — prejudicaria a "
     "correção gramatical do texto.", True, "Verbos TER e VIR (3ª pessoa)",
     "Correto — o sujeito “A inteligência artificial (IA)” é singular, exigindo a forma verbal "
     "singular “tem” (sem acento); flexionar para o plural “têm” quebraria a "
     "concordância verbal e, portanto, prejudicaria a correção do texto."),
    ("Os vocábulos “próprio”, “ciência” e “área” são acentuados "
     "graficamente de acordo com a mesma regra de acentuação gráfica.", False,
     "Paroxítonas terminadas em ditongo crescente",
     "Errado — “próprio” e “ciência” são paroxítonas terminadas em ditongo (Regra 2), "
     "mas “área” (Á-re-a) é proparoxítona, acentuada pela Regra 3 — não seguem, portanto, a "
     "mesma regra."),
    ("As palavras “pirólise” e “agrícolas” são acentuadas graficamente de acordo com "
     "a mesma regra de acentuação gráfica.", True, "Regra 3 — Proparoxítonas",
     "Correto — ambas são proparoxítonas (pi-RÓ-li-se e a-GRÍ-co-las, sílaba tônica antepenúltima nas "
     "duas), acentuadas pela mesma Regra 3."),
    ("Os vocábulos “república” e “cárcere” são acentuados graficamente de acordo com "
     "a mesma regra de acentuação gráfica.", True, "Regra 3 — Proparoxítonas",
     "Correto — ambas são proparoxítonas (re-PÚ-bli-ca e CÁR-ce-re, sílaba tônica antepenúltima nas "
     "duas), acentuadas pela mesma Regra 3."),
    ("Os vocábulos “semântico”, “sintático” e “linguísticas” são "
     "acentuados graficamente de acordo com a regra de acentuação gráfica das palavras proparoxítonas.",
     True, "Regra 3 — Proparoxítonas",
     "Correto — nos três casos a sílaba tônica é a antepenúltima (se-MÂN-ti-co, sin-TÁ-ti-co, "
     "lin-GUÍS-ti-cas), caracterizando proparoxítonas, acentuadas pela Regra 3."),
    ("Os vocábulos “língua” e “história” são acentuados graficamente em razão da "
     "regra que determina que se acentuem palavras paroxítonas terminadas em ditongo crescente, "
     "seguido, ou não, de s.", True, "Paroxítonas terminadas em ditongo crescente",
     "Correto — “língua” (LÍN-gua) é paroxítona terminada em ditongo crescente “ua”, "
     "e “história” (his-TÓ-ria) se enquadra na mesma regra, sendo também classificável como "
     "paroxítona terminada em ditongo crescente “ia” (ainda que também admita leitura como "
     "proparoxítona: his-tó-ri-a)."),
]

decoder = json.JSONDecoder()

# -------------------- insere o deck de teoria --------------------
array_literal = '[\n' + ',\n'.join(json.dumps(it, ensure_ascii=False) for it in TEORIA_ITEMS) + '\n]'

m = re.search(r'const TEORIA_DIREITO_PENAL_PCPE\s*=\s*\[', html)
assert m, "bloco TEORIA_DIREITO_PENAL_PCPE nao encontrado"
start = m.end() - 1
_arr, end = decoder.raw_decode(html, start)
insertion_point = end + 1  # depois do ';'
new_block = '\n\nconst TEORIA_LINGUA_PORTUGUESA_PCPE = ' + array_literal + ';'
html = html[:insertion_point] + new_block + html[insertion_point:]

old_teoria_tail = ('  direito_penal_pcpe: { label: "Direito Penal — Princípios (PC-PE)", '
                   'data: TEORIA_DIREITO_PENAL_PCPE, corp: "PCPE" }\n};')
assert old_teoria_tail in html, "final de TEORIA_DECKS nao encontrado como esperado"
new_teoria_tail = ('  direito_penal_pcpe: { label: "Direito Penal — Princípios (PC-PE)", '
                   'data: TEORIA_DIREITO_PENAL_PCPE, corp: "PCPE" },\n'
                   '  portugues_pcpe: { label: "Língua Portuguesa — Ortografia e Acentuação (PC-PE)", '
                   'data: TEORIA_LINGUA_PORTUGUESA_PCPE, corp: "PCPE" }\n};')
html = html.replace(old_teoria_tail, new_teoria_tail, 1)

old_disc_map_tail = ('const TEORIA_DECK_TO_DISC = {\n'
                      '  direito_penal_pcpe: "Direito Penal"\n'
                      '};')
assert old_disc_map_tail in html, "TEORIA_DECK_TO_DISC nao encontrado como esperado"
new_disc_map_tail = ('const TEORIA_DECK_TO_DISC = {\n'
                      '  direito_penal_pcpe: "Direito Penal",\n'
                      '  portugues_pcpe: "Língua Portuguesa"\n'
                      '};')
html = html.replace(old_disc_map_tail, new_disc_map_tail, 1)

with open('app-template.html', 'w', encoding='utf-8', newline='') as f:
    f.write(html)
print('TEORIA_LINGUA_PORTUGUESA_PCPE adicionada com', len(TEORIA_ITEMS), 'itens; registrada em TEORIA_DECKS e TEORIA_DECK_TO_DISC.')

# -------------------- insere as questoes --------------------
with open('questions.json', encoding='utf-8') as f:
    qdata = json.load(f)

next_id = max(q['id'] for q in qdata) + 1
added = 0
for enun, resp, assunto, exp in CE_QUESTIONS:
    qdata.append({
        "id": next_id,
        "corp": "PCPE",
        "disc": "Língua Portuguesa",
        "assunto": assunto,
        "tipo": "CE",
        "enun": enun,
        "resp": resp,
        "exp": exp,
    })
    next_id += 1
    added += 1

lines = [json.dumps(q, ensure_ascii=False) for q in qdata]
body = '[' + lines[0]
for line in lines[1:]:
    body += '\r\n, ' + line
body += ']'

with open('questions.json', 'w', encoding='utf-8', newline='') as f:
    f.write(body)

with open('questions.json', encoding='utf-8') as f:
    check = json.load(f)
assert len(check) == len(qdata)
print('OK --', added, 'questoes de Língua Portuguesa (PC-PE) adicionadas. Total no banco:', len(check))

# -------------------- regenera o HTML final --------------------
with open('questions.json', encoding='utf-8') as f:
    qdata_raw = f.read()
with open('app-template.html', encoding='utf-8') as f:
    html2 = f.read()
html2 = html2.replace('__QUESTIONS_JSON__', qdata_raw)
with open('estudo-cebraspe-ma.html', 'w', encoding='utf-8') as f:
    f.write(html2)
print('estudo-cebraspe-ma.html regenerado com sucesso')
