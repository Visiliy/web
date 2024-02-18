import os
import pygame
import requests

x, y = 0.2, 0.2
k = 1
kor1 = 30.304909
kor2 = 59.917966
color1 = (0, 205, 255)
color2 = (0, 205, 255)
color3 = (0, 205, 255)
color4 = (255, 200, 0)
color5 = (255, 235, 0)
color6 = (255, 235, 0)
true = True
regum = 'map'
text2 = ''

pygame.init()
screen = pygame.display.set_mode((600, 650))

running = True
FLAG1 = True
FLAG2 = False
user_text = ''

while running:
    if FLAG1:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                pos1, pos2 = event.pos
                if pos1 >= 445 and pos1 <= 565 and pos2 >= 196 and pos2 <= 234:
                    color4 = (255, 160, 0)
                else:
                    color4 = (255, 200, 0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos1, pos2 = event.pos
                if pos1 >= 445 and pos1 <= 565 and pos2 >= 196 and pos2 <= 234 and user_text not in ('', 'Ошибка!'):
                    try:
                        geocoder_request = f"http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={user_text}&format=json"
                        response = requests.get(geocoder_request)
                        json_response = response.json()
                        toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
                        toponym_coodrinates = toponym["Point"]["pos"]
                        top = toponym_coodrinates.split()
                        url = f'https://geocode-maps.yandex.ru/1.x?geocode={kor1},{kor2}&apikey=40d1649f-0493-4b70-98ba-98533de7710b&format=json'
                        response = requests.get(url)
                        json = response.json()
                        pos = json['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
                        full_address = json['response']['GeoObjectCollection']['featureMember'][
                            0]['GeoObject']['metaDataProperty']['GeocoderMetaData']['text']
                        toponym_address = toponym["metaDataProperty"]["GeocoderMetaData"]["text"]
                        text2 = toponym_address
                        kor1, kor2 = float(top[0]), float(top[1])
                        stat_kor1, stat_kor2 = float(top[0]), float(top[1])
                        FLAG1 = False
                        FLAG2 = True
                        user_text = ''
                    except:
                        user_text = 'Ошибка!'
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                elif len(user_text) < 25:
                    sim = event.unicode
                    user_text += sim
        fon1 = pygame.font.Font(None, 70)
        fon2 = pygame.font.Font(None, 40)
        rend_1 = fon1.render('New Maps', 0, (0, 255, 0))
        screen.blit(rend_1, (180, 50))
        pygame.draw.rect(screen, (255, 255, 255), ((20, 200), (400, 30)), width=0)
        pygame.draw.rect(screen, (255, 200, 0), ((16, 196), (408, 38)), width=4)
        pygame.draw.rect(screen, color4, ((445, 196), (120, 38)), width=0)
        rend_2 = fon2.render(user_text, 0, (0, 0, 0))
        rend_3 = fon2.render('Найти', 0, (0, 0, 0))
        screen.blit(rend_2, (25, 202))
        screen.blit(rend_3, (465, 202))
        pygame.display.flip()

    if FLAG2:
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                pos1, pos2 = event.pos
                if 30 <= pos1 <= 160 and 480 <= pos2 <= 520:
                    color1 = (0, 50, 255)
                    color2 = (0, 205, 255)
                    color3 = (0, 205, 255)
                    color5 = (255, 235, 0)
                    color6 = (255, 235, 0)
                elif 235 <= pos1 <= 365 and 480 <= pos2 <= 520:
                    color2 = (0, 50, 255)
                    color1 = (0, 205, 255)
                    color3 = (0, 205, 255)
                    color5 = (255, 235, 0)
                    color6 = (255, 235, 0)
                elif 440 <= pos1 <= 570 and 480 <= pos2 <= 520:
                    color3 = (0, 50, 255)
                    color1 = (0, 205, 255)
                    color2 = (0, 205, 255)
                    color5 = (255, 235, 0)
                    color6 = (255, 235, 0)
                elif 30 <= pos1 <= 365 and 540 <= pos2 <= 580:
                    color1 = (0, 205, 255)
                    color2 = (0, 205, 255)
                    color3 = (0, 205, 255)
                    color5 = (255, 200, 0)
                    color6 = (255, 235, 0)
                elif 440 <= pos1 <= 570 and 540 <= pos2 <= 580:
                    color1 = (0, 205, 255)
                    color2 = (0, 205, 255)
                    color3 = (0, 205, 255)
                    color5 = (255, 235, 0)
                    color6 = (255, 200, 0)
                else:
                    color1 = (0, 205, 255)
                    color2 = (0, 205, 255)
                    color3 = (0, 205, 255)
                    color5 = (255, 235, 0)
                    color6 = (255, 235, 0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos1, pos2 = event.pos
                if 30 <= pos1 <= 160 and 480 <= pos2 <= 520:
                    regum = 'map'
                elif 440 <= pos1 <= 570 and 480 <= pos2 <= 520:
                    regum = 'sat'
                elif 235 <= pos1 <= 365 and 480 <= pos2 <= 520:
                    regum = 'sat,skl'
                elif 30 <= pos1 <= 365 and 540 <= pos2 <= 580:
                    FLAG2 = False
                    FLAG1 = True
                    true = True
                    text2 = ''
                    x, y = 0.2, 0.2
                elif 440 <= pos1 <= 570 and 540 <= pos2 <= 580:
                    true = False
                    text2 = ''

        s = pygame.key.get_pressed()
        if s[pygame.K_PAGEUP]:
            if x < 10 and y < 10:
                if x < 0.1 and y < 0.1:
                    x, y = x + 0.001, y + 0.001
                elif x < 0.3 and y < 0.3:
                    x, y = x + 0.03, y + 0.03
                else:
                    x, y = x + 0.1, y + 0.1
        elif s[pygame.K_PAGEDOWN]:
            if x > 0.001 and y > 0.001:
                if x < 0.1 and y < 0.1:
                    x, y = x - 0.001, y - 0.001
                elif x < 0.3 and y < 0.3:
                    x, y = x - 0.03, y - 0.03
                else:
                    x, y = x - 0.1, y - 0.1
        elif s[pygame.K_UP]:
            if kor2 < 60:
                if x < 0.03:
                    kor2 += 00.002000
                elif x < 0.2:
                    kor2 += 00.008000
                elif x < 1:
                    kor2 += 00.012000
                else:
                    kor2 += 00.050000
        elif s[pygame.K_DOWN]:
            if kor2 > -60:
                if x < 0.03:
                    kor2 -= 00.002000
                elif x < 0.2:
                    kor2 -= 00.008000
                elif x < 1:
                    kor2 -= 00.012000
                else:
                    kor2 -= 00.050000
        elif s[pygame.K_RIGHT]:
            if x < 0.03:
                kor1 += 00.002000
            elif x < 0.2:
                kor1 += 00.008000
            elif x < 1:
                kor1 += 00.012000
            else:
                kor1 += 00.050000
        elif s[pygame.K_LEFT]:
            if x < 0.03:
                kor1 -= 00.002000
            elif x < 0.2:
                kor1 -= 00.008000
            elif x < 1:
                kor1 -= 00.012000
            else:
                kor1 -= 00.050000

        org_point = "{0},{1}".format(stat_kor1, stat_kor2)

        map_params = {
            "pt": "{0},pm2dgl".format(org_point)
        }
        map_request = f"http://static-maps.yandex.ru/1.x/?ll={kor1},{kor2}&spn={x},{y}&l={regum}"
        if true:
            response = requests.get(map_request, params=map_params)
        else:
            response = requests.get(map_request)
        map_file = "map.png"
        with open(map_file, "wb") as file:
            file.write(response.content)
        screen.blit(pygame.image.load(map_file), (0, 0))
        df = pygame.font.Font(None, 40)
        btn1 = 'Схема'
        btn2 = 'Гибрид'
        btn3 = 'Спутник'
        btn4 = 'На главную'
        btn5 = 'Сброс'
        text = 'Адрес: '
        rend1 = df.render(btn1, 0, (0, 0, 0))
        pygame.draw.rect(screen, color1, ((30, 480), (130, 40)), width=0)
        screen.blit(rend1, (53, 487))
        rend2 = df.render(btn2, 0, (0, 0, 0))
        pygame.draw.rect(screen, color2, ((235, 480), (130, 40)), width=0)
        screen.blit(rend2, (248, 487))
        rend3 = df.render(btn3, 0, (0, 0, 0))
        pygame.draw.rect(screen, color3, ((440, 480), (130, 40)), width=0)
        screen.blit(rend3, (450, 487))
        rend4 = df.render(btn4, 0, (0, 0, 0))
        pygame.draw.rect(screen, color5, ((30, 540), (335, 40)), width=0)
        screen.blit(rend4, (116, 547))
        pygame.draw.rect(screen, color6, ((440, 540), (130, 40)), width=0)
        rend5 = df.render(btn5, 0, (0, 0, 0))
        screen.blit(rend5, (465, 547))
        df2 = pygame.font.Font(None, 25)
        rend6 = df2.render(text, 0, (0, 0, 0))
        rend7 = df2.render(text2, 0, (0, 0, 0))
        screen.blit(rend6, (30, 610))
        screen.blit(rend7, (95, 610))
        pygame.display.flip()
        os.remove(map_file)

pygame.quit()