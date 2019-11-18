source_data=list(input("Enter numbers separated by spaces:").split())
shift=int(input('How much to shift?:'))
for x in source_data:
	print(int(x)+shift,end=' ')