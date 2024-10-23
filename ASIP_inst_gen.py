# Basic Function
def dec_to_bin_str(dec_num, bits):
    bin_representation = bin(dec_num)[2:]
    bin_num = bin_representation.zfill(bits)
    return bin_num
def hex_to_bin_str(hex_num, bits):
    if isinstance(hex_num, int):
        hex_num = hex(hex_num)[2:]
    dec_num = int(hex_num, 16)
    bin_representation = bin(dec_num)[2:]
    bin_num = bin_representation.zfill(bits)
    return bin_num
def dec_to_hex_str(dec_num, bits):
    hex_representation = hex(dec_num)[2:]
    hex_num = hex_representation.zfill(bits)
    return hex_num
def hex_to_dec_value(hex_num):
    if isinstance(hex_num, int):
        hex_num = hex(hex_num)[2:]
    dec_value = int(hex_num, 16)
    return dec_value
# Compiler
def ASIP_inst_gen(opcode, spi_data_size, data_num, start_addr, end_addr=0, choose_data_num=0):
    # LOAD & DUMP
    if ((opcode==1)|(opcode==2)):
        opcode_bin = dec_to_bin_str(opcode, 4)
        TBD_bin = dec_to_bin_str(0, 9)
        match spi_data_size:
            case 64:
                spi_data_size_encode = 3
            case 32:
                spi_data_size_encode = 2
            case 16:
                spi_data_size_encode = 1
            case 8:
                spi_data_size_encode = 0
            case _:
                spi_data_size_encode = 3
                raise ValueError("Invalid spi_data_size value")
        spi_data_size_bin = dec_to_bin_str(spi_data_size_encode, 3)

        if (choose_data_num==1):
            start_addr_plus_data_num = (hex_to_dec_value(start_addr))\
                + int(spi_data_size/4 * data_num)
            end_addr_bin = dec_to_bin_str(int(start_addr_plus_data_num), 24)
        else:
            end_addr_bin = hex_to_bin_str(end_addr, 24)

        start_addr_bin = hex_to_bin_str(start_addr, 24)
        ASIP_inst_bin = opcode_bin + TBD_bin + spi_data_size_bin\
            + end_addr_bin + start_addr_bin
    # change to hex type
    ASIP_inst_dec       = int(ASIP_inst_bin, 2)
    ASIP_inst_hex       = dec_to_hex_str(ASIP_inst_dec, 8)
    return ASIP_inst_hex
def ASIP_txt_gen(ASIP_inst_str, file_name):
    ASIP_inst_32bit = ASIP_inst_str.zfill(8)
    with open(file_name, 'w') as f:
        f.write(ASIP_inst_32bit)
    return ASIP_inst_32bit