# -*- coding: utf-8 -*-
import json

with open("/home/claude/qbank/questions.json","r",encoding="utf-8") as f:
    BANK = json.load(f)

qid = [max(q["id"] for q in BANK)]
def nid():
    qid[0]+=1
    return qid[0]

def mc(corp, disc, enun, alts, correct, exp):
    assert len(alts)==5
    BANK.append({"id":nid(),"corp":corp,"disc":disc,"tipo":"MC","enun":enun,"alts":alts,"resp":correct,"exp":exp})

# BM extra
mc("BM","Noções de Primeiros Socorros","Em caso de suspeita de intoxicação por inalação de fumaça, uma conduta inicial recomendada é:",
   ["Manter a vítima no ambiente enfumaçado até a chegada do resgate.","Remover a vítima do ambiente para local com ar fresco assim que for seguro fazê-lo, e avaliar a necessidade de oxigênio e suporte respiratório.","Oferecer imediatamente água à vítima, independentemente do seu nível de consciência.","Induzir a tosse forçada na vítima.","Aguardar a melhora espontânea, sem qualquer intervenção."],
   1,"Remover a vítima do ambiente enfumaçado, assim que for seguro, e avaliar a necessidade de suporte respiratório é conduta inicial recomendada em casos de intoxicação por inalação de fumaça.")
mc("BM","Noções de Combate a Incêndio","O agente extintor 'espuma mecânica' atua, principalmente, por qual dos seguintes métodos de extinção do fogo?",
   ["Resfriamento exclusivamente.","Abafamento, ao formar uma camada que isola o combustível do comburente.","Retirada do material combustível.","Interrupção da reação em cadeia exclusivamente.","Nenhum dos métodos citados."],
   1,"A espuma mecânica atua, principalmente, pelo método de abafamento, formando uma camada que isola o material combustível do comburente (oxigênio), interrompendo a combustão.")
mc("BM","Segurança Contra Incêndio e Pânico","As chamadas 'saídas de emergência' de uma edificação devem, entre outros requisitos, permanecer:",
   ["Trancadas durante o expediente, por questões de segurança patrimonial.","Desobstruídas e sinalizadas, permitindo a evacuação segura dos ocupantes a qualquer momento.","Utilizadas exclusivamente pela equipe de limpeza.","Reservadas apenas para simulados previamente agendados.","Fechadas com cadeado, cuja chave fica com o síndico."],
   1,"As saídas de emergência devem permanecer desobstruídas e devidamente sinalizadas, garantindo a evacuação segura dos ocupantes da edificação a qualquer momento em que uma emergência ocorra.")
mc("BM","Legislação Institucional","No que se refere ao teste de aptidão física (TAF), etapa comum em concursos para ingresso em corporações militares estaduais, é correto afirmar que:",
   ["Tem caráter meramente classificatório, nunca eliminatório.","Tem, em regra, caráter eliminatório, avaliando a aptidão física do candidato para o exercício das atividades do cargo.","Não é exigido em nenhuma corporação militar estadual.","Substitui integralmente a avaliação de saúde.","É aplicado exclusivamente a candidatos do sexo masculino."],
   1,"O teste de aptidão física (TAF), em concursos desse tipo, tem, em regra, caráter eliminatório, avaliando se o candidato possui condições físicas compatíveis com o exercício das atividades do cargo militar pretendido.")
mc("BM","Raciocínio Lógico","Considerando a proposição 'Se o alarme disparar, então a equipe será mobilizada', assinale a alternativa que apresenta uma proposição logicamente equivalente a ela.",
   ["Se a equipe não for mobilizada, então o alarme não disparou.","Se a equipe for mobilizada, então o alarme disparou.","O alarme dispara e a equipe não é mobilizada.","O alarme não dispara e a equipe é mobilizada.","A equipe é mobilizada ou o alarme dispara."],
   0,"A contrapositiva de 'se p então q' ('se não q, então não p') é logicamente equivalente à condicional original: 'se a equipe não for mobilizada, então o alarme não disparou'.")
mc("BM","Língua Portuguesa","Assinale a alternativa em que a colocação pronominal está de acordo com a norma-padrão para o início de uma oração.",
   ["Se apresentaram ao comandante no horário previsto.","Apresentaram-se ao comandante no horário previsto.","Apresentaram se ao comandante no horário previsto.","Se-apresentaram ao comandante no horário previsto.","Ao comandante se apresentaram, sem regra específica."],
   1,"Em início absoluto de oração, a norma-padrão exige a ênclise: 'Apresentaram-se ao comandante...', e não a próclise ('Se apresentaram...').")

# PC extra
mc("PC","Direito Constitucional","Assinale a alternativa correta acerca da repartição de competências legislativas na Constituição Federal.",
   ["Compete exclusivamente à União legislar sobre toda e qualquer matéria.","A Constituição prevê competências privativas da União, competências concorrentes entre União, Estados e Distrito Federal, e competências dos Municípios, entre outras.","Os Municípios não possuem qualquer competência legislativa própria.","Compete exclusivamente aos Estados legislar sobre direito penal.","Não existe repartição de competências no federalismo brasileiro."],
   1,"A CF estabelece um sistema de repartição de competências legislativas, com competências privativas da União (art. 22), competências concorrentes entre União, Estados e Distrito Federal (art. 24), e competências dos Municípios (art. 30), entre outras hipóteses.")
mc("PC","Direito Administrativo","Assinale a alternativa correta sobre o princípio da eficiência na Administração Pública.",
   ["Foi introduzido no art. 37, caput, da CF, pela Emenda Constitucional nº 19/1998.","É sinônimo do princípio da legalidade.","Dispensa a Administração de observar critérios de qualidade na prestação de serviços públicos.","Aplica-se apenas a empresas públicas, e não à Administração direta.","Foi revogado pela Constituição de 1988."],
   0,"O princípio da eficiência foi expressamente incluído no rol do art. 37, caput, da CF, pela Emenda Constitucional nº 19/1998, exigindo da Administração Pública atuação qualitativamente satisfatória e com bons resultados.")
mc("PC","Direito Penal","Assinale a alternativa correta sobre o instituto da prescrição no Direito Penal.",
   ["A prescrição extingue a punibilidade do agente pelo decurso do tempo, nos prazos e condições previstos em lei.","A prescrição é sinônimo de anistia.","Não existe prescrição para nenhum crime no ordenamento jurídico brasileiro.","A prescrição impede apenas a execução da pena, mas não a persecução penal.","A prescrição é instituto exclusivo do direito civil, sem aplicação penal."],
   0,"A prescrição é causa extintiva da punibilidade, decorrente do decurso do tempo sem que o Estado exerça sua pretensão punitiva ou executória, nos prazos e condições estabelecidos em lei.")
mc("PC","Direito Processual Penal","Assinale a alternativa correta a respeito da prisão temporária, prevista em lei específica.",
   ["Tem prazo indeterminado, podendo se estender por anos.","Destina-se, em regra, a assegurar a investigação de determinados crimes, tendo prazo determinado e podendo ser decretada apenas nas hipóteses legais específicas.","É decretada exclusivamente pela autoridade policial, sem participação judicial.","Substitui, em qualquer caso, a necessidade de prisão preventiva.","Não exige qualquer fundamentação judicial."],
   1,"A prisão temporária, prevista na Lei nº 7.960/1989, destina-se a assegurar as investigações durante o inquérito policial em determinados crimes, tendo prazo determinado e exigindo decisão fundamentada da autoridade judiciária.")
mc("PC","Direitos Humanos","Assinale a alternativa correta acerca do princípio da dignidade humana aplicado à execução penal.",
   ["Permite tratamento desumano de presos em situações excepcionais de superlotação.","Impõe que a pessoa presa seja tratada com respeito à sua integridade física e moral, vedando tratamento desumano ou degradante.","Aplica-se apenas a presos provisórios, e não a condenados.","Não possui qualquer previsão constitucional ou legal no Brasil.","É incompatível com a existência do sistema prisional."],
   1,"O princípio da dignidade humana impõe que a pessoa presa seja tratada com respeito à integridade física e moral, sendo vedado qualquer tratamento desumano ou degradante, conforme previsto na Constituição Federal (art. 5º, III e XLIX) e em tratados internacionais.")
mc("PC","Raciocínio Lógico","Considere a proposição 'Se o suspeito confessar, então o inquérito será concluído mais rapidamente.' Assinale a alternativa logicamente equivalente a essa proposição.",
   ["Se o inquérito não for concluído mais rapidamente, então o suspeito não confessou.","Se o inquérito for concluído mais rapidamente, então o suspeito confessou.","O suspeito confessa e o inquérito não é concluído mais rapidamente.","O suspeito não confessa e o inquérito é concluído mais rapidamente.","O inquérito é concluído mais rapidamente ou o suspeito confessa."],
   0,"A contrapositiva de 'se p então q' é 'se não q, então não p', sendo logicamente equivalente à condicional original.")

with open("/home/claude/qbank/questions.json","w",encoding="utf-8") as f:
    json.dump(BANK, f, ensure_ascii=False, indent=None)

print("total:", len(BANK))
from collections import Counter
print(Counter(q["corp"] for q in BANK))
