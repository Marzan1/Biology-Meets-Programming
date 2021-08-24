file = open("D:\\nrgvje.txt", "r")
genome = file.read()
string_without_line_breaks = ""
for line in genome:
  stripped_line = line.rstrip()
  string_without_line_breaks += stripped_line
print(string_without_line_breaks)
