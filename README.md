# 🇨🇭 ML Switzerland - Car Accidents & Weather Analysis

**Project:** Predictive model for car accident hotspots in Swiss cantons based on weather conditions

**Learning Goal:** Build a complete machine learning pipeline from scratch using object-oriented programming

---

## 🎯 Project Objective

Build a model that predicts:
1. **Where** car accidents are most likely to occur (by canton/region)
2. **How** weather conditions impact accident frequency
3. **When** high-risk periods occur (seasonal patterns)

---

## 📚 Learning Path

### Phase 1: Foundations (Weeks 1-2)
- [ ] Python OOP fundamentals
- [ ] Data structures for ML
- [ ] NumPy & Pandas mastery
- [ ] Data visualization (Matplotlib, Seaborn)

### Phase 2: Data Engineering (Weeks 3-4)
- [ ] Data collection & scraping
- [ ] Data cleaning & preprocessing
- [ ] Feature engineering
- [ ] Exploratory Data Analysis (EDA)

### Phase 3: Machine Learning Basics (Weeks 5-7)
- [ ] Supervised vs Unsupervised learning
- [ ] Regression algorithms
- [ ] Classification algorithms
- [ ] Model evaluation metrics

### Phase 4: Advanced Topics (Weeks 8-10)
- [ ] Feature selection
- [ ] Hyperparameter tuning
- [ ] Cross-validation
- [ ] Ensemble methods

### Phase 5: Deployment (Weeks 11-12)
- [ ] Model serialization
- [ ] API creation
- [ ] Dashboard/visualization
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

### 1. Setup Environment
```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install package in development mode
pip install -e .
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

## 📊 Data Requirements

### Accident Data (To Collect)
- **Canton** (ZH, BE, LU, UR, SZ, etc.)
- **Date & Time** of incident
- **Location** (coordinates or region)
- **Severity** (minor, serious, fatal)
- **Vehicle type** (car, motorcycle, truck, etc.)
- **Road conditions** (dry, wet, icy, snow)

### Weather Data (To Collect)
- **Temperature** (°C)
- **Precipitation** (mm)
- **Snow depth** (cm)
- **Wind speed** (km/h)
- **Visibility** (km)
- **Weather condition** (sunny, rainy, snowy, foggy)

### Data Collection Strategy
1. **Accidents:** BFS database, police reports, news scraping
2. **Weather:** MeteoSwiss API, historical weather APIs
3. **Time Period:** 2020-2025 (5 years for good patterns)

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
