import csv
from BTrees.OOBTree import OOBTree
from timeit import timeit


def load_data(file_path):
    data = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['ID'] = int(row['ID'])
            row['Price'] = float(row['Price'])
            data.append(row)
    return data


def add_item_to_tree(tree, item):
    tree[item['ID']] = {'Name': item['Name'], 'Category': item['Category'], 'Price': item['Price']}


def add_item_to_dict(dictionary, item):
    dictionary[item['ID']] = {'Name': item['Name'], 'Category': item['Category'], 'Price': item['Price']}


def range_query_tree(tree, min_price, max_price):
    return [item for _, item in tree.items() if min_price <= item['Price'] <= max_price]


def range_query_dict(dictionary, min_price, max_price):
    return [item for item in dictionary.values() if min_price <= item['Price'] <= max_price]


def analyze_performance(data, min_price, max_price):
    tree = OOBTree()
    dictionary = {}

    for item in data:
        add_item_to_tree(tree, item)
        add_item_to_dict(dictionary, item)

    tree_time = timeit(lambda: range_query_tree(tree, min_price, max_price), number=100)
    dict_time = timeit(lambda: range_query_dict(dictionary, min_price, max_price), number=100)

    print(f"OOBTree total time for 100 range queries: {tree_time:.4f} seconds")
    print(f"Dict total time for 100 range queries: {dict_time:.4f} seconds")

if __name__ == "__main__":
    while True:
        try:
            min_price = float(input("Enter min price: "))
            max_price = float(input("Enter max price: "))
            if min_price > max_price:
                print("Min price should be less than max price")
                continue
            else:
                break
        except ValueError:
            print("Please enter a valid number")

    file_path = "generated_items_data.csv"
    data = load_data(file_path)
    analyze_performance(data, min_price, max_price)
