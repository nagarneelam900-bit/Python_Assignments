import datetime
import pickle
def computeFine(mem_id):
    #print(mem_id)
    fine=[]
    file=open('Member.bin','rb')
    try:
        while True:
           # print("The member id inside while",mem_id)
            data=pickle.load(file)
            #print(data)
            if data==mem_id:
                fine.append(data)
                year =int(input("\t\tEnter Issue year(YYYY):"))
                month=int(input("\t\tEnter Issue month(1-12):"))
                day=int(input("\t\tEnter Issue day(1-31):"))
                Issue_date_obj=datetime.date(year,month,day)
                fine.append(Issue_date_obj)
                year1 =int(input("\t\tEnter Return year(YYYY):"))
                month1=int(input("\t\tEnter Return month(1-12):"))
                day1=int(input("\t\tEnter Return day(1-31):"))
                Return_date_obj=datetime.date(year1,month1,day1)
                fine.append(Return_date_obj)
                year2 =int(input("\t\tEnter Due year(YYYY):"))
                month2=int(input("\t\tEnter Due month(1-12):"))
                day2=int(input("\t\tEnter Due day(1-31):"))
                Due_date_obj=datetime.date(year2,month2,day2)
                fine.append(Due_date_obj)
    except:
        pass
    file.close()
    return fine
