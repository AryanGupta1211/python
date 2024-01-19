month = "April"

match(month):
    case "January":
        print("Winter")
    case "February":
        print("Winter")
    case "March":
        print("Summer")
    case "April":
        print("Summer")
    case "May":
        print("Summer")
    case "June":
        print("Summer")
    case "July":
        print("Rainy")
    case "August":
        print("Rainy")
    case "September":
        print("Rainy")
    case "October":
        print("Rainy")
    case "November":
        print("Winter")
    case "December":
        print("Winter")
    case _:
        print("Invalid Season")