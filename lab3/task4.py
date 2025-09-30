import json

def ProductDataTransformer():
    
    product_names_input = input("Enter product names (comma-separated): ")
    product_names = []
    for name in product_names_input.split(','):
        clean_name = name.strip()
        product_names.append(clean_name)

    
    product_prices_input = input("Enter product prices (comma-separated): ")
    product_prices = []
    for price in product_prices_input.split(','):
        clean_price = price.strip()
        product_prices.append(float(clean_price))

    product_pairs = list(zip(product_names, product_prices))

    valid_pairs = list(filter(lambda pair: pair[1] > 0, product_pairs))
    print(f"Valid pairs : {valid_pairs}")

    
    def transform_to_dict(pair):
        return {
            "product": pair[0], 
            "price": pair[1], 
            "discounted": round(pair[1] * 0.9, 2)
        }
    
    product_dictionaries = list(map(transform_to_dict, valid_pairs))

    with open("products.json", "w") as file:
        json.dump(product_dictionaries, file, indent=2)

    print("first 5 results : ")
    for i in range(min(5, len(product_dictionaries))):
        product = product_dictionaries[i]
        print(f"{product['product']} - price: ${product['price']}, discounted: ${product['discounted']}")