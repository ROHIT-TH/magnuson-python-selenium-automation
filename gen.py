import random

# Sample data for names and designations
names = ["John", "Alice", "Bob", "Emily", "Michael", "Sara", "David", "Olivia", "Daniel", "Sophia"]
designations = ["Software Engineer", "Data Scientist", "Project Manager", "UX Designer", "Network Administrator",
                "Business Analyst", "System Administrator", "Product Manager", "QA Tester", "Technical Writer"]

# Generate 100 random entries
for i in range(1, 101):
    random_name = random.choice(names)
    random_designation = random.choice(designations)

    print(f"{i}\n\"{random_name}\"\n\"{random_designation}\"")
