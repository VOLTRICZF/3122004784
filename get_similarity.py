import re
import jieba
from simhash import Simhash
import sys

# 打印系统默认编码（一般是utf-8）
print(sys.getdefaultencoding())

def get_similarity(original_text, copy_text):
    """
    计算两段文本的相似度（重复度）

    Args：
        original_text(str): 原始文本
        copy_text(str): 抄袭文本
    Returns:
        float: 文本相似度，值为0-1之间
    """
    # 清洗文本（去除非汉字字符）
    pattern = re.compile(r'[\u4e00-\u9fa5]+')
    cl_test1 = re.findall(pattern, original_text)  # 从原始文本提取汉字
    cl_test2 = re.findall(pattern, copy_text)  # 从抄袭文本提取汉字

    # 将清洗后的文本列表合并为字符串
    original_text = ''.join(cl_test1)
    copy_text = ''.join(cl_test2)

    # 对字符串进行分词
    original_words = list(jieba.cut(original_text))  # 原始文本分词
    copy_words = list(jieba.cut(copy_text))  # 抄袭文本分词

    # 生成simhash值
    original_simhash = Simhash(original_words)  # 原始文本的simhash值
    copy_simhash = Simhash(copy_words)  # 抄袭文本的simhash值

    # 计算海明距离（两个simhash值之间的距离）
    distance = original_simhash.distance(copy_simhash)

    # 计算重复率，海明距离越小，文本相似度越高
    similarity = 1 - distance / 64  # 64是simhash的位数
    return similarity  # 返回相似度