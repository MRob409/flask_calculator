from flask import Flask, render_template, request

app = Flask(__name__)

PreviousEquation = []
equation = ['0']


@app.route('/', methods=['POST', 'GET'])
def interface():

    global equation

    # button inputs
    if request.method == 'POST':

        if request.form['submit_button'] == '=':
            evaluate()
        elif request.form['submit_button'] == 'C':
            equation.clear()
            equation.append('0')
        elif request.form['submit_button'] == 'x²':
            equation.append('²')
        elif request.form['submit_button'] == '√':
            if (equation[0] == '0') and (len(equation) == 1):
                equation.extend(('√', '('))
                del equation[0]
            else:
                equation.extend(('√', '('))
        elif request.form['submit_button'] == 'Del':
            if len(equation) == 1:
                equation.append('0')
                del equation[0]
            else:
                del equation[-1]
        elif request.form['submit_button'] == '/':
            equation.append('/')
        elif request.form['submit_button'] == 'X':
            equation.append('X')
        elif request.form['submit_button'] == '+':
            equation.append('+')
        elif request.form['submit_button'] == '-':
            equation.append('-')
        elif request.form['submit_button'] == '(':
            if (equation[0] == '0') and (len(equation) == 1):
                equation.append('(')
                del equation[0]
            else:
                equation.append('(')
        elif request.form['submit_button'] == ')':
            if (equation[0] == '0') and (len(equation) == 1):
                equation.append(')')
                del equation[0]
            else:
                equation.append(')')

        # NUMBERS
        elif request.form['submit_button'] == '0':
            if (equation[0] == '0') and (len(equation) == 1):
                equation.append('0')
                del equation[0]
            else:
                equation.append('0')
        elif request.form['submit_button'] == '1':
            if (equation[0] == '0') and (len(equation) == 1):
                equation.append('1')
                del equation[0]
            else:
                equation.append('1')
        elif request.form['submit_button'] == '2':
            if (equation[0] == '0') and (len(equation) == 1):
                equation.append('2')
                del equation[0]
            else:
                equation.append('2')
        elif request.form['submit_button'] == '3':
            if (equation[0] == '0') and (len(equation) == 1):
                equation.append('3')
                del equation[0]
            else:
                equation.append('3')
        elif request.form['submit_button'] == '4':
            if (equation[0] == '0') and (len(equation) == 1):
                equation.append('4')
                del equation[0]
            else:
                equation.append('4')
        elif request.form['submit_button'] == '5':
            if (equation[0] == '0') and (len(equation) == 1):
                equation.append('5')
                del equation[0]
            else:
                equation.append('5')
        elif request.form['submit_button'] == '6':
            if (equation[0] == '0') and (len(equation) == 1):
                equation.append('6')
                del equation[0]
            else:
                equation.append('6')
        elif request.form['submit_button'] == '7':
            if (equation[0] == '0') and (len(equation) == 1):
                equation.append('7')
                del equation[0]
            else:
                equation.append('7')
        elif request.form['submit_button'] == '8':
            if (equation[0] == '0') and (len(equation) == 1):
                equation.append('8')
                del equation[0]
            else:
                equation.append('8')
        elif request.form['submit_button'] == '9':
            if (equation[0] == '0') and (len(equation) == 1):
                equation.append('9')
                del equation[0]
            else:
                equation.append('9')

    return render_template('interface.html', MainDis=MainDisplay(), SecondDis=SecondDisplay())


def evaluate():
    global equation
    equation = equation


def MainDisplay():
    return ''.join(equation)


def SecondDisplay():
    return ''.join(PreviousEquation)


if __name__ == "__main__":
    app.run(debug=True)
