def v(a=1, b='__0.0.0__ V'):
    if b == '__0.0.0__ V':
        return str(a / 10) + ' BETA ' + 'V'
    else:
        return str(a / 10) + ' BETA ' + b
