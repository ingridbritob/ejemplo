import numpy as np
import math
import matplotlib.pyplot as plt

Fc=300
t=np.arange(0,0.1,10**(-5.7))
x=np.sin(40*np.pi*t)
w=np.sin(2*Fc*np.pi*t)
p=w*x
y=(t,p)

plt.subplot(311)
plt.plot(t,x,linewidth=0.4,color='darkblue')
plt.title('Señal del mensaje - Onda moduladora',fontsize=12)

plt.subplot(312)
plt.plot(t,w,linewidth=0.4,color='gold')
plt.title('Funcion - Onda portadora',fontsize=12)

plt.subplot(313)
plt.xlabel('Indice de Tiempo')
plt.ylabel('Amplitud')
plt.plot(t,p,linewidth=0.4,color='g')
plt.title('Modulacion AM',fontsize=12)

plt.show()
