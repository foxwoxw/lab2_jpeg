import jpeg
import generate_test_data as gtd


#gtd.one_color(70, 130, 180, 700, 1000)
#gtd.random_color(700, 1000)

def main():
    print('Выбор изображения: 1 - цветное изображение, 2 - однотонное, 3 - случайный цвет.')
    print('type = ')
    img_type = int(input())
    if img_type == 1:
        file = 'color.png'
    elif img_type == 2:
        file = 'one_color.png'
    elif img_type == 3:
        file = 'random_color.png'
    else:
        print('error')
        return
    print('Качество: Q = ', end = '')
    q = int(input())
    if q < 0 or q > 100:
        print('error')
        return
    jpeg.encode_jpeg('png\\' + file, 2, 2, q)
    print('Результат сохранен в txt\\result.txt')
    print('Коэффициент сжатия: ', end = '')
    print(gtd.compression_ratio(file))
    print('Выполняется декодирование изображения..')
    jpeg.decode_jpeg('txt\\result.txt')



main()
