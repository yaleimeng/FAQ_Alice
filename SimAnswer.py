# -*- coding: utf-8 -*-
'''
@author: yaleimeng@sina.com
@license: (C) Copyright 2017
@desc: 
@DateTime: Created on 2017/11/23, at 8:32 by PyCharm '''

import csv
from jpype import *  # 启动JVM。如果是Linux，两个路径之间的分号;要替换为英文冒号:


class SimilarAnswer(object):
    '''
    句子相似度应答类。提供了构造函数，析构函数，应答函数。
    '''

    def __init__(self, datafile='D:/FAQ2.csv'):  # 虚拟机开销较大，最好是一开始就打开。
        self.__QA = dict()
        startJVM(getDefaultJVMPath(), "-Djava.class.path=C:/HanLP/hanlp-portable-1.5.1.jar;C:/HanLP",
                 "-Xms1g", "-Xmx1g")
        self.__Advisor = JClass('com.hankcs.hanlp.suggest.Suggester')
        self.Suggester = self.__Advisor()
        with open(datafile, 'r', encoding='utf-8') as f:
            f_csv = csv.reader(f)
            for row in f_csv:
                self.__QA[row[0]] = row[1]  # 将“问--答对”保存到字典中。
                self.Suggester.addSentence(row[0])  # 问句添加到Suggest的句子库。

    def __del__(self):  # 析构函数中关闭虚拟机。
        shutdownJVM()

    def get_answer(self, question):
        wen = self.Suggester.suggest(question, 1)  # 得到问句推荐的具体结果。
        for q, a in self.__QA.items():
            if wen[0] == q:  # 问句在字典中与key匹配，如果成功直接返回value
                print(a)
                break
        else:
            print('Sorry，我还不够聪明，不能回答您的问题。您能换种方式提问吗？')


####      自我测试代码。      ####
if __name__ == "__main__":
    Bot = SimilarAnswer()
    Bot.get_answer('请问贵司有哪些数据产品？')
