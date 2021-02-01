import urllib.request
import time

DataURL='https://raw.githubusercontent.com/robertoioi/trainer-telegram/main/training_schedule.csv'
        
while True:
    # Download data
    def get_data():
        while True:
            response=urllib.request.urlopen(DataURL)
            data=response.read().decode("utf-8")
            return data
            time.sleep(1)

    # Turn raw data into series
    rows=get_data().split("\n")
    days=rows[0].split(";")[0:7]
    while True:
        time.sleep(2)
        # Create weeks dataset
        list_weeks=[]
        for n in range(1,len(rows)-1):
                weeks=rows[n].split(";")[0]
                list_weeks.append(weeks)

        # Create activities dataset
        list_activities=[]
        for n in range(1,len(rows)):
            activity=rows[n].split(";")[1:8]
            list_activities.append(activity)
        #print(list_activities)

        # Assign activity to day of week
        tmp_list=[]
        master_list=[]
        for wk in range(len(list_weeks)-1):
            for dd in range(len(days)):
                tmp_list=[]
                #current_day=str(("(",list_weeks[wk],")",days[dd],": ",list_activities[wk][dd]))
                tmp_list.append(list_weeks[wk])
                tmp_list.append(days[dd])
                tmp_list.append(list_activities[wk][dd])
                master_list.append(tmp_list)
                #master_list.append(tmp_list[wk])
        break
        

    import telepot

    def on_chat_message(msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        if content_type == 'text':
            for n in range(len(master_list)-1):
                today_activity=master_list[n][0]+" - "+master_list[n][1]+"\n"+master_list[n][2]
                bot.sendMessage(chat_id, today_activity)
                time.sleep(5)

    TOKEN="INSERT YOUR TOKEN"

    bot = telepot.Bot(TOKEN)
    def start_bot():
        bot.message_loop(on_chat_message)

        print ('Listening ...')


        while 1:
            time.sleep(10)

    start_bot()
    time.sleep(1)
