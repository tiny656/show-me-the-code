# coding: utf-8

mask_word= [u'北京', u'程序员', u'公务员', u'领导', u'牛比', u'牛逼', u'你娘', u'你妈', 'love', 'sex', 'jiangge']

def input_check(inp):
    for m in mask_word:
        inp = inp.decode('gbk').replace(m, u'*'*len(m)).encode("gbk")
    return inp

if __name__ == '__main__':
    print input_check(raw_input())