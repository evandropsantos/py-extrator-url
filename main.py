from extrator_url import ExtratorURL


VALOR_DOLAR = 5.50  # 1 dólar = 5.50 reais
URL = f"bytebank.com/cambio? \
        quantidade=100& \
        moedaOrigem=real \
        &moedaDestino={VALOR_DOLAR}"

extrator_url = ExtratorURL(URL)

moeda_origem = extrator_url.get_valor_parametro("moedaOrigem")
moeda_destino = extrator_url.get_valor_parametro("moedaDestino")
quantidade = extrator_url.get_valor_parametro("quantidade")

print(moeda_origem)
print(moeda_destino)
print(quantidade)
