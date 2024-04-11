import mysql.connector
import json
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="saf"
)

mycursor = mydb.cursor()

with open ('ProductionCapacity/Info.json','r') as file:
    datas=json.load(file)
    for index,data in enumerate(datas):
        sql = "UPDATE production_capacity SET company=%s, announcement_date=%s, entry_in_service=%s, country=%s, city=%s, producing_now=%s, project_capacity=%s WHERE id=%s"
        values = (
            data["Company"],
            data["Annoucement Date"],
            data["year_entry_of_service"],
            data["country"],
            data["city"],
            data["producing_now"],
            data["projected_capacity"],
            index + 1
        )
        mycursor.execute(sql, values)
        mydb.commit()
        print(mycursor.rowcount, "record(s) affected")
        file.close()

mycursor.execute("SELECT * FROM production_capacity") 
  
# fetch all the matching rows  
result = mycursor.fetchall() 

# loop through the rows 
for row in result: 
    print(row) 
    print("\n") 
