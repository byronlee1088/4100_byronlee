import numpy as np
import matplotlib.pyplot as plt
ax=plt.subplots()

plt.title("Deltoid Curve")
th=np.linspace(0,2*np.pi);
x=2*np.cos(th)+np.cos(2*th);
y=2*np.sin(th)-np.sin(2*th);
plt.plot(x,y);
plt.show();

plt.title("Galilean Spiral")
th=np.linspace(0,10*np.pi,200);
r=th*th;
x=r*np.cos(th);
y=r*np.sin(th);
plt.plot(x,y);
plt.show();

plt.title("Fey's Function")
th = np.radians(np.linspace(0,4320,2000))
r = np.exp(np.cos(th)) - (2*np.cos(4*th)) + (np.sin(th/12)**5)
x = r*np.cos(th)
y = r*np.sin(th)
plt.plot(x,y)
plt.show()
