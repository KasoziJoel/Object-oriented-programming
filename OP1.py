

students = [

{'student_name': 'John','meal_type': 'Pizza','Daily_price': '2500'},
{'student_name': 'Sarah','meal_type': 'Burger','Daily_price': '2000'},
{'student_name': 'Mike','meal_type': 'Pasta','Daily_price': '2200'},
{'student_name': 'Grace','meal_type': 'Chicken and Rice','Daily_price': '3500'},
{'student_name': 'Peter','meal_type': 'Pizza','Daily_price': '2500'} 

]


print("\n========== STUDENT MEAL REPORT ==========")

# 1. Weekly spending for each student
print("\n--- Student Weekly Spending ---")

for student in students:
    daily_price = int(student['Daily_price'])
    weekly_price = daily_price * 5

    print(f"{student['student_name']}: {weekly_price}")

# 2. Students spending more than 15,000
print("\n--- Students Spending More Than 15,000 ---")

for student in students:
    daily_price = int(student['Daily_price'])
    weekly_price = daily_price * 5

    if weekly_price > 15000:
        print(f"{student['student_name']}: {weekly_price}")

# 3. Revenue by meal type
print("\n--- Weekly Revenue by Meal Type ---")

weekly_revenue = {}

for student in students:
    meal = student['meal_type']
    daily_price = int(student['Daily_price'])

    if meal not in weekly_revenue:
        weekly_revenue[meal] = 0

    weekly_revenue[meal] += daily_price * 5

for meal, revenue in weekly_revenue.items():
    print(f"{meal}: {revenue}")

# 4. Most popular meal
print("\n--- Most Popular Meal ---")

grouped = {}

for student in students:
    meal = student['meal_type']

    if meal not in grouped:
        grouped[meal] = []

    grouped[meal].append(student['student_name'])

most_popular = max(grouped, key=lambda meal: len(grouped[meal]))

print(f"Meal: {most_popular}")
print(f"Students: {len(grouped[most_popular])}")

print("\n==========================================")