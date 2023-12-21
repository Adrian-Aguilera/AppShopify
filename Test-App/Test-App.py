import requests
import json

shop = "gcm-testing"
password = "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"
Api_version = "2023-10"

headers = {
    'Content-Type': 'application/json',
    'X-Shopify-Access-Token': f'{password}',
}
#get products info of the API Shopify
def get_products():
    endpoint = f'https://{shop}.myshopify.com/admin/api/{Api_version}/products.json'
    response = requests.get(endpoint, headers=headers)
    return response.json()

#PUT funcion
def put_funcion(producto_id):
    endpoint = f'https://{shop}.myshopify.com/admin/api/{Api_version}/products/{producto_id}.json'
    json_data = {
        'product': {
            'title': "ttest nombre"
            #'status': status
        },
    }

    pr_response = requests.put(endpoint, headers=headers, json=json_data)

    return pr_response.json(), pr_response.status_code

if __name__ == "__main__":
    productos = get_products()
    with open("test.json", "w") as file:
        json.dump(productos, file)

    print(productos)
    id_productos = productos['products'][0]['id']
    #print(id_productos)
    status = "draft"
    Put_products, status_code = put_funcion(id_productos)
    #print(Put_products, status_code)