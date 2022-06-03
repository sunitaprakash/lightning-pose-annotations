import matplotlib.pyplot as plt

#img1
im = plt.imread('img1.png')
implot = plt.imshow(im)

# put a blue dot at (10, 20)
x = [53.44, 394.90, 202.49]
y = [330.78, 19.30, 299.76]
# put a red dot, size 40, at 2 locations:
plt.scatter(x=x, y=y, c='r', s=40)
plt.show()

#img2
im = plt.imread('img2.png')
implot = plt.imshow(im)
# put a blue dot at (10, 20)
x = [29.05, 255.61, 393.38]
y = [312.49, 289.80, 22.34]
# put a red dot, size 40, at 2 locations:
plt.scatter(x=x, y=y, c='r', s=40)
plt.show()

#img3
im = plt.imread('img3.png')
implot = plt.imshow(im)
# put a red dot at key points
x = [275.53,393.89,28.04]
y = [291.70,20.82,114.32]
# put a red dot, size 40, at 2 locations:
plt.scatter(x=x, y=y, c='r', s=40)
plt.show()

#img4
im = plt.imread('img4.png')
implot = plt.imshow(im)
# put a blue dot at (10, 20)
x = [35.66,308.25,392.88]
y = [7.61,294.55,20.82]
# put a red dot, size 40, at 2 locations:
plt.scatter(x=x, y=y, c='r', s=40)
plt.show()

#img5
im = plt.imread('img5.png')
implot = plt.imshow(im)
# put a blue dot at (10, 20)
x = [36.17,294.03,393.89]
y = [7.10,317.79,22.34]
# put a red dot, size 40, at 2 locations:
plt.scatter(x=x, y=y, c='r', s=40)
plt.show()

#img3
im = plt.imread('img6.png')
implot = plt.imshow(im)
# put a red dot at key points
x = [321.74,45.82,392.88]
y = [307.92,41.15,21.33]
# put a red dot, size 40, at 2 locations:
plt.scatter(x=x, y=y, c='r', s=40)
plt.show()
