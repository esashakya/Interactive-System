from datetime import datetime
from read import read_text_file
from write import *

def organize():
    information = read_text_file() #read the text file
    dictionary = {}
    id_ = 1
    for each in information:
        each = each.replace("\n","") #replace enter with spaces
        dictionary.update({id_:each.split(",")})
        id_+=1
    information.close()
    return dictionary
def choosing_option():
    #asking the user for the number of option
        value_entry_success=False
        while value_entry_success==False:#loop till it provides suitable answer
            try:
                user_input_value =int(input("Enter the number of option: "))
                value_entry_success=True
                
            except:
                print("\n")
                print("Please try again!! As you have entered inaccurate option")
        return user_input_value
def info_for_bill():
    print("In order to create the bill, you need to fill the following questions !!")
    print("----------------------------------------------------------------------------------------------------------------------")
    customer_full_name=input("Enter your full name ")
    print("----------------------------------------------------------------------------------------------------------------------")
    customer_phone_number=input("Enter your phone number ")
    print("----------------------------------------------------------------------------------------------------------------------")
    print("\n")
    return customer_full_name,customer_phone_number
def chosen_laptop_id(dictionary):
    #ask the user laptop id
    value_entry_success=False
    while value_entry_success==False:
            try:
                customer_chosen_laptop_id = int(input("Enter the id of the laptop that you have selected to buy:  "))
                while customer_chosen_laptop_id <= 0 or customer_chosen_laptop_id > len(dictionary):
                    print("Error!! Please try again")
                    customer_chosen_laptop_id = int(input("Enter the id of the laptop that you have selected to buy:  "))
                    print("\n")
                value_entry_success=True
            except:
                print("Please try again!! As you have entered inaccurate id number")
    return customer_chosen_laptop_id
def chosen_laptop_quantity(quantity_selected):
    #ask the user laptop quantity
    value_entry_success=False
    while value_entry_success==False:
        try:
            customer_chosen_laptop_quantity =int(input("Enter the quantity of the laptop that you have selected to buy:  "))
            while customer_chosen_laptop_quantity <=0 or customer_chosen_laptop_quantity>int(quantity_selected):
                print("Error!! Please try again")
                customer_chosen_laptop_quantity =int(input("Enter the quantity of the laptop that you have selected to buy:  "))
                print("\n")
            value_entry_success=True
        except:
            print("Please try again!! As you have entered inaccurate quantity number or we don't have the number")
            print("of quantity you are looking for")
    return customer_chosen_laptop_quantity


def organize_file():
    information = read_text_file()
    count = 1
    for each in information:
        print( count,"\t\t"+each.replace(",","\t\t"))#replace comma with tab
        count += 1
        print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
    information.close()
    
def new_values(dictionary,customer_chosen_laptop_id,customer_chosen_laptop_quantity,purchase_laptop):
    selected_product_name=dictionary[customer_chosen_laptop_id][0]
    selected_quantity = customer_chosen_laptop_quantity
    selected_product_price = dictionary[customer_chosen_laptop_id][2]
    price = dictionary[customer_chosen_laptop_id][2].replace("$","")
    selected_total_price=int(price)*int(selected_quantity)
    purchase_laptop.append([selected_product_name,selected_quantity,price,selected_total_price])
    return purchase_laptop
def shopping_permission():
        permission=input("Are you sure you want to keep shopping?(y/n)").lower()
        return permission
def time():
    present_time = datetime.now()#provides current time
    return present_time
def no_condition(purchase_laptop):
    entire_price=0
    delivery_charge = 250
    sum_=0
    for num in purchase_laptop:
        sum_ = sum_ +int(num[3])
    entire_price = sum_ + delivery_charge
    return entire_price,delivery_charge
def cost_and_change(entire_price):
        print ("Your entire cost is: "+str(entire_price))
def company_info():
    Company_name= input("Enter the company's name")
    Company_phone_number=input("Enter the company's phone number")
    return Company_name,Company_phone_number
def calculation(purchase_laptop):
    vat = 13/100
    sum_=0
                    
    for num in purchase_laptop:
        sum_ = sum_ +int(num[3])
    vat_amount = vat * sum_
    gross_amount = sum_ + vat_amount
    return vat_amount,gross_amount
def new_values2(dictionary,customer_chosen_laptop_id,customer_chosen_laptop_quantity,purchase_laptop):
    selected_product_name=dictionary[customer_chosen_laptop_id][0]
    selected_quantity = customer_chosen_laptop_quantity
    selected_product_price = dictionary[customer_chosen_laptop_id][2]
    price = dictionary[customer_chosen_laptop_id][2].replace("$","")
    selected_total_price=int(price)*int(selected_quantity)
    selected_company_name=dictionary[customer_chosen_laptop_id][1]
    purchase_laptop.append([selected_product_name,selected_quantity,price,selected_total_price,selected_company_name])
    return purchase_laptop
def updated_time(present_time):
    present_time=str(present_time)
    updated_date = present_time.replace(":","")
    
    return  updated_date      
    
    



