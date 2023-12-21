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
def put_funcion_products(producto_id):
    endpoint = f'https://{shop}.myshopify.com/admin/api/{Api_version}/products/{producto_id}.json'
    json_data = {
        'product': {
            'title': "ttest nombre"
            #'status': status
        },
    }

    pr_response = requests.put(endpoint, headers=headers, json=json_data)

    return pr_response.json(), pr_response.status_code


#fuction to get id of blogs 
def get_infoBlogs():
    endpoint = f'https://{shop}.myshopify.com/admin/api/{Api_version}/blogs.json'
    response = requests.get(endpoint, headers=headers)

    return response.json()
#fuction to modify metafields of blogs of shopify
def modifyBlogs(id_blog):
    endpoint = f'https://{shop}.myshopify.com/admin/api/{Api_version}/blogs/{id_blog}/metafields.json'
    metafields_data = {
        "blog": {
            "id": id_blog,
            "metafields": [
                {
                    "key": "faq",
                    "value": json.dumps({
                        "questions": [
                            {
                                "question": "¿Cuál es la pregunta 1?",
                                "answer": "Esta es la respuesta a la pregunta 1."
                            },
                            {
                                "question": "¿Cuál es la pregunta 2?",
                                "answer": "Esta es la respuesta a la pregunta 2."
                            }
                        ]
                    }),
                    "type": "json_string",
                    "namespace": "faq"
                }
            ]
        }
    }
    r = requests.put(endpoint, headers=headers, json=metafields_data)
    if r.status_code == 200 :
        return f"successible: {r.json()}"
    else:
        #messege = f"requests invalid {r.json()}"
        messege = r.text
        return messege

if __name__ == "__main__":
    blogs_info = get_infoBlogs()
    id_blogs = blogs_info["blogs"][0]["id"]
    data_blog = modifyBlogs(id_blogs)

    print(data_blog)
    #productos = get_products()
    #print(productos)
    #id_productos = productos['products'][0]['id']
    #print(id_productos)
    #status = "draft"
    #Put_products, status_code = put_funcion_products(id_productos)
    #print(Put_products, status_code)