from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLabel,
                              QApplication, QMessageBox, QRadioButton,
                               QHBoxLayout, QGroupBox, QPushButton, QButtonGroup)
from random import randint, shuffle

class Question():
    def __init__(self, question1, right_answer, wrong1, wrong2, wrong3):
        self.question1 = question1
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Question("На каком языке говорят в Бразилии?", 'Португальский', 'Английский', 'Бразильский', 'Итальянский'))
question_list.append(Question('Что мы изучаем в Алгоритмике?', 'Программирование', 'Математику', 'Строительство', 'Дизайн'))
question_list.append(Question('Какой самый большой материк?', 'Евразия', 'Австралия', 'Африка', 'Южная америка'))
question_list.append(Question('Какая планета Солнечной системы является самой горячей?', 'Венера', 'Меркурий', 'Марс', 'Юпитер'))
question_list.append(Question('Какой химический элемент является самым распространенным во Вселенной?', 'Водород', 'Кислород', 'Гелий', 'Железо'))
question_list.append(Question('Какой город является официальной столицей Австралии?', 'Канберра', 'Сидней', 'Мельбурн', 'Брисбен'))
question_list.append(Question('В какой стране находится самое глубокое озеро в мире — Байкал?', 'Россия', 'Канада', 'Китай', 'США'))
question_list.append(Question('Кто написал знаменитый роман «Преступление и наказание»?', 'Фёдор Достоевский', 'Лев Толстой', 'Антон Чехов', 'Александр Пушкин'))
question_list.append(Question('Какое человеческое чувство или орган поражает вирус COVID-19 при развитии аносмии?', 'Обоняние', 'Зрение', 'Слух', 'Осязание'))
question_list.append(Question('Какой цвет имеют чернила у осьминогов, которые они выбрасывают в воду в случае опасности?', 'Коричневый', 'Синий', 'Фиолетовый', 'Черный'))
question_list.append(Question('Какой химический элемент является самым редким в земной коре?', 'Астат', 'Франций', 'Технеций', 'Прометий'))
question_list.append(Question('Какая птица способна летать задом наперед и даже вверх ногами благодаря уникальному строению крыльев?', 'Колибри', 'Попугай', 'Сова', 'Стриж'))
question_list.append(Question('Какой предмет одежды изначально был создан для ковбоев и золотоискателей, так как нуждался в прочной ткани, а сегодня есть в гардеробе практически у каждого человека?', 'Джинсы', 'Косуха', 'Шляпа-федора', 'Берцы'))


def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    button.setText('Следующий вопрос')

def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    button.setText('Ответить')
    GroupBox.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    GroupBox.setExclusive(True)

def ask(q):
    shuffle(answers)
    question.setText(q.question1)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правда')
        window.score += 1
        print('Статистика\n-Всего вопросов: ', window.total, '\n=Правильных ответов: ', window.score)
        print('Рейтинг: ', (window.score/window.total*100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        # неправильный ответ!
            show_correct('Неверно')
            print('Рейтинг ', (window.score/window.total*100), '%')

def next_question():
    ''' задает случайный вопрос из списка '''
    window.total += 1
    print('Статистика\n-Всего вопросов: ', window.total, '\n=Правильных ответов: ', window.score)
    cur_question = randint(0, len(question_list) - 1)   # нам нужны старое значение, 
                                                        # поэтому можно использовать локальную перменную!
            # случайно взяли вопрос в пределах списка
            # если внести около сотни слов, то редко будет повторяться
    q = question_list[cur_question] # взяли вопрос
    ask(q) # спросили
    
def click_ok():
    if button.text() =='Ответить':
        check_answer()
    else:
        next_question()



app = QApplication([])
window = QWidget()
window.resize(450, 250)

question = QLabel('Вопрос')

rbtn1 = QRadioButton('Ответ1')
rbtn2 = QRadioButton('Ответ2')
rbtn3 = QRadioButton('Ответ3')
rbtn4 = QRadioButton('Ответ4')

answers = [rbtn1, rbtn2, rbtn3, rbtn4]

GroupBox = QButtonGroup()
GroupBox.addButton(rbtn1)
GroupBox.addButton(rbtn2)
GroupBox.addButton(rbtn3)
GroupBox.addButton(rbtn4)



RadioGroupBox = QGroupBox()

main_group_line = QVBoxLayout()
group_line1 = QHBoxLayout()
group_line2 = QHBoxLayout()

group_line1.addWidget(rbtn1)
group_line1.addWidget(rbtn2)
group_line2.addWidget(rbtn3)
group_line2.addWidget(rbtn4)


main_group_line.addLayout(group_line1)
main_group_line.addLayout(group_line2)

RadioGroupBox.setLayout(main_group_line)


AnsGroupBox = QGroupBox('Результат теста')
lb_result = QLabel('Правда/неправда')
lb_correct = QLabel('Сам верный ответ')

ans_group_line = QVBoxLayout()
ans_group_line.addWidget(lb_result, alignment=(Qt.AlignTop | Qt.AlignLeft))
ans_group_line.addWidget(lb_correct, alignment=Qt.AlignLeft)

AnsGroupBox.setLayout(ans_group_line)

button = QPushButton('Ответить')

main_line = QVBoxLayout()
line1 = QHBoxLayout()
line2 = QHBoxLayout()
line3 = QHBoxLayout()

line1.addWidget(question, alignment=Qt.AlignCenter)
line2.addWidget(RadioGroupBox)
line2.addWidget(AnsGroupBox)
line3.addStretch(2)
line3.addWidget(button, stretch=2)
line3.addStretch(2)
AnsGroupBox.hide()

main_line.addLayout(line1, stretch=2)
main_line.addLayout(line2, stretch=8)
main_line.addStretch(1)
main_line.addLayout(line3, stretch=2)
main_line.addStretch(1)
main_line.addSpacing(5)



window.setLayout(main_line)

window.setStyleSheet('''background-color: white;
                     font-size: 16px;
                     background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, 
                                            stop:0 6a16b8, stop:1 #eabbf0);''')

question.setStyleSheet('''background-color: white;
                     font-size: 16px;
                     background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, 
                                            stop:0 40c983, stop:1 #58456b);
                   color:white''')

rbtn1.setStyleSheet('''background-color: white;
                     font-size: 16px;
                     background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, 
                                            stop:0 40c983, stop:1 #58456b);
                   color:white''')

rbtn2.setStyleSheet('''background-color: white;
                     font-size: 16px;
                     background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, 
                                            stop:0 40c983, stop:1 #58456b);
                   color:white''')

rbtn3.setStyleSheet('''background-color: white;
                     font-size: 16px;
                     background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, 
                                            stop:0 40c983, stop:1 #58456b);
                   color:white''')

rbtn4.setStyleSheet('''background-color: white;
                     font-size: 16px;
                     background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, 
                                            stop:0 40c983, stop:1 #58456b);
                   color:white''')

button.clicked.connect(click_ok)

window.score = 0
window.total = 0
next_question()
window.resize(400, 300)
window.show()
app.exec()






