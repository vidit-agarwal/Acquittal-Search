from selenium import webdriver
import time
import  csv

csvfile = open("IndiaNGOList-part2.csv" , "a")
writer = csv.writer(csvfile)

#writer.writerow(("Name" , "Unique Id" , "cheif functionary" , "chairman" , "secretary" , "treasurer" , "Parent Organisation" , "registered with :" , "Type of Ngo" , "Reg No" ,"City of Reg" , "State of Reg" , "Date of Reg" , "frca" , "city_contact" , "state_contact" , "country_contact" , "telephone" , "telephone2"   , "mobile number" , "address", "email" , "website" , "fax"  ))

driver = webdriver.PhantomJS(executable_path=r"/home/vidit/Desktop/phantomjs-2.1.1-linux-x86_64/bin/phantomjs")

def scrape_function (url) :
    driver.get(url)

    print(url)
    try :

        global NGO_name
        if driver.find_element_by_xpath(".//*[@class='ngo_div1']/div[1]/div[1]").text == "NGO Name" :
            NGO_name= driver.find_element_by_xpath(".//*[@class='ngo_div1']/div[1]/div[2]").text
            print("NGO NAME " + NGO_name)
        else :
            NGO_name= "-"
            print("ngo name :"+ NGO_name)

        global Unique_Id
        if driver.find_element_by_xpath(".//*[@class='ngo_div1']/div[1]/div[1]").text == "Unique Id of VO/NGO" :
                Unique_Id= driver.find_element_by_xpath(".//*[@class='ngo_div1']/div[1]/div[2]").text
                print("Id " + Unique_Id)

        elif driver.find_element_by_xpath(".//*[@class='ngo_div1']/div[2]/div[1]").text == "Unique Id of VO/NGO" :
            Unique_Id= driver.find_element_by_xpath(".//*[@class='ngo_div1']/div[2]/div[2]").text
            print("Id " + Unique_Id)
        else :
            Unique_Id ='-'
            print(Unique_Id)


        global cheif_funct

        if  driver.find_element_by_xpath(".//*[@class='ngo_div1']/div[2]/div[1]").text == "Chief Functionary":
                cheif_funct= driver.find_element_by_xpath(".//*[@class='ngo_div1']/div[2]/div[2]").text
                print("cheif funct : "+cheif_funct)
        elif driver.find_element_by_xpath(".//*[@class='ngo_div1']/div[3]/div[1]").text == "Chief Functionary" :
            cheif_funct= driver.find_element_by_xpath(".//*[@class='ngo_div1']/div[3]/div[2]").text
            print("Cheif Funct " + cheif_funct)
        else :
            cheif_funct='-'
            print("cheif funct"+ cheif_funct)

        global chairman

        if driver.find_element_by_xpath(".//*[@class='ngo_div1']/div[3]/div[1]").text =="Chairman" :
                chairman = driver.find_element_by_xpath(".//*[@class='ngo_div1']/div[3]/div[2]").text
                print("chairman: "+chairman)
        elif  driver.find_element_by_xpath(".//*[@class='ngo_div1']/div[4]/div[1]").text == "Chairman" :
            chairman= driver.find_element_by_xpath(".//*[@class='ngo_div1']/div[4]/div[2]").text
            print("chairman : " +chairman)

        else :
            chairman ='-'
            print("chairman"+chairman)


        global secret
        if driver.find_element_by_xpath(".//*[@class='ngo_div1']/div[4]/div[1]").text == "Secretary" :
                secret = driver.find_element_by_xpath(".//*[@class='ngo_div1']/div[4]/div[2]").text
                print("secretary:" + secret)
        elif driver.find_element_by_xpath(".//*[@class='ngo_div1']/div[5]/div[1]").text == "Secretary" :
            secret = driver.find_element_by_xpath(".//*[@class='ngo_div1']/div[5]/div[2]").text
            print("Secretary: "+secret)
        else :
            secret='-'
            print("secretary"+secret)



        global treasure

        if driver.find_element_by_xpath(".//*[@class='ngo_div1']/div[5]/div[1]").text == "Treasurer" :
                treasure = driver.find_element_by_xpath(".//*[@class='ngo_div1']/div[5]/div[2]").text
                print("Treasure :"+ treasure)
        elif driver.find_element_by_xpath(".//*[@class='ngo_div1']/div[6]/div[1]").text == "Treasurer" :
            treasure = driver.find_element_by_xpath(".//*[@class='ngo_div1']/div[6]/div[2]").text
            print("treasurer " + treasure)
        else:
            treasure='-'
            print("Treasurer"+ treasure)

        global parent_org

        if driver.find_element_by_xpath(".//*[@class='ngo_div1']/div[6]/div[1]").text == "Umbrella/Parent Organization" :
                parent_org = driver.find_element_by_xpath(".//*[@class='ngo_div1']/div[6]/div[2]").text
                print("Parent Org:"+ parent_org)
        elif driver.find_element_by_xpath(".//*[@class='ngo_div1']/div[7]/div[1]").text== "Umbrella/Parent Organization" :
            parent_org = driver.find_element_by_xpath(".//*[@class='ngo_div1']/div[7]/div[2]").text
            print("Parent Org:"+ parent_org)
        else :
            parent_org='-'
            print("Parent Org : "+ parent_org)



        #part 2
        global registered_with


        registered_with= driver.find_element_by_xpath(".//*[@class='ngo_info']/div[4]/div[1]/div[2]").text
        print("Registered with : " + registered_with)

        global type
        type= driver.find_element_by_xpath(".//*[@class='ngo_info']/div[4]/div[2]/div[2]").text
        print("Type  :" + type)

        global reg_no
        reg_no= driver.find_element_by_xpath(".//*[@class='ngo_info']/div[4]/div[3]/div[2]").text
        print("Reg No  :" + reg_no)

        global city_reg
        city_reg= driver.find_element_by_xpath(".//*[@class='ngo_info']/div[4]/div[4]/div[2]").text
        print("City Reg  :" + city_reg)

        global state_reg
        state_reg= driver.find_element_by_xpath(".//*[@class='ngo_info']/div[4]/div[5]/div[2]").text
        print("State reg : "+state_reg)

        global date
        date= driver.find_element_by_xpath(".//*[@class='ngo_info']/div[4]/div[6]/div[2]").text
        print("DATE reg : "+date)

        global frca


        if driver.find_element_by_xpath(".//*[@class='ngo_info']/div[4]/div[7]/div[1]").text ==" frca  ":
            frca= driver.find_element_by_xpath(".//*[@class='ngo_info']/div[4]/div[7]/div[2]").text
            print("FRCA : "+frca)
        else :
            frca ='-'
            print("frca:"+frca)

        #part 3

        global city_contact
        city_contact= driver.find_element_by_xpath(".//*[@id='contact details']/div[1]/div[2]/a/span").text
        print("CITY CONTACT " + city_contact)

        global state_contact

        state_contact= driver.find_element_by_xpath(".//*[@id='contact details']/div[2]/div[2]/a/span").text
        print("STATE CONTACT "+ state_contact)

        global country
        country= driver.find_element_by_xpath(".//*[@id='contact details']/div[3]/div[2]/span/span").text
        print("COUNTRY"+country)

        global telephone
        telephone= driver.find_element_by_xpath(".//*[@id='contact details']/div[4]/div[2]/span").text
        print("TELEPHONE"+telephone)

        global telephone2

        if driver.find_element_by_xpath(".//*[@id='contact details']/div[5]/div[1]").text == "Telephone 2" :
            telephone2= driver.find_element_by_xpath(".//*[@id='contact details']/div[5]/div[2]/span").text
            print("telephone2"+telephone2)
        else :
            telephone2 = "-"
            print("telephone2 :"+ telephone2)


        global mobile

        if driver.find_element_by_xpath(".//*[@id='contact details']/div[5]/div[1]").text ==  "Mobile Number" :
            mobile= driver.find_element_by_xpath(".//*[@id='contact details']/div[5]/div[2]").text
            print("mobile"+mobile)
        elif driver.find_element_by_xpath(".//*[@id='contact details']/div[6]/div[1]").text =="Mobile Number":
            mobile= driver.find_element_by_xpath(".//*[@id='contact details']/div[6]/div[2]").text
            print("mobile"+mobile)
        else :
            mobile="-"
            print("mobile :"+mobile)

        global address

        if driver.find_element_by_xpath(".//*[@id='contact details']/div[6]/div[1]").text ==  "Address" :
            address= driver.find_element_by_xpath(".//*[@id='contact details']/div[6]/div[2]/span").text
            print("address : "+address)
        elif driver.find_element_by_xpath(".//*[@id='contact details']/div[7]/div[1]").text =="Address":
            address= driver.find_element_by_xpath(".//*[@id='contact details']div[7]/div[2]/span").text
            print("address: "+address)
        else :
            address ="-"
            print("address : "+ address)



        global email

        if driver.find_element_by_xpath(".//*[@id='contact details']/div[7]/div[1]").text ==  "Email" :
            email= driver.find_element_by_xpath(".//*[@id='contact details']/div[7]/div[2]/span").text
            print("email : "+ email)
        elif driver.find_element_by_xpath(".//*[@id='contact details']/div[8]/div[1]").text =="Email":
            email= driver.find_element_by_xpath(".//*[@id='contact details']div[8]/div[2]/span").text
            print("email: "+ email)
        else :
            email ="-"
            print("email :"+ email)


        global website

        if driver.find_element_by_xpath(".//*[@id='contact details']/div[8]/div[1]").text ==  "Website" :
            website= driver.find_element_by_xpath(".//*[@id='contact details']/div[8]/div[2]").text
            print("website : "+website)
        elif driver.find_element_by_xpath(".//*[@id='contact details']/div[9]/div[1]").text =="Website":
            website= driver.find_element_by_xpath(".//*[@id='contact details']div[9]/div[2]").text
            print("website: "+website)
        else :
            website ="-"
            print("website :"+website)

        global fax
        try :
            if driver.find_element_by_xpath(".//*[@id='contact details']/div[9]/div[1]").text ==  "Fax" :
                fax= driver.find_element_by_xpath(".//*[@id='contact details']/div[9]/div[2]").text
                print("fax : "+fax)
            elif driver.find_element_by_xpath(".//*[@id='contact details']/div[10]/div[1]").text =="Fax":
                fax= driver.find_element_by_xpath(".//*[@id='contact details']div[10]/div[2]").text
                print("fax: "+fax)
            else :
                fax ="-"
                print("fax :"+ fax)
        except Exception as e :
            fax = "-"


        writer.writerow((NGO_name , Unique_Id , cheif_funct , chairman , secret , treasure , parent_org , registered_with , type , reg_no ,city_reg , state_reg , date , frca , city_contact , state_contact , country , telephone , telephone2 , mobile , address, email , website , fax  ))

    except Exception as e:
        print(e)
        writer.writerow((NGO_name , Unique_Id , cheif_funct , chairman , secret , treasure , parent_org , registered_with , type , reg_no ,city_reg , state_reg , date , frca , city_contact , state_contact , country , telephone , telephone2 , mobile , address, email , website , fax ))







with open(r"/home/vidit/Documents/ngoslegalindia.csv") as f_obj:
     reader = csv.DictReader(f_obj, delimiter=',')
     for line in reader:
         if len(line) !=0 :

             scrape_function(line["url"])


