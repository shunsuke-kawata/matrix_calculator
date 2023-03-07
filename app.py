from flask import Flask,render_template,redirect,url_for,request
from crypt import methods
import os
import numpy as np


#行列をHTMLから取得するための関数
def matrix_calculation(row,column,key):
    matrix=np.zeros([row,column])
    for i in range(0,row):
        for j in range(0,column):
            matrix[i][j]=(float)(request.form.get(key+'_'+str(i)+'_'+str(j)))

    return matrix;


app = Flask(__name__)           #アプリ作成

@app.route("/",methods=['GET'])
def index():
    if (request.method == 'GET'):
        return render_template("index.html")
        

@app.route("/calculate",methods=['GET','POST'])
def calculate():
    if (request.method == 'POST'):
        A_row = [i for i in range((int)(request.form.get('A_row')))]
        A_column = [j for j in range((int)(request.form.get('A_column')))]
        B_row = [k for k in range((int)(request.form.get('B_row')))]
        B_column = [l for l in range((int)(request.form.get('B_column')))] #0,1,2...のリストを作成

        return render_template("/calculate.html",A_row=A_row,A_column=A_column,B_row=B_row,B_column=B_column)    #それぞれの行数、列数が引数
    else:
        return render_template("/calculate.html")

@app.route("/result",methods=['GET','POST'])
def result():
    if (request.method == 'POST'):
        A_row=(int)(request.form.get('A_r_len'))
        A_column=(int)(request.form.get('A_c_len'))
        B_row=(int)(request.form.get('B_r_len'))
        B_column=(int)(request.form.get('B_c_len'))
        
        matrix_A = matrix_calculation(A_row,A_column,'A')
        matrix_B = matrix_calculation(B_row,B_column,'B')


        matrix_AB = np.zeros([A_row,B_column])
        row_AB = [i for i in range(0,A_row)]
        column_AB = [i for i in range(0,B_column)]
        for i in range(0,A_row):
            for j in range(0,B_column):
                for k in range(0,A_column):
                    matrix_AB[i][j]+=matrix_A[i][k]*matrix_B[k][j];
        print(matrix_AB)#ターミナルに計算結果を出力

        return render_template("/result.html",matrix_AB=matrix_AB,column_AB=column_AB,row_AB=row_AB)  #行列、行数、列数が引数
    else:
        return render_template("/result.html")

"""
@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)
"""

if __name__=='__main__':
    app.run(debug=True)