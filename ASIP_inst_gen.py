def dec_to_bin_str(dec_num, bits):
    bin_representation = bin(dec_num)[2:]
    bin_num = bin_representation.zfill(bits)
    return bin_num
def dec_to_hex_str(dec_num, bits):
    hex_representation = hex(dec_num)[2:]
    hex_num = hex_representation.zfill(bits)
    return hex_num
def ASIP_inst_gen(opcode, end_target, end_addr, start_target, start_addr):
    # LOAD & DUMP
    if ((opcode==1)|(opcode==2)):
        opcode_bin          = dec_to_bin_str(opcode, 4)
        end_target_bin      = dec_to_bin_str(end_target, 5)
        end_addr_bin        = dec_to_bin_str(end_addr, 9)
        start_target_bin    = dec_to_bin_str(start_target, 5)
        start_addr_bin      = dec_to_bin_str(start_addr, 9)
        ASIP_inst_bin       = opcode_bin + end_target_bin + end_addr_bin +\
            start_target_bin + start_addr_bin

    # change to hex type
    ASIP_inst_dec       = int(ASIP_inst_bin, 2)
    ASIP_inst_hex       = dec_to_hex_str(ASIP_inst_dec, 4)
    return ASIP_inst_hex
def ASIP_txt_gen(ASIP_inst_str, file_name):
    ASIP_inst_32bit = ASIP_inst_str.zfill(8)
    with open(file_name, 'w') as f:
        f.write(ASIP_inst_32bit)
    return ASIP_inst_32bit