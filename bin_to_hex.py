bin_arr = []
hex_arr = []
with open('pat0.txt', 'r') as file:
    for line in file:
        bin_arr.append(line.strip())

hex_arr = [hex(int(b,2))[2:] for b in bin_arr]
"""
    r: if exist, read or write
    w: if exist, cover; else make a new file
    a: if exist, add; else make a new file
"""
with open('./pat0_hex.txt', 'w') as file:
    for item in hex_arr:
        file.write(f"{item}\n")

print(bin_arr)
print(hex_arr)