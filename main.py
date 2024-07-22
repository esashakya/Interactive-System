# import all the functions from different file
from operation import *
from write import *
from operation import *
#calling the function
welcome_message()
#to store the return datas
information = read_text_file()
dictionary = organize()

iterate = True
while iterate == True:
    select_option()
    user_input_value=choosing_option()
    if user_input_value == 1 or user_input_value == 2 or user_input_value == 3:
        #customer choses option no. 1 
        if user_input_value == 1:
            purchase_laptop=[]
            continue_=True #for looping if customer wants to keep buying
            while continue_==True:
                title()
                organize_file()
                customer_chosen_laptop_id= chosen_laptop_id(dictionary)#send the parameters through function
                quantity_selected=dictionary[customer_chosen_laptop_id][3]
                customer_chosen_laptop_quantity=chosen_laptop_quantity(quantity_selected)

                updated(dictionary,customer_chosen_laptop_id,customer_chosen_laptop_quantity)
                purchase_laptop=new_values(dictionary,customer_chosen_laptop_id,customer_chosen_laptop_quantity,purchase_laptop)
                #continue looping if customer chooses any other option than y or n
                loop=True
                while loop==True:
                    permission=shopping_permission()
                    if permission=="y":
                        purchase = True
                        loop=False
                    elif permission=="n":
                        entire_price,delivery_charge=no_condition(purchase_laptop)
                        cost_and_change(entire_price)
                        present_time=time()
                        updated_date=updated_time(present_time)
                        customer_full_name,customer_phone_number=info_for_bill()
                        bill_heading()
                        cutomer_info(customer_full_name,customer_phone_number,present_time)
                        title_for_bill()
                        chosen_products(purchase_laptop)
                        total_amt(delivery_charge,entire_price)
                        new_write_text_file(customer_full_name,customer_phone_number,present_time,delivery_charge,entire_price,purchase_laptop,updated_date)
                        continue_ = False
                        loop=False
                    else:
                        print("Please try again")
                        loop=True
            iterate=False
        elif user_input_value == 2:
            purchase_laptop=[]
            continue_=True #for looping if customer wants to keep buying
            while continue_==True:
                title()
                organize_file()
                customer_chosen_laptop_id= chosen_laptop_id(dictionary)#send the parameters through function
                quantity_selected=dictionary[customer_chosen_laptop_id][3]
                customer_chosen_laptop_quantity=chosen_laptop_quantity(quantity_selected)
                updated2(dictionary,customer_chosen_laptop_id,customer_chosen_laptop_quantity)
                purchase_laptop=new_values2(dictionary,customer_chosen_laptop_id,customer_chosen_laptop_quantity,purchase_laptop)
                #continue looping if customer chooses any other option than y or n
                loop=True
                while loop==True:
                    permission=shopping_permission()
                    if permission=="y":
                        purchase = True
                        loop=False
                    elif permission=="n":
                        vat_amount,gross_amount=calculation(purchase_laptop)
                        present_time=time()
                        updated_date=updated_time(present_time)
                        Company_name,Company_phone_number=company_info()
                        bill_heading()
                        print_company_info(Company_name,Company_phone_number,present_time)
                        title_for_bill()
                        chosen_products(purchase_laptop)
                        vat_and_grossamt(vat_amount,gross_amount)
                        new_write_text_file2(Company_name,Company_phone_number,present_time,vat_amount,gross_amount,purchase_laptop,updated_date)
                        continue_ = False
                        loop=False
                    else:
                        print("Please try again")
                        loop=True
            
            iterate=False
        elif user_input_value==3:
           thank_you_display()
           iterate=False
        else:
            invalid_display()
            iterate = True
    else:
        print("Please choose one of the above option")
        print ("\n")
       
                    
                    
                    
                
            
            
        
        
                    
            
    
    
        
    
    
    
    
    
