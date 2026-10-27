# -*- coding: utf-8 -*-
# Adiciona 18 questoes de multipla escolha (estilo CEBRASPE, por
# pedido explicito do usuario) sobre o Art. 5 da Constituicao
# Federal (Direitos e Garantias Fundamentais) pra PC-PE, disc
# "Direito Constitucional". O deck de leitura ja foi movido de
# Estrategia pra Legislacao via Edit direto (LAW_DECKS +
# LEITURA_DECK_TO_DISC), consistente com a observacao do usuario de
# que "a materia e direito constitucional" e deve ficar junto com os
# demais conteudos de legislacao.
import json

CE_LIKE_MC_QUESTIONS = [
    ("Segundo o art. 5º, caput, da CF/88, a igualdade perante a lei é garantida:",
     ["exclusivamente aos brasileiros natos.",
      "aos brasileiros e aos estrangeiros residentes no País.",
      "apenas aos brasileiros natos e naturalizados.",
      "a todos os estrangeiros, residentes ou não, no território nacional.",
      "exclusivamente aos cidadãos no gozo de direitos políticos."],
     1, "Art. 5º, caput",
     "O caput do art. 5º garante a inviolabilidade dos direitos ali listados \"aos brasileiros e "
     "aos estrangeiros residentes no País\" — não a todo e qualquer estrangeiro, mas aos residentes."),
    ("Conforme o art. 5º, II, da CF/88, ninguém será obrigado a fazer ou deixar de fazer alguma "
     "coisa senão:",
     ["por determinação de autoridade administrativa competente.",
      "em virtude de decisão judicial transitada em julgado.",
      "em virtude de lei.",
      "por ordem direta de autoridade policial.",
      "mediante decreto do Chefe do Poder Executivo."],
     2, "Art. 5º, II — Princípio da legalidade",
     "O inciso II consagra o princípio da legalidade em sentido amplo: só a lei pode obrigar alguém "
     "a fazer ou deixar de fazer algo, não bastando ato administrativo, decisão judicial isolada, "
     "ordem policial ou decreto."),
    ("De acordo com o art. 5º, XI, da CF/88, a casa é asilo inviolável do indivíduo. É correto "
     "afirmar que, sem consentimento do morador, é possível nela penetrar:",
     ["a qualquer hora, mediante simples suspeita de crime.",
      "em caso de flagrante delito ou desastre, para prestar socorro, ou, durante o dia, por "
      "determinação judicial.",
      "somente mediante autorização do Ministério Público.",
      "a qualquer hora, desde que haja mandado de busca e apreensão.",
      "exclusivamente durante a noite, por ordem judicial."],
     1, "Art. 5º, XI — Inviolabilidade de domicílio",
     "O texto constitucional admite entrada sem consentimento em quatro hipóteses: flagrante "
     "delito, desastre, prestação de socorro (a qualquer hora), ou por determinação judicial — mas "
     "esta última apenas durante o dia."),
    ("Sobre o inciso XII do art. 5º da CF/88 (sigilo das comunicações), é correto afirmar que:",
     ["o sigilo da correspondência e das comunicações telefônicas é absoluto, não admitindo "
      "exceção.",
      "apenas o sigilo das comunicações telefônicas pode ser excepcionado, mediante ordem judicial, "
      "nas hipóteses e forma que a lei estabelecer para investigação criminal ou instrução "
      "processual penal.",
      "o sigilo de dados pode ser quebrado por autoridade policial, independentemente de ordem "
      "judicial.",
      "o sigilo da correspondência pode ser quebrado por determinação do Poder Legislativo.",
      "todas as formas de sigilo previstas no inciso podem ser quebradas mediante simples "
      "requisição do Ministério Público, sem necessidade de ordem judicial."],
     1, "Art. 5º, XII — Sigilo das comunicações",
     "O inciso XII só admite exceção expressa para as comunicações telefônicas (\"no último "
     "caso\"), e ainda assim por ordem judicial, nas hipóteses e forma que a lei estabelecer, para "
     "investigação criminal ou instrução processual penal."),
    ("O inciso XXXIX do art. 5º da CF/88 consagra o princípio da:",
     ["anterioridade tributária.", "legalidade penal.", "irretroatividade tributária.",
      "presunção de inocência.", "individualização da pena."],
     1, "Art. 5º, XXXIX — Legalidade penal",
     "\"Não há crime sem lei anterior que o defina, nem pena sem prévia cominação legal\" é a "
     "formulação constitucional do princípio da legalidade penal (nullum crimen, nulla poena sine "
     "lege)."),
    ("Nos termos do art. 5º, XL, da CF/88, a lei penal:",
     ["retroagirá sempre, independentemente de beneficiar ou prejudicar o réu.",
      "jamais retroagirá, em qualquer hipótese.",
      "retroagirá apenas para beneficiar o réu.",
      "retroagirá apenas em crimes hediondos.",
      "retroagirá apenas quando determinado por tratado internacional."],
     2, "Art. 5º, XL — Irretroatividade da lei penal",
     "A regra é a irretroatividade da lei penal, com a única exceção constitucional de retroagir "
     "para beneficiar o réu (retroatividade da lei penal mais benéfica)."),
    ("Segundo o art. 5º, XLII, da CF/88, a prática do racismo constitui crime:",
     ["afiançável e prescritível.", "inafiançável e prescritível.", "afiançável e imprescritível.",
      "inafiançável e imprescritível.", "sujeito apenas a pena de multa."],
     3, "Art. 5º, XLII — Racismo",
     "O racismo é crime inafiançável e imprescritível, sujeito a pena de reclusão, nos termos da "
     "lei."),
    ("Conforme o art. 5º, XLV, da CF/88, a obrigação de reparar o dano e a decretação do "
     "perdimento de bens podem, nos termos da lei, ser estendidas aos sucessores do condenado:",
     ["de forma ilimitada, alcançando todo o patrimônio familiar.",
      "até o limite do valor do patrimônio transferido.",
      "somente se os sucessores também forem condenados no mesmo processo.",
      "apenas em crimes hediondos.",
      "nunca, pois a pena não passa da pessoa do condenado em nenhuma hipótese."],
     1, "Art. 5º, XLV — Intranscendência da pena",
     "A pena não passa da pessoa do condenado, mas a obrigação de reparar o dano e o perdimento de "
     "bens podem ser estendidos aos sucessores, LIMITADOS ao valor do patrimônio transferido."),
    ("O devido processo legal, previsto no art. 5º, LIV, da CF/88, estabelece que ninguém será "
     "privado:",
     ["apenas da liberdade, sem processo legal.", "apenas de seus bens, sem processo legal.",
      "da liberdade ou de seus bens, sem o devido processo legal.",
      "de sua nacionalidade, sem processo legal.",
      "de seus direitos políticos, sem processo legal."],
     2, "Art. 5º, LIV — Devido processo legal",
     "O devido processo legal abrange tanto a privação da liberdade quanto a privação de bens, "
     "sempre exigindo processo regular."),
    ("Nos termos do art. 5º, LVI, da CF/88, são inadmissíveis no processo:",
     ["as provas testemunhais contraditórias.", "as provas obtidas por meios ilícitos.",
      "as provas periciais produzidas por perito não oficial.",
      "as provas documentais sem reconhecimento de firma.",
      "os depoimentos de réus colaboradores."],
     1, "Art. 5º, LVI — Provas ilícitas",
     "O inciso LVI veda expressamente a admissão, no processo, de provas obtidas por meios "
     "ilícitos."),
    ("O princípio da presunção de inocência, consagrado no art. 5º, LVII, da CF/88, estabelece que "
     "ninguém será considerado culpado até:",
     ["o oferecimento da denúncia pelo Ministério Público.",
      "a prolação da sentença de primeiro grau.",
      "o trânsito em julgado de sentença penal condenatória.",
      "o encerramento do inquérito policial.",
      "a decisão de pronúncia, nos crimes de competência do júri."],
     2, "Art. 5º, LVII — Presunção de inocência",
     "A presunção de inocência (ou de não culpabilidade) perdura até o trânsito em julgado de "
     "sentença penal condenatória, e não até fases anteriores do processo."),
    ("De acordo com o art. 5º, LXIII, da CF/88, o preso será informado de seus direitos, entre os "
     "quais:",
     ["o de ser solto imediatamente após o pagamento de fiança.",
      "o de permanecer calado, sendo-lhe assegurada a assistência da família e de advogado.",
      "o de escolher o estabelecimento prisional onde cumprirá a pena.",
      "o de ser julgado exclusivamente pelo tribunal do júri.",
      "o de receber indenização imediata pelo Estado."],
     1, "Art. 5º, LXIII — Direito ao silêncio",
     "O inciso LXIII assegura ao preso o direito de permanecer calado, bem como a assistência da "
     "família e de advogado."),
    ("O remédio constitucional cabível sempre que alguém sofrer ou se achar ameaçado de sofrer "
     "violência ou coação em sua liberdade de locomoção, por ilegalidade ou abuso de poder, é:",
     ["o mandado de segurança.", "o mandado de injunção.", "o habeas data.", "o habeas corpus.",
      "a ação popular."],
     3, "Art. 5º, LXVIII — Habeas corpus",
     "O habeas corpus protege especificamente a liberdade de locomoção contra ilegalidade ou abuso "
     "de poder."),
    ("O mandado de segurança, previsto no art. 5º, LXIX, da CF/88, destina-se a proteger direito "
     "líquido e certo, não amparado por habeas corpus ou habeas data, quando o responsável pela "
     "ilegalidade ou abuso de poder for:",
     ["exclusivamente autoridade pública.",
      "qualquer particular, independentemente de função pública.",
      "autoridade pública ou agente de pessoa jurídica no exercício de atribuições do Poder "
      "Público.",
      "exclusivamente agente de empresa privada sem vínculo com o Poder Público.",
      "exclusivamente o Chefe do Poder Executivo."],
     2, "Art. 5º, LXIX — Mandado de segurança",
     "O texto constitucional abrange tanto a autoridade pública quanto o agente de pessoa jurídica "
     "que, no exercício de atribuições do Poder Público, pratique a ilegalidade ou abuso."),
    ("Qualquer cidadão é parte legítima para propor a ação prevista no art. 5º, LXXIII, da CF/88, "
     "que visa a anular ato lesivo ao patrimônio público, à moralidade administrativa, ao meio "
     "ambiente e ao patrimônio histórico e cultural. Trata-se:",
     ["do mandado de segurança coletivo.", "da ação popular.", "do habeas data.",
      "do mandado de injunção.", "da ação civil pública."],
     1, "Art. 5º, LXXIII — Ação popular",
     "A ação popular é o instrumento que qualquer cidadão (não qualquer pessoa jurídica ou "
     "entidade) pode propor para anular ato lesivo ao patrimônio público, à moralidade "
     "administrativa, ao meio ambiente e ao patrimônio histórico e cultural."),
    ("São características do Tribunal do Júri asseguradas pelo art. 5º, XXXVIII, da CF/88, "
     "EXCETO:",
     ["a plenitude de defesa.", "o sigilo das votações.", "a soberania dos veredictos.",
      "a competência para o julgamento dos crimes dolosos contra a vida.",
      "a possibilidade de recurso automático contra qualquer decisão absolutória, "
      "independentemente de recurso da acusação."],
     4, "Art. 5º, XXXVIII — Tribunal do Júri",
     "O inciso XXXVIII assegura apenas quatro garantias: plenitude de defesa, sigilo das votações, "
     "soberania dos veredictos e competência para julgar os crimes dolosos contra a vida — não há "
     "previsão de recurso automático de ofício contra absolvição."),
    ("O Estado prestará assistência jurídica integral e gratuita, nos termos do art. 5º, LXXIV, da "
     "CF/88:",
     ["a todos os cidadãos brasileiros, independentemente de renda.", "apenas aos presos.",
      "aos que comprovarem insuficiência de recursos.",
      "apenas aos réus em processos criminais.",
      "apenas em causas cíveis de valor inferior a determinado teto."],
     2, "Art. 5º, LXXIV — Assistência jurídica gratuita",
     "O direito à assistência jurídica integral e gratuita é condicionado à comprovação de "
     "insuficiência de recursos, não sendo universal nem restrito a presos ou a causas criminais."),
    ("Conforme o art. 5º, LXXII, da CF/88, o habeas data é cabível para assegurar o conhecimento "
     "de informações relativas à pessoa do impetrante constantes de registros ou bancos de dados "
     "de entidades governamentais ou de caráter público, bem como para:",
     ["a obtenção de indenização por danos morais.",
      "a retificação de dados, quando não se prefira fazê-lo por processo sigiloso, judicial ou "
      "administrativo.",
      "a anulação de ato lesivo ao patrimônio público.",
      "a suspensão de atividades de associação.",
      "a proteção de direito líquido e certo não amparado por habeas corpus."],
     1, "Art. 5º, LXXII — Habeas data",
     "A alínea \"b\" do inciso LXXII prevê o habeas data também para a retificação de dados, "
     "quando o impetrante não prefira fazê-lo por processo sigiloso, judicial ou administrativo."),
]

with open('questions.json', encoding='utf-8') as f:
    qdata = json.load(f)

next_id = max(q['id'] for q in qdata) + 1
added = 0
for enun, alts, resp_idx, assunto, exp in CE_LIKE_MC_QUESTIONS:
    qdata.append({
        "id": next_id,
        "corp": "PCPE",
        "disc": "Direito Constitucional",
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
print('OK --', added, 'questoes de Direito Constitucional (PC-PE, MC) adicionadas. Total no banco:', len(check))

with open('questions.json', encoding='utf-8') as f:
    qdata_raw = f.read()
with open('app-template.html', encoding='utf-8') as f:
    html2 = f.read()
html2 = html2.replace('__QUESTIONS_JSON__', qdata_raw)
with open('estudo-cebraspe-ma.html', 'w', encoding='utf-8') as f:
    f.write(html2)
print('estudo-cebraspe-ma.html regenerado com sucesso')
