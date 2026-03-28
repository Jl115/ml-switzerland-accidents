"""
Base Model - Abstract Base Class for All ML Models

LEARNING GOALS:
- Understand abstract base classes (ABC)
- Learn common model interface patterns
- Practice type hints and docstrings

TODO: Implement this class following the comments
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Tuple
import numpy as np


class BaseModel(ABC):
    """
    Abstract base class for all machine learning models.
    
    Every model must implement:
    - fit(): Train the model on data
    - predict(): Make predictions on new data
    - get_params(): Return model parameters
    - set_params(): Set model parameters
    
    Attributes:
        is_fitted (bool): Whether model has been trained
        params (Dict): Model hyperparameters
    """
    
    def __init__(self, **kwargs):
        """
        Initialize model with hyperparameters.
        
        Args:
            **kwargs: Hyperparameters specific to each model
            
        Example:
            >>> model = LinearRegression(learning_rate=0.01, n_iterations=1000)
        """
        # TODO: Store hyperparameters in self.params
        # TODO: Set self.is_fitted = False
        pass
    
    @abstractmethod
    def fit(self, X: np.ndarray, y: np.ndarray) -> 'BaseModel':
        """
        Train the model on training data.
        
        Args:
            X: Feature matrix of shape (n_samples, n_features)
            y: Target vector of shape (n_samples,)
            
        Returns:
            self: The fitted model
            
        Raises:
            ValueError: If data shapes don't match
            
        Example:
            >>> X = np.array([[1, 2], [3, 4], [5, 6]])
            >>> y = np.array([1, 2, 3])
            >>> model.fit(X, y)
        """
        # TODO: Implement training logic in child classes
        # TODO: Validate input shapes
        # TODO: Set self.is_fitted = True after training
        # TODO: Return self for method chaining
        pass
    
    @abstractmethod
    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Make predictions on new data.
        
        Args:
            X: Feature matrix of shape (n_samples, n_features)
            
        Returns:
            predictions: Predicted values of shape (n_samples,)
            
        Raises:
            NotFittedError: If model hasn't been trained yet
            
        Example:
            >>> X_test = np.array([[7, 8], [9, 10]])
            >>> predictions = model.predict(X_test)
        """
        # TODO: Check if model is fitted (raise error if not)
        # TODO: Implement prediction logic in child classes
        # TODO: Return predictions as numpy array
        pass
    
    @abstractmethod
    def get_params(self) -> Dict[str, Any]:
        """
        Get model hyperparameters.
        
        Returns:
            params: Dictionary of hyperparameters
            
        Example:
            >>> params = model.get_params()
            >>> print(params)
            {'learning_rate': 0.01, 'n_iterations': 1000}
        """
        # TODO: Return copy of self.params
        pass
    
    @abstractmethod
    def set_params(self, **params) -> 'BaseModel':
        """
        Set model hyperparameters.
        
        Args:
            **params: Hyperparameters to set
            
        Returns:
            self: Model with updated parameters
            
        Example:
            >>> model.set_params(learning_rate=0.001, n_iterations=2000)
        """
        # TODO: Update self.params with new values
        # TODO: Return self for method chaining
        pass
    
    def score(self, X: np.ndarray, y: np.ndarray) -> float:
        """
        Calculate model performance score (accuracy for classification,
        R² for regression).
        
        Args:
            X: Feature matrix
            y: True target values
            
        Returns:
            score: Performance score (0-1 for accuracy, -∞ to 1 for R²)
            
        Note:
            Override this method in child classes for specific metrics
        """
        # TODO: Implement in child classes based on model type
        # TODO: For classification: return accuracy
        # TODO: For regression: return R² score
        pass
    
    def __repr__(self) -> str:
        """
        String representation of the model.
        
        Returns:
            String showing model name and parameters
            
        Example:
            >>> print(model)
            LinearRegression(learning_rate=0.01, n_iterations=1000)
        """
        # TODO: Format model name and params as string
        pass


class NotFittedError(Exception):
    """
    Exception raised when trying to predict with unfitted model.
    
    TODO: Use this in predict() methods when is_fitted is False
    """
    pass
