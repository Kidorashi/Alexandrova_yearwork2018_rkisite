from flask import Flask, render_template, url_for, request, redirect
from flask_bootstrap import Bootstrap
import os


app = Flask(__name__)
bootstrap = Bootstrap(app)


def get_num_mistake(num):
    num = str(num)
    path_test = 'tests/test_' + num + '.txt'
    # path_text = 'tests/text_' + num + '.txt'
    path_answrs = 'tests/write_answrs_' + num + '.txt'
    f_test = open(path_test, 'r', encoding = 'UTF-8')
    # f_text = open(path_text, 'r', encoding = 'UTF-8')
    f_answrs = open(path_answrs, 'r', encoding = 'UTF-8')
    
    test = f_test.readlines()
    # text = f_text.readlines()
    answrs = f_answrs.readlines()
    
    get_nums = []
    
    for n in range (0, len(test)):
        if test[n] != answrs[n]:
            get_nums.append(n)
            
    return get_nums


def add_check(answ):
    f = open('tests/write_answrs_1.txt', 'w', encoding = 'UTF-8')
    if answ == '':
        f.write('None')
    else:
        f.write(answ)
    return

@app.route('/index')
def index():
    if request.args:
       answ1 = request.args['answ1']
       return render_template('index.html', answ1 = answ1)
    return render_template('index.html')


@app.route('/main')
def main():
    return render_template('main.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/theory')
def theory():
    return render_template('theory.html')


@app.route('/exercise')
def exercise():
    return render_template('exercise.html')
 
    
@app.route('/ex1')
def ex1():
    f_a = open('tests/write_answrs_1.txt', 'w', encoding = 'UTF-8')
    if request.args:
        answ1 = request.args['answ1'].lower()
        add_check(answ1)
        answ2 = request.args['answ2'].lower()
        add_check(answ2)
        answ3 = request.args['answ3'].lower()
        add_check(answ3)
        answ4 = request.args['answ4'].lower()
        add_check(answ4)
        answ5 = request.args['answ5'].lower()
        add_check(answ5)
        answ6 = request.args['answ6'].lower()
        add_check(answ6)
        answ7 = request.args['answ7'].lower()
        add_check(answ7)
        answ8 = request.args['answ8'].lower()
        add_check(answ8)
        answ9 = request.args['answ9'].lower()
        add_check(answ9)
        answ10 = request.args['answ10'].lower()
        add_check(answ10)
        answ11 = request.args['answ11'].lower()
        add_check(answ11)
        answ12 = request.args['answ12'].lower()
        add_check(answ12)
        answ13 = request.args['answ13'].lower()
        add_check(answ13)
        answ14 = request.args['answ14'].lower()
        add_check(answ14)
        answ15 = request.args['answ15'].lower()
        add_check(answ15)
        
        f_a.write(answ1+'\n'+answ2+'\n'+answ3+'\n'+answ4+'\n'+answ5+'\n')
        f_a.write(answ6+'\n'+answ7+'\n'+answ8+'\n'+answ9+'\n'+answ10+'\n')
        f_a.write(answ11+'\n'+answ12+'\n'+answ13+'\n'+answ14+'\n'+answ15)
        
        #nums_mis = get_num_mistake(1)
       
        
        return redirect(url_for('exercise')) 
		# if answ1 != correct[0]:
			# correct[0] = 0
		# if answ2 != correct[1]:
			# correct[1] = 0
	
    return render_template('ex1.html')
	
@app.route('/ex21')
def ex21():
    f_a = open('tests/write_answrs_21.txt', 'w', encoding = 'UTF-8')
    if request.args:
        answ1 = request.args['answ1'].lower()
        add_check(answ1)
        answ2 = request.args['answ2'].lower()
        add_check(answ2)
        answ3 = request.args['answ3'].lower()
        add_check(answ3)
        answ4 = request.args['answ4'].lower()
        add_check(answ4)
        answ5 = request.args['answ5'].lower()
        add_check(answ5)
        answ6 = request.args['answ6'].lower()
        add_check(answ6)
        answ7 = request.args['answ7'].lower()
        add_check(answ7)
        answ8 = request.args['answ8'].lower()
        add_check(answ8)
        answ9 = request.args['answ9'].lower()
        add_check(answ9)
        answ10 = request.args['answ10'].lower()
        add_check(answ10)
        
		# if answ1 != correct[0]:
			# correct[0] = 0
		# if answ2 != correct[1]:
			# correct[1] = 0
        f_a.write(answ1+'\n'+answ2+'\n'+answ3+'\n'+answ4+'\n'+answ5+'\n')
        f_a.write(answ6+'\n'+answ7+'\n'+answ8+'\n'+answ9+'\n'+answ10+'\n')
         #nums_mis = get_num_mistake(21)

        return redirect(url_for('exercise')) 

    return render_template('ex21.html')


@app.route('/ex22')
def ex22():
    f_a = open('tests/write_answrs_22.txt', 'w', encoding = 'UTF-8')
    if request.args:
        answ1 = request.args['answ1'].lower()
        add_check(answ1)
        answ2 = request.args['answ2'].lower()
        add_check(answ2)
        answ3 = request.args['answ3'].lower()
        add_check(answ3)
        answ4 = request.args['answ4'].lower()
        add_check(answ4)
        answ5 = request.args['answ5'].lower()
        add_check(answ5)
        answ6 = request.args['answ6'].lower()
        add_check(answ6)
        answ7 = request.args['answ7'].lower()
        add_check(answ7)
        answ8 = request.args['answ8'].lower()
        add_check(answ8)
        answ9 = request.args['answ9'].lower()
        add_check(answ9)
        answ10 = request.args['answ10'].lower()
        add_check(answ10)
        
		# if answ1 != correct[0]:
			# correct[0] = 0
		# if answ2 != correct[1]:
			# correct[1] = 0
        f_a.write(answ1+'\n'+answ2+'\n'+answ3+'\n'+answ4+'\n'+answ5+'\n')
        f_a.write(answ6+'\n'+answ7+'\n'+answ8+'\n'+answ9+'\n'+answ10+'\n')
         #nums_mis = get_num_mistake(21)

        return redirect(url_for('exercise')) 

    return render_template('ex22.html')

if __name__ == '__main__':
    app.run(debug=True)
