# Project Report: House Price Prediction Using Linear Regression

## 1. Abstract
This project demonstrates the use of Simple Linear Regression to estimate a house price from its area in square feet. Python libraries are used for data handling, model training, evaluation, and visualization.

## 2. Problem Statement
Predict the approximate price of a house based on its area using a supervised Machine Learning algorithm.

## 3. Objectives
- Understand Simple Linear Regression.
- Prepare a small dataset.
- Train and test a regression model.
- Predict a price for a new house area.
- Evaluate model performance and plot the fitted line.

## 4. Tools and Technologies
- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Jupyter Notebook or a local Python environment

## 5. Theory
Simple Linear Regression models the relationship between one input variable and a continuous target using a straight line:

`ŷ = b₀ + b₁x`

Here, `ŷ` is the predicted price, `x` is the house area, `b₀` is the intercept, and `b₁` is the slope. The model estimates the line by minimizing the sum of squared residuals.

## 6. Dataset
The project uses the following illustrative dataset. Prices are in ₹ lakhs.

| Area (sq. ft.) | Price (₹ lakhs) |
|---:|---:|
| 500 | 15 |
| 700 | 20 |
| 900 | 25 |
| 1100 | 30 |
| 1300 | 35 |
| 1500 | 40 |
| 1700 | 45 |
| 1900 | 50 |
| 2100 | 55 |
| 2300 | 60 |

This data is created for learning and is not real market data.

## 7. Methodology
1. Import the required libraries.
2. Create the dataset.
3. Set `Area` as the input feature and `Price` as the target.
4. Split the data into training and test sets.
5. Train a Linear Regression model.
6. Predict test-set prices.
7. Calculate MAE, MSE, RMSE, and R².
8. Plot the actual data and fitted regression line.
9. Predict the price for a 1,600 sq. ft. house.

## 8. Evaluation Metrics
- **MAE:** Average absolute difference between actual and predicted values.
- **MSE:** Average squared difference between actual and predicted values.
- **RMSE:** Square root of MSE, in the target's units.
- **R²:** Indicates how well the model explains variation in the target.

## 9. Expected Result
For the constructed dataset, the underlying relationship is `Price = 2.5 + 0.025 × Area`. A 1,600 sq. ft. house therefore has an illustrative predicted price of ₹42.5 lakhs. Because the data follows an exact straight line, evaluation scores should be close to perfect.

## 10. Limitations
- The sample dataset is very small and artificial.
- Actual prices depend on location, property age, bedrooms, amenities, and market conditions.
- Extrapolating beyond the training data can be unreliable.
- Results are educational and should not be used for real property valuation.

## 11. Future Scope
The project can be extended using a real housing dataset and multiple features such as location, number of bedrooms, and property age. More advanced models can also be compared.

## 12. Conclusion
This project demonstrates the basic Machine Learning workflow: data preparation, model training, prediction, evaluation, and visualization using Simple Linear Regression.
