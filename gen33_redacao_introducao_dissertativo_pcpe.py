# -*- coding: utf-8 -*-
# Adiciona conteudo de Redacao (Introducao do Texto Dissertativo)
# pra PC-PE: um deck de teoria na aba Teoria (corp PCPE). O material
# nao tem questoes (e so uma aula de tecnica de redacao), entao so
# adicionamos o deck de teoria, sem registrar em TEORIA_DECK_TO_DISC
# (nao ha banco de questoes de "Redacao" pra ligar o botao de
# praticar). Fonte: "Introducao do Texto Dissertativo", Prof. Douglas
# W., Focus Concursos.
import re
import json

with open('app-template.html', encoding='utf-8') as f:
    html = f.read()

TEORIA_ITEMS = [
    {"t": "tit", "x": "REDAÇÃO — INTRODUÇÃO DO TEXTO DISSERTATIVO (PC-PE)"},
    {"t": "art", "n": "O que você PODE/DEVE fazer na introdução",
     "x": "Aludir rapidamente ao tema. Fazer referência ao comando da proposta. Apresentar sua tese "
          "(obrigatório). Antecipar brevemente a linha argumentativa a ser seguida. Fazer uma citação."},
    {"t": "art", "n": "O que você NÃO PODE fazer na introdução",
     "x": "Prolongar-se demais. Dirigir-se ao leitor. Usar a 1ª pessoa ou expressões como \"eu acho\" / "
          "\"na minha opinião\". Apresentar conclusões (isso é papel da conclusão, não da introdução). "
          "Escrever uma sequência de frases sem coesão entre si. Mostrar-se inseguro."},
    {"t": "art", "n": "Estratégia 1 — Construção da tese",
     "x": "Apresenta o tema de forma contextualizada e já deixa clara a tese (o problema que será "
          "discutido no texto).",
     "s": "Exemplo: \"Durante, principalmente, a década de 1980, o Brasil mostrou-se um país de "
          "emigração. Na chamada década perdida, inúmeros brasileiros deixaram o país em busca de "
          "melhores condições de vida. No século XXI, um fenômeno inverso é evidente: a chegada ao "
          "Brasil de grandes contingentes imigratórios, com indivíduos de países subdesenvolvidos "
          "latino-americanos. No entanto, as condições precárias de vida dessas pessoas são desafios ao "
          "governo e à sociedade brasileira para a plena adaptação de todos os cidadãos à nova "
          "realidade.\""},
    {"t": "art", "n": "Estratégia 2 — Roteiro",
     "x": "Anuncia diretamente o caminho que o texto vai seguir (quais aspectos do tema serão "
          "discutidos), sem rodeios.",
     "s": "Exemplo: \"Para se analisar a questão da violência contra o menor no Brasil, é essencial que "
          "se discutam suas causas e suas consequências.\""},
    {"t": "art", "n": "Estratégia 3 — Base histórica",
     "x": "Situa o tema a partir de um contraste com um momento histórico anterior, mostrando uma "
          "mudança de cenário ao longo do tempo.",
     "s": "Exemplo: \"Diferentemente do que ocorreu em séculos passados durante o processo de "
          "colonização, o Brasil, no século XXI, destaca-se no cenário mundial por atuar como área de "
          "atração populacional.\""},
    {"t": "art", "n": "Estratégia 4 — Estatística",
     "x": "Abre o texto com um dado numérico de impacto, que evidencia a gravidade ou relevância do "
          "tema.",
     "s": "Exemplo: \"Quarenta mil crianças morreram hoje no mundo, vítimas de doenças comuns combinadas "
          "com a desnutrição. Para cada criança que morreu hoje, muitas outras vivem com a saúde "
          "debilitada. Entre os sobreviventes, metade nunca colocará os pés em uma sala de aula.\""},
    {"t": "art", "n": "Estratégia 5 — Contraponto",
     "x": "Apresenta uma ideia aparentemente positiva ou consensual e, em seguida, introduz uma ressalva "
          "('porém', 'apesar de') que conduz à tese — útil para temas com duplo aspecto (benefício x "
          "risco, por exemplo).",
     "s": "Exemplo: \"Chocolate faz bem à humanidade. Porém, apesar de trazer benefícios, o seu consumo "
          "em excesso é, muitas vezes, prejudicial.\""},
    {"t": "art", "n": "Estratégia 6 — Citação",
     "x": "Abre com a fala de um autor/pensador relacionado ao tema e, na sequência, conecta essa ideia "
          "à realidade discutida no texto, já apontando a tese.",
     "s": "Exemplo: \"O educador e filósofo brasileiro Paulo Freire afirmava que 'se a educação sozinha "
          "não transforma a sociedade, sem ela tampouco a sociedade muda'. Analisando o pensamento e "
          "relacionando-o à realidade da educação no Brasil, percebe-se a necessidade de um olhar mais "
          "atento para o aprimoramento do sistema de ensino, considerando sua importância para a "
          "promoção de uma sociedade mais crítica e reflexiva, que, consequentemente, tende a ser mais "
          "justa, igualitária e humanizada.\""},
    {"t": "art", "n": "Estratégia 7 — Definição",
     "x": "Começa definindo um conceito-chave do tema, para então apontar suas consequências ou "
          "desdobramentos.",
     "s": "Exemplo: \"Define-se como sedentário o indivíduo que não pratica atividades físicas no seu "
          "cotidiano. Doenças como obesidade, diabetes, aumento do colesterol e problemas cardíacos são "
          "algumas das que podem aparecer como consequência deste mau hábito.\""},
    {"t": "art", "n": "Estratégia 8 — Comparação",
     "x": "Contrasta a realidade de dois contextos (ex.: dois países) para evidenciar o problema a ser "
          "discutido no Brasil.",
     "s": "Exemplo: \"Os Estados Unidos, referência em desenvolvimento tecnológico, são um bom exemplo "
          "de que a educação de qualidade e com a valorização adequada gera bons frutos. Em "
          "contrapartida, no Brasil a realidade tem sido bem distinta. O baixo piso salarial dos "
          "professores explicita essa falta de reconhecimento aos profissionais da educação. Tal "
          "desvalorização é fruto de baixos investimentos governamentais, aliado ao passado histórico "
          "brasileiro.\""},
]

array_literal = '[\n' + ',\n'.join(json.dumps(it, ensure_ascii=False) for it in TEORIA_ITEMS) + '\n]'

decoder = json.JSONDecoder()
m = re.search(r'const TEORIA_INFORMATICA_WIN11_PCPE\s*=\s*\[', html)
assert m, "bloco TEORIA_INFORMATICA_WIN11_PCPE nao encontrado"
start = m.end() - 1
_arr, end = decoder.raw_decode(html, start)
insertion_point = end + 1  # depois do ';'
new_block = '\n\nconst TEORIA_REDACAO_PCPE = ' + array_literal + ';'
html = html[:insertion_point] + new_block + html[insertion_point:]

old_teoria_tail = ('  informatica_win11_pcpe: { label: "Informática — Sistema Operacional Windows 11 (PC-PE)", '
                   'data: TEORIA_INFORMATICA_WIN11_PCPE, corp: "PCPE" }\n};')
assert old_teoria_tail in html, "final de TEORIA_DECKS nao encontrado como esperado"
new_teoria_tail = ('  informatica_win11_pcpe: { label: "Informática — Sistema Operacional Windows 11 (PC-PE)", '
                   'data: TEORIA_INFORMATICA_WIN11_PCPE, corp: "PCPE" },\n'
                   '  redacao_pcpe: { label: "Redação — Introdução do Texto Dissertativo (PC-PE)", '
                   'data: TEORIA_REDACAO_PCPE, corp: "PCPE" }\n};')
html = html.replace(old_teoria_tail, new_teoria_tail, 1)

with open('app-template.html', 'w', encoding='utf-8', newline='') as f:
    f.write(html)
print('TEORIA_REDACAO_PCPE adicionada com', len(TEORIA_ITEMS), 'itens; registrada em TEORIA_DECKS.')

with open('questions.json', encoding='utf-8') as f:
    qdata_raw = f.read()
with open('app-template.html', encoding='utf-8') as f:
    html2 = f.read()
html2 = html2.replace('__QUESTIONS_JSON__', qdata_raw)
with open('estudo-cebraspe-ma.html', 'w', encoding='utf-8') as f:
    f.write(html2)
print('estudo-cebraspe-ma.html regenerado com sucesso')
