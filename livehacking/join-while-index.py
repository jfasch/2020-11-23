def join(stringlist, separator):
    joined_str = ''
    i = 0
    while i < len(stringlist):
        joined_str += stringlist[i]
        if i < len(stringlist) - 1:
            joined_str += separator
        i += 1
    return joined_str

stringlist = ['eins', 'zwei', 'drei']
# stringlist = ['eins']
# stringlist = []
joined_stringlist = join(stringlist, '-')
print(joined_stringlist)

# -> 'eins-zwei-drei'
