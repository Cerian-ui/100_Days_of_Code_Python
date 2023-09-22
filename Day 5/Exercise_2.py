# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
#Para este código, setamos uma variável de valor 0, logo após criamos um comando for, dentro deste comando iremos verificar com cada item da lista se o score é maior do que a variável que criamos
#vamos armazena-la em seguida, isso vai seguir até fazer com todos os itens e o item que vai ficar guardado vai ser o que atender a função IF, ou seja, o maior item
higher = 0
for score in student_scores:
    if score > higher:
        higher = score
print(f"The highest score in the class is: {higher}")
