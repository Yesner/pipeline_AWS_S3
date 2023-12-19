import pandas as pd

# clean data
def clean_data(df):
    """
    Sales Transformation Function in Python with Error Handling
    :param df: pandas dataframe, extracted ecommerce data
    :return: pandas dataframe, transformed data
    """

    # Drop duplicate rows
    df = df.drop_duplicates()

    # Fill missing values in numeric columns with the mean
    df.fillna(df.mean(), inplace=True)

    # Drop rows with any remaining null values
    df.dropna(inplace=True)

    return df

# transform data
def transform_data(orders_df, products_df, customers_df):
    """
    Sales Transformation Function in Python with Error Handling
    :param orders_df: pandas dataframe, extracted sales data
    :param products_df: pandas dataframe, extracted sales data
    :param customers_df: pandas dataframe, extracted sales data
    :return: pandas dataframe, transformed data
    """

    # Merge the orders and products DataFrames
    product_orders_df = pd.merge(orders_df, products_df, on='product_id')

    # Calculate the total price for each order
    product_orders_df['total_price'] = product_orders_df['quantity'] * product_orders_df['price']

    # Merge the resulting DataFrame with the customers DataFrame
    sales_df = pd.merge(product_orders_df, customers_df, on='customer_id')

    return sales_df
