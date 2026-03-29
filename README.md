# 🇨🇭 ML Switzerland - Learn ML with Real Swiss Data

**Project:** Learn machine learning by building algorithms from scratch using REAL Swiss government data

**Current REAL Datasets:**
1. ✅ **Uri Geodata** - 112,145 land cover features (REAL, from Kanton Uri WMS)
2. ✅ **Frauenfeld Parking** - 10,800 hourly records (REAL, from opendata.swiss, updated March 28, 2026)

**Learning Goal:** Build a complete machine learning pipeline from scratch using object-oriented programming

**Data Policy:** ONLY REAL DATA - No synthetic or dummy data for training

---

## 🎯 Project Objective

Learn machine learning by building algorithms from scratch using REAL Swiss government data.

**Current Focus Datasets:**

1. **Frauenfeld Parking** (Recommended for beginners)
   - Predict parking availability (binary classification)
   - Time-series forecasting (when will spots be free?)
   - Pattern recognition (rush hour, weekends, events)

2. **Uri Geodata** (Advanced, geospatial)
   - Land use classification (what type of land cover?)
   - Geographic clustering (find natural regions)
   - Area prediction (how large are parcels?)

**All algorithms built from scratch - no sklearn black boxes!**

---

## 📚 Learning Path (Using REAL Swiss Data)

### Phase 1: Foundations (Weeks 1-2)
- [x] Python OOP fundamentals
- [x] Data structures for ML
- [x] NumPy & Pandas mastery
- [ ] Data visualization (Matplotlib, Seaborn, Folium for maps)
- [ ] **START HERE:** Choose your dataset:
  - Option A: Frauenfeld Parking (easier, time-series)
  - Option B: Uri Geodata (geospatial, larger dataset)

### Phase 2: Data Engineering (Weeks 3-4)
- [ ] Data cleaning & preprocessing (handle missing values)
- [ ] Feature engineering (create ML features from geodata)
- [ ] Exploratory Data Analysis (EDA)
- [ ] Geographic data handling (projections, coordinates)

### Phase 3: Machine Learning Basics (Weeks 5-7)
- [ ] Supervised vs Unsupervised learning
- [ ] **Implement from scratch:** Linear Regression
- [ ] **Implement from scratch:** Logistic Regression
- [ ] **Implement from scratch:** Decision Trees
- [ ] Model evaluation metrics (accuracy, precision, recall, F1)

### Phase 4: Advanced Topics (Weeks 8-10)
- [ ] **Implement from scratch:** K-Means Clustering
- [ ] Feature selection for geospatial data
- [ ] Hyperparameter tuning
- [ ] Cross-validation

### Phase 5: Deployment (Weeks 11-12)
- [ ] Model serialization
- [ ] API creation (FastAPI)
- [ ] Interactive map visualization
- [ ] Documentation

---

## 🏗️ Project Structure

```
ml-switzerland-accidents/
├── src/
│   ├── data/
│   │   ├── collect_uri_geodata.py         # ✅ Uri geodata collector (REAL data)
│   │   ├── collect_frauenfeld_parking.py  # ✅ Parking data collector (REAL data)
│   │   ├── data_loader.py                 # TODO: Generic data loading
│   │   └── data_validator.py              # TODO: Validate data quality
│   ├── preprocessing/
│   │   ├── cleaner.py              # TODO: Handle missing values
│   │   ├── normalizer.py           # TODO: Feature scaling
│   │   ├── encoder.py              # TODO: Categorical encoding
│   │   └── feature_engineer.py     # TODO: Create new features
│   ├── models/
│   │   ├── base_model.py           # ✅ Abstract base class (started)
│   │   ├── linear_regression.py    # TODO: Implement from scratch
│   │   ├── logistic_regression.py  # TODO: Implement from scratch
│   │   ├── decision_tree.py        # TODO: Implement from scratch
│   │   └── kmeans.py               # TODO: Implement from scratch
│   ├── evaluation/
│   │   ├── metrics.py              # TODO: Accuracy, Precision, Recall, F1, RMSE
│   │   └── cross_validator.py      # TODO: K-fold cross-validation
│   └── utils/
│       └── logger.py               # TODO: Logging utility
├── notebooks/
│   ├── 01_frauenfeld_parking_exploration.ipynb  # ✅ Parking EDA (ready to start)
│   └── 02_uri_geodata_exploration.ipynb         # ✅ Uri geodata EDA (ready to start)
├── data/
│   ├── raw/
│   │   ├── uri_geodata/           # ✅ 112,145 features from Kanton Uri
│   │   └── frauenfeld_parking/    # ✅ 10,800 records (March 2026)
│   ├── processed/
│   │   ├── uri_geodata_ml_ready.csv       # ✅ ML-ready Uri dataset
│   │   └── frauenfeld_parking_ml_ready.csv # ✅ ML-ready parking dataset
│   └── external/                  # For future datasets
├── tests/
│   ├── test_data_loader.py         # TODO: Test data loading
│   └── test_models.py              # TODO: Test model predictions
├── docs/
│   ├── learning_resources.md       # ✅ Curated learning materials
│   └── build_from_scratch.md       # ✅ Philosophy: No sklearn black boxes
├── resources/
│   └── swiss_cantons.json          # ✅ Canton codes & names
├── requirements.txt                # ✅ Python dependencies (uv managed)
└── README.md                       # This file
```

---

## 📖 Learning Resources

### Free Courses
1. **[Machine Learning by Andrew Ng (Coursera)](https://www.coursera.org/learn/machine-learning)** - Best foundational course
2. **[fast.ai - Practical Deep Learning](https://www.fast.ai/)** - Top-down approach
3. **[Kaggle Learn](https://www.kaggle.com/learn)** - Hands-on micro-courses
4. **[StatQuest with Josh Starmer (YouTube)](https://www.youtube.com/c/joshstarmer)** - Intuitive explanations

### Books (Free)
1. **[Hands-On Machine Learning](https://github.com/ageron/handson-ml2)** - Code examples
2. **[Pattern Recognition and Machine Learning](http://users.isr.ist.utl.pt/~wurml/LVCS2010/PRML_book.pdf)** - Mathematical foundation
3. **[The Hundred-Page Machine Learning Book](http://themlbook.com/wiki/doku.php)** - Quick reference

### Practice Platforms
1. **[Kaggle](https://www.kaggle.com/)** - Competitions & datasets
2. **[Google Colab](https://colab.research.google.com/)** - Free GPU for training
3. **[Hugging Face](https://huggingface.co/)** - Pre-trained models & datasets

### Swiss Data Sources
1. **[Bundesamt für Statistik (BFS)](https://www.bfs.admin.ch/)** - Official Swiss statistics
2. **[MeteoSwiss](https://www.meteoswiss.admin.ch/)** - Weather data
3. **[Viasuisse](https://www.viasuisse.ch/)** - Traffic data
4. **[Open Data Switzerland](https://handbook.opendata.ch/)** - Government open data

---

## 🚀 Getting Started

### 1. Install uv (Python Package Manager)
```bash
# On macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# On Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Verify installation
uv --version
```

### 2. Setup Project Environment
```bash
cd ml-switzerland-accidents

# Create virtual environment with uv
uv venv

# Activate environment
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install all dependencies
uv pip install -r requirements.txt
```

### 3. Verify Setup
```bash
# Check Python version (should be 3.9+)
python --version

# Check installed packages
uv pip list

# List available datasets
ls data/processed/
```

### 4. Choose Your Starting Dataset

**🇨🇭 Uri Geodata (CURRENT FOCUS - Recommended for Learning)**
```bash
# Open Jupyter notebook
jupyter notebook notebooks/02_uri_geodata_exploration.ipynb
```
- 58,689 land parcels with real Swiss geodata
- Multi-class classification (27 land cover types)
- Learn: Decision Trees, feature engineering, categorical encoding

**Option B: Frauenfeld Parking (Alternative - Time Series)**
```bash
# Open Jupyter notebook
jupyter notebook notebooks/01_frauenfeld_parking_exploration.ipynb
```
- 10,800 parking records (easier, binary classification)
- Time-series patterns, rush hour prediction

### 2. Start with Notebooks
1. Open `notebooks/01_data_exploration.ipynb`
2. Follow the TODO comments
3. Run cells and experiment

### 3. Build Modules
1. Start with `src/data/data_loader.py`
2. Implement TODOs one by one
3. Write tests as you go

### 4. Track Progress
- Update `docs/project_plan.md` weekly
- Commit code with descriptive messages
- Document learnings in notebook comments

---

## 📊 Available REAL Datasets

### ✅ Uri Geodata (REAL - 100% Official Swiss Data)
**Source:** Kanton Uri WMS/WFS (https://geo.ur.ch/wms)

**Land Cover Data:**
- **58,689 land parcels** (buildings, roads, forest, water, agriculture)
- **53,445 individual objects** (small geographic features)
- **11 protected biotopes** (conservation areas)
- **Coordinates:** Swiss LV95 / WGS84
- **File:** `data/raw/uri_geodata/uri_bodenbedeckung.csv`

**ML Tasks:**
- Land use classification (what type of land cover?)
- Geographic clustering (find natural regions)
- Area prediction (how large are parcels?)
- Object detection (identify small features)

### ✅ Frauenfeld Parking (REAL - Updated March 28, 2026!)
**Source:** opendata.swiss (Canton Thurgau)

**Parking Data:**
- **10,800 hourly records** (90 days, 5 locations)
- **5 parking locations** in Frauenfeld (Unteres Mätteli, Oberes Mätteli, Marktplatz, Bahnhof)
- **Real-time occupancy** data
- **Weather correlation** included
- **File:** `data/processed/frauenfeld_parking_ml_ready.csv`

**ML Tasks:**
- Predict hard-to-find parking (binary classification)
- Time-series forecasting (when will spots be free?)
- Pattern recognition (rush hour, weekends, events)
- Weather impact analysis

### 🔍 More Real Data Sources (Optional Extensions)

**Swiss Accident Data:**
- **Source:** BFS (Bundesamt für Statistik)
- **URL:** https://www.pxweb.bfs.admin.ch/pxweb/de/px-x-1106010100_103/
- **Format:** Manual download → CSV
- **Instructions:** See `docs/download_real_data.md`

**Swiss Weather Data:**
- **Source:** MeteoSwiss
- **URL:** https://www.meteoswiss.admin.ch/home.html
- **Alternative:** Open-Meteo API (free, no key needed)

**Air Quality Data:**
- **Source:** opendata.swiss
- **URL:** https://opendata.swiss/en/dataset/stickstoffdioxid-no
- **Format:** WFS download → CSV

---

## 🎓 Key Concepts to Learn

### Object-Oriented Programming
- Classes & Objects
- Inheritance & Polymorphism
- Encapsulation
- Abstract Base Classes
- Design Patterns (Factory, Strategy, Observer)

### Machine Learning
- **Supervised Learning:** Regression, Classification
- **Unsupervised Learning:** Clustering, Dimensionality Reduction
- **Model Evaluation:** Cross-validation, Metrics
- **Feature Engineering:** Selection, Transformation
- **Hyperparameter Tuning:** Grid Search, Random Search

### Mathematics
- **Linear Algebra:** Vectors, Matrices, Operations
- **Calculus:** Derivatives, Gradients, Optimization
- **Statistics:** Distributions, Hypothesis Testing
- **Probability:** Bayes' Theorem, Conditional Probability

---

## ✅ Success Criteria

By project completion, you should be able to:
- [ ] Build ML models from scratch (no sklearn black boxes)
- [ ] Explain every line of code in your models
- [ ] Work with REAL Swiss government data
- [ ] Clean and preprocess real-world datasets
- [ ] Evaluate models with proper metrics (accuracy, precision, recall, F1)
- [ ] Deploy a working prediction system
- [ ] Understand mathematical foundations (gradient descent, decision trees, clustering)
- [ ] Write clean, modular, testable code
- [ ] Create data visualizations and explore patterns

---

## 📝 How to Use This Repo

1. **Choose a dataset** - Start with Frauenfeld Parking (easier) or Uri Geodata (advanced)
2. **Explore the data** - Open the corresponding Jupyter notebook
3. **Implement algorithms from scratch** - Follow the learning path
4. **Build incrementally** - Start with simple models, then advance
5. **Test your implementations** - Compare with sklearn (for validation only)
6. **Document learnings** - Add comments explaining concepts
7. **Ask questions** - When stuck, research or ask for help

---

## 🧠 Weekly Check-ins

Every week, update `docs/weekly_progress.md`:
- What did I learn?
- What challenges did I face?
- What's next week's goal?
- Code snippets that helped

---

## 📊 Dataset Summary

### Frauenfeld Parking (Recommended for Beginners)
- **Records:** 10,800 hourly measurements
- **Time Period:** 90 days (Jan-Mar 2026)
- **Locations:** 5 parking lots in Frauenfeld
- **Features:** occupancy_rate, hour, day_of_week, weather, is_rush_hour
- **Target:** hard_to_find_parking (binary: 0 or 1)
- **ML Tasks:** Binary classification, time-series forecasting
- **File:** `data/processed/frauenfeld_parking_ml_ready.csv`

### Uri Geodata (Advanced, Geospatial)
- **Records:** 112,145 geographic features
- **Source:** Kanton Uri WMS/WFS (official Swiss government data)
- **Layers:** 
  - 58,689 land parcels (buildings, roads, forest, water, agriculture)
  - 53,445 individual objects
  - 11 protected biotopes
- **Features:** area, land_cover_type, coordinates, quality
- **Target:** land_cover_type (multi-class) or area (regression)
- **ML Tasks:** Classification, clustering, regression
- **File:** `data/raw/uri_geodata/uri_bodenbedeckung.csv`

---

## 🎯 Quick Start Guide

**Complete Beginner?** Start here:
1. Open `notebooks/01_frauenfeld_parking_exploration.ipynb`
2. Run all cells to explore the data
3. Implement your first model in `src/models/logistic_regression.py`
4. Train and evaluate your model

**Have ML Experience?** Try this:
1. Open `notebooks/02_uri_geodata_exploration.ipynb`
2. Explore the geospatial data
3. Implement Decision Tree from scratch
4. Classify land cover types

---

**Remember:** The goal is **learning**, not perfection. Build, break, fix, repeat! 🚀

*Last Updated: 2026-03-29*
*Created by: J (with Lexy's guidance)*
*Data Sources: Kanton Uri WMS, opendata.swiss (Canton Thurgau)*
