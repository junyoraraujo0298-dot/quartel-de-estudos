# -*- coding: utf-8 -*-
"""
Primeiro conteudo de Direito Processual Penal do app (PC-PE) -- a partir
do PDF "Disposicoes Preliminares" (Focus Concursos, prof. Priscilla
Fernandes), que cobre o item 1 do edital (Aplicacao da lei processual no
tempo, no espaco e em relacao as pessoas) -- disciplina ate entao SEM
NENHUMA cobertura no app (era so mencionada na carga horaria do
cronograma).

A mudanca estrutural em app-template.html ja foi feita via Edit antes
deste script rodar: foi criado o novo deck TEORIA_DIREITO_PROCESSUAL_
PENAL_PCPE (20 itens, cobrindo conceito/finalidade/persecucao penal/
fontes, os 3 sistemas processuais -- com destaque pro art. 3-A do CPP,
sistema acusatorio pos-Pacote Anticrime, que o PDF nao trazia -- e os
arts. 1 a 3 do CPP, inciso a inciso, incluindo a pegadinha da remissao
desatualizada do art. 1, II a artigos de constituicao anterior a 1988),
e registrado em TEORIA_DECKS / TEORIA_DECK_TO_DISC.

O PDF trazia 7 questoes (Certo/Errado e multipla escolha), com bastante
repeticao da mesma ideia central (regra geral x excecoes do art. 1).
Essa repeticao foi consolidada em 10 questoes originais de multipla
escolha, usando a capacidade liberada pra cobrir tambem os sistemas
processuais (inquisitivo/acusatorio/misto), a pegadinha da remissao
constitucional desatualizada no inciso II, e o contraste entre a
analogia no processo penal (ampla, inclusive in malam partem) e no
direito penal material (so in bonam partem).

Este script cuida so de: (1) acrescentar as questoes a questions.json,
(2) regenerar estudo-cebraspe-ma.html a partir do app-template.html ja
editado.
"""
import json

ASSUNTO = "1 — Direito Processual Penal: Aplicação da Lei Processual no Tempo, no Espaço e em Relação às Pessoas (Disposições Preliminares, arts. 1º a 3º, CPP)"

MC_QUESTIONS = [
    (
        "Acerca do conceito e da finalidade do Direito Processual Penal, assinale a alternativa correta:",
        [
            "É ramo do Direito Privado que disciplina exclusivamente a fase de inquérito policial.",
            "É ramo do Direito Público formado por princípios, normas e procedimentos que disciplinam a persecução penal, desde a investigação até a aplicação da pena, tendo finalidade imediata de aplicar a lei penal e finalidades mediatas de assegurar a paz social e a dignidade da pessoa humana.",
            "Sua finalidade mediata é a aplicação da lei penal, e a finalidade imediata é a paz social.",
            "Disciplina apenas a ação penal, não abrangendo o inquérito policial.",
            "É ramo do Direito Civil, por regular relações entre particulares no processo penal.",
        ],
        1,
        ASSUNTO,
        "Correto o item B. O Direito Processual Penal é ramo do Direito PÚBLICO que disciplina toda a persecução penal (investigação + processo + aplicação da pena), tendo finalidade IMEDIATA de aplicar a lei penal e finalidades MEDIATAS de assegurar a paz social e a dignidade da pessoa humana. O item C inverte as finalidades (a paz social é mediata, não imediata); os demais descrevem incorretamente a natureza (pública, não privada ou civil) e o alcance (abrange inquérito e ação penal) da disciplina.",
    ),
    (
        "Quanto à persecução penal e aos sistemas processuais penais, é correto afirmar que:",
        [
            "O sistema inquisitivo caracteriza-se pela separação das funções de acusar, defender e julgar.",
            "O sistema acusatório, expressamente adotado pelo art. 3º-A do CPP, veda a iniciativa do juiz na fase de investigação e a substituição da atuação probatória do órgão de acusação.",
            "O sistema misto é aquele em que existe apenas a fase processual em juízo, sem qualquer investigação preliminar.",
            "O inquérito policial é considerado, isoladamente, a fase de aplicação da pena dentro da persecução penal.",
            "O sistema acusatório permite que o juiz produza provas de ofício na fase de investigação, em nome da busca da verdade real.",
        ],
        1,
        ASSUNTO,
        "Correto o item B. O art. 3º-A do CPP (Lei nº 13.964/2019 — Pacote Anticrime) consagra o sistema acusatório, vedando expressamente a iniciativa do juiz na fase de investigação e a substituição da atuação probatória da acusação. O sistema inquisitivo, ao contrário do item A, CONCENTRA as funções de acusar/defender/julgar; o sistema misto combina fase inquisitiva (investigação) com fase acusatória (processo), não eliminando a investigação; o inquérito policial é a fase de INVESTIGAÇÃO, não de aplicação da pena.",
    ),
    (
        "Sobre as fontes do Direito Processual Penal, assinale a alternativa correta:",
        [
            "A lei é a única fonte admitida, sendo vedado o uso de costumes, analogia ou princípios gerais do direito para suprir lacunas.",
            "Compete exclusivamente aos Municípios legislar sobre direito processual penal.",
            "A lei é a fonte primária; costumes, princípios gerais do direito e analogia são fontes secundárias (mediatas, indiretas ou supletivas); há polêmica doutrinária quanto a doutrina e jurisprudência serem ou não fontes do direito.",
            "A jurisprudência é, de forma pacífica e sem controvérsia, considerada fonte formal do Direito Processual Penal por todas as bancas examinadoras.",
            "Compete privativamente aos Estados legislar sobre direito processual penal, cabendo à União apenas os procedimentos.",
        ],
        2,
        ASSUNTO,
        "Correto o item C. A LEI é a fonte primária (imediata) do Direito Processual Penal (art. 22, I, CF — competência privativa da União); costumes, princípios gerais do direito e analogia são fontes secundárias (mediatas/indiretas/supletivas); doutrina e jurisprudência geram polêmica quanto à sua natureza de fonte. A competência é da UNIÃO (não dos Municípios ou exclusivamente dos Estados), e as fontes secundárias SÃO admitidas para suprir lacunas.",
    ),
    (
        "Conforme o art. 1º do CPP, julgue a assertiva a seguir e assinale a alternativa correta: \"o processo penal brasileiro rege-se, em regra, pelo CPP em todo o território nacional, podendo essa aplicação ser afastada por tratado, convenção ou regra de direito internacional regularmente incorporada ao ordenamento jurídico brasileiro.\"",
        [
            "A assertiva está correta — é exatamente a regra geral do caput combinada com o inciso I do art. 1º do CPP.",
            "A assertiva está errada, pois tratados internacionais jamais podem afastar a aplicação do CPP.",
            "A assertiva está errada, pois o CPP não se aplica a todo o território nacional, apenas aos Estados que o ratificaram.",
            "A assertiva está correta, mas apenas quando o tratado for aprovado por maioria simples do Congresso Nacional.",
            "A assertiva está errada, pois apenas leis estaduais podem afastar a aplicação do CPP.",
        ],
        0,
        ASSUNTO,
        "Correto o item A. É a transcrição fiel da regra geral do art. 1º, caput, do CPP (aplicação em todo o território brasileiro) combinada com a primeira ressalva, o inciso I (tratados, convenções e regras de direito internacional regularmente incorporados).",
    ),
    (
        "Considere a seguinte situação hipotética: um cidadão brasileiro, acusado de tráfico de drogas cometido inteiramente em território brasileiro, alega que deveria ser julgado por um tribunal internacional, invocando genericamente \"tratados de cooperação internacional\". Com base no art. 1º, I, do CPP, assinale a alternativa correta:",
        [
            "Assiste razão ao acusado, pois qualquer tratado internacional sempre prevalece sobre o CPP, independentemente de seu objeto.",
            "Não assiste razão ao acusado, pois o CPP é absoluto e tratados internacionais jamais podem afastar sua aplicação.",
            "Assiste razão ao acusado, pois tratados de cooperação internacional têm natureza de emenda constitucional.",
            "Não assiste razão ao acusado, pois apenas tratados, convenções e regras de direito internacional regularmente incorporados ao ordenamento e efetivamente aplicáveis ao caso concreto afastam o CPP — a mera invocação genérica de \"cooperação internacional\", sem base em norma específica aplicável, não desloca a jurisdição nacional.",
            "Assiste razão ao acusado, pois crimes transnacionais são sempre julgados por tribunais internacionais, nunca pela Justiça brasileira.",
        ],
        3,
        ASSUNTO,
        "Correto o item D. A ressalva do inciso I exige um tratado/convenção/regra de direito internacional REGULARMENTE INCORPORADO e efetivamente aplicável ao caso concreto — a invocação genérica e sem base normativa específica não afasta a aplicação do CPP e da jurisdição penal brasileira comum.",
    ),
    (
        "Quanto ao inciso II do art. 1º do CPP (prerrogativas constitucionais), assinale a alternativa correta:",
        [
            "O Presidente da República, os Ministros de Estado (nos crimes conexos com os do Presidente) e os Ministros do STF (nos crimes de responsabilidade) têm processo e julgamento regidos por regras constitucionais próprias, afastando o CPP comum — ainda que a redação literal do CPP cite artigos de uma Constituição anterior à de 1988.",
            "Essa ressalva deixou de ter qualquer efeito prático, pois a CF/88 não prevê qualquer regra especial de foro para essas autoridades.",
            "A ressalva somente se aplica a crimes de responsabilidade do Presidente da República, não alcançando Ministros de Estado ou Ministros do STF.",
            "A numeração dos artigos constitucionais citada no inciso II do CPP corresponde, sem qualquer desatualização, aos artigos 86, 89 e 100 da Constituição Federal de 1988.",
            "Trata-se de ressalva aplicável apenas a Deputados Estaduais e Vereadores.",
        ],
        0,
        ASSUNTO,
        "Correto o item A. A ideia central da ressalva — foro por prerrogativa de função afastando o rito comum do CPP para Presidente, Ministros de Estado (crimes conexos) e Ministros do STF (crimes de responsabilidade) — permanece válida, embora a remissão literal do CPP a arts. 86, 89, §2º e 100 corresponda a uma Constituição anterior à CF/88, estando desatualizada quanto à numeração.",
    ),
    (
        "É correto afirmar, quanto ao inciso III do art. 1º do CPP, que:",
        [
            "Os processos de competência da Justiça Militar seguem o mesmo procedimento do CPP comum, sem regramento específico.",
            "Os processos de competência da Justiça Militar possuem regramento processual penal próprio, regido pelo Código de Processo Penal Militar.",
            "O CPP se aplica subsidiariamente aos processos da Justiça Militar, por força do parágrafo único do art. 1º.",
            "A Justiça Militar foi extinta pela Constituição de 1988, não havendo mais processos dessa natureza.",
            "O Código de Processo Penal Militar é aplicável apenas aos militares das Forças Armadas, nunca às polícias militares estaduais.",
        ],
        1,
        ASSUNTO,
        "Correto o item B. Os processos da competência da Justiça Militar têm regramento PRÓPRIO: o Código de Processo Penal Militar (Decreto-Lei nº 1.002/1969). O parágrafo único do art. 1º do CPP NÃO alcança o inciso III — a aplicação subsidiária do CPP é restrita aos incisos IV e V.",
    ),
    (
        "Sobre os incisos IV e V do art. 1º do CPP, assinale a alternativa correta:",
        [
            "O tribunal especial mencionado no inciso IV, previsto em Constituição anterior, permanece plenamente aplicável hoje, pois a CF/88 não veda juízos ou tribunais de exceção.",
            "A antiga Lei de Imprensa (Lei nº 5.250/1967) continua plenamente vigente e regula, até hoje, os crimes de imprensa no Brasil.",
            "O STF, no julgamento da ADPF nº 130, declarou a Lei de Imprensa integralmente não recepcionada pela CF/88, por ser incompatível com a liberdade de expressão e conter mecanismos de censura.",
            "A CF/88 permite expressamente a criação de tribunais de exceção, desde que instituídos por lei complementar.",
            "Após a ADPF nº 130, os crimes de imprensa passaram a ser julgados exclusivamente pelo STF, em instância única.",
        ],
        2,
        ASSUNTO,
        "Correto o item C. O STF, na ADPF nº 130 (2009), declarou a Lei de Imprensa (Lei nº 5.250/1967) integralmente não recepcionada pela CF/88. Já o tribunal especial do inciso IV não tem correspondência na CF/88, que VEDA juízo ou tribunal de exceção (art. 5º, XXXVII); e, após a revogação da Lei de Imprensa, os conflitos envolvendo liberdade de expressão/honra/privacidade seguem o Código Civil e a Constituição, não havendo instância única exclusiva do STF.",
    ),
    (
        "Quanto ao parágrafo único do art. 1º do CPP, assinale a alternativa correta:",
        [
            "O CPP aplica-se subsidiariamente a todos os cinco incisos do art. 1º, sem exceção.",
            "O CPP aplica-se subsidiariamente apenas aos processos referidos nos incisos IV e V, quando as leis especiais que os regulam não dispuserem de modo diverso.",
            "O CPP nunca se aplica, nem mesmo subsidiariamente, aos processos referidos nos incisos IV e V.",
            "A aplicação subsidiária do CPP, prevista no parágrafo único, abrange os incisos I, II e III, mas não os incisos IV e V.",
            "O parágrafo único trata da aplicação subsidiária do Código de Processo Civil, e não do CPP.",
        ],
        1,
        ASSUNTO,
        "Correto o item B. O parágrafo único do art. 1º do CPP restringe a aplicação subsidiária do próprio CPP aos processos dos incisos IV (tribunal especial) e V (crimes de imprensa) — não alcançando os incisos I, II e III.",
    ),
    (
        "Com relação à aplicação da lei processual penal no tempo e à sua interpretação (arts. 2º e 3º, CPP), assinale a alternativa correta:",
        [
            "A lei processual penal aplica-se desde logo (tempus regit actum), sem prejuízo da validade dos atos realizados sob a vigência da lei anterior; além disso, admite interpretação extensiva e aplicação analógica, inclusive em prejuízo do réu, já que não define crimes nem comina penas.",
            "A lei processual penal, assim como a lei penal material, jamais retroage, ainda que mais benéfica ao réu.",
            "É vedada, no âmbito processual penal, a interpretação analógica, admitindo-se apenas a interpretação extensiva.",
            "A analogia no Direito Processual Penal somente é admitida quando beneficiar o réu (in bonam partem), tal como ocorre no Direito Penal material.",
            "Os atos processuais já praticados sob a lei anterior são automaticamente invalidados quando sobrevém lei processual nova.",
        ],
        0,
        ASSUNTO,
        "Correto o item A. O art. 2º do CPP consagra a aplicação imediata da lei processual (tempus regit actum), preservando os atos já praticados; o art. 3º admite expressamente interpretação extensiva E aplicação analógica, inclusive in malam partem, pois a norma processual não define crimes nem comina penas — diferente do Direito Penal material, onde a analogia só é admitida in bonam partem.",
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
            "disc": "Direito Processual Penal",
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
