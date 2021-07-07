from flask import Flask, request, render_template, send_file, session, redirect, url_for
import pandas as pd
import Model
import flask_excel as excel
import os
import helper


app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config["USE_X_SENDFILE"] = True


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # print(request.files['file'])
        f = request.files['file']
        data_xls = pd.read_excel(f)
        res = Model.predict(data_xls)
        dict_obj = res.to_dict('list')
        session['data'] = dict_obj
        session['filename'] = f.filename
        session.modified = True
        # print(session.items())
        # return redirect(url_for('download_file'))
        return render_template('index.html', tables=[res.to_html()], titles=res.columns.values)
    return render_template('index.html')


@app.route('/download')
def download_file():
    dict_obj = session["data"]
    key_order = ["Question", "Variation", "Answer", "Recommendation", "Cards", "Images", "Videos", "Entity", "Context",
                 "Main Category", "Callback Param", "Is Static Response"]
    sorted_dictionary = helper.custom_sort(dict_obj, key_order)
    filename = session.get("filename")
    return excel.make_response_from_dict(sorted_dictionary, file_type='xls', file_name=filename)


if __name__ == "__main__":
    excel.init_excel(app)
    app.run(host='0.0.0.0', debug=True, port=8000, use_reloader=False)
