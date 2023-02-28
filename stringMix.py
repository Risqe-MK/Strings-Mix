def mix(s1, s2):
    s1u,s2u, s1f,s2f = [],[],[],[]
    str1 = ''.join(sorted(s1))
    str2 = ''.join(sorted(s2))
    
    m1,m2 = '',''
    for c in str1:
        if c.islower():
            m1 += c
    for c in str2:
        if c.islower():
            m2 += c
    for c in m1:
        if c not in s1u:
            if m1.count(c) != 1:
                s1u.append(c)
    for c in m2:
        if c not in s2u:
            if m2.count(c) != 1:
                s2u.append(c)
    for i, v in enumerate(s1u):
        s1f.append([v])
        s1f[i].append(m1.count(v))
        s1f[i].append('1')
    for i, v in enumerate(s2u):
        s2f.append([v])
        s2f[i].append(m2.count(v))
        s2f[i].append('2')

    temp = []
        
    for i, v in enumerate(s1f):
        for j, z in enumerate(s2f):
            if v[0]==z[0] and v[1]==z[1] and v[1] > 1:
                temp.append([v[0],v[1],'='])
    for v in s1f.copy():
        for z in temp:
            if v[0]==z[0]:
                s1f.remove(v)
        for z in s2f:
            if v[0]==z[0]:
                if v[1] < z[1]:
                    s1f.remove(v)

    for v in s2f.copy():
        for z in temp:
            if v[0]==z[0]:
                s2f.remove(v)
        for z in s1f:
            if v[0]==z[0]:
                if v[1] < z[1]:
                    s2f.remove(v)
    
    final = s1f + s2f +temp
    f = []
    max = []
    for v in final:
        max.append(v[1])
    for x in sorted(max,reverse=True):
        for y in final:
            if x == y[1]:
                if y not in f:
                    f.append(y)
    s = ""
    for v in f:
        s += str(v[2]) + ":" + v[0]*v[1] + "/"
    return s[0:len(s)-1]
