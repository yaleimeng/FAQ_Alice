# -*- coding: utf-8 -*-
'''
@author: yaleimeng@sina.com
@license: (C) Copyright 2017
@desc: 
@DateTime: Created on 2017/11/22, at 13:13 by PyCharm '''

import Kernel

alice = Kernel.Kernel()
alice.learn("cn-test.aiml")

while True:
    print(alice.respond(input('Alice请您提问...>>')))