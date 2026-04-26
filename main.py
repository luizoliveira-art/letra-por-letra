from flask import Flask, request, Response, stream_with_context
import time

app = Flask(__name__)

@app.route('/')
def homepage():
    return '''
    <form action="/temporario" method="GET">
        <input name="msg" placeholder="Digite sua frase" required>
        <button type="submit">Mostrar</button>
    </form>
    '''

@app.route('/temporario')
def temporario():
    msg = request.args.get('msg', '')
    
    if not msg:
        return 'Nenhuma mensagem. <a href="/">Voltar</a>'
    
    def gerar():
        yield '<h2>Mensagem:</h2><p style="font-size:24px; font-family:monospace;">'
        for letra in msg:
            yield letra
            time.sleep(1) 
        yield '</p><br><a href="/">Voltar</a>'
    
    return Response(stream_with_context(gerar()), mimetype='text/html')

if __name__ == '__main__':
    app.run(debug=True)

# cd letra-por-letra, cd flask, python3 main.py