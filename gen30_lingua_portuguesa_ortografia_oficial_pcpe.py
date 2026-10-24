# -*- coding: utf-8 -*-
# Complementa o deck de Lingua Portuguesa (PC-PE) com o conteudo do
# segundo material da Focus Concursos: regras de ortografia oficial
# (S, SS, ç, X, G, Z, isar/izar), expressoes que geram duvidas,
# homonimos e paronimos -- alem das 5 novas questoes Certo/Errado
# (textos CESPE sobre arquitetura/jornalismo). Fonte:
# "material (5).pdf" -- Lingua Portuguesa, Dominio da Ortografia
# Oficial, Profa. Maria Augusta G. Almeida, Focus Concursos.
import json

with open('app-template.html', encoding='utf-8') as f:
    html = f.read()

NEW_ITEMS = [
    {"t": "sec", "x": "Ortografia oficial — regras de grafia"},
    {"t": "art", "n": "Regra do S — substantivos/adjetivos de verbos terminados em -CORR, -ND, -PEL, -RG, -RT",
     "x": "Escrevem-se com S os substantivos e adjetivos relacionados a verbos que têm, no final do "
          "radical do infinitivo, -corr, -nd, -pel, -rg, -rt.",
     "s": "Ex.: recorrer–recurso, concorrer–concurso, distender–distensão, ascender–ascensão, "
          "expelir–expulsão, compelir–compulsão, emergir–emersão, aspergir–aspersão, inverter–inversão, "
          "reverter–reversão."},
    {"t": "art", "n": "Regra do SS — verbos terminados em -CED, -GRED, -PRIM, -MET, -TIR",
     "x": "Escrevem-se com SS os substantivos cujos verbos cognatos têm radical terminado em -ced, "
          "-gred, -prim, -met, ou cujo infinitivo termina em -tir.",
     "s": "Ex.: ceder–cessão, suceder–sucessão, agredir–agressão, progredir–progressão, "
          "imprimir–impressão, suprimir–supressão, intrometer–intromissão, prometer–promessa, "
          "remeter–remessa, admitir–admissão, demitir–demissão, permitir–permissão, discutir–discussão, "
          "repercutir–repercussão."},
    {"t": "art", "n": "Regra do Ç — verbos terminados em -TER",
     "x": "Escrevem-se com Ç os substantivos cujos verbos cognatos terminam o infinitivo em -ter.",
     "s": "Ex.: ater–atenção, reter–retenção, deter–detenção, obter–obtenção, manter–manutenção."},
    {"t": "art", "n": "Regra do X — após ditongo e em EN-/ME- seguidos do fonema \"x\"",
     "x": "Usa-se X após ditongo (ex.: caixa, peixe, feixe, trouxa, faixa, caixote, frouxa — exceções: "
          "caucho e recauchutar). Usa-se X em palavras iniciadas por \"en\" seguido do fonema \"x\" "
          "(ex.: enxofre, enxada, enxame, enxaqueca, enxaguar — exceções: encher e seus derivados "
          "encharcar, enchumbar, enchapelar, enchova, enchumaçar). Usa-se X em palavras iniciadas por "
          "\"me\" seguido do fonema \"x\" (ex.: mexerica, mexilhão, México — exceção: mecha)."},
    {"t": "art", "n": "Regra do G — substantivos terminados em -AGEM, -IGEM, -UGEM",
     "x": "Usa-se G em substantivos terminados em -agem, -igem, -ugem (ex.: penugem, fuligem, folhagem, "
          "coragem, ferrugem — exceções: lambujem e pajem). Atenção: isso vale só para o SUBSTANTIVO — "
          "o verbo correspondente na 3ª pessoa do presente do subjuntivo usa J: coragem (subst.) × "
          "encorajem (verbo); viagem (subst.) × viajem (verbo); ferrugem (subst.) × enferrujem (verbo)."},
    {"t": "art", "n": "Uso do S — profissões, títulos, origem, nacionalidade e ocupações femininas",
     "x": "Usa-se S em substantivos e adjetivos que definam profissões, títulos honoríficos, origem ou "
          "nacionalidade (ex.: freguês, camponês, japonês, inglês, português, duquesa, marquesa, "
          "francesa, inglesa, holandesa), e também nos vocábulos que expressam ocupações femininas "
          "(ex.: poetisa, sacerdotisa, pitonisa, profetisa)."},
    {"t": "art", "n": "Uso do Z — substantivos abstratos derivados de adjetivos",
     "x": "Usa-se Z em substantivos abstratos derivados de adjetivos.",
     "s": "Ex.: leve–leveza, avaro–avareza, áspero–aspereza, nobre–nobreza, ácido–acidez, "
          "rígido–rigidez, rude–rudeza, ávido–avidez."},
    {"t": "art", "n": "Verbos terminados em -ISAR e -IZAR",
     "x": "Quando o substantivo de origem já tem S, o verbo derivado mantém S (pesquisa–pesquisar, "
          "liso–alisar, paralisia–paralisar, análise–analisar, improviso–improvisar). Quando o "
          "substantivo de origem já tem Z, o verbo derivado mantém Z (vez–revezar, cicatriz–cicatrizar, "
          "raiz–enraizar, capuz–encapuzar, menosprezo–menosprezar). Quando o substantivo de origem NÃO "
          "tem nem S nem Z, usa-se Z no verbo (padrão–padronizar, região–regionalizar, legal–legalizar, "
          "aval–avalizar, frágil–fragilizar, cristal–cristalizar).",
     "s": "Atenção às exceções clássicas, em que o substantivo termina em -SE mas o verbo leva Z: "
          "catequese–catequizar, ênfase–enfatizar, síntese–sintetizar, parabéns–parabenizar, "
          "hipnose–hipnotizar."},
    {"t": "sec", "x": "Expressões que geram dúvidas"},
    {"t": "art", "n": "A cerca de / Há cerca de / Acerca de",
     "x": "A CERCA DE = aproximadamente, referindo-se a tempo futuro ou distância (\"Daqui a cerca de "
          "dois meses...\"; \"Ele mora a cerca de dois quilômetros...\"). HÁ CERCA DE = tempo decorrido "
          "ou existência, com o verbo haver (\"Há cerca de dois anos, estive em Paquetá\"; \"Há cerca de "
          "dez pousadas nesta região\"). ACERCA DE = sobre, a respeito de (\"Conversamos muito acerca "
          "das provas\")."},
    {"t": "art", "n": "A fim de / Afim de",
     "x": "A FIM DE (separado) = finalidade, objetivo (\"Ele estuda a fim de realizar um sonho antigo\"). "
          "AFIM (junto, adjetivo) = semelhante, similar (\"Eles sempre tinham ideias afins\")."},
    {"t": "art", "n": "À medida que / Na medida em que",
     "x": "À MEDIDA QUE = à proporção que, ideia de proporcionalidade (\"À medida que comia doces, "
          "engordava\"). NA MEDIDA EM QUE = porque, devido a, ideia causal (\"Na medida em que trabalha "
          "com seriedade, colhe bons frutos\"). NÃO EXISTE a expressão \"à medida em que\" — é um erro "
          "comum misturar as duas formas."},
    {"t": "art", "n": "A princípio / Em princípio",
     "x": "A PRINCÍPIO = no início (\"A princípio eles nunca brigavam\"). EM PRINCÍPIO = em tese, em "
          "regra (\"Em princípio, ele é inocente, até que se prove o contrário\")."},
    {"t": "art", "n": "Ao encontro de / De encontro a",
     "x": "AO ENCONTRO DE = a favor de, em concordância (\"O que ele fez foi ao encontro dos pedidos "
          "dos alunos\"). DE ENCONTRO A = contra, em oposição (\"Suas palavras iam de encontro a seus "
          "atos\")."},
    {"t": "art", "n": "Ao invés de / Em vez de",
     "x": "AO INVÉS DE = ao contrário de, ideias opostas (\"Ao invés de chorar, ele gargalhou\"). EM VEZ "
          "DE = em lugar de, substituição (\"Em vez de estudar Penal, ele estudou Administrativo\")."},
    {"t": "art", "n": "Expectador / Espectador",
     "x": "EXPECTADOR = aquele que está na expectativa de algo (\"Expectador de receber grande herança, "
          "ele já gastava por conta\"). ESPECTADOR = aquele que assiste a algo (\"Espectador do jogo, "
          "roía as unhas, muito nervoso\")."},
    {"t": "art", "n": "Senão / Se não",
     "x": "SENÃO (junto) = a não ser, com exceção de, ou caso contrário (\"Senão ele, quem nos poderia "
          "ajudar?\"; \"Eles devem trabalhar muito, senão a falência será inevitável\"). SE NÃO "
          "(separado) = ideia de condição negativa (\"Se não houver chuvas fortes, teremos várias "
          "festas na cidade\")."},
    {"t": "art", "n": "Por hora / Por ora",
     "x": "POR HORA = por 60 minutos, uma hora de tempo (\"Ele ganha R$ 50,00 por hora de trabalho\"). "
          "POR ORA = por enquanto (\"Por ora, não temos uma decisão acerca da compra do imóvel\")."},
    {"t": "art", "n": "Ver / Vir (confusão nas formas verbais)",
     "x": "VER no infinitivo pessoal (\"Para eu ver o filme, precisarei sair mais cedo\") não deve ser "
          "confundido com VIR no futuro do subjuntivo do verbo VER, que se escreve \"vir\" "
          "(\"Quando eu vir o filme, poderei dar minha opinião\")."},
    {"t": "art", "n": "Sequer / Se quer",
     "x": "SEQUER (junto) = nem, tampouco, ao menos (\"Ele não trabalha, sequer estuda\"). SE QUER "
          "(separado) = caso + verbo querer, ideia de condição (\"Se quer ter bons resultados, lute "
          "por eles!\")."},
    {"t": "art", "n": "Demais / De mais",
     "x": "DEMAIS (junto) = muito, como advérbio de intensidade (\"Ele come demais\"), ou = os outros, "
          "como pronome (\"Alguns ficaram em casa; os demais saíram\"). DE MAIS (separado) = muitos, "
          "o contrário de \"de menos\" (\"Comprei móveis de mais para a sala\"; \"Havia pessoas de mais "
          "na fila de ingressos\")."},
    {"t": "art", "n": "Porque / Por que / Porquê / Por quê",
     "x": "PORQUE (junto, sem acento) = conjunção explicativa/causal, equivale a pois, já que, visto "
          "que (\"Ele venceu porque lutou muito\"). POR QUE (separado, sem acento) = usado quando se "
          "pode subentender \"motivo\" ou \"razão\" depois do termo, em pergunta direta ou indireta "
          "(\"Não entendi por que ele não gostou da peça\"), ou quando pode ser substituído por \"pelo "
          "qual/pela qual/pelos quais/pelas quais\" (\"As mudanças por que lutavam eram necessárias\"). "
          "PORQUÊ (junto, com acento) = substantivo, vem precedido de artigo (\"Não sabemos o porquê de "
          "tal atitude\"). POR QUÊ (separado, com acento) = usado no final de frase ou antes de uma "
          "pausa (pontuação), quando se pode subentender \"motivo\" ou \"razão\" (\"Os imóveis tiveram "
          "seu preço reduzido e não sabemos por quê\")."},
    {"t": "sec", "x": "Significação de palavras"},
    {"t": "art", "n": "Homônimos — grafia ou fonética iguais, significados diferentes",
     "x": "Principais pares: acender (atear fogo)/ascender (subir); bucho (estômago de animal)/buxo "
          "(arbusto); caçar (perseguir)/cassar (anular); cela (compartimento)/sela (arreio); censo "
          "(recenseamento)/senso (juízo); cerração (nevoeiro)/serração (ato de serrar); cidra "
          "(fruto)/sidra (vinho de maçã); concertar (harmonizar)/consertar (reparar); insipiente "
          "(ignorante)/incipiente (iniciante); laço (nó)/lasso (frouxo); paço (palácio)/passo (andar); "
          "seção (divisão, parte)/sessão (reunião); tacha (prego)/taxa (imposto)."},
    {"t": "art", "n": "Parônimos — grafia e pronúncia parecidas, significados diferentes",
     "x": "Principais pares: absolver (perdoar)/absorver (consumir); aprender (instruir-se)/apreender "
          "(assimilar); área (medida)/ária (peça musical); arrear (pôr arreios)/arriar (abaixar); "
          "comprimento (extensão)/cumprimento (saudação); costear (navegar junto à costa)/custear "
          "(financiar); deferir (conceder)/diferir (adiar); degredado (exilado)/degradado (rebaixado); "
          "delatar (denunciar)/dilatar (ampliar); descrição (descrever)/discrição (ser discreto); "
          "descriminar (inocentar)/discriminar (distinguir); despensa (mantimentos)/dispensa (isenção); "
          "despercebido (não percebido)/desapercebido (desprovido); discente (aluno)/docente "
          "(professor); emergir (vir à tona)/imergir (mergulhar); emigrar (sair do país)/imigrar "
          "(entrar no país); eminente (ilustre)/iminente (prestes a acontecer)."},
    {"t": "art", "n": "Parônimos (continuação)",
     "x": "Mais pares: estufar (aquecer)/estofar (encher); flagrante (evidente)/fragrante (perfumado); "
          "fluir (correr)/fruir (desfrutar); imoral (contrário à moral)/amoral (nem a favor nem contra "
          "a moral); indefeso (sem defesa)/indefesso (incansável); infligir (aplicar)/infringir "
          "(transgredir); intimorato (corajoso)/intemerato (íntegro, puro); mandato (procuração)/"
          "mandado (ordem judicial); pleito (demanda, eleição)/preito (homenagem); precedente "
          "(antecedente)/procedente (proveniente); prescrever (ordenar)/proscrever (condenar); "
          "recreação (diversão)/recriação (ato de recriar); retificar (corrigir)/ratificar (confirmar); "
          "soar (produzir som)/suar (transpirar); sortir (abastecer)/surtir (resultar); tráfego "
          "(trânsito)/tráfico (comércio ilícito); vadear (atravessar o rio a pé)/vadiar (viver no "
          "ócio); vultoso (de grande vulto)/vultuoso (inchado)."},
]

old_last_item = ('{"t": "art", "n": "Derivados de TER e VIR", "x": "O mesmo padrão (singular sem acento / '
                 'plural com acento) vale para os verbos derivados de TER e VIR. Ex.: OBTER — ele obtém / '
                 'eles obtêm. INTERVIR — ele intervém / eles intervêm. Outros exemplos comuns: manter (ele '
                 'mantém/eles mantêm), conter (contém/contêm), convir (convém/convêm)."}\n];')
assert old_last_item in html, "fim do array TEORIA_LINGUA_PORTUGUESA_PCPE nao encontrado como esperado"

new_items_literal = ',\n' + ',\n'.join(json.dumps(it, ensure_ascii=False) for it in NEW_ITEMS)
new_last_item = old_last_item[:-2] + new_items_literal + '\n];'  # remove o "];" antigo e reconstroi
html = html.replace(old_last_item, new_last_item, 1)

with open('app-template.html', 'w', encoding='utf-8', newline='') as f:
    f.write(html)
print('TEORIA_LINGUA_PORTUGUESA_PCPE complementada com', len(NEW_ITEMS), 'novos itens.')

CE_QUESTIONS = [
    ("Seria preservada a correção gramatical e os sentidos do texto caso o termo “Por que”, "
     "no trecho “– Por que arquitetura?”, fosse substituído por Por qual.", False,
     "Por que / Por qual (interrogativo)",
     "Errado — nesse trecho, “por que” equivale a “por qual motivo/razão” "
     "(pergunta sobre a causa da escolha pela arquitetura). Substituí-lo por “por qual” "
     "isoladamente muda o sentido da pergunta (passaria a perguntar “qual arquitetura”, e não "
     "“por que razão a arquitetura”), prejudicando tanto a correção quanto o sentido "
     "original."),
    ("Em “A despeito de não entender por quê, eu deveria tirá-lo da equipe” e “A "
     "despeito de não entender por quê, após três longos anos de trabalho produtivo, eu deveria "
     "demiti-lo, tal atitude me era inevitável”, fez-se uso adequado dos termos grifados.", True,
     "Por quê (final de frase/antes de pausa)",
     "Correto — em ambos os casos, “por quê” vem seguido de uma pausa (vírgula) e pode-se "
     "subentender “motivo” ou “razão” logo depois dele (“não entender por quê "
     "[motivo]”), o que exige a forma separada e acentuada “por quê”."),
    ("Em “Os prognósticos sobre os resultados daquele empreendimento tão vultoso não eram os "
     "melhores”, a substituição de “sobre os resultados” por “a cerca dos "
     "resultados” não prejudicaria a correção do período.", False,
     "Acerca de × A cerca de",
     "Errado — “sobre”, no sentido de “a respeito de”, deveria ser substituído por "
     "“acerca de” (uma só palavra). A forma “a cerca de” (separada) significa "
     "aproximadamente (tempo ou distância), não “a respeito de”, de modo que a substituição "
     "alteraria o sentido e prejudicaria a correção do período."),
    ("O trecho “Durante a seção de treinamento, fez-se a discrição de métodos a serem utilizados "
     "apenas pelos técnicos mais expertos” apresenta uso inadequado de homônimos e parônimos.",
     True, "Homônimos e Parônimos",
     "Correto — “seção” (divisão, parte) foi usada no lugar de “sessão” (reunião, "
     "encontro, que é o sentido correto para uma sessão de treinamento), e “discrição” "
     "(qualidade de discreto) foi usada no lugar de “descrição” (ato de descrever métodos), "
     "configurando dois usos inadequados de homônimos/parônimos no mesmo trecho."),
    ("Em “À medida que fazia uso daqueles medicamentos, mais apresentava sintomas "
     "incapacitantes”, a substituição de “à medida que” por “na medida em que” "
     "não prejudicaria a correção nem o sentido original do período.", False,
     "À medida que × Na medida em que",
     "Errado — “à medida que” expressa proporcionalidade (quanto mais usava o medicamento, "
     "mais sintomas apresentava), enquanto “na medida em que” tem valor causal (porque, "
     "devido a). A substituição é gramaticalmente possível, mas MUDA o sentido original, de uma relação "
     "proporcional para uma relação de causa."),
]

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

with open('questions.json', encoding='utf-8') as f:
    qdata_raw = f.read()
with open('app-template.html', encoding='utf-8') as f:
    html2 = f.read()
html2 = html2.replace('__QUESTIONS_JSON__', qdata_raw)
with open('estudo-cebraspe-ma.html', 'w', encoding='utf-8') as f:
    f.write(html2)
print('estudo-cebraspe-ma.html regenerado com sucesso')
