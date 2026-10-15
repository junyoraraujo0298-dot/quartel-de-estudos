# -*- coding: utf-8 -*-
# Acrescenta a TEORIA_COMBATE_INCENDIO o conteudo de "Processos de
# Combustao" (classificacao por velocidade e por liberacao de produtos,
# fumaca/QOMIT, pontos notaveis de temperatura), baseado no PDF Focado
# da Focus Concursos fornecido pelo usuario, e adiciona 10 questoes de
# multipla escolha de nivel avancado (combinam o conteudo do PDF com
# conhecimento consolidado de ciencia do fogo -- ex.: backdraft,
# toxicidade comparada do CO -- nao apenas repeticao literal do texto).
import json
import re

with open('questions.json', encoding='utf-8') as f:
    raw = f.read()

data_check = json.loads(raw)
max_id = max(q['id'] for q in data_check)
assert max_id == 964, max_id

with open('app-template.html', encoding='utf-8') as f:
    html = f.read()

NEW_TEORIA_ITEMS = [
    {"t": "cap", "x": "Processos de Combustão"},
    {"t": "art", "n": "Classificação quanto à velocidade de reação",
     "x": "Combustão VIVA: fogo caracterizado pela presença de chama; pelo impacto visual e "
          "psicológico que gera, é considerada o tipo mais importante de combustão e costuma "
          "concentrar quase todas as atenções durante o combate. Combustão LENTA (incandescência): "
          "processo relativamente lento entre o oxigênio e um sólido combustível, formando a brasa; "
          "pode ser o início OU o fim de uma combustão viva, com produção de luz, calor e fumaça; "
          "geralmente presente na fase final dos incêndios.",
     "s": "Pegadinha: a incandescência não é só \"o que sobra\" no fim do incêndio — ela também pode "
          "ser o PONTO DE PARTIDA de uma combustão viva (ex.: uma brasa mal apagada que reacende em "
          "chama horas depois)."},
    {"t": "art", "n": "Classificação quanto à liberação de produtos",
     "x": "Combustão INCOMPLETA: ocorre quando não há oxigênio suficiente para queimar todo o "
          "combustível; é a condição típica de incêndios estruturais (ambiente fechado por teto e "
          "paredes), onde o oxigênio disponível tende a decrescer, fazendo as chamas diminuírem ou "
          "até se apagarem — mas a camada gasosa da fumaça permanece aquecida e carregada de material "
          "capaz de reagir com o oxigênio, necessitando apenas de ar para \"fechar\" o tetraedro do "
          "fogo e reiniciar a combustão. Combustão COMPLETA: produz calor e chamas em ambiente rico "
          "em oxigênio.",
     "s": "Combustão incompleta é a REGRA em incêndio estrutural (ambiente fechado, pouco O₂) — não a "
          "exceção. É justamente essa fumaça \"faminta\" por oxigênio que explica fenômenos perigosos "
          "como o backdraft, quando a entrada repentina de ar (ex.: ao abrir uma porta) reacende toda "
          "a massa gasosa de uma vez."},
    {"t": "art", "n": "Combustão completa ≠ queima total",
     "x": "Combustão completa é a combinação perfeita entre combustível e oxigênio, fazendo todo o "
          "combustível reagir — ocorre apenas em situações especiais ou em laboratório, não sendo "
          "encontrada na prática de combate a incêndio. Queima total é a situação em que todo o "
          "material combustível presente no ambiente já foi atingido pela combustão. Como não se "
          "atinge um índice de 100% de queima facilmente, 99% de queima já significa combustão "
          "INCOMPLETA, pois ainda ficou combustível sem queimar.",
     "s": "Não confunda: \"queimou tudo que tinha para queimar\" (queima total) é diferente de "
          "\"queimou perfeitamente, sem sobra de combustível não reagido\" (combustão completa) — a "
          "prova adora trocar um conceito pelo outro."},
    {"t": "cap", "x": "Produtos da Combustão — a Fumaça (mnemônico QOMIT)"},
    {"t": "art", "n": "As 5 características da fumaça",
     "x": "QUENTE: produto da combustão, possui alta energia térmica. OPACA: seus produtos, "
          "principalmente a fuligem, permanecem suspensos na massa gasosa, dificultando a "
          "visibilidade tanto para bombeiros quanto para vítimas. MÓVEL: fluido em convecção "
          "constante, que se movimenta por fossos, dutos e aberturas, podendo levar produtos da "
          "combustão e energia térmica para outros ambientes e propagar o incêndio para novos "
          "compartimentos. INFLAMÁVEL: em incêndios estruturais prevalece a combustão incompleta, "
          "que deixa na fumaça produtos instáveis ainda capazes de reagir com o oxigênio — a própria "
          "fumaça é combustível, podendo queimar ou até explodir. TÓXICA: contém monóxido de carbono "
          "(CO), dióxido de carbono (CO₂), ácido cianídrico (HCN) entre outros, com propriedades "
          "asfixiantes e irritantes, podendo matar bombeiros e vítimas em poucos minutos.",
     "s": "Decore o mnemônico QOMIT (Quente, Opaca, Móvel, Inflamável, Tóxica). A característica mais "
          "cobrada e menos intuitiva é a INFLAMÁVEL — muita gente lembra só da toxicidade da fumaça e "
          "esquece que ela também pode pegar fogo ou explodir."},
    {"t": "cap", "x": "Pontos Notáveis de Temperatura"},
    {"t": "art", "n": "Ponto de fulgor",
     "x": "Temperatura mínima na qual o material libera vapores em quantidade suficiente para se "
          "incendiarem na presença de uma fonte externa de calor, mas a queima NÃO SE MANTÉM se essa "
          "fonte for retirada — os vapores liberados, em pequena quantidade, são capazes apenas de "
          "alimentar uma combustão já existente, não de sustentá-la sozinhos.",
     "s": "Fulgor = \"lampeja e apaga\". Precisa da fonte externa o tempo todo; sem ela, a chama "
          "morre."},
    {"t": "art", "n": "Ponto de combustão",
     "x": "Prosseguindo no aquecimento, temperatura na qual a liberação de vapores do material é tal "
          "que, ao entrarem em contato com uma fonte externa de calor, iniciam a combustão e "
          "CONTINUAM queimando mesmo com a retirada dessa fonte. É o ponto em que se atinge a reação "
          "em cadeia: o calor da queima dos vapores já liberados é suficiente para causar a liberação "
          "de mais vapor, em quantidade capaz de sustentar a combustão.",
     "s": "Combustão = \"pega e sustenta sozinho\", diferente do fulgor (que apaga assim que a fonte "
          "externa é retirada)."},
    {"t": "art", "n": "Ponto de ignição",
     "x": "Continuando o aquecimento, temperatura na qual os vapores liberados pelo combustível estão "
          "em quantidade tal que, expostos ao ar, entram em combustão SEM que haja fonte externa de "
          "calor — a energia que os vapores apresentam já é suficiente por si só.",
     "s": "Ordem crescente de temperatura e de \"independência\" da fonte externa: fulgor (precisa da "
          "fonte sempre) → combustão (precisa só para começar) → ignição (não precisa nem para "
          "começar)."},
]

m = re.search(r'const TEORIA_COMBATE_INCENDIO\s*=\s*\[', html)
assert m, "TEORIA_COMBATE_INCENDIO nao encontrada"
array_start = m.end() - 1
decoder = json.JSONDecoder()
_arr, array_end = decoder.raw_decode(html, array_start)
# array_end é o indice logo apos o "]" de fechamento
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
    {"enun": "Durante o rescaldo de um incêndio estrutural já aparentemente extinto, o comandante da "
             "guarnição observa apenas brasas incandescentes, sem chamas visíveis. Do ponto de vista "
             "técnico da classificação da combustão quanto à velocidade de reação, é correto afirmar "
             "que essa incandescência:",
     "alts": ["representa necessariamente o fim do processo de combustão, não podendo dar origem a "
              "uma nova combustão viva.",
              "pode constituir tanto o fim quanto o início de uma nova combustão viva, razão pela "
              "qual o rescaldo deve ser rigoroso mesmo sem chamas aparentes.",
              "não produz luz, calor ou fumaça, por se tratar de combustão lenta.",
              "só ocorre em líquidos inflamáveis, nunca em sólidos combustíveis.",
              "indica obrigatoriamente que a combustão atingida foi do tipo completa."],
     "resp": 1,
     "exp": "Correto. A incandescência (combustão lenta) pode ser tanto o fim quanto o início de uma "
            "combustão viva — por isso brasas aparentemente inofensivas no rescaldo podem reacender em "
            "chamas, com produção de luz, calor e fumaça."},

    {"enun": "Em um incêndio estrutural de longa duração, a guarnição observa que o ambiente está "
             "tomado por fumaça densa e quente, mas sem chamas visíveis, pouco antes da abertura de "
             "uma porta. Combinando os conceitos de combustão incompleta e de tetraedro do fogo, o "
             "principal risco técnico dessa situação, ao se abrir repentinamente a porta, é:",
     "alts": ["a extinção espontânea do incêndio pela entrada de ar frio.",
              "a ocorrência de backdraft: a entrada súbita de oxigênio \"fecha\" o tetraedro do fogo "
              "numa massa gasosa aquecida e rica em produtos de combustão incompleta, podendo causar "
              "explosão/reignição generalizada.",
              "a transformação automática da combustão incompleta em combustão completa, sem "
              "qualquer risco adicional.",
              "a imediata queda da temperatura ambiente a níveis seguros para entrada sem EPR.",
              "a impossibilidade de reinício da combustão, já que a fumaça não é inflamável."],
     "resp": 1,
     "exp": "Correto. Isso é justamente o fenômeno do backdraft: a fumaça de uma combustão incompleta "
            "está carregada de produtos ainda capazes de reagir com o oxigênio (fumaça é inflamável); "
            "ao reintroduzir ar de forma súbita, \"fecha-se\" o tetraedro do fogo (faltava apenas "
            "comburente) e a massa gasosa pode entrar em combustão de forma explosiva."},

    {"enun": "Em um incêndio estrutural, constatou-se que 99% do material combustível presente no "
             "ambiente foi efetivamente atingido e consumido pelo fogo. Nesse cenário, é correto "
             "afirmar que:",
     "alts": ["ocorreu combustão completa, visto que praticamente todo o combustível reagiu.",
              "ocorreu queima total, mas não necessariamente combustão completa, pois ainda restou 1% "
              "de combustível sem queimar, o que já caracteriza combustão incompleta.",
              "ocorreu simultaneamente combustão completa e queima total, por serem conceitos "
              "equivalentes.",
              "a combustão completa é diretamente proporcional à porcentagem de material consumido.",
              "não é possível classificar a combustão sem conhecer a classe do incêndio envolvido."],
     "resp": 1,
     "exp": "Correto. Combustão completa e queima total não são sinônimos. Queima total é atingir todo "
            "o material combustível disponível; combustão completa exige reação perfeita entre "
            "combustível e oxigênio, sem sobra de combustível não reagido. Como restou 1% sem "
            "queimar, trata-se de combustão INCOMPLETA, ainda que a queima tenha sido quase total."},

    {"enun": "Comparando-se, do ponto de vista químico, os produtos típicos da combustão completa e "
             "da combustão incompleta de um material orgânico, é correto afirmar que:",
     "alts": ["ambas produzem exclusivamente dióxido de carbono (CO₂) e água, sem diferença relevante "
              "de toxicidade.",
              "a combustão completa tende a gerar predominantemente CO₂ e água, ao passo que a "
              "combustão incompleta gera quantidades relevantes de monóxido de carbono (CO), gás "
              "muito mais tóxico por se ligar à hemoglobina e prejudicar o transporte de oxigênio no "
              "sangue.",
              "a combustão incompleta nunca produz monóxido de carbono, apenas fuligem.",
              "a combustão completa é mais perigosa para a saúde humana do que a incompleta.",
              "o monóxido de carbono só é produzido em incêndios de classe D."],
     "resp": 1,
     "exp": "Correto. A combustão incompleta (falta de O₂ suficiente) favorece a formação de CO, que "
            "compete com o oxigênio pela hemoglobina (afinidade muito maior), explicando por que o CO "
            "é historicamente uma das principais causas de morte em incêndios — muito mais do que as "
            "queimaduras em si."},

    {"enun": "A respeito da característica MÓVEL da fumaça, é correto afirmar que:",
     "alts": ["a fumaça permanece estática no ambiente de origem do incêndio, não se deslocando para "
              "outros compartimentos.",
              "o deslocamento da fumaça por convecção pode levar produtos da combustão e energia "
              "térmica, por fossos, dutos e aberturas, a ambientes distantes do foco original, "
              "propagando o incêndio para novos compartimentos.",
              "a movimentação da fumaça depende exclusivamente da ação mecânica de ventiladores "
              "instalados no ambiente.",
              "a fumaça só se movimenta horizontalmente, nunca por dutos verticais.",
              "a característica MÓVEL está relacionada apenas à toxicidade da fumaça, não à sua "
              "capacidade de propagação de incêndio."],
     "resp": 1,
     "exp": "Correto. A convecção constante da fumaça é um fluido em movimento que pode ocupar "
            "qualquer espaço disponível (fossos, dutos, aberturas), levando produtos de combustão e "
            "calor para novos compartimentos e propagando o incêndio para além do ambiente de origem."},

    {"enun": "Considerando os três pontos notáveis de temperatura relacionados à liberação de vapores "
             "de um material combustível, assinale a alternativa que ordena corretamente, da menor "
             "para a maior temperatura, e descreve com precisão a diferença entre eles.",
     "alts": ["Ponto de ignição (não sustenta a chama sem fonte externa) < ponto de fulgor (sustenta "
              "parcialmente) < ponto de combustão (não precisa de fonte externa em nenhum momento).",
              "Ponto de fulgor (chama não se mantém sem fonte externa) < ponto de combustão (chama se "
              "mantém mesmo sem a fonte externa, uma vez iniciada) < ponto de ignição (entra em "
              "combustão sem qualquer fonte externa de calor).",
              "Ponto de combustão < ponto de ignição < ponto de fulgor, sendo os três conceitos "
              "equivalentes entre si.",
              "Não há relação de ordem de temperatura entre os três pontos, pois dependem apenas do "
              "tipo de agente extintor utilizado.",
              "Ponto de fulgor e ponto de ignição são sinônimos, diferindo apenas do ponto de "
              "combustão."],
     "resp": 1,
     "exp": "Correto. Em ordem crescente de temperatura e de \"independência\" da fonte externa: "
            "fulgor (precisa da fonte externa o tempo todo, a chama não se mantém sem ela) → "
            "combustão (precisa da fonte só para iniciar, depois se sustenta sozinho pela reação em "
            "cadeia) → ignição (nem precisa de fonte externa para começar)."},

    {"enun": "Em relação à afirmação de que a combustão viva \"costuma receber quase todas as "
             "atenções durante o combate a incêndio\", é correto concluir que:",
     "alts": ["a combustão lenta (incandescência) pode ser negligenciada com segurança durante o "
              "rescaldo, por ser menos visível.",
              "embora a combustão viva concentre a atenção visual e operacional por seu impacto, a "
              "combustão lenta não deve ser negligenciada, pois pode reacender uma combustão viva, "
              "exigindo rescaldo cuidadoso.",
              "apenas incêndios de combustão viva são classificados tecnicamente como incêndios.",
              "a combustão lenta não produz calor suficiente para reacender qualquer material.",
              "o risco de reignição só existe em incêndios de classe B."],
     "resp": 1,
     "exp": "Correto. O fato de a combustão viva concentrar as atenções não torna a combustão lenta "
            "irrelevante — justamente por poder ser o início de uma nova combustão viva, a "
            "incandescência exige rescaldo cuidadoso para evitar reignição."},

    {"enun": "Em um incêndio estrutural ainda em fase de combustão incompleta, friamente contido em "
             "ambiente fechado, assinale a alternativa que relaciona corretamente DUAS características "
             "da fumaça (mnemônico QOMIT) ao risco operacional que cada uma representa.",
     "alts": ["OPACA reduz a visibilidade de bombeiros e vítimas; INFLAMÁVEL significa que a própria "
              "fumaça, carregada de produtos de combustão incompleta, pode queimar ou explodir ao "
              "receber oxigênio.",
              "QUENTE está relacionada exclusivamente ao risco de explosão; TÓXICA está relacionada "
              "exclusivamente à perda de visibilidade.",
              "MÓVEL significa que a fumaça nunca ultrapassa os limites do cômodo de origem; OPACA "
              "está relacionada à produção de monóxido de carbono.",
              "TÓXICA refere-se apenas ao risco de queimaduras térmicas, não a efeitos respiratórios.",
              "INFLAMÁVEL e TÓXICA são, na prática, a mesma característica, apenas com nomes "
              "diferentes."],
     "resp": 0,
     "exp": "Correto. OPACA (fuligem suspensa dificultando a visão) e INFLAMÁVEL (fumaça de combustão "
            "incompleta ainda capaz de reagir com o oxigênio, podendo queimar ou explodir) são "
            "características distintas, cada uma com seu próprio risco operacional — não devem ser "
            "confundidas com QUENTE (energia térmica) ou TÓXICA (asfixia/intoxicação)."},

    {"enun": "Um material é aquecido progressivamente. Ao atingir determinada temperatura, libera "
             "vapores que se incendeiam na presença de uma chama-piloto externa, mas a chama se apaga "
             "assim que essa chama-piloto é retirada. Esse comportamento caracteriza, com precisão "
             "técnica, o:",
     "alts": ["ponto de combustão, pois já há liberação relevante de vapores.",
              "ponto de fulgor, pois a combustão não se sustenta sem a fonte externa de calor.",
              "ponto de ignição, pois houve incêndio dos vapores liberados.",
              "ponto de fulgor e o ponto de combustão, simultaneamente, por serem a mesma coisa.",
              "tetraedro do fogo, por envolver os quatro elementos da combustão."],
     "alts_fix": None,
     "resp": 1,
     "exp": "Correto. A marca registrada do PONTO DE FULGOR é exatamente essa: os vapores liberados "
            "incendeiam-se com uma fonte externa, mas a chama NÃO SE MANTÉM quando essa fonte é "
            "retirada, por serem liberados em quantidade ainda insuficiente para sustentar sozinhos a "
            "combustão."},

    {"enun": "Assinale a alternativa correta acerca da relação entre a combustão incompleta e o risco "
             "de intoxicação de vítimas e bombeiros em incêndios estruturais.",
     "alts": ["A combustão incompleta é rara em incêndios estruturais, predominando a combustão "
              "completa, de modo que o risco de intoxicação é residual.",
              "A combustão incompleta, predominante em ambientes fechados com oxigênio limitado, "
              "favorece a produção de monóxido de carbono e outros gases asfixiantes/irritantes (como "
              "HCN), sendo uma das principais causas de óbito em incêndios, por vezes mais relevante "
              "do que as queimaduras.",
              "O risco de intoxicação em incêndios estruturais está associado exclusivamente à "
              "inalação de dióxido de carbono em baixíssimas concentrações.",
              "A combustão completa produz mais monóxido de carbono do que a incompleta, por reagir "
              "com maior quantidade de oxigênio.",
              "Vítimas de incêndio só correm risco de intoxicação se estiverem em contato direto com "
              "as chamas."],
     "resp": 1,
     "exp": "Correto. Em ambientes fechados (típicos de incêndios estruturais), o oxigênio limitado "
            "favorece a combustão incompleta, gerando CO, HCN e outros gases tóxicos — a intoxicação "
            "por esses gases é reconhecidamente uma das principais causas de morte em incêndios, "
            "muitas vezes mais determinante do que as queimaduras térmicas."},
]

assert len(NEW_QUESTIONS) == 10

next_id = 965
built = []
for item in NEW_QUESTIONS:
    built.append({
        "id": next_id, "corp": "BM", "disc": DISC, "assunto": DISC, "tipo": "MC",
        "enun": item["enun"], "alts": item["alts"], "resp": item["resp"],
        "exp": item["exp"] + " (Baseado no PDF Focado \"Processos de Combustão\" — Focus Concursos — "
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
