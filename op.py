class student:
    def __init__(self,first,last,marks):
        self.first=first
        self.last=last
        self.marks=marks
        self.email=first+'.'+last+'@school.com'
        
std_1=student('neel','varma',60)
std_2=student('hemanth','sharma',90)
print(std_1.email)
print(std_2.last)

print('{} {}'.format(std_1.first,std_1.last))
