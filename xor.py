def list_xor(list):
    eor = 0
    for i in list:
        eor ^= i
    return eor

def list_xor_2(list):
    eor = 0
    for i in list:
        eor ^= i
    
    right_one = eor & (~eor + 1) #提取二进制表示最右边的1
    
    num1 = 0
    num2 = 0

    for i in list:
        if i & right_one == 0:
            num1 ^= i
        else:
            num2 ^= i
    return num1,num2

if __name__ == "__main__":
    list = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7]
    #print(list_xor(list))
    print(list_xor_2(list))