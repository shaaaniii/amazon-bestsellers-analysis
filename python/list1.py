#ORGANIZING STUDENT GRADES 
grades = [56,89,90,78,94]

#add grade 
grades.append(97)

#calculate average 
average_grade = sum(grades)/len(grades)
print("Average grade is :" , average_grade)

#find highest and lowest marks 
high_marks = max(grades)
low_marks = min(grades)

print("Highest grade is : " ,high_marks)
print("lowest grade is : " , low_marks)
