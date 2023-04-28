from flask import Flask, request, render_template
import datetime, io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    nome = request.form['nome']
    data = datetime.datetime.now().strftime('%d/%m/%Y')

    # Salvar os dados em um arquivo de texto
    with io.open('log.txt', 'a', encoding='utf-8') as f:
        f.write(f"Nome: {nome} Data: {data} \n")

    return render_template('submit.html', nome=nome, data=data)

if __name__ == '__main__':
    app.run(debug=True)