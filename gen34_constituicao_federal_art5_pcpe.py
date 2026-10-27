# -*- coding: utf-8 -*-
# Adiciona o texto integral do Art. 5 da Constituicao Federal
# (Direitos e Garantias Fundamentais) pra PC-PE: um novo deck na aba
# Estrategia (mesmo lugar onde ja estao Cronograma, Programa, a
# Constituicao de PE e o Estatuto do Policial Civil), ja que e
# conteudo de Direito Constitucional previsto no edital (Nocoes de
# Direito). Material sem questoes -- so o texto da lei. Fonte:
# "Slides-Direito-Constitucional-Direitos e Deveres Individuais e
# Coletivos (Art. 5o)", Prof. Franco, Focus Concursos.
import re
import json

with open('app-template.html', encoding='utf-8') as f:
    html = f.read()

LAW_ITEMS = [
    {"t": "tit", "x": "CONSTITUIÇÃO FEDERAL — ART. 5º (DIREITOS E DEVERES INDIVIDUAIS E COLETIVOS) — PC-PE"},
    {"t": "cap", "x": "TÍTULO II — Dos Direitos e Garantias Fundamentais / CAPÍTULO I — Dos Direitos e Deveres Individuais e Coletivos"},
    {"t": "art", "n": "Art. 5º, caput", "x": "Todos são iguais perante a lei, sem distinção de qualquer natureza, garantindo-se aos brasileiros e aos estrangeiros residentes no País a inviolabilidade do direito à vida, à liberdade, à igualdade, à segurança e à propriedade, nos termos seguintes:"},
    {"t": "art", "n": "Art. 5º, I", "x": "homens e mulheres são iguais em direitos e obrigações, nos termos desta Constituição;"},
    {"t": "art", "n": "Art. 5º, II", "x": "ninguém será obrigado a fazer ou deixar de fazer alguma coisa senão em virtude de lei;"},
    {"t": "art", "n": "Art. 5º, III", "x": "ninguém será submetido a tortura nem a tratamento desumano ou degradante;"},
    {"t": "art", "n": "Art. 5º, IV", "x": "é livre a manifestação do pensamento, sendo vedado o anonimato;"},
    {"t": "art", "n": "Art. 5º, V", "x": "é assegurado o direito de resposta, proporcional ao agravo, além da indenização por dano material, moral ou à imagem;"},
    {"t": "art", "n": "Art. 5º, VI", "x": "é inviolável a liberdade de consciência e de crença, sendo assegurado o livre exercício dos cultos religiosos e garantida, na forma da lei, a proteção aos locais de culto e a suas liturgias;"},
    {"t": "art", "n": "Art. 5º, VII", "x": "é assegurada, nos termos da lei, a prestação de assistência religiosa nas entidades civis e militares de internação coletiva;"},
    {"t": "art", "n": "Art. 5º, VIII", "x": "ninguém será privado de direitos por motivo de crença religiosa ou de convicção filosófica ou política, salvo se as invocar para eximir-se de obrigação legal a todos imposta e recusar-se a cumprir prestação alternativa, fixada em lei;"},
    {"t": "art", "n": "Art. 5º, IX", "x": "é livre a expressão da atividade intelectual, artística, científica e de comunicação, independentemente de censura ou licença;"},
    {"t": "art", "n": "Art. 5º, X", "x": "são invioláveis a intimidade, a vida privada, a honra e a imagem das pessoas, assegurado o direito a indenização pelo dano material ou moral decorrente de sua violação;"},
    {"t": "art", "n": "Art. 5º, XI", "x": "a casa é asilo inviolável do indivíduo, ninguém nela podendo penetrar sem consentimento do morador, salvo em caso de flagrante delito ou desastre, ou para prestar socorro, ou, durante o dia, por determinação judicial;"},
    {"t": "art", "n": "Art. 5º, XII", "x": "é inviolável o sigilo da correspondência e das comunicações telegráficas, de dados e das comunicações telefônicas, salvo, no último caso, por ordem judicial, nas hipóteses e na forma que a lei estabelecer para fins de investigação criminal ou instrução processual penal;"},
    {"t": "art", "n": "Art. 5º, XIII", "x": "é livre o exercício de qualquer trabalho, ofício ou profissão, atendidas as qualificações profissionais que a lei estabelecer;"},
    {"t": "art", "n": "Art. 5º, XIV", "x": "é assegurado a todos o acesso à informação e resguardado o sigilo da fonte, quando necessário ao exercício profissional;"},
    {"t": "art", "n": "Art. 5º, XV", "x": "é livre a locomoção no território nacional em tempo de paz, podendo qualquer pessoa, nos termos da lei, nele entrar, permanecer ou dele sair com seus bens;"},
    {"t": "art", "n": "Art. 5º, XVI", "x": "todos podem reunir-se pacificamente, sem armas, em locais abertos ao público, independentemente de autorização, desde que não frustrem outra reunião anteriormente convocada para o mesmo local, sendo apenas exigido prévio aviso à autoridade competente;"},
    {"t": "art", "n": "Art. 5º, XVII", "x": "é plena a liberdade de associação para fins lícitos, vedada a de caráter paramilitar;"},
    {"t": "art", "n": "Art. 5º, XVIII", "x": "a criação de associações e, na forma da lei, a de cooperativas independem de autorização, sendo vedada a interferência estatal em seu funcionamento;"},
    {"t": "art", "n": "Art. 5º, XIX", "x": "as associações só poderão ser compulsoriamente dissolvidas ou ter suas atividades suspensas por decisão judicial, exigindo-se, no primeiro caso, o trânsito em julgado;"},
    {"t": "art", "n": "Art. 5º, XX", "x": "ninguém poderá ser compelido a associar-se ou a permanecer associado;"},
    {"t": "art", "n": "Art. 5º, XXI", "x": "as entidades associativas, quando expressamente autorizadas, têm legitimidade para representar seus filiados judicial ou extrajudicialmente;"},
    {"t": "art", "n": "Art. 5º, XXII", "x": "é garantido o direito de propriedade;"},
    {"t": "art", "n": "Art. 5º, XXIII", "x": "a propriedade atenderá a sua função social;"},
    {"t": "art", "n": "Art. 5º, XXIV", "x": "a lei estabelecerá o procedimento para desapropriação por necessidade ou utilidade pública, ou por interesse social, mediante justa e prévia indenização em dinheiro, ressalvados os casos previstos nesta Constituição;"},
    {"t": "art", "n": "Art. 5º, XXV", "x": "no caso de iminente perigo público, a autoridade competente poderá usar de propriedade particular, assegurada ao proprietário indenização ulterior, se houver dano;"},
    {"t": "art", "n": "Art. 5º, XXVI", "x": "a pequena propriedade rural, assim definida em lei, desde que trabalhada pela família, não será objeto de penhora para pagamento de débitos decorrentes de sua atividade produtiva, dispondo a lei sobre os meios de financiar o seu desenvolvimento;"},
    {"t": "art", "n": "Art. 5º, XXVII", "x": "aos autores pertence o direito exclusivo de utilização, publicação ou reprodução de suas obras, transmissível aos herdeiros pelo tempo que a lei fixar;"},
    {"t": "art", "n": "Art. 5º, XXVIII", "x": "são assegurados, nos termos da lei: a) a proteção às participações individuais em obras coletivas e à reprodução da imagem e voz humanas, inclusive nas atividades desportivas; b) o direito de fiscalização do aproveitamento econômico das obras que criarem ou de que participarem aos criadores, aos intérpretes e às respectivas representações sindicais e associativas;"},
    {"t": "art", "n": "Art. 5º, XXIX", "x": "a lei assegurará aos autores de inventos industriais privilégio temporário para sua utilização, bem como proteção às criações industriais, à propriedade das marcas, aos nomes de empresas e a outros signos distintivos, tendo em vista o interesse social e o desenvolvimento tecnológico e econômico do País;"},
    {"t": "art", "n": "Art. 5º, XXX", "x": "é garantido o direito de herança;"},
    {"t": "art", "n": "Art. 5º, XXXI", "x": "a sucessão de bens de estrangeiros situados no País será regulada pela lei brasileira em benefício do cônjuge ou dos filhos brasileiros, sempre que não lhes seja mais favorável a lei pessoal do \"de cujus\";"},
    {"t": "art", "n": "Art. 5º, XXXII", "x": "o Estado promoverá, na forma da lei, a defesa do consumidor;"},
    {"t": "art", "n": "Art. 5º, XXXIII", "x": "todos têm direito a receber dos órgãos públicos informações de seu interesse particular, ou de interesse coletivo ou geral, que serão prestadas no prazo da lei, sob pena de responsabilidade, ressalvadas aquelas cujo sigilo seja imprescindível à segurança da sociedade e do Estado;"},
    {"t": "art", "n": "Art. 5º, XXXIV", "x": "são a todos assegurados, independentemente do pagamento de taxas: a) o direito de petição aos Poderes Públicos em defesa de direitos ou contra ilegalidade ou abuso de poder; b) a obtenção de certidões em repartições públicas, para defesa de direitos e esclarecimento de situações de interesse pessoal;"},
    {"t": "art", "n": "Art. 5º, XXXV", "x": "a lei não excluirá da apreciação do Poder Judiciário lesão ou ameaça a direito;"},
    {"t": "art", "n": "Art. 5º, XXXVI", "x": "a lei não prejudicará o direito adquirido, o ato jurídico perfeito e a coisa julgada;"},
    {"t": "art", "n": "Art. 5º, XXXVII", "x": "não haverá juízo ou tribunal de exceção;"},
    {"t": "art", "n": "Art. 5º, XXXVIII", "x": "é reconhecida a instituição do júri, com a organização que lhe der a lei, assegurados: a) a plenitude de defesa; b) o sigilo das votações; c) a soberania dos veredictos; d) a competência para o julgamento dos crimes dolosos contra a vida;"},
    {"t": "art", "n": "Art. 5º, XXXIX", "x": "não há crime sem lei anterior que o defina, nem pena sem prévia cominação legal;"},
    {"t": "art", "n": "Art. 5º, XL", "x": "a lei penal não retroagirá, salvo para beneficiar o réu;"},
    {"t": "art", "n": "Art. 5º, XLI", "x": "a lei punirá qualquer discriminação atentatória dos direitos e liberdades fundamentais;"},
    {"t": "art", "n": "Art. 5º, XLII", "x": "a prática do racismo constitui crime inafiançável e imprescritível, sujeito à pena de reclusão, nos termos da lei;"},
    {"t": "art", "n": "Art. 5º, XLIII", "x": "a lei considerará crimes inafiançáveis e insuscetíveis de graça ou anistia a prática da tortura, o tráfico ilícito de entorpecentes e drogas afins, o terrorismo e os definidos como crimes hediondos, por eles respondendo os mandantes, os executores e os que, podendo evitá-los, se omitirem;"},
    {"t": "art", "n": "Art. 5º, XLIV", "x": "constitui crime inafiançável e imprescritível a ação de grupos armados, civis ou militares, contra a ordem constitucional e o Estado Democrático;"},
    {"t": "art", "n": "Art. 5º, XLV", "x": "nenhuma pena passará da pessoa do condenado, podendo a obrigação de reparar o dano e a decretação do perdimento de bens ser, nos termos da lei, estendidas aos sucessores e contra eles executadas, até o limite do valor do patrimônio transferido;"},
    {"t": "art", "n": "Art. 5º, XLVI", "x": "a lei regulará a individualização da pena e adotará, entre outras, as seguintes: a) privação ou restrição da liberdade; b) perda de bens; c) multa; d) prestação social alternativa; e) suspensão ou interdição de direitos;"},
    {"t": "art", "n": "Art. 5º, XLVII", "x": "não haverá penas: a) de morte, salvo em caso de guerra declarada, nos termos do art. 84, XIX; b) de caráter perpétuo; c) de trabalhos forçados; d) de banimento; e) cruéis;"},
    {"t": "art", "n": "Art. 5º, XLVIII", "x": "a pena será cumprida em estabelecimentos distintos, de acordo com a natureza do delito, a idade e o sexo do apenado;"},
    {"t": "art", "n": "Art. 5º, XLIX", "x": "é assegurado aos presos o respeito à integridade física e moral;"},
    {"t": "art", "n": "Art. 5º, L", "x": "às presidiárias serão asseguradas condições para que possam permanecer com seus filhos durante o período de amamentação;"},
    {"t": "art", "n": "Art. 5º, LI", "x": "nenhum brasileiro será extraditado, salvo o naturalizado, em caso de crime comum, praticado antes da naturalização, ou de comprovado envolvimento em tráfico ilícito de entorpecentes e drogas afins, na forma da lei;"},
    {"t": "art", "n": "Art. 5º, LII", "x": "não será concedida extradição de estrangeiro por crime político ou de opinião;"},
    {"t": "art", "n": "Art. 5º, LIII", "x": "ninguém será processado nem sentenciado senão pela autoridade competente;"},
    {"t": "art", "n": "Art. 5º, LIV", "x": "ninguém será privado da liberdade ou de seus bens sem o devido processo legal;"},
    {"t": "art", "n": "Art. 5º, LV", "x": "aos litigantes, em processo judicial ou administrativo, e aos acusados em geral são assegurados o contraditório e ampla defesa, com os meios e recursos a ela inerentes;"},
    {"t": "art", "n": "Art. 5º, LVI", "x": "são inadmissíveis, no processo, as provas obtidas por meios ilícitos;"},
    {"t": "art", "n": "Art. 5º, LVII", "x": "ninguém será considerado culpado até o trânsito em julgado de sentença penal condenatória;"},
    {"t": "art", "n": "Art. 5º, LVIII", "x": "o civilmente identificado não será submetido a identificação criminal, salvo nas hipóteses previstas em lei;"},
    {"t": "art", "n": "Art. 5º, LIX", "x": "será admitida ação privada nos crimes de ação pública, se esta não for intentada no prazo legal;"},
    {"t": "art", "n": "Art. 5º, LX", "x": "a lei só poderá restringir a publicidade dos atos processuais quando a defesa da intimidade ou o interesse social o exigirem;"},
    {"t": "art", "n": "Art. 5º, LXI", "x": "ninguém será preso senão em flagrante delito ou por ordem escrita e fundamentada de autoridade judiciária competente, salvo nos casos de transgressão militar ou crime propriamente militar, definidos em lei;"},
    {"t": "art", "n": "Art. 5º, LXII", "x": "a prisão de qualquer pessoa e o local onde se encontre serão comunicados imediatamente ao juiz competente e à família do preso ou à pessoa por ele indicada;"},
    {"t": "art", "n": "Art. 5º, LXIII", "x": "o preso será informado de seus direitos, entre os quais o de permanecer calado, sendo-lhe assegurada a assistência da família e de advogado;"},
    {"t": "art", "n": "Art. 5º, LXIV", "x": "o preso tem direito à identificação dos responsáveis por sua prisão ou por seu interrogatório policial;"},
    {"t": "art", "n": "Art. 5º, LXV", "x": "a prisão ilegal será imediatamente relaxada pela autoridade judiciária;"},
    {"t": "art", "n": "Art. 5º, LXVI", "x": "ninguém será levado à prisão ou nela mantido, quando a lei admitir a liberdade provisória, com ou sem fiança;"},
    {"t": "art", "n": "Art. 5º, LXVII", "x": "não haverá prisão civil por dívida, salvo a do responsável pelo inadimplemento voluntário e inescusável de obrigação alimentícia e a do depositário infiel;"},
    {"t": "art", "n": "Art. 5º, LXVIII", "x": "conceder-se-á \"habeas-corpus\" sempre que alguém sofrer ou se achar ameaçado de sofrer violência ou coação em sua liberdade de locomoção, por ilegalidade ou abuso de poder;"},
    {"t": "art", "n": "Art. 5º, LXIX", "x": "conceder-se-á mandado de segurança para proteger direito líquido e certo, não amparado por \"habeas-corpus\" ou \"habeas-data\", quando o responsável pela ilegalidade ou abuso de poder for autoridade pública ou agente de pessoa jurídica no exercício de atribuições do Poder Público;"},
    {"t": "art", "n": "Art. 5º, LXX", "x": "o mandado de segurança coletivo pode ser impetrado por: a) partido político com representação no Congresso Nacional; b) organização sindical, entidade de classe ou associação legalmente constituída e em funcionamento há pelo menos um ano, em defesa dos interesses de seus membros ou associados;"},
    {"t": "art", "n": "Art. 5º, LXXI", "x": "conceder-se-á mandado de injunção sempre que a falta de norma regulamentadora torne inviável o exercício dos direitos e liberdades constitucionais e das prerrogativas inerentes à nacionalidade, à soberania e à cidadania;"},
    {"t": "art", "n": "Art. 5º, LXXII", "x": "conceder-se-á \"habeas-data\": a) para assegurar o conhecimento de informações relativas à pessoa do impetrante, constantes de registros ou bancos de dados de entidades governamentais ou de caráter público; b) para a retificação de dados, quando não se prefira fazê-lo por processo sigiloso, judicial ou administrativo;"},
    {"t": "art", "n": "Art. 5º, LXXIII", "x": "qualquer cidadão é parte legítima para propor ação popular que vise a anular ato lesivo ao patrimônio público ou de entidade de que o Estado participe, à moralidade administrativa, ao meio ambiente e ao patrimônio histórico e cultural, ficando o autor, salvo comprovada má-fé, isento de custas judiciais e do ônus da sucumbência;"},
    {"t": "art", "n": "Art. 5º, LXXIV", "x": "o Estado prestará assistência jurídica integral e gratuita aos que comprovarem insuficiência de recursos;"},
    {"t": "art", "n": "Art. 5º, LXXV", "x": "o Estado indenizará o condenado por erro judiciário, assim como o que ficar preso além do tempo fixado na sentença;"},
    {"t": "art", "n": "Art. 5º, LXXVI", "x": "são gratuitos para os reconhecidamente pobres, na forma da lei: a) o registro civil de nascimento; b) a certidão de óbito;"},
    {"t": "art", "n": "Art. 5º, LXXVII", "x": "são gratuitas as ações de \"habeas-corpus\" e \"habeas-data\", e, na forma da lei, os atos necessários ao exercício da cidadania;"},
    {"t": "art", "n": "Art. 5º, LXXVIII", "x": "a todos, no âmbito judicial e administrativo, são assegurados a razoável duração do processo e os meios que garantam a celeridade de sua tramitação;"},
    {"t": "art", "n": "Art. 5º, LXXIX", "x": "é assegurado, nos termos da lei, o direito à proteção dos dados pessoais, inclusive nos meios digitais."},
    {"t": "art", "n": "Art. 5º, § 1º", "x": "As normas definidoras dos direitos e garantias fundamentais têm aplicação imediata."},
    {"t": "art", "n": "Art. 5º, § 2º", "x": "Os direitos e garantias expressos nesta Constituição não excluem outros decorrentes do regime e dos princípios por ela adotados, ou dos tratados internacionais em que a República Federativa do Brasil seja parte."},
    {"t": "art", "n": "Art. 5º, § 3º", "x": "Os tratados e convenções internacionais sobre direitos humanos que forem aprovados, em cada Casa do Congresso Nacional, em dois turnos, por três quintos dos votos dos respectivos membros, serão equivalentes às emendas constitucionais."},
    {"t": "art", "n": "Art. 5º, § 4º", "x": "O Brasil se submete à jurisdição de Tribunal Penal Internacional a cuja criação tenha manifestado adesão."},
]

array_literal = '[\n' + ',\n'.join(json.dumps(it, ensure_ascii=False) for it in LAW_ITEMS) + '\n]'

decoder = json.JSONDecoder()
m = re.search(r'const LAW_PE_ESTATUTO_POLICIAL\s*=\s*\[', html)
assert m, "bloco LAW_PE_ESTATUTO_POLICIAL nao encontrado"
start = m.end() - 1
_arr, end = decoder.raw_decode(html, start)
insertion_point = end + 1  # depois do ';'
new_block = '\n\nconst LAW_CF_ART5_PCPE = ' + array_literal + ';'
html = html[:insertion_point] + new_block + html[insertion_point:]

old_estrategia_tail = (
    '  estatuto_policial_pe: { label: "Estatuto do Policial Civil de PE (Lei 6.425/1972)", '
    'data: LAW_PE_ESTATUTO_POLICIAL, corp: "PCPE" }\n};'
)
assert old_estrategia_tail in html, "final de ESTRATEGIA_DECKS nao encontrado como esperado"
new_estrategia_tail = (
    '  estatuto_policial_pe: { label: "Estatuto do Policial Civil de PE (Lei 6.425/1972)", '
    'data: LAW_PE_ESTATUTO_POLICIAL, corp: "PCPE" },\n'
    '  cf_art5_pcpe: { label: "Constituição Federal — Art. 5º (Direitos e Garantias Fundamentais)", '
    'data: LAW_CF_ART5_PCPE, corp: "PCPE" }\n};'
)
html = html.replace(old_estrategia_tail, new_estrategia_tail, 1)

with open('app-template.html', 'w', encoding='utf-8', newline='') as f:
    f.write(html)
print('LAW_CF_ART5_PCPE adicionada com', len(LAW_ITEMS), 'itens; registrada em ESTRATEGIA_DECKS.')

with open('questions.json', encoding='utf-8') as f:
    qdata_raw = f.read()
with open('app-template.html', encoding='utf-8') as f:
    html2 = f.read()
html2 = html2.replace('__QUESTIONS_JSON__', qdata_raw)
with open('estudo-cebraspe-ma.html', 'w', encoding='utf-8') as f:
    f.write(html2)
print('estudo-cebraspe-ma.html regenerado com sucesso')
