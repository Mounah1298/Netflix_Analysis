# Netflix_Analysis
Quick exploratory data analysis of Netflix titles to extract insights on movies vs TV shows, popular genres, and release years

# Repository Structure

Netflix_Analysis/
│
├── data/netflix_cleaned.csv
├── notebooks/netflix_eda.ipynb
├── dashboard/netflix_dashboard.py
├── dashboard/run_dashboard.bat
└── README.md

# Features

Data Cleaning: missing values handled, multi-value columns exploded

EDA: top genres, titles per year, average duration, heatmaps

Dashboard: interactive filters for country, type, year, genre; bar charts, line charts, heatmaps, key metrics

# Installation & Run


 # create and activate environment
conda create -n netflix python=3.11
conda activate netflix

# After cloning the repo, you can install all dependencies at once:

```bash
conda create -n netflix python=3.11
conda activate netflix
pip install -r requirements.txt

# Install dependencies
conda install -c conda-forge streamlit plotly pandas seaborn matplotlib

 # run dashboard
cd dashboard
streamlit run netflix_dashboard.py
