# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
#Primeiro definimos a variável para a altura, depois, utilizando o for para o loop da lista que foi criada pelo usuário, utilizamos a formula x += y para somar as alturas
totalHeight = 0
for height in student_heights:
    totalHeight += height
#Depois criamos uma variável para definir a quantidade de estudantes, após isso utilizamos a formular x += 1 para que possa ser somado a quantidade de itens dentro da lista
number_of_students = 0
for student in student_heights:
  number_of_students += 1
#No final faremos uma formula normal de média de altura, utilizando round. 
average_height = round(totalHeight / number_of_students)
print(average_height)
