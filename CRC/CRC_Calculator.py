"""
    CRC Reference : http://www.sunshine2k.de/coding/javascript/crc/crc_js.html

    CAN => 15 = 0x4599, 17 = 0x16858, 21 = 0x102899 / init_value = 0x0 / Fianl Xor vaule = 0x0
    
    CRC Final xor value that is over 0 is not matching, But it is 0 matching(why??)

"""
class CrcCalculator(object):  
    def __init__(self, crcbit, poly, init_value, final_xor_value):
        self.crcbit = crcbit
        self.poly = poly
        self.crctable = []
        self.init_value = init_value
        self.final_xor_value = final_xor_value

        # start create crctable
        for value in range(256):
            test_byte = value
            for x in range(crcbit):
                if (test_byte & (1<<(crcbit-1))) != 0: # & crcbit MSB
                    test_byte = test_byte << 1 & ((1<<crcbit)-1) ^ self.poly
                else:
                    test_byte = test_byte << 1 & ((1<<crcbit)-1)
            self.crctable.append(test_byte)
        # end crctable

        # start set onebyte_over_bytes
        if 8 <= self.crcbit <= 16:
            self.onebyte_over_bytes = 0xff00
        elif 16 < self.crcbit <= 32:
            self.onebyte_over_bytes = 0xffff00
        elif 32 < self.crcbit <= 64:
            self.onebyte_over_bytes = 0xffffff00
        elif 64 < self.crcbit <= 128:
            self.onebyte_over_bytes = 0xffffffff00
        # end onebyte_over_bytes

    def byte_get_crc(self, byte_data):
        return self.make_crc(byte_data)

    def binay_get_crc(self, bin_data : str):
        # start makeing data list
        split_count = len(bin_data)//8
        if (len(bin_data) % 8) != 0:
            split_count += 1
        
        data_list = []

        data_list.append(bin_data[-8:])
        data_list.extend([bin_data[-(x+1)*8: -x*8] for x in range(1, split_count)])
        data_list = data_list[::-1]

        data_list = [int(x,2) for x in data_list]
        # end makeing data list

        return self.make_crc(data_list)

    def make_crc(self, data_list : "list[int]"):
        crc = self.init_value
        for data in data_list:
            if self.crcbit == 8:
                crc = self.crctable[(crc ^ data)]
            else:
                # if crc 16
                # c      : crc = crc << 8 ^ crctable((crc >> 8) ^ data)
                # python : crc = (crc << 8 & 0xff00) ^ crctable[((crc >> 8) & 0xff) ^ data]
                crc = (crc << 8 & self.onebyte_over_bytes) ^ self.crctable[(((crc >> (self.crcbit-8)) & 0xff) ^ data)]

        return (crc ^ self.final_xor_value)

if __name__ == "__main__":
    bin_message_data = "10101010"
    crc8_SAE_J1850 = CrcCalculator(8, 0x1D, 0xFF, 0xFF)
    print("crc8_SAE_J1850")
    print("Output value : {}".format(hex(crc8_SAE_J1850.binay_get_crc(bin_message_data))))
    print(">>>>")
    print("Expected value : 0x48")
    print("\n-----------------\n")

    crc16_CCIT_FALSE = CrcCalculator(16, 0x1021, 0xFFFF, 0x0)
    print("crc16_CCIT_FALSE")
    print("Output value : {}".format(hex(crc16_CCIT_FALSE.binay_get_crc(bin_message_data))))
    print(">>>>")
    print("Expected value : 0xf550")
    print("\n-----------------\n")

    CRC32_MPEG2 = CrcCalculator(32, 0x4C11DB7, 0xFFFFFFFF, 0x0)
    print("CRC32_MPEG2")
    print("Output value : {}".format(hex(CRC32_MPEG2.binay_get_crc(bin_message_data))))
    print(">>>>")
    print("Expected value : 0x90AD3F6C")
    print("\n-----------------\n")
      
    CRC64_ECMA_182 = CrcCalculator(64, 0x42F0E1EBA9EA3693, 0x0, 0x0)
    byte_message_data = [0xAA]
    print("CRC64_ECMA_182")
    print("Output value : {}".format(hex(CRC64_ECMA_182.byte_get_crc(byte_message_data))))
    print(">>>>")
    print("Expected value : 0x2D071B6213A0CB8B")
    print("\n-----------------\n")
      


