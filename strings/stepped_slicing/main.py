filename = "Annual Budget Report 2024"
pos=filename.index("2")
year_code = filename[pos:len(filename):2]

print("Variable sliced_string equals:", year_code)