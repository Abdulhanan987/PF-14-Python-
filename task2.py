def length(number):
         count =0
         while number!=0: 
            
            number = number//10 
            count = count + 1
            return count 

def main():
   a = int(input("Enter the number:"))
   b=length(a)       
   print(b) 
if __name__ == "__main__":
    main()