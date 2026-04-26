"""
UTILITIES FOR LIBRARY MANAGEMENT SYSTEM
"""
import pickle
import os
from DateTesting import computeFine
#FUNCTION FOR ADDING A BOOK
def addBooks():
    file=open('Book.bin','ab')
    #AUTHOR_NAME,BOOK_ID,TITLE,PRICE,AVAIL_STATUS
    book_id=int(input("\n\t\t Enter the Book Id:"))
    author_Name=input("\t\tEnter Author_Name of the Book:")
    title=input("\t\tEnter the Title of Book:")
    price=int(input("\t\tEnter the price of book:"))
    avail_status=input("\t\tEnter the available Status for Book:")
    #Adding the data to Book.bin file
    pickle.dump(book_id,file)
    pickle.dump(author_Name,file)
    pickle.dump(title,file)
    pickle.dump(price,file)
    pickle.dump(avail_status,file)
    print("\n\t\tBook Added Successfully")
    file.close()
    input("\t\tPress Enter to Continue:")

#FUNCTION TO VIEW THE DETAILS OF ALL THE BOOKS
def viewAllBooks():
    file=open('Book.bin','rb')
    try:
        while True:
            #pickle.load(file)
            print("\t\tBook_id is:",pickle.load(file))
            print("\t\tAuthor Name of Book is:",pickle.load(file))
            print("\t\tTitle of Book is:",pickle.load(file))
            print("\t\tPrice of Book is:",pickle.load(file))
            print("\t\tAvailable status is:",pickle.load(file))
            print("\t\t*********************************************************")
    except:
        print("\t\tHere is The details of all your Books:")
        print("*****************************************************************")
    
    file.close()
    input("\t\tPress Enter to Continue:")

#FUNCTION TO UPDATE BOOK DETAILS
def updateBook():
    file1=open('Book.bin','rb')
    file2=open('temp.bin','ab')
    Book_id=int(input("\t\tEnter the Book Id to update:"))
    flag=0
    try:
        while True:
            data=pickle.load(file1)
            if data==Book_id:
                pickle.dump(data,file2)
                author_name=pickle.load(file1)
                pickle.dump(author_name,file2)
                title=pickle.load(file1)
                pickle.dump(title,file2)
                print("\t\tOld Price of Book is:",pickle.load(file1))
                price=int(input("\t\tEnter The new Price to update:"))
                pickle.dump(price,file2)
                print("\t\tOld Available Status is:",pickle.load(file1))
                avail_status=input("\t\tEnter the new available status:")
                pickle.dump(avail_status,file2)
                flag=1
            else:
                pickle.dump(data,file2)
    except:
        if flag==1:
            print("\t\tBook Details updated Successfully!")
        else:
            print("\t\tBook Not Found")
    file1.close()
    file2.close()
    os.remove('Book.bin')
    os.rename('temp.bin','Book.bin')
    input("\t\tPress Enter to Continue:")

#FUNCTION TO DELETE BOOK DETAILS
def deleteBook():
    file1=open('Book.bin','rb')
    file2=open('temp.bin','ab')
    book_id=int(input("\t\tEnter the Book Id to be deleted:"))
    flag=0
    try:
        while True:
            data=pickle.load(file1)
            if data==book_id:
                print("\t\tBook Id is:",data)
                print("\t\tAuthor of the Book is:",pickle.load(file1))
                print("\t\ttitle of the book is:",pickle.load(file1))
                print("\t\tPrice of the Book is:",pickle.load(file1))
                print("\t\tStatus of the Book is:",pickle.load(file1))
               # pickle.load(file1)
                flag=1
            else:
                pickle.dump(data,file2)
    except:
        if flag==1:
            print("\n\t\tBook Deleted Successfully!")
        else:
            print("\n\t\tBook Not Found.....")
    file1.close()
    file2.close()
    os.remove('Book.bin')
    os.rename('temp.bin','Book.bin')
    input("\t\tPress Enter to Continue:")

#FUNCTION TO Add A Publisher
#PUBLISHED BY(P_ID,ADDRESS,NAME,BOOK_ID,TITLE)
def addPublisher():
    file=open('publisher.bin','ab')
    p_id=int(input("\t\tEnter The Publisher Id:"))
    book_id=int(input("\t\tEnter The Book Id:"))
    pub_add=input("\t\tEnter The Publisher Address:")
    pub_Name=input("\t\tEnter The Publisher Name:")
    book=getBook(book_id)
    if len(book)!=0:
        print("\t\tBook Id:",book[0])
        print("\t\tBook Title:",book[2])
        pickle.dump(book[0],file)
        pickle.dump(book[2],file)
        pickle.dump(p_id,file)
        pickle.dump(pub_add,file)
        pickle.dump(pub_Name,file)        
        print("\t\tPublisher Added Succefully!!")
        print("***********************************************")
    else:
        print("\t\tBook Not Found")             
    file.close()
    input("\t\tPress Enter to Continue:")
#FUNCTION TO GET BOOK INFORMATION
def getBook(book_id):
    book=[]
    file=open('Book.bin','rb')
    try:
        while True:
            data=pickle.load(file)
            if data==book_id:
                book.append(data)
                book.append(pickle.load(file))
                book.append(pickle.load(file))
                book.append(pickle.load(file))
                book.append(pickle.load(file))
    except:
        pass
    file.close()
    return book

#FUNCTION TO GET MEMBER INFORMATION
def getMember(mem_id):
    member=[]
    file=open('Member.bin','rb')
    try:
        while True:
            data=pickle.load(file)
            if data==mem_id:
                member.append(data)
                member.append(pickle.load(file))
                member.append(pickle.load(file))
                member.append(pickle.load(file))
                member.append(pickle.load(file))
    except:
        pass
    file.close()
    return member

#FUNCTION TO VIEW ALL PUBLISHER
def viewAllPublisher():
    file=open('publisher.bin','rb')
    try:
        while True:
            print("\t\tBook Id:", pickle.load(file))
            print("\t\tBook Title:",pickle.load(file))
            print("\t\tPublisher Id:",pickle.load(file))
            print("\t\tPublisher Address:", pickle.load(file))
            print("\t\tPublisher Name:",pickle.load(file))
            print("---------------------------------------------")
    except:
            print("\t\tHere is the Detail of all The publishers")
    file.close()
    input("\t\tPress Enter to Continue:")

#FUNCTION TO UPDATE PUBLISHER
def updatePublisher():
    file1=open('publisher.bin','rb')
    file2=open('temp.bin','ab')
    book_id=int(input("\t\tEnter The Book_Id for which publisher details need to be updated:"))
    try:
        while True:
            data=pickle.load(file1)
            if data==book_id:
                pickle.dump(data,file2)
                book_name=pickle.load(file1)
                pickle.dump(book_name,file2)
                pub_id=pickle.load(file1)
                pickle.dump(pub_id,file2)
                pub_address=pickle.load(file1)
                print("\t\t Old publisher Address:",pub_address)
                pub_address1=input("\t\tEnter New Publisher Address:")
                pickle.dump(pub_address1,file2)
                pub_name=pickle.load(file1)
                print("\t\t Old Publisher Name:",pub_name)
                pub_name1=input("\t\tEnter The New Name:")
                pickle.dump(pub_name1,file2)
            else:
                pickle.dump(data,file2)
    except:
         print("\t\tPublisher Details Updated Successfully!!")
    file1.close()
    file2.close()
    os.remove('publisher.bin')
    os.rename('temp.bin','publisher.bin')
    input("\t\tPress Enter to Continue:")

#FUNCTION TO DELETE PUBLISHER
def deletePublisher():
    file1=open('publisher.bin','rb')
    file2=open('temp.bin','ab')
    book_id=int(input("\t\tEnter The Book Id for which Publisher Needs to be deleted:"))
    flag=0
    try:
        while True:
            data=pickle.load(file1)
            if data==book_id:
                print("\t\tBook_Id:",data)
                print("\t\tBook Title:",pickle.load(file1))
                print("\t\tPublisher Id:",pickle.load(file1))
                print("\t\tPublisher Address:",pickle.load(file1))
                print("\t\tPublisher Name:",pickle.load(file1))
                flag=1
            else:
                pickle.dump(data,file2)
    except:
        if flag==1:
            print("\t\tPublisher Deleted Successfully!!")
        else:
            print("\t\tBook Not Found")
    file1.close()
    file2.close()
    os.remove('publisher.bin')
    os.rename('temp.bin','publisher.bin')
    input("\t\tPress Enter to Continue:")
    

#FUNCTION TO ADD MEMBER
def addMember():
    file=open('Member.bin','ab')
    mem_id=int(input("\n\t\tEnter Member Id:"))
    mem_name=input("\t\tEnter Member Name:")
    mem_Add=input("\t\tEnter Member Address:")
    mem_date=input("\t\tEnter Member Date:")
    memid_expirydate=input("\t\tEnter Member Id Expiry Date:")
    pickle.dump(mem_id,file)
    pickle.dump(mem_name,file)
    pickle.dump(mem_Add,file)
    pickle.dump(mem_date,file)
    pickle.dump(memid_expirydate,file)
    print("\t\tMember Added Successfully!!")

    file.close()
    input("\t\tPress Enter to Continue:")

#FUNCTION TO VIEW ALL MEMBERS
def viewAllMembers():
    file=open('Member.bin','rb')
    try:
        while True:    
            print("\n\t\tMember Id is:",pickle.load(file))
            print("\t\tMember Name is:",pickle.load(file))
            print("\t\tMember Address is:",pickle.load(file))
            print("\t\tMember Date of Joining is:",pickle.load(file))
            print("\t\tMember Id Expiration Date is:",pickle.load(file))
    except:
        print("\t\tHere is the List of All Members")
        print("-----------------------------------------------")
    file.close()
    input("\t\tPress Enter to Continue:")

#FUNCTION TO UPDATE MEMBERS DETAILS
def updateMemberDetails():
    file1=open('Member.bin','rb')
    file2=open('temp.bin','ab')
    mem_id=int(input("\t\tEnter The Member Id to update Details:"))
    try:
        while True:
            data=pickle.load(file1)
            if data==mem_id:
                print("\n\t\t Member Id is:",data)
                pickle.dump(data,file2)
                name=pickle.load(file1)
                print("\t\tMember Name is:",name)
                pickle.dump(name,file2)
                address=pickle.load(file1)
                print("\t\tOld Address of Member is:",address)
                address1=input("\t\tEnter New Address:")
                pickle.dump(address1,file2)
                mem_date=pickle.load(file1)
                print("\t\tMember Date of Joining is:",mem_date)
                pickle.dump(mem_date,file2)
                memid_expirydate=pickle.load(file1)
                print("\t\tOld Member Id Expiration Date is:",memid_expirydate)
                memid_new_expirydate=input("\t\tEnter The new MemberId Expiration Date:")
                pickle.dump(memid_new_expirydate,file2)
            else:
                pickle.dump(data,file2)
    except:
        print("\t\tDetails Updated Successfully....!!")
        print("-----------------------------------------------------------")
    file1.close()
    file2.close()
    os.remove('Member.bin')
    os.rename('temp.bin','Member.bin')
    input("\t\tPress Enter to Continue:")
    
#FUNCTION TO DELETE LIBRARY MEMBER DETAILS
def deleteMember():
    file1=open('Member.bin','rb')
    file2=open('temp.bin','ab')
    mem_id=int(input("\t\tEnter The Member Id to be deleted:"))
    flag=0
    try:
        while True:
            data=pickle.load(file1)
            if data==mem_id:
                print("\t\tMember Id is:",data)
                print("\t\tMember Name is:",pickle.load(file1))
                print("\t\tMember Address is:",pickle.load(file1))
                print("\t\tMember Date of Joining is:",pickle.load(file1))
                print("\t\tMember Id Expiration Date is:",pickle.load(file1))
                flag=1
            else:
                pickle.dump(data,file2)
    except:
        if flag==1:
            print("\t\tLibrary Member Deleted SuccessFully....!")
            print("\t\t--------------------------------------------------")
        else:
            print("\t\tMember Id Not Found.....!!!")
    file1.close()
    file2.close()
    os.remove('Member.bin')
    os.rename('temp.bin','Member.bin')
    input("\t\tPress Enter to Continue:")
#FUNCTION TO ADD BORROWER DETAILS
#ADD BORROWER DETAILS(DUE_DATE,Return_date,Issue ye user se enter karaya and MemId,MemName Member
#se get kiya and BookId,Title Books se get kiya)
# Abhi isme Book Ka count fetch krna bacha hai

def addBorrower():
    file=open('Borrower.bin','ab')
    mem_id=int(input("\t\tEnter the Member Id to whom book needs to be assign:"))
    member=getMember(mem_id)
    if len(member)!=0:
        pickle.dump(member[0],file)
        pickle.dump(member[1],file)
        book_id=int(input("\t\tEnter The Book Id to issue:"))
        book=getBook(book_id)
        if len(book)!=0:
            pickle.dump(book[0],file)
            pickle.dump(book[1],file)
            pickle.dump(book[2],file)
            Issue_status=input("\t\tEnter The Issue Status:")
            pickle.dump(Issue_status,file)
            #Fine=computeFine(mem_id)
            Fine=computeFine(mem_id)
            #print("The Fine list is:",Fine)
            if len(Fine)!=0:
                pickle.dump(Fine[1],file)
                #print(Fine[1])
                pickle.dump(Fine[2],file)
               # print(Fine[2])
                pickle.dump(Fine[3],file)

            print("\t\tBorrower Details Added Successfully....")
            print("\t\t---------------------------------------------------")
        else:
            print("\t\tBook Not Found...!!")
    else:
        print("\t\tMember Not Found....!!")        
    file.close()
    input("\t\tPress Enter to Continue:")

#FUNCTION TO VIEW BORROWER DETAILS
def viewBorrowerDetails():
    file=open('Borrower.bin','rb')
    try:
        while True:
            data=pickle.load(file)
            #print(data)
            print("\n\t\tBorrower Id:",data)
            print("\t\tBorrower Name:", pickle.load(file))
            print("\t\t Book Id:",pickle.load(file))
            print("\t\t Book Author Name:",pickle.load(file))
            print("\t\t Book Title:",pickle.load(file))
            print("\t\t Issue Status:",pickle.load(file))
            print("\t\t Issue Date:",pickle.load(file))
            print("\t\t Return Date:",pickle.load(file))
            print("\t\t Due Date:",pickle.load(file))
            print("\t\t**********************************************************")
    except:
        print("\t\t Here is the details of all The borrowers.!!")
    file.close()
    input("\t\tPress Enter to Continue:")

#FUNCTION TO DELETE BORROWER DETAILS
def deleteBorrower():
    file1=open('Borrower.bin','rb')
    file2=open('temp.bin','ab')
    mem_id=int(input("\t\tEnter The Borrower Id to be Deleted:"))
    try:
        while True:
            data=pickle.load(file1)
            if data==mem_id:
                print("\t\tBorrower Id is:",data)
                print("\t\tBorrower Name is:",pickle.load(file1))
                print("\t\tBook Id is:",pickle.load(file1))
                print("\t\tBook Author Name is:",pickle.load(file1))
                print("\t\tBook Title is:",pickle.load(file1))
                print("\t\tBook Assigned Status:",pickle.load(file1))
                print("\t\tBook Issued Date:",pickle.load(file1))
                print("\t\tBook Returned Date:",pickle.load(file1))
                print("\t\tBook Due Date:",pickle.load(file1))
                print("\t\t************************************")
            else:
               pickle.dump(data,file2)
    except:
        print("\t\tBorrower Deleted Successfully:")
        print("\t\t*****************************************")
    file1.close()
    file2.close()
    os.remove('Borrower.bin')
    os.rename('temp.bin','Borrower.bin')
    input("\t\tPress Enter to Continue:")

#FUNCTION TO BORROW BOOK
def borrowBook():
    count=0
    Mem_id=int(input("\t\tEnter Member Id:"))
    member=getMember(Mem_id)
    if Mem_id==member[0]:
        count=count+1
        if len(member)!=0:
            print("\t\tMember Name:",member[1])
            print("\t\tMember Address:",member[2])
            book_id=int(input("\t\tEnter The book Id:"))
            book=getBook(book_id)
            if len(book)!=0:
                print("\t\t Book Author Name:",book[1])
                print("\t\t Book Title:",book[2])
           # print("\t\tThe number of books Assigned:",count)
                file=open('BorrowBook.bin','ab')
                pickle.dump(Mem_id,file)
                pickle.dump(book_id,file)
                pickle.dump(count,file)
                
            #pickle.dump(count,file)
                print("\t\t Book Borrowed Successfully!!")
                print("\t\t*****************************************")
                file.close()
        else:
            print("\t\tBook Id not Found")
    else:
            print("\t\tMember Id not Found")
    input("\t\tPress Enter to Continue:")


#FUNCTION TO VIEW BOOK STATUS BY ID
def viewBookStatusById():
    file=open('Borrower.bin','rb')
    n=1001
    count=0
    mem_id=int(input("\t\tEnter Borrower Id to view book Assigned"))
    member=getMember(mem_id)
    print("\t\tMember Name:",member[1])
    print("\t\tMember Address:",member[2])
    try:
        while True:
            data=pickle.load(file)
            if data==mem_id:
                count=count+1
                pickle.load(file)
                book=getBook(pickle.load(file))
                print("\t\tBook No:",n)
                print("\t\tBook Name:",book[1])
                print("\t\tNo. Of Books:",count)
                print("\t\t*****************************")
                n=n+1
    except:
        print("\t\tHere is your Order for the Customer")
                
            
    file.close()
    input("\t\tPress Enter to Continue...")
'''
#FUNCTION FOR PASSWORD AND AUTHENTICATION
def authentication():
    userName=input("\t\tEnter The User Name:")
    user='admin'
    password=input("\t\tEnter The password:")
    password1='admin1234'
    if(userName==user and password==password1):
        print("\t\tAdmin Logged In...")
        input("\tPress Enter to Continue...")
    else:
        print("\t\tIncorrect UserName and Password")
        input("\tPress Enter to Continue...")
'''        
#FUNCTION TO UPDATE FINE AND REFUND DETAILS
def updateFineAndRefundDetails():
    file1=open('Borrower.bin','rb')
    file2=open('temp.bin','ab')
    mem_id=int(input("\t\tEnter The Borrower Id to be updated:"))
    fine=0
    try:
        while True:
            data=pickle.load(file1) 
            if data==mem_id:
                print("\t\tBorrower Id:",data)
                pickle.dump(data,file2)
                name= pickle.load(file1)
                pickle.dump(name,file2)
                book_id=pickle.load(file1)
                pickle.dump(book_id,file2)
                book_author_name=pickle.load(file1)
                pickle.dump(book_author_name,file2)
                book_title=pickle.load(file1)
                pickle.dump(book_title,file2)
                book_Issued_Status=pickle.load(file1)
                pickle.dump(book_Issued_Status,file2)
                Issue_Date=pickle.load(file1)
                pickle.dump(Issue_Date,file2)
                return_date=pickle.load(file1)
                #print(return_date)
                pickle.dump(return_date,file2)
                due_date=pickle.load(file1)
                #print(due_date)
                pickle.dump(due_date,file2)
                if return_date>due_date:
                    file3=open('BorrowBook.bin','rb')
                    pickle.load(file3)
                    pickle.load(file3)
                    num=pickle.load(file3)
                    fine=num*10+fine
                    print("\t\tTotal Fine is:",fine)
                    print("\t\tFine Status:Please Submit Fine.")
                elif return_date==due_date:
                    print("\t\tBooks submitted on time.No Fine")
                else:
                    print("\t\tBooks Submitted on time.No Fine")
                    file3.close()
            else:
                pickle.dump(data,file2)
    except:
        print("\t\tRefund and Fine Status updated Successfully...!!")
    file1.close()
    file2.close()
    os.remove('Borrower.bin')
    os.rename('temp.bin','Borrower.bin')
    

    
    
    
    
            
            
            
