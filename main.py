# House Price Prediction Using Linear Regression
# Run: python main.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def main():
    # Sample educational dataset; prices are in INR lakhs.
    data = {
        "Area": [500, 700, 900, 1100, 1300, 1500, 1700, 1900, 2100, 2300],
        "Price": [15, 20, 25, 30, 35, 40, 45, 50, 55, 60],
    }
    df = pd.DataFrame(data)

    print("\\nHOUSE PRICE PREDICTION USING LINEAR REGRESSION")
    print("=" * 48)
    print("\\nDataset:")
    print(df.to_string(index=False))

    X = df[["Area"]]
    y = df["Price"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    print("\\nModel training completed.")
    print(f"Intercept: {model.intercept_:.4f}")
    print(f"Slope: {model.coef_[0]:.4f}")
    print("\\nTest results:")
    results = pd.DataFrame({
        "Area (sq. ft.)": X_test["Area"].values,
        "Actual Price (₹ lakhs)": y_test.values,
        "Predicted Price (₹ lakhs)": np.round(y_pred, 2),
    })
    print(results.to_string(index=False))

    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)

    print("\\nEvaluation metrics:")
    print(f"MAE:  {mae:.4f}")
    print(f"MSE:  {mse:.4f}")
    print(f"RMSE: {rmse:.4f}")
    print(f"R²:   {r2:.4f}")

    new_area_value = 1600
    new_area = pd.DataFrame({"Area": [new_area_value]})
    predicted_price = model.predict(new_area)[0]
    print(f"\\nEstimated price for a {new_area_value} sq. ft. house: "
          f"₹{predicted_price:.2f} lakhs")

    # Plot observed data and fitted regression line.
    x_line = pd.DataFrame({"Area": np.linspace(X["Area"].min(), X["Area"].max(), 100)})
    plt.scatter(X["Area"], y, label="Actual data")
    plt.plot(x_line["Area"], model.predict(x_line), label="Regression line")
    plt.xlabel("House Area (sq. ft.)")
    plt.ylabel("House Price (₹ lakhs)")
    plt.title("House Price Prediction Using Linear Regression")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("regression_plot.png", dpi=150)
    print("\\nGraph saved as regression_plot.png")
    plt.show()


if __name__ == "__main__":
    main()
