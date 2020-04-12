def show_magicians(listpara):
        "打印列表中的每个成员"
        for para in listpara:
                print(para)
def make_great(listpara):
        "为列表中每个成员加上'the Great'"
        result = []
        for para in listpara:
                result.append(('the Great' + para))

        listpara = result
        
        print(listpara)
        print(result)
        return listpara

def make_great1(listpara):
        for i in range(len(listpara)):
              listpara[i] = 'the great' +  listpara[i]

        return listpara
                
        
magic = ['zhao',"qian",'sun','li']

show_magicians(magic)

make_great(magic)
#make_great1(magic)

show_magicians(magic)
