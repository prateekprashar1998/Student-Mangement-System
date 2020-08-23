class_1 = [ 'Geoffrey Hinton' , 'Andrew Ng', 'Sebastian Raschka', 'Yoshua Bengio']
class_2 = ['Hilary Mason', 'Carla Gentry' , 'corinnna Cortes']
new_class = class_1 + class_2
print(new_class)
new_class.append('Peter Warden')
print(new_class)
new_class.remove('Carla Gentry' )
print(new_class)
courses= { 'Maths' : '65' , 'English': '70' , 'History' : '80' , 'French' : '70' , 'Science' : '60'}
total= (65+70+80+70+60)
print(total)
percentage = total/5
print(percentage)
mathematics = { 'Geoffrey Hinton' : 78 , 'Andrew Ng' : 95 , 'Sebastian Raschka' : 65 , 'Yoshua Benjio' : 50 , 'Hilary Mason' : 70 , 'Corinna Cortes' : 66 , 'Peter Warden' : 75 }
print(mathematics)
topper = max(mathematics ,key= mathematics.get )
print(topper)

x= topper.split()
first_name= x[0]
last_name= x[1]
lastname_length= len(last_name)+1
lastname_revised= last_name.ljust(lastname_length)
print(lastname_revised)
print(first_name)
full_name=lastname_revised + first_name   
# print the full_name
print(full_name)
# print the name in upper case
certificate_name = full_name.upper()
print(certificate_name)
