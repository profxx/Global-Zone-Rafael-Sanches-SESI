'''
Aula 22
Instrutor: Alexandre
Data: 02/06/2021
Conteúdo: Desafio - Global Zone
'''
print('=' * 135)
print(' ' * 55, 'Desafio - Global Zone')
print('=' * 135)
print('Bem vindo ao conversor de fusos horários Global Zone!')
print('Primeiramente, escolha um continente no qual está localizado o país desejado para a conversão:')
print('1 - África;')
print('2 - Ásia;')
print('3 - América Central')
print('4 - América do Norte;')
print('5 - América do Sul;')
print('6 - Europa;')
print('7 - Oceania.')
print('=' * 135)
print('NOTA: O programa em questão exibirá o horário padrão de cada país, portanto, o horário de verão não é considerado. Logo, alguns')
print('horários do hemisfério norte podem aparentar errados à primeira vista, porém, deve-se levar a em conta a afirmação anterior.')
print('=' * 135)
continente = input('Insira aqui o número da opção desejada: ')
print('=' * 135)
if continente == '1':
    print('Agora, escolha a região africana na qual localiza-se o país desejado para a conversão:')
    print('1 - África Setentrional (Norte da África);')
    print('2 - África Ocidental (Oeste da África);')
    print('3 - África Central;')
    print('4 - África Oriental (Leste da África);')
    print('5 - África Austral ou África Meridional (Sul da África);')
    print('6 - Países Insulares (Ilhas).')
    print('=' * 120)
    regiao_africana = input('Insira aqui o número da opção desejada: ')
    print('=' * 120)
    if regiao_africana == '1':
        print('Estamos quase acabando, escolha o país desejado para a conversão:')
        print('Marrocos;')
        print('Saara Ocidental;')
        print('Argélia;')
        print('Tunísia;')
        print('Líbia;')
        print('Egito (Porção continental);')
        print('Sudão.')
        print('=' * 120)
        pais_africa_setentrional = input('Insira aqui o nome do país desejado: ')
        print('=' * 120)
        if pais_africa_setentrional == 'Marrocos' or pais_africa_setentrional == 'Saara Ocidental' or pais_africa_setentrional ==  'Argélia' or  pais_africa_setentrional == 'Tunísia':
            hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
            print('=' * 120)
            if 0 <= hb <= 23:
                hr = hb + 4
                if hr >= 24:
                    v = hr - 24
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {v} hora(s) em/no(a) {pais_africa_setentrional}.')
                    print('=' * 120)
                else:
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) em/no(a) {pais_africa_setentrional}.')
                    print('=' * 120)
            else:
                print('Erro:')
                print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
        elif pais_africa_setentrional == 'Líbia' or pais_africa_setentrional == 'Egito' or pais_africa_setentrional == 'Sudão' or pais_africa_setentrional == 'Egito (Porção continental)':
            hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
            print('=' * 120)
            if 0 <= hb <= 23:
                hr = hb + 5
                if hr >= 24:
                    v = hr - 24
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {v} hora(s) em/no(a) {pais_africa_setentrional}.')
                    print('=' * 120)
                else:
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) em/no(a) {pais_africa_setentrional}.')
                    print('=' * 120)
            else:
                print('Erro:')
                print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
        else:
            print('Erro:')
            print(f'Desculpe, {pais_africa_setentrional} não é uma das opções disponíveis.')
    elif regiao_africana == '2':
        print('Estamos quase acabando, escolha o país desejado para a conversão:')
        print('Mauritânia;')
        print('Senegal;')
        print('Gâmbia;')
        print('Guiné-Bissau;')
        print('Guiné')
        print('Serra Leoa;')
        print('Libéria;')
        print('Mali;')
        print('Burkina Faso;')
        print('Costa do Marfim;')
        print('Gana;')
        print('Togo;')
        print('Benim;')
        print('Níger;')
        print('Nigéria.')
        print('=' * 120)
        pais_africa_ocidental = input('Insira aqui o nome do país desejado: ')
        print('=' * 120)
        if pais_africa_ocidental == 'Mauritânia' or pais_africa_ocidental == 'Senegal' or pais_africa_ocidental ==  'Gâmbia' or  pais_africa_ocidental == 'Guiné-Bissau' or pais_africa_ocidental == 'Guiné' or pais_africa_ocidental == 'Serra Leoa' or pais_africa_ocidental == 'Libéria' or pais_africa_ocidental == 'Mali' or pais_africa_ocidental == 'Burkina Faso' or pais_africa_ocidental == 'Costa do Marfim' or pais_africa_ocidental == 'Gana' or pais_africa_ocidental == 'Togo':
            hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
            print('=' * 120)
            if 0 <= hb <= 23:
                hr = hb + 3
                if hr >= 24:
                    v = hr - 24
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {v} hora(s) em/no(a) {pais_africa_ocidental}.')
                    print('=' * 120)
                else:
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) em/no(a) {pais_africa_ocidental}.')
                    print('=' * 120)
            else:
                print('Erro:')
                print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
        elif pais_africa_ocidental == 'Benim' or pais_africa_ocidental == 'Níger' or pais_africa_ocidental ==  'Nigéria':
            hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
            print('=' * 120)
            if 0 <= hb <= 23:
                hr = hb + 4
                if hr >= 24:
                    v = hr - 24
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {v} hora(s) em/no(a) {pais_africa_ocidental}.')
                    print('=' * 120)
                else:
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) em/no(a) {pais_africa_ocidental}.')
                    print('=' * 120)
            else:
                print('Erro:')
                print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
        else:
            print('Erro:')
            print(f'Desculpe, {pais_africa_ocidental} não é uma das opções disponíveis.')
    elif regiao_africana == '3':
        print('Estamos quase acabando, escolha o país desejado para a conversão:')
        print('Chade;')
        print('Camarões;')
        print('República Centro Africana;')
        print('Guiné-Equatorial;')
        print('Gabão')
        print('República do Congo;')
        print('República Democrática do Congo;')
        print('Angola;')
        print('=' * 120)
        pais_africa_central = input('Insira aqui o nome do país desejado: ')
        print('=' * 120)
        if pais_africa_central == 'Chade' or pais_africa_central == 'Camarões' or pais_africa_central == 'Guiné-Equatorial' or pais_africa_central == 'Gabão' or pais_africa_central ==  'República Centro-Africana' or pais_africa_central == 'República do Congo' or pais_africa_central == 'República Democrática do Congo' or pais_africa_central == 'Angola':
            hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
            print('=' * 120)
            if 0 <= hb <= 23:
                hr = hb + 4
                if hr >= 24:
                    v = hr - 24
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {v} hora(s) em/no(a) {pais_africa_central}.')
                    print('=' * 120)
                else:
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) em/no(a) {pais_africa_central}.')
                    print('=' * 120)
            else:
                print('Erro:')
                print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
        else:
            print('Erro:')
            print(f'Desculpe, {pais_africa_central} não é uma das opções disponíveis.')
    elif regiao_africana == '4':
        print('Estamos quase acabando, escolha o país desejado para a conversão:')
        print('Sudão do Sul;')
        print('Eritréia;')
        print('Etiópia;')
        print('Uganda;')
        print('Djibouti;')
        print('Somália;')
        print('Quênia;')
        print('Ruanda;')
        print('Burundi;')
        print('Tanzânia;')
        print('Malawi;')
        print('Zâmbia;')
        print('Zimbábue;')
        print('Moçambique;')
        print('=' * 120)
        pais_africa_oriental = input('Insira aqui o nome do país desejado: ')
        print('=' * 120)
        if pais_africa_oriental == 'Sudão do Sul' or pais_africa_oriental == 'Ruanda' or pais_africa_oriental ==  'Burundi' or pais_africa_oriental == 'Malawi' or pais_africa_oriental == 'Zâmbia' or pais_africa_oriental == 'Zimbábue' or pais_africa_oriental == 'Moçambique':
            hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
            print('=' * 120)
            if 0 <= hb <= 23:
                hr = hb + 5
                if hr >= 24:
                    v = hr - 24
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {v} hora(s) em/no(a) {pais_africa_oriental}.')
                    print('=' * 120)
                else:
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) em/no(a) {pais_africa_oriental}.')
                    print('=' * 120)
            else:
                print('Erro:')
                print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
        elif pais_africa_oriental == 'Eritréia' or pais_africa_oriental == 'Etiópia' or pais_africa_oriental == 'Uganda' or pais_africa_oriental == 'Djibouti' or pais_africa_oriental == 'Somália' or pais_africa_oriental == 'Quênia' or pais_africa_oriental == 'Tanzânia':
            hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
            print('=' * 120)
            if 0 <= hb <= 23:
                hr = hb + 6
                if hr >= 24:
                    v = hr - 24
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {v} hora(s) em/no(a) {pais_africa_oriental}.')
                    print('=' * 120)
                else:
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) em/no(a) {pais_africa_oriental}.')
                    print('=' * 120)
            else:
                print('Erro:')
                print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
        else:
            print('Erro:')
            print(f'Desculpe, {pais_africa_oriental} não é uma das opções disponíveis.')
    elif regiao_africana == '5':
        print('Estamos quase acabando, escolha o país desejado para a conversão:')
        print('Namíbia;')
        print('Botswana;')
        print('África do Sul;')
        print('Lesoto;')
        print('Essuatíni (Antiga Suazilândia);')
        print('=' * 120)
        pais_africa_austral = input('Insira aqui o nome do país desejado: ')
        print('=' * 120)
        if pais_africa_austral == 'Namíbia' or pais_africa_austral == 'Botswana' or pais_africa_austral == 'África do Sul' or pais_africa_austral == 'Lesoto' or pais_africa_austral == 'Essuatíni':
            hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
            print('=' * 120)
            if 0 <= hb <= 23:
                hr = hb + 5
                if hr >= 24:
                    v = hr - 24
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {v} hora(s) em/no(a) {pais_africa_austral}.')
                    print('=' * 120)
                else:
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) em/no(a) {pais_africa_austral}.')
                    print('=' * 120)
            else:
                print('Erro:')
                print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
        else:
            print('Erro:')
            print(f'Desculpe, {pais_africa_austral} não é uma das opções disponíveis.')
    elif regiao_africana == '6':
        print('Estamos quase acabando, escolha o país desejado para a conversão:')
        print('Cabo Verde;')
        print('Comores;')
        print('Madagascar;')
        print('República de Maurício;')
        print('São Tomé e Príncipe;')
        print('Ilhas Seychelles')
        print('=' * 120)
        pais_africa_insular = input('Insira aqui o nome do país desejado: ')
        print('=' * 120)
        if pais_africa_insular == 'Cabo Verde':
            hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
            print('=' * 120)
            if 0 <= hb <= 23:
                hr = hb + 2
                if hr >= 24:
                    v = hr - 24
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {v} hora(s) em/no(a) {pais_africa_insular}.')
                    print('=' * 120)
                else:
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) em/no(a) {pais_africa_insular}.')
                    print('=' * 120)
            else:
                print('Erro:')
                print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
        elif pais_africa_insular == 'Comores' or pais_africa_insular == 'Madagascar':
            hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
            print('=' * 120)
            if 0 <= hb <= 23:
                hr = hb + 6
                if hr >= 24:
                    v = hr - 24
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {v} hora(s) em/no(a) {pais_africa_insular}.')
                    print('=' * 120)
                else:
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) em/no(a) {pais_africa_insular}.')
                    print('=' * 120)
            else:
                print('Erro:')
                print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
        elif pais_africa_insular == 'República de Maurício' or pais_africa_insular == 'Ilhas Seychelles':
            hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
            print('=' * 120)
            if 0 <= hb <= 23:
                hr = hb + 7
                if hr >= 24:
                    v = hr - 24
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {v} hora(s) em/no(a) {pais_africa_insular}.')
                    print('=' * 120)
                else:
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) em/no(a) {pais_africa_insular}.')
                    print('=' * 120)
            else:
                print('Erro:')
                print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
        elif pais_africa_insular == 'São Tomé e Príncipe':
            hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
            print('=' * 120)
            if 0 <= hb <= 23:
                hr = hb + 3
                if hr >= 24:
                    v = hr - 24
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {v} hora(s) em/no(a) {pais_africa_insular}.')
                    print('=' * 120)
                else:
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) em/no(a) {pais_africa_insular}.')
                    print('=' * 120)
            else:
                print('Erro:')
                print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
        else:
            print('Erro:')
            print(f'Desculpe, {pais_africa_insular} não é uma das opções disponíveis.')
    else:
        print('Erro:')
        print(f'Desculpe, {regiao_africana} não é uma das opções disponíveis.')
elif continente == '2':
    print('Agora, escolha a região asiática na qual localiza-se o país desejado para a conversão:')
    print('1 - Ásia Setentrional (Norte da Ásia ou Rússia Oriental);')
    print('2 - Ásia Ocidental ou Oriente Médio (Oeste Asiático);')
    print('3 - Ásia Central;')
    print('4 - Ásia Meridional (Sul da Ásia);')
    print('5 - Sudeste Asiático;')
    print('6 - Extremo Oriente ou Ásia Oriental (Leste Asiático).')
    print('=' * 120)
    regiao_asiatica = input('Insira aqui o número da opção desejada: ')
    print('=' * 120)
    if regiao_asiatica == '1':
        print('Estamos quase acabando, escolha a zona russa desejada para a conversão:')
        print('Zona 4 (Horário Padrão de Yekaterimburgo);')
        print('Zona 5 (Horário Padrão de Omsk);')
        print('Zona 6 (Horário Padrão de Novosibirsk );')
        print('Zona 7 (Horário Padrão de Irkutsk);')
        print('Zona 8 (Horário Padrão de Yakutsk);')
        print('Zona 9 (Horário Padrão de Vladivostok);')
        print('Zona 10 (Horário Padrão de Magadan);')
        print('Zona 11 (Horário Padrão de Petropavlovsk-Kamchatski).')
        print('=' * 120)
        zona = input('Insira aqui o número da Zona desejada: ')
        print('=' * 120)
        if zona == '4':
            hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
            print('=' * 120)
            if 0 <= hb <= 23:
                hr = hb + 8
                if hr >= 24:
                    v = hr - 24
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {v} hora(s)na Zona {zona} russa.')
                    print('=' * 120)
                else:
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) na Zona {zona} russa.')
                    print('=' * 120)
            else:
                print('Erro:')
                print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
        elif zona == '5':
            hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
            print('=' * 120)
            if 0 <= hb <= 23:
                hr = hb + 9
                if hr >= 24:
                    v = hr - 24
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {v} hora(s)na Zona {zona} russa.')
                    print('=' * 120)
                else:
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) na Zona {zona} russa.')
                    print('=' * 120)
            else:
                print('Erro:')
                print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
        elif zona == '6':
            hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
            print('=' * 120)
            if 0 <= hb <= 23:
                hr = hb + 10
                if hr >= 24:
                    v = hr - 24
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {v} hora(s)na Zona {zona} russa.')
                    print('=' * 120)
                else:
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) na Zona {zona} russa.')
                    print('=' * 120)
            else:
                print('Erro:')
                print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
        elif zona == '7':
            hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
            print('=' * 120)
            if 0 <= hb <= 23:
                hr = hb + 11
                if hr >= 24:
                    v = hr - 24
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {v} hora(s)na Zona {zona} russa.')
                    print('=' * 120)
                else:
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) na Zona {zona} russa.')
                    print('=' * 120)
            else:
                print('Erro:')
                print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
        elif zona == '8':
            hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
            print('=' * 120)
            if 0 <= hb <= 23:
                hr = hb + 12
                if hr >= 24:
                    v = hr - 24
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {v} hora(s)na Zona {zona} russa.')
                    print('=' * 120)
                else:
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) na Zona {zona} russa.')
                    print('=' * 120)
            else:
                print('Erro:')
                print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
        elif zona == '9':
            hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
            print('=' * 120)
            if 0 <= hb <= 23:
                hr = hb + 13
                if hr >= 24:
                    v = hr - 24
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {v} hora(s)na Zona {zona} russa.')
                    print('=' * 120)
                else:
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) na Zona {zona} russa.')
                    print('=' * 120)
            else:
                print('Erro:')
                print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
        elif zona == '10':
            hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
            print('=' * 120)
            if 0 <= hb <= 23:
                hr = hb + 14
                if hr >= 24:
                    v = hr - 24
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {v} hora(s)na Zona {zona} russa.')
                    print('=' * 120)
                else:
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) na Zona {zona} russa.')
                    print('=' * 120)
            else:
                print('Erro:')
                print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
        elif zona == '11':
            hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
            print('=' * 120)
            if 0 <= hb <= 23:
                hr = hb + 15
                if hr >= 24:
                    v = hr - 24
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {v} hora(s)na Zona {zona} russa.')
                    print('=' * 120)
                else:
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) na Zona {zona} russa.')
                    print('=' * 120)
            else:
                print('Erro:')
                print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
        else:
            print('Erro:')
            print(f'Desculpe, Zona {zona} não é uma das opções disponíveis.')
    elif regiao_asiatica == '2':
        print('Estamos quase acabando, escolha o país desejado para a conversão:')
        print('Turquia (Península da Anatólia);')
        print('Egito (Península do Sinai);')
        print('Chipre;')
        print('Síria;')
        print('Líbano;')
        print('Israel;')
        print('Jordânia;')
        print('Arábia Saudita')
        print('Iraque;')
        print('Kuwait;')
        print('Bahrein;')
        print('Catar;')
        print('Emirados Árabes Unidos;')
        print('Omã;')
        print('Iêmen;')
        print('Irã.')
        print('=' * 120)
        pais_oriente_medio = input('Insira aqui o nome do país desejado: ')
        print('=' * 120)
        if pais_oriente_medio == 'Egito' or pais_oriente_medio == 'Chipre' or pais_oriente_medio == 'Síria' or pais_oriente_medio == 'Líbano' or pais_oriente_medio == 'Israel' or pais_oriente_medio == 'Jordânia':
            hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
            print('=' * 120)
            if 0 <= hb <= 23:
                hr = hb + 5
                if hr >= 24:
                    v = hr - 24
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {v} hora(s) em/no(a) {pais_oriente_medio}.')
                    print('=' * 120)
                else:
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) em/no(a) {pais_oriente_medio}.')
                    print('=' * 120)
            else:
                print('Erro:')
                print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
        elif pais_oriente_medio == 'Turquia' or pais_oriente_medio == 'Arábia Saudita' or pais_oriente_medio == 'Iraque' or pais_oriente_medio == 'Kuwait' or pais_oriente_medio == 'Bahrein' or pais_oriente_medio == 'Catar' or pais_oriente_medio == 'Iêmen':
            hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
            print('=' * 120)
            if 0 <= hb <= 23:
                hr = hb + 6
                if hr >= 24:
                    v = hr - 24
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {v} hora(s) em/no(a) {pais_oriente_medio}.')
                    print('=' * 120)
                else:
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) em/no(a) {pais_oriente_medio}.')
                    print('=' * 120)
            else:
                print('Erro:')
                print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
        elif pais_oriente_medio == 'Emirados Árabes Unidos' or pais_oriente_medio == 'Omã':
            hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
            print('=' * 120)
            if 0 <= hb <= 23:
                hr = hb + 7
                if hr >= 24:
                    v = hr - 24
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {v} hora(s) em/no(a) {pais_oriente_medio}.')
                    print('=' * 120)
                else:
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) em/no(a) {pais_oriente_medio}.')
                    print('=' * 120)
            else:
                print('Erro:')
                print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
        elif pais_oriente_medio == 'Irã':
            hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
            print('=' * 120)
            if 0 <= hb <= 23:
                hr = hb + 6
                if hr >= 24:
                    v = hr - 24
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {v}:30 hora(s) em/no(a) {pais_oriente_medio}.')
                    print('=' * 120)
                else:
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {hr}:30 hora(s) em/no(a) {pais_oriente_medio}.')
                    print('=' * 120)
            else:
                print('Erro:')
                print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
        else:
            print('Erro:')
            print(f'Desculpe, {pais_oriente_medio} não é uma das opções disponíveis.')
    elif regiao_asiatica == '3':
        print('Estamos quase acabando, escolha o país desejado para a conversão:')
        print('Cazaquistão (Ocidental);')
        print('Cazaquistão (Oriental);')
        print('Quirguistão;')
        print('Tajiquistão;')
        print('Turcomenistão;')
        print('Uzbequistão;')
        print('Afeganistão.')
        print('=' * 120)
        pais_asia_central = input('Insira aqui o nome do país desejado: ')
        print('=' * 120)
        if pais_asia_central == 'Afeganistão':
            hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
            print('=' * 120)
            if 0 <= hb <= 23:
                hr = hb + 7
                if hr >= 24:
                    v = hr - 24
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {v}:30 hora(s) em/no(a) {pais_asia_central}.')
                    print('=' * 120)
                else:
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {hr}:30 hora(s) em/no(a) {pais_asia_central}.')
                    print('=' * 120)
            else:
                print('Erro:')
                print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
        elif pais_asia_central == 'Cazaquistão (Ocidental)' or pais_asia_central == 'Tajiquistão' or pais_asia_central == 'Turcomenistão' or pais_asia_central == 'Uzbequistão':
            hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
            print('=' * 120)
            if 0 <= hb <= 23:
                hr = hb + 8
                if hr >= 24:
                    v = hr - 24
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {v} hora(s) em/no(a) {pais_asia_central}.')
                    print('=' * 120)
                else:
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) em/no(a) {pais_asia_central}.')
                    print('=' * 120)
            else:
                print('Erro:')
                print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
        elif pais_asia_central == 'Cazaquistão (Oriental)' or pais_asia_central == 'Quirguistão':
            hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
            print('=' * 120)
            if 0 <= hb <= 23:
                hr = hb + 9
                if hr >= 24:
                    v = hr - 24
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {v} hora(s) em/no(a) {pais_asia_central}.')
                    print('=' * 120)
                else:
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) em/no(a) {pais_asia_central}.')
                    print('=' * 120)
            else:
                print('Erro:')
                print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
        else:
            print('Erro:')
            print(f'Desculpe, {pais_asia_central} não é uma das opções disponíveis.')
    elif regiao_asiatica == '4':
        print('Estamos quase acabando, escolha o país desejado para a conversão:')
        print('Paquistão;')
        print('Índia;')
        print('Bangladesh;')
        print('Butão;')
        print('Nepal;')
        print('Maldivas;')
        print('Sri Lanka.')
        print('=' * 120)
        pais_asia_meridional = input('Insira aqui o nome do país desejado: ')
        print('=' * 120)
        if pais_asia_meridional == 'Paquistão' or pais_asia_meridional == 'Maldivas':
            hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
            print('=' * 120)
            if 0 <= hb <= 23:
                hr = hb + 8
                if hr >= 24:
                    v = hr - 24
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {v} hora(s) em/no(a) {pais_asia_meridional}.')
                    print('=' * 120)
                else:
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) em/no(a) {pais_asia_meridional}.')
                    print('=' * 120)
            else:
                print('Erro:')
                print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
        elif pais_asia_meridional == 'Índia' or pais_asia_meridional == 'Sri Lanka':
            hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
            print('=' * 120)
            if 0 <= hb <= 23:
                hr = hb + 8
                if hr >= 24:
                    v = hr - 24
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {v}:30 hora(s) em/no(a) {pais_asia_meridional}.')
                    print('=' * 120)
                else:
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {hr}:30 hora(s) em/no(a) {pais_asia_meridional}.')
                    print('=' * 120)
            else:
                print('Erro:')
                print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
        elif pais_asia_meridional == 'Bangladesh' or pais_asia_meridional == 'Butão':
            hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
            print('=' * 120)
            if 0 <= hb <= 23:
                hr = hb + 9
                if hr >= 24:
                    v = hr - 24
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {v} hora(s) em/no(a) {pais_asia_meridional}.')
                    print('=' * 120)
                else:
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) em/no(a) {pais_asia_meridional}.')
                    print('=' * 120)
            else:
                print('Erro:')
                print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
        elif pais_asia_meridional == 'Nepal':
            hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
            print('=' * 120)
            if 0 <= hb <= 23:
                hr = hb + 8
                if hr >= 24:
                    v = hr - 24
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {v}:45 hora(s) em/no(a) {pais_asia_meridional}.')
                    print('=' * 120)
                else:
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {hr}:45 hora(s) em/no(a) {pais_asia_meridional}.')
                    print('=' * 120)
            else:
                print('Erro:')
                print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
        else:
            print('Erro:')
            print(f'Desculpe, {pais_asia_meridional} não é uma das opções disponíveis.')
    elif regiao_asiatica == '5':
        print('Estamos quase acabando, escolha o país desejado para a conversão:')
        print('Brunei;')
        print('Mianmar;')
        print('Camboja;')
        print('Indonésia (Ocidental);')
        print('Indonésia (Central);')
        print('Indonésia (Oriental);')
        print('Malásia;')
        print('Filipinas;')
        print('Singapura;')
        print('Tailândia;')
        print('Vietnã;')
        print('Laos;')
        print('Timor-Leste.')
        print('=' * 120)
        pais_sudeste_asiatico = input('Insira aqui o nome do país desejado: ')
        print('=' * 120)
        if pais_sudeste_asiatico == 'Tailândia' or pais_sudeste_asiatico == 'Laos' or pais_sudeste_asiatico == 'Camboja' or pais_sudeste_asiatico == 'Indonésia (Ocidental)':
            hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
            print('=' * 120)
            if 0 <= hb <= 23:
                hr = hb + 10
                if hr >= 24:
                    v = hr - 24
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {v} hora(s) em/no(a) {pais_sudeste_asiatico}.')
                    print('=' * 120)
                else:
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) em/no(a) {pais_sudeste_asiatico}.')
                    print('=' * 120)
            else:
                print('Erro:')
                print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
        if pais_sudeste_asiatico == 'Mianmar':
            hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
            print('=' * 120)
            if 0 <= hb <= 23:
                hr = hb + 9
                if hr >= 24:
                    v = hr - 24
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {v}:30 hora(s) em/no(a) {pais_sudeste_asiatico}.')
                    print('=' * 120)
                else:
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {hr}:30 hora(s) em/no(a) {pais_sudeste_asiatico}.')
                    print('=' * 120)
            else:
                print('Erro:')
                print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
        elif pais_sudeste_asiatico == 'Indonésia (Central)' or pais_sudeste_asiatico == 'Malásia' or pais_sudeste_asiatico == 'Filipinas' or pais_sudeste_asiatico == 'Brunei' or pais_sudeste_asiatico == 'Singapura':
            hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
            print('=' * 120)
            if 0 <= hb <= 23:
                hr = hb + 11
                if hr >= 24:
                    v = hr - 24
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {v} hora(s) em/no(a) {pais_sudeste_asiatico}.')
                    print('=' * 120)
                else:
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) em/no(a) {pais_sudeste_asiatico}.')
                    print('=' * 120)
            else:
                print('Erro:')
                print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
        elif pais_sudeste_asiatico == 'Vietnã':
            hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
            print('=' * 120)
            if 0 <= hb <= 23:
                hr = hb + 10
                if hr >= 24:
                    v = hr - 24
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {v} hora(s) em/no(a) {pais_sudeste_asiatico}.')
                    print('=' * 120)
                else:
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) em/no(a) {pais_sudeste_asiatico}.')
                    print('=' * 120)
            else:
                print('Erro:')
                print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
        elif pais_sudeste_asiatico == 'Timor leste' or pais_sudeste_asiatico == 'Indonésia (Oriental)':
            hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
            print('=' * 120)
            if 0 <= hb <= 23:
                hr = hb + 12
                if hr >= 24:
                    v = hr - 24
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {v} hora(s) em/no(a) {pais_sudeste_asiatico}.')
                    print('=' * 120)
                else:
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) em/no(a) {pais_sudeste_asiatico}.')
                    print('=' * 120)
            else:
                print('Erro:')
                print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
        else:
            print('Erro:')
            print(f'Desculpe, {pais_sudeste_asiatico} não é uma das opções disponíveis.')
    elif regiao_asiatica == '6':
        print('Estamos quase acabando, escolha o país desejado para a conversão:')
        print('China;')
        print('Japão;')
        print('Coreia do Sul;')
        print('Coreia do Norte;')
        print('Taiwan;')
        print('Hong Kong;')
        print('Mongólia;')
        print('Macau.')
        print('=' * 120)
        pais_extremo_oriente = input('Insira aqui o nome do país desejado: ')
        print('=' * 120)
        if pais_extremo_oriente == 'China' or pais_extremo_oriente == 'Taiwan' or pais_extremo_oriente == 'Hong Kong' or pais_extremo_oriente == 'Macau' or pais_extremo_oriente == 'Mongólia':
            hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
            print('=' * 120)
            if 0 <= hb <= 23:
                hr = hb + 11
                if hr >= 24:
                    v = hr - 24
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {v} hora(s) em/no(a) {pais_extremo_oriente}.')
                    print('=' * 120)
                else:
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) em/no(a) {pais_extremo_oriente}.')
                    print('=' * 120)
            else:
                print('Erro:')
                print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
        elif pais_extremo_oriente == 'Japão' or pais_extremo_oriente == 'Coreia do Norte' or pais_extremo_oriente == 'Coreia do Sul':
            hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
            print('=' * 120)
            if 0 <= hb <= 23:
                hr = hb + 12
                if hr >= 24:
                    v = hr - 24
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {v} hora(s) em/no(a) {pais_extremo_oriente}.')
                    print('=' * 120)
                else:
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) em/no(a) {pais_extremo_oriente}.')
                    print('=' * 120)
            else:
                print('Erro:')
                print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
        else:
            print('Erro:')
            print(f'Desculpe, {pais_extremo_oriente} não é uma das opções disponíveis.')
    else:
        print('Erro:')
        print(f'Desculpe, {regiao_asiatica} não é uma das opções disponíveis.')
elif continente == '3':
    print('Agora, escolha a região mesoamericana na qual localiza-se o país desejado para a conversão:')
    print('1 - Mesoamérica Continental;')
    print('2 - Mesoamérica Insular (Caribe).')
    print('=' * 120)
    regiao_mesoamericana = input('Insira aqui o número da opção desejada: ')
    print('=' * 120)
    if regiao_mesoamericana == '1':
        print('Estamos quase acabando, escolha o país desejado para a conversão:')
        print('Guatemala;')
        print('Belize;')
        print('El Salvador;')
        print('Honduras;')
        print('Nicarágua;')
        print('Costa Rica;')
        print('Panamá.')
        print('=' * 120)
        pais_mesoamerica_continental = input('Insira aqui o nome do país desejado: ')
        print('=' * 120)
        if pais_mesoamerica_continental == 'Guatemala' or pais_mesoamerica_continental == 'Belize' or pais_mesoamerica_continental == 'El Salvador' or pais_mesoamerica_continental == 'Honduras' or pais_mesoamerica_continental == 'Nicarágua' or pais_mesoamerica_continental == 'Costa Rica':
            hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
            print('=' * 120)
            if 0 <= hb <= 23:
                hr = hb - 3
                if hr <= 0:
                    v = hr + 24
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {v} hora(s) em/no(a) {pais_mesoamerica_continental}.')
                    print('=' * 120)
                else:
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) em/no(a) {pais_mesoamerica_continental}.')
                    print('=' * 120)
            else:
                print('Erro:')
                print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
        elif pais_mesoamerica_continental == 'Panamá': 
            hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
            print('=' * 120)
            if 0 <= hb <= 23:
                hr = hb - 2
                if hr <= 0:
                    v = hr + 24
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {v} hora(s) em/no(a) {pais_mesoamerica_continental}.')
                    print('=' * 120)
                else:
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) em/no(a) {pais_mesoamerica_continental}.')
                    print('=' * 120)
            else:
                print('Erro:')
                print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
        else:
            print('Erro:')
            print(f'Desculpe, {pais_mesoamerica_continental} não é uma das opções disponíveis.')
    elif regiao_mesoamericana == '2':
        print('Estamos quase acabando, escolha o país desejado para a conversão:')
        print('Antígua e Barbuda;')
        print('Bahamas;')
        print('Barbados;')
        print('Cuba;')
        print('República Dominicana;')
        print('Granada;')
        print('Haiti;')
        print('Jamaica;')
        print('Porto Rico;')
        print('Dominica;')
        print('Santa Lúcia;')
        print('São Cristóvão e Névis;')
        print('São Vicente e Granadinas.')
        print('=' * 120)
        pais_mesoamerica_insular = input('Insira aqui o nome do país desejado: ')
        print('=' * 120)
        if pais_mesoamerica_insular == 'Antígua e Barbuda' or pais_mesoamerica_insular == 'Bahamas' or pais_mesoamerica_insular == 'Barbados' or pais_mesoamerica_insular == 'Cuba' or pais_mesoamerica_insular == 'República Dominicana' or pais_mesoamerica_insular == 'Granada' or pais_mesoamerica_insular == 'Haiti' or pais_mesoamerica_insular == 'Porto Rico' or pais_mesoamerica_insular == 'Dominica' or pais_mesoamerica_insular == 'Santa Lúcia' or pais_mesoamerica_insular == 'São Cristovão e Névis' or pais_mesoamerica_insular == 'São Vicente e Granadinas':
            hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
            print('=' * 120)
            if 0 <= hb <= 23:
                hr = hb - 1
                if hr <= 0:
                    v = hr + 24
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {v} hora(s) em/no(a) {pais_mesoamerica_insular}.')
                    print('=' * 120)
                else:
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) em/no(a) {pais_mesoamerica_insular}.')
                    print('=' * 120)
            else:
                print('Erro:')
                print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
        elif pais_mesoamerica_insular == 'Jamaica':
            hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
            print('=' * 120)
            if 0 <= hb <= 23:
                hr = hb - 2
                if hr <= 0:
                    v = hr + 24
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {v} hora(s) em/no(a) {pais_mesoamerica_insular}.')
                    print('=' * 120)
                else:
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) em/no(a) {pais_mesoamerica_insular}.')
                    print('=' * 120)
            else:
                print('Erro:')
                print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
        else:
            print('Erro:')
            print(f'Desculpe, {pais_mesoamerica_insular} não é uma das opções disponíveis.')
    else:
        print('Erro:')
        print(f'Desculpe, {regiao_mesoamericana} não é uma das opções disponíveis.')
elif continente == '4':
    print('Estamos quase acabando, escolha o país desejado para a conversão:')
    print('Estados Unidos (Oriental);')
    print('Estados Unidos (Central);')
    print('Estados Unidos (Montanhas);')
    print('Estados Unidos (Pacífico);')
    print('Estados Unidos (Alasca);')
    print('Estados Unidos (Havaí);')
    print('Canadá (Terra-Nova e Labrador);')
    print('Canadá (Atlântico);')
    print('Canadá (Oriental);')
    print('Canadá (Central);')
    print('Canadá (Montanhas);')
    print('Canadá (Pacífico);')
    print('México (Central);')
    print('México (Montanhas);')
    print('México (Pacífico).')
    print('=' * 120)
    regiao_norte_americana = input('Insira aqui o número da opção desejada: ')
    print('=' * 120)
    if regiao_norte_americana == 'Canadá (Terra-Nova e Labrador)':
        hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
        print('=' * 120)
        if 0 <= hb <= 23:
            hr = hb - 1
            if hr <= 0:
                v = hr + 24
                print(f'{hb} hora(s) no horário de Brasília equivalem à {v}:30 hora(s) em/no(a) {regiao_norte_americana}.')
                print('=' * 120)
            else:
                print(f'{hb} hora(s) no horário de Brasília equivalem à {hr}:30 hora(s) em/no(a) {regiao_norte_americana}.')
                print('=' * 120)
        else:
            print('Erro:')
            print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
    elif regiao_norte_americana == 'Canadá (Atlântico)':
        hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
        print('=' * 120)
        if 0 <= hb <= 23:
            hr = hb - 1
            if hr <= 0:
                v = hr + 24
                print(f'{hb} hora(s) no horário de Brasília equivalem à {v} hora(s) em/no(a) {regiao_norte_americana}.')
                print('=' * 120)
            else:
                print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) em/no(a) {regiao_norte_americana}.')
                print('=' * 120)
        else:
            print('Erro:')
            print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
    elif regiao_norte_americana == 'Estados Unidos (Oriental)' or regiao_norte_americana == 'Canadá (Oriental)':
        hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
        print('=' * 120)
        if 0 <= hb <= 23:
            hr = hb - 2
            if hr <= 0:
                v = hr + 24
                print(f'{hb} hora(s) no horário de Brasília equivalem à {v} hora(s) em/no(a) {regiao_norte_americana}.')
                print('=' * 120)
            else:
                print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) em/no(a) {regiao_norte_americana}.')
                print('=' * 120)
        else:
            print('Erro:')
            print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
    elif regiao_norte_americana == 'Estados Unidos (Central)' or regiao_norte_americana == 'Canadá (Central)' or regiao_norte_americana == 'México (Central)':
        hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
        print('=' * 120)
        if 0 <= hb <= 23:
            hr = hb - 3
            if hr <= 0:
                v = hr + 24
                print(f'{hb} hora(s) no horário de Brasília equivalem à {v} hora(s) em/no(a) {regiao_norte_americana}.')
                print('=' * 120)
            else:
                print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) em/no(a) {regiao_norte_americana}.')
                print('=' * 120)
        else:
            print('Erro:')
            print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
    elif regiao_norte_americana == 'Estados Unidos (Montanhas)' or regiao_norte_americana == 'Canadá (Montanhas)' or regiao_norte_americana == 'México (Montanhas)':
        hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
        print('=' * 120)
        if 0 <= hb <= 23:
            hr = hb - 4
            if hr <= 0:
                v = hr + 24
                print(f'{hb} hora(s) no horário de Brasília equivalem à {v} hora(s) em/no(a) {regiao_norte_americana}.')
                print('=' * 120)
            else:
                print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) em/no(a) {regiao_norte_americana}.')
                print('=' * 120)
        else:
            print('Erro:')
            print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
    elif regiao_norte_americana == 'Estados Unidos (Pacífico)' or regiao_norte_americana == 'Canadá (Pacífico)' or regiao_norte_americana == 'México (Pacífico)':
        hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
        print('=' * 120)
        if 0 <= hb <= 23:
            hr = hb - 5
            if hr <= 0:
                v = hr + 24
                print(f'{hb} hora(s) no horário de Brasília equivalem à {v} hora(s) em/no(a) {regiao_norte_americana}.')
                print('=' * 120)
            else:
                print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) em/no(a) {regiao_norte_americana}.')
                print('=' * 120)
        else:
            print('Erro:')
            print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
    elif regiao_norte_americana == 'Estados Unidos (Alasca)':
        hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
        print('=' * 120)
        if 0 <= hb <= 23:
            hr = hb - 6
            if hr <= 0:
                v = hr + 24
                print(f'{hb} hora(s) no horário de Brasília equivalem à {v} hora(s) em/no(a) {regiao_norte_americana}.')
                print('=' * 120)
            else:
                print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) em/no(a) {regiao_norte_americana}.')
                print('=' * 120)
        else:
            print('Erro:')
            print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
    elif regiao_norte_americana == 'Havaí':
        hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
        print('=' * 120)
        if 0 <= hb <= 23:
            hr = hb - 7
            if hr <= 0:
                v = hr + 24
                print(f'{hb} hora(s) no horário de Brasília equivalem à {v} hora(s) em/no(a) {regiao_norte_americana}.')
                print('=' * 120)
            else:
                print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) em/no(a) {regiao_norte_americana}.')
                print('=' * 120)
        else:
            print('Erro:')
            print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
    else:
        print('Erro:')
        print(f'Desculpe, {regiao_norte_americana} não é uma das opções disponíveis.')
elif continente == '5':
    print('Agora, escolha a região sul americana na qual localiza-se o país desejado para a conversão:')
    print('1 - Guianas;')
    print('2 - América Andina;')
    print('3 - América Platina;')
    print('4 - Brasil;')
    print('=' * 120)
    regiao_sul_americana = input('Insira aqui o número da opção desejada: ')
    print('=' * 120)
    if regiao_sul_americana == '1':
        print('Estamos quase acabando, escolha o país desejado para a conversão:')
        print('Guiana;')
        print('Guiana Francesa;')
        print('Suriname.')
        print('=' * 120)
        pais_guianas = input('Insira aqui o nome do país desejado: ')
        print('=' * 120)
        if pais_guianas == 'Guiana':
            hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
            print('=' * 120)
            if 0 <= hb <= 23:
                hr = hb - 1
                if hr <= 0:
                    v = hr + 24
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {v} hora(s) em/no(a) {pais_guianas}.')
                    print('=' * 120)
                else:
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) em/no(a) {pais_guianas}.')
                    print('=' * 120)
            else:
                print('Erro:')
                print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
        elif pais_guianas == 'Guiana Francesa' or pais_guianas == 'Suriname':
            hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
            print('=' * 120)
            if 0 <= hb <= 23:
                hr = hb
                print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) em/no(a) {pais_guianas}.')
                print('=' * 120)
            else:
                print('Erro:')
                print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
        else:
            print('Erro:')
            print(f'Desculpe, {pais_guianas} não é uma das opções disponíveis.')
    elif regiao_sul_americana == '2':
        print('Estamos quase acabando, escolha o país desejado para a conversão:')
        print('Bolívia;')
        print('Chile;')
        print('Colômbia;')
        print('Equador;')
        print('Peru;')
        print('Venezuela.')
        print('=' * 120)
        pais_america_andina = input('Insira aqui o número da opção desejada: ')
        print('=' * 120)
        if pais_america_andina == 'Bolívia' or pais_america_andina == 'Chile' or pais_america_andina == 'Venezuela':
            hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
            print('=' * 120)
            if 0 <= hb <= 23:
                hr = hb - 1
                if hr <= 0:
                    v = hr + 24
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {v} hora(s) em/no(a) {pais_america_andina}.')
                    print('=' * 120)
                else:
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) em/no(a) {pais_america_andina}.')
                    print('=' * 120)
            else:
                print('Erro:')
                print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
        elif pais_america_andina == 'Colômbia' or pais_america_andina == 'Equador' or pais_america_andina == 'Peru':
            hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
            print('=' * 120)
            if 0 <= hb <= 23:
                hr = hb - 2
                if hr <= 0:
                    v = hr + 24
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {v} hora(s) em/no(a) {pais_america_andina}.')
                    print('=' * 120)
                else:
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) em/no(a) {pais_america_andina}.')
                    print('=' * 120)
            else:
                print('Erro:')
                print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
        else:
            print('Erro:')
            print(f'Desculpe, {pais_america_andina} não é uma das opções disponíveis.')
    elif regiao_sul_americana == '3':
        print('Estamos quase acabando, escolha o país desejado para a conversão:')
        print('Argentina;')
        print('Uruguai;')
        print('Paraguai.')
        print('=' * 120)
        pais_america_platina = input('Insira aqui o número da opção desejada: ')
        print('=' * 120)
        if pais_america_platina == 'Argentina' or pais_america_platina == 'Uruguai':
            hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
            print('=' * 120)
            if 0 <= hb <= 23:
                hr = hb
                print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) em/no(a) {pais_america_platina}.')
                print('=' * 120)
            else:
                print('Erro:')
                print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
        if pais_america_platina == 'Paraguai':
            hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
            print('=' * 120)
            if 0 <= hb <= 23:
                hr = hb - 1
                if hr <= 0:
                    v = hr + 24
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {v} hora(s) em/no(a) {pais_america_platina}.')
                    print('=' * 120)
                else:
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) em/no(a) {pais_america_platina}.')
                    print('=' * 120)
            else:
                print('Erro:')
                print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
        else:
            print('Erro:')
            print(f'Desculpe, {pais_america_platina} não é uma das opções disponíveis.')
    elif regiao_sul_americana == '4':
        print('Estamos quase acabando, escolha o fuso horário brasileiro desejado para a conversão:')
        print('Fuso Insular - UTC-2;')
        print('Fuso UTC-4 ;')
        print('Fuso UTC-5.')
        print('=' * 120)
        fuso_brasileiro = input('Insira aqui o nome do país desejado: ')
        print('=' * 120)
        if fuso_brasileiro == 'Fuso Insular - UTC-2':
            hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
            print('=' * 120)
            if 0 <= hb <= 23:
                hr = hb + 1
                if hr >= 24:
                    v = hr - 24
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {v} hora(s) no {fuso_brasileiro}.')
                    print('=' * 120)
                else:
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) no {fuso_brasileiro}.')
                    print('=' * 120)
            else:
                print('Erro:')
                print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
        elif fuso_brasileiro == 'Fuso UTC-4':
            hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
            print('=' * 120)
            if 0 <= hb <= 23:
                hr = hb - 1
                if hr <= 0:
                    v = hr + 24
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {v} hora(s) no {fuso_brasileiro}.')
                    print('=' * 120)
                else:
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) no {fuso_brasileiro}.')
                    print('=' * 120)
            else:
                print('Erro:')
                print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
        elif fuso_brasileiro == 'Fuso UTC-5':
            hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
            print('=' * 120)
            if 0 <= hb <= 23:
                hr = hb - 2
                if hr <= 0:
                    v = hr + 24
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {v} hora(s) no {fuso_brasileiro}.')
                    print('=' * 120)
                else:
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) no {fuso_brasileiro}.')
                    print('=' * 120)
            else:
                print('Erro:')
                print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
        else:
            print('Erro:')
            print(f'Desculpe, {fuso_brasileiro} não é uma das opções disponíveis.')
    else:
        print('Erro:')
        print(f'Desculpe, {regiao_sul_americana} não é uma das opções disponíveis.')
elif continente == '6':
    print('Agora, escolha a região europeia na qual localiza-se o país desejado para a conversão:')
    print('1 - Europa Setentrional (Rússia Ocidental);')
    print('2 - Europa Ocidental (Oeste Europeu);')
    print('3 - Europa Meridional (Europa Mediterrânea);')
    print('4 - Europa Oriental (Leste Europeu).')
    print('=' * 120)
    regiao_europeia = input('Insira aqui o número da opção desejada: ')
    print('=' * 120)
    if regiao_europeia == '1':
        print('Estamos quase acabando, escolha o país desejado para a conversão:')
        print('Islândia;')
        print('Dinamarca;')
        print('Noruega;')
        print('Suécia;')
        print('Finlândia;')
        print('Lituânia;')
        print('Letônia;')
        print('Estônia;')
        print('Ilhas Faroé;')
        print('Arquipélago Åland;')
        print('Groenlândia.')
        print('=' * 120)
        pais_europa_setentrional = input('Insira aqui o número da opção desejada: ')
        print('=' * 120)
        if pais_europa_setentrional == 'Groelândia':
            hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
            print('=' * 120)
            if 0 <= hb <= 23:
                hr = hb
                print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) em/no(a) {pais_europa_setentrional}.')
                print('=' * 120)
            else:
                print('Erro:')
                print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
        elif pais_europa_setentrional == 'Islândia' or pais_europa_setentrional == 'Ilhas Faroé':
            hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
            print('=' * 120)
            if 0 <= hb <= 23:
                hr = hb + 3
                if hr >= 24:
                    v = hr - 24
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {v} hora(s) em/no(a) {pais_europa_setentrional}.')
                    print('=' * 120)
                else:
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) em/no(a) {pais_europa_setentrional}.')
                    print('=' * 120)
            else:
                print('Erro:')
                print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
        elif pais_europa_setentrional == 'Dinamarca' or pais_europa_setentrional == 'Noruega' or pais_europa_setentrional == 'Suécia':
            hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
            print('=' * 120)
            if 0 <= hb <= 23:
                hr = hb + 4
                if hr >= 24:
                    v = hr - 24
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {v} hora(s) em/no(a) {pais_europa_setentrional}.')
                    print('=' * 120)
                else:
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) em/no(a) {pais_europa_setentrional}.')
                    print('=' * 120)
            else:
                print('Erro:')
                print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
        elif pais_europa_setentrional == 'Arquipélago Åland' or pais_europa_setentrional == 'Finlândia' or pais_europa_setentrional == 'Lituânia' or pais_europa_setentrional == 'Letônia' or pais_europa_setentrional == 'Estônia':
            hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
            print('=' * 120)
            if 0 <= hb <= 23:
                hr = hb + 5
                if hr >= 24:
                    v = hr - 24
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {v} hora(s) em/no(a) {pais_europa_setentrional}.')
                    print('=' * 120)
                else:
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) em/no(a) {pais_europa_setentrional}.')
                    print('=' * 120)
            else:
                print('Erro:')
                print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
        else:
            print('Erro:')
            print(f'Desculpe, {pais_europa_setentrional} não é uma das opções disponíveis.')
    elif regiao_europeia == '2':
        print('Estamos quase acabando, escolha o país desejado para a conversão:')
        print('Reino Unido;')
        print('Irlanda;')
        print('França;')
        print('Países Baixos;')
        print('Bélgica;')
        print('Luxemburgo;')
        print('Alemanha;')
        print('Suíça;')
        print('Liechtenstein;')
        print('Áustria.')
        print('=' * 120)
        pais_europa_ocidental = input('Insira aqui o número da opção desejada: ')
        print('=' * 120)
        if pais_europa_ocidental == 'Reino Unido' or pais_europa_ocidental == 'Irlânda':
            hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
            print('=' * 120)
            if 0 <= hb <= 23:
                hr = hb + 3
                if hr >= 24:
                    v = hr - 24
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {v} hora(s) em/no(a) {pais_europa_ocidental}.')
                    print('=' * 120)
                else:
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) em/no(a) {pais_europa_ocidental}.')
                    print('=' * 120)
            else:
                print('Erro:')
                print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
        elif pais_europa_ocidental == 'França' or pais_europa_ocidental == 'Bélgica' or pais_europa_ocidental == 'Luxemburgo' or pais_europa_ocidental == 'Alemanha' or pais_europa_ocidental == 'Suíça' or pais_europa_ocidental == 'Liechtenstein' or pais_europa_ocidental == 'Áustria':
            hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
            print('=' * 120)
            if 0 <= hb <= 23:
                hr = hb + 4
                if hr >= 24:
                    v = hr - 24
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {v} hora(s) em/no(a) {pais_europa_ocidental}.')
                    print('=' * 120)
                else:
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) em/no(a) {pais_europa_ocidental}.')
                    print('=' * 120)
            else:
                print('Erro:')
                print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
        else:
            print('Erro:')
            print(f'Desculpe, {pais_europa_ocidental} não é uma das opções disponíveis.')
    elif regiao_europeia == '3':
        print('Estamos quase acabando, escolha o país desejado para a conversão:')
        print('Portugal;')
        print('Espanha;')
        print('Andorra;')
        print('Itália;')
        print('San Marino;')
        print('Malta;')
        print('Vaticano;')
        print('Mônaco;')
        print('Eslovênia;')
        print('Croácia;')
        print('Bósnia-Hezergovina;')
        print('Sérvia;')
        print('Montenegro;')
        print('Kosovo;')
        print('Albânia;')
        print('Macedônia;')
        print('Grécia;')
        print('Turquia (Trácia Ocidental).')
        print('=' * 120)
        pais_europa_meridional = input('Insira aqui o número da opção desejada: ')
        print('=' * 120)
        if pais_europa_meridional == 'Portugal':
            hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
            print('=' * 120)
            if 0 <= hb <= 23:
                hr = hb + 3
                if hr >= 24:
                    v = hr - 24
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {v} hora(s) em/no(a) {pais_europa_meridional}.')
                    print('=' * 120)
                else:
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) em/no(a) {pais_europa_meridional}.')
                    print('=' * 120)
            else:
                print('Erro:')
                print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
        elif pais_europa_meridional == 'Espanha' or pais_europa_meridional == 'Andorra' or pais_europa_meridional == 'Itália' or pais_europa_meridional == 'San Marino' or pais_europa_meridional == 'Malta' or pais_europa_meridional == 'Vaticano' or pais_europa_meridional == 'Mônaco' or pais_europa_meridional == 'Eslovênia' or pais_europa_meridional == 'Croácia' or pais_europa_meridional == 'Bósnia-Hezergovina' or pais_europa_meridional == 'Sérvia' or pais_europa_meridional == 'Montenegro' or pais_europa_meridional == 'Kosovo' or pais_europa_meridional == 'Albânia' or pais_europa_meridional == 'Macedônia':
            hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
            print('=' * 120)
            if 0 <= hb <= 23:
                hr = hb + 4
                if hr >= 24:
                    v = hr - 24
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {v} hora(s) em/no(a) {pais_europa_meridional}.')
                    print('=' * 120)
                else:
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) em/no(a) {pais_europa_meridional}.')
                    print('=' * 120)
            else:
                print('Erro:')
                print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
        elif pais_europa_meridional == 'Grécia' or pais_europa_meridional == 'Turquia':
            hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
            print('=' * 120)
            if 0 <= hb <= 23:
                hr = hb + 5
                if hr >= 24:
                    v = hr - 24
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {v} hora(s) em/no(a) {pais_europa_meridional}.')
                    print('=' * 120)
                else:
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) em/no(a) {pais_europa_meridional}.')
                    print('=' * 120)
            else:
                print('Erro:')
                print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
        else:
            print('Erro:')
            print(f'Desculpe, {pais_europa_meridional} não é uma das opções disponíveis.')
    elif regiao_europeia == '4':
        print('Estamos quase acabando, escolha o país desejado para a conversão:')
        print('Armênia;')
        print('Azerbajão;')
        print('Belarus;')
        print('Bulgária;')
        print('República Checa;')
        print('Geórgia;')
        print('Eslováquia;')
        print('Romênia;')
        print('Hungria;')
        print('Moldávia;')
        print('Ucrânia;')
        print('Polônia;')
        print('Rússia.')
        print('=' * 120)
        pais_europa_oriental = input('Insira aqui o número da opção desejada: ')
        print('=' * 120)
        if pais_europa_oriental == 'Armênia' or pais_europa_oriental == 'Geórgia' or pais_europa_oriental == 'Azerbajão':
            hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
            print('=' * 120)
            if 0 <= hb <= 23:
                hr = hb + 7
                if hr >= 24:
                    v = hr - 24
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {v} hora(s) em/no(a) {pais_europa_oriental}.')
                    print('=' * 120)
                else:
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) em/no(a) {pais_europa_oriental}.')
                    print('=' * 120)
            else:
                print('Erro:')
                print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
        elif pais_europa_oriental == 'Polônia' or pais_europa_oriental == 'República Checa' or pais_europa_oriental == 'Hungria' or pais_europa_oriental == 'Eslováquia' or pais_europa_oriental == 'Polônia':
            hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
            print('=' * 120)
            if 0 <= hb <= 23:
                hr = hb + 4
                if hr >= 24:
                    v = hr - 24
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {v} hora(s) em/no(a) {pais_europa_oriental}.')
                    print('=' * 120)
                else:
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) em/no(a) {pais_europa_oriental}.')
                    print('=' * 120)
            else:
                print('Erro:')
                print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
        elif pais_europa_oriental == 'Bulgária' or pais_europa_oriental == 'Romênia' or pais_europa_oriental == 'Moldávia' or pais_europa_oriental == 'Ucrânia' or pais_europa_oriental == 'Belarus':
            hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
            print('=' * 120)
            if 0 <= hb <= 23:
                hr = hb + 5
                if hr >= 24:
                    v = hr - 24
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {v} hora(s) em/no(a) {pais_europa_oriental}.')
                    print('=' * 120)
                else:
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) em/no(a) {pais_europa_oriental}.')
                    print('=' * 120)
            else:
                print('Erro:')
                print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
        elif pais_europa_oriental == 'Rússia':
            print('Por último, escolha a zona russa desejada para a conversão:')
            print('Zona 1 (Horário Padrão de Kaliningrado);')
            print('Zona 2 (Horário Padrão de Moscow);')
            print('Zona 3 (Horário Padrão de Samara ).')
            print('=' * 120)
            zona = input('Insira aqui o número da Zona desejada: ')
            print('=' * 120)
            if zona == '1':
                hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
                print('=' * 120)
                if 0 <= hb <= 23:
                    hr = hb + 5
                    if hr >= 24:
                        v = hr - 24
                        print(f'{hb} hora(s) no horário de Brasília equivalem à {v} hora(s)na Zona {zona} russa.')
                        print('=' * 120)
                    else:
                        print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) na Zona {zona} russa.')
                        print('=' * 120)
                else:
                    print('Erro:')
                    print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
            elif zona == '2':
                hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
                print('=' * 120)
                if 0 <= hb <= 23:
                    hr = hb + 6
                    if hr >= 24:
                        v = hr - 24
                        print(f'{hb} hora(s) no horário de Brasília equivalem à {v} hora(s)na Zona {zona} russa.')
                        print('=' * 120)
                    else:
                        print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) na Zona {zona} russa.')
                        print('=' * 120)
                else:
                    print('Erro:')
                    print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
            elif zona == '3':
                hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
                print('=' * 120)
                if 0 <= hb <= 23:
                    hr = hb + 7
                    if hr >= 24:
                        v = hr - 24
                        print(f'{hb} hora(s) no horário de Brasília equivalem à {v} hora(s)na Zona {zona} russa.')
                        print('=' * 120)
                    else:
                        print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) na Zona {zona} russa.')
                        print('=' * 120)
                else:
                    print('Erro:')
                    print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
            else:
                print('Erro:')
                print(f'Desculpe, Zona {zona} não é uma das opções disponíveis.')
        else:
            print('Erro:')
            print(f'Desculpe, {pais_europa_oriental} não é uma das opções disponíveis.')
    else:
        print('Erro:')
        print(f'Desculpe, {regiao_europeia} não é uma das opções disponíveis.')
elif continente == '7':
    print('Agora, escolha a região sul oceânica na qual localiza-se o país desejado para a conversão:')
    print('1 - Australásia;')
    print('2 - Melanésia;')
    print('3 - Micronésia;')
    print('4 - Polinésia.')
    print('=' * 120)
    regiao_oceania = input('Insira aqui o número da opção desejada: ')
    print('=' * 120)
    if regiao_oceania == '1':
        print('Estamos quase acabando, escolha o país desejado para a conversão:')
        print('Austrália (Ocidental);')
        print('Austrália (Central);')
        print('Austrália (Oriental);')
        print('Nova Zelândia.')
        print('=' * 120)
        pais_australasia = input('Insira aqui o número da opção desejada: ')
        print('=' * 120)
        if pais_australasia == 'Austrália (Ocidental)':
            hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
            print('=' * 120)
            if 0 <= hb <= 23:
                hr = hb + 11
                if hr >= 24:
                    v = hr - 24
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {v} hora(s) em/no(a) {pais_australasia}.')
                    print('=' * 120)
                else:
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) em/no(a) {pais_australasia}.')
                    print('=' * 120)
            else:
                print('Erro:')
                print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
        elif pais_australasia == 'Austrália (Central)':
            hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
            print('=' * 120)
            if 0 <= hb <= 23:
                hr = hb + 12
                if hr >= 24:
                    v = hr - 24
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {v}:30 hora(s) em/no(a) {pais_australasia}.')
                    print('=' * 120)
                else:
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {hr}:30 hora(s) em/no(a) {pais_australasia}.')
                    print('=' * 120)
            else:
                print('Erro:')
                print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
        elif pais_australasia == 'Austrália (Oriental)':
            hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
            print('=' * 120)
            if 0 <= hb <= 23:
                hr = hb + 13
                if hr >= 24:
                    v = hr - 24
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {v} hora(s) em/no(a) {pais_australasia}.')
                    print('=' * 120)
                else:
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) em/no(a) {pais_australasia}.')
                    print('=' * 120)
            else:
                print('Erro:')
                print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
        elif pais_australasia == 'Nova Zelândia':
            hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
            print('=' * 120)
            if 0 <= hb <= 23:
                hr = hb + 15
                if hr >= 24:
                    v = hr - 24
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {v} hora(s) em/no(a) {pais_australasia}.')
                    print('=' * 120)
                else:
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) em/no(a) {pais_australasia}.')
                    print('=' * 120)
            else:
                print('Erro:')
                print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
        else:
            print('Erro:')
            print(f'Desculpe, {pais_australasia} não é uma das opções disponíveis.')
    elif regiao_oceania == '2':
        print('Estamos quase acabando, escolha o país desejado para a conversão:')
        print('Papua-Nova Guiné;')
        print('Vanuatu;')
        print('Ilhas Salomão;')
        print('Fiji;')
        print('Nova Caledónia.')
        print('=' * 120)
        pais_melanesia = input('Insira aqui o número da opção desejada: ')
        print('=' * 120)
        if pais_melanesia == 'Papua-Nova Guiné':
            hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
            print('=' * 120)
            if 0 <= hb <= 23:
                hr = hb + 13
                if hr >= 24:
                    v = hr - 24
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {v} hora(s) em/no(a) {pais_melanesia}.')
                    print('=' * 120)
                else:
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) em/no(a) {pais_melanesia}.')
                    print('=' * 120)
            else:
                print('Erro:')
                print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
        elif pais_melanesia == 'Vanuatu' or pais_melanesia == 'Ilhas Salomão' or pais_melanesia == 'Nova Caledónia':
            hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
            print('=' * 120)
            if 0 <= hb <= 23:
                hr = hb + 14
                if hr >= 24:
                    v = hr - 24
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {v} hora(s) em/no(a) {pais_melanesia}.')
                    print('=' * 120)
                else:
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) em/no(a) {pais_melanesia}.')
                    print('=' * 120)
            else:
                print('Erro:')
                print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
        else:
            print('Erro:')
            print(f'Desculpe, {pais_melanesia} não é uma das opções disponíveis.')
    elif regiao_oceania == '3':
        print('Estamos quase acabando, escolha o país desejado para a conversão:')
        print('Estados Federados da Micronésia;')
        print('Ilhas Marshall;')
        print('Kiribati;')
        print('Nauru;')
        print('Palau.')
        print('=' * 120)
        pais_micronesia = input('Insira aqui o número da opção desejada: ')
        print('=' * 120)
        if pais_micronesia == 'Palau':
            hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
            print('=' * 120)
            if 0 <= hb <= 23:
                hr = hb + 12
                if hr >= 24:
                    v = hr - 24
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {v} hora(s) em/no(a) {pais_micronesia}.')
                    print('=' * 120)
                else:
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) em/no(a) {pais_micronesia}.')
                    print('=' * 120)
            else:
                print('Erro:')
                print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
        elif pais_micronesia == 'Estados Federados da Micronésia':
            hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
            print('=' * 120)
            if 0 <= hb <= 23:
                hr = hb + 14
                if hr >= 24:
                    v = hr - 24
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {v} hora(s) em/no(a) {pais_micronesia}.')
                    print('=' * 120)
                else:
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) em/no(a) {pais_micronesia}.')
                    print('=' * 120)
            else:
                print('Erro:')
                print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
        elif pais_micronesia == 'Ilhas Marshall' or pais_micronesia == 'Kiribati' or pais_micronesia == 'Nauru':
            hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
            print('=' * 120)
            if 0 <= hb <= 23:
                hr = hb + 15
                if hr >= 24:
                    v = hr - 24
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {v} hora(s) em/no(a) {pais_micronesia}.')
                    print('=' * 120)
                else:
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) em/no(a) {pais_micronesia}.')
                    print('=' * 120)
            else:
                print('Erro:')
                print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
        else:
            print('Erro:')
            print(f'Desculpe, {pais_micronesia} não é uma das opções disponíveis.')
    elif regiao_oceania == '4':
        print('Estamos quase acabando, escolha o país desejado para a conversão:')
        print('Samoa;')
        print('Tonga;')
        print('Tuvalu;')
        print('=' * 120)
        pais_polinesia = input('Insira aqui o número da opção desejada: ')
        print('=' * 120)
        if pais_polinesia == 'Tonga' or pais_polinesia == 'Samoa':
            hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
            print('=' * 120)
            if 0 <= hb <= 23:
                hr = hb + 16
                if hr >= 24:
                    v = hr - 24
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {v} hora(s) em/no(a) {pais_polinesia}.')
                    print('=' * 120)
                else:
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) em/no(a) {pais_polinesia}.')
                    print('=' * 120)
            else:
                print('Erro:')
                print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
        elif pais_polinesia == 'Tuvalu':
            hb = int(input('Por fim, insira o horário desejado conforme o fuso de Brasília (de 0 à 23 horas inteiras): '))
            print('=' * 120)
            if 0 <= hb <= 23:
                hr = hb + 15
                if hr >= 24:
                    v = hr - 24
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {v} hora(s) em/no(a) {pais_polinesia}.')
                    print('=' * 120)
                else:
                    print(f'{hb} hora(s) no horário de Brasília equivalem à {hr} hora(s) em/no(a) {pais_polinesia}.')
                    print('=' * 120)
            else:
                print('Erro:')
                print('Desculpe, não é possível contabilizar uma quantidade de horas menor que 0 ou maior que 23.')
        else:
            print('Erro:')
            print(f'Desculpe, {pais_polinesia} não é uma das opções disponíveis.')
    else:
        print('Erro:')
        print(f'Desculpe, {regiao_oceania} não é uma das opções disponíveis.')
else:
    print('Erro:')
    print(f'Desculpe, {continente} não é uma das opções disponíveis.')
print('Obrigado por utilizar o conversor de horários Global Zone!')
input('Insira algo para Finalizar: ')
print('=' * 120)
