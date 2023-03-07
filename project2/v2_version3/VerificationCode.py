# hyjGOAT
# 2022/11/11 19:23

import random
# 注意： 这里生成的是0-9A-Za-z的列表
# 比如： code_list = ['P','y','t','h','o','n','T','a','b'] # PythonTab的字母


class VerificationCode:

    def generate_verification_code(self):
        code_list = []
        for i in range(10):  # 0-9数字
            code_list.append(str(i))
        for j in range(65, 91):  # 对应从“A”到“Z”的ASCII码
            code_list.append(chr(j))
        for k in range(97, 123):  # 对应从“a”到“z”的ASCII码
            code_list.append(chr(k))
        my_slice = random.sample(code_list, 6)  # 从list中随机获取6个元素，作为一个片断返回
        verification_code = ''.join(my_slice)  # list to string
        return verification_code




