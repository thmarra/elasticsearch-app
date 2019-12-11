# Testando o ElasticSearch

## Objetivo e regras negociais:
Para testar o comportamento do elasticsearch foi criada uma aplicação que visa salvar arquivos, obedecendo as seguintes regras negociais:
1. Cada arquivo possui um único dono;
2. Cada arquivo precisa estar dentro de um diretório;
3. Os diretórios podem mudar de donos;
4. Os donos podem possuir mais de um diretório;

**Donos:**
Possuem ID e NOME

**Diretórios:**
Possuem ID, NOME e um DONO_ID

**Arquivos:**
Possuem um ID, NOME, CONTEÚDO, TAGS e DIRETORIO_ID

## Endpoints:
- Lista com pesquisa de arquivos
- Lista de diretórios
- Alterar dono do diretório
- Excluir arquivo
- Alterar arquivo (tags)

## Indexação dos dados:
