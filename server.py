
#pobieranie zdjecia
# wyciagniecie ze zdjeica danych za pomoca numpy
import os
from pathlib import Path
from flask import Flask, render_template, request, redirect , url_for , flash
from werkzeug.utils import secure_filename

from forms import AddFileForm
from flask_bootstrap import Bootstrap5

UPLOAD_FOLDER= 'uploaded'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
#czy jest folder
folder_uploaded_files= Path(UPLOAD_FOLDER)
if not folder_uploaded_files.is_dir():
    os.system(f'mkdir {UPLOAD_FOLDER}')


app= Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('FLASK_KEY','12345')
app.config['UPLOAD_FOLDER'] =UPLOAD_FOLDER
bootstrap=Bootstrap5(app)

def allowed_extension(filename:str) -> bool:
    if filename.rsplit('.',1)[1] in ALLOWED_EXTENSIONS:
        return True
    else:
        return False

@app.route('/',methods=['POST','GET'])
def home():
    add_file_form=AddFileForm()
    if add_file_form.validate_on_submit():
        #pobieram plik z formularza
        file = request.files['file_field']

        #jesli pole formularza jest puste to zwracam strone
        if file.filename == '':
            flash('Nie wybrano pliku')
            return redirect(url_for('home'))
        # sprawdzam czy jest dobre rozszerzenie pliku
        if file and allowed_extension(file.filename):
            #ustwawiam bezpiczena nazwe zeby mi nie zepsulo czegos na serwerze
            file_name= secure_filename(file.filename)
            #zapisuje plik
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],file_name))
            flash(f'Plik {file_name} zostal zapisany')
        else:
            flash('Niedozwolone rozszerzenie pliku')
            return redirect(url_for('home'))


    return render_template('index.html', form=add_file_form)

if __name__=='__main__':
    app.run(debug=True,port=5001)