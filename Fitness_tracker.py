import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# ---------- Load and Prepare Dataset ----------
df = pd.read_csv("/content/workout_fitness_tracker_data.csv")

# Only select practical features for clustering
selected_features = ['Age', 'Weight (kg)', 'Height (cm)']
df = df.dropna(subset=selected_features)  # Drop rows with missing values in selected features

scaler = StandardScaler()
df_scaled = scaler.fit_transform(df[selected_features])

# ---------- Train KMeans ----------
kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(df_scaled)

# ---------- BMI and Body Type ----------
def calculate_bmi(weight, height):
    return weight / ((height / 100) ** 2)

def body_type_analysis(bmi):
    if bmi < 18.5:
        return 'Underweight', 'Ectomorph'
    elif 18.5 <= bmi < 24.9:
        return 'Normal weight', 'Mesomorph'
    elif 25 <= bmi < 29.9:
        return 'Overweight', 'Endomorph'
    else:
        return 'Obese', 'Endomorph'

# ---------- Plans ----------
def generate_workout_plan(cluster, goal):
    goal = goal.lower()
    plans = {
        0: {
            'fat loss': ["Cardio + HIIT", "Bodyweight HIIT", "Active Recovery",
                         "Core + Stretching", "Strength Training", "Rest", "Rest"],
            'muscle gain': ["Upper Body Strength", "Leg Day", "Core Stability",
                            "Strength Circuits", "Cardio + Abs", "Active Recovery", "Rest"],
            'flexibility': ["Yoga Flow", "Flexibility Training", "Active Recovery",
                            "Strength Training", "Core Stability", "Yoga + Stretching", "Rest"]
        },
        1: {
            'fat loss': ["HIIT Cardio", "Active Recovery", "Strength + Cardio Circuits",
                         "Core + Stretching", "HIIT + Bodyweight", "Full Body Strength", "Rest"],
            'muscle gain': ["Strength Training", "Leg Day", "Push/Pull Split",
                            "Strength Circuits", "Core Burn", "Cardio + Abs", "Rest"],
            'flexibility': ["Yoga", "Stretching + Flexibility", "Cardio + Abs",
                            "Yoga Flow", "Strength Training", "Rest", "Rest"]
        },
        2: {
            'fat loss': ["Bodyweight HIIT", "Cardio + Strength", "Core + Stability",
                         "HIIT + Full Body", "Cardio + Strength", "Active Recovery", "Rest"],
            'muscle gain': ["Strength Training", "Leg Day", "HIIT",
                            "Push/Pull Split", "Core + Stability", "Strength + Endurance", "Rest"],
            'flexibility': ["Yoga + Flexibility", "Active Recovery", "Cardio + Core",
                            "Yoga + Stretching", "Strength Training", "Rest", "Rest"]
        }
    }
    return plans.get(cluster, {}).get(goal, ["Custom Plan Needed"])

def generate_food_plan(goal):
    goal = goal.lower()
    return {
        'fat loss': [
            "Breakfast: Oatmeal + Fruits",
            "Lunch: Grilled Chicken + Vegetables",
            "Dinner: Salmon + Salad",
            "Snacks: Almonds + Greek Yogurt"
        ],
        'muscle gain': [
            "Breakfast: Scrambled Eggs + Avocado",
            "Lunch: Chicken + Quinoa + Veggies",
            "Dinner: Steak + Sweet Potatoes",
            "Snacks: Protein Shake + Nuts"
        ],
        'flexibility': [
            "Breakfast: Smoothie Bowl + Chia Seeds",
            "Lunch: Tofu Stir-Fry + Rice",
            "Dinner: Grilled Veggies + Lentils",
            "Snacks: Hummus + Veggie Sticks"
        ]
    }.get(goal, ["Custom Food Plan Needed"])

# ---------- Interactive Bot ----------
def interactive_bot():
    print("Welcome to the Personalized Health Bot!\n")

    # Get user input
    try:
        age = float(input("Enter your age: "))
        weight = float(input("Enter your weight (in kg): "))
        height = float(input("Enter your height (in cm): "))
    except ValueError:
        print("⚠️ Please enter valid numbers.")
        return

    fitness_goal = input("What's your fitness goal? (Fat Loss / Muscle Gain / Flexibility): ").strip().lower()

    # BMI analysis
    bmi = calculate_bmi(weight, height)
    status, body_type = body_type_analysis(bmi)
    print(f"\n🧮 BMI: {bmi:.2f} - {status}")
    print(f"🏷️ Body Type: {body_type}\n")

    # Predict cluster
    user_input = pd.DataFrame([[age, weight, height]], columns=selected_features)
    user_scaled = scaler.transform(user_input)
    cluster = kmeans.predict(user_scaled)[0]

    # print(f"🔍 Based on your input, you belong to cluster {cluster}\n")

    # Show plans
    workout_plan = generate_workout_plan(cluster, fitness_goal)
    print("🏋️‍♂️ Your 7-Day Personalized Workout Plan:")
    for i, plan in enumerate(workout_plan):
        print(f"Day {i+1}: {plan}")

    food_plan = generate_food_plan(fitness_goal)
    print("\n🍽️ Your Daily Food Plan:")
    for meal in food_plan:
        print(meal)

# Run the bot
interactive_bot()
