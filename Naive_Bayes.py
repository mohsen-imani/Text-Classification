import os, copy, random, math
global folder_l, file_name, path, group
group = 'NULL'
print "\nPlease set the value of variable 'path' to the location of the extracted 20_newsgroups folder\nexample path = '/home/mohsen/ML/20_newsgroups/'\nNOTICE: do NOT forget to put the last '/' \n"
path = '/home/mohsen/mohsen/ML/20_newsgroups/'
def clean_text(data):
    data = data.replace('\n', ' ')
    remove_l = ['<','>','?','.','"',')','(','|','-','#','*','+']
    replace_l = ["'",'!','/','\\','=',',',':']
    data = data.lower()
    for i in remove_l:
        data = data.replace(i,'')
    for i in replace_l:
        data = data.replace(i,' ')
    return data

def get_file():
    global group
    while (len(folder_l)):
        r_fo = random.randint(0,len(folder_l)-1)
        folder_n = folder_l[r_fo]
        if len(file_name[folder_n])== 0:
            folder_l.remove(folder_n)
        else:
            r_fi = random.randint(0, len(file_name[folder_n])-1)
            fil = file_name[folder_n][r_fi]
            file_name[folder_n].remove(fil)
            group = folder_n
            data = open(path + folder_n + '/'+ fil,'r')
            return data.read()
    group = 'NULL'
    return 'NULL'

def get_probability(fields, dic):
    sum_ = sum(dic.values())
    p = 0.0
    for f in fields:
        value = dic.get(f, 0.0) + 0.0001
        p = p + math.log(float(value)/float(sum_))
    return p
#--------------------------Main --------------------------------------------
training_set = 500
folder_list = os.listdir(path)
i = 0 
total_dic = {}
dictionary = {}
file_name ={}
group = 'NULL'
print "Starting training part...."
for fo in folder_list:
    dic = {}
    folder_ = path + fo
    files = os.listdir(folder_)
    it = 0
    for fi in files:
        it = it + 1
        if it > training_set:
            break
        add = folder_ + '/'+fi
        myfile = open(add,'r')
        data = clean_text(myfile.read())
        fields = data.split(' ')
        for field in fields:
            if field == ' ' or field == '':
                continue
            value = dic.get(field, 0)
            value_t = total_dic.get(field, 0)
            if value == 0:
                dic[field] = 1
            else:
                dic[field] = value + 1
            if value_t == 0:
                total_dic[field] = 1
            else:
                total_dic[field] = value_t + 1
        files.remove(fi)
    file_name[fo] = files
    dictionary[fo] = dic
print len(total_dic), 'different words found in all files'
print "Starting testing part...."
data = 1
folder_l = copy.deepcopy(folder_list)
iteration = 0
success = 0
while (data):
    data = get_file()
    iteration = iteration + 1
    if data =='NULL':
        break
    data = clean_text(data)
    fields = data.split(' ')
    if '' in fields: fields.remove('')
    if ' ' in fields: fields.remove(' ')
    probabilities = []
    for c in folder_list:
        probabilities.append(get_probability(fields,dictionary[c]))
    if group == folder_list[probabilities.index(max(probabilities))]:
        success = success + 1   
print ('Success rate = %.1f'% (float(success)/float(iteration - 1)*100))



                
            

