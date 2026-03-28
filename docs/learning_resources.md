# 📚 Learning Resources - ML Switzerland

Curated resources for learning machine learning while building the Switzerland accidents project.

---

## 🎯 Learning Path by Week

### Week 1-2: Python & OOP Foundations

**Topics:**
- Classes & Objects
- Inheritance & Polymorphism
- Magic methods (`__init__`, `__repr__`, `__str__`)
- Type hints
- Error handling

**Resources:**
1. [Python OOP Tutorial (Corey Schafer)](https://www.youtube.com/watch?v=ZDa-Z5JzLYM) - 4 part series
2. [Real Python - OOP in Python 3](https://realpython.com/python3-object-oriented-programming/)
3. [Python Type Checking Guide](https://realpython.com/python-type-checking/)

**Practice:**
- Implement `BaseModel` class
- Create custom exceptions
- Add type hints to all functions

---

### Week 3-4: NumPy & Pandas Mastery

**Topics:**
- Array operations
- Broadcasting
- DataFrame manipulation
- GroupBy operations
- Time series handling

**Resources:**
1. [NumPy Quickstart Tutorial](https://numpy.org/doc/stable/user/quickstart.html)
2. [Pandas Documentation - 10 Minutes to Pandas](https://pandas.pydata.org/docs/user_guide/10min.html)
3. [Kaggle - Pandas Course](https://www.kaggle.com/learn/pandas) - Free interactive

**Practice:**
- Load Swiss canton data
- Merge accident + weather datasets
- Group accidents by canton/month

---

### Week 5-6: Data Visualization

**Topics:**
- Matplotlib basics
- Seaborn statistical plots
- Distribution plots
- Correlation heatmaps
- Time series visualization

**Resources:**
1. [Matplotlib Tutorial (Python Graph Gallery)](https://python-graph-gallery.com/)
2. [Seaborn Tutorial (DataCamp)](https://www.datacamp.com/tutorial/seaborn-python-tutorial)
3. [Storytelling with Data](https://www.storytellingwithdata.com/blog)

**Practice:**
- Plot accident distribution by canton
- Create weather correlation heatmap
- Visualize seasonal accident patterns

---

### Week 7-8: Mathematics for ML

**Topics:**
- Linear Algebra (vectors, matrices, operations)
- Calculus (derivatives, gradients)
- Statistics (mean, variance, distributions)
- Probability (Bayes' theorem)

**Resources:**
1. [3Blue1Brown - Essence of Linear Algebra](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_abr) - Visual intuition
2. [Khan Academy - Linear Algebra](https://www.khanacademy.org/math/linear-algebra)
3. [StatQuest - Statistics Fundamentals](https://www.youtube.com/c/joshstarmer) - Easy explanations

**Practice:**
- Implement matrix multiplication from scratch
- Calculate gradients manually
- Compute probability distributions of accidents

---

### Week 9-12: Machine Learning Algorithms

**Topics:**
- Linear Regression (from scratch)
- Logistic Regression
- Decision Trees
- Model Evaluation
- Cross-Validation

**Resources:**
1. [Andrew Ng - Machine Learning (Coursera)](https://www.coursera.org/learn/machine-learning) - Weeks 1-3
2. [ML from Scratch (GitHub)](https://github.com/eriklindernoren/ML-From-Scratch) - Code examples
3. [Scikit-learn Documentation](https://scikit-learn.org/stable/) - For comparison

**Practice:**
- Implement LinearRegression class
- Add gradient descent optimization
- Compare with sklearn implementation

---

## 📖 Books (Free PDFs)

1. **[The Hundred-Page Machine Learning Book](http://themlbook.com/wiki/doku.php)** - Quick overview
2. **[Pattern Recognition and Machine Learning](http://users.isr.ist.utl.pt/~wurml/LVCS2010/PRML_book.pdf)** - Deep theory
3. **[Hands-On Machine Learning](https://github.com/ageron/handson-ml2)** - Practical code

---

## 🎓 Online Courses (Free)

| Platform | Course | Time | Certificate |
|----------|--------|------|-------------|
| Coursera | [Machine Learning (Andrew Ng)](https://www.coursera.org/learn/machine-learning) | 11 weeks | Paid (audit free) |
| edX | [MIT Intro to Deep Learning](https://www.edx.org/course/introduction-to-deep-learning) | 6 weeks | Free |
| Udacity | [Intro to Machine Learning](https://www.udacity.com/course/intro-to-machine-learning-nanodegree--nd229) | 4 weeks | Paid |
| Kaggle | [Micro-Courses](https://www.kaggle.com/learn) | 4-8 hours each | Free |
| Fast.ai | [Practical Deep Learning](https://www.fast.ai/) | 7 weeks | Free |

**Recommendation:** Start with Kaggle micro-courses (fast, practical), then Andrew Ng (deep understanding)

---

## 🇨🇭 Swiss Data Sources

### Official Government Data

1. **[Bundesamt für Statistik (BFS)](https://www.bfs.admin.ch/bfs/de/home.html)**
   - Traffic accident statistics
   - Cantonal data
   - Historical trends
   - Download: Excel, CSV, API

2. **[MeteoSwiss](https://www.meteoswiss.admin.ch/home.html)**
   - Historical weather data
   - Temperature, precipitation, snow
   - Station data by canton
   - API access available

3. **[Open Data Switzerland](https://handbook.opendata.ch/en/)**
   - Portal to all Swiss open data
   - Cantonal portals linked
   - Search by topic

### Traffic Data

4. **[Viasuisse](https://www.viasuisse.ch/)**
   - Traffic flow data
   - Road conditions
   - Accident reports

5. **[ASTRA (Federal Roads Office)](https://www.astra.admin.ch/astra/de/home.html)**
   - Road infrastructure
   - Traffic volume statistics

---

## 💻 Coding Practice Platforms

1. **[LeetCode](https://leetcode.com/)** - Algorithm practice
2. **[HackerRank](https://www.hackerrank.com/)** - Python challenges
3. **[Exercism](https://exercism.org/tracks/python)** - Python exercises with mentorship
4. **[Codewars](https://www.codewars.com/)** - Kata challenges

---

## 🧪 Experiment Tracking

1. **[MLflow](https://mlflow.org/)** - Track experiments, models
2. **[Weights & Biases](https://wandb.ai/)** - Free tier available
3. **[TensorBoard](https://www.tensorflow.org/tensorboard)** - Visualization

**For this project:** Start with simple CSV logging, add MLflow later

---

## 📝 Note-Taking Tools

1. **[Jupyter Notebooks](https://jupyter.org/)** - Code + notes together
2. **[Obsidian](https://obsidian.md/)** - Knowledge base (markdown)
3. **[Notion](https://www.notion.so/)** - Project management

**Recommendation:** Use notebooks for code experiments, Obsidian for concepts

---

## 🤝 Communities

1. **[r/MachineLearning](https://www.reddit.com/r/MachineLearning/)** - News & discussions
2. **[r/learnmachinelearning](https://www.reddit.com/r/learnmachinelearning/)** - Beginner-friendly
3. **[Kaggle Forums](https://www.kaggle.com/discussion)** - Help & tips
4. **[Stack Overflow](https://stackoverflow.com/questions/tagged/machine-learning)** - Q&A

---

## 📅 Weekly Study Plan Template

```markdown
## Week X: [Topic]

### Goals
- [ ] Complete [course/module]
- [ ] Implement [feature]
- [ ] Read [chapter/article]

### Learnings
- Concept 1: [Explanation]
- Concept 2: [Explanation]

### Challenges
- Problem: [Description]
- Solution: [How I solved it]

### Code Snippets
```python
# Best code from this week
```

### Next Week
- [ ] Continue with [topic]
- [ ] Start [new feature]
```

---

## 🎯 Project Milestones

| Milestone | Target Date | Status |
|-----------|-------------|--------|
| Complete OOP basics | Week 2 | ⏳ |
| Load first dataset | Week 3 | ⏳ |
| EDA complete | Week 4 | ⏳ |
| First model from scratch | Week 6 | ⏳ |
| Model evaluation | Week 8 | ⏳ |
| Final project complete | Week 12 | ⏳ |

---

**Tip:** Don't try to learn everything at once. Build, get stuck, research, implement, repeat! 🚀

*Last Updated: 2026-03-28*
