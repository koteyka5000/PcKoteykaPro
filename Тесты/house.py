# def build_roof(r, rc):
#     """
#     :param r: data for build roof
#     :param rc: data for roof color
#     :return: bool
#     """
#     return True
#     pass
#
#
# def build_walls(r, rc):
#     """
#     :param r: data for build walls
#     :param rc: data for walls color
#     :return: bool
#     """
#     return True
#     pass
#
#
# def build_door(r, rc):
#     """
#     :param r: data for build door
#     :param rc: data for door color
#     :return: bool
#     """
#     return True
#     pass
#
# def build_house(dream, color):
#     house = False
#     roof_color = colors[0]
#     house_color = colors[1]
#     door_color = colors[2]
#     roof = dream[0]
#     walls = dream[1]
#
#     while not house:
#         root_status = build_roof(roof, roof_color)
#         walls_status = build_walls(walls, house_color)
#         door_status = build_door(door_color, door_color)
#         if root_status and walls_status and door_status:
#             house = True
#             print('Дом построен')
#     return house
#
#
# idea = ('roof', 'walls')
# colors = ('red', 'white', 'blue')
# build_house(idea, colors)

def calc_saving(q, w, e):
    m = int(w)
    for i in range(e):
        m += m * (int(q) / 100)
    return m


prosent = float(input("Процент: "))
money = int(input("Деньги: "))
years = int(input('Время: '))
print(calc_saving(prosent, money, years))