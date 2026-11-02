# House Price Prediction Using Linear Regression

A beginner-friendly Machine Learning mini-project using Python and Simple Linear Regression.

## Features
- Creates a small sample dataset of house areas and prices.
- Splits data into training and testing sets.
- Trains a `LinearRegression` model.
- Predicts prices for test records and a new 1,600 sq. ft. house.
- Reports MAE, MSE, RMSE, and R².
- Saves a graph as `regression_plot.png`.

## Requirements
- Python 3.9 or later recommended
- Libraries listed in `requirements.txt`

## How to run
1. Extract the ZIP file.
2. Open a terminal/command prompt in this folder.
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the project:

   ```bash
   python main.py
   ```

The program prints the results and opens a graph. It also saves `regression_plot.png` in the project folder.

## Dataset note
The included dataset is illustrative data made for learning. Prices are in Indian rupees lakhs and areas are in square feet. It is not real property-market data, and the model should not be used to estimate actual property values.

## Project summary
- **Input feature:** House area (sq. ft.)
- **Target:** House price (₹ lakhs)
- **Algorithm:** Simple Linear Regression
- **Evaluation:** MAE, MSE, RMSE, R²
