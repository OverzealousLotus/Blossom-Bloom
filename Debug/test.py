"""Testing File for Python methods"""


with open("/home/karsonparker/Coding/Python/Debug/groceries.txt", "r", encoding="utf-8") as file:
    results: list[str] = file.read().split("\n")
    for item in results:
        if item == "Cereal":
            print("I do not need Cereal.")
        else:
            print(f"{item} is on my shopping list!")
