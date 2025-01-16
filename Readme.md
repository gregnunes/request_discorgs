# Readme 📜

Bem-vindo(a) ao repositório request_discorgs! Aqui você encontrará o passo a passo da construção do projeto e todas as ações importantes necessárias para sua execução.

# Planejamento ☕️

O projeto consiste em capturar dados de artistas e seus álbuns no site Discogs. Inicialmente, foi feito um estudo da estrutura do site para, posteriormente, capturar dados específicos, como artistas, detalhes atribuídos a eles e aos seus álbuns.

# Mapeamento 📜
O primeiro passo foi realizar uma pesquisa para entender a estrutura do site e como funcionam as requisições. Cheguei à página de documentação da API aqui.

Durante o desenvolvimento, encontrei um erro ao tentar utilizar o import requests, que foi corrigido ao atualizar o Python para a versão 3.12. Após estudar as bibliotecas necessárias, percebi a necessidade de gerar um token de acesso no próprio site, após efetuar o login, acessando essa página.

# Construção ✨

O projeto tem como objetivo realizar uma requisição para capturar dados sobre:

Gênero
Nome do artista
Membros do artista
Sites do artista
Ano de lançamento do álbum
Nome do álbum
Gravadora do álbum
Faixas do álbum
Duração de cada faixa
Número da faixa
Estilos do álbum

A requisição é feita de maneira estruturada, com blocos separados para captura e alocação dos dados, organizados por ID's retornados em formato JSON. O uso de time_sleep foi implementado para evitar o erro 429, que ocorre quando as requisições são feitas em um curto período de tempo.

# Execução do final_file.py 🔥

Neste arquivo, a estrutura foi organizada para facilitar a visualização e compreensão do projeto. Os dados são capturados em blocos distintos, com tratamento de erros utilizando try e except para evitar excessos de if/elif/else.

Os artistas estão previamente definidos nas listas, e, para alterá-los, será necessário modificar as listas e as referências no código. Para melhor dinâmica, os 10 artistas foram divididos em 3 listas de execução.

**Para executar o código:**

Abra o arquivo na sua IDE ou execute o código diretamente no terminal com o comando:

**python final_file.py**

O script retornará um arquivo JSON com todos os dados solicitados.
Caso ocorram erros relacionados aos imports, verifique se as bibliotecas estão instaladas. Se necessário, instale-as com o comando:
**pip3 install requests**

# Execução do test-argparse.py ✨

Neste arquivo, a estrutura é semelhante ao código anterior, mas foi implementada a utilização da biblioteca argparse. O código agora permite que você passe parâmetros diretamente para a API Discogs, utilizando a URL https://api.discogs.com/database/search.

**Para executar o código:**
Execute o script passando o nome de um ou mais artistas como argumento:

*python test-argparse.py "Nirvana"*, (ou qualquer artista de sua preferência).

O código retornará um arquivo JSON com os dados dos artistas consultados, permitindo que a API faça a busca com base nos parâmetros fornecidos.

# Importante: Verifique se as bibliotecas necessárias estão instaladas ⚠️ 

Nesse projeto não foi necessária a utilização do **requirements.txt**, apenas com as lib obtive um bom resultado junto a API.



