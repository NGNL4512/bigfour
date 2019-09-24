import jieba
import os
import matplotlib.pyplot as plt

#切換自訂詞庫
jieba.set_dictionary('dict1.txt')
#jieba.add_word('增加') 手動增加詞庫

'''
文章斷詞
'''
def cutword(filename):
    cutin=filename #放進去斷詞的文章
    outtxt='./斷詞輸出/斷詞輸出.txt'

    f=open(cutin,'r',encoding='UTF-8')
    out=open(outtxt,'w',encoding='UTF-8')

    w=f.read()

    seg_list = jieba.cut(w)  #精準模式
    cuttext="/".join(seg_list)
    out.write(cuttext)
    #print(cuttext)
    f.close()
    out.close()
'''
跟詞庫比較，並返回加總分數
'''
def searchkey(filesimilar):
    outtxt='./斷詞輸出/斷詞輸出.txt'
    #outtxt=filename
    keytxt=filesimilar

    fl=open(outtxt,'r+',encoding='UTF-8')
    f=open(keytxt,'r')
    w=fl.read()
    lines = f.readlines()
    keyword = []  ## 空列表, 将第i行数据存入list中
    for i in range(0,lines.__len__(),1):
        keyword.append([])
        for word in lines[i].split('，'): #切割逗號
            if word != '':
                keyword[i].append(word) 
# =============================================================================
#                 global K
#                 k=0
#                 for x in range(0,word.__len__(),1):
#                     asc=ord(word[x])
#                     if asc>127:
#                         k+=asc
#                 #print(hash(k),id(k))
#                 print(hash(50))
# =============================================================================
    f.close()
# =============================================================================
#     for i in range(0,len(keyword),1):
#         for j in range(1,len(keyword[i]),1):
#             print(keyword[i][j])
# =============================================================================
    cutarray=[]
    for word in w.split('/'):
        if word != '':
            cutarray.append(word) 
            #print(word)

    #cutarray.sort()
    setcut=set(cutarray)
    #print("想死" in setcut)

    sum=0
    allkey=[]
    
# =============================================================================
#     a=0
#     for i in range(0,len(keyword),1):
#         for j in range(1,len(keyword[i]),1):
#             while True:
#             #從a的位置開始找keyword[i][j] 
#                 idkey=w.find(keyword[i][j],a)
#                 if idkey==-1:  #-1等於沒找到退出迴圈
#                     break
#                 else:
#                     a=idkey+1
#                     sum+=int(keyword[i][0])
#                     allkey.append(keyword[i][j])
# =============================================================================
                    
    for i in range(0,len(keyword),1):
        for j in range(1,len(keyword[i]),1):
                if keyword[i][j] in setcut:
                    sum+=int(keyword[i][0])*cutarray.count(keyword[i][j])
                    allkey.append(keyword[i][j])
# =============================================================================
#     if allkey==[]:
#         print("沒有關鍵字")
# =============================================================================
# =============================================================================
#     else:
#         allkey.sort()
#         #set() 函数创建一个无序不重复元素集
#         #就是把同樣關鍵字砍到只剩下1個
#         allkeyset=set(allkey)
#         for item in allkeyset: #顯示關鍵字幾次
#             print (item,":",cutarray.count(item),"次")
#         print("總共",sum,"分")
# =============================================================================
    fl.close()
    return sum
'''
選擇哪個文字檔
#現沒用到#
'''
def readfile():
    filepath = "./speaktxt/" #存放文字檔的路徑
    filename= os.listdir(filepath) #資料夾下的所有檔案 
    num=0
    for file in range(len(filename)):
        print(num+1, end=".")
        num+=1
        print(filename[file])
    name = input('請輸入檔名：')
    return filepath+filename[int(name)-1]

def similar_score():
    filepath = "./similar/" #存放文字檔的路徑
    filename= os.listdir(filepath) #資料夾下的所有檔案 
    allsimilar=[]
    for file in range(len(filename)):
        #print(filepath+filename[file])
        score=searchkey(filepath+filename[file])
        allsimilar.append(score)
    #for i in range(0,score.__len__(),1):
    return allsimilar

'''
繪製長條圖
#現沒用到#
'''
def bar_graph(score): #害怕，悲傷，憂鬱，焦慮，生氣
    similarname = ['scared', 'sad', 'melancholy', 'anxiety', 'angry']
    #X軸名稱，Y軸分數
    plt.bar(similarname, score, label = '情緒')
    for a,b in zip(similarname,score):  
        plt.text(a, b+0.05, '%.0f' % b,fontsize=11)
    plt.xlabel("similar")  #设置X轴Y轴名稱  
    plt.ylabel("score")    
    plt.show()
    
    
def init():
    filename="./speaktxt/recording.txt" #選擇錄音轉換成文字的檔案
    #filesimilar=keysimilar()
    cutword(filename) #斷詞
    score=similar_score()
    #bar_graph(score)
    #print(score)
    return score
    
    
if __name__ == '__main__':
    init()