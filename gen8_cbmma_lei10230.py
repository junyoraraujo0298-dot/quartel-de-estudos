# -*- coding: utf-8 -*-
# Acrescenta ao banco de questoes um bloco MC (Multipla Escolha) nivel-prova
# sobre a Lei n. 10.230/2015 (Organizacao Basica do CBMMA), no mesmo
# formato ja usado para o corp "BM" no restante do banco (tipo "MC",
# com "alts" e "resp" numerico 0-based), com distratores plausiveis e
# algumas pegadinhas cruzadas com a Lei 12.896/2026 (PMMA).
#
# IMPORTANTE: questions.json tem uma linha gigante inicial (ids 1..~610)
# seguida de UMA QUESTAO POR LINHA (", {...}") para os ids adicionados
# depois, terminando com "]". Para nao gerar um diff gigante inutil,
# este script NAO recarrega/regrava o JSON inteiro com json.dump --
# ele so acrescenta novas linhas nesse mesmo formato, antes do "]" final.
import json

with open('questions.json', encoding='utf-8') as f:
    raw = f.read()

data_check = json.loads(raw)  # so para validar e checar o max id
max_id = max(q['id'] for q in data_check)
assert max_id == 790, f"id maximo inesperado: {max_id}"

DISC = "Lei 10.230/2015 (Organização Básica do CBMMA)"

new_questions = [
    {"id": 791, "corp": "BM", "disc": DISC, "tipo": "MC",
     "enun": "Assinale a alternativa correta acerca da natureza institucional do CBMMA, nos termos da Lei nº 10.230/2015.",
     "alts": [
        "Órgão autônomo e independente, não vinculado a nenhum dos ramos das Forças Armadas.",
        "Força auxiliar e reserva da Marinha do Brasil.",
        "Força auxiliar e reserva do Exército, organizado com base na hierarquia e na disciplina.",
        "Força auxiliar exclusivamente da Aeronáutica, por força de convênio federal.",
        "Reserva do Exército, mas sem base na hierarquia e disciplina, por se tratar de corporação civil."],
     "resp": 2,
     "exp": "Nos termos do art. 1º da Lei nº 10.230/2015, o CBMMA é força auxiliar e reserva do Exército, organizado com base na hierarquia e disciplina (art. 144, §§5º e 6º, CF) — mesma base constitucional da PMMA."},

    {"id": 792, "corp": "BM", "disc": DISC, "tipo": "MC",
     "enun": "Além de força auxiliar e reserva do Exército, o art. 1º da Lei nº 10.230/2015 estabelece que o CBMMA é também:",
     "alts": [
        "órgão central do Sistema Estadual de Proteção e Defesa Civil.",
        "órgão de assessoramento do Alto Comando da PMMA.",
        "unidade subordinada à Diretoria de Inteligência da PMMA.",
        "órgão vinculado diretamente ao Ministério da Defesa.",
        "integrante do Sistema Único de Segurança Pública, com exclusão da PMMA."],
     "resp": 0,
     "exp": "Correto, nos termos do art. 1º da Lei nº 10.230/2015 — atribuição que não existe na Lei nº 12.896/2026 (PMMA)."},

    {"id": 793, "corp": "BM", "disc": DISC, "tipo": "MC",
     "enun": "No exercício de suas competências relativas à Segurança Contra Incêndio e Pânico, nos termos do art. 2º, III, da Lei nº 10.230/2015, o CBMMA atua:",
     "alts": [
        "no exercício de polícia judiciária, podendo autuar criminalmente os infratores.",
        "apenas em caráter consultivo, sem qualquer poder de polícia.",
        "exclusivamente mediante delegação prévia da Polícia Militar do Maranhão.",
        "no exercício de polícia administrativa, podendo vistoriar, embargar e interditar obras, serviços e locais que não ofereçam condições de segurança.",
        "somente após decisão judicial que autorize a fiscalização."],
     "resp": 3,
     "exp": "Correto, nos termos do art. 2º, III — trata-se de atividade de polícia ADMINISTRATIVA (vistoria, embargo, interdição), e não de polícia judiciária."},

    {"id": 794, "corp": "BM", "disc": DISC, "tipo": "MC",
     "enun": "Assinale a alternativa que apresenta, de forma correta, competências do CBMMA previstas no art. 2º da Lei nº 10.230/2015.",
     "alts": [
        "Exercer o policiamento ostensivo fardado e a polícia judiciária militar.",
        "Controlar e fiscalizar a formação de guarda-vidas em meio aquático, realizar atendimento e transporte pré-hospitalar e proceder à perícia de incêndios.",
        "Processar e julgar infrações penais militares.",
        "Administrar o Departamento Estadual de Trânsito (DETRAN).",
        "Presidir o Conselho Estadual de Segurança Pública."],
     "resp": 1,
     "exp": "Correto, nos termos do art. 2º, IV, VII e VIII, da Lei nº 10.230/2015. As demais opções são atribuições de outros órgãos (PMMA, DETRAN, SSP)."},

    {"id": 795, "corp": "BM", "disc": DISC, "tipo": "MC",
     "enun": "Nos termos do art. 3º da Lei nº 10.230/2015, o CBMMA pode exercer atividades de assessoramento, por meio de seu pessoal, junto a diversos órgãos, inclusive ao(à):",
     "alts": [
        "Organização das Nações Unidas.",
        "Supremo Tribunal Federal.",
        "Parlamento do Mercosul.",
        "Comando do Exército, com exclusão de qualquer órgão legislativo.",
        "Congresso Nacional."],
     "resp": 4,
     "exp": "Correto, nos termos do art. 3º, XIII, da Lei nº 10.230/2015, que inclui o Congresso Nacional no rol de órgãos a que o CBMMA pode prestar assessoramento."},

    {"id": 796, "corp": "BM", "disc": DISC, "tipo": "MC",
     "enun": "O CBMMA integra a estrutura da Secretaria de Estado da Segurança Pública, nos termos do art. 4º da Lei nº 10.230/2015, na condição de:",
     "alts": [
        "órgão autônomo e juridicamente independente da Secretaria de Estado da Segurança Pública.",
        "Unidade Executora Descentralizada, com contabilidade própria e aquisição direta de materiais e equipamentos específicos.",
        "unidade meramente consultiva, sem orçamento ou contabilidade próprios.",
        "autarquia estadual dotada de personalidade jurídica própria.",
        "departamento subordinado diretamente ao Tribunal de Contas do Estado."],
     "resp": 1,
     "exp": "Correto, nos termos do art. 4º, caput e incisos III e IV, da Lei nº 10.230/2015."},

    {"id": 797, "corp": "BM", "disc": DISC, "tipo": "MC",
     "enun": "Acerca da subordinação e do comando do CBMMA, segundo os arts. 5º e 6º da Lei nº 10.230/2015, é correto afirmar que:",
     "alts": [
        "o Comandante-Geral subordina-se ao Governador do Estado, Comandante Superior da Corporação, competindo a ele (Comandante-Geral) a administração e o comando da Corporação.",
        "a administração e o comando competem, em regime de corresponsabilidade, ao Comandante-Geral e ao Secretário de Estado da Segurança Pública.",
        "o CBMMA subordina-se diretamente ao Comandante-Geral da Polícia Militar do Maranhão.",
        "o Governador do Estado não possui qualquer ingerência sobre o comando da Corporação.",
        "o comando da Corporação é exercido em sistema de rodízio pelos Diretores setoriais."],
     "resp": 0,
     "exp": "Correto, nos termos dos arts. 5º e 6º da Lei nº 10.230/2015."},

    {"id": 798, "corp": "BM", "disc": DISC, "tipo": "MC",
     "enun": "A estrutura do CBMMA, segundo o art. 7º da Lei nº 10.230/2015, compreende:",
     "alts": [
        "quatro categorias de órgãos: direção, assessoramento, apoio e execução.",
        "cinco categorias de órgãos: direção, assessoramento, apoio, execução e correição, no mesmo modelo da Lei nº 12.896/2026.",
        "três categorias de órgãos: de direção, de apoio e de execução.",
        "duas categorias de órgãos: direção e execução, sem órgãos de apoio.",
        "seis categorias de órgãos, incluindo correição e controle externo."],
     "resp": 2,
     "exp": "Correto. O art. 7º da Lei nº 10.230/2015 (de 2015) prevê apenas três categorias — diferente das cinco categorias adotadas pela Lei nº 12.896/2026 para a PMMA."},

    {"id": 799, "corp": "BM", "disc": DISC, "tipo": "MC",
     "enun": "Assinale a alternativa que relaciona corretamente as funções às patentes previstas no art. 7º da Lei nº 10.230/2015.",
     "alts": [
        "Diretorias e Comandos Operacionais — Tenente-Coronel; Centros e Batalhões — Major.",
        "Centros e Batalhões de Bombeiros Militar — Coronel; Diretorias — Capitão.",
        "Diretorias — Major; Comandos Operacionais — Capitão.",
        "Diretorias e Comandos Operacionais — Coronel; Centros e Batalhões de Bombeiros Militar — Tenente-Coronel.",
        "Seções e Comandos de Companhia — Tenente-Coronel; Subseções — Major."],
     "resp": 3,
     "exp": "Correto, nos termos dos §§5º e 6º do art. 7º da Lei nº 10.230/2015."},

    {"id": 800, "corp": "BM", "disc": DISC, "tipo": "MC",
     "enun": "Segundo o art. 7º, §8º, da Lei nº 10.230/2015, as funções nas Seções e nos Comandos das Companhias de Bombeiros Militar, exceto as Chefias das Seções do Estado-Maior-Geral, são previstas para o posto de:",
     "alts": ["Major.", "Tenente-Coronel.", "Capitão.", "1º Tenente.", "Subtenente."],
     "resp": 2,
     "exp": "Correto, nos termos do art. 7º, §8º, da Lei nº 10.230/2015."},

    {"id": 801, "corp": "BM", "disc": DISC, "tipo": "MC",
     "enun": "São órgãos de direção do CBMMA, nos termos do art. 8º da Lei nº 10.230/2015, EXCETO:",
     "alts": ["Alto Comando.", "Estado-Maior-Geral.", "Ajudância-Geral.", "Ouvidoria.", "Comando Operacional de Área."],
     "resp": 4,
     "exp": "O Comando Operacional de Área é órgão de EXECUÇÃO (art. 28), e não órgão de direção (art. 8º) do CBMMA."},

    {"id": 802, "corp": "BM", "disc": DISC, "tipo": "MC",
     "enun": "Para o exercício da função de Comandante-Geral do CBMMA, o art. 8º, §1º, da Lei nº 10.230/2015 exige que o oficial seja:",
     "alts": [
        "Coronel do Quadro de Oficiais Combatentes, possuidor do Curso de Formação de Oficial Bombeiro Militar e do Curso Superior de Bombeiro Militar ou equivalente.",
        "Coronel de qualquer Quadro de Oficiais, independentemente de curso de formação específico.",
        "Tenente-Coronel do Quadro de Oficiais Administrativos.",
        "o oficial mais antigo da Corporação, por critério exclusivo de antiguidade, independentemente do Quadro a que pertença.",
        "Coronel do Quadro de Oficiais de Saúde, eleito pelos pares."],
     "resp": 0,
     "exp": "Correto, nos termos do art. 8º, §1º, da Lei nº 10.230/2015."},

    {"id": 803, "corp": "BM", "disc": DISC, "tipo": "MC",
     "enun": "Acerca do Alto Comando do CBMMA, nos termos do art. 9º da Lei nº 10.230/2015, é correto afirmar que:",
     "alts": [
        "é órgão deliberativo, com poder de veto sobre atos do Comandante-Geral.",
        "é órgão consultivo, presidido pelo Comandante-Geral, cujos membros natos são o Comandante Adjunto/Chefe do EMG, o Subchefe do EMG e o Coordenador Estadual de Proteção e Defesa Civil.",
        "tem como membro nato o Diretor de Finanças da Corporação.",
        "é presidido pelo Secretário de Estado da Segurança Pública.",
        "delibera, em caráter vinculante, sobre promoções de oficiais e de praças."],
     "resp": 1,
     "exp": "Correto, nos termos do art. 9º, caput e §1º. O Diretor de Finanças, quando designado, pode no máximo ser membro EFETIVO (§2º), nunca nato."},

    {"id": 804, "corp": "BM", "disc": DISC, "tipo": "MC",
     "enun": "Quanto à chefia do Estado-Maior-Geral do CBMMA, o art. 10 da Lei nº 10.230/2015 estabelece que ela é exercida:",
     "alts": [
        "por Chefe próprio, em caráter exclusivo e incompatível com qualquer outra função.",
        "rotativamente pelos Chefes das Seções do EMG.",
        "pelo Subchefe do EMG, em caráter permanente e exclusivo.",
        "cumulativamente pelo Comandante Adjunto do CBMMA.",
        "pelo Comandante-Geral, cumulativamente com suas demais funções."],
     "resp": 3,
     "exp": "Correto, nos termos do art. 10 da Lei nº 10.230/2015 — não há Chefe do EMG em tempo integral; a função é cumulada pelo Comandante Adjunto."},

    {"id": 805, "corp": "BM", "disc": DISC, "tipo": "MC",
     "enun": "Assinale a alternativa correta quanto às Seções do Estado-Maior-Geral do CBMMA, nos termos do art. 11 da Lei nº 10.230/2015.",
     "alts": [
        "A 2ª Seção (BM/2) trata de legislação técnica, pesquisa técnica, perícias e prevenção.",
        "A 2ª Seção (BM/2) trata de relações públicas e comunicação social.",
        "A 4ª Seção (BM/4) trata de relações públicas, ação comunitária e comunicação social.",
        "A 5ª Seção (BM/5) trata de armamento, material operacional e orçamento.",
        "A 1ª Seção (BM/1) trata de ensino, instrução e doutrina de emprego."],
     "resp": 0,
     "exp": "Correto, nos termos do art. 11, IV, 'b'. As demais alternativas trocam as atribuições entre as seções BM/1, BM/4 e BM/5."},

    {"id": 806, "corp": "BM", "disc": DISC, "tipo": "MC",
     "enun": "São Diretorias do CBMMA, nos termos do art. 13 da Lei nº 10.230/2015, EXCETO:",
     "alts": ["Diretoria de Pessoal.", "Diretoria de Finanças.", "Diretoria de Ensino e Pesquisa.", "Diretoria de Inteligência.", "Diretoria-Geral de Ensino Regular."],
     "resp": 4,
     "exp": "A Diretoria-Geral de Ensino Regular (DGER) é órgão da PMMA, previsto na Lei nº 12.896/2026, e não integra a lista de Diretorias do CBMMA no art. 13 da Lei nº 10.230/2015."},

    {"id": 807, "corp": "BM", "disc": DISC, "tipo": "MC",
     "enun": "A Ajudância-Geral do CBMMA, responsável pela gestão administrativa do Quartel do Comando-Geral, subordina-se, nos termos do art. 14 da Lei nº 10.230/2015:",
     "alts": ["ao Estado-Maior-Geral.", "diretamente ao Governador do Estado.", "ao Comandante Adjunto.", "à Diretoria de Pessoal.", "à Controladoria."],
     "resp": 2,
     "exp": "Correto, nos termos do art. 14 da Lei nº 10.230/2015."},

    {"id": 808, "corp": "BM", "disc": DISC, "tipo": "MC",
     "enun": "Assinale a alternativa correta quanto às atribuições dos órgãos de direção do CBMMA.",
     "alts": [
        "À Controladoria compete receber reclamações e denúncias dos cidadãos.",
        "À Ouvidoria compete receber reclamações e denúncias dos cidadãos, funcionando como canal de atendimento em última instância.",
        "À Ajudância-Geral compete o controle financeiro, contábil e patrimonial da Corporação.",
        "Ao Gabinete do Comandante-Geral compete a condução de processos licitatórios.",
        "À Ouvidoria compete presidir a Comissão de Promoção de Oficiais."],
     "resp": 1,
     "exp": "Correto, nos termos do art. 16 da Lei nº 10.230/2015. O controle financeiro/contábil/patrimonial é da Controladoria (art. 15), e a licitação é conduzida pela Comissão Setorial de Licitação (art. 18)."},

    {"id": 809, "corp": "BM", "disc": DISC, "tipo": "MC",
     "enun": "Acerca dos órgãos de apoio do CBMMA, previstos no art. 21 da Lei nº 10.230/2015, é correto afirmar que:",
     "alts": [
        "o Colégio Militar, órgão de apoio, destina-se ao desenvolvimento educacional dos dependentes de bombeiros militares e também da sociedade civil.",
        "o Colégio Militar atende exclusivamente aos dependentes de bombeiros militares.",
        "a Academia de Bombeiros Militar é classificada como órgão de execução, e não de apoio.",
        "o Centro de Suprimento e Manutenção subordina-se à Diretoria de Inteligência.",
        "a Coordenadoria Médica de Saúde é classificada como órgão de direção."],
     "resp": 0,
     "exp": "Correto, nos termos do art. 27 da Lei nº 10.230/2015 — o Colégio Militar atende tanto dependentes de bombeiros quanto a sociedade civil em geral."},

    {"id": 810, "corp": "BM", "disc": DISC, "tipo": "MC",
     "enun": "A Coordenadoria Médica de Saúde e a Coordenadoria de Serviços Odontológicos do CBMMA subordinam-se, nos termos dos arts. 22 e 23 da Lei nº 10.230/2015:",
     "alts": ["diretamente ao Comandante-Geral.", "à Diretoria de Pessoal.", "ao Estado-Maior-Geral.", "ao Comandante Adjunto da Corporação.", "à Secretaria de Estado da Saúde."],
     "resp": 3,
     "exp": "Correto, nos termos dos arts. 22 e 23 da Lei nº 10.230/2015."},

    {"id": 811, "corp": "BM", "disc": DISC, "tipo": "MC",
     "enun": "São exemplos de unidades especializadas de execução do CBMMA, nos termos do art. 28 da Lei nº 10.230/2015, EXCETO:",
     "alts": ["Batalhão de Bombeiros Marítimo.", "Batalhão de Bombeiros de Emergências Médicas.", "Batalhão de Bombeiros de Busca e Salvamento.", "Batalhão de Bombeiros Ambiental.", "Batalhão de Polícia Militar Rodoviária."],
     "resp": 4,
     "exp": "O Batalhão de Polícia Militar Rodoviária (BPRv) é unidade da PMMA (Lei nº 12.896/2026), e não do CBMMA."},

    {"id": 812, "corp": "BM", "disc": DISC, "tipo": "MC",
     "enun": "Nos termos do art. 28, §1º, da Lei nº 10.230/2015, as Unidades Operacionais em nível de Batalhão de Bombeiros podem ser estruturadas em, no máximo:",
     "alts": ["duas Companhias.", "três Companhias.", "quatro Companhias.", "cinco Companhias.", "número ilimitado de Companhias, a critério do Comandante-Geral."],
     "resp": 1,
     "exp": "Correto, nos termos do art. 28, §1º, da Lei nº 10.230/2015."},

    {"id": 813, "corp": "BM", "disc": DISC, "tipo": "MC",
     "enun": "Os Comandos Operacionais do CBMMA, denominação genérica dada às organizações bombeiro-militares operacionais de mais alto escalão, subordinam-se, nos termos do art. 29 da Lei nº 10.230/2015:",
     "alts": ["ao Comandante Adjunto da Corporação.", "ao Secretário de Estado da Segurança Pública.", "diretamente ao Governador do Estado.", "ao Chefe do Estado-Maior-Geral da Polícia Militar do Maranhão.", "à Coordenadoria Executiva de Defesa Civil."],
     "resp": 0,
     "exp": "Correto, nos termos do art. 29, caput, da Lei nº 10.230/2015."},

    {"id": 814, "corp": "BM", "disc": DISC, "tipo": "MC",
     "enun": "Nos termos do art. 29, §2º, da Lei nº 10.230/2015, NÃO exercem a função de coordenadores regionais de proteção e defesa civil:",
     "alts": [
        "todos os Comandos Operacionais de Área, sem exceção.",
        "apenas o COCB-7 (Pinheiro).",
        "o COCB-1 (São Luís) e o Comando Operacional Especializado (COECB).",
        "nenhum Comando Operacional exerce essa função.",
        "apenas o Comando Operacional Especializado (COECB), com exclusão do COCB-1."],
     "resp": 2,
     "exp": "Correto, nos termos do art. 29, §2º, da Lei nº 10.230/2015, que excepciona o COCB-1 e o COECB dessa função, atribuída aos demais Comandos Operacionais de Área."},

    {"id": 815, "corp": "BM", "disc": DISC, "tipo": "MC",
     "enun": "Quanto à vedação de transferência entre Quadros na estrutura de pessoal do CBMMA, é correto afirmar, nos termos dos arts. 41 e 51 da Lei nº 10.230/2015, que:",
     "alts": [
        "é permitida a transferência entre Quadros de Oficiais, mediante autorização do Comandante-Geral.",
        "é vedada a transferência de militares entre os diferentes Quadros de Oficiais e também entre os diferentes Quadros de Praças Bombeiros Militar.",
        "é permitida a transferência entre Quadros de Praças, desde que observado o interesse do serviço.",
        "a vedação de transferência aplica-se somente aos Quadros de Praças, não aos de Oficiais.",
        "a transferência entre Quadros é automática após dez anos de efetivo serviço."],
     "resp": 1,
     "exp": "Correto, nos termos dos arts. 41 e 51 da Lei nº 10.230/2015, que vedam, sem ressalva, a transferência tanto entre Quadros de Oficiais quanto entre Quadros de Praças."},

    {"id": 816, "corp": "BM", "disc": DISC, "tipo": "MC",
     "enun": "O Quadro de Praças Especiais Bombeiros Militar (QPBME), nos termos do art. 42 da Lei nº 10.230/2015, é constituído por:",
     "alts": [
        "Aspirantes-a-Oficial Bombeiro Militar e Cadetes do Curso de Formação de Oficiais.",
        "apenas Cadetes do Curso de Formação de Oficiais.",
        "Subtenentes e Primeiros-Sargentos.",
        "Alunos-soldados e Alunos-sargentos.",
        "Oficiais do Quadro de Oficiais Especialistas."],
     "resp": 0,
     "exp": "Correto, nos termos do art. 42 da Lei nº 10.230/2015."},

    {"id": 817, "corp": "BM", "disc": DISC, "tipo": "MC",
     "enun": "Quanto à fixação do efetivo do CBMMA, é correto afirmar, nos termos do art. 53 da Lei nº 10.230/2015, que:",
     "alts": [
        "o efetivo é fixado por ato exclusivo do Comandante-Geral, sem necessidade de lei específica.",
        "a distribuição por postos e graduações é de competência do Alto Comando.",
        "o efetivo é fixado em lei específica, mediante proposta do Governador do Estado, ouvido o Comandante-Geral, cabendo ao Secretário de Segurança Pública aprovar a distribuição pormenorizada por postos e graduações.",
        "o efetivo é definido anualmente pela Assembleia Legislativa, sem proposta do Poder Executivo.",
        "não há necessidade de lei específica, bastando ato do Secretário de Segurança Pública."],
     "resp": 2,
     "exp": "Correto, nos termos do art. 53, caput e parágrafo único, da Lei nº 10.230/2015 (efetivo hoje fixado pela Lei nº 7.764/2002)."},

    {"id": 818, "corp": "BM", "disc": DISC, "tipo": "MC",
     "enun": "Nos termos do art. 56 da Lei nº 10.230/2015, na ausência de legislação específica do CBMMA sobre determinada matéria, aplicam-se, no que couber:",
     "alts": [
        "exclusivamente as normas do Exército Brasileiro, sendo vedada a aplicação de normas da Polícia Militar do Maranhão.",
        "as normas pertinentes à Polícia Militar do Maranhão e ao Exército Brasileiro.",
        "as normas da Marinha do Brasil.",
        "nenhuma norma subsidiária, por se tratar de lacuna insuperável.",
        "as normas do Corpo de Bombeiros do Distrito Federal, por delegação federal."],
     "resp": 1,
     "exp": "Correto, nos termos do art. 56 da Lei nº 10.230/2015 — é a regra que liga o CBMMA, de forma subsidiária, ao Estatuto da PM/MA, à Lei nº 12.896/2026 e às normas do Exército."},

    {"id": 819, "corp": "BM", "disc": DISC, "tipo": "MC",
     "enun": "O CBMMA pode firmar convênios com prefeituras municipais para ampliar a articulação operacional, nos termos do art. 57 da Lei nº 10.230/2015, EXCETO quanto a:",
     "alts": ["atividades de apoio logístico comum.", "ações educativas de prevenção de incêndio.", "campanhas de conscientização comunitária.", "atividades militares e técnicas exclusivas da Corporação.", "cessão de instalações físicas para eventos comunitários."],
     "resp": 3,
     "exp": "Correto, nos termos do art. 57 da Lei nº 10.230/2015, que ressalva expressamente as atividades militares e técnicas exclusivas do CBMMA."},

    {"id": 820, "corp": "BM", "disc": DISC, "tipo": "MC",
     "enun": "Acerca do Quadro de Pessoal Civil do CBMMA, é correto afirmar, nos termos do art. 52 da Lei nº 10.230/2015, que:",
     "alts": [
        "é vedada a existência de pessoal civil na estrutura do CBMMA.",
        "é constituído exclusivamente por militares da reserva remunerada.",
        "é constituído por civis cedidos dos Quadros de Servidores do Estado, nomeados ou contratados, para exercerem funções administrativas ou técnicas.",
        "seus integrantes exercem, obrigatoriamente, função de oficial combatente.",
        "é subordinado diretamente ao Alto Comando, com direito a voto em suas deliberações."],
     "resp": 2,
     "exp": "Correto, nos termos do art. 52 da Lei nº 10.230/2015."},

    {"id": 821, "corp": "BM", "disc": DISC, "tipo": "MC",
     "enun": "São Quadros de Oficiais da Ativa do CBMMA, previstos no art. 30 da Lei nº 10.230/2015, EXCETO:",
     "alts": ["Quadro de Oficiais Combatentes Bombeiros Militar (QOC).", "Quadro de Oficiais de Saúde Médicos Bombeiros Militar (QOSM).", "Quadro de Oficiais de Polícia Judiciária Militar (QOPJM).", "Quadro de Oficiais Administrativos Bombeiros Militar (QOA).", "Quadro de Oficiais Técnicos Bombeiros Militar (QOT)."],
     "resp": 2,
     "exp": "Não existe, na Lei nº 10.230/2015, Quadro de Oficiais de Polícia Judiciária Militar (QOPJM) — trata-se de quadro fictício, criado para fins de pegadinha."},

    {"id": 822, "corp": "BM", "disc": DISC, "tipo": "MC",
     "enun": "Em contraste com a Polícia Militar do Maranhão, cuja competência constitucional está centrada na preservação da ordem pública e no policiamento ostensivo, a atuação do CBMMA, segundo a Constituição Federal e a Lei nº 10.230/2015, está centrada:",
     "alts": [
        "na execução de atividades de defesa civil, na prevenção e no combate a incêndios e no socorro público em casos de sinistro.",
        "exclusivamente no policiamento ostensivo de trânsito.",
        "na investigação de infrações penais comuns.",
        "na administração do sistema penitenciário estadual.",
        "na fiscalização de trânsito rodoviário estadual."],
     "resp": 0,
     "exp": "Correto, nos termos do art. 144, §5º, da CF, c/c o art. 2º da Lei nº 10.230/2015."},

    {"id": 823, "corp": "BM", "disc": DISC, "tipo": "MC",
     "enun": "Ao Comandante Adjunto do CBMMA, substituto do Comandante-Geral nos seus afastamentos, ausências e impedimentos legais, compete, nos termos do art. 8º, §§3º e 4º, da Lei nº 10.230/2015, entre outras atribuições:",
     "alts": [
        "a nomeação direta de oficiais para o posto de Coronel.",
        "a presidência exclusiva do Alto Comando, com exclusão do Comandante-Geral.",
        "a aprovação do orçamento estadual de segurança pública.",
        "a representação do Estado perante o Supremo Tribunal Federal.",
        "a aplicação da disciplina, a fiscalização do funcionamento dos órgãos internos e a implementação das políticas definidas pelo Comando-Geral."],
     "resp": 4,
     "exp": "Correto, nos termos do art. 8º, §§3º e 4º, da Lei nº 10.230/2015."},

    {"id": 824, "corp": "BM", "disc": DISC, "tipo": "MC",
     "enun": "Compete ao Centro de Operações e Comunicações do CBMMA, nos termos do art. 24 da Lei nº 10.230/2015:",
     "alts": [
        "o planejamento, a coordenação e a execução das atividades operacionais e de comunicações, bem como pesquisas tecnológicas, perícias e prevenção de incêndios.",
        "a formação e o aperfeiçoamento profissional dos oficiais da Corporação.",
        "a assistência odontológica aos bombeiros militares e seus dependentes.",
        "a administração financeira e orçamentária da Corporação.",
        "a condução de processos licitatórios da Corporação."],
     "resp": 0,
     "exp": "Correto, nos termos do art. 24 da Lei nº 10.230/2015."},

    {"id": 825, "corp": "BM", "disc": DISC, "tipo": "MC",
     "enun": "A Diretoria de Apoio Logístico do CBMMA tem como atribuição, entre outras, nos termos do art. 13 da Lei nº 10.230/2015:",
     "alts": [
        "a formação de oficiais e praças da Corporação.",
        "o suprimento e a manutenção de materiais, equipamentos e viaturas da Corporação.",
        "a perícia de incêndios e o controle de edificações.",
        "a assistência religiosa aos integrantes da Corporação.",
        "a representação institucional perante o Congresso Nacional."],
     "resp": 1,
     "exp": "Correto, nos termos do art. 13, IV, da Lei nº 10.230/2015."},

    {"id": 826, "corp": "BM", "disc": DISC, "tipo": "MC",
     "enun": "Nos termos do art. 55 da Lei nº 10.230/2015, aos militares das Unidades de Bombeiros Militar existentes antes da aprovação dessa lei:",
     "alts": [
        "são extintos os direitos anteriormente adquiridos, em razão da reorganização promovida pela lei.",
        "aplica-se, retroativamente, apenas o novo regime de promoções.",
        "é exigida nova habilitação para a manutenção do posto ou da graduação já ocupados.",
        "ficam assegurados todos os direitos adquiridos.",
        "perdem a precedência hierárquica anteriormente conquistada."],
     "resp": 3,
     "exp": "Correto, nos termos do art. 55 da Lei nº 10.230/2015 — clássica cláusula de proteção ao direito adquirido."},
]

assert len(new_questions) == 36
ids = [q['id'] for q in new_questions]
assert ids == list(range(791, 827)), ids
for q in new_questions:
    assert 0 <= q['resp'] < len(q['alts']), q['id']

# O arquivo original termina em "...}]" sem quebra de linha antes do "]",
# e cada questao adicionada em commits anteriores aparece em sua propria
# linha, no formato CRLF + ", " + json-da-questao. Replicamos exatamente
# esse padrao para nao reformatar o restante do arquivo.
assert raw.endswith(']'), "arquivo nao termina em ']' como esperado"
body = raw[:-1]  # remove o "]" final
for q in new_questions:
    body += '\r\n, ' + json.dumps(q, ensure_ascii=False)
body += ']'

with open('questions.json', 'w', encoding='utf-8', newline='') as f:
    f.write(body)

# valida que o resultado final ainda e um JSON valido e com o total certo
with open('questions.json', encoding='utf-8') as f:
    data = json.load(f)
assert len(data) == len(data_check) + len(new_questions)
print('OK -- total de questoes agora:', len(data))
print('novo total BM:', sum(1 for q in data if q['corp'] == 'BM'))

# Regenera o arquivo final a partir do template, conforme LEIA-ME.txt
with open('questions.json', encoding='utf-8') as f:
    qdata = f.read()
with open('app-template.html', encoding='utf-8') as f:
    html = f.read()
html = html.replace('__QUESTIONS_JSON__', qdata)
with open('estudo-cebraspe-ma.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('estudo-cebraspe-ma.html regenerado com sucesso')
