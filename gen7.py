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

ce("PM","Raciocínio Lógico","Se a proposição 'p' é falsa, a disjunção 'p ou q' será necessariamente falsa, independentemente do valor lógico de 'q'.",False,"Errado. A disjunção 'p ou q' só é falsa quando ambas as proposições, p e q, forem falsas; se p for falsa mas q for verdadeira, a disjunção será verdadeira.")
ce("PM","Geografia do Brasil","A Amazônia Legal é uma delimitação administrativa brasileira que engloba estados da região Norte e também parte de estados de outras regiões, como o Maranhão e o Mato Grosso.",True,"Correto. A Amazônia Legal é uma área definida por critérios administrativos que engloba, além dos estados da região Norte, parte do Maranhão e do Mato Grosso, entre outros, para fins de planejamento e políticas públicas regionais.")
mc("BM","Língua Portuguesa","Assinale a alternativa em que a palavra destacada está grafada corretamente.",
   ["Rúbrica","Ruubrica","Rúbryca","Rubrika","Rubryca"],
   0,"A grafia correta é 'rúbrica', com acento agudo na sílaba tônica 'rú'.")
mc("PC","Direito Penal","Assinale a alternativa correta acerca do princípio da insignificância (ou bagatela) no Direito Penal.",
   ["É aplicado indiscriminadamente a qualquer crime, independentemente de suas circunstâncias.","Pode, conforme construção jurisprudencial, afastar a tipicidade material de condutas que, embora formalmente típicas, sejam materialmente insignificantes, consideradas a mínima ofensividade e a ausência de periculosidade social.","É previsto expressamente, de forma literal, em todos os artigos do Código Penal.","Aplica-se exclusivamente a crimes militares.","Impede qualquer responsabilização, inclusive civil, do agente."],
   1,"O princípio da insignificância, de construção jurisprudencial, pode afastar a tipicidade material de condutas formalmente típicas, mas materialmente insignificantes, consideradas critérios como a mínima ofensividade da conduta e a ausência de periculosidade social.")
mc("PC","Noções de Informática","Assinale a alternativa correta a respeito do conceito de 'engenharia social' aplicado à segurança da informação.",
   ["Técnica de programação de sistemas operacionais.","Conjunto de técnicas utilizadas para manipular psicologicamente pessoas, induzindo-as a fornecer informações sigilosas ou realizar ações que comprometam a segurança.","Sinônimo de criptografia de dados.","Tipo de hardware utilizado em redes corporativas.","Protocolo de comunicação segura equivalente ao HTTPS."],
   1,"Engenharia social refere-se a técnicas de manipulação psicológica utilizadas para induzir pessoas a fornecer informações sigilosas ou realizar ações que comprometam a segurança de sistemas, sem exploração de falhas técnicas propriamente ditas.")

with open("/home/claude/qbank/questions.json","w",encoding="utf-8") as f:
    json.dump(BANK, f, ensure_ascii=False, indent=None)
print("total:", len(BANK))
from collections import Counter
print(Counter(q["corp"] for q in BANK))
