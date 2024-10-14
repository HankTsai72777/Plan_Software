import os
def hex_file_to_array(file_path):
    """
    從指定的 .hex 文件中讀取數據，忽略以 @ 開頭的地址行，並將數據轉換為一維數組。
    """
    hex_array = []
    # 讀取文件中的所有行
    with open(file_path, 'r') as file:
        lines = file.readlines()
    # 遍歷每一行
    for line in lines:
        # 忽略以 '@' 開頭的地址行
        if line.startswith('@'):
            continue
        # 去除空格並按每兩個字符分割
        hex_values = line.strip().split(' ')
        # 將非空的十六進制值加入數組
        hex_array.extend([value for value in hex_values if value])
    return hex_array
def combine_hex_file(file_path, output_file_path):
    file_path0 = os.path.join(file_path, "main0.hex")
    file_path1 = os.path.join(file_path, "main1.hex")
    file_path2 = os.path.join(file_path, "main2.hex")
    file_path3 = os.path.join(file_path, "main3.hex")

    hex_array0 = hex_file_to_array(file_path0)
    hex_array1 = hex_file_to_array(file_path1)
    hex_array2 = hex_file_to_array(file_path2)
    hex_array3 = hex_file_to_array(file_path3)

    combined_hex_array = [a+b+c+d for a, b, c, d in zip(hex_array3, hex_array2, hex_array1, hex_array0)]
    with open(output_file_path, 'w') as output_file:
        for item in combined_hex_array:
            output_file.write(item + '\n')