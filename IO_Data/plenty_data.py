#Exam number: B140990

#an attribute to hold the name of the fucntion
__all__ = ['line_reader']

#a function to open the input file, parse the data, append it to one of two lists and return two variables
def line_reader(file):
    #create two lists to hold x coordinate and y coordinate data from the input file
    data_x = []
    data_y = []

    #open the input file for reading
    with open(file,'r') as inFile:

    #loop over each line in the input file and perform a number of operations
        for line in inFile:
            data = line.strip('\n').split(' ') #strip '\n' from each line and split the line into individual elements using spaces.
            data_x.append(float(data[0])) #convert the first element in the line to a float and append to the list 'data_x'
            data_y.append([float(a) for a in data[1:]]) #use list comprehension to convert the next elements in the line and append to 'data_y'

    #return two variables
    return data_x, data_y