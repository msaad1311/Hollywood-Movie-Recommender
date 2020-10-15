from flask import Flask, request, jsonify, render_template
from flask_cors import CORS, cross_origin
from Recommendation import *

app = Flask(__name__, template_folder='templates')

# @app.route("/", methods=['GET', 'POST'])
# @cross_origin()
# def main():
#     data = reader()
#     sim_model = transformer(data,False,True)
#     if request.method == 'GET':
#         return render_template('index.html')

#     if request.method == 'POST':
#         movie_name = request.form['movie_name']
#         movie_name = movie_name.title()
        
#         if movie_name not in data['original_title'].unique():
#             return render_template('negative.html')
#         else:
#             res=recommendations(movie_name,data,sim_model)
#             return render_template('positive.html', movie_names=res['Title'].tolist(), 
#             director=res['Director'].tolist(), search_name=movie_name)


@app.route("/", methods=['GET', 'POST'])
@cross_origin()
def main():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        movie_name = request.form['movie_name']
        movie_name = movie_name.title()
        res = results(movie_name)
        if not isinstance(res, pd.DataFrame):
            return render_template('negative.html')
        else:
            return render_template('positive.html', movie_names=res['Title'].tolist(), 
            director=res['Director'].tolist(), search_name=movie_name)


if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host='0.0.0.0',port=8080) #for aws this is supposed to be set