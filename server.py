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
    # stub for evaluate code
    global equation
    EvalODMAS(equation)


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
            n2 = float(''.join(li[i + 2:z]))
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

            z = i-1

            # finds n1
            while z >= 0:
                if (li[z] == '+') or (li[z] == '-') or (li[z] == '/') or (li[z] == 'X') or (li[z] == '²') or (
                        li[z] == '√'):
                    break
                else:
                    z -= 1

            n1 = float(''.join(li[z+1:i]))
            print('n1: ' + str(n1))

            result = n1*n1
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

            z = i-1

            # finds n1
            while z >= 0:
                if (li[z] == '+') or (li[z] == '-') or (li[z] == '/') or (li[z] == 'X') or (li[z] == '²') or (
                        li[z] == '√'):
                    break
                else:
                    z -= 1

            n1 = float(''.join(li[z + 1:i]))
            print('n1: ' + str(n1))

            x = z+1
            z = i+1

            # accounts for -n2
            if li[i+1] == '-':
                z = i+2

            # finds n2
            # loop starting from z, will break if item == +, -, /, X, ², √
            while z < len(li):
                if (li[z] == '+') or (li[z] == '-') or (li[z] == '/') or (li[z] == 'X') or (li[z] == '²') or (
                        li[z] == '√'):
                    break
                else:
                    z += 1

            # n2
            n2 = float(''.join(li[i+1:z]))
            print('n2: ' + str(n2))

            result = n1/n2
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
