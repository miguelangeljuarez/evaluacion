from flask import Flask, render_template, request, redirect
from functions import comp_tot, vent_net
app = Flask(__name__)


@app.route('/')
def hello()-> '302':
    return redirect('/entry')


@app.route ('/entry')
def entry_page()->'html':
    return render_template('entry.html', the_title='exam_unit2')
@app.route ('/exec_equation', methods=['GET','POST'])
def execute()->'html':
    comps=float((request.form['comps']))
    spends=float((request.form['spends']))
    title='This is the functions result'
    tot=float(comp_tot(comps,spends))
    return render_template('results.html', the_title=title, the_comps=comps, the_spends=spends, the_result=
                           tot)
if __name__=='__main__':
    app.run(debug=True)
    #app.run('localhost', '5001', debug=true)
