# Initialize dictionary with employee salaries. 
# initialize empty dictionary for updated salaries. 
# Loop through each key-value pair in employee_salaries

emplyee_current_salaries = {"Kim": 3000, "Lee": 2500, "Ahmed": 2000}
updated_salaries = {}

for name, value in emplyee_current_salaries.items():
    updated_salaries = value*2
    print(name, updated_salaries)