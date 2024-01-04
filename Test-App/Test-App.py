import requests
import json

shop = "gcm-testing"
password = "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"
Api_version = "2024-01"

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
            "metafield":{
                'namespace': 'FAQpagePython',
                "key": "faq",
                "type": "json_string",
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
            }
    }
    r = requests.post(endpoint, headers=headers, json=metafields_data)
    if r.status_code == 200 :
        return f"successible: {r.json()}"
    else:
        return f"error requests invalid {r.text}"


def createProducts():
    enpoint = f"https://{shop}.myshopify.com/admin/api/{Api_version}/products.json"
    metafield_html = ""
    json_data = {
        'product': {
            'title': 'script inyection',
            'body_html': """
            <strong>Good snowboard!</strong>
            <script type="application/ld+json">
            {
                "@context": "https://schema.org",
                "@type": "Product",
                "name": "Good snowboard!",
                "description": "this is a description of Json-DL from  python code,
                "image": "https://example.com/images/my-product.jpg",
                "sku": "12345",
                "brand": {
                "@type": "Brand",
                "name": "My Brand"
                },
                "offers": {
                "@type": "Offer",
                "price": "19.99",
                "priceCurrency": "USD",
                "availability": "https://schema.org/InStock"
                }
            }
            </script>
            """,
            'vendor': 'Burton',
            'product_type': 'Snowboard',
            'status': 'draft',
        },
    }
    request = requests.post(enpoint, headers=headers, json=json_data)
    if request.status_code == 200:
        return f"successible json data: {request.json()}, status response : {request.status_code} "
    else:
        return f"fail requests json data: {request.text} , status response : {request.status_code}"

def EditProduct(id_product):
    endpoint = f"https://{shop}.myshopify.com/admin/api/{Api_version}/products/{id_product}.json"
    json_data = {
        'product': {
            'id': id_product,
            'title': "change from python code",
            "body_html": """
                <p>this a description from python code, the product of test of continued add a Schema of FAQpage:  </p>
                <script type="application/ld+json">
                    {
                        "@context": "https://schema.org",
                        "@type": "FAQPage",
                        "mainEntity": [
                            {
                                "@type": "Question",
                                "name": "pregunta  1",
                                "acceptedAnswer": {
                                    "@type": "Answer",
                                    "text": "respuesta 1"
                                }
                            }
                        ]
                    }
                </script>
            """
        }
    }

    request = requests.put(endpoint, headers=headers, json=json_data)
    if request.status_code == 200 or 201:
        return f"the requests is successible: {request.json()}, statuscode: {request.status_code}"
    else:
        return f"fail to complate operation: {request.text}, statuscode: {request.status_code}"


def create_metafiels(id_products):
    endpoint = f"https://{shop}.myshopify.com/admin/api/{Api_version}/products/{id_products}/metafields.json"
    metafields_data = {
            "metafield":{
                'namespace': 'FAQpage4',
                "key": "faq",
                "type": "json_string",
                "value":json.dumps({
                    "@context": "https://schema.org",
                    "@type": "FAQPage",
                    "mainEntity": [
                        {
                            "@type": "Question",
                            "name": "pregunta  1 con formato Schema",
                            "acceptedAnswer": {
                                "@type": "Answer",
                                "text": "respuesta 1"
                            }
                        },
                        {
                            "@type": "Question",
                            "name": "pregunta  2 con formato Schema",
                            "acceptedAnswer": {
                                "@type": "Answer",
                                "text": "respuesta 2"
                            }
                        }
                    ]
                })
            }
    }
    r = requests.post(endpoint, headers=headers, json=metafields_data)
    if r.status_code == 200 or 201 :
        return f"successible: {r.json()}, status code : {r.status_code}"
    else:
        return f"error requests invalid {r.text}, status code: {r.status_code}"

if __name__ == "__main__":
    blogs_info = get_infoBlogs()
    id_blogs = blogs_info["blogs"][0]["id"]
    data_blog = modifyBlogs(id_blogs)
    products_get = get_products()
    #for i in range(10):
        #print(products_get['products'][i]['id'])
    id_product = products_get['products'][0]['id']
    #edit_produt = EditProduct(id_product)
    create_mtfiels = create_metafiels(id_product)

    print(id_product)
    print(create_mtfiels)
    #create_product = createProducts()
    #print(create_product)