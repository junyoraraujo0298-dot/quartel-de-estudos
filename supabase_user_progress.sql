-- ======================================================================
-- Tabela de progresso do usuario (historico de respostas), pra
-- sincronizar entre aparelhos usando um "codigo de perfil" simples.
--
-- IMPORTANTE (leia antes de rodar): como o app nao tem sistema de
-- login, esta tabela usa leitura E escrita publicas (qualquer um com a
-- URL + chave publishable do seu projeto Supabase, mais o codigo de
-- perfil certo, consegue ler ou sobrescrever aquele historico). Isso e
-- aceitavel pra um historico de respostas de estudo (nao e dado
-- sensivel), mas NAO e um sistema de login seguro -- nao reutilize
-- senhas nem informacoes sensiveis como "codigo de perfil".
--
-- Cole este arquivo no SQL Editor do Supabase e rode uma vez.
-- ======================================================================

create table if not exists user_progress (
  profile_id text primary key,
  history jsonb not null default '[]'::jsonb,
  updated_at timestamptz not null default now()
);

alter table user_progress enable row level security;

drop policy if exists "public read user_progress" on user_progress;
create policy "public read user_progress" on user_progress for select using (true);

drop policy if exists "public insert user_progress" on user_progress;
create policy "public insert user_progress" on user_progress for insert with check (true);

drop policy if exists "public update user_progress" on user_progress;
create policy "public update user_progress" on user_progress for update using (true) with check (true);

-- Conferencia rapida (rode separadamente, depois):
-- select * from user_progress;
