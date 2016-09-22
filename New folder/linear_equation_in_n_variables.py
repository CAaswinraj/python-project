#determinant by induction

from inp import gi
def get_two_dimentional_square_matrix():
	a= gi()
	lst=[[0 for x in range(a)]for y in range(a)]
	for i in range(a):
		print(i+1,"row")
		for j in range(a):
			print(j+1,"column")
			lst[i][j]=gi()
	print(lst)
	return lst
def determinant(c,l):
	if (c==2):
		s=l[0][0]*l[1][1]-l[0][1]*l[1][0]
		return s
	elif(c>2):
		s=0
		for i in range(c):
			n=[[l[x][y] for y in range(c) if (y!=i)]for x in range(c) if (x!=0)]
			print(n)
			s+=l[0][i]*((-1)**i)*determinant(len(n),n)
		return s
#cramers rule to get values of variables		
			
def get_linear_equation_in_n_variables():

	print("enter the no of vaiables")
	a=gi()
	lst=[[0 for x in range(a+1)]for y in range(a)]
	for i in range(a):
		print(i+1,"row")
		for j in range(a+1):
			print(j+1,"column")
			lst[i][j]=gi()
	print(lst)
	return lst

def swap_column(i,j,l):
	for x in range(len(l)):
		c=l[x][i]
		l[x][i]=l[x][j]
		l[x][j]=c
	return l
def get_square_matrix_from_rectangular_matrix(l):
	lst=[[l[x][y] for y in range(len(l))]for x in range(len(l))]
	return lst



def linear_equation_solution(l):
	a=get_square_matrix_from_rectangular_matrix(l)
	b=determinant(len(a),a)
	print(b)
	for x in range(len(l)):
		l=swap_column(x,(len(l)),l)
		print(l)
		d=determinant(len(l),l)
		print(d)		
		f=d/b
		print(x+1,"st var is ",f)
		l=swap_column(x,(len(l)),l)
		print(l)

test=get_linear_equation_in_n_variables()
solution(test)
b= input()








