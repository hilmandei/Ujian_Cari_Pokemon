from flask import Flask, send_from_directory, render_template, request, redirect, url_for
import json
import requests

app = Flask(__name__, static_url_path='')

@app.route('/')
def welcome():
    return render_template('welcomeujian.html')


@app.route('/hasil', methods=['POST'])
def hasil():
    try:
        nama = request.form['nama']
        print('"Yang diinput dr Web: " Nama :', nama)

        if nama == "":
            return render_template('pokemonerror.html')

        else:
            url2 = 'https://pokeapi.co/api/v2/pokemon/'+nama
            pokemon = requests.get(url2)
            id = pokemon.json()["id"]
            nama2 = pokemon.json()["name"]
            tinggi = pokemon.json()["height"]
            berat = pokemon.json()["weight"]
            foto2= "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/"+str(id)+".png"
            print(id)
            print(nama2)
            print(tinggi)
            print(berat)
            print('========')

            return render_template ('profilepokemon.html', a=nama2, b=id, c=tinggi, d=berat, e=foto2)

    except(ValueError):
        return redirect(url_for('error'))
    except() :
        return redirect(url_for('error'))


@app.route('/error')
def error():
    return render_template('pokemonerror.html')



if __name__ == '__main__':
    app.run(debug=True)