def dpll(operacion, params={}):
    if len(operacion) == 0:
        return True, params
    
    for c in operacion:
        if len(c)==0:
            bandera = True
            return False, None

    l = ''
    for c in operacion:
        for literal in c:
            l = literal[0]
            break
    
    operacionb =[]
    for x in operacion:
        if (l, True) not in x:
            operacionb.append(x)


    operaciond = []
    for x in operacionb:
        operaciond.append(x.difference({(l, False)}))


    sat, vals = dpll(operaciond, {**params, **{l: True}})
    if sat:
        return sat, vals
 
    operacionb =[]
    for x in operacion:
        if (l, False) not in x:
            operacionb.append(x)

    operaciond = []
    for x in operacionb:
        operaciond.append(x.difference({(l, True)}))
    sat, vals = dpll(operaciond, {**params, **{l: False}})
    if sat:
        return sat, vals
 
    return False, None


