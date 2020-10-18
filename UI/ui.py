from flask import Flask,render_template,request
import pandas as pd
import os
import predict
import webbrowser

feature_list = list(pd.read_csv('result.csv'))[3:-3]
app = Flask(__name__)

@app.route("/",methods=["GET", "POST"])
def show_hi():
    if request.method=="GET":
        return render_template("index.html")
    else:
        res = []
        for key in feature_list:
            check = request.form.get(key)
            if check:
                is_checked = True
                res.append(1)
            else:
                is_checked = False
                res.append(0)
        filepath = os.path.abspath('.') + "\\templates\\result.html"
        predict.show_results(res,filepath)
        return render_template("result.html")
        #return str(res)

def main():
    
    if not os.environ.get("WERKZEUG_RUN_MAIN"):
        webbrowser.open_new('http://127.0.0.1:5000/')

    app.run(host="127.0.0.1", port=5000)

if __name__ == "__main__":
    main()
    app.run(debug=True)
