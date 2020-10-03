from flask import Flask, render_template, request
import requests as req
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def inicio():
    if request.method == 'POST':
        nome = request.form['nome']
        obj_dict = req.get('https://api.github.com/users/%s' % nome)
        dict_ = dict(obj_dict.json())
        
        try:
            repos = req.get(dict_['repos_url'])
            dict_['repos'] = repos.json()
        except:
            pass

        try:
            seguindo = req.get(dict_['following_url'])
            seguidor = req.get(dict_['followers_url'])
            dict_['seguindo'] = seguindo.json()
            dict_['seguidor'] = seguidor.json()
            print(dict_['seguindo'])
            print('-----------------------------------------------------------------------------')
            print(dict_['seguidor'])
        except:
            pass
        
        try:
            if dict_['message'] == 'Not Found':
                msg = dict({'msg': 'perfil não encontrado!'})
                return render_template('index.html', msg=msg)
        except:
            return render_template('index.html', dict_=dict_)
    return render_template('index.html')