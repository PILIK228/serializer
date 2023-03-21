with open('db1.json') as DB:
    m = DB.read().split('\n')
global_dict = dict()
d = dict()
empty_dict = dict()

i = 0

def CreateDict(index):
    d = dict()
    
    global i
    for _ in range(index+1, len(m)):
        i += 1
        s = str(m[i].strip())
        if s == "{" or s == "},": #пропуск фигурных скобок
            continue
        ind = s.find('"', 1)
        key = s[1:ind]
        if s.endswith(": {"): 
            d[key]= CreateDict(i)
            continue
        if s.endswith(","):
            if s[-2] == '"':
                value = s[ind+4: -2]
                d[key] = value
            else:
                value = int(s[ind+3: -1])
                d[key] = value
        elif s.endswith('"'): #закрытие словаря
            value = s[ind+4: -1]
            d[key] = value
            return d
        else:
            value = int(s[ind+3:])
            d[key] = value
            return d
        #if s.endswith(": ["):


print(CreateDict(0))
