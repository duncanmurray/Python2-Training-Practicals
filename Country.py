class Country:

    index = {'name':0,'population':1,'capital':2,'citypop':3,'continent':4,
             'ind_date':5,'currency':6,'religion':7,'language':8}
    
    # Insert your code here
    # 1a) Implement a constructor    
    # Initialize the object 
    def __init__(self, line):
        # Split the input on ',' and place it into the 'self' __attr
        self.__attr = line.split(',')
        #print self.index    
            
    # 1b) Implement a printit method
    # Define the printit function which takes the 'self' object        
    def printit(self):
        # print the atribute of 'self' with the key 'name' from the dictionary 'index'
        print self.__attr[Country.index['name']]
        
    # 1c) Overloaded stringification
    # Define the function to to output a string
    def __str__(self):
        # return back a atribute of 'self' with the key 'name' from the dictionary 'index'
        return self.__attr[Country.index['name']]
        
    # Getter methods
    # 1d) Implement a getter method for country name
        
    # 1e) Overloaded + and -
    
        
    # If time allows:
    # 1f)  Overloaded == (for index search)
   

