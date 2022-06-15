import requests

response = requests.get('https://viacep.com.br/ws/01001000/json/')
print(response.status_code)
print(response.json())
dados_cep = response.json()
print(dados_cep['logradouro'])

def retorna_response(url):
    response = requests.get(url)
    return response.text

if __name__ == '__main__':
    response = retorna_response('https://globallabs.academy/')
    print(response)