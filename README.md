# py-extrator-url

- [Expressões Regulares HOWTO](https://docs.python.org/pt-br/3/howto/regex.html#regex-howto)
- [Python: Qual a diferença entre == e is?](https://www.alura.com.br/artigos/qual-a-diferenca-entre-e-is-no-python?_gl=1*l8zkxd*_ga*Nzc3MzI5MjEuMTY5NTA2NDY2Ng..*_ga_1EPWSW3PCS*MTY5ODQ1NTk4MS4xMTkuMS4xNjk4NDU3MDA5LjAuMC4w*_fplc*VW9hbEFpS0lmM0lvRVhOM01QbVNFWktSbWt6b0xSUE9GenF3T2hQN1RYQUtjUyUyRm9FdEElMkJBZFRrYyUyRjAxcVk2OSUyQmM0aSUyRlh4biUyRkNObyUyQlkzeldReHNNRW1TNVBKdDVqTGRkNm9xWG1lRkdwbDU5V2N2czN2dGlsZFFzMkN6OUElM0QlM0Q.)

## O método dir
O método dir(objeto) é um método embutido (built-in) que retorna uma lista de strings com todos os métodos e atributos do objeto passado.

Por exemplo, se fizermos dir(str) temos o seguinte retorno (simplifiquei devido a grande quantidade de métodos e atributos da classe str):

```python
    dir(str)
    # [..., ‘__len__’, ... , ‘strip’, … ‘]
```
Inclusive, se você souber o nome do método que está procurando, pode verificar se ele está nessa lista utilizando o operador in:

```python
    ‘__len__’ in dir(str)  # Verifica se o método __len__ existe na classe str
    # True
```