# 🧠 Build From Scratch Philosophy

**Core Principle:** You will implement ALL machine learning algorithms yourself to truly understand how they work.

---

## ✅ What You CAN Use (Infrastructure)

These libraries handle infrastructure, not ML logic:

### Data Handling
- **NumPy** - Array operations, linear algebra (you'll build ON TOP of this)
- **Pandas** - Loading CSV, data manipulation (NOT for ML algorithms)

### Visualization
- **Matplotlib** - Plotting graphs
- **Seaborn** - Statistical plots
- **Plotly** - Interactive visualizations

### Development
- **pytest** - Testing your implementations
- **black/flake8** - Code formatting
- **mypy** - Type checking
- **jupyter** - Experimentation notebooks

### Utilities
- **requests** - Downloading data from APIs
- **tqdm** - Progress bars
- **logging** - Debug output

---

## ❌ What You MUST Build Yourself (ML Algorithms)

### Phase 1: Basic Algorithms (Weeks 5-8)

#### 1. Linear Regression
**DON'T:** `from sklearn.linear_model import LinearRegression`

**DO:** Implement yourself:
```python
class LinearRegression:
    def __init__(self, learning_rate=0.01, n_iterations=1000):
        self.weights = None
        self.bias = None
        self.lr = learning_rate
        self.n_iters = n_iterations
    
    def fit(self, X, y):
        # TODO: Implement gradient descent
        # Calculate gradients
        # Update weights
        pass
    
    def predict(self, X):
        # TODO: Return X @ self.weights + self.bias
        pass
```

**Learn:**
- Cost function (MSE)
- Gradient descent
- Weight updates
- Learning rate impact

---

#### 2. Logistic Regression
**DON'T:** `from sklearn.linear_model import LogisticRegression`

**DO:** Implement yourself:
```python
class LogisticRegression:
    def sigmoid(self, z):
        # TODO: Implement 1 / (1 + exp(-z))
        pass
    
    def fit(self, X, y):
        # TODO: Implement gradient descent with sigmoid
        pass
    
    def predict(self, X):
        # TODO: Return binary predictions
        pass
```

**Learn:**
- Sigmoid function
- Binary cross-entropy loss
- Decision boundaries
- Probability outputs

---

#### 3. Decision Trees
**DON'T:** `from sklearn.tree import DecisionTreeClassifier`

**DO:** Implement yourself:
```python
class DecisionTree:
    def fit(self, X, y):
        # TODO: Implement recursive tree building
        # Calculate information gain
        # Find best split
        # Create child nodes
        pass
    
    def predict(self, X):
        # TODO: Traverse tree for each sample
        pass
```

**Learn:**
- Information gain / Gini impurity
- Recursive splitting
- Feature selection
- Overfitting prevention

---

#### 4. K-Nearest Neighbors
**DON'T:** `from sklearn.neighbors import KNeighborsClassifier`

**DO:** Implement yourself:
```python
class KNN:
    def fit(self, X, y):
        # TODO: Store training data
        pass
    
    def predict(self, X):
        # TODO: Find k nearest neighbors
        # Calculate distances
        # Vote on class
        pass
```

**Learn:**
- Distance metrics (Euclidean, Manhattan)
- Lazy learning
- Voting mechanisms
- Curse of dimensionality

---

### Phase 2: Advanced Algorithms (Weeks 9-12)

#### 5. Neural Networks
**DON'T:** `import torch.nn as nn` or `from tensorflow import keras`

**DO:** Implement yourself:
```python
class NeuralNetwork:
    def __init__(self, layers):
        # TODO: Initialize weights for each layer
        pass
    
    def forward(self, X):
        # TODO: Implement forward propagation
        # Apply weights and activations
        pass
    
    def backward(self, X, y, output):
        # TODO: Implement backpropagation
        # Calculate gradients
        pass
    
    def train(self, X, y):
        # TODO: Combine forward + backward
        pass
```

**Learn:**
- Forward propagation
- Backpropagation
- Activation functions (ReLU, sigmoid, tanh)
- Chain rule calculus

---

#### 6. K-Means Clustering
**DON'T:** `from sklearn.cluster import KMeans`

**DO:** Implement yourself:
```python
class KMeans:
    def fit(self, X):
        # TODO: Initialize centroids
        # TODO: Iterate until convergence
        # Assign clusters
        # Update centroids
        pass
    
    def predict(self, X):
        # TODO: Return cluster assignments
        pass
```

**Learn:**
- Unsupervised learning
- Centroid optimization
- Convergence criteria
- Elbow method

---

#### 7. Support Vector Machines
**DON'T:** `from sklearn.svm import SVC`

**DO:** Implement yourself (simplified):
```python
class SVM:
    def fit(self, X, y):
        # TODO: Implement gradient descent for hinge loss
        # Maximize margin
        pass
    
    def predict(self, X):
        # TODO: Return predictions based on decision boundary
        pass
```

**Learn:**
- Margin maximization
- Hinge loss
- Support vectors
- Kernel trick (later)

---

## ⚠️ When You CAN Use sklearn/torch

### For Comparison (AFTER building your own):

```python
# 1. Build your own implementation
my_model = LinearRegression(learning_rate=0.01)
my_model.fit(X_train, y_train)
my_predictions = my_model.predict(X_test)

# 2. Then compare with sklearn
from sklearn.linear_model import LinearRegression
sklearn_model = LinearRegression()
sklearn_model.fit(X_train, y_train)
sklearn_predictions = sklearn_model.predict(X_test)

# 3. Compare results
print(f"My accuracy: {accuracy(y_test, my_predictions)}")
print(f"sklearn accuracy: {accuracy(y_test, sklearn_predictions)}")
```

**This teaches you:**
- If your implementation is correct
- Performance differences
- Trade-offs in your approach

---

## 📊 What Counts as "Building Yourself"

### ✅ Valid Implementation:
```python
def linear_regression(X, y):
    # Initialize weights
    weights = np.zeros(X.shape[1])
    
    # Gradient descent loop
    for i in range(n_iterations):
        # Forward pass
        predictions = X @ weights
        
        # Calculate gradient
        gradient = (2/n_samples) * X.T @ (predictions - y)
        
        # Update weights
        weights -= learning_rate * gradient
    
    return weights
```

### ❌ NOT Valid:
```python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X, y)
return model.coef_
```

---

## 🎯 Learning Checklist

Before using any library, ask:

1. **Does this implement the ML algorithm?**
   - Yes → Build it yourself first
   - No → OK to use

2. **Will I understand every line if I use this?**
   - Yes → OK to use
   - No → Study the concept first

3. **Am I using this to avoid learning?**
   - Yes → Don't use it
   - No → Probably OK

---

## 🔍 Gray Areas (Case-by-Case)

### OK After Understanding:
- **scipy.optimize** - For optimization (after implementing gradient descent)
- **scipy.spatial.distance** - Distance calculations (after implementing Euclidean)
- **scikit-learn metrics** - Evaluation metrics (after implementing accuracy/F1 yourself)

### NOT OK:
- **scikit-learn estimators** - The actual ML models
- **torch.nn.Module** - Neural network layers
- **tensorflow.keras.Model** - Deep learning models

---

## 📝 Commitment

By using this project, you commit to:

- [ ] Building every ML algorithm from scratch
- [ ] Understanding the math behind each line
- [ ] Not copying implementations from StackOverflow
- [ ] Testing against sklearn (for validation only)
- [ ] Documenting your learnings

---

## 💡 Why This Matters

**Building from scratch teaches you:**

1. **Deep Understanding** - Not just API calls
2. **Debugging Skills** - When it breaks, you'll know why
3. **Mathematical Intuition** - Gradients, losses, optimizations
4. **Confidence** - You built it, you own it
5. **Interview Prep** - You can explain every detail

**Using black boxes teaches you:**

- How to import libraries 😅

---

## 🚀 The Path Forward

1. **Week 1-4:** Data handling, NumPy, Pandas (OK to use fully)
2. **Week 5-8:** Build basic ML algorithms from scratch
3. **Week 9-12:** Build advanced algorithms from scratch
4. **Week 13+:** Compare with sklearn, learn optimizations

---

**Remember:** The goal is learning, not speed. Take your time, understand each line! 🧠

*Last Updated: 2026-03-28*
