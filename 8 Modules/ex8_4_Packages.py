# import courses
#
# print(dir(courses))
# courses.python.get_python()


import courses

# вызов функции напрямую, когда она добавлена в пространство имен проекта
print(courses.get_python())
courses.java.get_java()
courses.get_php()

print(courses.python_doc.doc)

print(dir(courses))


