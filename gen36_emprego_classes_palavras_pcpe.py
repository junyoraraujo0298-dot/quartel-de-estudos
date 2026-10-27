# -*- coding: utf-8 -*-
# Complementa o deck de Lingua Portuguesa (PC-PE) com o conteudo do
# material "Emprego das Classes de Palavras" (as 10 classes
# gramaticais, pronomes, numeral, adverbio, preposicao, conjuncao,
# interjeicao) e adiciona questoes de multipla escolha (regra atual
# pro PC-PE: tipo MC, nao CE -- ver memoria
# feedback_quartel_estudos_pcpe_formato_prova). 6 das 10 questoes do
# material sao reformuladas em MC a partir do texto de Gottlob Frege
# ("Pensamentos compostos") dado nos slides; as outras 3 questoes do
# material (sobre "o todo se torne algo mais...", "pianista
# austriaco" e "varios temas") referenciam um trecho do texto que
# NAO veio incluido nesta extracao do PDF -- foram deixadas de fora
# pra nao arriscar fabricar gabarito sem a fonte.
import re
import json

with open('app-template.html', encoding='utf-8') as f:
    html = f.read()

NEW_ITEMS = [
    {"t": "sec", "x": "Emprego das classes de palavras"},
    {"t": "art", "n": "As 10 classes gramaticais",
     "x": "São dez as classes gramaticais (ou classes morfológicas): seis variáveis e quatro "
          "invariáveis.",
     "tbl": [["Variáveis (6)", "Invariáveis (4)"],
             ["Artigo", "Advérbio"],
             ["Substantivo", "Conjunção"],
             ["Adjetivo", "Preposição"],
             ["Verbo", "Interjeição"],
             ["Pronome", ""],
             ["Numeral", ""]]},
    {"t": "art", "n": "Artigo, Substantivo e Adjetivo",
     "x": "ARTIGO: palavra que se coloca antes do substantivo, definindo-o, determinando-o e "
          "indicando seu gênero e número. Definidos: o, a, os, as. Indefinidos: um, uma, uns, "
          "umas. SUBSTANTIVO: palavra que designa os seres — objetos, pessoas, lugares etc. "
          "(ex.: juiz, livro, Paula, Paris, alegria, esperança). ADJETIVO: modificador do "
          "substantivo, aquilo que o caracteriza ou qualifica (ex.: alegre, novo, caridoso, "
          "esperançoso, alto, forte)."},
    {"t": "art", "n": "Verbo",
     "x": "Palavra variável que exprime uma ação ou um estado (ex.: ler, cantar, ser, estar, "
          "pensar)."},
    {"t": "art", "n": "Pronomes — tipos",
     "x": "Pronomes são elementos que acompanham os substantivos ou os substituem. Dividem-se em "
          "sete tipos.",
     "tbl": [["Tipo", "Exemplos"],
             ["Pessoais retos", "eu, tu, ele, ela, nós, vós, eles, elas"],
             ["Pessoais oblíquos", "me, mim, comigo, te, ti, contigo, se, si, consigo, nos, "
              "conosco, vos, convosco, o, a, os, as, lhe, lhes"],
             ["De tratamento", "você, senhor, senhora, Vossa Excelência, Vossa Majestade, Vossa "
              "Eminência, Vossa Alteza, Vossa Reverendíssima, Vossa Magnificência, Vossa "
              "Santidade, Vossa Senhoria"],
             ["Possessivos", "meu(s)/minha(s), teu(s)/tua(s), seu(s)/sua(s), nosso(s)/nossa(s), "
              "vosso(s)/vossa(s)"],
             ["Demonstrativos", "este/esta/estes/estas, esse/essa/esses/essas, "
              "aquele/aquela/aqueles/aquelas, isto/isso/aquilo, o/a/os/as — tal, mesmo, "
              "semelhante e próprio também podem funcionar como demonstrativos"],
             ["Relativos", "que, quem, onde, o qual, a qual, os quais, as quais, cujo, cuja, "
              "cujos, cujas, quanto, quanta, quantos, quantas"],
             ["Interrogativos", "que, quem, qual, quanto"],
             ["Indefinidos", "algum, alguém, nenhum, tudo, todo, outro, muito, pouco, certo, "
              "vários, tanto, quanto, qualquer, cada, quem quer que, seja quem for, entre "
              "outros"]]},
    {"t": "art", "n": "Numeral",
     "x": "O numeral se divide em quatro tipos.",
     "tbl": [["Tipo", "Exemplos"],
             ["Cardinais", "dois, cinco, nove, mil"],
             ["Ordinais", "décimo, nonagésimo, milésimo, segundo, vigésimo"],
             ["Multiplicativos", "dobro, triplo, óctuplo"],
             ["Fracionários", "terço, meio"]]},
    {"t": "art", "n": "Advérbio",
     "x": "É o elemento modificador do verbo, do adjetivo ou de outro advérbio, com diferentes "
          "naturezas (circunstâncias).",
     "tbl": [["Circunstância", "Exemplos"],
             ["Intensidade", "muito, pouco, tão"],
             ["Afirmação", "sim, certamente, sem dúvida"],
             ["Dúvida", "talvez, quiçá"],
             ["Lugar", "aqui, ali, lá, acolá"],
             ["Modo", "assim, alegremente, seriamente, à toa"],
             ["Negação", "não, de forma alguma, de modo algum"],
             ["Tempo", "hoje, ontem, sempre, em breve"],
             ["Companhia", "com ele, com ela"],
             ["Instrumento", "com a faca, com o serrote"]]},
    {"t": "art", "n": "Preposição",
     "x": "Elementos invariáveis que relacionam dois termos de uma oração: a, até, após, com, "
          "contra, de, desde, em, entre, para, per, perante, por, sem, sob, sobre, trás. Há "
          "ainda as locuções prepositivas: abaixo de, acerca de, acima de, a despeito de, ao "
          "lado de, ao redor de, a par de, debaixo de, em cima de, junto a, diante de, entre "
          "outras."},
    {"t": "art", "n": "Conjunção — Coordenadas",
     "x": "Conjunção é o elemento que relaciona duas orações ou dois termos semelhantes da mesma "
          "oração. Dividem-se em coordenadas e subordinadas. As coordenadas ligam orações "
          "independentes entre si.",
     "tbl": [["Tipo", "Exemplos"],
             ["Aditivas", "e, nem"],
             ["Adversativas", "mas, porém, contudo, todavia, entretanto"],
             ["Alternativas", "ou (repetida ou não), ora, quer, seja, nem"],
             ["Conclusivas", "logo, então, portanto, pois, por conseguinte, por isso, assim"],
             ["Explicativas", "que, porque, pois"]]},
    {"t": "art", "n": "Conjunção — Subordinadas",
     "x": "As conjunções subordinadas ligam uma oração dependente (subordinada) à oração principal.",
     "tbl": [["Tipo", "Exemplos"],
             ["Causais", "porque, pois, como, pois que, já que, uma vez que, visto que, "
              "porquanto"],
             ["Concessivas", "embora, ainda que, apesar de, mesmo que, conquanto, se bem que, "
              "por mais que, posto que, malgrado, não obstante, em que pese"],
             ["Condicionais", "se, caso, contanto que, sem que, desde que, a menos que, a não "
              "ser que"],
             ["Finais", "para que, a fim de que, porque (= para que)"],
             ["Temporais", "quando, antes de, depois de, até que, logo que, sempre que, assim "
              "que, todas as vezes que, cada vez que, apenas, mal"],
             ["Consecutivas", "que (combinada com tanto, tão), de forma que, de maneira que, de "
              "modo que, de sorte que"],
             ["Comparativas", "que, do que, quanto, como, assim como, bem como, que nem"],
             ["Integrantes", "que e se"],
             ["Conformativas", "como, segundo, conforme, de acordo com, para"],
             ["Proporcionais", "à medida que, à proporção que"]]},
    {"t": "art", "n": "Interjeição",
     "x": "Elemento usado para expressar emoções e reações (ex.: Ah!, Oh!, Bis!, Psiu!, Alô!, "
          "Ui!, Ai!, Oxalá!)."},
]

array_literal = ',\n' + ',\n'.join(json.dumps(it, ensure_ascii=False) for it in NEW_ITEMS)

decoder = json.JSONDecoder()
m = re.search(r'const TEORIA_LINGUA_PORTUGUESA_PCPE\s*=\s*\[', html)
assert m, "bloco TEORIA_LINGUA_PORTUGUESA_PCPE nao encontrado"
start = m.end() - 1
_arr, end = decoder.raw_decode(html, start)
insertion_point = end - 1  # logo antes do "]" de fechamento
html = html[:insertion_point] + array_literal + html[insertion_point:]

with open('app-template.html', 'w', encoding='utf-8', newline='') as f:
    f.write(html)
print('TEORIA_LINGUA_PORTUGUESA_PCPE complementada com', len(NEW_ITEMS), 'novos itens (Emprego das Classes de Palavras).')

# -------------------- questoes (MC, regra atual pro PC-PE) --------------------
MC_QUESTIONS = [
    ("No último período do primeiro parágrafo do texto de Gottlob Frege (\"Isso não seria "
     "possível se não pudéssemos distinguir no pensamento partes que correspondem a partes de "
     "uma sentença, de modo que a estrutura da sentença sirva como imagem da estrutura do "
     "pensamento\"), o \"que\" da locução \"de modo que\" tem valor semântico de:",
     ["causa.", "concessão.", "consequência.", "condição.", "finalidade."],
     2, "Classes de Palavras — Conjunção consecutiva",
     "\"De modo que\" é locução conjuntiva subordinativa CONSECUTIVA: introduz uma oração que "
     "exprime a consequência/resultado do que foi dito (\"de tal forma que...\")."),
    ("Em \"Se encaramos os pensamentos como compostos de partes simples\" (Gottlob Frege), o "
     "termo \"como\" expressa:",
     ["causa.", "conformidade (no sentido de \"na qualidade de\").", "consequência.",
      "tempo.", "finalidade."],
     1, "Classes de Palavras — Conjunção conformativa",
     "Nesse trecho, \"como\" tem valor conformativo/comparativo (equivale a \"na qualidade de\", "
     "\"enquanto\"), e não valor causal."),
    ("Em \"...ela encontra uma roupagem por meio da qual um outro ser humano é capaz de "
     "apreendê-lo\" (Gottlob Frege), o \"por\", na locução \"por meio de\", tem valor de:",
     ["lugar.", "tempo.", "companhia.", "meio (instrumento).", "causa."],
     3, "Classes de Palavras — Locução prepositiva de meio",
     "\"Por meio de\" é locução prepositiva que indica meio/instrumento, não lugar."),
    ("Em \"Com poucas sílabas, ela consegue expressar um incalculável número de pensamentos\" "
     "(Gottlob Frege), o termo \"Com\" tem valor de:",
     ["companhia.", "concessão.", "meio (instrumento).", "tempo.", "causa."],
     2, "Classes de Palavras — Preposição de meio",
     "\"Com poucas sílabas\" indica o meio/instrumento pelo qual a linguagem expressa "
     "pensamentos, e não companhia (que exigiria um ser animado acompanhando a ação)."),
    ("Em \"...ainda que esse pensamento lhe seja inteiramente novo\" (Gottlob Frege), a locução "
     "\"ainda que\" expressa:",
     ["tempo.", "concessão.", "causa.", "condição.", "consequência."],
     1, "Classes de Palavras — Conjunção concessiva",
     "\"Ainda que\" é locução conjuntiva subordinativa CONCESSIVA (equivale a \"embora\", "
     "\"mesmo que\"), não expressando tempo."),
    ("O primeiro período do texto de Gottlob Frege (\"É surpreendente o que a linguagem "
     "consegue fazer.\") apresenta quantos pronomes?",
     ["Nenhum.", "Um.", "Dois.", "Três.", "Quatro."],
     2, "Classes de Palavras — Pronomes em contexto",
     "Há dois pronomes: \"o\" (pronome demonstrativo, equivalente a \"aquilo que\") e \"que\" "
     "(pronome relativo). O \"a\" antes de \"linguagem\" é artigo definido, não pronome."),
    ("São classes gramaticais INVARIÁVEIS, EXCETO:",
     ["advérbio.", "conjunção.", "pronome.", "preposição.", "interjeição."],
     2, "Classes de Palavras — Variáveis x Invariáveis",
     "O pronome é uma classe VARIÁVEL (varia em gênero, número e pessoa). As invariáveis são "
     "advérbio, conjunção, preposição e interjeição."),
    ("Assinale a alternativa que apresenta apenas pronomes pessoais RETOS:",
     ["me, ti, se.", "eu, tu, ele.", "meu, teu, seu.", "este, esse, aquele.",
      "que, quem, qual."],
     1, "Classes de Palavras — Pronomes pessoais retos",
     "Pronomes pessoais retos exercem função de sujeito: eu, tu, ele, ela, nós, vós, eles, "
     "elas. As demais alternativas trazem, respectivamente, oblíquos, possessivos, "
     "demonstrativos e relativos/interrogativos."),
    ("O numeral \"terço\" classifica-se como:",
     ["cardinal.", "ordinal.", "multiplicativo.", "fracionário.", "coletivo."],
     3, "Classes de Palavras — Numeral fracionário",
     "\"Terço\" (assim como \"meio\") é numeral fracionário, indicando uma fração/parte de um "
     "todo."),
    ("São conjunções coordenativas ADVERSATIVAS:",
     ["e, nem.", "mas, porém, contudo.", "logo, portanto.", "que, porque, pois.",
      "ou, ora, quer."],
     1, "Classes de Palavras — Conjunção adversativa",
     "Mas, porém, contudo, todavia e entretanto são as conjunções coordenativas adversativas "
     "clássicas, que exprimem oposição/contraste."),
]

with open('questions.json', encoding='utf-8') as f:
    qdata = json.load(f)

next_id = max(q['id'] for q in qdata) + 1
added = 0
for enun, alts, resp_idx, assunto, exp in MC_QUESTIONS:
    qdata.append({
        "id": next_id,
        "corp": "PCPE",
        "disc": "Língua Portuguesa",
        "assunto": assunto,
        "tipo": "MC",
        "enun": enun,
        "alts": alts,
        "resp": resp_idx,
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
print('OK --', added, 'questoes de Língua Portuguesa (PC-PE, MC) adicionadas. Total no banco:', len(check))

with open('questions.json', encoding='utf-8') as f:
    qdata_raw = f.read()
with open('app-template.html', encoding='utf-8') as f:
    html2 = f.read()
html2 = html2.replace('__QUESTIONS_JSON__', qdata_raw)
with open('estudo-cebraspe-ma.html', 'w', encoding='utf-8') as f:
    f.write(html2)
print('estudo-cebraspe-ma.html regenerado com sucesso')
