from flask import Flask, render_template, request
import math

app = Flask(__name__)

PreviousEquation = []
equation = ['0']
result = 0
resulted = False


@app.route('/', methods=['POST', 'GET'])
def interface():
    global resulted
    global equation

    # button inputs
    if request.method == 'POST':

        if request.form['submit_button'] == '=':
            evaluate()

        elif request.form['submit_button'] == 'C':
            equation.clear()
            equation.append('0')

        elif request.form['submit_button'] == 'x²':
            if resulted:
                resulted = False
            equation.append('²')

        elif request.form['submit_button'] == '√':
            if (equation[0] == '0') and (len(equation) == 1):
                equation.extend(('√', '('))
                del equation[0]
            else:
                equation.extend(('√', '('))

            if resulted:
                resulted = False

        elif request.form['submit_button'] == 'Del':
            if len(equation) == 1:
                equation.append('0')
                del equation[0]
            else:
                del equation[-1]

        elif request.form['submit_button'] == '/':
            equation.append('/')

            if resulted:
                resulted = False

        elif request.form['submit_button'] == 'X':
            equation.append('X')

            if resulted:
                resulted = False

        elif request.form['submit_button'] == '+':
            if resulted:
                resulted = False

            equation.append('+')

        elif request.form['submit_button'] == '-':
            if resulted:
                resulted = False

            equation.append('-')

        elif request.form['submit_button'] == '(':
            if (equation[0] == '0') and (len(equation) == 1):
                equation.append('(')
                del equation[0]
            else:
                equation.append('(')

            resulted = False

        elif request.form['submit_button'] == ')':
            if (equation[0] == '0') and (len(equation) == 1):
                equation.append(')')
                del equation[0]
            else:
                equation.append(')')

            resulted = False

        elif request.form['submit_button'] == '.':
            if resulted:
                equation.clear()
                equation.append('0')
                equation.append('.')
                resulted = False
            else:
                equation.append('.')

        # NUMBERS
        elif request.form['submit_button'] == '0':
            if (equation[0] == '0') and (len(equation) == 1):
                equation.append('0')
                del equation[0]
            elif resulted:
                equation.clear()
                equation.append('0')
            else:
                equation.append('0')

            resulted = False

        elif request.form['submit_button'] == '1':
            if (equation[0] == '0') and (len(equation) == 1):
                equation.append('1')
                del equation[0]
            elif resulted:
                equation.clear()
                equation.append('1')
            else:
                equation.append('1')

            resulted = False

        elif request.form['submit_button'] == '2':
            if (equation[0] == '0') and (len(equation) == 1):
                equation.append('2')
                del equation[0]
            elif resulted:
                equation.clear()
                equation.append('2')
            else:
                equation.append('2')

            resulted = False

        elif request.form['submit_button'] == '3':
            if (equation[0] == '0') and (len(equation) == 1):
                equation.append('3')
                del equation[0]
            elif resulted:
                equation.clear()
                equation.append('3')
            else:
                equation.append('3')

            resulted = False

        elif request.form['submit_button'] == '4':
            if (equation[0] == '0') and (len(equation) == 1):
                equation.append('4')
                del equation[0]
            elif resulted:
                equation.clear()
                equation.append('4')
            else:
                equation.append('4')

            resulted = False

        elif request.form['submit_button'] == '5':
            if (equation[0] == '0') and (len(equation) == 1):
                equation.append('5')
                del equation[0]
            elif resulted:
                equation.clear()
                equation.append('5')
            else:
                equation.append('5')

            resulted = False

        elif request.form['submit_button'] == '6':
            if (equation[0] == '0') and (len(equation) == 1):
                equation.append('6')
                del equation[0]
            elif resulted:
                equation.clear()
                equation.append('6')
            else:
                equation.append('6')

            resulted = False

        elif request.form['submit_button'] == '7':
            if (equation[0] == '0') and (len(equation) == 1):
                equation.append('7')
                del equation[0]
            elif resulted:
                equation.clear()
                equation.append('7')
            else:
                equation.append('7')

            resulted = False

        elif request.form['submit_button'] == '8':
            if (equation[0] == '0') and (len(equation) == 1):
                equation.append('8')
                del equation[0]
            elif resulted:
                equation.clear()
                equation.append('8')
            else:
                equation.append('8')

            resulted = False

        elif request.form['submit_button'] == '9':
            if (equation[0] == '0') and (len(equation) == 1):
                equation.append('9')
                del equation[0]
            elif resulted:
                equation.clear()
                equation.append('9')
            else:
                equation.append('9')

            resulted = False

    return render_template('interface.html', MainDis=MainDisplay(), SecondDis=SecondDisplay())


def evaluate():
    global equation
    global PreviousEquation
    i = 0
    z = 0
    NumBracketPairs = 0
    Error = False

    # sets previous equation
    PreviousEquation.clear()
    while i < len(equation):
        PreviousEquation.append(equation[i])
        i += 1

    PreviousEquation.append('=')

    i = 0

    # checks to see brackets are even
    while i < len(equation):

        if equation[i] == '(':
            z += 1
        elif equation[i] == ')':
            NumBracketPairs += 1

        if equation[i] == '(' and equation[i + 1] == ')':
            Error = True

        # increments loop
        i += 1

    print('NumBracketPairs: ' + str(NumBracketPairs))

    # if brackets are even and not "()"
    if z == NumBracketPairs and Error is False:

        if NumBracketPairs > 0:
            EvalBrackets(NumBracketPairs)

        # solves final equation
        FinalEvalODMAS()

    # if there is an error
    else:
        equation.clear()
        equation.append('NaN')

    # sets previous equation
    if equation[0] != 'Infinity' and equation[0] != 'NaN':
        PreviousEquation.append(equation[0])


def EvalBrackets(NumBracketPairs):
    global result
    global equation
    i = 0
    y = 0
    MultiplyBracket = False
    InnerBrackets = False
    TempEquation = []

    print('evaluating brackets')

    while y < NumBracketPairs:

        # finds first left bracket index
        while i < len(equation):

            if equation[i] == '(':
                break
            else:
                # increments loop
                i += 1

        # moves z to 1 in front of bracket to avoid infinite loop
        z = i + 1

        # checks for inner brackets
        # finds first right bracket and any brackets in between
        while equation[z] != ')':

            if equation[z] == '(':
                InnerBrackets = True
                i = z
                break
            elif equation[z] != '(':
                InnerBrackets = False

            # increments loop
            z += 1

        print('Inner brackets:' + str(InnerBrackets))
        z += 1

        while InnerBrackets:
            while equation[z] != ')':

                if equation[z] == '(':
                    InnerBrackets = True
                    i = z
                    break
                elif equation[z] != '(':
                    InnerBrackets = False

                # increments loop
                z += 1

            print('Inner brackets:' + str(InnerBrackets))
            z += 1

        # finds end of final set of inner brackets
        z = i
        while equation[z] != ')':
            # increments loop
            z += 1

        # index of final inner bracket
        print('Start of final bracket index: ' + str(i))
        # end of new array
        print('End of final bracket index: ' + str(z))

        # checks for multiplication
        if (equation[i - 1] != '+') and (equation[i - 1] != '-') and (equation[i - 1] != '/') and (
                equation[i - 1] != 'X') and (equation[i - 1] != '(') and (equation[i - 1] != '√') and (i != 0):
            MultiplyBracket = True
        print('Multiply brackets = ' + str(MultiplyBracket))

        # sets temp equation
        x = i
        while i < (z + 1):
            TempEquation.append(equation[i])
            i += 1

        i = x

        print('Final brackets equation: ' + ''.join(TempEquation))
        print('Full equation: ' + ''.join(equation))

        # solves brackets
        EvalODMAS(TempEquation)

        print('Temp equation result: ' + str(result))

        if MultiplyBracket:
            equation = equation[:i] + ['X'] + [str(result)] + equation[z + 1:]
        else:
            equation = equation[:i] + [str(result)] + equation[z + 1:]

        print('New equation: ' + ''.join(equation))

        i = 0
        MultiplyBracket = False
        InnerBrackets = False
        TempEquation = []

        # increments loop
        y += 1


def EvalODMAS(li):
    global result
    global resulted

    i = 0

    print('li: ' + ''.join(li))

    # If () deletes them
    if li[0] == '(' and li[-1] == ')':
        del li[0]
        del li[-1]
        print('Brackets removed: ' + ''.join(li))

    # if list has no operators (for square routes)
    while i < len(equation):
        if (equation[i] == '√') or (equation[i] == '²') or (equation[i] == 'X') or (equation[i] == '/') or (
                equation[i] == '+') or (equation[i] == '-'):
            break
        else:
            i += 1

    if i == len(equation) - 1:
        result = float(''.join(equation))

    # Solves each √
    while i < len(li):

        if li[i] == '√':

            print('square route')

            # position of (
            z = i + 1

            # finds n2
            # loop starting from z, will break if item == +, -, /, X, ², √
            while z < len(li):
                if (li[z] == '+') or (li[z] == '-') or (li[z] == '/') or (li[z] == 'X') or (li[z] == '²') or (
                        li[z] == '√'):
                    break
                else:
                    z += 1

            # n2
            n2 = float(''.join(li[i + 1:z]))
            print('n2: ' + str(n2))

            # checks for multiplication
            if li[i - 1] != '+' and li[i - 1] != '-' and li[i - 1] != '/' and li[i - 1] != 'X' and li[i - 1] != '(' and \
                    li[i - 1] != '√' and i != 0:
                result = math.sqrt(n2)
                print('result = ' + str(result))
                li = li[:i] + ['X'] + [str(result)] + li[z + 1:]
                print(li)
            else:
                result = math.sqrt(n2)
                print('result = ' + str(result))
                li = li[:i] + [str(result)] + li[z + 1:]
                print(li)

            # resets i to 0 so can recheck the array
            i = 0

            # signals resulted
            resulted = True
            print('Resulted: ' + str(resulted))

        # increments loop
        i += 1

    i = 0

    # Solves each x²
    while i < len(li):

        if li[i] == '²':
            print('squared')

            z = i - 1

            # finds n1
            while z >= 0:
                if (li[z] == '+') or (li[z] == '-') or (li[z] == '/') or (li[z] == 'X') or (li[z] == '²') or (
                        li[z] == '√'):
                    break
                else:
                    z -= 1

            n1 = float(''.join(li[z + 1:i]))
            print('n1: ' + str(n1))

            result = n1 * n1
            print('result = ' + str(result))

            li = li[:z + 1] + [str(result)] + li[i + 1:]
            print(li)

            # resets i to 0 so can recheck the array
            i = 0

            # signals resulted
            resulted = True
            print('Resulted: ' + str(resulted))

        # increments loop
        i += 1

    i = 0

    # solves each div/mul
    while i < len(li):

        if li[i] == '/':
            print('division')

            if li[i+1] == '0':
                li.clear()
                li.append('Infinity')
            else:
                z = i - 1

                # finds n1
                while z >= 0:
                    if (li[z] == '+') or (li[z] == '-') or (li[z] == '/') or (li[z] == 'X') or (li[z] == '²') or (
                            li[z] == '√'):
                        break
                    else:
                        z -= 1

                n1 = float(''.join(li[z + 1:i]))
                print('n1: ' + str(n1))

                x = z + 1
                z = i + 1

                # accounts for -n2
                if li[i + 1] == '-':
                    z = i + 2

                # finds n2
                # loop starting from z, will break if item == +, -, /, X, ², √
                while z < len(li):
                    if (li[z] == '+') or (li[z] == '-') or (li[z] == '/') or (li[z] == 'X') or (li[z] == '²') or (
                            li[z] == '√'):
                        break
                    else:
                        z += 1

                # n2
                n2 = float(''.join(li[i + 1:z]))
                print('n2: ' + str(n2))

                result = n1 / n2
                print('result: ' + str(result))

                li = li[:x] + [str(result)] + li[z:]
                print(li)

                # resets i to 0 so can recheck the array
                i = 0

                # signals resulted
                resulted = True
                print('Resulted: ' + str(resulted))



        elif li[i] == 'X':
            print('multiplication')

            z = i - 1

            # finds n1
            while z >= 0:
                if (li[z] == '+') or (li[z] == '-') or (li[z] == '/') or (li[z] == 'X') or (li[z] == '²') or (
                        li[z] == '√'):
                    break
                else:
                    z -= 1

            n1 = float(''.join(li[z + 1:i]))
            print('n1: ' + str(n1))

            x = z + 1
            z = i + 1

            # accounts for -n2
            if li[i + 1] == '-':
                z = i + 2

            # finds n2
            # loop starting from z, will break if item == +, -, /, X, ², √
            while z < len(li):
                if (li[z] == '+') or (li[z] == '-') or (li[z] == '/') or (li[z] == 'X') or (li[z] == '²') or (
                        li[z] == '√'):
                    break
                else:
                    z += 1

            # n2
            n2 = float(''.join(li[i + 1:z]))
            print('n2: ' + str(n2))

            result = n1 * n2
            print('result: ' + str(result))

            li = li[:x] + [str(result)] + li[z:]
            print(li)

            # resets i to 0 so can recheck the array
            i = 0

            # signals resulted
            resulted = True
            print('Resulted: ' + str(resulted))

        # increments loop
        i += 1

    i = 0

    # solves each addition / subtraction
    while i < len(li):

        if li[i] == '+':
            print('addition')

            z = i - 1

            # finds n1
            while z >= 0:
                if (li[z] == '+') or (li[z] == '-') or (li[z] == '/') or (li[z] == 'X') or (li[z] == '²') or (
                        li[z] == '√'):
                    break
                else:
                    z -= 1

            n1 = float(''.join(li[z + 1:i]))
            print('n1: ' + str(n1))

            x = z + 1
            z = i + 1

            # accounts for -n2
            if li[i + 1] == '-':
                z = i + 2

            # finds n2
            # loop starting from z, will break if item == +, -, /, X, ², √
            while z < len(li):
                if (li[z] == '+') or (li[z] == '-') or (li[z] == '/') or (li[z] == 'X') or (li[z] == '²') or (
                        li[z] == '√'):
                    break
                else:
                    z += 1

            # n2
            n2 = float(''.join(li[i + 1:z]))
            print('n2: ' + str(n2))

            result = n1 + n2
            print('result: ' + str(result))

            li = li[:x] + [str(result)] + li[z:]
            print(li)

            # resets i to 0 so can recheck the array
            i = 0

            # signals resulted
            resulted = True
            print('Resulted: ' + str(resulted))

        elif li[i] == '-':
            print('addition')

            z = i - 1

            # finds n1
            while z >= 0:
                if (li[z] == '+') or (li[z] == '-') or (li[z] == '/') or (li[z] == 'X') or (li[z] == '²') or (
                        li[z] == '√'):
                    break
                else:
                    z -= 1

            n1 = float(''.join(li[z + 1:i]))
            print('n1: ' + str(n1))

            x = z + 1
            z = i + 1

            # accounts for -n2
            if li[i + 1] == '-':
                z = i + 2

            # finds n2
            # loop starting from z, will break if item == +, -, /, X, ², √
            while z < len(li):
                if (li[z] == '+') or (li[z] == '-') or (li[z] == '/') or (li[z] == 'X') or (li[z] == '²') or (
                        li[z] == '√'):
                    break
                else:
                    z += 1

            # n2
            n2 = float(''.join(li[i + 1:z]))
            print('n2: ' + str(n2))

            result = n1 - n2
            print('result: ' + str(result))

            li = li[:x] + [str(result)] + li[z:]
            print(li)

            # resets i to 0 so can recheck the array
            i = 0

            # signals resulted
            resulted = True
            print('Resulted: ' + str(resulted))

        # increments loop
        i += 1


def FinalEvalODMAS():
    global equation
    global result
    global resulted

    i = 0

    print('equation: ' + ''.join(equation))

    # If () deletes them
    if equation[0] == '(' and equation[-1] == ')':
        del equation[0]
        del equation[-1]
        print('Brackets removed: ' + ''.join(equation))

    # if list has no operators (for square routes)
    while i < len(equation):
        if (equation[i] == '√') or (equation[i] == '²') or (equation[i] == 'X') or (equation[i] == '/') or (
                equation[i] == '+') or (equation[i] == '-'):
            break
        else:
            i += 1

    if i == len(equation) - 1:
        result = float(''.join(equation))

    i = 0

    # Solves each √
    while i < len(equation):

        if equation[i] == '√':

            print('square route')

            # position of (
            z = i + 1

            # finds n2
            # loop starting from z, will break if item == +, -, /, X, ², √
            while z < len(equation):
                if (equation[z] == '+') or (equation[z] == '-') or (equation[z] == '/') or (equation[z] == 'X') or (
                        equation[z] == '²') or (
                        equation[z] == '√'):
                    break
                else:
                    z += 1

            # n2
            n2 = float(''.join(equation[i + 1:z]))
            print('n2: ' + str(n2))

            # checks for multiplication
            if equation[i - 1] != '+' and equation[i - 1] != '-' and equation[i - 1] != '/' and equation[
                i - 1] != 'X' and equation[i - 1] != '(' and \
                    equation[i - 1] != '√' and i != 0:
                result = math.sqrt(n2)
                print('result = ' + str(result))
                equation = equation[:i] + ['X'] + [str(result)] + equation[z + 1:]
                print(equation)
            else:
                result = math.sqrt(n2)
                print('result = ' + str(result))
                equation = equation[:i] + [str(result)] + equation[z + 1:]
                print(equation)

            # resets i to 0 so can recheck the array
            i = 0

            # signals resulted
            resulted = True
            print('Resulted: ' + str(resulted))

        # increments loop
        i += 1

    i = 0

    # Solves each x²
    while i < len(equation):

        if equation[i] == '²':
            print('squared')

            z = i - 1

            # finds n1
            while z >= 0:
                if (equation[z] == '+') or (equation[z] == '-') or (equation[z] == '/') or (equation[z] == 'X') or (
                        equation[z] == '²') or (
                        equation[z] == '√'):
                    break
                else:
                    z -= 1

            n1 = float(''.join(equation[z + 1:i]))
            print('n1: ' + str(n1))

            result = n1 * n1
            print('result = ' + str(result))

            equation = equation[:z + 1] + [str(result)] + equation[i + 1:]
            print(equation)

            # resets i to 0 so can recheck the array
            i = 0

            # signals resulted
            resulted = True
            print('Resulted: ' + str(resulted))

        # increments loop
        i += 1

    i = 0

    # solves each div/mul
    while i < len(equation):

        if equation[i] == '/':
            print('division')

            if equation[i+1] == '0':
                equation.clear()
                equation.append('Infinity')
            else:
                z = i - 1

                # finds n1
                while z >= 0:
                    if (equation[z] == '+') or (equation[z] == '-') or (equation[z] == '/') or (equation[z] == 'X') or (
                            equation[z] == '²') or (
                            equation[z] == '√'):
                        break
                    else:
                        z -= 1

                n1 = float(''.join(equation[z + 1:i]))
                print('n1: ' + str(n1))

                x = z + 1
                z = i + 1

                # accounts for -n2
                if equation[i + 1] == '-':
                    z = i + 2

                # finds n2
                # loop starting from z, will break if item == +, -, /, X, ², √
                while z < len(equation):
                    if (equation[z] == '+') or (equation[z] == '-') or (equation[z] == '/') or (equation[z] == 'X') or (
                            equation[z] == '²') or (
                            equation[z] == '√'):
                        break
                    else:
                        z += 1

                # n2
                n2 = float(''.join(equation[i + 1:z]))
                print('n2: ' + str(n2))

                result = n1 / n2
                print('result: ' + str(result))

                equation = equation[:x] + [str(result)] + equation[z:]
                print(equation)

                # resets i to 0 so can recheck the array
                i = 0

                # signals resulted
                resulted = True
                print('Resulted: ' + str(resulted))



        elif equation[i] == 'X':
            print('multiplication')

            z = i - 1

            # finds n1
            while z >= 0:
                if (equation[z] == '+') or (equation[z] == '-') or (equation[z] == '/') or (equation[z] == 'X') or (
                        equation[z] == '²') or (
                        equation[z] == '√'):
                    break
                else:
                    z -= 1

            n1 = float(''.join(equation[z + 1:i]))
            print('n1: ' + str(n1))

            x = z + 1
            z = i + 1

            # accounts for -n2
            if equation[i + 1] == '-':
                z = i + 2

            # finds n2
            # loop starting from z, will break if item == +, -, /, X, ², √
            while z < len(equation):
                if (equation[z] == '+') or (equation[z] == '-') or (equation[z] == '/') or (equation[z] == 'X') or (
                        equation[z] == '²') or (
                        equation[z] == '√'):
                    break
                else:
                    z += 1

            # n2
            n2 = float(''.join(equation[i + 1:z]))
            print('n2: ' + str(n2))

            result = n1 * n2
            print('result: ' + str(result))

            equation = equation[:x] + [str(result)] + equation[z:]
            print(equation)

            # resets i to 0 so can recheck the array
            i = 0

            # signals resulted
            resulted = True
            print('Resulted: ' + str(resulted))

        # increments loop
        i += 1

    i = 0

    # solves each addition / subtraction
    while i < len(equation):

        if equation[i] == '+':
            print('addition')

            z = i - 1

            # finds n1
            while z >= 0:
                if (equation[z] == '+') or (equation[z] == '-') or (equation[z] == '/') or (equation[z] == 'X') or (
                        equation[z] == '²') or (
                        equation[z] == '√'):
                    break
                else:
                    z -= 1

            n1 = float(''.join(equation[z + 1:i]))
            print('n1: ' + str(n1))

            x = z + 1
            z = i + 1

            # accounts for -n2
            if equation[i + 1] == '-':
                z = i + 2

            # finds n2
            # loop starting from z, will break if item == +, -, /, X, ², √
            while z < len(equation):
                if (equation[z] == '+') or (equation[z] == '-') or (equation[z] == '/') or (equation[z] == 'X') or (
                        equation[z] == '²') or (
                        equation[z] == '√'):
                    break
                else:
                    z += 1

            # n2
            n2 = float(''.join(equation[i + 1:z]))
            print('n2: ' + str(n2))

            result = n1 + n2
            print('result: ' + str(result))

            equation = equation[:x] + [str(result)] + equation[z:]
            print(equation)

            # resets i to 0 so can recheck the array
            i = 0

            # signals resulted
            resulted = True
            print('Resulted: ' + str(resulted))

        elif equation[i] == '-':
            print('addition')

            z = i - 1

            # finds n1
            while z >= 0:
                if (equation[z] == '+') or (equation[z] == '-') or (equation[z] == '/') or (equation[z] == 'X') or (
                        equation[z] == '²') or (
                        equation[z] == '√'):
                    break
                else:
                    z -= 1

            n1 = float(''.join(equation[z + 1:i]))
            print('n1: ' + str(n1))

            x = z + 1
            z = i + 1

            # accounts for -n2
            if equation[i + 1] == '-':
                z = i + 2

            # finds n2
            # loop starting from z, will break if item == +, -, /, X, ², √
            while z < len(equation):
                if (equation[z] == '+') or (equation[z] == '-') or (equation[z] == '/') or (equation[z] == 'X') or (
                        equation[z] == '²') or (
                        equation[z] == '√'):
                    break
                else:
                    z += 1

            # n2
            n2 = float(''.join(equation[i + 1:z]))
            print('n2: ' + str(n2))

            result = n1 - n2
            print('result: ' + str(result))

            equation = equation[:x] + [str(result)] + equation[z:]
            print(equation)

            # resets i to 0 so can recheck the array
            i = 0

            # signals resulted
            resulted = True
            print('Resulted: ' + str(resulted))

        # increments loop
        i += 1


def MainDisplay():
    global equation

    if equation[0] == 'NaN':
        return 'Malformed expression'
    elif equation[0] == 'Infinity':
        return 'Math error: dividing by 0'
    else:
        return ''.join(equation)


def SecondDisplay():
    return ''.join(PreviousEquation)


if __name__ == "__main__":
    app.run(debug=True)
