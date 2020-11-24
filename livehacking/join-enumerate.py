def join(stringlist, separator):
    joined_str = ''
    for index, s in enumerate(stringlist):
        joined_str += s
        if index < len(stringlist) - 1:
            joined_str += separator
    return joined_str

stringlist = ['eins', 'zwei', 'drei']
# stringlist = ['eins']
# stringlist = []
joined_stringlist = join(stringlist, '-')
print(joined_stringlist)

# -> 'eins-zwei-drei'
