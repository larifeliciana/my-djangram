## Djangram
Minha versão do sistema desenvolvido para o curso de Django da Jornada de Cursos do CITI-CIN/UFPE. 
O Djangram é uma rede social inspirada no Instagram e desenvolvida utilizando o framework Django, HTML e CSS.


## Como utilizar
* Clona repositório
  ```bash
  $ git clone https://github.com/larifeliciana/my-djangram
  $ cd my-djangram
  ```
* Preparando o ambiente virtual
  ```bash
  $ python3 -m venv env
  $ source env/bin/activate
  $ pip install -r requirements.txt
  ```
* Roda as migrações
  ```bash
  $ python manage.py migrate
  ```
* Inicia o servidor
  ```bash
  $ python manage.py runserver
  ```
 * Editar Settings
  Nos campos abaixo adicione seu e-mail e senha
  ```
  EMAIL_HOST_USER = ''
  EMAIL_HOST_PASSWORD =''
```
 Links úteis:
 
 * https://github.com/pamella/djangram/
 
 * https://github.com/vintasoftware/django-templated-email/
 
* https://www.treinaweb.com.br/blog/deploy-de-uma-aplicacao-django-no-heroku/
 
* https://medium.com/@BennettGarner/deploying-django-to-heroku-connecting-heroku-postgres-fcc960d290d1
 
* https://medium.com/@johngrant/deploying-a-django-app-to-heroku-226eed92d1e5
