"""
COVERS THE BASICS OF PYTHON
"""

from time import sleep


def tutorial():
    """
    A tutorial function demonstrating basic Python concepts through
    educational print statements with pauses between each topic.
    """

    print("=== WELCOME TO THE PYTHON TUTORIAL ===")
    sleep(1)

    print("\n--- VARIABLES AND DATA TYPES ---")
    sleep(1)
    print("Variables are containers that store values. Python has several basic data types:")
    sleep(1)
    print("- Integers (int): whole numbers like 42, -7, 0")
    sleep(1)
    print("- Floats (float): decimal numbers like 3.14, -2.5")
    sleep(1)
    print("- Strings (str): text enclosed in quotes like 'Hello' or \"World\"")
    sleep(1)
    print("- Booleans (bool): True or False values used for conditions")
    sleep(1)

    print("\n--- CREATING AND USING VARIABLES ---")
    sleep(1)
    name = "Python"
    age = 33
    version = 3.11
    is_powerful = True
    print(f"Variable 'name' stores: {name}")
    sleep(1)
    print(f"Variable 'age' stores: {age}")
    sleep(1)
    print(f"Variable 'version' stores: {version}")
    sleep(1)
    print(f"Variable 'is_powerful' stores: {is_powerful}")
    sleep(1)

    print("\n--- CONDITIONAL STATEMENTS (IF/ELSE) ---")
    sleep(1)
    print("Conditionals allow your code to make decisions based on conditions:")
    sleep(1)
    if age > 30:
        print(f"Python is {age} years old, which is older than 30!")
    else:
        print("Python is 30 or younger.")
    sleep(1)

    print("\n--- LOOPS: THE FOR LOOP ---")
    sleep(1)
    print("A for loop repeats code a specific number of times:")
    sleep(1)
    print("Counting from 1 to 5:")
    for i in range(1, 6):
        print(f"  Count: {i}")
        sleep(0.5)
    sleep(1)

    print("\n--- LOOPS: THE WHILE LOOP ---")
    sleep(1)
    print("A while loop repeats code as long as a condition is true:")
    sleep(1)
    print("Counting down from 3:")
    countdown = 3
    while countdown > 0:
        print(f"  {countdown}...")
        countdown -= 1
        sleep(0.5)
    print("  Blastoff!")
    sleep(1)

    print("\n--- LISTS (COLLECTIONS OF DATA) ---")
    sleep(1)
    print("A list is an ordered collection of items:")
    sleep(1)
    fruits = ["apple", "banana", "orange", "grape"]
    print(f"Our list of fruits: {fruits}")
    sleep(1)
    print("Accessing items by position (index starts at 0):")
    print(f"  First fruit (index 0): {fruits[0]}")
    sleep(1)
    print(f"  Last fruit (index -1): {fruits[-1]}")
    sleep(1)
    print("Looping through the list:")
    for fruit in fruits:
        print(f"  - {fruit}")
        sleep(0.5)
    sleep(1)

    print("\n--- DICTIONARIES (KEY-VALUE PAIRS) ---")
    sleep(1)
    print("A dictionary stores data as key-value pairs:")
    sleep(1)
    student = {
        "name": "Alice",
        "grade": "A",
        "age": 20,
        "major": "Computer Science"
    }
    print(f"Student dictionary: {student}")
    sleep(1)
    print("Accessing values by key:")
    print(f"  Student name: {student['name']}")
    sleep(1)
    print(f"  Student grade: {student['grade']}")
    sleep(1)

    print("\n--- DEFINING YOUR OWN FUNCTIONS ---")
    sleep(1)
    print("Functions are reusable blocks of code that perform specific tasks:")
    sleep(1)

    def greet(person_name):
        """A simple greeting function"""
        return f"Hello, {person_name}! Welcome to Python."

    print("Function defined: greet(person_name)")
    sleep(1)
    print("Calling the function:")
    greeting = greet("World")
    print(f"  {greeting}")
    sleep(1)

    print("\n--- FUNCTION WITH MULTIPLE PARAMETERS ---")
    sleep(1)

    def add_numbers(num1, num2):
        """A function that adds two numbers"""
        return num1 + num2

    result = add_numbers(15, 27)
    print(f"Adding 15 + 27 using our function: {result}")
    sleep(1)

    print("\n--- UNDERSTANDING SCOPE ---")
    sleep(1)
    print("Variables defined inside functions are local (only work inside that function)")
    print("Variables defined outside functions are global (work everywhere)")
    sleep(1)

    global_var = "I'm global"
    print(f"Global variable: {global_var}")

    def show_scope():
        local_var = "I'm local"
        print(f"Inside function - Local: {local_var}")
        print(f"Inside function - Global: {global_var}")

    show_scope()
    sleep(1)

    print("\n--- STRING MANIPULATION ---")
    sleep(1)
    text = "Python is awesome"
    print(f"Original string: '{text}'")
    sleep(1)
    print(f"Uppercase: '{text.upper()}'")
    sleep(1)
    print(f"Lowercase: '{text.lower()}'")
    sleep(1)
    print(f"First 6 characters: '{text[:6]}'")
    sleep(1)

    print("\n--- COMBINING CONCEPTS: A PRACTICAL EXAMPLE ---")
    sleep(1)
    print("Let's calculate the average of student scores:")
    sleep(1)

    scores = [85, 92, 78, 95, 88]
    print(f"Scores: {scores}")
    sleep(1)

    total = 0
    for score in scores:
        total += score

    average = total / len(scores)
    print(f"Average score: {average:.2f}")
    sleep(1)

    if average >= 90:
        print("Excellent performance! A-level work.")
    elif average >= 80:
        print("Good work! B-level performance.")
    elif average >= 70:
        print("Satisfactory work. C-level performance.")
    else:
        print("Needs improvement. Keep practicing!")
    sleep(1)

    print("\n=== TUTORIAL COMPLETE ===")
    print("say thanks")


# Run the tutorial
if __name__ == "__main__":
    pass
