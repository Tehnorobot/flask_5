from flask import Flask, url_for, request

app = Flask(__name__)
  
    
def show_file(name_file):
     return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style3.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1 Align=center>Загрузка фотографии</h1>
                            <h2 Align=center>для участия в миссии</h2>
                            <div>
                                <form class="login_form" method="post">
                                <h1>Загрузим файл</h1>
                                <form method="post" enctype="multipart/form-data">
                                   <div class="form-group">
                                        <label for="photo">Выберите файл</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                        <img src="static\img\{name_file}">
                                    </div>
                                <button type="submit" class="btn btn-primary">Обновить</button>
                            </form>
                            </div>
                          </body>
                        </html>'''                      
                        

@app.route('/sample_file_upload2', methods=['POST', 'GET'])

def sample_file_upload2(name_file='file_o.png'):
    if request.method == 'GET':
        return show_file(name_file)
                        
    elif request.method == 'POST':
        name_file = request.form['file']
        return show_file(name_file)

                        
if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')