_author_ = "Ермаченков Кирилл"

import random


class Ticket:
    def __init__(self, name):
        self.released = []
        self.name = name
        self.nums = random.sample([_ for _ in range(1, 91)], 15)
        self.lines = [sorted(random.sample([_ for _ in range(0, 9)], 5)),
                      sorted(random.sample([_ for _ in range(0, 9)], 5)),
                      sorted(random.sample([_ for _ in range(0, 9)], 5))]

    def get_released_nums(self, released):
        self.released = released

    def __str__(self):
        print(f"{'>'*int((25-len(self.name))/2)} {self.name} {'<'*int((25-len(self.name))/2)}")
        i = 0
        sort_nums = sorted(self.nums[0:5]) + sorted(self.nums[5:10]) + sorted(self.nums[10:15])
        for _r in range(0, 3):
            for _c in range(0, 9):
                if _c in self.lines[_r]:
                    if sort_nums[i] not in self.released:
                        print("{:3d}".format(sort_nums[i]), end='')
                    else:
                        print(" --", end='')
                    i += 1
                else:
                    print(end='  ')
            print(end='\n')
        return '_' * 27



class Generator:
    def __init__(self):
        self.released = []

    def __iter__(self):
        return self

    def __next__(self):
        try:
            result = random.choice([_ for _ in range(1, 91) if _ not in self.released])
            self.released.append(result)
            return result
        except IndexError:
            raise StopIteration



while True:
    t_player = Ticket('Игрок')
    t_comp = Ticket('Компьютер')
    game_mode = input('Выберите тип игры: норма(any key)/auto(a) :').lower()

    print(t_player)
    print(t_comp)

    bucket = []
    barrel = Generator()

    for _i in barrel:
        print()
        print(f'Боченок с номером: {_i}\n{"_" * 27}')
        ask = ''
        if game_mode not in ['auto', 'a', 'а']:
            while True:
                ask = input("зачеркнуть(1) / продолжить(2):").lower()
                if ask in ["зачеркнуть", "1", "продолжить", "2"]:
                    break
                else:
                    print('Введено неверное значение, введите корректный номер действия')
        if (ask in ["зачеркнуть", "1"] and _i in t_player.nums) or \
               (ask in ["продолжить", "2"] and _i not in t_player.nums) or (game_mode in ['auto', 'a', 'а']):
            bucket.append(_i)
            print(f'Выбывшие номера: {bucket}')
            t_player.get_released_nums(bucket)
            t_comp.get_released_nums(bucket)
            print(t_player)
            print(t_comp)
        else:
            print()
            print(f'{t_player.name} проиграл')
            break
        if not [_ for _ in t_comp.nums if _ not in bucket]:
            print(f'{t_player.name} проиграл')
            break
        if not [_ for _ in t_player.nums if _ not in bucket]:
            print(f'{t_player.name} выиграл!!!')
            break
    if input('Начать заново? да(1) / нет(any key):').lower() in ['да', 'y', '1']:
        continue
    else:
        break
                
