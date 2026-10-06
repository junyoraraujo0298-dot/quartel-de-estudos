# -*- coding: utf-8 -*-
import json

with open("/home/claude/qbank/questions.json","r",encoding="utf-8") as f:
    BANK = json.load(f)

qid = [max(q["id"] for q in BANK)]
def nid():
    qid[0]+=1
    return qid[0]

def ce(corp, disc, enun, resp, exp):
    BANK.append({"id":nid(),"corp":corp,"disc":disc,"tipo":"CE","enun":enun,"resp":resp,"exp":exp})

def mc(corp, disc, enun, alts, correct, exp):
    assert len(alts)==5
    BANK.append({"id":nid(),"corp":corp,"disc":disc,"tipo":"MC","enun":enun,"alts":alts,"resp":correct,"exp":exp})

ce("PM","Noções de Informática","O termo 'wi-fi' refere-se a uma tecnologia de rede sem fio que permite a conexão de dispositivos à internet ou a uma rede local sem a necessidade de cabos.",True,"Correto. O Wi-Fi é uma tecnologia de rede local sem fio (WLAN), baseada em padrões IEEE 802.11, que permite a conexão de dispositivos sem a necessidade de cabeamento físico.")
ce("PM","Noções de Informática","Um arquivo compactado, com extensão '.zip', ocupa exatamente o mesmo espaço em disco que o arquivo original, sem qualquer redução de tamanho.",False,"Errado. A compactação de arquivos, como no formato .zip, tem justamente por objetivo reduzir o espaço ocupado em disco, por meio de algoritmos de compressão de dados.")
ce("PM","Legislação Institucional PM","O Boletim Geral (ou boletim interno) é um instrumento utilizado pelas corporações militares para a publicação de atos administrativos, promoções, punições e demais assuntos de interesse do efetivo.",True,"Correto. O Boletim Geral (ou boletim interno) é o meio oficial pelo qual as corporações militares tornam públicos atos administrativos e assuntos de interesse do efetivo, como promoções, punições, escalas e demais determinações.")
ce("PM","Geografia do Maranhão","O clima do leste maranhense, mais próximo do sertão nordestino, tende a apresentar índices pluviométricos mais baixos e maior irregularidade de chuvas do que o litoral e o centro-norte do estado.",True,"Correto. A porção leste do Maranhão, mais próxima do semiárido nordestino, tende a apresentar menores índices pluviométricos e maior irregularidade de chuvas em comparação a outras regiões do estado.")
ce("PM","História do Maranhão","O Maranhão, no período colonial, foi um dos poucos territórios brasileiros a ser colonizado inicialmente por potência europeia distinta de Portugal antes da consolidação do domínio português.",True,"Correto. Diferentemente da maior parte do litoral brasileiro, o Maranhão teve, inicialmente, colonização francesa (1612), antes de os portugueses expulsarem os franceses e, posteriormente, os holandeses, consolidando o domínio luso na região.")
mc("BM","Noções de Primeiros Socorros","Assinale a alternativa que apresenta corretamente a sigla PCR, utilizada no atendimento de emergência.",
   ["Procedimento Clínico de Resgate","Parada Cardiorrespiratória","Plano de Contingência Regional","Programa de Combate a Riscos","Protocolo de Comunicação em Resgate"],
   1,"PCR é a sigla utilizada para 'parada cardiorrespiratória', situação de emergência que exige reanimação cardiopulmonar imediata.")
mc("BM","Geografia do Maranhão","O bioma predominante na porção mais a leste do território maranhense, em transição para o semiárido nordestino, apresenta maior semelhança com qual bioma brasileiro?",
   ["Pampa","Caatinga","Pantanal","Mata de Araucárias","Manguezal exclusivo"],
   1,"A porção leste do Maranhão, em transição para o sertão nordestino, apresenta maior semelhança com a vegetação e o clima característicos da Caatinga.")
mc("PC","Direito Administrativo","Assinale a alternativa correta sobre o instituto da reversão no serviço público.",
   ["É a forma de provimento em que o servidor aposentado retorna à atividade, nas hipóteses previstas em lei.","É sinônimo de exoneração.","Aplica-se exclusivamente a cargos em comissão.","Extingue definitivamente o vínculo do servidor com a Administração.","É forma de ingresso originário no serviço público, sem necessidade de concurso."],
   0,"A reversão é a forma de provimento pela qual o servidor aposentado retorna à atividade, nas hipóteses e condições previstas na legislação estatutária aplicável.")
mc("PC","Criminologia","Assinale a alternativa que descreve corretamente o conceito de 'labeling approach' (teoria da rotulação), no âmbito da criminologia.",
   ["Defende que o crime é resultado exclusivo de fatores biológicos.","Sustenta que o desvio e a criminalidade resultam, em parte, de um processo social de rotulação (etiquetamento) de determinados indivíduos como criminosos.","É sinônimo da Escola Clássica de Criminologia.","Nega qualquer papel do controle social na definição do crime.","Aplica-se apenas a crimes patrimoniais."],
   1,"A teoria da rotulação (labeling approach) sustenta que a criminalidade, em parte, resulta de um processo social de rotulação (etiquetamento) de certos indivíduos como desviantes ou criminosos, influenciando sua trajetória subsequente.")
mc("PC","Legislação Especial","Assinale a alternativa correta a respeito da Lei de Execução Penal (Lei nº 7.210/1984).",
   ["Tem por objetivo exclusivo a punição do condenado, sem qualquer preocupação com sua reintegração social.","Tem por objetivo efetivar as disposições da sentença criminal e proporcionar condições para a integração social do condenado e do internado.","Aplica-se apenas a presos provisórios.","Não prevê qualquer direito ao preso durante o cumprimento da pena.","Foi revogada integralmente pelo Código Penal."],
   1,"O art. 1º da Lei de Execução Penal estabelece que ela tem por objetivo efetivar as disposições da sentença ou decisão criminal e proporcionar condições para a harmônica integração social do condenado e do internado.")
mc("PC","Medicina Legal","Assinale a alternativa correta a respeito do conceito de 'asfixia', estudado na medicina legal.",
   ["Refere-se exclusivamente a mortes por afogamento.","Refere-se à dificuldade ou impossibilidade de realizar as trocas gasosas normais do organismo, podendo ocorrer por diferentes mecanismos, como esganadura, enforcamento ou sufocação.","É sinônimo de intoxicação alimentar.","Aplica-se apenas a vítimas de acidentes de trânsito.","Não é objeto de estudo da medicina legal."],
   1,"A asfixia refere-se à dificuldade ou impossibilidade de realizar as trocas gasosas normais do organismo, podendo ocorrer por diferentes mecanismos, como esganadura, enforcamento, sufocação direta ou indireta, entre outros, sendo tema central da tanatologia forense.")

with open("/home/claude/qbank/questions.json","w",encoding="utf-8") as f:
    json.dump(BANK, f, ensure_ascii=False, indent=None)

print("total:", len(BANK))
from collections import Counter
print(Counter(q["corp"] for q in BANK))
