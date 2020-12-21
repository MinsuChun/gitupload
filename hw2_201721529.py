def string_sort(*args,case=1):
    if args== () :
        print('"There is no input"')
    else:
        a= list(args)
        b= ' '.join(a)
        if case== 'u':
            c= b.upper()
        elif case== 'l':
            c= b.lower()
        else:
            c= b
        d= c.split()
        d.sort()
        e= ' '.join(d)
        print(e)

string_sort()
string_sort('my name is')
string_sort('abc fgh', 'edg')
string_sort('Abc', 'Edf', 'agh', 'ff')
string_sort('Abc', 'Edf', 'agh', 'ff', case= 'l')
string_sort('Abc', 'Edf', 'agh', 'ff', case= 'u')
