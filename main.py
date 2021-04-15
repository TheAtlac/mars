from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/astronaut_selection')
def promotion_image():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1>Анкета претендента</h1>
                            <h2>на участие в миссии</h2>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="email" class="form-control" id="second_name" aria-describedby="emailHelp" placeholder="Введите фамилию" name="second_name">
                                    <input type="email" class="form-control" id="name" placeholder="Введите имя" name="name">
                                    <input type="email" class="form-control" id="email" placeholder="Введите адрес электронной почты" name="email">

                                    <div class="form-class">
                                        <label for="classSelect">Какое у вас образование</label>
                                        <select class="form-control" id="class" name="class">
                                          <option>Начальное</option>
                                          <option>Среднее</option>
                                          <option>Среднее неоконченное</option>
                                          <option>Высшее</option>
                                          <option>Высшее неоконченное</option>
                                        </select>
                                     </div>


                                        <label for="form-check">Укажите профессию</label>
                                    <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="profession" id="Engeneer_explorer" value="Инжинер-исследователь">
                                          <label class="form-check-label" for="Engeneer_explorer">
                                            Инжинер-исследователь
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="profession" id="Engeneer_builder" value="Инжинер-строитель">
                                          <label class="form-check-label" for="Engeneer_builder">
                                            Инжинер-строитель
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="profession" id="Pilot" value="Пилот" >
                                          <label class="form-check-label" for="Pilot">
                                            Пилот
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="profession" id="Meteorologist" value="Метеоролог">
                                          <label class="form-check-label" for="Meteorologist">
                                            Метеоролог
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="profession" id="Engeneer_life" value="Инжинер по жизнеобеспечению">
                                          <label class="form-check-label" for="Engeneer_life">
                                            Инжинер по жизнеобеспечению
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="profession" id="Engeneer_radiation" value="Инжинер по радиационной защите">
                                          <label class="form-check-label" for="Engeneer_radiation">
                                            Инжинер по радиационной защите
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="profession" id="Doctor" value="Врач">
                                          <label class="form-check-label" for="Doctor">
                                            Врач
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="profession" id="Ecobiologist" value="Экобиолог">
                                          <label class="form-check-label" for="Ecobiologist">
                                            Экобиолог
                                          </label>
                                        </div>
                                    </div>
                                    </form>
                                <form class="login_form" method="post">
                                        <label for="form-check">Укажите пол</label>
                                    <div class="form-check2">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male">
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>

                                    <div class="form-group">
                                        <label for="about">Почему вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>

                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>

                                    <div class="form-group">
                                    <div class="form-group form-check">
                                        <input type="radio" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на марсе</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['name'])
        print(request.form['second_name'])
        print(request.form['email'])
        print(request.form['class'])
        print(request.form['profession'])
        print(request.form['sex'])
        print(request.form['about'])
        print(request.form['accept'])
        # print(request.form['file'])
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
