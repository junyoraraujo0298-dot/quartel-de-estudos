# -*- coding: utf-8 -*-
# Acrescenta a TEORIA_COMBATE_INCENDIO o conteudo de "Fases do Incendio"
# (inicial, crescimento, desenvolvimento completo, decaimento) e dos
# fenomenos extremos do fogo (flashover, backdraft, rollover), baseado
# no PDF Focado da Focus Concursos, complementado com conhecimento
# consolidado de ciencia do fogo. Adiciona 10 questoes de multipla
# escolha dificeis (corp BM).
import json
import re

with open('questions.json', encoding='utf-8') as f:
    raw = f.read()

data_check = json.loads(raw)
max_id = max(q['id'] for q in data_check)
assert max_id == 974, max_id

with open('app-template.html', encoding='utf-8') as f:
    html = f.read()

NEW_TEORIA_ITEMS = [
    {"t": "cap", "x": "Fases do Incêndio (Desenvolvimento do Incêndio)"},
    {"t": "art", "n": "As 4 fases do incêndio estrutural (confinado)",
     "x": "O desenvolvimento de um incêndio estrutural (confinado) ocorre em 4 fases: inicial, "
          "crescimento, desenvolvimento completo e decaimento. A temperatura do ambiente sobe "
          "lentamente na fase inicial, acelera bruscamente na fase de crescimento, atinge o pico na "
          "fase de desenvolvimento completo e cai gradualmente na fase de decaimento — formando a "
          "clássica \"curva de desenvolvimento do incêndio\" (temperatura x tempo).",
     "s": "Decore a sequência: INICIAL → CRESCIMENTO → DESENVOLVIMENTO COMPLETO → DECAIMENTO. É a "
          "base para entender onde cada fenômeno extremo (flashover, backdraft) se encaixa."},
    {"t": "art", "n": "Fase Inicial",
     "x": "Começa a partir da ignição de algum material combustível no interior do ambiente, com o "
          "foco de incêndio ainda pequeno. Não se verifica aumento significativo de temperatura, "
          "existindo ainda todo o suprimento de combustível e comburente a ser consumido. Pode ser "
          "identificada por um pequeno foco isolado, com chama e pouca fumaça sendo produzida.",
     "s": "Fase inicial = \"tudo ainda abundante\": sobra combustível, sobra comburente, a temperatura "
          "mal subiu."},
    {"t": "art", "n": "Fase de Crescimento",
     "x": "Ainda há considerável material combustível, que, com a elevação da temperatura, libera "
          "grande volume de gases inflamáveis; a concentração de comburente ainda disponível permite "
          "a rápida evolução do incêndio. A elevação de temperatura segue progressão muito acelerada, "
          "podendo atingir valores próximos a 600°C em menos de 3 minutos. Em determinado ponto, "
          "todos os combustíveis do cômodo sofrem pirólise simultaneamente, recebendo calor por "
          "radiação da fumaça, do teto e das paredes (fenômeno conhecido como feedback radiativo).",
     "s": "Decore o número: até ~600°C em menos de 3 minutos — mostra como a fase de crescimento é "
          "brutalmente rápida. O \"feedback radiativo\" é o que acelera a pirólise simultânea de tudo "
          "no ambiente, preparando o terreno para o flashover."},
    {"t": "art", "n": "Fase de Desenvolvimento Completo",
     "x": "Ocorre o consumo de todo o combustível disponível; o incêndio atinge seu ápice de produção "
          "de energia, com temperatura podendo ultrapassar 1000°C. Nesse ponto, o comburente já não é "
          "suficiente para manter ativa toda a reação de combustão, e, paralelamente, a disponibilidade "
          "de combustível também começa a diminuir (as chamas já consomem todo o material disponível). "
          "Tudo o que se vê no ambiente são chamas vivas, turbulentas e volumosas.",
     "s": "PEGADINHA: na fase de desenvolvimento completo, comburente E combustível diminuem "
          "SIMULTANEAMENTE — não é só um ou só o outro. É o pico de temperatura (>1000°C), não o pico "
          "de disponibilidade de material."},
    {"t": "art", "n": "Fase de Decaimento",
     "x": "Após o consumo da disponibilidade dos materiais, ou escassez de comburente, o ambiente "
          "entra em fase de liberação do excesso de energia e queda natural da temperatura. Há ainda "
          "forte presença de combustão incompleta e grande taxa de liberação de monóxido de carbono "
          "(CO), que, se não se incendiar devido às baixas temperaturas, representa risco a quem "
          "respirar esse ar sem equipamento autônomo de proteção respiratória (EPR/SCBA).",
     "s": "PEGADINHA clássica: \"as chamas diminuíram, já pode tirar a máscara\" está ERRADO — a fase "
          "de decaimento ainda é extremamente perigosa pela alta concentração de CO no ar, mesmo sem "
          "chamas visíveis."},
    {"t": "cap", "x": "Fenômenos Extremos do Fogo"},
    {"t": "art", "n": "Visão geral — \"incêndios de propagação rápida\"",
     "x": "Os fenômenos de comportamento extremo do fogo estão todos associados à ignição da fumaça "
          "que, sendo combustível, queima ao entrar em mistura adequada com o oxigênio e receber "
          "energia suficiente. Têm ocorrência repentina — por isso são chamados, na doutrina de língua "
          "inglesa, de \"incêndios de propagação rápida\" (rapid fire progress) — e se reúnem em 3 "
          "grupos: generalização do incêndio (flashover), explosão da fumaça (backdraft) e outros "
          "fenômenos de ignição da fumaça (como o rollover). Ocorrem em espaço físico limitado "
          "(confinado ou compartimentado, com portas/janelas fechadas dificultando o escoamento da "
          "fumaça) e surgem com POUCO tempo de queima — não exigem longos períodos.",
     "s": "PEGADINHA: não é preciso um incêndio \"demorado\" para esses fenômenos ocorrerem — eles "
          "surgem com pouco tempo de queima, desde que o ambiente seja confinado/compartimentado."},
    {"t": "art", "n": "Flashover (Generalização do Incêndio)",
     "x": "É a passagem SÚBITA do incêndio da fase de crescimento para a fase de desenvolvimento "
          "completo. Caracteriza-se pela ignição quase simultânea de todos os combustíveis em um "
          "compartimento — incluindo a fase GASOSA dos combustíveis (gases de pirólise acumulados) —, "
          "fazendo com que todo o volume do cômodo pegue fogo de uma vez.",
     "s": "Flashover não é \"mais um pedaço do móvel pegando fogo\": é todo o AMBIENTE (inclusive os "
          "gases no ar) entrando em ignição praticamente ao mesmo tempo."},
    {"t": "art", "n": "Rollover (chamas rolando)",
     "x": "Fenômeno que costuma preceder o flashover: com a fumaça se acumulando e se espalhando "
          "horizontalmente próxima ao teto (pré-generalização do incêndio), os gases quentes de "
          "pirólise ali concentrados entram em ignição intermitente, formando línguas de fogo que "
          "parecem \"rolar\" pelo teto do ambiente, pouco antes da generalização total (flashover).",
     "s": "Sequência típica até o flashover: desenvolvimento da camada de fumaça no teto → fumaça se "
          "espalhando horizontalmente (pré-generalização) → chamas rolando pelo teto (rollover) → "
          "generalização do incêndio (flashover). Ver o rollover é um sinal de alerta de flashover "
          "iminente."},
    {"t": "art", "n": "Backdraft (Explosão da Fumaça)",
     "x": "É a deflagração rápida e violenta da fumaça aquecida e combustível em ambiente CONFINADO "
          "com pouquíssima ventilação, induzida pelo acesso de oxigênio ao ambiente por alguma "
          "abertura. A entrada de ar pode se dar pela abertura de uma porta ou janela (por curiosos ou "
          "bombeiros) ou pela ruptura de algum acesso devido à degradação do material pelo calor "
          "(vidros podem quebrar-se pelas altas temperaturas). O backdraft NÃO ocorre imediatamente "
          "após a abertura: o intervalo entre a abertura e a explosão pode variar de vários segundos a "
          "alguns minutos.",
     "s": "Decore: o backdraft tem DELAY — não explode no instante exato em que a porta é aberta. E a "
          "entrada de ar não depende só de alguém abrir a porta: pode vir de um vidro que estoura "
          "sozinho pelo calor."},
    {"t": "art", "n": "Flashover x Backdraft — não confundir",
     "x": "Flashover: ocorre em ambiente que ainda tem alguma troca de ar (chamas já visíveis, "
          "pirólise, fumaça se acumulando e se espalhando), representando a generalização SÚBITA de "
          "um incêndio que já estava se desenvolvendo. Backdraft: ocorre em ambiente totalmente "
          "FECHADO/confinado, sem chamas visíveis (muitas vezes só fumaça saindo por frestas), e é "
          "DESENCADEADO pela entrada repentina de oxigênio que faltava — ou seja, o oxigênio é a peça "
          "que estava ausente e completa o tetraedro do fogo.",
     "s": "Pergunta clássica de prova: \"ao abrir a porta de um cômodo esfumaçado sem chamas visíveis, "
          "o fenômeno que pode ocorrer é...\" → BACKDRAFT (faltava oxigênio). Já \"o incêndio que já "
          "estava com chamas generalizou repentinamente\" → FLASHOVER (ambiente já tinha alguma "
          "ventilação/combustão ativa)."},
]

m = re.search(r'const TEORIA_COMBATE_INCENDIO\s*=\s*\[', html)
assert m, "TEORIA_COMBATE_INCENDIO nao encontrada"
array_start = m.end() - 1
decoder = json.JSONDecoder()
_arr, array_end = decoder.raw_decode(html, array_start)
close_bracket_idx = array_end - 1
assert html[close_bracket_idx] == ']'

insertion = ''.join(',\n' + json.dumps(item, ensure_ascii=False) for item in NEW_TEORIA_ITEMS)
new_html = html[:close_bracket_idx] + insertion + '\n' + html[close_bracket_idx:]

with open('app-template.html', 'w', encoding='utf-8', newline='') as f:
    f.write(new_html)
print('TEORIA_COMBATE_INCENDIO: +', len(NEW_TEORIA_ITEMS), 'itens')

# ---------------- 10 questoes de multipla escolha (BM, nivel avancado) ----------------
DISC = "Noções de Combate a Incêndio"

NEW_QUESTIONS = [
    {"enun": "Uma guarnição de bombeiros chega a uma residência em chamas e observa, ao se aproximar "
             "de um cômodo, fumaça saindo por frestas da porta, sem qualquer chama visível e sem ruído "
             "de combustão ativa. Diante desse cenário, o fenômeno extremo do fogo cujo risco deve ser "
             "imediatamente considerado antes de abrir a porta é:",
     "alts": ["o flashover, pois o ambiente já apresenta sinais de generalização do incêndio.",
              "o backdraft, pois o ambiente confinado com fumaça aquecida e sem chamas visíveis sugere "
              "falta de oxigênio, que pode ser subitamente suprida ao se abrir a porta.",
              "o rollover, que só ocorre em ambientes totalmente abertos e ventilados.",
              "nenhum fenômeno extremo, pois a ausência de chamas visíveis indica incêndio já "
              "controlado.",
              "a combustão completa, por não haver mais liberação de fumaça."],
     "resp": 1,
     "exp": "Correto. Ambiente confinado, fumaça aquecida sem chamas visíveis e pouca ventilação são "
            "exatamente as condições clássicas que antecedem um backdraft — a entrada de ar ao abrir a "
            "porta pode fornecer o oxigênio que faltava para a explosão da fumaça."},

    {"enun": "Em relação ao fenômeno do backdraft, é correto afirmar que:",
     "alts": ["ocorre imediatamente, no exato instante em que uma porta ou janela é aberta.",
              "o intervalo entre a abertura de uma via de acesso e a efetiva explosão da fumaça pode "
              "variar de vários segundos a alguns minutos, não sendo instantâneo.",
              "só pode ser desencadeado pela ação deliberada de bombeiros, nunca por rupturas "
              "acidentais.",
              "depende exclusivamente da presença de líquidos inflamáveis no ambiente.",
              "é sinônimo de flashover, sendo apenas outro nome para o mesmo fenômeno."],
     "resp": 1,
     "exp": "Correto. O backdraft não é instantâneo: pode haver um intervalo de segundos a minutos "
            "entre a entrada de ar (por abertura de porta/janela ou ruptura de vidro pelo calor) e a "
            "efetiva deflagração da fumaça."},

    {"enun": "Durante a fase de crescimento de um incêndio estrutural, é correto afirmar que a "
             "elevação de temperatura:",
     "alts": ["é lenta e gradual, levando horas para ultrapassar 200°C.",
              "pode atingir valores próximos a 600°C em menos de 3 minutos, à medida que os "
              "combustíveis sofrem pirólise simultânea por feedback radiativo da fumaça, do teto e "
              "das paredes.",
              "permanece estável, só se elevando de fato na fase de decaimento.",
              "depende exclusivamente da classe de incêndio envolvida, sendo irrelevante a "
              "disponibilidade de comburente.",
              "só ocorre se houver intervenção humana aumentando a ventilação do ambiente."],
     "resp": 1,
     "exp": "Correto. A fase de crescimento é marcada por elevação de temperatura muito acelerada, "
            "podendo chegar a cerca de 600°C em menos de 3 minutos, com todos os combustíveis do "
            "cômodo entrando em pirólise simultânea pelo feedback radiativo."},

    {"enun": "Sobre a fase de desenvolvimento completo de um incêndio estrutural, assinale a "
             "alternativa correta.",
     "alts": ["O comburente disponível permanece constante, apenas o combustível se esgota "
              "progressivamente.",
              "A temperatura pode ultrapassar 1000°C, e tanto o comburente quanto a disponibilidade de "
              "combustível começam a diminuir simultaneamente, já que as chamas consomem o material "
              "disponível.",
              "É a fase em que a temperatura está em seu ponto mais baixo desde o início do incêndio.",
              "Caracteriza-se pela ausência total de chamas visíveis, predominando apenas fumaça "
              "densa.",
              "Ocorre antes da fase de crescimento, sendo a primeira etapa do desenvolvimento do "
              "incêndio."],
     "resp": 1,
     "exp": "Correto. Na fase de desenvolvimento completo, o incêndio atinge seu ápice (temperatura "
            "podendo superar 1000°C), com queda simultânea tanto do comburente disponível quanto do "
            "combustível ainda não consumido."},

    {"enun": "Uma guarnição realiza o rescaldo de um incêndio estrutural já em fase de decaimento, com "
             "temperatura em queda e sem chamas visíveis. Do ponto de vista da segurança respiratória, "
             "é correto afirmar que:",
     "alts": ["o uso de equipamento autônomo de proteção respiratória (EPR) torna-se dispensável, já "
              "que as chamas diminuíram.",
              "mesmo sem chamas visíveis, a fase de decaimento ainda apresenta forte presença de "
              "combustão incompleta e alta taxa de liberação de monóxido de carbono, exigindo o uso "
              "contínuo de EPR.",
              "o monóxido de carbono só representa risco se houver reignição das chamas.",
              "a ausência de chamas elimina totalmente o tetraedro do fogo, tornando o ambiente seguro "
              "para respiração sem proteção.",
              "o risco de intoxicação na fase de decaimento é menor do que na fase inicial do "
              "incêndio."],
     "resp": 1,
     "exp": "Correto. A fase de decaimento mantém forte presença de combustão incompleta e alta "
            "liberação de CO — mesmo sem chamas visíveis, o ar permanece perigoso para quem o respirar "
            "sem EPR."},

    {"enun": "Considerando a sequência de eventos que costuma preceder a generalização de um incêndio "
             "(flashover) em ambiente confinado, assinale a ordem correta.",
     "alts": ["Generalização do incêndio → desenvolvimento da camada de fumaça no teto → rollover → "
              "fumaça se espalhando horizontalmente.",
              "Desenvolvimento da camada de fumaça no teto → fumaça se espalhando horizontalmente "
              "(pré-generalização) → chamas rolando pelo teto (rollover) → generalização do incêndio "
              "(flashover).",
              "Rollover → flashover → desenvolvimento da camada de fumaça no teto → backdraft.",
              "Backdraft → rollover → flashover, sempre nessa ordem fixa, em qualquer incêndio "
              "confinado.",
              "Não existe sequência típica; os fenômenos ocorrem de forma totalmente aleatória."],
     "resp": 1,
     "exp": "Correto. A sequência típica é: acúmulo de fumaça no teto → espalhamento horizontal da "
            "fumaça (pré-generalização) → rollover (chamas rolando pelo teto, sinal de alerta) → "
            "flashover (generalização total do incêndio)."},

    {"enun": "No que se refere à caracterização técnica do flashover, é correto afirmar que:",
     "alts": ["ocorre pela ignição exclusiva dos materiais sólidos do compartimento, sem envolver a "
              "fase gasosa dos combustíveis.",
              "caracteriza-se pela ignição quase simultânea de todos os combustíveis do compartimento, "
              "incluindo a fase gasosa resultante da pirólise, fazendo todo o volume do cômodo pegar "
              "fogo de uma vez.",
              "é um fenômeno gradual, que se desenvolve ao longo de várias horas.",
              "ocorre apenas em ambientes completamente vedados, sem qualquer troca de ar com o "
              "exterior.",
              "é sinônimo de combustão lenta, por envolver apenas incandescência."],
     "resp": 1,
     "exp": "Correto. O flashover envolve a ignição quase simultânea de TODOS os combustíveis do "
            "compartimento, incluindo a fase gasosa (gases de pirólise acumulados), e é um fenômeno "
            "súbito, não gradual."},

    {"enun": "Os fenômenos extremos do fogo (flashover, backdraft e demais fenômenos de ignição da "
             "fumaça), classificados como \"incêndios de propagação rápida\", apresentam como "
             "característica comum, EXCETO:",
     "alts": ["ocorrência em espaço físico limitado, confinado ou compartimentado.",
              "associação com a ignição da fumaça, que é combustível quando em mistura adequada com o "
              "oxigênio e energia suficiente.",
              "necessidade de longos períodos de queima, não ocorrendo em incêndios recentes.",
              "ocorrência repentina, justificando a denominação rapid fire progress.",
              "dificuldade de escoamento da fumaça para o exterior, sobretudo com portas e janelas "
              "fechadas."],
     "resp": 2,
     "exp": "A exceção é a alternativa que exige longos períodos de queima: esses fenômenos surgem com "
            "POUCO tempo de queima, não sendo necessários longos períodos para que um incêndio de "
            "propagação rápida ocorra."},

    {"enun": "Quanto às formas de entrada de oxigênio que podem desencadear um backdraft, é correto "
             "afirmar que:",
     "alts": ["só pode ocorrer pela abertura deliberada de uma porta ou janela por bombeiros ou "
              "curiosos.",
              "pode ocorrer tanto pela abertura de uma porta ou janela quanto pela ruptura acidental de "
              "algum acesso, como vidros que se quebram pelas altas temperaturas do ambiente.",
              "nunca ocorre por ruptura acidental de vidros, apenas por ação humana deliberada.",
              "depende exclusivamente da atuação do sistema de ventilação mecânica do prédio.",
              "é impossível em edificações com janelas de vidro temperado."],
     "resp": 1,
     "exp": "Correto. Além da abertura deliberada de portas/janelas, o backdraft também pode ser "
            "desencadeado pela ruptura acidental de acessos, como vidros que se quebram pela "
            "degradação térmica causada pelo calor do incêndio."},

    {"enun": "Em um incêndio estrutural que já apresenta chamas visíveis generalizando-se rapidamente "
             "por todo um compartimento, incluindo a ignição simultânea dos gases de pirólise "
             "acumulados — sem que tenha havido qualquer abertura súbita de porta ou janela momentos "
             "antes —, o fenômeno mais compatível com essa descrição é:",
     "alts": ["o backdraft, por envolver ignição de gases acumulados.",
              "o flashover, pois representa a passagem súbita da fase de crescimento para a de "
              "desenvolvimento completo, sem depender de uma entrada repentina de oxigênio por "
              "abertura externa.",
              "a combustão completa, por envolver todos os combustíveis do ambiente.",
              "o ponto de fulgor, por envolver ignição de vapores.",
              "a queima total, por consumir todo o material do compartimento instantaneamente."],
     "resp": 1,
     "exp": "Correto. A ausência de uma abertura externa recente que tenha introduzido oxigênio afasta "
            "o backdraft (que depende dessa entrada repentina de ar); o quadro descrito — generalização "
            "súbita das chamas já existentes, com ignição da fase gasosa — é a definição clássica de "
            "flashover."},
]

assert len(NEW_QUESTIONS) == 10

next_id = 975
built = []
for item in NEW_QUESTIONS:
    built.append({
        "id": next_id, "corp": "BM", "disc": DISC, "assunto": DISC, "tipo": "MC",
        "enun": item["enun"], "alts": item["alts"], "resp": item["resp"],
        "exp": item["exp"] + " (Baseado no PDF Focado \"Fases do Incêndio\" — Focus Concursos — "
               "complementado com conhecimento consolidado de ciência do fogo.)",
    })
    next_id += 1

body = raw[:-1]
for q in built:
    body += '\r\n, ' + json.dumps(q, ensure_ascii=False)
body += ']'

with open('questions.json', 'w', encoding='utf-8', newline='') as f:
    f.write(body)

with open('questions.json', encoding='utf-8') as f:
    check = json.load(f)
assert len(check) == len(data_check) + len(built)
print('OK -- total de questoes agora:', len(check))

with open('questions.json', encoding='utf-8') as f:
    qdata = f.read()
with open('app-template.html', encoding='utf-8') as f:
    html2 = f.read()
html2 = html2.replace('__QUESTIONS_JSON__', qdata)
with open('estudo-cebraspe-ma.html', 'w', encoding='utf-8') as f:
    f.write(html2)
print('estudo-cebraspe-ma.html regenerado com sucesso')
