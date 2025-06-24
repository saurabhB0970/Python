
# HOMEWORk  :-  An employee has name, salary and phone.Phone means mobile number , email address . Employee has one operation which display salary and name of employee.

# Define a class named Employee
class Employee:
    def emp(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
        
e1 = Employee()

e1.name = "Saurabh"
e1.salary = 40000
e1.phone = "7385413158"
e1.email = "bhosale123@gmail.com"

# Call the show method to display name and salary
e1.emp()