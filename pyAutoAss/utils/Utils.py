# 获取汉字首字母
def multiGetLetter(str_input:str)->str:
    """获取汉字首字母
    
    Keyword arguments:
    str_input -- 输入需要获取汉字首字母的字符串
    Return: 汉字首字母
    """
    

    def single_get_first(unicode1):
        str1 = unicode1.encode('gbk')
        # print(len(str1))
        try:
            ord(str1)
            return str1
        except:
            asc = str1[0] * 256 + str1[1] - 65536
            # print(asc)
            if asc >= -20319 and asc <= -20284:
                return 'a'
            if asc >= -20283 and asc <= -19776:
                return 'b'
            if asc >= -19775 and asc <= -19219:
                return 'c'
            if asc >= -19218 and asc <= -18711:
                return 'd'
            if asc >= -18710 and asc <= -18527:
                return 'e'
            if asc >= -18526 and asc <= -18240:
                return 'f'
            if asc >= -18239 and asc <= -17923:
                return 'g'
            if asc >= -17922 and asc <= -17418:
                return 'h'
            if asc >= -17417 and asc <= -16475:
                return 'j'
            if asc >= -16474 and asc <= -16213:
                return 'k'
            if asc >= -16212 and asc <= -15641:
                return 'l'
            if asc >= -15640 and asc <= -15166:
                return 'm'
            if asc >= -15165 and asc <= -14923:
                return 'n'
            if asc >= -14922 and asc <= -14915:
                return 'o'
            if asc >= -14914 and asc <= -14631:
                return 'p'
            if asc >= -14630 and asc <= -14150:
                return 'q'
            if asc >= -14149 and asc <= -14091:
                return 'r'
            if asc >= -14090 and asc <= -13119:
                return 's'
            if asc >= -13118 and asc <= -12839:
                return 't'
            if asc >= -12838 and asc <= -12557:
                return 'w'
            if asc >= -12556 and asc <= -11848:
                return 'x'
            if asc >= -11847 and asc <= -11056:
                return 'y'
            if asc >= -11055 and asc <= -10247:
                return 'z'
            return ''
    
    if isinstance(str_input, unicode):
        unicode_str = str_input
    else:
        try:
            unicode_str = str_input.decode('utf8')
        except:
            try:
                unicode_str = str_input.decode('gbk')
            except:
                print('unknown coding')
                return
    return_list = ""
    for one_unicode in unicode_str:
        try:
            return_list += single_get_first(one_unicode)
        except Exception:
            return_list += one_unicode
    return return_list

# 

# 坐标精度算法
# 比较数组中所有数据的差值，计算误差，取误差其中误差相近的一组数据，计算其中位坐标，返回中位坐标 可以考虑采用聚类算法kmeans、DBSCAN、 Hierarchical clustering
def coordinateAccuracy(avg_list:list) -> set:
    ...