import jieba
import re
from simhash import Simhash

def readfile(path):
    f=open(path,'r',encoding='UTF-8')
    return f.read()

def writefile(path,similarity):
    f=open(path,'w',encoding='UTF-8')
    f.write(f"文本相似度为：%.2f"%similarity)

def cut(str):
    str=jieba.cut(str)
    result=[]
    for flag in str:     #将文本中除英文和中文外的其它过滤掉
        if(re.match(u"[a-zA-Z0-9\u4e00-\u9fa5]",flag)):
            result.append(flag)
        else:
            pass
    return result

def Analyse(text1,text2):
    a_simhash = Simhash(text1)
    b_simhash = Simhash(text2)
    max_hashbit = max(len(bin(a_simhash.value)), len(bin(b_simhash.value)))
    # 汉明距离
    distince = a_simhash.distance(b_simhash)
    print(distince)
    similar = 1 - distince / max_hashbit
    return similar

f1=readfile("orig.txt")
f2=readfile("orig_0.8_add.txt")
s1=cut(f1)
s2=cut(f2)
result=Analyse(s1,s2)
print(f"文本相似度为：%.2f"%result)
writefile("savefile.txt",result)
