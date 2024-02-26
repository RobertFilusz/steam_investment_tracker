import requests
import json
import pandas as pd

def get_price_overview(item_name):
    url = f"https://steamcommunity.com/market/priceoverview/?country=PL&currency=1&appid=730&market_hash_name={item_name}"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return {"error": f"Error for {item_name}: {response.status_code}"}

    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed for {item_name}: {e}"}


def main():
    try:
        # Try to read existing data from the Excel file
        data_frame = pd.read_excel("item_prices.xlsx")
    except FileNotFoundError:
        # If the file doesn't exist, create an empty DataFrame
        data_frame = pd.DataFrame(columns=["Item Name", "Price"])

    while True:
        market_hash_name_input = input("Enter item name (or type 'done' to exit): ")
        if len(market_hash_name_input) < 1:
            print("Try Again")
            continue
        elif market_hash_name_input.lower() == "done":
            break

        result = get_price_overview(market_hash_name_input)

        if "error" in result:
            print(result["error"])
        else:
            item_name = market_hash_name_input
            price = result.get(
                "lowest_price", "N/A"
            )  # Assuming 'lowest_price' is the key in the result JSON
            print(f"Price overview for {item_name}: {price}")
            print("-" * 40)

            # Check if the item already exists in the DataFrame
            existing_index = data_frame[data_frame["Item Name"] == item_name].index

            if not existing_index.empty:
                # Update the price if the item already exists
                data_frame.loc[existing_index, "Price"] = price
            else:
                # Append the data if the item doesn't exist
                new_data = pd.DataFrame({"Item Name": [item_name], "Price": [price]})
                data_frame = pd.concat([data_frame, new_data], ignore_index=True)

    # Save the updated DataFrame to the Excel file
    data_frame.to_excel("item_prices.xlsx", index=False)
    print("Data saved to 'item_prices.xlsx'.")


if __name__ == "__main__":
    main()
