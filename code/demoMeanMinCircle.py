from matplotlib import pyplot as plt
import numpy as np
import minmaxradiuscircle
import functions

# This demo presents the minimum radius enclosing ball of 100% data, its center and the average point as a new point is added by the user.
# Input: The x and y coordinates of the starting point.
# Output: Minimum radius enclosing ball that includes all data, its center, and the average point of user clicked data points.

def onclick(event):
    print(event.xdata, event.ydata)

class MinradCirclebuilder:
    def __init__(self, point):
        self.point = point
        self.xs = list(point.get_xdata())
        self.ys = list(point.get_ydata())
        self.cid = point.figure.canvas.mpl_connect('button_press_event', self)
        #print(self.xs)


    def __call__(self, event):
        #print('click', event)
        if event.inaxes!=self.point.axes: return
        self.xs.append(event.xdata)
        self.ys.append(event.ydata)
        self.point.set_data(self.xs, self.ys)

        xCoord = np.asarray(self.xs)
        yCoord = np.asarray(self.ys)

        prevXcoord = xCoord[0: len(xCoord) - 1]
        prevYcoord = yCoord[0: len(yCoord) - 1]

        #Find the average points
        #xMean = np.mean(presentPts[:, 0])
        #yMean = np.mean(presentPts[:, 1])
        xMean = np.mean(xCoord)
        yMean = np.mean(yCoord)



        #print(event.xdata)
        #print(event.ydata)
        #print(type(self.xs))
        #print(self.xs, self.ys)
        #print(self.xs)
        #print(firstPts)

        prevCircle = minmaxradiuscircle.make_circle(prevXcoord, prevYcoord, len(prevXcoord))


        presentCircle = minmaxradiuscircle.make_circle(xCoord, yCoord, len(xCoord))



        circle1 = plt.Circle((presentCircle[0], presentCircle[1]), presentCircle[2], color='r', fill=False)
        #percentCircle1 = plt.Circle((percentPresentCircle[0], percentPresentCircle[1]), percentPresentCircle[2], color='b', fill=False)

        centerOfCircle = plt.Circle((presentCircle[0], presentCircle[1]), 1.2, color='r', fill=True)
        avgPoint = plt.Circle((xMean, yMean), 1.2, color='k', fill=True)

        #rad = np.minimum(prevCircle[2], presentCircle[2])

        distPointToCen = functions.distCordwise(event.xdata, event.ydata, presentCircle[0], presentCircle[1])

        #print(prevCircle[2])
        #print(presentCircle[2])
        #print(maxRad)
        #print(distPointToCen)

        if distPointToCen <= prevCircle[2]:
            print("New point ({}, {}) entered, keep minimum radius disk and only update the average point.".format(round(event.xdata,4),round(event.ydata,4)))
        else:
            print("New point ({}, {}) entered, update minimum radius disk and the average point.".format(round(event.xdata,4),round(event.ydata,4)))

        #print(percent)
        #circle2 = plt.plot([actual[0]], [actual[1]], marker='o', markersize=3, color="red")
        ax.add_artist(circle1)
        ax.add_artist(centerOfCircle)
        #ax.add_artist(percentCircle1)
        ax.add_artist(avgPoint)
        self.point.figure.canvas.draw()
        circle1.remove()
        centerOfCircle.remove()
        #percentCircle1.remove()
        avgPoint.remove()

        #canvas.update()


fig = plt.figure(figsize=(7,8))
ax = fig.add_subplot(111)
ax.set_xlim([-100, 100])
ax.set_ylim([-100, 100])
ax.set_title('Click a point to build an Minimum radius enclosing circles')

xflag = 1
yflag = 1

while xflag == 1:
    try:
        xTemp = float(input("Enter x coordinate of the first point between -50 and 50, x: "))
        xflag = 0
    except ValueError:
        print("Please enter a float number.")

while yflag == 1:
    try:
        yTemp = float(input("Enter y coordinate of the first point between -50 and 50, y: "))
        yflag = 0
    except ValueError:
        print("Please enter a float number.")

x = float(xTemp)
y = float(yTemp)

point, = ax.plot([x], [y], marker="o", linestyle="")  #first point
minradcirclebuilder = MinradCirclebuilder(point)

plt.show()