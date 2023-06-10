import os
import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="mukil",
    database='performancedata'
)

mycursor = mydb.cursor()

# Execute the SQL query
sql_query = "SELECT * FROM productivity"
mycursor.execute(sql_query)

# Fetch all rows from the result set
result = mycursor.fetchall()

# Get the column names
columns = [desc[0] for desc in mycursor.description]

# Create a pandas DataFrame from the result data and column names
df = pd.DataFrame(result, columns=columns)

# Get the path to the Downloads folder
downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")

# Specify the desired output file name
output_filename = "output.xlsx"

# Create the full path to the output file
output_file = os.path.join(downloads_folder, output_filename)

# Save the DataFrame to an Excel file
df.to_excel(output_file, index=False)

print(f"Result grid saved to {output_file}")