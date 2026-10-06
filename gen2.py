# -*- coding: utf-8 -*-
import json, random
random.seed(7)

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

def shuffle_alts(correct_val, distractors):
    opts = [correct_val]+distractors
    idxs = list(range(5))
    random.shuffle(idxs)
    alts = [None]*5
    correct_idx = None
    vals = opts[:]
    random.shuffle(vals)
    for i,v in enumerate(vals):
        alts[i]=str(v)
        if v==correct_val:
            correct_idx=i
    return alts, correct_idx

# =====================================================================
# RACIOCINIO LOGICO - sequences (PA/PG) - PM (CE)
# =====================================================================
contexts_pm = ["viaturas em patrulhamento","policiais escalados para o plantão","ocorrências registradas no boletim",
               "rondas realizadas na semana","armamentos vistoriados no quartel"]
for i in range(14):
    a = random.randint(2,9)
    r = random.randint(2,6)
    terms = [a+k*r for k in range(5)]
    ctx = contexts_pm[i % len(contexts_pm)]
    true_stmt = f"Na sequência {', '.join(map(str,terms))}, referente a {ctx}, cada termo é obtido somando-se {r} unidades ao termo anterior, tratando-se de uma progressão aritmética de razão {r}."
    ce("PM","Raciocínio Lógico", true_stmt, True, f"Correto. De fato, {terms[1]}-{terms[0]}={r}, {terms[2]}-{terms[1]}={r}, e assim sucessivamente: trata-se de progressão aritmética de razão {r}.")
    wrong_r = r+random.choice([1,2,-1])
    if wrong_r==r or wrong_r<=0: wrong_r = r+3
    false_stmt = f"Na sequência {', '.join(map(str,terms))}, referente a {ctx}, cada termo é obtido somando-se {wrong_r} unidades ao termo anterior."
    ce("PM","Raciocínio Lógico", false_stmt, False, f"Errado. A diferença constante entre os termos é {r}, e não {wrong_r}; trata-se de progressão aritmética de razão {r}.")

for i in range(10):
    a = random.randint(1,4)
    r = random.choice([2,3])
    terms = [a*(r**k) for k in range(5)]
    true_stmt = f"Na sequência numérica {', '.join(map(str,terms))}, cada termo é obtido multiplicando-se o termo anterior por {r}, caracterizando progressão geométrica de razão {r}."
    ce("PM","Raciocínio Lógico", true_stmt, True, f"Correto. Cada termo é o produto do anterior por {r} (progressão geométrica de razão {r}): {terms}.")
    ce("PM","Raciocínio Lógico", f"Na sequência numérica {', '.join(map(str,terms))}, cada termo é obtido somando-se {r} unidades ao termo anterior.", False, f"Errado. Trata-se de progressão geométrica (multiplicação por {r} a cada termo), e não de progressão aritmética por soma.")

# Inclusion-exclusion word problems - PM (CE)
groups_pm = [("policiais","curso de tiro","curso de trânsito"), ("viaturas","equipadas com rádio","equipadas com câmera"),
             ("sargentos","lotados na capital","lotados no interior")]
for i in range(8):
    total = random.randint(40,90)
    a_ = random.randint(20,total-10)
    b_ = random.randint(15,total-10)
    both = random.randint(5, min(a_,b_)-2) if min(a_,b_)>7 else 5
    at_least_one = a_+b_-both
    grp, x1, x2 = groups_pm[i % len(groups_pm)]
    stmt_true = f"Considerando um grupo de {total} {grp}, sendo {a_} com {x1} e {b_} com {x2}, havendo {both} com ambas as qualificações, o número de {grp} com pelo menos uma dessas qualificações é {at_least_one}."
    ce("PM","Raciocínio Lógico", stmt_true, True, f"Correto. Pelo princípio da inclusão-exclusão: {a_} + {b_} − {both} = {at_least_one}.")
    wrong_val = at_least_one + random.choice([-3,3,5])
    stmt_false = f"Considerando um grupo de {total} {grp}, sendo {a_} com {x1} e {b_} com {x2}, havendo {both} com ambas as qualificações, o número de {grp} com pelo menos uma dessas qualificações é {wrong_val}."
    ce("PM","Raciocínio Lógico", stmt_false, False, f"Errado. Pelo princípio da inclusão-exclusão, o correto é {a_} + {b_} − {both} = {at_least_one}, e não {wrong_val}.")

# =====================================================================
# RACIOCINIO LOGICO - sequences (PA/PG) - BM & PC (MC)
# =====================================================================
def seq_mc(corp):
    a = random.randint(2,9)
    r = random.randint(2,7)
    terms = [a+k*r for k in range(5)]
    nxt = terms[-1]+r
    distractors = [nxt+r, nxt-1, nxt+2, terms[-1]+random.choice([1,3,5])]
    distractors = list(dict.fromkeys([d for d in distractors if d!=nxt]))[:4]
    while len(distractors)<4:
        distractors.append(nxt+random.randint(2,9))
    alts, idx = shuffle_alts(nxt, distractors[:4])
    stmt = f"Considere a sequência: {', '.join(map(str,terms))}. O próximo número da sequência é:"
    mc(corp,"Raciocínio Lógico", stmt, alts, idx, f"A sequência é uma progressão aritmética de razão {r} (cada termo soma {r} ao anterior); o próximo termo é {terms[-1]} + {r} = {nxt}.")

def geo_mc(corp):
    a = random.randint(1,5)
    r = random.choice([2,3])
    terms=[a*(r**k) for k in range(5)]
    nxt = terms[-1]*r
    distractors=[terms[-1]+terms[-2], nxt+r, nxt-r, terms[-1]*2]
    distractors = list(dict.fromkeys([d for d in distractors if d!=nxt]))[:4]
    while len(distractors)<4:
        distractors.append(nxt+random.randint(3,20))
    alts, idx = shuffle_alts(nxt, distractors[:4])
    stmt = f"Considere a sequência: {', '.join(map(str,terms))}. O próximo número da sequência é:"
    mc(corp,"Raciocínio Lógico", stmt, alts, idx, f"Trata-se de progressão geométrica de razão {r} (cada termo é o produto do anterior por {r}); o próximo termo é {terms[-1]} × {r} = {nxt}.")

for i in range(6): seq_mc("BM")
for i in range(4): geo_mc("BM")
for i in range(6): seq_mc("PC")
for i in range(4): geo_mc("PC")

groups_bmpc = {
 "BM": [("bombeiros","curso de resgate em altura","curso de mergulho"), ("viaturas de resgate","equipadas com desencarcerador","equipadas com autonomia respiratória")],
 "PC": [("investigadores","especialização em crimes cibernéticos","especialização em crimes patrimoniais"), ("escrivães","lotados na capital","lotados no interior")]
}
for corp,glist in groups_bmpc.items():
    for i in range(5):
        total = random.randint(40,90)
        a_ = random.randint(20,total-10)
        b_ = random.randint(15,total-10)
        both = random.randint(5, min(a_,b_)-2) if min(a_,b_)>7 else 5
        at_least_one = a_+b_-both
        grp,x1,x2 = glist[i % len(glist)]
        distractors=[at_least_one+3, at_least_one-3, a_+b_, both]
        distractors = list(dict.fromkeys([d for d in distractors if d!=at_least_one]))[:4]
        while len(distractors)<4:
            distractors.append(at_least_one+random.randint(2,15))
        alts, idx = shuffle_alts(at_least_one, distractors[:4])
        stmt = f"Em um grupo de {total} {grp}, {a_} têm {x1} e {b_} têm {x2}, havendo {both} com ambas as qualificações. O número de {grp} com pelo menos uma dessas qualificações é:"
        mc(corp,"Raciocínio Lógico", stmt, alts, idx, f"Pelo princípio da inclusão-exclusão: {a_} + {b_} − {both} = {at_least_one}.")

# =====================================================================
# PORTUGUES - additional templated drills (crase / concordancia impessoal)
# =====================================================================
crase_true = [
 ("Cheguei à escola no horário certo.","escola"), ("Referia-se à diretora com respeito.","diretora"),
 ("Estava à espreita havia horas.","espreita"), ("Voltou à cidade natal após anos.","cidade natal"),
 ("Fez tudo às pressas.","pressas"), ("Andava à toa pelo quartel.","toa"),
 ("Respondeu à pergunta com calma.","pergunta"), ("Foi à feira comprar mantimentos.","feira"),
]
for frase, termo in crase_true:
    corp = random.choice(["PM","BM","PC"])
    if corp=="PM":
        ce(corp,"Língua Portuguesa", f"Na frase '{frase}', o uso do acento indicativo de crase está correto, por se tratar de locução ou de regência que exige o artigo feminino 'a' combinado à preposição 'a'.", True, f"Correto. Antes de '{termo}', ocorre a fusão da preposição 'a' com o artigo feminino 'a', justificando o emprego da crase.")
    else:
        wrong = frase.replace(" à "," a ").replace(" às "," as ")
        mc(corp,"Língua Portuguesa", "Assinale a alternativa em que o emprego (ou não) da crase está de acordo com a norma-padrão.",
           [frase, wrong, frase.replace(" à "," há ") if " à " in frase else frase, frase.upper(), frase.replace(".", " apenas.")],
           0, f"A forma correta é '{frase}', com o acento indicativo de crase antes de '{termo}', pela fusão da preposição 'a' com o artigo feminino.")

hp_periods = ["três anos","seis meses","dois anos","dez dias","um ano"]
for periodo in hp_periods:
    corp = random.choice(["PM","BM","PC"])
    if corp=="PM":
        ce(corp,"Língua Portuguesa", f"Na frase 'Fazem {periodo} que o concurso não é realizado', há desvio da norma-padrão, pois o verbo 'fazer', indicando tempo decorrido, deveria permanecer impessoal, no singular.", True, f"Correto. Indicando tempo decorrido, 'fazer' é impessoal e deve ficar sempre no singular: 'Faz {periodo}...'.")
    else:
        mc(corp,"Língua Portuguesa", f"Assinale a alternativa correta quanto à concordância verbal, indicando tempo decorrido.",
           [f"Fazem {periodo} que o fato ocorreu.", f"Faz {periodo} que o fato ocorreu.", f"Houveram {periodo} desde o fato.", f"Vão fazer, no plural, {periodo}.", f"Fazem-se {periodo} de apuração."],
           1, f"O correto é 'Faz {periodo} que o fato ocorreu', pois o verbo 'fazer', indicando tempo decorrido, é impessoal e permanece sempre no singular.")

regencia_pairs = [("assistir (presenciar)","a"), ("obedecer","a"), ("aspirar (desejar)","a"), ("preferir X a Y","a"), ("chegar","a"), ("visar (pretender)","a")]
for verbo, prep in regencia_pairs:
    corp = random.choice(["PM","BM","PC"])
    if corp=="PM":
        ce(corp,"Língua Portuguesa", f"O verbo '{verbo}', na norma-padrão, rege-se com a preposição '{prep}'.", True, f"Correto. A regência padrão do verbo '{verbo}' exige a preposição '{prep}'.")
    else:
        mc(corp,"Língua Portuguesa", f"Assinale a alternativa que indica corretamente a preposição exigida, na norma-padrão, pelo verbo '{verbo}'.",
           ["de","em","com","para", prep] if prep!="para" else ["de","em","com","a","para"],
           4 if prep!="para" else 3,
           f"A regência padrão do verbo '{verbo}' exige a preposição '{prep}'.")

# =====================================================================
# INFORMATICA - additional facts
# =====================================================================
info_facts = [
 ("O termo 'spyware' designa um tipo de software malicioso que coleta informações do usuário sem seu consentimento.", True, "Correto. Spyware é um malware que espiona e coleta dados do usuário, geralmente de forma oculta, sem seu consentimento."),
 ("Um 'worm' é um tipo de malware que, ao contrário do vírus, não precisa de um programa hospedeiro para se replicar e se espalhar pela rede.", True, "Correto. O worm se autorreplica e se propaga de forma autônoma pela rede, sem necessidade de infectar um arquivo hospedeiro como o vírus tradicional faz."),
 ("O protocolo POP3 e o protocolo IMAP são utilizados exclusivamente para navegação em páginas web, e não para recebimento de e-mails.", False, "Errado. POP3 e IMAP são protocolos utilizados para recebimento de e-mails; a navegação web utiliza majoritariamente o protocolo HTTP/HTTPS."),
 ("Um endereço IP é um identificador numérico usado para localizar um dispositivo em uma rede de computadores.", True, "Correto. O endereço IP (Internet Protocol) identifica de forma única um dispositivo dentro de uma rede, permitindo o roteamento de dados."),
 ("O Bluetooth é uma tecnologia de comunicação sem fio de curto alcance, utilizada para conectar dispositivos como fones de ouvido e teclados.", True, "Correto. O Bluetooth é uma tecnologia de curto alcance amplamente usada para conectar periféricos sem fio, como fones, teclados e mouses."),
 ("O termo 'VPN' refere-se a uma rede privada virtual, que cria uma conexão criptografada sobre uma rede pública, aumentando a privacidade do usuário.", True, "Correto. A VPN (Virtual Private Network) cria um túnel criptografado sobre uma rede pública, como a internet, protegendo a privacidade e os dados do usuário."),
 ("No Windows, o atalho Ctrl+C é utilizado para colar um conteúdo previamente copiado.", False, "Errado. Ctrl+C é utilizado para copiar um conteúdo selecionado; o atalho para colar é Ctrl+V."),
 ("O termo 'cookie', na navegação web, refere-se a um pequeno arquivo de texto armazenado pelo navegador, utilizado para guardar informações sobre a navegação do usuário.", True, "Correto. Cookies são pequenos arquivos armazenados pelo navegador que guardam dados sobre a navegação, preferências e sessões do usuário em um site."),
 ("Um SSD (Solid State Drive) utiliza discos magnéticos giratórios para armazenamento de dados, da mesma forma que um HD tradicional.", False, "Errado. Diferentemente do HD tradicional, o SSD utiliza memória flash (sem partes móveis), o que o torna geralmente mais rápido e resistente a impactos."),
 ("O termo 'DDoS' refere-se a um ataque cibernético que visa sobrecarregar um servidor ou serviço com um volume excessivo de requisições, tornando-o indisponível.", True, "Correto. O ataque DDoS (Distributed Denial of Service) busca tornar um serviço indisponível sobrecarregando-o com tráfego excessivo, geralmente proveniente de múltiplas origens."),
 ("No Microsoft Excel, a função SE (IF) permite realizar testes lógicos, retornando um valor caso a condição seja verdadeira e outro caso seja falsa.", True, "Correto. A função SE (=SE(teste_lógico;valor_se_verdadeiro;valor_se_falso)) é amplamente usada para testes condicionais em planilhas."),
 ("O termo 'criptografia de ponta a ponta' significa que apenas o remetente e o destinatário conseguem ler o conteúdo da mensagem, impedindo que intermediários tenham acesso ao conteúdo.", True, "Correto. Na criptografia de ponta a ponta (end-to-end), somente os dispositivos do remetente e do destinatário possuem as chaves para decifrar a mensagem, impedindo o acesso por terceiros, incluindo o próprio provedor do serviço."),
 ("Um navegador de internet (browser) é um tipo de sistema operacional utilizado para gerenciar o hardware do computador.", False, "Errado. O navegador é um software para acessar páginas web; o sistema operacional é que gerencia o hardware e os recursos do computador (como Windows, Linux ou macOS)."),
 ("O uso de autenticação em dois fatores (2FA) é uma medida recomendada de segurança da informação, pois adiciona uma camada extra de proteção além da senha.", True, "Correto. A autenticação em dois fatores exige uma segunda forma de verificação além da senha, dificultando o acesso não autorizado, mesmo que a senha seja comprometida."),
 ("Um arquivo com extensão '.pdf' é, necessariamente, editável em qualquer editor de texto simples, como o Bloco de Notas, sem perda de formatação.", False, "Errado. Arquivos PDF possuem formatação e estrutura interna específicas; não são adequadamente editáveis em um editor de texto simples sem perda de formatação, exigindo softwares específicos para edição."),
]
for enun, resp, exp in info_facts:
    corp = random.choice(["PM","PC"])
    if corp=="PM":
        ce(corp,"Noções de Informática", enun, resp, exp)
    else:
        # convert into MC true/false style ("assinale a alternativa correta")
        if resp:
            wrong_versions = [enun.replace("permite","impede") if "permite" in enun else "Afirmação contrária à correta.",
                               "Nenhuma das afirmações anteriores está correta.",
                               enun.replace("é","não é",1) if " é " in enun else "Informação incorreta sobre o tema.",
                               "O conceito descrito não existe em informática."]
        else:
            wrong_versions = [enun, "Nenhuma das afirmações anteriores está correta.", "Informação incorreta sobre o tema.", "O conceito descrito não existe em informática."]
        correct_stmt = exp.split(". ",1)[-1] if resp else exp.split(". ",1)[-1]
        alts5 = [correct_stmt] + wrong_versions[:4]
        alts, idx = shuffle_alts(correct_stmt, wrong_versions[:4])
        mc(corp,"Noções de Informática", "Assinale a alternativa correta sobre o tema tratado a seguir: " + enun.split(",")[0] + ".", alts, idx, exp)

with open("/home/claude/qbank/questions.json","w",encoding="utf-8") as f:
    json.dump(BANK, f, ensure_ascii=False, indent=None)

print("total:", len(BANK))
from collections import Counter
c = Counter((q["corp"]) for q in BANK)
print(c)
c2 = Counter((q["corp"],q["disc"]) for q in BANK)
for k,v in sorted(c2.items()):
    print(k,v)
