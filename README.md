# ⚙ PredictX – Predictive Maintenance for Industrial Machines

Welcome to *PredictX, a cutting-edge predictive maintenance system designed to detect machine failures *before they happen. Built using machine learning and Flask, this project aims to minimize downtime and improve operational efficiency across industrial systems.


## 🚀 Project Overview

Industrial machinery faces inevitable wear and tear, but unexpected breakdowns can cost companies time, money, and safety. PredictX leverages historical sensor data to *predict potential failures, giving industries the power to act *before damage occurs.

With a clean UI, Power BI dashboard, and an intelligent ML core, PredictX is your all-in-one solution for smart machine monitoring.


## 🧠 Tech Stack

| Layer                   | Tools & Frameworks                                  |
|-------------          --|---------------------------------------------------- |
| *Frontend*              | HTML and CSS     |
| *Backend*               | Python, Flask                                       |
| *Machine Learning*      | RandomForestClassifier (sklearn)                    |
| *Data*                  | Kaggle dataset: Predictive Maintenance              |
| *Dashboard*             | Microsoft Power BI (Static Screenshot Display)      |
| *Deployment*            | Render.com                                          |
| *Version Control*       | Git & GitHub                                        |


## 🔍 How It Works

1. *User uploads sensor data* via the interface.
2. *Flask backend* processes the input and feeds it to the trained ML model.
3. *ML model* predicts if failure is expected.
4. *Results displayed* instantly with clear alerts.
5. *Power BI Dashboard* (as a screenshot) showcases real-time analytics overview.


## 📝 Dataset

- 📦 Source: [Kaggle – Predictive Maintenance Dataset](https://www.kaggle.com/datasets)
- 🔢 Features used:
  - Air temperature [K]
  - Process temperature [K]
  - Rotational speed [rpm]
  - Torque [Nm]
  - Tool wear [min]
- 🎯 Target: Failure Type & Target (Binary classification)

### 1. Clone the repository

```bash
git clone https://github.com/Manisha378/PredictX--Predictive-maintenance-for-Industrial-Machines.git
cd PredictX--Predictive-maintenance-for-Industrial-Machines
