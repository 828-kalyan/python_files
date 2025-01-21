dict = {
    "red tshirt": "cloth",
    "trending tshirt": "cloth",
    "branded tshirt": "cloth",
    "cotton tshirt": "cloth",
    "Dr. set": "toy",
    "kitchen set": "toy",
    "teddy": "toy",
    "unicorn": "toy",
    "fishing": "toy",
    "chair": "furniture",
    "table": "furniture",
    "sofa": "furniture"
}
def suggested_items(item):
    for k,v in dict.items():
        if dict[item] == v and k != item:
            print(k)

item = input("search: ")
if item in dict:
    print(f"Item name: {item}")
    print("Suggested items for you: ")
    suggested_items(item)
else:
    print("No matching item found.")


