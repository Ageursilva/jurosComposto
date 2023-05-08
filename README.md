

# Projeto de Estudo - Cálculo de Juros Compostos

Este é um projeto simples de estudo em Python que tem como objetivo calcular o valor final de um investimento com juros compostos, a partir do capital inicial, taxa de juros anual e tempo de investimento em meses.

## Como Funciona?

O programa solicita ao usuário que informe o valor do capital inicial, a taxa de juros anual em porcentagem e o tempo de investimento em meses. Em seguida, é realizada a conversão da taxa de juros para o formato decimal e do tempo para anos. 

Com esses valores em mãos, é possível calcular o valor final do investimento utilizando a fórmula dos juros compostos, que é dada por:

``` python
valor_final = capital * (1 + juros) ** tempo
```

O programa retorna o valor final do investimento e o valor dos juros do rendimento.

## Como Utilizar?

Para utilizar este projeto, é necessário ter o Python instalado na máquina. Após isso, basta copiar o código-fonte para um arquivo com extensão ".py" e executá-lo em um terminal ou IDE Python.

## Exemplo de Utilização

``` python
Qual o capital de Investimento? 10000
Qual a taxa de juros anual em porcentagem (%) ? 10
Quantos meses sera o investimento? 12
O montante final será de : R$11047.02
O juros do rendimento foram de : R$1047.02
```

## Conclusão

Este projeto é um exemplo simples de como é possível utilizar a linguagem Python para realizar cálculos financeiros. É importante lembrar que, na prática, existem outros fatores que podem influenciar o resultado de um investimento, como impostos, inflação e variações na taxa de juros.
