import requests
import pandas as pd

border = "=" * 40
# step 1 : firstly we will extract the data from the API
url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)

# step 2 : check the response status code
if response.status_code == 200:
    data = response.json()
    print("Data extracted successfully from the API")
else:
    print("error response code:", response.status_code)


# step 3 : transform the data into a pandas dataframe
df = pd.json_normalize(data)
print(df.head())

# step 4 : load the data into a CSV file
df.to_csv("users_data.csv", index=False)
print("CSV file saved in data folder successfully")
