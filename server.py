
#pobieranie zdjecia
# wyciagniecie ze zdjeica danych za pomoca numpy
import os

from flask import Flask, render_template, request
from forms import AddFileForm
from flask_bootstrap import Bootstrap5

app= Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('FLASK_KEY','12345')
bootstrap=Bootstrap5(app)




@app.route('/',methods=['POST','GET'])
def home():
    add_file_form=AddFileForm()
    if add_file_form.validate_on_submit():
        file=request.form['file']
        print(file)
    return render_template('index.html', form=add_file_form)

if __name__=='__main__':
    app.run(debug=True,port=5001)