#Exam number: B140990

#an attribute to hold the names of the fucntion
__all__ = ['plotter']

#import matplotlib for plotting
from matplotlib import pyplot as plt

#a function to plot data handed to the function as variables data_x and data_y
def plotter(data_x, data_y):
    #plot the data stored in 'data_x' and 'data_y' using a 10x6 grid 
    plt.figure(figsize=(10,6))
    plt.plot(data_x, data_y)

    #format the plot to make it more readable
    plt.ylabel('Y Values')
    plt.xlabel('X Values')
    plt.title('A Plot of Xs and Ys')
    plt.grid(color = 'gray')

    #show the plot
    plt.show()
