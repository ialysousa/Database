# Database

## Estoque Residência :card_index_dividers: 

## Repositório para o exercício sobre estoque em Python.

### :white_large_square: Descrição
  :red_circle: Construa o estoque da residência, nesse estoque existem os itens e a equipe de funcionários.

  :red_circle: Os itens têm: id, nome, tipo, quantidade total, quantidade em estoque, quantidade emprestada.

  :red_circle: Os funcionários tem: id, nome, cargo, itens emprestados.

 :red_circle: No sistema, deve ser possível  fazer cadastro de itens e de funcionários.

  :red_circle: No sistema, deve ser possível fazer pesquisa de itens e funcionários por id. e retorne os dados do item ou do funcionário. 

 :red_circle: No sistema deve ser possível mostrar todos os itens e os funcionários cadastrados no sistema em ordem alfabética. 

  :red_circle: No sistema deve ser possível atualizar itens e funcionários. 

 :red_circle: No sistema, deve ser possível fazer um empréstimo de itens, quando um item for emprestado, a quantidade de itens em estoque diminui e aumenta o valor de itens emprestados, além de que, o nome do item tem que ser adicionado em itens emprestados ao cadastro de funcionários. 

 :red_circle: No sistema, deve ser possível fazer a devolução de itens, quando a devolução acontecer, a quantidade de itens emprestados diminui e a quantidade de itens em estoque aumenta, além disso, o item tem que ser tirado do funcionário ao qual foi devolvido. 

 :red_circle: No sistema, deve ser possível fazer a exclusão de itens e funcionários, mas, para apagar itens e funcionários é necessário que os funcionários não tenham nenhum item emprestado e os itens não tenham nenhuma quantidade fora do estoque. 


 ### :white_large_square: Casos de Testes

:memo: Adicione 10 funcionários

:memo: Adicione 10 itens com 5 unidades(adicione um dos itens com apenas 3 unidades)

:memo: Atualize o nome de 2 funcionários e o cargo de 1

:memo: Atualize o nome de 5 itens, a quantidade total de 2 e o tipo de 1

:memo: Liste todos os funcionários

:memo: Liste todos os itens

:memo: Pesquise 3 itens pelo id

:memo: Pesquise 3 funcionários por id

:memo: Empreste 3 itens a um funcionário

:memo: Empreste 5 itens a um funcionário

:memo: Emprete 2 itens a um funcionário

:memo: Devolva 2 itens de cada um dos funcionários

:memo: Tente devolver um item que não está com o funcionário

:memo: Tente emprestar um item que não tem estoque

:memo: Tente excluir um funcionário

:memo: Excluir um item

:memo: Tente excluir um funcionário que está com algum item emprestado

:memo: Tente excluir um item que tem alguma quantidade emprestada. 

