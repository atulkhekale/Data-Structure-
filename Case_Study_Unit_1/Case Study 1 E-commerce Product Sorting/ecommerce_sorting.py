
def merge(products, left, mid, right):
    temp = []
    i = left
    j = mid + 1

    while i <= mid and j <= right:
        if products[i][1] <= products[j][1]:
            temp.append(products[i])
            i += 1
        else:
            temp.append(products[j])
            j += 1

    while i <= mid:
        temp.append(products[i])
        i += 1

    while j <= right:
        temp.append(products[j])
        j += 1

    for k in range(len(temp)):
        products[left + k] = temp[k]


def merge_sort(products, left, right):
    if left < right:
        mid = (left + right) // 2

        merge_sort(products, left, mid)
        merge_sort(products, mid + 1, right)

        merge(products, left, mid, right)


products = [
    ["Mobile", 15000],
    ["Headphones", 1500],
    ["Laptop", 45000],
    ["Mouse", 500],
    ["Keyboard", 1000]
]

n = len(products)
merge_sort(products, 0, n - 1)

print("Products sorted by price:")
for product in products:
    print(product[0], "- Rs.", product[1])
