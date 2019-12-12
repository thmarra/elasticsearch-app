# Testando o ElasticSearch

## Objetivo e regras negociais:
Para testar o comportamento do elasticsearch foi criada uma aplicação que visa salvar arquivos, obedecendo as seguintes regras negociais:
1. A aplicação deve receber e indexar arquivos PDF;
2. Cada arquivo precisa necessariamente de uma categoria e um autor;
3. As categorias possuem um ou mais autores;
4. Cada autor pertence a apenas uma categoria;
5. Os autores podem mudar de categoria;
6. Os arquivos não podem mudar de autor;

### Modelo normalizado:
Um dos objetivos do teste é descobrir a melhor forma de importar para o ElasticSearch dados que estão normalizados no banco relacional em uma estrutura similar a seguinte:

![Modelo normalizado](https://github.com/thmarra/elasticsearch-app/blob/master/modelo_normalizado.png)

## Endpoints:
- Lista com pesquisa de arquivos
- Alterar arquivo (tags)
- Alterar categoria

## Indexação dos dados:
A categoria será um campo obrigatório em todas as pesquisas. É preciso enviar um ID para iniciar a pesquisa.

Os demais campos a serem pesquisados são:
- Autor
- Tags
- Data de criação
- Data de envio
- Conteúdo do arquivo