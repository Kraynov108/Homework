grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
sorted_students = sorted(students)
average_rating0 = sum(grades[0]) / len(grades[0])
average_rating1 = sum(grades[1]) / len(grades[1])
average_rating2 = sum(grades[2]) / len(grades[2])
average_rating3 = sum(grades[3]) / len(grades[3])
average_rating4 = sum(grades[4]) / len(grades[4])
final_dictionary = dict()
final_dictionary[sorted_students[0]] = average_rating0
final_dictionary[sorted_students[1]] = average_rating1
final_dictionary[sorted_students[2]] = average_rating2
final_dictionary[sorted_students[3]] = average_rating3
final_dictionary[sorted_students[4]] = average_rating4
print(final_dictionary)
