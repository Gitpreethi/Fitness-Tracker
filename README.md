# Fitness-Tracker
# 🤖 Personalized Health Bot

The **Personalized Health Bot** is a lightweight AI-powered assistant that:
- Clusters users by body type and fitness goal
- Calculates BMI and classifies body type
- Recommends a weekly personalized workout plan
- Provides a sample daily diet plan
- Designed to be extensible into a chatbot or web app

---

## 🚀 Features

- 🔢 **BMI Calculation**: Detects underweight, normal, overweight, or obese.
- 🧬 **Body Type Classification**: Labels as Ectomorph, Mesomorph, or Endomorph based on BMI.
- 📊 **User Clustering**: Uses KMeans clustering on simulated health data.
- 🏋‍♂️ **Weekly Workout Plan**: 7-day schedule based on goal and body type.
- 🍽 **Basic Food Recommendation**: A simple nutrition suggestion for each day.
- 💡 **Custom Input Friendly**: Accepts user responses via CLI (terminal or Colab).

---

## 📦 Dataset

This project uses a **simulated dataset** (`workout_fitness_tracker_data.csv`) containing features like:
- Age, Weight, Height, Experience
- Fitness Level, Goal, Preferred Time
- Workout Location, Equipment Type

Each row is a synthetic user profile to help train the clustering model.

---

## 🛠 Technologies Used

- Python 🐍
- Pandas, NumPy for data handling
- Scikit-learn for clustering
- StandardScaler for normalization

---

## 🖥 How to Run

1. Clone this repo or open in Google Colab
2. Upload the `workout_fitness_tracker_data.csv`
3. Run the Python script and answer the questions
4. The bot will output:
    - Your BMI and body type
    - Cluster assignment
    - 7-day workout plan
    - Sample meal suggestions

---

## 🧠 Example Output
<img width="455" alt="image" src="https://github.com/user-attachments/assets/5f50b96f-6945-441d-8463-873d09a605c3" />
