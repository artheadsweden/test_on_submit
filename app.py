import json

from flask import Flask, request, render_template, url_for, redirect

app = Flask(__name__)

countries = None

@app.get('/')
def index_get():  # put application's code here
    return render_template('index.html')


@app.post('/')
def index_post():
    # PLockar upp det gömda input-fältet
    the_list = request.form['the_list']
    # Har en global variabel, men här kan du spara i databasen
    global countries
    # Låter listan med valda länder hamna i den globala listan
    countries = json.loads(the_list)
    # Skickar vidare till nästa sida
    return redirect(url_for('other_get'))


@app.get('/other')
def other_get():
    # Rendera sidan och skicka med listan med länder
    return render_template('other.html', countries=countries)

if __name__ == '__main__':
    app.run()
