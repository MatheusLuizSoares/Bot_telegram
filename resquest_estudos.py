import requests

#resp=requests.get("https://viacep.com.br/ws/01001000/json/")

#requests.post()
#print(resp.text)
#d=resp.json()
#print(d)


def get_info_cep(cep):
  url_base=f'https://viacep.com.br/ws/{cep}/json/'
  r=requests.get(url_base)
  return r.json()

d=get_info_cep('01001000')
print(d)