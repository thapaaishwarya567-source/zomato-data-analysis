🍽️ Zomato Restaurant Analysis

An interactive data analysis project that explores Zomato restaurant data to understand **restaurant ratings, cuisines, locations, online delivery availability, and average dining costs**.

The project combines **Python-based data analysis and an interactive Streamlit dashboard** to turn restaurant data into useful visual insights.

---

## 📌 Project Overview

This project analyzes restaurant data from Zomato and provides an interactive dashboard where users can filter the data by **city** and **online delivery availability**.

The dashboard displays key metrics and visualizations to help explore restaurant patterns across different locations.

### 🎯 Objectives

* Analyze restaurant ratings
* Explore popular cuisines
* Identify locations with the most restaurants
* Analyze online delivery availability
* Understand restaurant cost distribution
* Identify highly rated restaurants
* Create an interactive dashboard for data exploration

---

## 🛠️ Technologies Used

* **Python**
* **Pandas** – Data manipulation and cleaning
* **NumPy** – Numerical operations
* **Matplotlib** – Data visualization
* **Seaborn** – Statistical visualization
* **Streamlit** – Interactive dashboard
* **Jupyter Notebook** – Data analysis and exploration

---

## 🧹 Data Cleaning

Before analysis, the dataset is cleaned and prepared for visualization.

The project includes:

* Converting **Aggregate Rating** into a numeric format
* Cleaning the **Average Cost for two** column
* Removing commas from cost values
* Converting cost values into numeric data
* Handling invalid numeric values using `errors='coerce'`

These cleaning steps make the data suitable for further analysis.

---

## 📊 Interactive Dashboard

The Streamlit dashboard provides filters for:

### 🔍 Filters

* **City**
* **Online Delivery Availability**

The selected filters dynamically update the dashboard results.

---

## 📈 Dashboard Metrics

The dashboard displays three important KPIs:

| Metric               | Description                                  |
| -------------------- | -------------------------------------------- |
| 🍴 Total Restaurants | Number of restaurants after applying filters |
| ⭐ Average Rating     | Average restaurant rating                    |
| 💰 Average Cost      | Average cost for two people                  |

These metrics change based on the selected city and online-delivery filters.

---

## 📊 Visualizations

### 🏆 Top Restaurant Types / Cuisines

A bar chart displays the **top 10 cuisines** based on their frequency in the filtered dataset.

### 📦 Online Order Analysis

A count plot compares restaurants based on whether they provide **online delivery**.

### 📍 Top Locations

A bar chart shows the **top 10 cities/locations** with the highest number of restaurants.

### ⭐ Rating Distribution

A histogram with KDE is used to understand the distribution of restaurant ratings.

### 💰 Cost Distribution

A histogram with KDE shows how restaurant costs are distributed across the dataset.

### 🌟 Top Rated Restaurants

The dashboard displays a table containing the **top 10 restaurants by aggregate rating**, along with their city.

---

## 📂 Project Structure

```text
Zomato-Data-Analysis/
│
├── data/
│   └── zomato.csv
│
├── notebook/
│   └── zomato_analysis.ipynb
│
├── dashboard/
│   └── app.py
│
├── README.md
└── requirements.txt
```

---

## ▶️ How to Run the Dashboard

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the project

```bash
cd Zomato-Data-Analysis
```

### 3. Install the required libraries

```bash
pip install pandas matplotlib seaborn streamlit
```

### 4. Run the Streamlit application

```bash
python -m streamlit run web(zomato).py
```

The application will open in your browser.

---

## 💡 Key Insights

This project can be used to explore questions such as:

* Which locations have the highest number of restaurants?
* Which cuisines are most common?
* How are restaurant ratings distributed?
* What is the typical cost for two people?
* How common is online delivery?
* Which restaurants have the highest ratings?

---

## 🚀 Future Improvements

Possible improvements include:

* Add more interactive filters
* Add cuisine-level filtering
* Add price-range analysis
* Compare ratings across cities
* Analyze votes and rating relationships
* Add more advanced KPIs
* Deploy the Streamlit dashboard online
* Improve dashboard responsiveness

---

## 🎓 Skills Demonstrated

This project demonstrates practical skills in:

**Data Cleaning → Exploratory Data Analysis → Data Visualization → Python → Pandas → Seaborn → Streamlit → Dashboard Development**

---

## 👩‍💻 Author

**Aishwarya**

BCA – Data Science Student

---

⭐ If you find this project useful, consider giving the repository a star!
