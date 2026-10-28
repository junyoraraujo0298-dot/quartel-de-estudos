# -*- coding: utf-8 -*-
# Complementa o deck "Direito Penal - Principios (PC-PE)" com o item
# 3 do conteudo programatico oficial (Aplicacao da lei penal: 3.1 a
# 3.6), a partir do material "Aplicacao da Lei Penal no Tempo e no
# Espaco" (Focus Concursos). Os campos "n" dos itens de teoria e
# "assunto" das questoes usam a numeracao oficial do edital (3.1-3.6)
# pra manter a disciplina/assunto rastreavel ao conteudo programatico
# (ver PROGRAMA_PCPE_AGENTE -> "Direito Penal" -> item 3), conforme
# pedido do usuario.
#
# As 17 questoes adicionadas sao todas de multipla escolha (regra
# atual pro PC-PE) e foram colhidas INTEGRALMENTE do material, que ja
# trazia enunciado + 5 alternativas + gabarito comentado prontos --
# nao houve necessidade de reformular nem fabricar alternativas.
import re
import json

with open('app-template.html', encoding='utf-8') as f:
    html = f.read()

NEW_ITEMS = [
    {"t": "sec", "x": "Aplicação da Lei Penal no Tempo e no Espaço (Edital: Direito Penal, item 3)"},
    {"t": "art", "n": "3.1 — Tempus Regit Actum",
     "x": "A lei a ser aplicada é a lei vigente ao tempo do fato. Princípios: irretroatividade da lei penal "
          "(art. 5º, XL, CF) e, como exceção, retroatividade da lei penal benéfica. No período de vacatio "
          "legis (vacância da lei) é proibida a aplicação da lei penal, mesmo que seja para beneficiar o "
          "réu, já que os seus efeitos só iniciam no dia da entrada em vigor."},
    {"t": "art", "n": "3.1 — Os 4 conflitos de leis penais no tempo",
     "x": "Diante da sucessão de leis penais no tempo, há 4 cenários distintos.",
     "tbl": [["Conflito", "O que é", "Retroage?"],
             ["Abolitio criminis", "Lei posterior que exclui um fato como criminoso (descriminalização)",
              "Sim — alcança até sentença transitada em julgado, cessando execução e efeitos penais"],
             ["Novatio legis in mellius", "Lei nova mais favorável que a anterior (o fato não deixa de ser "
              "crime, só \"melhora\")", "Sim"],
             ["Novatio legis in pejus (lex gravior)", "Lei nova mais severa que a anterior", "Não"],
             ["Novatio legis incriminadora", "Lei posterior que criminaliza conduta antes irrelevante para "
              "o Direito Penal", "Não"]]},
    {"t": "art", "n": "3.2 — Tempo do crime: Teoria da Atividade",
     "x": "Considera-se praticado o crime no momento da ação ou omissão, ainda que outro seja o momento do "
          "resultado (art. 4º, CP) — é a teoria adotada para o TEMPO do crime. Súmula 711, STF: a lei penal "
          "mais grave aplica-se ao crime continuado ou permanente, se sua vigência é anterior à cessação da "
          "continuidade ou permanência."},
    {"t": "art", "n": "3.2 — Lugar do crime: Teoria da Ubiquidade",
     "x": "Considera-se praticado o crime no lugar em que ocorreu a ação ou omissão, no todo ou em parte, "
          "bem como onde se produziu ou deveria produzir-se o resultado (art. 6º, CP) — é a teoria adotada "
          "para o LUGAR do crime, usada para resolver os \"crimes à distância\" (ação em um país, resultado "
          "em outro).",
     "tbl": [["Teoria", "Define o crime como praticado...", "Usada para"],
             ["Da Atividade", "no lugar/momento da ação ou omissão", "TEMPO do crime (art. 4º, CP)"],
             ["Do Resultado", "no lugar/momento em que ocorre o resultado", "Não adotada pelo CP"],
             ["Da Ubiquidade (mista)", "tanto na ação/omissão quanto no resultado", "LUGAR do crime (art. 6º, CP)"]],
     "s": "Mnemônico \"LUTA\": LU = Lugar → Ubiquidade; TA = Tempo → Atividade."},
    {"t": "art", "n": "3.1/3.6 — Extra-atividade da lei penal",
     "x": "Extra-atividade é o gênero: possibilidade de uma lei já revogada ou que perdeu efeitos ser "
          "aplicada a fatos ocorridos antes, durante ou após sua vigência. Suas duas espécies: "
          "RETROATIVIDADE (a lei nova regula fatos anteriores à sua vigência) e ULTRATIVIDADE (a lei já "
          "revogada continua sendo aplicada a fatos ocorridos durante sua vigência, mesmo após ter cessado)."},
    {"t": "art", "n": "3.3 — Lei excepcional ou temporária",
     "x": "Art. 3º, CP: a lei excepcional ou temporária, embora decorrido o período de sua duração ou "
          "cessadas as circunstâncias que a determinaram, aplica-se ao fato praticado durante sua vigência. "
          "Lei temporária é a que tem vigência previamente fixada pelo legislador; lei excepcional é a que "
          "tem duração condicionada ao fim da situação de anormalidade (guerra, calamidade etc.). Ambas são "
          "SEMPRE ultra-ativas (ao contrário das leis regulares, cuja ultratividade depende de serem mais "
          "benéficas) e AUTORREVOGÁVEIS (seus efeitos cessam automaticamente com o fim do prazo/situação, "
          "sem precisar de nova lei revogando-as)."},
    {"t": "art", "n": "3.1 — Combinação de leis (Lex Tertia)",
     "x": "Ocorre quando há conflito entre duas leis penais sucessivas no tempo, cada uma com uma parte "
          "favorável e outra desfavorável ao réu. O STF e o STJ NÃO admitem a combinação de leis penais "
          "(teoria da ponderação unitária/global — a lei deve ser aplicada por inteiro). Súmula 501, STJ: "
          "\"É cabível a aplicação retroativa da Lei nº 11.343/2006, desde que o resultado da incidência das "
          "suas disposições, na íntegra, seja mais favorável ao réu do que o advindo da aplicação da Lei nº "
          "6.368/1976, sendo vedada a combinação de leis.\""},
    {"t": "art", "n": "3.1 — Princípio da continuidade normativo-típica",
     "x": "Ocorre quando um tipo penal é formalmente revogado, mas o fato criminoso passa a integrar outro "
          "dispositivo legal — a conduta nunca deixa de ser crime (ex.: a fusão do antigo \"atentado violento "
          "ao pudor\" dentro do tipo de \"estupro\" pela Lei 12.015/09). Não se confunde com abolitio "
          "criminis.",
     "tbl": [["", "Abolitio criminis", "Continuidade normativo-típica"],
             ["Supressão do tipo", "Formal e material", "Só formal (a conduta continua tipificada em outro "
              "dispositivo)"],
             ["A conduta", "Deixa de ser crime", "Permanece crime"],
             ["Efeito", "Extinção da punibilidade", "Migração para outro tipo penal"]]},
    {"t": "art", "n": "3.4 — Territorialidade (art. 5º, CP)",
     "x": "Regra geral no espaço: aplica-se a lei brasileira, sem prejuízo de convenções, tratados e regras "
          "de direito internacional, ao crime cometido no território nacional — é a territorialidade "
          "temperada/mitigada (ex.: imunidade diplomática). Território por extensão (§§1º e 2º): "
          "embarcações/aeronaves brasileiras públicas ou a serviço do governo são território nacional ONDE "
          "QUER QUE SE ENCONTREM; já as privadas/mercantes só são extensão quando em alto-mar ou no espaço "
          "aéreo correspondente. A lei brasileira também se aplica a crimes a bordo de aeronave/embarcação "
          "ESTRANGEIRA privada, quando em pouso/porto/mar territorial do Brasil. Embaixada NÃO é território "
          "estrangeiro — é território brasileiro normal, salvo a imunidade do próprio diplomata."},
    {"t": "art", "n": "3.4 — Extraterritorialidade (art. 7º, CP)",
     "x": "Possibilita que a lei brasileira seja aplicada a fatos cometidos no estrangeiro.",
     "tbl": [["Tipo", "Hipóteses (art. 7º)", "Requisito", "Princípio"],
             ["Incondicionada (inciso I)", "Vida/liberdade do Presidente; patrimônio/fé pública de ente "
              "público; administração pública por quem a serve; genocídio (brasileiro/domiciliado no Brasil)",
              "Nenhum — pune mesmo se absolvido/condenado no estrangeiro", "Defesa (a-c) / Justiça universal (d)"],
             ["Condicionada (inciso II)", "Tratado/convenção; praticado por brasileiro; a bordo de "
              "aeronave/embarcação privada brasileira não julgado no estrangeiro",
              "5 condições cumulativas do §2º: entrar no território, ser punível lá também, autorizar "
              "extradição, não ter sido absolvido/cumprido pena, não ter sido perdoado/extinta punibilidade",
              "Justiça universal (a) / Nacionalidade ativa (b) / Representação (c)"],
             ["Hipercondicionada (§3º)", "Crime de estrangeiro contra brasileiro fora do Brasil",
              "As 5 do §2º + extradição não pedida/negada + requisição do Ministro da Justiça", "—"]],
     "s": "A lei penal brasileira não se aplica às contravenções penais praticadas no estrangeiro (art. 2º "
          "da LCP) — as regras de extraterritorialidade do art. 7º falam só em \"crimes\"."},
    {"t": "art", "n": "3.4 — Pena cumprida no estrangeiro (art. 8º, CP)",
     "x": "A pena cumprida no estrangeiro atenua a pena imposta no Brasil pelo mesmo crime, quando "
          "diversas, ou nela é computada, quando idênticas. Relaciona-se com a extraterritorialidade "
          "incondicionada (o agente pode ser punido pela lei brasileira mesmo já condenado lá fora)."},
    {"t": "art", "n": "3.4 — Eficácia de sentença estrangeira (art. 9º, CP)",
     "x": "A sentença estrangeira pode ser homologada no Brasil, quando a aplicação da lei brasileira "
          "produz as mesmas consequências, para: I) obrigar o condenado à reparação do dano, restituições e "
          "outros efeitos civis (depende de pedido da parte interessada); II) sujeitá-lo a medida de "
          "segurança (depende de tratado de extradição com o país, ou, na falta, requisição do Ministro da "
          "Justiça). A competência para homologar é do STJ (art. 105, I, \"i\", CF), exigindo prova do "
          "trânsito em julgado (Súmula 420, STF). A execução já homologada cabe aos juízes federais de 1º "
          "grau. A sentença estrangeira NÃO depende de homologação para gerar reincidência, impedir sursis "
          "ou revogar livramento condicional — basta prova idônea da condenação."},
    {"t": "art", "n": "3.5 — Contagem de prazo (art. 10, CP)",
     "x": "O dia do começo inclui-se no cômputo do prazo penal. Contam-se os dias, os meses e os anos pelo "
          "calendário comum. O prazo penal (ligado ao poder punitivo do Estado) é sempre IMPRORROGÁVEL, "
          "ainda que termine em sábado, domingo ou feriado — quanto mais curto, mais benéfico ao réu. Isso é "
          "diferente do prazo processual penal (art. 798, §1º, CPP), que EXCLUI o dia do começo e pode ser "
          "prorrogado para o próximo dia útil. Prescrição, decadência e perempção seguem a regra do prazo "
          "penal (improrrogável), por estarem ligadas ao poder punitivo estatal."},
    {"t": "art", "n": "3.5 — Frações não computáveis da pena (art. 11, CP)",
     "x": "Desprezam-se, nas penas privativas de liberdade e nas restritivas de direitos, as frações de "
          "dia; e, na pena de multa, as frações de cruzeiro (hoje, centavos de real)."},
    {"t": "art", "n": "3.3 — Legislação especial (art. 12, CP)",
     "x": "As regras gerais do Código Penal aplicam-se aos fatos incriminados por lei especial, se esta não "
          "dispuser de modo diverso — ou seja, a Parte Geral do CP tem aplicação subsidiária em relação às "
          "leis penais especiais."},
    {"t": "art", "n": "3.1 — Interpretação da lei penal: analogia × interpretação extensiva × analógica",
     "x": "Analogia é forma de INTEGRAÇÃO (preenche lacuna, não existe norma pro caso) — no Direito Penal só "
          "se admite analogia \"in bonam partem\" (para beneficiar o réu); é vedada a analogia \"in malam "
          "partem\". Interpretação extensiva ocorre quando a lei disse menos do que queria dizer (minus "
          "dixit quam voluit), e o STJ admite seu uso mesmo em normas incriminadoras. Interpretação "
          "analógica existe quando o texto traz uma fórmula casuística seguida de fórmula genérica (ex.: "
          "art. 121, §2º, III — \"veneno, fogo, explosivo [...] ou outro meio insidioso ou cruel\").",
     "tbl": [["", "Interpretação extensiva", "Interpretação analógica", "Analogia"],
             ["Natureza", "Forma de interpretação", "Forma de interpretação", "Forma de integração"],
             ["Existe norma pro caso?", "Sim", "Sim", "Não"],
             ["O que faz", "Amplia o alcance de uma palavra", "Amplia via cláusula aberta (fórmula "
              "casuística + genérica)", "Cria regra nova a partir de outra análoga"]]},
    {"t": "art", "n": "3.1 — Conflito aparente de leis penais",
     "x": "Ocorre quando duas ou mais normas vigentes parecem, aparentemente, se aplicar ao mesmo fato — "
          "resolvido por 4 princípios (mnemônico CASE: Consunção, Alternatividade, Subsidiariedade, "
          "Especialidade), evitando o bis in idem.",
     "tbl": [["Princípio", "Quando se aplica"],
             ["Especialidade", "A norma especial (com elemento especializante) prevalece sobre a geral, "
              "numa comparação ABSTRATA entre os tipos (art. 12, CP) — ex.: infanticídio é homicídio "
              "especializado"],
             ["Subsidiariedade", "A norma \"soldado de reserva\" só incide se não ficar caracterizado fato "
              "mais grave; pode ser expressa (\"se o fato não constitui crime mais grave\", ex.: art. 132) "
              "ou tácita"],
             ["Consunção (absorção)", "O crime-fim (mais amplo) absorve o crime-meio — casos de crime "
              "progressivo e progressão criminosa; Súmula 17, STJ: quando o falso se exaure no estelionato, "
              "sem mais potencialidade lesiva, é por este absorvido"],
             ["Alternatividade", "Nos tipos mistos alternativos (vários núcleos/verbos, ex.: art. 33 da Lei "
              "de Drogas), praticar mais de um verbo no mesmo contexto é crime único"]]},
]

array_literal = ',\n' + ',\n'.join(json.dumps(it, ensure_ascii=False) for it in NEW_ITEMS)

decoder = json.JSONDecoder()
m = re.search(r'const TEORIA_DIREITO_PENAL_PCPE\s*=\s*\[', html)
assert m, "bloco TEORIA_DIREITO_PENAL_PCPE nao encontrado"
start = m.end() - 1
_arr, end = decoder.raw_decode(html, start)
insertion_point = end - 1  # antes do "]" de fechamento
html = html[:insertion_point] + array_literal + html[insertion_point:]

with open('app-template.html', 'w', encoding='utf-8', newline='') as f:
    f.write(html)
print('TEORIA_DIREITO_PENAL_PCPE complementada com', len(NEW_ITEMS), 'novos itens (Aplicacao da Lei Penal no Tempo e no Espaco).')

# -------------------- questoes (MC, todas colhidas do material) --------------------
MC_QUESTIONS = [
    ("Em tema de lei penal no tempo, é correto se afirmar que:",
     ["se o agente praticou crime na vigência de lei mais benéfica, que, durante a ação penal, acabou "
      "derrogada por lei mais severa, deverá ser julgado na forma desta última.",
      "em qualquer fase do processo ou mesmo da execução da pena, deve ser imediatamente aplicada a "
      "retroatividade da norma que retira a tipicidade de qualquer fato.",
      "prolatada sentença condenatória no período de vacatio de nova lei penal, não se admite a "
      "ultratividade da lei derrogada, mesmo que esta se mostre mais favorável ao réu.",
      "havendo sentença condenatória transitada em julgado, a lei posterior mais benéfica ao agente não é "
      "retroativa nem ultrativa.",
      "não pode ser utilizada lei intermediária e que surgiu depois da prática do fato criminoso, mas que "
      "foi revogada antes de o juiz proferir a sentença condenatória, ainda que mais benigna."],
     1, "3.1 — Irretroatividade da lei penal",
     "A abolitio criminis (ou qualquer norma que retire a tipicidade do fato) deve ser aplicada "
     "imediatamente em qualquer fase do processo ou da execução da pena, por força da retroatividade da "
     "lei penal benéfica (art. 2º, CP)."),
    ("A lei penal aplica-se retroativamente quando:",
     ["a contravenção penal torna-se crime.", "o crime torna-se contravenção penal.",
      "a pena de detenção torna-se de reclusão.", "a pena de multa torna-se de detenção.",
      "ocorrer a prescrição da pretensão punitiva."],
     1, "3.1 — Irretroatividade da lei penal",
     "Transformar um crime em contravenção penal é uma melhora para o agente (lex mitior), logo a lei "
     "nova retroage. As demais alternativas representam pioras (novatio legis in pejus) ou são alheias ao "
     "tema."),
    ("A respeito da Lei penal no tempo e no espaço considere: I. Ninguém pode ser punido por fato que lei "
     "posterior deixa de considerar crime, cessando em virtude dela a execução e os efeitos penais da "
     "sentença condenatória. II. A lei posterior, que de qualquer modo favorecer o agente, aplica-se aos "
     "fatos anteriores, ainda que decididos por sentença condenatória transitada em julgado. III. Para os "
     "efeitos penais, consideram-se como extensão do território nacional as embarcações brasileiras de "
     "natureza pública, privada ou a serviço do governo brasileiro onde quer que se encontrem. IV. Ficam "
     "sujeitos à lei brasileira, embora cometidos no estrangeiro, os crimes contra o patrimônio ou a fé "
     "pública de autarquia ou fundação instituída pelo Poder Público. De acordo com o Código Penal "
     "brasileiro, está correto o que consta APENAS em:",
     ["II, III e IV.", "I, II e III.", "I, II e IV.", "III e IV.", "I e II."],
     2, "3.1/3.4 — Abolitio criminis e território por extensão",
     "I e II espelham o art. 2º do CP (abolitio criminis). IV espelha o art. 7º, I, \"b\" "
     "(extraterritorialidade incondicionada). III está errada: embarcações PRIVADAS só são extensão do "
     "território quando em alto-mar/espaço aéreo correspondente, não \"onde quer que se encontrem\" (isso "
     "vale só para as de natureza pública ou a serviço do governo)."),
    ("Considerando apenas a regra constitucional sobre os efeitos da lei penal no tempo, imagine a "
     "situação em que determinado cidadão comentou com colegas de trabalho que vez ou outra tinha vontade "
     "de matar sua ex-esposa. Duas semanas após a conversa, foi editada lei definindo como crime o ato de "
     "pensar em delinquir. O cidadão acima mencionado:",
     ["poderá ser processado, mas terá a pena reduzida porque praticou a conduta antes de ter ciência de "
      "sua tipificação como crime.",
      "deverá ser processado pela prática de crime, uma vez que a confissão foi feita em intervalo "
      "inferior a 30 (trinta) dias antes da edição da lei.",
      "deverá ser processado pela prática de crime, uma vez que a lei mais severa retroage para atingir o "
      "delinquente, em prol da segurança pública.",
      "não poderá ser processado, uma vez que a tipificação de conduta como crime exige prévia lei assim "
      "definindo.",
      "não poderá ser processado, uma vez que a lei não pode retroagir para beneficiar ou prejudicar a "
      "pessoa que praticou a conduta."],
     3, "3.6 — Irretroatividade da lei penal",
     "Pelo princípio da legalidade (art. 5º, XXXIX, CF), não há crime sem lei ANTERIOR que o defina. A lei "
     "nova incriminadora (novatio legis incriminadora) não retroage para alcançar fato praticado antes de "
     "sua vigência."),
    ("Sobre as fontes do Direito Penal, a interpretação da Lei Penal, bem como seu âmbito de eficácia e "
     "sua aplicação no tempo e no espaço, é correto afirmar que:",
     ["em razão do caráter fragmentário do Direito Penal, este deverá ser preferencialmente observado para "
      "a solução de conflitos, devendo abranger a tutela do maior número de bens jurídicos possível.",
      "o princípio da Legalidade obriga a que toda deliberação referente ao Direito Penal, incriminador ou "
      "não incriminador, seja feita por meio de lei.",
      "o nosso Código Penal, quanto ao tempo do crime, acolheu a teoria do resultado.",
      "a lei penal nova mais benéfica retroage para abarcar também os fatos ocorridos antes de sua "
      "vigência, devendo aplicar-se inclusive aos processos com decisão já transitada em julgado, cabendo "
      "ao juízo da execução a sua aplicação.",
      "é vedada, em qualquer hipótese, a aplicação de interpretação extensiva em normas penais "
      "incriminadoras."],
     3, "3.2 — Teoria da Atividade e retroatividade benéfica",
     "A lei penal benéfica retroage mesmo após o trânsito em julgado (art. 2º, parágrafo único, CP), "
     "cabendo ao juízo da execução aplicá-la (Súmula 611, STF). Quanto ao tempo do crime, o CP adota a "
     "Teoria da Atividade, não a do resultado."),
    ("Assinale a alternativa correta em relação à lei penal no tempo e no espaço.",
     ["Se Carlos foi preso após a prática de crime contra os costumes e, quando da prolação da sentença, o "
      "magistrado observou que havia sido publicada nova lei, com pena mínima inferior, que entraria em "
      "vigor no prazo de 45 dias, então esse fato caracteriza uma novatio legis in mellius no período de "
      "vacatio legis, que, ao entrar em vigor, provocará um abolitio criminis.",
      "a extra-atividade da lei ocorre quando a lei nova regula situações fora de seu período de vigência, "
      "seja passado ou futuro, e ocorrerá conflito intertemporal quando a lei nova regular inteiramente a "
      "matéria veiculada na anterior.",
      "a abolitio criminis poderá gerar os seguintes efeitos: 1 - se a denúncia ainda não foi recebida, o "
      "processo não pode ser iniciado; 2 - se o processo está em andamento ou o réu está cumprindo a pena, "
      "deve ser decretada a extinção da punibilidade; 3 - havendo sentença condenatória transitada em "
      "julgado, a pretensão executória não pode ser iniciada, e o nome do réu será riscado do rol dos "
      "culpados, permanecendo, em qualquer desses casos, os efeitos civis da condenação.",
      "os princípios da territorialidade, da nacionalidade, da defesa e da justiça penal universal "
      "auxiliam a determinar a aplicação da lei penal no tempo, face a teoria da atividade adotada no "
      "ordenamento penal material em vigor.",
      "a novatio legis in pejus confunde-se com a novatio legis incriminadora porque ambas prejudicam a "
      "situação do réu."],
     2, "3.1 — Abolitio criminis e territorialidade temperada",
     "A abolitio criminis extingue os efeitos penais (inclusive reincidência) em qualquer fase — "
     "investigação, processo ou execução —, mas preserva os efeitos CIVIS da condenação (ex.: dever de "
     "indenizar)."),
    ("De acordo com os dispositivos da parte geral do Código Penal, é correto afirmar:",
     ["na hipótese de abolitio criminis a reincidência permanece como efeito secundário da prática do "
      "crime.",
      "o território nacional estende-se a embarcações e aeronaves brasileiras de natureza pública, desde "
      "que se encontrem no espaço aéreo brasileiro ou em alto-mar.",
      "crimes à distância são aqueles em que a ação ou omissão ocorre em um país e o resultado, em outro.",
      "o desconhecimento da lei é inescusável. O erro sobre a ilicitude do fato, se evitável, isenta de "
      "pena; se inevitável, poderá diminuí-la de um sexto a um terço.",
      "é isento de pena o agente que pratica crime sem violência ou grave ameaça à pessoa, desde que, "
      "voluntariamente, repare o dano ou restitua a coisa, até o recebimento da denúncia ou da queixa."],
     2, "3.2 — Crimes à distância (Teoria da Ubiquidade)",
     "Crimes à distância são aqueles em que a conduta (ação/omissão) ocorre em um país e o resultado se "
     "produz em outro — é exatamente a hipótese que o art. 6º do CP (Teoria da Ubiquidade) resolve."),
    ("No direito brasileiro, adota-se, no âmbito espacial, como regra, o princípio da territorialidade. "
     "Assinale a alternativa INCORRETA:",
     ["a lei brasileira é aplicável, por força do princípio da justiça cosmopolita, ao crime contra a "
      "dignidade sexual de criança praticado no estrangeiro, quando o agente ou vítima for brasileiro ou "
      "pessoa domiciliada no Brasil, falando a doutrina, nesse caso, de aplicação extraterritorial "
      "incondicionada.",
      "a lei brasileira é aplicável, por força do princípio da personalidade, ao crime praticado no "
      "estrangeiro por brasileiro, falando a doutrina, nesse caso, de extraterritorialidade condicionada.",
      "a lei brasileira é aplicável, por força do princípio da proteção, ao crime praticado no estrangeiro "
      "contra a Administração Pública por quem está a seu serviço, falando a doutrina, nesse caso, de "
      "aplicação extraterritorial incondicionada.",
      "a lei brasileira é aplicável, por força do princípio do pavilhão, ao crime praticado a bordo de "
      "embarcação mercante brasileira, quando em território estrangeiro e aí não seja julgado, falando a "
      "doutrina, nesse caso, de aplicação extraterritorial condicionada."],
     1, "3.4 — Princípios da extraterritorialidade",
     "O crime praticado no estrangeiro POR BRASILEIRO (art. 7º, II, \"b\") é regido pelo princípio da "
     "NACIONALIDADE ATIVA, e não simplesmente \"da personalidade\" — a nomenclatura técnica importa nesse "
     "tipo de questão."),
    ("No que se refere à aplicação da lei penal no espaço, assinale a opção correta.",
     ["de acordo com o princípio da nacionalidade, é possível a aplicação da lei penal brasileira a fato "
      "criminoso lesivo a interesse nacional ocorrido no exterior.",
      "a aplicação da lei penal brasileira a cidadão brasileiro que cometa crime no exterior é possível, de "
      "acordo com o princípio da defesa.",
      "de acordo com o princípio da representação, a lei penal brasileira poderá ser aplicada a delitos "
      "cometidos em aeronaves ou embarcações brasileiras privadas, quando estes delitos ocorrerem no "
      "estrangeiro e aí não forem julgados.",
      "de acordo com o princípio da justiça penal universal, a aplicação da lei penal brasileira é "
      "possível independentemente da nacionalidade do delinquente e do local da prática do crime, se este "
      "estiver previsto em convenção ou tratado celebrado pelo Brasil.",
      "segundo o princípio da territorialidade, a lei penal brasileira poderá ser aplicada no exterior "
      "quando o sujeito ativo do crime praticado for brasileiro."],
     2, "3.4 — Princípio da representação",
     "O princípio da representação (ou da bandeira/pavilhão) rege exatamente o art. 7º, II, \"c\": crimes "
     "cometidos em aeronaves/embarcações brasileiras privadas, em território estrangeiro, quando ali não "
     "forem julgados."),
    ("Sobre a Aplicação da Lei Penal no tempo e no espaço, é correto afirmar que são verdadeiras APENAS as "
     "seguintes assertivas: II - A lei posterior, que de qualquer modo favorecer o agente, aplica-se aos "
     "fatos anteriores, ainda que decididos por sentença condenatória transitada em julgado. III – A "
     "exceção ao princípio de que a lei não pode retroagir, salvo para beneficiar o acusado, restringe-se "
     "às normas de caráter penal, não se estendendo às normas processuais penais. IV - No Brasil adota-se "
     "o Princípio da territorialidade temperada, segundo o qual a lei penal brasileira aplica-se, em regra, "
     "ao crime cometido no território nacional, podendo a lei estrangeira ser aplicável a delitos cometidos "
     "total ou parcialmente em território nacional, quando assim determinarem tratados e convenções "
     "internacionais.",
     ["I, II e III.", "I, II e IV.", "II, IV e V.", "II, III e IV.", "II, III e V."],
     3, "3.4 — Territorialidade temperada",
     "A retroatividade benéfica (II) alcança até a coisa julgada; ela vale só para normas penais, não "
     "processuais (III); e o Brasil adota a territorialidade temperada, cedendo à lei estrangeira em casos "
     "previstos em tratados/convenções (IV)."),
    ("Atinente à aplicação da Lei penal no tempo e no espaço, é correto afirmar:",
     ["no que tange ao tempo do crime, o código penal adotou a teoria da ubiquidade.",
      "leis temporárias e excepcionais (art. 3º, CP) são hipóteses excepcionais de ultra-atividade "
      "maléfica.",
      "para os efeitos penais, consideram-se como extensão do território nacional as embarcações e "
      "aeronaves brasileiras, de natureza pública ou a serviço do governo brasileiro onde quer que se "
      "encontrem, bem como as aeronaves e as embarcações brasileiras, mercantes ou de propriedade privada, "
      "que se achem, respectivamente, no espaço aéreo correspondente ou em alto-mar. Tal instituto é "
      "denominado Extraterritorialidade.",
      "de acordo com o princípio da territorialidade, não é possível, por conta de regras internacionais, "
      "que um crime cometido no Brasil não sofra as consequências da Lei Brasileira."],
     1, "3.3 — Ultratividade das leis temporárias e excepcionais",
     "As leis temporárias e excepcionais são sempre ultra-ativas, inclusive quando mais gravosas ao réu — é "
     "exceção à regra geral de que só retroage/ultra-age o que for benéfico, justamente porque, sem essa "
     "regra, bastaria \"esperar o prazo acabar\" para escapar da punição."),
    ("No que concerne à aplicação da lei penal no espaço, o princípio pelo qual se aplica a lei do país ao "
     "fato que atinge bem jurídico nacional, sem nenhuma consideração a respeito do local onde o crime foi "
     "praticado ou da nacionalidade do agente, denomina-se princípio:",
     ["da nacionalidade.", "da territorialidade.", "de proteção.", "da competência universal.",
      "de representação."],
     2, "3.4 — Princípio da proteção (defesa)",
     "O princípio da proteção (ou da defesa) protege bens jurídicos nacionais relevantes (ex.: vida do "
     "Presidente, patrimônio público) independentemente de onde o crime foi praticado ou de quem o praticou "
     "— é o fundamento das hipóteses de extraterritorialidade incondicionada do art. 7º, I, \"a\" a \"c\"."),
    ("Sobre a eficácia da sentença estrangeira, é correto afirmar que:",
     ["depende de homologação para produzir reincidência;", "depende de homologação para impedir a "
      "obtenção de sursis;", "depende de homologação para aumentar o período para concessão de livramento "
      "condicional;", "não depende de homologação para revogação do livramento condicional;",
      "não depende de homologação para aplicar medida de segurança."],
     3, "3.4 — Eficácia de sentença estrangeira",
     "A sentença penal estrangeira condenatória não depende de homologação para incidir sobre reincidência, "
     "sursis ou livramento condicional (inclusive sua revogação) — basta prova idônea da condenação. A "
     "homologação (pelo STJ) só é exigida para os efeitos do art. 9º, CP: reparação civil e medida de "
     "segurança."),
    ("À luz do que dispõe a parte geral do Código Penal Brasileiro, assinale a alternativa correta:",
     ["a sentença estrangeira, quando a aplicação da lei brasileira produz na espécie as mesmas "
      "consequências, pode ser homologada no Brasil, para obrigar o condenado à reparação do dano, a "
      "restituições e a outros efeitos civis e, ainda, sujeitá-lo à medida de segurança.",
      "a sentença estrangeira... pode ser homologada no Brasil, para, dentre outras hipóteses, sujeitar o "
      "condenado ao cumprimento de penas restritivas de direitos.",
      "a pena cumprida no estrangeiro é computada na pena imposta no Brasil pelo mesmo crime, quando "
      "diversas, ou é atenuada, quando idênticas.",
      "considera-se praticado o crime no lugar onde se produziu ou deveria produzir-se o resultado. O "
      "Código Penal, quanto a essa regra, adotou a teoria do resultado.",
      "a lei excepcional ou temporária aplica-se ao fato praticado durante sua vigência, salvo se vier "
      "norma posterior mais benéfica, tendo em vista o princípio da retroatividade da norma penal em "
      "benefício do réu."],
     0, "3.4 — Eficácia de sentença estrangeira (art. 9º, CP)",
     "O art. 9º, CP permite a homologação de sentença estrangeira tanto para reparação civil/restituições "
     "(inciso I) quanto para sujeitar o condenado a medida de segurança (inciso II)."),
    ("Assinale a opção correta acerca da interpretação da lei penal:",
     ["a interpretação extensiva é admitida em direito penal para estender o sentido e o alcance da norma "
      "até que se atinja sua real acepção.",
      "a interpretação analógica não é admitida em direito penal porque prejudica o réu.",
      "a interpretação teleológica consiste em extrair o sentido e o alcance da norma de acordo com a "
      "posição da palavra na estrutura do texto legal.",
      "a analogia penal permite ao juiz atuar para suprir a lacuna da lei, desde que isso favoreça o réu.",
      "a interpretação judicial da lei penal se manifesta na edição de súmulas vinculantes editadas pelos "
      "tribunais."],
     0, "3.1 — Interpretação extensiva",
     "A interpretação extensiva amplia o alcance da norma até alcançar sua real vontade, quando o "
     "legislador \"disse menos do que queria dizer\" — é admitida inclusive em normas incriminadoras. A "
     "analogia (alternativa D), embora também só caiba in bonam partem, não é uma forma de INTERPRETAÇÃO, "
     "mas de integração — por isso não responde à pergunta do enunciado."),
    ("Quando o agente invade domicílio para praticar furto, há concurso aparente de normas entre os "
     "delitos de invasão de domicílio e furto. Tal conflito resolve-se pelo princípio da:",
     ["alternatividade.", "especialidade.", "subsidiariedade.", "consunção."],
     3, "3.1 — Consunção",
     "A invasão de domicílio é meio normal de execução do furto qualificado pela invasão — o crime-fim "
     "(furto) absorve o crime-meio (violação de domicílio), caracterizando consunção."),
    ("Sobre o conflito aparente de normas penais, acerca do princípio da especialidade, assinale a "
     "alternativa que constitui a EXCEÇÃO (ou seja, está incorreta):",
     ["o princípio da especialidade determina que o tipo penal especial prevalece sobre o tipo penal de "
      "caráter geral afastando, desta forma, o bis in idem, pois a conduta do agente só é enquadrada na "
      "norma incriminadora especial, embora também estivesse descrita na geral.",
      "para se saber qual norma é geral e qual é especial é preciso analisar o fato concreto praticado, "
      "não bastando que se comparem abstratamente as descrições contidas nos tipos penais.",
      "a comparação entre as leis não se faz da mais grave para a menos grave, nem da mais completa para a "
      "menos completa — a norma especial pode descrever tanto um crime mais leve quanto um mais grave.",
      "o princípio da especialidade é o único previsto expressamente no Código Penal."],
     1, "3.1 — Princípio da especialidade",
     "A identificação de qual norma é geral e qual é especial se faz por comparação ABSTRATA entre as "
     "descrições típicas (ex.: homicídio × infanticídio), e não pela análise do caso concreto — por isso a "
     "alternativa que afirma o contrário é a incorreta."),
    ("\"Um fato definido por uma norma incriminadora é meio necessário ou normal fase de preparação ou "
     "execução de outro crime, bem como quando constitui conduta anterior ou posterior do agente, cometida "
     "com a mesma finalidade prática atinente àquele crime.\" No conflito aparente de normas, esta "
     "afirmação explica o princípio da:",
     ["especialidade.", "subsidiariedade.", "alternatividade.", "consunção."],
     3, "3.1 — Consunção",
     "É a definição clássica do princípio da consunção (ou absorção): o fato mais amplo e grave absorve os "
     "fatos menos amplos que funcionam como meio de preparação, execução ou exaurimento daquele."),
]

with open('questions.json', encoding='utf-8') as f:
    qdata = json.load(f)

next_id = max(q['id'] for q in qdata) + 1
added = 0
for enun, alts, resp_idx, assunto, exp in MC_QUESTIONS:
    qdata.append({
        "id": next_id,
        "corp": "PCPE",
        "disc": "Direito Penal",
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
print('OK --', added, 'questoes de Direito Penal (PC-PE, MC) adicionadas. Total no banco:', len(check))

with open('questions.json', encoding='utf-8') as f:
    qdata_raw = f.read()
with open('app-template.html', encoding='utf-8') as f:
    html2 = f.read()
html2 = html2.replace('__QUESTIONS_JSON__', qdata_raw)
with open('estudo-cebraspe-ma.html', 'w', encoding='utf-8') as f:
    f.write(html2)
print('estudo-cebraspe-ma.html regenerado com sucesso')
