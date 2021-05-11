

def Read():
    file= input('enter a file path:')
    handle=open(file, encoding='utf-8')
    dictionery(handle)
               
def dictionery(handle:str):
    idL=list()
    fileL=list()
    Data=dict()
    counter=-1
    for line in handle:
        counter+=1
        if counter==1:
            nStart=line.find(' "')
            nEnd=line.find('" ',nStart)
            chat_name=line[nStart+1:nEnd]
            creatAnd=line.find(',')
            creation_date=line[0:creatAnd-1]
        try:
            float(line[0])
            endDate=line.find('-')
            sNum=line.find('-')
            endNum=line.find(':',sNum)
            num=line[sNum+1:endNum].rstrip()
            if endNum != -1:
                if num not in idL:
                    idL.append(num)
                    index=idL.index(num)
                    fileL.append({"datetime":line[0:endDate],"id":index, "text":line[endNum:].rsplit()},)        
        
        except:
            continue
    Data = {'chat_name': chat_name , 'creation_date':creation_date , 'num_of_purtic':len(idL) , 'creator':idL[0] }
    fileL.append(Data)
    import json
    noya_birthday_party=json.dumps(fileL)
    print(fileL)