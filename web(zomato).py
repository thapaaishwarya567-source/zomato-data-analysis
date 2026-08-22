
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------- PAGE SETTINGS ----------------
st.set_page_config(
    page_title="Zomato Analysis",
    page_icon="🍽️",
    layout="wide"
)

# ---------------- CUSTOM STYLE ----------------
st.markdown("""
<style>
.main {
    background-color: #0f172a;
    color: black;
}
h1, h2, h3 {
    color: #f97316;
}
[data-testid="metric-container"] {
    background-color: #1e293b;
    border-radius: 15px;
    padding: 20px;
    border: 1px solid #334155;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SEABORN STYLE ----------------
sns.set_style("darkgrid")

# ---------------- TITLE ----------------
st.title("🍽️ Zomato Restaurant Analysis Dashboard")
st.markdown("### Explore restaurant ratings, costs, online orders and top locations")

# ---------------- LOAD DATA ----------------
df = pd.read_csv(r"C:\Users\Aishwarya\OneDrive\Desktop\projects\zomato data set.csv",encoding='latin')

# ---------------- CLEAN DATA ----------------
df['Aggregate rating'] = pd.to_numeric(df['Aggregate rating'], errors='coerce')

df['Average Cost for two'] = (
    df['Average Cost for two']
    .astype(str)
    .str.replace(',', '')
)

df['Average Cost for two'] = pd.to_numeric(
    df['Average Cost for two'],
    errors='coerce'
)

# ---------------- SIDEBAR ----------------
st.sidebar.title("🔍 Filters")

City = st.sidebar.multiselect(
    "Select City",
    options=sorted(df['City'].dropna().unique()),
    default=sorted(df['City'].dropna().unique())[:5]
)

online_order = st.sidebar.multiselect(
    "Has Online delivery",
    options=df['Has Online delivery'].dropna().unique(),
    default=df['Has Online delivery'].dropna().unique()
)

# ---------------- FILTER DATA ----------------
filtered_df = df[
    (df['City'].isin(City)) &
    (df['Has Online delivery'].isin(online_order))
]

# ---------------- KPI SECTION ----------------
st.subheader("📌 Dashboard Metrics")

col1, col2, col3 = st.columns(3)

col1.metric(
    "🍴 Total Restaurants",
    filtered_df.shape[0]
)

col2.metric(
    "⭐ Average Rating",
    round(filtered_df['Aggregate rating'].mean(), 2)
)

col3.metric(
    "💰 Average Cost",
    f"₹ {round(filtered_df['Average Cost for two'].mean(), 0)}"
)

st.markdown("---")

# ---------------- TOP RESTAURANT TYPES ----------------
st.subheader("🏆 Top Restaurant Types")

top_types = filtered_df['Cuisines'].value_counts().head(10)

fig1, ax1 = plt.subplots(figsize=(12,6))

colors1 = sns.color_palette("magma", len(top_types))

bars = ax1.bar(
    top_types.index,
    top_types.values,
    color=colors1
)

ax1.set_facecolor("#111827")
fig1.patch.set_facecolor("#111827")

ax1.set_title(
    "Top 10 Restaurant Types",
    fontsize=18,
    color="white",
    weight='bold'
)

ax1.set_xlabel("Restaurant Type", color="white")
ax1.set_ylabel("Count", color="white")

ax1.tick_params(colors='white')

plt.xticks(rotation=45, ha='right')

# Labels
for bar in bars:
    height = bar.get_height()
    ax1.text(
        bar.get_x() + bar.get_width()/2,
        height,
        int(height),
        ha='center',
        color='white',
        fontsize=10
    )

st.pyplot(fig1)

# ---------------- ONLINE ORDER ANALYSIS ----------------
st.subheader("📦 Online Order Analysis")

fig2, ax2 = plt.subplots(figsize=(7,5))

sns.countplot(
    x='Has Online delivery',
    data=filtered_df,
    palette="coolwarm",
    ax=ax2
)

ax2.set_facecolor("#111827")
fig2.patch.set_facecolor("#111827")

ax2.set_title(
    "Online Orders",
    fontsize=18,
    color="white",
    weight='bold'
)

ax2.set_xlabel("Online Order", color="white")
ax2.set_ylabel("Count", color="white")

ax2.tick_params(colors='white')

# Labels
for p in ax2.patches:
    ax2.annotate(
        str(int(p.get_height())),
        (p.get_x() + p.get_width()/2., p.get_height()),
        ha='center',
        color='white',
        fontsize=10
    )

st.pyplot(fig2)

# ---------------- TOP LOCATIONS ----------------
st.subheader("📍 Top Locations")

top_locations = filtered_df['City'].value_counts().head(10)

fig3, ax3 = plt.subplots(figsize=(12,6))

sns.barplot(
    x=top_locations.index,
    y=top_locations.values,
    palette="viridis",
    ax=ax3
)

ax3.set_facecolor("#111827")
fig3.patch.set_facecolor("#111827")

ax3.set_title(
    "Top Restaurant Locations",
    fontsize=18,
    color="white",
    weight='bold'
)

ax3.set_xlabel("Location", color="white")
ax3.set_ylabel("Restaurants", color="white")

ax3.tick_params(colors='white')

plt.xticks(rotation=45, ha='right')

for p in ax3.patches:
    ax3.annotate(
        str(int(p.get_height())),
        (p.get_x() + p.get_width()/2., p.get_height()),
        ha='center',
        color='white',
        fontsize=10
    )

st.pyplot(fig3)

# ---------------- RATING DISTRIBUTION ----------------
st.subheader("⭐ Rating Distribution")

fig4, ax4 = plt.subplots(figsize=(10,5))

sns.histplot(
    filtered_df['Aggregate rating'],
    bins=20,
    kde=True,
    color="#f97316",
    ax=ax4
)

ax4.set_facecolor("#111827")
fig4.patch.set_facecolor("#111827")

ax4.set_title(
    "Restaurant Rating Distribution",
    fontsize=18,
    color="white",
    weight='bold'
)

ax4.set_xlabel("Ratings", color="white")
ax4.set_ylabel("Count", color="white")

ax4.tick_params(colors='white')

st.pyplot(fig4)

# ---------------- COST DISTRIBUTION ----------------
st.subheader("💰 Cost Distribution")

fig5, ax5 = plt.subplots(figsize=(10,5))

sns.histplot(
    filtered_df['Average Cost for two'],
    bins=20,
    kde=True,
    color="#38bdf8",
    ax=ax5
)

ax5.set_facecolor("#111827")
fig5.patch.set_facecolor("#111827")

ax5.set_title(
    "Cost Distribution",
    fontsize=18,
    color="white",
    weight='bold'
)

ax5.set_xlabel("Approx Cost", color="white")
ax5.set_ylabel("Count", color="white")

ax5.tick_params(colors='white')

st.pyplot(fig5)

# ---------------- TOP RATED RESTAURANTS ----------------
st.subheader("🌟 Top Rated Restaurants")

top_rated = filtered_df.sort_values(
    by='Aggregate rating',
    ascending=False
)[['Restaurant Name', 'Aggregate rating', 'City']].head(10)

st.dataframe(
    top_rated,
    use_container_width=True
)

# ---------------- RAW DATA ----------------
with st.expander("📄 View Dataset"):
    st.dataframe(
        filtered_df,
        use_container_width=True
    )
    #python -m streamlit run app.py ,Local URL: http://localhost:8501
    


