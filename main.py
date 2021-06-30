grade = int(input('Please enter your PSTP grade:'))

if(grade >= 90):
  print('This is A1')
elif(grade >= 80 and grade < 90):
  print('This is A2')
elif(grade >= 70 and grade < 80):
  print('This is A3')
elif(grade >= 65 and grade < 70):
  print('This is B1')
elif(grade >= 60 and grade < 65):
  print('This is B2')
elif(grade >= 55 and grade < 60):
  print('This is B3')
elif(grade >= 50 and grade < 55):
  print('This is C1')
elif(grade >= 45 and grade < 50):
  print('This is C2')
elif(grade >= 40 and grade < 45):
  print('This is C3')
else:
    print('Unfortunately, you have failed, fatality.')