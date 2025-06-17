import matplotlib.pyplot as plt

lst =[1,2,3,4,5,6,7,8]




#Scatter Plot
x1 =[1,2,3,4,5,6,7,8,9]
y1=[12,45,2,78,3,4,77,55,99]

# plt.scatter(x=x1,y=y1,c='r')
# plt.xlabel("X-axis")
# plt.ylabel('Y - axis')
# plt.title("2D Scatter  Diagram")

plt.plot(x1,y1,c='r')
plt.xlabel("X-axis")
plt.ylabel('Y - axis')
plt.title("2D Diagram")

plt.show()
