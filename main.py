def capital_indexes(arg):
    upperchars = []
    x=-1
    for s in arg:
        x+=1
        if s.isupper():
            upperchars.append(arg.find(s, l))
    return upperchars
