from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def interface():
    return render_template('interface.html')


if __name__ == "__main__":
    app.run(debug=True)


Equation = ['0']
PreviousEquation = ['6', '-', '6', '=', '0']


# def MainDisplay():
#     return Equation
#
#
# def SecondDisplay():
#     return PreviousEquation
