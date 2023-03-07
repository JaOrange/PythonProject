# hyjGOAT
# 2022/11/4 12:00

from pypinyin import lazy_pinyin, Style
import time
import re
import sys

res = list()


def write_log(action, str2):
    localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    with open(str2, "a", encoding='UTF-8') as f:
        f.write(localtime+"  "+action)


def get_first_letter(str1):
    ans = ''.join(lazy_pinyin(str1, style=Style.FIRST_LETTER))
    return ans.upper()


def is_chinese(word):
    for ch in word:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False


def fuzzysearch(str2, str3):
    str1 = input("请输入省会城市的名称：")
    write_log("输入了省会城市的名称：%s，进行模糊搜索\n" % str1, str2)
    while not is_chinese(str1):
        print("城市名称不存在！请输入中文：")
        write_log("输入了非中文名称，搜索失败!\n", str2)
        str1 = input()
        write_log("输入了省会城市的名称：%s，进行模糊搜索\n" % str1, str2)

    # with open("test.txt", "r", encoding='UTF-8') as f:
    #     for content in f:
    #         item1 = list(content)
    #         item2 = list(str1)
    #         for i in item1:
    #             if i in item2:
    #                 res.append(item1)
    #                 break
    # for item in res:
    #     sep = ""
    #     del item[-1]
    #     print(res.index(item), sep.join(item))

    with open(str3, "r", encoding='UTF-8') as f:
        for content in f:
            if re.search(str1, content) is not None:
                # tup = re.search(content, str1).span()
                # if tup[1] - tup[0] <= len(str1):
                res.append(content.replace('\n',''))
        for i in res:
            print(res.index(i), i)


def progress_bar():
    t = 60
    start = time.perf_counter()
    print("正在搜索中......")
    for i in range(t + 1):
        finsh = "▓" * i
        need_do = "-" * (t - i)
        progress = (i / t) * 100
        dur = time.perf_counter() - start
        print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(progress, finsh, need_do, dur), end="")
        time.sleep(0.05)
    print("\n")


def choose_city_num(str2):
    num = int(input("请输入你选择城市的序号："))
    while num >= len(res):
        print("城市序号输入错误！请再次输入：")
        write_log("由于输入了错误的序号所以没有查询到结果\n", str2)
        num = int(input())
    sep = ""
    item = res[num]
    write_log("输入了正确的城市序号：%d，确定了所选择城市的名称：%s\n" % (num, sep.join(item)), str2)
    initial_letter = get_first_letter(sep.join(item))
    progress_bar()
    print("搜索结果为：%s，所对应的文件路径为：%s" % (sep.join(item)+"->"+initial_letter,\
                    "D:\python_demo\\v1_version\city\\"+sep.join(item)+".txt"))
    write_log("成功得到最终搜索结果：%s\n" % (sep.join(item)+"->"+initial_letter), str2)


def generate_city_file():
    with open("test.txt", "r", encoding='UTF-8') as f:
        for content in f:
             open("D:\python_demo\\v1_version\city\\" + content[0:-1] + ".txt", "a")


def main(argv):
    # generate_city_file()
    # str1 = sys.argv[1]  #城市名称
    str2 = sys.argv[1]  # 日志文件路径
    str3 = sys.argv[2]  # 城市文件路径
    # num = int(sys.argv[4])   #城市编号
    fuzzysearch(str2, str3)
    choose_city_num(str2)


if __name__ == '__main__':
    main(sys.argv)




# python D:\python_demo\v1_version1\v1.py D:\python_demo\v1_version1\Log.txt D:\python_demo\v1_version1\test.txt






