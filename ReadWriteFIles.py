# Read from file
path = 'Example.cs'
days_file = open(path, 'r')
days = days_file.read()

# Write to another
path = 'ExampleW.cs'
days_filew = open(path, 'w')
dayswrite = days_filew.write(days)

print("Text copied from Example.cs to ExampleW.cs")