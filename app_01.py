import requests



def fetch_page(url):
     response = requests.get(url)
     return response.text

if __name__ == "__main__":
     url = "https://www.mercadolivre.com.br/apple-iphone-16-128-gb-preto-distribuidor-autorizado/p/MLB1040287808#polycard_client=search-nordic&searchVariation=MLB1040287808&wid=MLB5120546360&position=1&search_layout=stack&type=product&tracking_id=ed6d4694-f7db-4933-8647-96b2bda1885b&sid=search"
     page_content = fetch_page()
     print(page_content)