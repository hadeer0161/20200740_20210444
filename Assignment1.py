import random
from sympy import sympify, to_cnf
from nltk.tokenize import word_tokenize

def eliminate_implication(expression):
    expression_list = list(expression)

    while ( '→' in expression_list ) :
        index = expression_list.index('→')
        expression_list[index] = '∨'
        expression_list.insert((index - 4 ) , '¬')

    while ('↔' in expression_list):
        index = expression_list.index('↔')

        sliced_part = expression_list[index - 4 : index + 5]
        before_slice = expression_list[:index - 4]
        after_slice = expression_list[index + 5:]

        first_part = sliced_part[:]
        second_part = sliced_part[:]

        first_part[4] = '∨'
        first_part.insert(0 , '¬')
        first_part.insert(0 , '(')
        first_part.insert(-1 , ')')

        second_part[4] = '∨'
        second_part.insert(5 , '¬')
        second_part.insert(0 , '(')
        second_part.insert(-1 , ')')
        second_part.insert(0, '∧')

        expression_list = before_slice + first_part + second_part + after_slice

    expression = ''.join(expression_list)
    return expression

def deMorgans(expression) :
    expression_list = list(expression)
    if ( '¬(' in expression ) :
        index = expression_list.index('¬')
        del expression_list[index]
        expression_list.insert(index + 1 , "NOT")
        expression_list.insert(index + 7 , "NOT")

        if (expression_list[index + 6] == '∧') :
            expression_list[index + 6] = '∨'
        elif (expression_list[index + 6] == '∨'):
            expression_list[index + 6] = '∧'
    return ''.join(expression_list)

# def apply_deMorgans(expression):
#     if ("¬(" in expression) :
#         # Step 1: Remove '¬' from its position
#         expression = expression.replace('¬', '')
#
#         # Step 2: Add '¬' before predicates
#         expression = re.sub(r'([A-Za-z]\([A-Za-z]\))', r'¬\1', expression)
#
#         # Change ")∧¬" to ")∨¬"
#         expression = re.sub(r'\)(?:∧¬)', ')∨¬', expression)
#
#         # Change ")∨¬" to ")∧¬"
#         expression = re.sub(r'\)(?:∨¬)', ')∧¬', expression)
#     return expression

def doubleNeg(expression_list) :
    if ('¬' in expression_list):
        index = expression_list.index('¬')
        if (expression_list[index] == '¬' and  expression_list[index + 1] == '¬') :
            del expression_list[index + 1]
            del expression_list[index]
    return expression_list

def find_index(expression_list , symbol) :
    index = 0
    if (symbol in expression_list):
        index = expression_list.index(symbol)
    return index


def prenex_form(expression_list):
    result = []
    exp = []

    i = 0

    while i < len(expression_list):
        if expression_list[i] in  ['∀', '∃']:
            exp.append(expression_list[i])
            exp.append(expression_list[i+1])
            i += 2
        else:
            result.append(expression_list[i])
            i += 1

    if len(exp) > 0:
        i = 0
        arr = []
        arr2 = []
        while i < len(exp):
            if exp[i] == '∀':
                arr.append(exp[i])
                arr.append(exp[i + 1])
            else:
                arr2.append(exp[i])
                arr2.append(exp[i + 1])
            i += 2

        exp = arr + arr2
        # t=''.join(reversed(result))

        result = exp + result

    return result

def Skolemization_existential(expression_list):
    i=0
    c=''
    exp=[]
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u', 'v']
    while i<len(expression_list):
        if expression_list[i]== '∃':
            c=c+expression_list[i+1]
            i+=2
        elif expression_list[i] in c:
            tem= random.choice(alphabets)
            i+=1
            exp.append(tem)
            #print(exp ,"    ",tem)
        else :

            exp.append(expression_list[i])
            i += 1
    return exp

def Eliminate_universal (expressions_list):
    exp=[]
    i=0
    while i < len(expressions_list):
        if expressions_list[i]=='∀':
            i+=2
            continue
        else:
            exp.append(expressions_list[i])
            i+=1
    return exp
import random

import random

import random

def conjunctions_into_clauses(expression_list):
    exp = []
    c = ''
    i = 0
    issue = ['∃', '∀']
    d=''
    while i < len(expression_list):
        if expression_list[i] in issue and i + 1 < len(expression_list):
            exp.append(expression_list[i])
            if expression_list[i + 1] =='∃':
                alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                             's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
                temp = random.choice(alphabets)

                if temp == expression_list[i + 1]:
                    a = random.choice(alphabets)
                    while a == expression_list[i + 1]:
                        a = random.choice(alphabets)
                    c += a
                    j = i
                    while j < len(expression_list):
                        if expression_list[i + 1] == expression_list[j]:
                            pass
                        j += 1


                    i += 2
                else:
                    c += expression_list[i + 1]

                    i += 2
                exp.append(expression_list[i+1])
            else:
                i += 2
                exp.append(expression_list[i + 1])
            if expression_list[i + 1] == '∀':
                alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                             's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
                temp = random.choice(alphabets)

                if temp == expression_list[i + 1]:
                    a = random.choice(alphabets)
                    while a == expression_list[i + 1]:
                        a = random.choice(alphabets)
                    d += a
                    j = i
                    while j < len(expression_list):
                        if expression_list[i + 1] == expression_list[j]:
                            pass
                        j += 1

                    i += 2
                else:
                    d += expression_list[i + 1]

                    i += 2
                exp.append(expression_list[i + 1])
            else:
                i += 2
                exp.append(expression_list[i + 1])

        else:
            exp.append(expression_list[i])
            i += 1

    return exp
def count_function(expression_list):
    exp = {}

    for i in range(len(expression_list)):
        count = 0
        j = i
        while j < len(expression_list):
            if expression_list[j] == '¬':
                count = -1
            if expression_list[j] == '∧' or expression_list[j] == '∨' or expression_list[j] == '→' or expression_list[j] == '↔':
                break
            j += 1
        if count == 0:
            count = 1
            exp[expression_list[i]] = count
    return exp

def is_consistent(counts):
    total_sum = 0
    for key, value in counts.items():
        total_sum += value
    if total_sum != 0:
        print("Not consistent")
    else:
        print("Consistent")

expression = "∀x∃y((P(x)→Q(y))∧¬(P(x)∧Q(x))∨(R(x)↔S(y)))∨(∃z(T(z)→U(z))∧(∀w(V(w)↔W(w)∨¬(R(y)∧S(x))))"
processed_expression = list(eliminate_implication(expression))
# print(''.join(processed_expression))
# processed_expression = list(deMorgans(expression))
processed_expression = list(doubleNeg(expression))
processed_expression = conjunctions_into_clauses(processed_expression)
processed_expression = doubleNeg(processed_expression)
processed_expression = prenex_form(processed_expression)
processed_expression = Skolemization_existential(processed_expression)
processed_expression = Eliminate_universal(processed_expression)
print(''.join(processed_expression))
result = count_function(processed_expression)
is_consistent(result)