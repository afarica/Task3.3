# "Аналог шифра цезаря ". Программа должна запрашивать элементы списка через
# пробел. После чего пользователь должен ввести значение для сдвига элементов списка.
# Значение может быть как положительным, так и отрицательным. Если значение
# положительное, элементы списка должны сдвигаться вправо, если отрицательное -
# влево. Результат необходимо вывести на экран:
source_data=list(input("Enter numbers separated by spaces:")
shift=int(input('How much to shift?:'))
for x in source_data:
	a=int(ord(x))
	b=a+shift
	print(str(chr(b)),end='')

