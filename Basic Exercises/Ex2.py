#Exercise 2: More strings
text = "  Hello, World! Welcome to Python Programming.  "
print("Stripped:", text.strip())
print("Number of words:", len(text.strip().split(" ")))
print("Title case:", text.strip().title())
print("Starts with 'Hello':", text.strip().startswith("Hello"))
print("Ends with 'ing.':", text.strip().endswith("ing."))
print("Position of the word 'Python':", text.strip().find("Python"))
text1 = text.strip().split(" ")
print("Joined:", "-".join(text1))