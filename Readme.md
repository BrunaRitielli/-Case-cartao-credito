#  Case – Análise de Parcelas de Cartão de Crédito com Pandas

Este projeto demonstra como transformar compras parceladas de cartão de crédito em um cronograma completo de parcelas, com datas de vencimento e valores distribuídos mês a mês por cliente.

##  Objetivo do projeto

Responder à pergunta:

> **Como determinar as datas e os valores de cada parcela de compras no cartão de crédito, organizando tudo por cliente e por mês?**


##  O que o código faz

1. Lê a base de compras parceladas.  
2. Converte a data da compra para formato datetime.  
3. Calcula o valor individual de cada parcela.  
4. Cria uma lista com o número de parcelas.  
5. Usa `explode` para transformar cada parcela em uma linha.  
6. Calcula a data de cada parcela somando meses.  
7. Agrupa por cliente e mês e soma o valor de parcelas.  
8. Gera a tabela final de valores a pagar por cliente.

## 🛠 Tecnologias utilizadas

- Python 3  
- Pandas  
- VS Code ou Google Colab  