def famous_writer(question,data):
     inf= input(question)
     while inf != data:
        print("Не верно")
        inf = input(question)
     print('Верно')
famous_writer(question= 'Введите год рождения А.С.Пушкина :',data='1799')
famous_writer(question= 'Введите день рождения А.С.Пушкина :',data='6')


