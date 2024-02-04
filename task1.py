def  area_of_country(countryname,countryarea):
     return (countryarea/148940000) * 100

def main () :

     countryname = input("Enter country name:")
     countryarea = float(input("Enter country area:"))
     result=area_of_country(countryname,countryarea)
     print(countryname,"is ",result,"% of total world's landmass ") 
if __name__ == "__main__":
    main()