import edit_distance
import search


def init():
    res=search.init()
    ree=edit_distance.init()
    mainsun=[]
    for i in range(len(res)):
        mainsun.append(res[i]+ree[i])
    print(mainsun) #害怕，悲傷，憂鬱，焦慮，生氣
if __name__ == '__main__':
    init()