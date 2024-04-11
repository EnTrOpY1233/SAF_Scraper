import openai,json

key=open("chatgptAPI.txt","r").read()

class ChatApp:
    def __init__(self):
        # Setting the API key to use the OpenAI API
        openai.api_key = key
        self.default2 ={"role": "system", "content": "Read the article and find the SAF company(string), annoucement_date, year_entry_of_service(int, when the facility can start to product SAF), country(string), city(string), projected_capacity (must converted all units to million liter per year), producing_now or not (bool). Put all information in Json format. If some information is not found or unsure, set it to null. "}

    def chat(self, text):
        input={"role": "user", "content": text}
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            response_format={ "type": "json_object" },
            messages=[self.default2,input]
        )
        return response.choices[0].message.content


if __name__=='__main__':
    bot=ChatApp()


    with open("ProductionCapacity/Info.json",'r') as file:
       datas=json.load(file)
       file.close()

    for data in datas:
        text=data["Text body"]
        response=json.loads(bot.chat(text))
        
        data["country"]=response["country"]
        data["city"]=response["city"]
        data["year_entry_of_service"]=response["year_entry_of_service"]
        data["projected_capacity"]=response["projected_capacity"]
        data["producing_now"]=response["producing_now"]
        print(response)

    with open("ProductionCapacity/Info.json",'w') as file:
       json.dump(datas,file,indent=4)
       print('Information is updated')
       file.close()

     



