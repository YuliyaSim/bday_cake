birth_year = int(input("What year were you born? "))
age = 2019 - birth_year
candel = int(list(str(age))[-1])

num_of_candels = "i" * candel
happy = " "*3 + "|:H:a:p:p:y:|"
birthday = "|:B:i:r:t:h:d:a:y:|"
bottom = "~" * 19
top = (" "*6 + "__" + num_of_candels + "__")
middle = " "*3 + "|" + " "*11 + "|"
middle_second = "|" + "^" * 17 + "|"
pre_bottom = "|" + " " * 17 + "|"


cake = f"""
	{top}
	{happy}
	{middle}
	{middle_second}
	{birthday}
	{pre_bottom}
	{bottom}
 """

if (birth_year % 4 == 0):
	print(cake * 2)
else:
	print(cake)	 
