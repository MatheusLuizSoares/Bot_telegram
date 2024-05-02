import requests
def get_ticks(moeda="BTC", metodo="ticker"):
  url_base=f"https://www.mercadobitcoin.net/api/{moeda}/{metodo}/"
  r=requests.get(url_base)
  return r.json()

d=get_ticks("ETH")
print(d)
