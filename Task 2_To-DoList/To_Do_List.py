
def task():

    tasks = []
    print("----- W  E L C O M E  TO  T O-D O  L I S T -------\n")
    
    total_task = int(input("enter the number of tasks = "))

    for i in range (1,total_task+1):
        task_name = input(f"enter the name of task {i} = ")
        tasks.append(task_name)

    print(f"your tasks are =\n {tasks}\n")


    while True:

        print(f"----- M E N U --------\n")
        print("1.ADD TASK")
        print("2.VIEW ALL TASKS")
        print("3.UPDATE A PARTICULAR TASK")
        print("4.DELETE THE PARTICULAR TASK..")
        print("5.DELETE ALL TASKS")
        print("6.EXITT..")


        select_choice = int(input(f"Enter you choice from menu (1 , 2 , 3 ,4 ,5 ,6) = "))

        if(select_choice ==1):
                add_task = int(input("enter number of tasks you want to add = ")) 

                for i in range (1,add_task+1):
                    new_task = input(f"enter the new task {i} = ")
                    tasks.append(new_task)

                print(f"you have these tasks till now to do =\n {tasks}\n")


        elif select_choice ==2:
             print("...............................................................")
             print(f"Your all tasks are as follow :--\n {tasks}")
             print("...............................................................")

             

        elif select_choice==3:
             print(f"Your all tasks are as follow :--\n {tasks}")
             old_task  = input(f"Which task you want to update = ")
             if old_task in tasks:  
                updated_task = input("Enter the new task to update =  ")
                position = tasks.index(old_task) 
                tasks[position]=updated_task 
                print(".................................................................................")
                print(f"you task {updated_task} has been updated..")
                print(f"This is your updated TO DO list = {tasks}\nAnything else then see the MENU section below")
                print(".................................................................................")


        elif select_choice ==4:
                 print(f"Your all tasks are as follow :--\n {tasks}")
                 old_task = input(f"Which task you want to DELETE = ")
                 if old_task in tasks:  
                      deleted = tasks.remove(old_task) 
                      print("...............................................................")
                      print(f"Your task {old_task} has been deleted.....")
                      print(f"This is your updated TO DO list = {tasks}\nAnything else then see the MENU section below")
                      print("...............................................................")



                      
        elif select_choice==5:
             print(f"ARE YOU SURE YOU WANT TO DELETE/CLEAR ALL TASKS...")
             print(f"1.YES\n2.NO")

             choice = input("Enter yes or no = ")

             if (choice=="yes"):
                  print("deleting all tasks.....")
                  tasks.clear()
                  print("...............................................................")
                  print(f"Your all tasks is deleted..Here is your TO DO list \n{tasks}")

             if choice=="no":
                  print("carefull bext time while deleting....")
                  print("...............................................................")
                  print(f"this is your TO DO list {tasks}")

        elif select_choice==6:
            print("...............................................................")
            print(f"exiting...")
            break

task()