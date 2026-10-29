# -*- coding: utf-8 -*-
"""
A teoria de "Emprego das classes de palavras" (item 5.1 do edital de Lingua
Portuguesa do PC-PE) e as 10 questoes de classificacao isolada (ids
1084-1093, disc "Lingua Portuguesa") ja existiam no app antes deste script,
cobrindo integralmente o conteudo do slide "Emprego das Classes de Palavras"
(Maria Augusta G. Almeida) enviado pelo usuario -- as 10 classes gramaticais,
tipos de pronome, numeral, advergio, preposicao e conjuncao (coordenadas e
subordinadas) ja estavam la.

A parte do slide que ainda nao tinha equivalente no app era o bloco de
questoes de leitura (paginas 21-32), que aplica a classificacao gramatical
a um texto de Gottlob Frege. Essas questoes originais, porem, nao trazem
gabarito e uma delas (pagina 25) referencia "segundo paragrafo" de forma
inconsistente com o recorte do texto mostrado no slide (o trecho citado
esta no terceiro paragrafo) -- por isso nao foram transcritas literalmente.
Em vez disso, foram escritas 12 questoes de multipla escolha (regra atual
pro PC-PE) originais, usando o mesmo texto-base de Frege, pedindo a
classificacao gramatical de termos cuja resposta e inequivoca e rastreavel
as proprias regras ja ensinadas na secao "Emprego das classes de palavras"
do app (concessiva, obliquo atono, preposicao x funcao adverbial,
adversativa, demonstrativo, condicional, relativo, consecutiva, aditiva,
locucao prepositiva, relativo+crase) -- juntando o item 1 do edital
("Compreensao e interpretacao de textos") com o item 5.1.

Este script cuida so de: (1) acrescentar as 12 questoes a questions.json,
(2) regenerar estudo-cebraspe-ma.html a partir do app-template.html (sem
mudancas estruturais nele, pois o deck e o disc "Lingua Portuguesa" ja
existiam).
"""
import json

TEXTO = (
    "\"É surpreendente o que a linguagem consegue fazer. Com poucas sílabas, "
    "ela consegue expressar um incalculável número de pensamentos, a tal "
    "ponto que, até para um pensamento pela primeira vez apreendido por um "
    "ser humano, ela encontra uma roupagem por meio da qual um outro ser "
    "humano é capaz de apreendê-lo, ainda que esse pensamento lhe seja "
    "inteiramente novo. Isso não seria possível se não pudéssemos "
    "distinguir no pensamento partes que correspondem a partes de uma "
    "sentença, de modo que a estrutura da sentença sirva como imagem da "
    "estrutura do pensamento. É verdade que falamos figuradamente quando "
    "aplicamos ao pensamento a relação todo-parte. Essa analogia, porém, é "
    "tão clara e, de modo geral, tão pertinente que dificilmente nos "
    "deixamos perturbar por suas eventuais imperfeições. Se encaramos os "
    "pensamentos como compostos de partes simples, e se a estas "
    "correspondem, por sua vez, partes simples da sentença, então podemos "
    "compreender como é possível formar, a partir de poucas partes da "
    "sentença, uma grande variedade de sentenças, às quais, por sua vez, "
    "corresponde uma grande variedade de pensamentos.\" (Gottlob Frege, excerto)"
)

MC_QUESTIONS = [
    (
        TEXTO + " No trecho \"ainda que esse pensamento lhe seja inteiramente novo\", o termo destacado \"ainda que\" classifica-se, quanto à classe gramatical, como:",
        ["Conjunção coordenativa adversativa.", "Conjunção subordinativa concessiva.", "Conjunção subordinativa condicional.", "Locução adverbial de tempo.", "Pronome indefinido."],
        1,
        "Classes de Palavras — Conjunção subordinativa concessiva (leitura de texto)",
        "Correto o item B. \"Ainda que\" introduz oração subordinada adverbial concessiva (equivale a \"embora\"), como já classificado na própria lista de conjunções subordinadas concessivas (embora, ainda que, apesar de, mesmo que...)."
    ),
    (
        TEXTO + " Ainda no trecho \"ainda que esse pensamento lhe seja inteiramente novo\", o termo \"lhe\" classifica-se como:",
        ["Pronome pessoal oblíquo átono, com função de objeto indireto.", "Pronome pessoal reto.", "Pronome de tratamento.", "Pronome possessivo.", "Pronome demonstrativo."],
        0,
        "Classes de Palavras — Pronome pessoal oblíquo átono (leitura de texto)",
        "Correto o item A. \"Lhe\" é pronome pessoal oblíquo átono de 3ª pessoa (equivalente a \"a ele/a ela\"), aqui com valor de objeto indireto de \"seja\" — o pensamento é novo \"para ele\"."
    ),
    (
        TEXTO + " No início do texto, em \"Com poucas sílabas, ela consegue expressar...\", a palavra \"Com\" classifica-se, quanto à classe gramatical, como:",
        ["Advérbio de instrumento.", "Preposição.", "Conjunção coordenativa aditiva.", "Pronome indefinido.", "Locução conjuntiva."],
        1,
        "Classes de Palavras — Preposição x função adverbial (leitura de texto)",
        "Correto o item B. \"Com\" é preposição — essa é a classe gramatical da palavra isolada. A locução \"com poucas sílabas\" é que exerce função de adjunto adverbial de instrumento/meio; não se deve confundir a classe de uma palavra com a função sintática do grupo em que ela aparece."
    ),
    (
        TEXTO + " No segundo parágrafo, em \"Essa analogia, porém, é tão clara...\", o termo \"porém\" classifica-se como:",
        ["Conjunção subordinativa concessiva.", "Conjunção coordenativa adversativa.", "Conjunção coordenativa conclusiva.", "Advérbio de negação.", "Preposição."],
        1,
        "Classes de Palavras — Conjunção coordenativa adversativa (leitura de texto)",
        "Correto o item B. \"Porém\" é uma das conjunções coordenativas adversativas clássicas (mas, porém, contudo, todavia, entretanto), ligando ideias que se contrapõem."
    ),
    (
        TEXTO + " Ainda no segundo parágrafo, em \"dificilmente nos deixamos perturbar por suas eventuais imperfeições\", o termo \"nos\" classifica-se como:",
        ["Pronome pessoal reto.", "Pronome de tratamento.", "Pronome pessoal oblíquo átono, com função de objeto direto.", "Pronome possessivo.", "Pronome relativo."],
        2,
        "Classes de Palavras — Pronome oblíquo átono, objeto direto (leitura de texto)",
        "Correto o item C. \"Nos\" é pronome pessoal oblíquo átono de 1ª pessoa do plural, funcionando como objeto direto de \"deixamos\" na construção \"deixamos [nos] perturbar\"."
    ),
    (
        TEXTO + " No primeiro parágrafo, em \"Isso não seria possível se não pudéssemos distinguir...\", o termo \"Isso\" classifica-se como:",
        ["Pronome demonstrativo, retomando a ideia do período anterior.", "Pronome indefinido.", "Pronome pessoal reto.", "Pronome relativo.", "Conjunção integrante."],
        0,
        "Classes de Palavras — Pronome demonstrativo (leitura de texto)",
        "Correto o item A. \"Isso\" é pronome demonstrativo neutro que retoma toda a ideia expressa no período anterior (a capacidade da linguagem de comunicar até pensamentos inéditos)."
    ),
    (
        TEXTO + " Ainda em \"Isso não seria possível se não pudéssemos distinguir...\", o termo \"se\" classifica-se como:",
        ["Conjunção subordinativa concessiva.", "Conjunção subordinativa condicional.", "Conjunção coordenativa alternativa.", "Pronome reflexivo.", "Conjunção integrante."],
        1,
        "Classes de Palavras — Conjunção subordinativa condicional (leitura de texto)",
        "Correto o item B. \"Se\", nesse contexto, introduz uma oração subordinada adverbial condicional — a mesma classificação de \"se, caso, contanto que\" vista na lista de conjunções subordinadas condicionais."
    ),
    (
        TEXTO + " No trecho \"partes que correspondem a partes de uma sentença\", o termo \"que\" classifica-se como:",
        ["Conjunção integrante.", "Conjunção subordinativa consecutiva.", "Pronome relativo, retomando \"partes\" como sujeito de \"correspondem\".", "Pronome interrogativo.", "Advérbio de intensidade."],
        2,
        "Classes de Palavras — Pronome relativo (leitura de texto)",
        "Correto o item C. \"Que\" retoma o antecedente \"partes\" e exerce a função de sujeito de \"correspondem\" — é pronome relativo, diferente do \"que\" conjunção (integrante ou consecutiva) que aparece em outros trechos do mesmo texto."
    ),
    (
        TEXTO + " No trecho \"de modo que a estrutura da sentença sirva como imagem da estrutura do pensamento\", a locução \"de modo que\" classifica-se como:",
        ["Locução conjuntiva subordinativa consecutiva.", "Locução conjuntiva subordinativa final.", "Locução conjuntiva subordinativa proporcional.", "Locução prepositiva.", "Locução adverbial de modo."],
        0,
        "Classes de Palavras — Locução conjuntiva consecutiva (leitura de texto)",
        "Correto o item A. \"De modo que\" introduz oração subordinada consecutiva, indicando a consequência de a linguagem conseguir expressar tantos pensamentos com poucas sílabas — mesma locução já listada entre as conjunções subordinadas consecutivas (de modo que, de forma que, de maneira que, de sorte que)."
    ),
    (
        TEXTO + " No terceiro parágrafo, em \"Se encaramos os pensamentos como compostos de partes simples, e se a estas correspondem...\", o termo \"e\" classifica-se como:",
        ["Conjunção coordenativa aditiva.", "Conjunção coordenativa adversativa.", "Conjunção subordinativa condicional.", "Preposição.", "Advérbio."],
        0,
        "Classes de Palavras — Conjunção coordenativa aditiva (leitura de texto)",
        "Correto o item A. \"E\" liga duas orações coordenadas de sentido semelhante (ambas introduzidas por \"se\"), exercendo o papel clássico da conjunção coordenativa aditiva."
    ),
    (
        TEXTO + " Ainda no terceiro parágrafo, em \"a partir de poucas partes da sentença\", a expressão \"a partir de\" classifica-se como:",
        ["Locução conjuntiva.", "Locução prepositiva.", "Locução adverbial de negação.", "Conjunção subordinativa proporcional.", "Pronome indefinido."],
        1,
        "Classes de Palavras — Locução prepositiva (leitura de texto)",
        "Correto o item B. \"A partir de\" é locução prepositiva — mais de uma palavra funcionando como uma preposição única —, relacionando \"formar\" a \"poucas partes da sentença\", do mesmo modo que outras locuções prepositivas já vistas (abaixo de, acerca de, ao lado de...)."
    ),
    (
        TEXTO + " No final do texto, em \"...uma grande variedade de sentenças, às quais, por sua vez, corresponde uma grande variedade de pensamentos\", a expressão \"às quais\" classifica-se como:",
        ["Pronome relativo precedido da preposição exigida pelo verbo \"corresponder\" (corresponder A algo).", "Pronome interrogativo.", "Pronome demonstrativo.", "Conjunção integrante.", "Pronome possessivo."],
        0,
        "Classes de Palavras — Pronome relativo + crase (leitura de texto)",
        "Correto o item A. O verbo \"corresponder\" rege a preposição \"a\" (corresponder A algo); como o antecedente (\"sentenças\", feminino plural) é retomado pelo pronome relativo \"qual\", forma-se \"a + as quais\" = \"às quais\", com o sinal indicativo de crase."
    ),
]

def main():
    with open('questions.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    max_id = max(q['id'] for q in data)

    new_objs = []
    for i, (enun, alts, resp, assunto, exp) in enumerate(MC_QUESTIONS, start=1):
        new_objs.append({
            "id": max_id + i,
            "corp": "PCPE",
            "disc": "Língua Portuguesa",
            "tipo": "MC",
            "enun": enun,
            "alts": alts,
            "resp": resp,
            "exp": exp,
            "assunto": assunto,
        })

    with open('questions.json', 'w', encoding='utf-8', newline='') as f:
        f.write('[' + json.dumps(data[0], ensure_ascii=False))
        for q in data[1:]:
            f.write('\r\n, ' + json.dumps(q, ensure_ascii=False))
        for q in new_objs:
            f.write('\r\n, ' + json.dumps(q, ensure_ascii=False))
        f.write(']')

    print(f"Added {len(new_objs)} new questions, ids {max_id+1}..{max_id+len(new_objs)}")

    with open('app-template.html', 'r', encoding='utf-8') as f:
        template = f.read()
    with open('questions.json', 'r', encoding='utf-8') as f:
        questions_json = f.read()
    final_html = template.replace('__QUESTIONS_JSON__', questions_json)
    with open('estudo-cebraspe-ma.html', 'w', encoding='utf-8', newline='') as f:
        f.write(final_html)
    print("Regenerated estudo-cebraspe-ma.html")

if __name__ == '__main__':
    main()
