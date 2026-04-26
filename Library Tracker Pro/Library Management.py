"""
LIBRARY MANAGEMENT SYSTEM
"""

'''
BOOKS(AUTHOR_NAME,BOOK_ID,TITLE,PRICE,AVAIL_STATUS)
PUBLISHED BY(P_ID,ADDRESS,NAME,BOOK_ID,TITLE)
MEMBER(EXPIRY_DATE,NAME,ADDRESS,MEM_ID,MEM_DATE,MEM_NAME)
BORROWED BY(DUE_DATE,RETURN_DATE,ISSUE,MEM_ID,MEM_NAME,BOOK_ID,TITLE)


1. ADD A BOOK
2. VIEW ALL BOOKS
3. UPDATE BOOK
4. DELETE BOOK
5. ADD A PUBLISHER
6. VIEW ALL PUBLISHER
7. UPDATE PUBLISHER DETAILS #A book can have multiple publishers(Update publisher details for a book)
8. DELETE A PUBLISHER #Delete Publisher Id and associated details - Book_id,Title,Address,Name
9. ADD A MEMBER
10.VIEW ALL MEMBERS
11. UPDATE MEMBER DETAILS
12. DELETE MEMBER
13. ADD BORROWER DETAILS(DUE_DATE,Return_date,Issue ye user se enter karaya and MemId,MemName Member se get kiya and BookId,Title Books se get kiya)
14. VIEW BORROWER DETAILS
15. UPDATE FINE/REFUND DETAILS(In Borrower Table due date ,status and return date will be changed
16. DELETE BORROWER DETAILS(Status Returned and No Fine delete MemId and associated details)
17. BORROW A BOOK(Member will borrow book= MemId,MemName, BookId,P_id,BooktITLE)
18. VIEW ALL BOOKS STATUS BY MEMBER_ID
19. VIEW AND UPDATE FINE AND REFUND STATUS
20. PASSWORD AND AUTHENTICATION

'''
from utils import addBooks,viewAllBooks,updateBook,deleteBook,addPublisher,viewAllPublisher,updatePublisher,deletePublisher,addMember,viewAllMembers,updateMemberDetails,deleteMember,addBorrower,viewBorrowerDetails,borrowBook,viewBookStatusById,deleteBorrower,updateFineAndRefundDetails
#DASHBOARD
input("\t\tPress Enter to Continue...")
#authentication()

while True:
    userName=input("\t\tEnter The User Name:")
    user='admin'
    password=input("\t\tEnter The password:")
    password1='admin1234'
    if(userName==user and password==password1):
        print("\t\t**************************************")
        print("\t\tAdmin Logged In...")
        print("\t\t**************************************")
        input("\t\tPress Enter to Continue...")
        
        print("\n\t\t************LIBRARY MANAGEMENT SYSTEM**************")
        print('''\t\t\t1.  ADD A BOOK
            \t\t2.  VIEW ALL BOOKS
            \t\t3.  UPDATE BOOK
            \t\t4.  DELETE BOOK
            \t\t5.  ADD A PUBLISHER
            \t\t6.  VIEW ALL PUBLISHER
            \t\t7.  UPDATE PUBLISHER DETAILS
            \t\t8.  DELETE A PUBLISHER
            \t\t9.  ADD A MEMBER
            \t\t10. VIEW ALL MEMBERS
            \t\t11. UPDATE MEMBER DETAILS
            \t\t12. DELETE MEMBER
            \t\t13. ADD BORROWER DETAILS
            \t\t14. VIEW BORROWER DETAILS
            \t\t15. UPDATE FINE/REFUND DETAILS
            \t\t16. DELETE BORROWER DETAILS
            \t\t17. BORROW A BOOK
            \t\t18. VIEW ALL BOOKS STATUS BY MEMBER_ID
            \t\t19. EXIT''')
        ch=int(input("\n\t\tEnter your choice:"))
        if ch==19:
            print("\n\t\t BYE-BYE ADMIN!")
            break
        elif ch==1:
            addBooks()
        elif ch==2:
            viewAllBooks()
        elif ch==3:
            updateBook()
        elif ch==4:
            deleteBook()
        elif ch==5:
            addPublisher()
        elif ch==6:
            viewAllPublisher()
        elif ch==7:
            updatePublisher()
        elif ch==8:
            deletePublisher()
        elif ch==9:
            addMember()
        elif ch==10:
            viewAllMembers()
        elif ch==11:
            updateMemberDetails()
        elif ch==12:
            deleteMember()
        elif ch==13:
            addBorrower()   
        elif ch==14:
            viewBorrowerDetails()
        elif ch==15:
            updateFineAndRefundDetails()
        elif ch==16:
            deleteBorrower()
        elif ch==17:
            borrowBook()
        elif ch==18:
            viewBookStatusById()
                        
                        
        print("\t\t*************************************************************")
                
    else:
        print("\t\tIncorrect UserName and Password")
        break
        

