# -*- coding: utf-8 -*-
# Gera um arquivo SQL (supabase_migration.sql) com:
#   1) criacao das tabelas (questions, content_decks, content_items) + RLS
#      de leitura publica;
#   2) INSERT de todo o conteudo hoje embutido no app: as 964 questoes
#      (questions.json) e os "decks" de leitura (leis, teoria, flashcards,
#      historia do MA, comparativo entre leis), extraidos diretamente do
#      app-template.html.
#
# O arquivo gerado deve ser colado inteiro no SQL Editor do Supabase e
# executado uma vez. Nao precisa de credenciais do Supabase para RODAR
# este script Python -- ele so LE os arquivos locais e ESCREVE o .sql;
# quem efetivamente cria as tabelas e insere os dados e voce, rodando o
# SQL gerado no painel do seu projeto.
import json
import re

with open('questions.json', encoding='utf-8') as f:
    questions = json.load(f)

with open('app-template.html', encoding='utf-8') as f:
    html = f.read()

decoder = json.JSONDecoder()

def extract_const_array(name):
    m = re.search(r'const %s\s*=\s*' % re.escape(name), html)
    if not m:
        raise SystemExit(f"const {name} nao encontrada em app-template.html")
    start = html.index('[', m.end())
    arr, _end = decoder.raw_decode(html, start)
    return arr

def extract_law_comparison():
    # LAW_COMPARISON usa chaves JS sem aspas (tema:, l6513:, ...), nao e JSON
    # valido -- extrai via regex em vez de json.loads.
    m = re.search(r'const LAW_COMPARISON\s*=\s*\[', html)
    if not m:
        raise SystemExit("const LAW_COMPARISON nao encontrada")
    start = m.end() - 1
    depth = 0
    end = None
    for i in range(start, len(html)):
        if html[i] == '[':
            depth += 1
        elif html[i] == ']':
            depth -= 1
            if depth == 0:
                end = i
                break
    block = html[start:end + 1]
    pattern = re.compile(
        r'tema:\s*"((?:[^"\\]|\\.)*)"\s*,\s*'
        r'l6513:\s*"((?:[^"\\]|\\.)*)"\s*,\s*'
        r'l12896:\s*"((?:[^"\\]|\\.)*)"\s*,\s*'
        r'l14751:\s*"((?:[^"\\]|\\.)*)"', re.S)
    rows = []
    for tema, l6513, l12896, l14751 in pattern.findall(block):
        unesc = lambda s: s.replace('\\"', '"').replace('\\n', '\n')
        rows.append({"tema": unesc(tema), "l6513": unesc(l6513), "l12896": unesc(l12896),
                     "l14751": unesc(l14751)})
    return rows


LAW_6513 = extract_const_array('LAW_6513')
LEI_12896 = extract_const_array('LEI_12896')
LAW_14751 = extract_const_array('LAW_14751')
LAW_10230 = extract_const_array('LAW_10230')
LAW_11390 = extract_const_array('LAW_11390')
TEORIA_PORTUGUES = extract_const_array('TEORIA_PORTUGUES')
TEORIA_GEOGRAFIA_MA = extract_const_array('TEORIA_GEOGRAFIA_MA')
TEORIA_INGLES = extract_const_array('TEORIA_INGLES')
TEORIA_RACIOCINIO_LOGICO = extract_const_array('TEORIA_RACIOCINIO_LOGICO')
TEORIA_PRIMEIROS_SOCORROS = extract_const_array('TEORIA_PRIMEIROS_SOCORROS')
TEORIA_COMBATE_INCENDIO = extract_const_array('TEORIA_COMBATE_INCENDIO')
CRONOGRAMA_PCPE = extract_const_array('CRONOGRAMA_PCPE')
LAW_PE_CONSTITUICAO = extract_const_array('LAW_PE_CONSTITUICAO')
LAW_PE_ESTATUTO_POLICIAL = extract_const_array('LAW_PE_ESTATUTO_POLICIAL')
PROGRAMA_PCPE_AGENTE = extract_const_array('PROGRAMA_PCPE_AGENTE')
LAW_COMPARISON = extract_law_comparison()
FLASHCARDS = extract_const_array('FLASHCARDS')
HIST_MA_LESSON = extract_const_array('HIST_MA_LESSON')
HIST_MA_CARDS = extract_const_array('HIST_MA_CARDS')

print('Itens extraidos:')
for name, arr in [('LAW_6513', LAW_6513), ('LEI_12896', LEI_12896), ('LAW_14751', LAW_14751),
                   ('LAW_10230', LAW_10230), ('LAW_11390', LAW_11390),
                   ('TEORIA_PORTUGUES', TEORIA_PORTUGUES),
                   ('TEORIA_GEOGRAFIA_MA', TEORIA_GEOGRAFIA_MA), ('TEORIA_INGLES', TEORIA_INGLES),
                   ('TEORIA_RACIOCINIO_LOGICO', TEORIA_RACIOCINIO_LOGICO),
                   ('TEORIA_PRIMEIROS_SOCORROS', TEORIA_PRIMEIROS_SOCORROS),
                   ('TEORIA_COMBATE_INCENDIO', TEORIA_COMBATE_INCENDIO),
                   ('CRONOGRAMA_PCPE', CRONOGRAMA_PCPE),
                   ('LAW_PE_CONSTITUICAO', LAW_PE_CONSTITUICAO),
                   ('LAW_PE_ESTATUTO_POLICIAL', LAW_PE_ESTATUTO_POLICIAL),
                   ('PROGRAMA_PCPE_AGENTE', PROGRAMA_PCPE_AGENTE),
                   ('LAW_COMPARISON', LAW_COMPARISON), ('FLASHCARDS', FLASHCARDS),
                   ('HIST_MA_LESSON', HIST_MA_LESSON), ('HIST_MA_CARDS', HIST_MA_CARDS)]:
    print(f'  {name}: {len(arr)} itens')

# deck_key -> (label, category, mode_ou_None, lista_de_itens)
DECKS = {
    'law_6513':       ("Lei 6.513/95 (Estatuto — PM e BM)", 'lei', None, LAW_6513),
    'law_12896':      ("Lei 12.896/2026 (PMMA)", 'lei', None, LEI_12896),
    'law_10230':      ("Lei 10.230/2015 (CBMMA)", 'lei', None, LAW_10230),
    'law_14751':      ("Lei 14.751/2023 (Nacional — PM e BM)", 'lei', None, LAW_14751),
    'law_11390':      ("Lei 11.390/2020 (Segurança Contra Incêndio)", 'lei', None, LAW_11390),
    'law_comparativo':("Comparativo das 3 Leis (PMMA)", 'comparativo', None, LAW_COMPARISON),
    'teoria_portugues':("Língua Portuguesa", 'teoria', None, TEORIA_PORTUGUES),
    'teoria_geografia':("Geografia do Maranhão", 'teoria', None, TEORIA_GEOGRAFIA_MA),
    'teoria_ingles':  ("Inglês", 'teoria', None, TEORIA_INGLES),
    'teoria_logica':  ("Raciocínio Lógico", 'teoria', None, TEORIA_RACIOCINIO_LOGICO),
    'teoria_socorros':("Primeiros Socorros (BMMA)", 'teoria', None, TEORIA_PRIMEIROS_SOCORROS),
    'teoria_incendio':("Combate a Incêndio (BMMA)", 'teoria', None, TEORIA_COMBATE_INCENDIO),
    'teoria_historia':("História do Maranhão", 'teoria', None, HIST_MA_LESSON),
    'estrategia_cronograma_pcpe': ("Edital e Cronograma — PC-PE (Pernambuco), Agente de Polícia", 'estrategia', None, CRONOGRAMA_PCPE),
    'estrategia_constituicao_pe': ("Constituição de PE (trechos) — Segurança Pública e Administração", 'estrategia', None, LAW_PE_CONSTITUICAO),
    'estrategia_estatuto_policial_pe': ("Estatuto do Policial Civil de PE (Lei 6.425/1972)", 'estrategia', None, LAW_PE_ESTATUTO_POLICIAL),
    'estrategia_programa_pcpe': ("Conteúdo Programático Oficial — PC-PE Agente de Polícia (Edital 2026)", 'estrategia', None, PROGRAMA_PCPE_AGENTE),
    'flash_6513':     ("Lei 6.513/95 (pergunta e resposta)", 'flashcard', 'quiz', FLASHCARDS),
    'flash_historia': ("História do Maranhão (leitura)", 'flashcard', 'read', HIST_MA_CARDS),
}


def sql_str(s):
    """Escapa uma string para um literal SQL 'texto'."""
    return "'" + s.replace("'", "''") + "'"


def sql_str_or_null(s):
    if s is None:
        return 'NULL'
    return sql_str(s)


def sql_jsonb(obj):
    return sql_str(json.dumps(obj, ensure_ascii=False)) + '::jsonb'


def sql_bool_or_null(b):
    if b is None:
        return 'NULL'
    return 'TRUE' if b else 'FALSE'


def sql_int_or_null(i):
    if i is None:
        return 'NULL'
    return str(i)


out = []
out.append('-- ======================================================================')
out.append('-- Migracao do Quartel de Estudos para o Supabase')
out.append('-- Gerado automaticamente por gen13_build_supabase_migration.py')
out.append('-- Cole este arquivo inteiro no SQL Editor do Supabase e rode uma vez.')
out.append('-- ======================================================================')
out.append('')
out.append('begin;')
out.append('')

# -------------------- SCHEMA --------------------
out.append('-- ---------- schema ----------')
out.append('''
create table if not exists questions (
  id integer primary key,
  corp text not null,
  disc text not null,
  assunto text not null,
  tipo text not null check (tipo in ('CE','MC')),
  enun text not null,
  resp_bool boolean,
  resp_idx integer,
  alts jsonb,
  exp text not null
);
alter table questions enable row level security;
drop policy if exists "public read questions" on questions;
create policy "public read questions" on questions for select using (true);

create table if not exists content_decks (
  deck_key text primary key,
  label text not null,
  category text not null,
  mode text
);
alter table content_decks enable row level security;
drop policy if exists "public read content_decks" on content_decks;
create policy "public read content_decks" on content_decks for select using (true);

create table if not exists content_items (
  id bigserial primary key,
  deck_key text not null references content_decks(deck_key) on delete cascade,
  order_index integer not null,
  data jsonb not null,
  unique (deck_key, order_index)
);
alter table content_items enable row level security;
drop policy if exists "public read content_items" on content_items;
create policy "public read content_items" on content_items for select using (true);
create index if not exists content_items_deck_idx on content_items(deck_key, order_index);
'''.strip())
out.append('')

# -------------------- DATA: questions --------------------
out.append('-- ---------- dados: questions (%d linhas) ----------' % len(questions))
out.append('truncate table questions restart identity cascade;')
BATCH = 200
for start in range(0, len(questions), BATCH):
    chunk = questions[start:start + BATCH]
    values = []
    for q in chunk:
        if q['tipo'] == 'CE':
            resp_bool = sql_bool_or_null(q['resp'])
            resp_idx = 'NULL'
            alts = 'NULL'
        else:
            resp_bool = 'NULL'
            resp_idx = sql_int_or_null(q['resp'])
            alts = sql_jsonb(q['alts'])
        row = (f"({q['id']}, {sql_str(q['corp'])}, {sql_str(q['disc'])}, {sql_str(q['assunto'])}, "
               f"{sql_str(q['tipo'])}, {sql_str(q['enun'])}, {resp_bool}, {resp_idx}, {alts}, "
               f"{sql_str(q['exp'])})")
        values.append(row)
    out.append('insert into questions (id, corp, disc, assunto, tipo, enun, resp_bool, resp_idx, alts, exp) values')
    out.append(',\n'.join(values) + ';')
out.append('')

# -------------------- DATA: content_decks + content_items --------------------
out.append('-- ---------- dados: content_decks + content_items ----------')
out.append('truncate table content_decks restart identity cascade;')
out.append('')
deck_rows = []
for key, (label, category, mode, _items) in DECKS.items():
    deck_rows.append(f"({sql_str(key)}, {sql_str(label)}, {sql_str(category)}, {sql_str_or_null(mode)})")
out.append('insert into content_decks (deck_key, label, category, mode) values')
out.append(',\n'.join(deck_rows) + ';')
out.append('')

for key, (_label, _category, _mode, items) in DECKS.items():
    if not items:
        continue
    out.append(f'-- deck: {key} ({len(items)} itens)')
    for start in range(0, len(items), BATCH):
        chunk = items[start:start + BATCH]
        values = []
        for i, item in enumerate(chunk, start=start):
            values.append(f"({sql_str(key)}, {i}, {sql_jsonb(item)})")
        out.append('insert into content_items (deck_key, order_index, data) values')
        out.append(',\n'.join(values) + ';')
    out.append('')

out.append('commit;')
out.append('')
out.append('-- Conferencia rapida (rode depois do commit, separadamente):')
out.append('-- select count(*) from questions;')
out.append('-- select deck_key, count(*) from content_items group by deck_key order by deck_key;')

sql_text = '\n'.join(out)
with open('supabase_migration.sql', 'w', encoding='utf-8') as f:
    f.write(sql_text)

print()
print('OK -- supabase_migration.sql gerado, tamanho:', len(sql_text), 'caracteres')
