from collections import deque
# Create an empty queue
call_queue = deque()

# Add a call to the queue
def addCall(customerID, callTime):
 	call = (customerID, callTime)
    	call_queue.append(call)
    	print("Call added successfully.")

# Answer the first call
def answerCall():
 if call_queue:
        		call = call_queue.popleft()
        		print("Answering call:")
        		print("Customer ID:", call[0])
        		print("Call Time:", call[1], "minutes")
 else:
       		 print("Queue is empty. No call to answer.")

# Display all calls
def viewQueue():
 	if call_queue:
        		print("\nCalls currently in queue:")
 for call in call_queue:
           			 print("Customer ID:", call[0],
                 		 "| Call Time:", call[1], "minutes")
else:
       		 print("Queue is empty.")


# Check whether queue is empty
def isQueueEmpty():
 if not call_queue:
        		print("Queue is empty.")
 	else:
        		print("Queue is not empty.")

# Main program
while True:
print("\n----- CALL CENTER QUEUE -----")
    	print("1. Add Call")
   	 print("2. Answer Call")
    	print("3. View Queue")
    	print("4. Check if Queue is Empty")
   	 print("5. Exit")

choice = input("Enter your choice: ")

 if choice == "1":
 customerID = input("Enter Customer ID: ")
        		callTime = int(input("Enter Call Time (minutes): "))
 addCall(customerID, callTime)

elif choice == "2":
        		answerCall()

elif choice == "3":
        		viewQueue()

elif choice == "4":
        		isQueueEmpty()

 elif choice == "5":
        		print("Program ended.")
       		 break

    	else:
       		 print("Invalid choice.")
