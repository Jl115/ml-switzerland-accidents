# 🇨🇭 ML Switzerland - Real Swiss Geodata Learning

**Project:** Learn machine learning by building algorithms from scratch using REAL Swiss geospatial data

**Dataset:** 112,145 land cover features from Kanton Uri (100% official Swiss government data)

**Learning Goal:** Build a complete machine learning pipeline from scratch using object-oriented programming

**Data Policy:** ONLY REAL DATA - No synthetic or dummy data for training

---

## 🎯 Project Objective

Build a model that predicts:
1. **Where** car accidents are most likely to occur (by canton/region)
2. **How** weather conditions impact accident frequency
3. **When** high-risk periods occur (seasonal patterns)

---

## 📚 Learning Path (Using REAL Uri Geodata)

### Phase 1: Foundations (Weeks 1-2)
- [x] Python OOP fundamentals
- [x] Data structures for ML
- [x] NumPy & Pandas mastery
- [ ] Data visualization (Matplotlib, Seaborn, Folium for maps)
- [ ] **START HERE:** Load Uri geodata, create first maps

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
│   │   ├── data_loader.py          # TODO: Load data from CSV/APIs
│   │   ├── data_validator.py       # TODO: Validate data quality
│   │   └── dataset.py              # TODO: Dataset class with getitem/len
│   ├── preprocessing/
│   │   ├── cleaner.py              # TODO: Handle missing values
│   │   ├── normalizer.py           # TODO: Feature scaling
│   │   ├── encoder.py              # TODO: Categorical encoding
│   │   └── feature_engineer.py     # TODO: Create new features
│   ├── models/
│   │   ├── base_model.py           # TODO: Abstract base class for all models
│   │   ├── linear_regression.py    # TODO: Implement from scratch
│   │   ├── logistic_regression.py  # TODO: Implement from scratch
│   │   ├── decision_tree.py        # TODO: Implement from scratch
│   │   └── neural_network.py       # TODO: Implement from scratch
│   ├── evaluation/
│   │   ├── metrics.py              # TODO: Accuracy, Precision, Recall, F1, RMSE
│   │   ├── cross_validator.py      # TODO: K-fold cross-validation
│   │   └── visualizer.py           # TODO: Confusion matrix, ROC curves
│   └── utils/
│       ├── logger.py               # TODO: Logging utility
│       ├── config.py               # TODO: Configuration management
│       └── helpers.py              # TODO: Helper functions
├── notebooks/
│   ├── 01_data_exploration.ipynb   # TODO: EDA notebook
│   ├── 02_preprocessing.ipynb      # TODO: Preprocessing experiments
│   ├── 03_model_training.ipynb     # TODO: Model training experiments
│   └── 04_evaluation.ipynb         # TODO: Model evaluation
├── data/
│   ├── raw/                        # Original data (DO NOT MODIFY)
│   ├── processed/                  # Cleaned, ready-to-use data
│   └── external/                   # Third-party data
├── tests/
│   ├── test_data_loader.py         # TODO: Test data loading
│   ├── test_preprocessing.py       # TODO: Test preprocessing
│   └── test_models.py              # TODO: Test model predictions
├── docs/
│   ├── learning_resources.md       # Curated learning materials
│   ├── project_plan.md             # Detailed project plan
│   └── api_reference.md            # Class/function documentation
├── resources/
│   ├── swiss_cantons.json          # Canton codes & names
│   └── weather_codes.json          # Weather condition codes
├── requirements.txt                # Python dependencies
├── setup.py                        # Package installation
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

### 1. Install uv (if you haven't already)
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

# Install package in development mode
uv pip install -e .
```

### 3. Verify Setup
```bash
# Check Python version
python --version

# Check installed packages
uv pip list

# Run a test
pytest tests/ -v
```

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

## 📊 Available Real Data

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

### 🔍 More Real Data Sources (To Download)

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
- [ ] Collect, clean, and preprocess real-world data
- [ ] Evaluate models with proper metrics
- [ ] Deploy a working prediction system
- [ ] Understand mathematical foundations
- [ ] Write clean, modular, testable code

---

## 📝 How to Use This Repo

1. **Read TODO comments** - They guide what to implement
2. **Start simple** - Don't over-engineer initially
3. **Test frequently** - Write tests before/after code
4. **Document learnings** - Add comments explaining concepts
5. **Ask questions** - When stuck, research or ask for help
6. **Iterate** - First version doesn't need to be perfect

---

## 🧠 Weekly Check-ins

Every week, update `docs/weekly_progress.md`:
- What did I learn?
- What challenges did I face?
- What's next week's goal?
- Code snippets that helped

---

**Remember:** The goal is **learning**, not perfection. Build, break, fix, repeat! 🚀

*Last Updated: 2026-03-28*
*Created by: J (with Lexy's guidance)*
