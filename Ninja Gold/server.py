from flask import Flask, render_template, request, redirect, session
import datetime
import random
app = Flask(__name__)
app.secret_key='flkdbglkdfjbvo'


@app.route('/')         
def index():
    if 'message' not in session:
        session['message'] = []
    if 'gold_amount' not in session:
        session['gold_amount'] = 0
    return render_template("index.html", message = session['message'], gold_amount = session['gold_amount'])
@app.route('/process_money', methods = ['POST'])
def money():
    if request.form['action'] == 'farm':
        acquired_gold = random.randrange(1,21)
        session['gold_amount'] += acquired_gold
        session['message'].append('Earned '+str(acquired_gold)+ ' gold from the farm! ({:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now()))
    elif request.form['action'] == 'cave':
        acquired_gold = random.randrange(5, 11)
        session['gold_amount'] += acquired_gold
        session['message'].append('Earned '+str(acquired_gold)+ ' gold from the cave! ({:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now()))
    elif request.form['action'] == 'house':
        acquired_gold = random.randrange(2, 6)
        session['gold_amount'] += acquired_gold
        session['message'].append('Earned '+str(acquired_gold)+ ' gold from the house! ({:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now()))
    elif request.form['action'] == 'casino':
        acquired_gold = random.randrange(-50, 51)
        session['gold_amount'] += acquired_gold
        if acquired_gold < 0:
            session['message'].append('Lost '+str(abs(acquired_gold))+ ' gold at the casino! ({:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now()))
        else:
            session['message'].append('Earned '+str(acquired_gold)+ ' gold from the casino! ({:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now()))
    return redirect('/')
@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')

if __name__=="__main__":   
    app.run(debug=True)    