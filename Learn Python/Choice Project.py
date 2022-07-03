while True:
    print()
    print("----------------")
    print("1. Temperature |")
    print("2. Speed       |")
    print("3. Length      |")
    print("4. Exit        |")
    print("----------------")
    choice_main = input("Enter Your Choice : ")
    if choice_main == '1': 
        print()
        print("         Temperature         ")
        print("-----------------------------")
        print("1. Fahrenheit -> Celsius    |")
        print("2. Fahrenheit -> Kelvin     |")
        print("3. Celsius    -> Fahrenheit |")
        print("4. Celsius    -> Kelvin     |")
        print("5. Kelvin     -> Fahrenheit |")
        print("6. Kelvin     -> Kelvin     |")
        print("7. Exit                     |")
        print("-----------------------------")
        while True:
            print()
            temp = input("Enter Your Choice : ")
            if temp == '1':
                foc = float(input("Enter Faherenheit Value : "))
                logic_foc = ((foc-32)*(5/9))
                print("Fahrenheit -> Celsius : ", round(logic_foc,2), "C")
            elif temp == '2':
                fok = float(input("Enter Faherenheit Value : "))
                logic_cof = ((fok-32)*(5/9) + 273.15)
                print("Fahrenheit -> Kelvin : ", round(logic_cof,2) , "K")
            elif temp == '3':
                cof = float(input("Enter Celsius Value : "))
                logic_cof = ((cof)*(9/5)) + 32
                print("Celsius -> Fahrenheit : ", round(logic_cof,2), "F")
            elif temp == '4':
                cok = float(input("Enter Celsius Value : "))
                logic_cof = ((cok) + 273.15)
                print("Celsius -> Kelvin : ", round(logic_cof,2), "K")
            elif temp == '5':
                kof = float(input("Enter Kelvin Value : "))
                logic_kof = ((kof-273.15)*(9/5) + 32)
                print("Kelvin -> Fahrenheit : ", round(logic_kof,2), "F")
            elif temp == '6':
                koc = float(input("Enter Kelvin Value : "))
                logic_koc = (koc-273.15)
                print("Kelvin -> Fahrenheit : ", round(logic_koc,2), "C")
            elif temp == '7':
                break;
            else:
                print("Please Select Valid Choice")
    elif choice_main == '2':
        print()
        print("                       Speed                      ")
        print("--------------------------------------------------")
        print("1.  Miles Per Hour     -> Foot Per Second        |")
        print("2.  Miles Per Hour     -> Meter Per Second       |")
        print("3.  Miles Per Hour     -> Kilometer Per Hour     |")
        print("4.  Miles Per Hour     -> knot                   |")
        print("5.  Foot Per Second    -> Miles Per Hour         |")
        print("6.  Foot Per Second    -> Meter Per Second       |")
        print("7.  Foot Per Second    -> Kilometer Per Hour     |")
        print("8.  Foot Per Second    -> knot                   |")
        print("9.  Kilometer Per Hour -> Foot Per Second        |")
        print("10. Kilometer Per Hour -> Meter Per Second       |")
        print("11. Kilometer Per Hour -> Miles Per Hour         |")
        print("12. Kilometer Per Hour -> knot                   |")
        print("13. Exit                                         |")
        print("--------------------------------------------------")
        while True:
            print()
            speed = input("Enter Your Choice : ")
            if speed == '1':
                mof = float(input("Enter Miles Per Hour : "))
                logic_mof = mof * 1.467
                print("Miles Per Hour -> Foot Per Second :" , round(logic_mof, 2))
            elif speed == '2':
                mom = float(input("Enter Miles Per Hour : "))
                logic_mom = (mom/2.237)
                print("Miles Per Hour -> Meter Per Second :" , round(logic_mom, 2))
            elif speed == '3':
                moki = float(input("Enter Miles Per Hour : "))
                logic_moki = (moki*1.609)
                print("Miles Per Hour -> Kilometer Per Hour :" , round(logic_moki, 2))
            elif speed == '4':
                mok = float(input("Enter Miles Per Hour : "))
                logic_mok = (mok/1.151)
                print("Miles Per Hour -> Knot :" , round(logic_mok, 2))
            elif speed == '5':
                fomi = float(input("Enter Foot Per Second : "))
                logic_fomi = (fomi/1.467)
                print("Foot Per Second -> Miles Per Hour : ", round(logic_fomi,2))
            elif speed == '6':
                fom = float(input("Enter Foot Per Second : "))
                logic_fom = (fom/3.281)
                print("Foot Per Second -> Meter Per Second : ", round(logic_fom,2))
            elif speed == '7':
                moki = float(input("Enter Foot Per Second : "))
                logic_moki = (moki/1.097)
                print("Foot Per Second -> Kilometer Per Hour : ", round(logic_moki,2))
            elif speed == '8':
                mok = float(input("Enter Foot Per Second : "))
                logic_mok = (mok/1.688)
                print("Foot Per Second -> knot : ", round(logic_mok,2))
            elif speed == '9':
                kof = float(input("Enter Kilometer Per Hour : "))
                logic_kof = (kof/1.097)
                print("Kilometer Per Hour -> Foot Per Second : ", round(logic_kof,2))
            elif speed == '10':
                kom = float(input("Enter Kilometer Per Hour : "))
                logic_kom = (kom/3.6)
                print("Kilometer Per Hour -> Meter Per Second : ", round(logic_kom,2))
            elif speed == '11':
                komi = float(input("Enter Kilometer Per Hour : "))
                logic_komi = (komi/1.609)
                print("Kilometer Per Hour -> Miles Per Hour : ", round(logic_komi,2))
            elif speed == '12':
                kok = float(input("Enter Kilometer Per Hour : "))
                logic_kok = (kok/1.852)
                print("Kilometer Per Hour -> Knot : ", round(logic_kok,2))
            elif speed == '13':
                break;
            else:
                print("Please Select Valid Choice")
    elif choice_main == '3':
        print()
        print("           Length             ")
        print("------------------------------")
        print("1. Kilometer  -> Meter       |")
        print("2. Kilometer  -> Centimeter  |")
        print("3. Meter      -> Kilometer   |")
        print("4. Centimeter -> Kilometer   |")
        print("5. Meter      -> Foot        |")
        print("6. Meter      -> Yard        |")
        print("7. Meter      -> Inch        |")
        print("8. Foot       -> Meter       |")
        print("9. Yard       -> Meter       |")
        print("10. Inch      -> Meter       |")
        print("11. Exit                     |")
        print("------------------------------")
        while True:
            print()
            length = input("Enter Your Choice : ")
            if length == '1':
                kom = float(input("Enter Kilometer : "))
                logic_kom = (kom*1000)
                print("Kilometer -> Meter : ", round(logic_kom,2))
            elif length == '2':
                koc = float(input("Enter Kilometer : "))
                logic_koc = (koc*100000)
                print("Kilometer -> CentiMeter : ", round(logic_koc,2))
            elif length == '3':
                kom = float(input("Enter Meter : "))
                logic_kom = (kom/1000)
                print("Meter -> Kilometer : ", round(logic_kom,2))
            elif length == '4':
                cok = float(input("Enter Centimeter : "))
                logic_cok = (cok/10000)
                print("Centimeter -> Kilometer : ", round(logic_cok,2))
            elif length == '5':
                mof = float(input("Enter Meter : "))
                logic_mof = (mof*3.281)
                print("Meter -> Foot : ", round(logic_mof,2))
            elif length == '6':
                moy = float(input("Enter Meter : "))
                logic_moy = (moy*1.094)
                print("Meter -> Yard : ", round(logic_moy,2))
            elif length == '7':
                moi = float(input("Enter Meter : "))
                logic_moi = (moi*39.37)
                print("Meter -> Inch : ", round(logic_moi,2))
            elif length == '8':
                fom = float(input("Enter Foot : "))
                logic_fom = (fom/3.281)
                print("Foot -> Meter : ", round(logic_fom,2))
            elif length == '9':
                yom = float(input("Enter Yard : "))
                logic_yom = (yom/1.094)
                print("Yard -> Meter : ", round(logic_yom,2))
            elif length == '10':
                iom = float(input("Enter Inch : "))
                logic_iom = (iom/39.37)
                print("Inch -> Meter : ", round(logic_iom,2))
            elif length == '11':
                break;
            else:
                print("Please Select Valid Choice")
    elif choice_main == '4':
        break;
    else:
        print("Please Select Valid Choice")
