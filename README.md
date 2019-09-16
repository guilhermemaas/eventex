# Eventex

Sistema de Eventos.

## Como desenvolver?

1. Clone o repositorio.
2. Crie um virtualenv com Python 3.5.
3. Ative o virtualenv.
4. Instale as dependencias.
5. Configure a instancia com o .env.
6. Execute os testes.

```console
git clone git@github.com:guilhermemaas/eventex/git wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -requirements.txt
cp contrib/env-sample .env
python manage.py test
```
## Como fazer o deploy?

1. Crie uma instancia no Heroku.
2. Envie as configuracoes para o Heroku.
3. Defina uma SECRET_KEY segura para a instancia.
4. Defina DEBUG=False
5. Configure o servico de email.
6. Envie o codigo para o Heroku.

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
# configuro o -email
git push heroku master --force
```
