from operation import *
def write_text_file():
        information = open("gadget.txt","w") #write in the text file
        return information
def new_write_text_file(customer_full_name,customer_phone_number,present_time,delivery_charge,entire_price,purchase_laptop,updated_date):
        information = open(str(customer_full_name) + str(updated_date)+".txt","w")#open a new text file which name is user name and the time during the transaction
        information.write("\n")
        information.write("\t\t\t\t\t INVOICE ")
        information.write("\n")
        information.write("\t\t\t----------- Kamalpokhari , Kathmandu------------")
        information.write("\n")
        information.write("\t\t\t\t\t\t ---------Phone Number:9999999900--------")
        information.write("\n")
        information.write("Your name: " + str(customer_full_name))
        information.write("\n")
        information.write("Your phone number: "+str(customer_phone_number))
        information.write("\n")
        information.write("Transaction date: "+ str(present_time))
        information.write("\n")
        information.write("\n")
        information.write("-----------------------------------------------------------------------------------------------------------------------------")
        information.write("\n")
        information.write("Product Name \t\t\t Quantity \t\t Rate \t\t\t Amount")
        information.write("\n")
        information.write("-----------------------------------------------------------------------------------------------------------------------------")
        information.write("\n")
        for num in purchase_laptop:
                information.write(str(num[0])+ "\t\t\t"+str(num[1])+"\t\t\t"+str(num[2])+"\t\t\t"+str(num[3]))
                information.write("\n")
        information.write("-----------------------------------------------------------------------------------------------------------------------------")
        information.write("\n")
        information.write("\t\t\t\t\t\t\t\t Delivery charge: "+ str(delivery_charge))
        information.write("\n")
        information.write("\t\t\t\t\t\t\t\t Net Amount: "+str(entire_price))
        information.write("\n")
        information.close()
def new_write_text_file2(Company_name,Company_phone_number,present_time,vat_amount,gross_amount,purchase_laptop,updated_date):
        information = open (str(Company_name) + str(updated_date)+".txt","w")#open a new text file which name is user name and the time during the transaction
        information.write("\n")
        information.write("\t\t\t\t\t INVOICE ")
        information.write("\n")
        information.write("\t\t\t----------- Laptop Manufacturers, Kathmandu------------")
        information.write("\n")
        information.write("\t\t\t\t\t\t ---------Phone Number:9999999900--------")
        information.write("\n")
        information.write("Company's name: Laptop Manufacturers")
        information.write("\n")
        information.write("Company's phone number:9999999900" )
        information.write("\n")
        information.write("Transaction date: "+ str(present_time))
        information.write("\n")
        information.write("\n")
        information.write("-----------------------------------------------------------------------------------------------------------------------------")
        information.write("\n")
        information.write("Product Name \t\t\t Company's Name \t\t Quantity \t\t Rate \t\t\t Amount")
        information.write("\n")
        information.write("-----------------------------------------------------------------------------------------------------------------------------")
        information.write("\n")
        for num in purchase_laptop:
                information.write(str(num[0]) + "\t\t\t"+str(num[4])+"\t\t\t"+str(num[1])+"\t\t\t"+str(num[2])+"\t\t\t"+str(num[3]))
                information.write("\n")
        information.write("-----------------------------------------------------------------------------------------------------------------------------")
        information.write("\n")           
        information.write("\t\t\t\t\t\t\t\t VAT amount: "+ str(vat_amount))
        information.write("\n")
        information.write("\t\t\t\t\t\t\t\t Gross Amount: "+ str(gross_amount))
        information.close()
        
def select_option():
        print ("Press 1 to sell laptops/computers")
        print ("Press 2 to buy laptops/computers from manufactures")
        print ("Press 3 to exit")
        print ("----------------------------------------------------------------------------------------------------------------------")
        print ("\n")
        
def title():
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")
    print("s/n\t\tLaptop Name\t\tCompany Name\t\tPrice\t\tQuantity\tProcessor Details\t\tGraphics")
    print("\n")
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
def title_for_bill():
        print("-----------------------------------------------------------------------------------------------------------------------------")
        print("\n")
        print("Product Name \t\t\t Quantity \t\t Rate \t\t\t Amount")
        print("\n")
        print("-----------------------------------------------------------------------------------------------------------------------------")
                    
def vat_and_grossamt(vat_amount,gross_amount):
         print("\t\t\t\t\t\t\t\t VAT amount: "+ str(vat_amount))
         print("\t\t\t\t\t\t\t\t Gross Amount: "+ str(gross_amount))
         
        
    

def updated(dictionary,customer_chosen_laptop_id,customer_chosen_laptop_quantity):
        dictionary[customer_chosen_laptop_id][3]=int(dictionary[customer_chosen_laptop_id][3])-int(customer_chosen_laptop_quantity)#reduce the quantity
        information=write_text_file()
        for value in dictionary.values():
                information.write(str(value[0])+"," + str(value[1])+"," +str(value[2])+"," +str(value[3])+","+str(value[4])+","+str(value[5]))
                information.write("\n")
        information.close()


def bill_heading():
        print("\n")
        print("\t\t\t\t\t INVOICE ")
        print("\n")
        print("\t\t\t----------- Kamalpokhari , Kathmandu------------")
        print("\t\t\t\t\t\t ---------Phone Number:9999999900--------")
        print("\n")
def cutomer_info(customer_full_name,customer_phone_number,present_time):
        print("Your name: " + str(customer_full_name))
        print("Your phone number: "+str(customer_phone_number))
        print("Transaction date: "+ str(present_time))
        print("\n")
        
        
def chosen_products(purchase_laptop):
        for num in purchase_laptop:
                print(num[0] , "\t\t\t",num[1],"\t\t\t",num[2],"\t\t\t",num[3])
                    
        
def total_amt(delivery_charge,entire_price):
        print("-----------------------------------------------------------------------------------------------------------------------------")
        print("\t\t\t\t\t\t\t\t Delivery charge: "+ str(delivery_charge))
        print("\t\t\t\t\t\t\t\t Net Amount: "+ str(entire_price))

def updated2(dictionary,customer_chosen_laptop_id,customer_chosen_laptop_quantity):
        dictionary[customer_chosen_laptop_id][3]=int(dictionary[customer_chosen_laptop_id][3])+int(customer_chosen_laptop_quantity)#increase the quantity
        information=write_text_file()
        for value in dictionary.values():
                information.write(str(value[0])+"," + str(value[1])+"," +str(value[2])+"," +str(value[3])+","+str(value[4])+","+str(value[5]))
                information.write("\n")
        information.close()        
def print_company_info(Company_name,Company_phone_number,present_time):
    print("\n")
    print("Company's name: "+Company_name)
    print("Company's phone number: "+Company_phone_number)
    print("Transaction date: "+ str(present_time))
    print("\n")
    print("\n")

def thank_you_display():
        print("Thank you for visting!!We hope you visit us soon")
def invalid_display():
        print("Invalid input")

def welcome_message():
        print("----------------------------------------------------------WELCOME TO THE SHOP-----------------------------------------")
        print("\n")
        print ("\t\t\t\t\tI hope you like the experience of shopping with us")
        print("----------------------------------------------------------------------------------------------------------------------")
        print("\n")
    
        
