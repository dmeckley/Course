class Course(object):

	# Initializer Constructor Method:
	def __init__(self, courseName):
		"""Initializes self.__courseName variable and
		   self.__students list."""
		self.__courseName = courseName
		self.__students = []

	# Accessor Methods:
	def getStudents(self):
		"""Returns self.__students list."""
		return(self.__students)

	def getNumberOfStudents(self):
		"""Returns length of self.__students list."""
		return(len(self.__students))

	def getCourseName(self):
		"""Returns self.__courseName variable."""
		return(self.__courseName)

	# Mutator Methods:
	def addStudent(self, student):
		"""Adds student variable to self.__students list."""
		self.__students.append(student)

	def dropStudent(self, student):
		"""Removes student variable from self.__students list"""
		self.__students.remove(student)
		