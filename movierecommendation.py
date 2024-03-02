from flask import Flask, render_template, request
import pickle


app = Flask(__name__)


# Load the similarity matrix
with open("C:\Users\susha\OneDrive\Desktop\similarity_matrix\similarity_matrix.pickle", 'rb') as file:
    loaded_similarity = pickle.load(file)

# Load the newdf dataframe

with open("C:\Users\susha\OneDrive\Desktop\similarity_matrix\similarity_matrix.pickle", 'rb') as file:
    loaded_newdf = pickle.load(file)


def recommend(movie):
    if movie not in loaded_newdf['title'].values:
        return "Please enter a different movie name."
    movie_index=loaded_newdf[loaded_newdf['title']==movie].index[0]
    distances=loaded_similarity[movie_index]
    recommendd_moevies=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:9]
    x=[]
    for i in recommendd_moevies:
        x.append(loaded_newdf.iloc[i[0]].title)
    return x

@app.route('/', methods=['GET', 'POST'])
def index():
    recommendations = None
    if request.method == 'POST':
        movie_input = request.form['movie_input']
        recommendations = recommend(movie_input)

    return render_template('index.html', recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
