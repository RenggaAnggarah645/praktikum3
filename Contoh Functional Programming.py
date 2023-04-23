# Fungsi penjumlahan
def add(x, y):
    return x + y

# Fungsi higher order
def apply_operation(x, y, operation):
    return operation(x, y)

# Contoh pemanggilan fungsi
result = apply_operation(2, 3, add)
print(result) # Output: 5
