def correct(string):
    return string.replace('5','S').replace('0','O').replace('1','I')
    
OR

def correct(str_, replacements = {'5': 'S', '0': 'O', '1': 'I'}):
    return "".join(replacements.get(c, c) for c in str_)
