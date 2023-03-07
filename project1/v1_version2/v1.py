# hyjGOAT
# 2022/11/4 11:45

# hyjGOAT
# 2022/11/4 10:37

from pypinyin import lazy_pinyin, Style
import time
import re
import sys
from loguru import logger
from my_Log import Log


res = list()
log = Log()


# def write_log(action):
#     localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
#     with open("Log.txt", "a", encoding='UTF-8') as f:
#         f.write(localtime+"  "+action)


def get_first_letter(str1):
    ans = ''.join(lazy_pinyin(str1, style=Style.FIRST_LETTER))
    return ans.upper()


def is_chinese(word):
    for ch in word:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False


def fuzzysearch():
    str1 = input("请输入省会城市的名称：")
    # write_log("输入了省会城市的名称：%s，进行模糊搜索\n" % str1)
    # logger.add('my_log.log')
    # logger.info("输入了城市名称，正在检测输入格式是否正确")
    log.info("输入了城市名称，正在检测输入格式是否正确")
    while not is_chinese(str1):
        print("城市名称不存在！请输入中文：")
        # write_log("输入了非中文名称，搜索失败!\n")
        # logger.add('my_log.log')
        # logger.error("输入了非中文名称!")
        log.error("输入了非中文名称!")
        str1 = input()
        # write_log("输入了省会城市的名称：%s，进行模糊搜索\n" % str1)
        # logger.add('my_log.log')
        # logger.info("输入了正确的城市名称，正在进行模糊搜索")
        log.info("输入了正确的城市名称，正在进行模糊搜索")

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

    with open("test.txt", "r", encoding='UTF-8') as f:
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


def choose_city_num():
    num = int(input("请输入你选择城市的序号："))
    while num >= len(res):
        print("城市序号输入错误！请再次输入：")
        # write_log("由于输入了错误的序号所以没有查询到结果\n")
        # logger.add('my_log.log')
        # logger.error("输入了错误的序号，没有查询到结果")
        log.error("输入了错误的序号，没有查询到结果")
        num = int(input())
    sep = ""
    item = res[num]
    # write_log("输入了正确的城市序号：%d，确定了所选择城市的名称：%s\n" % (num, sep.join(item)))
    # logger.add('my_log.log')
    # logger.info("输入了正确的城市序号")

    initial_letter = get_first_letter(sep.join(item))
    progress_bar()
    print("搜索结果为：%s，所对应的文件路径为：%s" % (sep.join(item)+"->"+initial_letter,\
                    "D:\python_demo\\v1_version2\city\\"+sep.join(item)+".txt"))
    # write_log("成功得到最终搜索结果：%s\n" % (sep.join(item)+"->"+initial_letter))
    # logger.add('my_log.log')
    # logger.success('搜索成功！')
    log.info("搜索成功")


def generate_city_file():
    with open("test.txt", "r", encoding='UTF-8') as f:
        for content in f:
             open("D:\python_demo\\v1_version2\city\\" + content[0:-1] + ".txt", "a")


fuzzysearch()
choose_city_num()












