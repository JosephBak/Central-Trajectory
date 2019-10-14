import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import functions

# Input: The number of time steps, x-perturbation constant, y-perturbation constant, and
#           the percent of data points that user wants to include.
# Output: 3D graphs of original trajectory (black), minimum radius circle trajectory (blue),
#           subset minimum radius circle trajectory (green), and average trajectory (red) using 100 generated trajectories.


Axes3D = Axes3D  # pycharm auto import


plt.ion()

# set up a figure twice as wide as it is tall
fig = plt.figure(figsize=plt.figaspect(0.5))


ax = fig.add_subplot(1, 2, 1, projection='3d')



plt.show()

show()


flag = True
endFlag = 1
while True:

    #yOrnFlag = 1
    tFlag = 1
    sxFlag = 1
    syFlag = 1
    percFlag = 1

    if endFlag != 1:
        #print(endFlag)
        yOrn = input("Do you want to compute more graphs (Enter y/n) ?")
        if yOrn == 'n':
            flag = False

    if (flag == False): break

    while tFlag == 1:
        try:
            n = int(input("Enter the number of time steps between 1 and 500: "))
            tFlag = 0
        except ValueError:
            print("Please enter an integer number.")

    while sxFlag == 1:
        try:
            sx = float(input("Enter the x-perturbation (standard deviation of normal random variable) between 0 and 10: "))
            sxFlag = 0
        except ValueError:
            print("Please enter a float number.")

    while syFlag == 1:
        try:
            sy = float(input("Enter the y-perturbation (standard deviation of normal random variable) between 0 and 10: "))
            syFlag = 0
        except ValueError:
            print("Please enter a float number.")

    while percFlag == 1:
        try:
            percent = float(input("Enter the percentage of data you want to include between 0 and 100: "))
            percFlag = 0
        except ValueError:
            print("Please enter a float number.")

    endFlag = endFlag +1




    tData = np.linspace(0, 1000, n)
    xTraj, yTraj = functions.generate_one_traj(n, 0, 0.1, 0, 30, 0, 1.5, 0, 5)
    xData, yData, tData = functions.multiple_traj(100, xTraj, yTraj, sx, sy)
    xMinmaxTraj, yMinmaxTraj = functions.minmax_Traj(xData, yData)
    xAverTraj, yAverTraj = functions.average_traj(xData, yData)
    xPercMinmaxTraj, yPercMinmaxTraj, validNumData = functions.percent_minmax_Traj(xData, yData, percent)

    ax.clear()

    #ax.plot(x, f(x, sx=float(sx)))
    ax.plot_surface(tData,xTraj, yTraj, linestyle='--', marker='o', color = 'k')


plt.show()