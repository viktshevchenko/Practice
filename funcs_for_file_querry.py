import random
variable_2 = ['x', 'y']
variable_3 = ['x', 'y', 'z']
variable_4 = ['x', 'y', 'z', 't']

boolean_operations = ['<=', '==', '&', '|', '^']
sign = ['', '~']

def generate_function(count_var):
    function = ""
    var_last = ''
    match count_var:
        case 2:
            for i in range(random.randint(3, 8)):
                negation = random.choice(sign)
                var = random.choice(variable_2)
                while var == var_last:
                    var = random.choice(variable_2)
                var_last = var
                function += negation + var + " "
                op = random.choice(boolean_operations)
                function += op + " "
        case 3:
            for i in range(random.randint(3, 10)):
                negation = random.choice(sign)
                var = random.choice(variable_3)
                while var == var_last:
                    var = random.choice(variable_2)
                var_last = var
                function += negation + var + " "
                op = random.choice(boolean_operations)
                function += op + " "
        case 4:
            for i in range(random.randint(3, 12)):
                negation = random.choice(sign)
                var = random.choice(variable_2)
                while var == var_last:
                    var = random.choice(variable_4)
                var_last = var
                function += negation + var + " "
                op = random.choice(boolean_operations)
                function += op + " "
        case _:
            if count_var < 2:
                return generate_function(2)
            elif count_var > 4:
                return generate_function(4)
    function = function[:-3]
    value_bool_func = truth_table(str(function), count_var)

    while (not '0' in value_bool_func) or (not '1' in value_bool_func) or '-' in value_bool_func:
        function = generate_function(count_var)
        value_bool_func = truth_table(str(function), count_var)
    return function

def truth_table(func, count_var):
    value = ''
    match count_var:
        case 2:
            #print('x y f')
            for x in range(2):
                for y in range(2):
                    f = eval(func)
                    #print(x, y, int(f))
                    value += str(int(f))
        case 3:
            #print('x y z f')
            for x in range(2):
                for y in range(2):
                    for z in range(2):
                        f = eval(func)
                        #print(x, y, z, int(f))
                        value += str(int(f))
        case 4:
            #print('x y z t f')
            for x in range(2):
                for y in range(2):
                    for z in range(2):
                        for t in range(2):
                            f = eval(func)
                            #print(x, y, z, t, int(f))
                            value += str(int(f))
        case _:
            if count_var < 2:
                return truth_table(func, 2)
            elif count_var > 4:
                return truth_table(func, 4)
    return value

def sdnf(bool_func, count_var):
    value_bool_func = str(truth_table(str(bool_func), count_var))
    result = ''
    i = 0
    match count_var:
        case 2:
            for x in range(2):
                for y in range(2):
                    if value_bool_func[i] == '0':
                        result += '('
                        if x == 0:
                            result += 'x & '
                        elif x == 1:
                            result += '~x & '
                        if y == 0:
                            result += 'y'
                        elif y == 1:
                            result += '~y'
                        result += ') | '
                    i += 1
        case 3:
            for x in range(2):
                for y in range(2):
                    for z in range(2):
                        if value_bool_func[i] == '0':
                            result += '('
                            if x == 0:
                                result += 'x & '
                            elif x == 1:
                                result += '~x & '
                            if y == 0:
                                result += 'y & '
                            elif y == 1:
                                result += '~y & '
                            if z == 0:
                                result += 'z'
                            elif z == 1:
                                result += '~z'
                            result += ') | '
                        i += 1
        case 4:
            for x in range(2):
                for y in range(2):
                    for z in range(2):
                        for t in range(2):
                            if value_bool_func[i] == '0':
                                result += '('
                                if x == 0:
                                    result += 'x & '
                                elif x == 1:
                                    result += '~x & '
                                if y == 0:
                                    result += 'y & '
                                elif y == 1:
                                    result += '~y & '
                                if z == 0:
                                    result += 'z & '
                                elif z == 1:
                                    result += '~z & '
                                if t == 0:
                                    result += 't'
                                elif t == 1:
                                    result += '~t'
                                result += ') | '
                            i += 1
    return result[:-3]

def sknf(bool_func, count_var):
    value_bool_func = truth_table(str(bool_func), count_var)
    result = ''
    i = 0
    match count_var:
        case 2:
            for x in range(2):
                for y in range(2):
                    if value_bool_func[i] == '1':
                        result += '('
                        if x == 1:
                            result += 'x | '
                        elif x == 0:
                            result += '~x | '
                        if y == 1:
                            result += 'y'
                        elif y == 0:
                            result += '~y'
                        result += ') & '
                    i += 1
        case 3:
            for x in range(2):
                for y in range(2):
                    for z in range(2):
                        if value_bool_func[i] == '1':
                            result += '('
                            if x == 1:
                                result += 'x | '
                            elif x == 0:
                                result += '~x | '
                            if y == 1:
                                result += 'y | '
                            elif y == 0:
                                result += '~y | '
                            if z == 1:
                                result += 'z'
                            elif z == 0:
                                result += '~z'
                            result += ') & '
                        i += 1
        case 4:
            for x in range(2):
                for y in range(2):
                    for z in range(2):
                        for t in range(2):
                            if value_bool_func[i] == '1':
                                result += '('
                                if x == 1:
                                    result += 'x | '
                                elif x == 0:
                                    result += '~x | '
                                if y == 1:
                                    result += 'y | '
                                elif y == 0:
                                    result += '~y | '
                                if z == 1:
                                    result += 'z | '
                                elif z == 0:
                                    result += '~z | '
                                if t == 1:
                                    result += 't'
                                elif t == 0:
                                    result += '~t'
                                result += ') & '
                            i += 1
    return result[:-3]

def polinom_Zhegalkina(bool_func, count_var):
    value_bool_func = truth_table(str(bool_func), count_var)
    func_sdnf = str(sdnf(value_bool_func, count_var))
    if '~x' in func_sdnf:
        func_sdnf = func_sdnf.replace('~x', '(1 ^ x)')
    if '~y' in func_sdnf:
        func_sdnf = func_sdnf.replace('~y', '(1 ^ y)')
    if '~z' in func_sdnf:
        func_sdnf = func_sdnf.replace('~z', '(1 ^ z)')
    if '~t' in func_sdnf:
        func_sdnf = func_sdnf.replace('~t', '(1 ^ t)')
    if '|' in func_sdnf:
        func_sdnf = func_sdnf.replace('|', '^')
    return func_sdnf
