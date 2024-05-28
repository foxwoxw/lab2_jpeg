import jpeg
import generate_test_data as gtd
from PIL import Image


#gtd.one_color(70, 130, 180, 700, 1000)
#gtd.random_color(700, 1000)
#gtd.basic_color(128)
#gtd.blocks(768, 768, 64)



def main():
    print('Выбор изображения: 1 - цветное изображение, 2 - однотонное, 3 - случайный цвет,\n\t\t   4 - базовые цвета, 5 - блоки из нескольких цветов.')
    print('Изображение: ', end = '')
    img_type = int(input())
    if img_type == 1:
        file = 'color.png'
    elif img_type == 2:
        file = 'one_color.png'
    elif img_type == 3:
        file = 'random_color.png'
    elif img_type == 4:
        file = 'basic_color.png'
    elif img_type == 5:
        file = 'blocks.png'
    else:
        print('error')
        return
    print('Качество: Q = ', end = '')
    q = int(input())
    if q < 1 or q > 100:
        print('error')
        return
    jpeg.encode_jpeg('png\\' + file, 2, 2, q)
    print('Результат сохранен в txt\\result.txt')
    print('Коэффициент сжатия: ', end = '')
    print(gtd.compression_ratio(file))
    print('Выполняется декодирование изображения..')
    rgb = jpeg.decode_jpeg('txt\\result.txt')
    print("Сохранить? ('y'/'n'): ", end = '')
    a = input()
    if a == 'y':
        print("Введите имя файла: ", end = '')
        a = input()
        Image.fromarray((rgb),mode="RGB").save('results\\' + a)



main()

