#Exam number: B140990

#import the IO_Data module
import IO_Data

#an attribute to hold a list of names of fucntions to import as part of the module
if __name__=='__main__':
    #assign the input filename to the variable 'file' which will be handed to the first function
    file = 'plenty.data'

    #call the function 'line_reader' that will read the data and append to two lists.  
    #the function returns two lists, x and y, which will be used to plot 
    x,y = IO_Data.line_reader(file)

    #call the function 'plotter' to plot the lists x and y
    IO_Data.plotter(x,y)
