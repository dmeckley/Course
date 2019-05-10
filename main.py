from course import Course 

def main():

	# Create and Allocate Course Object Instances in Memory:
	course1 = Course("Data Structures")
	course2 = Course("SQL Programming")

	# Add Students to course1 Object Instance:
	course1.addStudent("Peter Jones")
	course1.addStudent("Brian Smith")
	course1.addStudent("Annie Kennedy")

	# Add Students to course2 Object Instance:
	course2.addStudent("Tom Jones")
	course2.addStudent("Lee Smith")
	course2.addStudent("Mary Jane")

	# Display course1 Object Instance List and Length of List:
	print("Number of students in course 1:", course1.getNumberOfStudents())
	for student in course1.getStudents():
		print(student, end = ", ")
	print('\n')

	# Remove Student from course2 Object Instance:
	if "Tom Jones" in course2.getStudents():
		course2.dropStudent("Tom Jones")
		
	# Display course2 Object Instance List and Length of List:
	print("Number of students in course 2:", course2.getNumberOfStudents())
	for student in course2.getStudents():
			print(student, end = ", ")
	print('\n')


if __name__ == '__main__':
	main()