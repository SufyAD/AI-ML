# Basic technique to write
f = open("C:\\GenAI\\ai_ml\\AI-ML\\advance_python\\test.txt", "w")
f.write("Test successfully completed")
f.close()

# Append - now overwrite
f = open("C:\\GenAI\\ai_ml\\AI-ML\\advance_python\\test.txt", "a")
f.write("\nTest 2 to append successfully completed")
f.close()

# Reading line by line
# split(): split the cahrachers on " " and returns an array of characters
f = open("C:\\GenAI\\ai_ml\\AI-ML\\advance_python\\read_test.txt", "r")
for line in f:
    tokens = line.split(" ")
    print(str(tokens))

# Use with statement and some other ways to read-write
with open("C:\\GenAI\\ai_ml\\AI-ML\\advance_python\\read_test.txt", "r") as f:
    for line in f:
        tokens = line.strip().split(':')
        print(str(tokens))
        
with open("C:\\GenAI\\ai_ml\\AI-ML\\advance_python\\read_test.txt", "a") as f:
    f.write("\n Reading Test successfully completed\n")


#Note: Using with is safe as it automatically closes the file