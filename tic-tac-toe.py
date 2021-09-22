pole = [i for i in range(1, 11)] # собираем доску
player1 = 0
player2 = 0
player1_hody = []
player2_hody = []
b = True
kolhod = 0 # счетчик ходов игроков
uspekh = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]] # выйгрышные комбинации ячеек

def igra(new_pole): # обновлялка доски
    for i in range(0, 9, 3):
        print('|', new_pole[i], '|',new_pole[i + 1], '|', new_pole[i + 2], '|')
igra(pole) # собираем поле

player1 = int(input('X. Ход игрока 1. Введите номер ячейки'))
player2 = int(input('O. Ход игрока 2. Введите номер ячейки'))

while kolhod < 5 and b: # цикл с игрой
   if player1 > 0 and player1 < 10 and player2 > 0 and player2 < 10: # проверка что оба игрока попали ходом в игровую доску
      if player1 not in player1_hody and player1 not in player2_hody and player2 not in player1_hody and player2 not in player2_hody and player1 != player2: # проверка что оба игрока не сходили в занятую ячейку
               kolhod += 1
               player1_hody += [player1]
               pole.insert(player1 - 1, 'X')
               pole.pop(player1)
               for e in uspekh: # цикл в цикле, чтобы из ходов игрока 1 попробовать сложить выйгрышную комбинацию ячеек
                    if b == False:
                         break
                    schet_uspeh = 0
                    for c in player1_hody:
                         if c in e:
                            schet_uspeh += 1 #если в списке ходов есть успешная комбинация, счетчик дойдет до 3
                         if schet_uspeh == 3:
                            print('Победил игрок 1')
                            b = False
                            break
               if schet_uspeh != 3: #проверка, что игрок 1 не сложил успешную комбинацию
                  player2_hody += [player2]
                  pole.insert(player2 - 1, 'O')
                  pole.pop(player2)
                  for z in uspekh: # цикл в цикле, чтобы из ходов игрока 2 попробовать сложить выйгрышную комбинацию ячеек
                     schet_uspeh = 0
                     for x in player2_hody:
                            if x in z:
                               schet_uspeh += 1
                               if schet_uspeh == 3:
                                 print('Победил игрок 2')
                                 b = False
                                 break
      else:
         print('Ячейка занята')
   else:
      print('Нет такой ячейки')
   if len(player1_hody) == 4: # зайдем сюда, если останется пустой только одна ячейка на поле (знаю, что костыль, пардон)
       igra(pole)
       player1 = int(input('X. Ход игрока 1. Введите номер ячейки'))
       if player1 > 0 and player1 < 10 and player2 > 0 and player2 < 10:
           if player1 not in player1_hody and player1 not in player2_hody and player1 != player2:
               kolhod += 1
               player1_hody += [player1]
               pole.insert(player1 - 1, 'X')
               pole.pop(player1)
               for p in uspekh:
                   if b == False:
                       break
                   schet_uspeh = 0
                   for l in player1_hody:
                       if l in p:
                           schet_uspeh += 1
                       if schet_uspeh == 3:
                           print('Победил игрок 1')
                           b = False
                           break
   else:
       igra(pole) #рисуем доску со сделанными ходами
       player1 = int(input('X. Ход игрока 1. Введите номер ячейки'))
       player2 = int(input('O. Ход игрока 2. Введите номер ячейки'))

if schet_uspeh == 3:
    print('Игра окончена')
else:
    print('Игра окончена. Ничья')
igra(pole)
