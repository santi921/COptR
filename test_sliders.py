import numpy as np
import matplotlib.pyplot as plt

from matplotlib.widgets import Slider, Button, RadioButtons
from Diag_trans import trans

#there lines create the defaults of the plots
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.25)
#start points
EJ0 = 20
EC0 = 0.25

t=np.arange(-10,10,1)

circuit_test=trans(20,EC0,EJ0)

E0,E1,E2=circuit_test.energies(terms=10)

mean=np.mean(E0),np.mean(E1),np.mean(E2)

#normalized energy transitions
E0-=mean[0]
E1-=mean[0]
E2-=mean[0]

l = plt.plot(t, E0, 'red', t, E1, 'blue', t, E2, 'green')

plt.axis([-10, 10, -10 ,3*E2[np.argmax(E2)]])

axcolor = 'lightgoldenrodyellow'

axfreq = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
axamp = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)

sEC = Slider(axfreq, 'EC', 0, 100, valinit=EC0) 
sEJ = Slider(axamp, 'EJ', 0, 100, valinit=EJ0)

#updates values when sliders are moved
def update(val):
    EC = sEC.val
    EJ = sEJ.val
    
    #recalculates energies
    circuit_test=trans(20,EC,EJ)
    E0,E1,E2=circuit_test.energies(terms=10)
    mean=np.array([np.mean(E0),np.mean(E1),np.mean(E2)])

    #updates y values for energies
    l[0].set_ydata(E0-mean[0])
    l[1].set_ydata(E1-mean[0])
    l[2].set_ydata(E2-mean[0])
    fig.canvas.draw_idle()

    #prints circuit statistics
    print((np.sqrt(8*EC*EJ)-EC)/(mean[1]-mean[0]))
    
    print(" var 1: \t"+str(np.var(E1)))

    print(" var 2: \t"+str(np.var(E2)))

    print(" anharm coef: \t"+str(np.log((np.mean(E2)-np.mean(E1))/(np.mean(E1)-np.mean(E0))-0.7)))

    print(" anharm: \t"+str((np.mean(E2)-np.mean(E1))/(np.mean(E1)-np.mean(E0))))

    print(" 4 ghz thresh: \t"+str(((np.mean(E1)-np.mean(E0))-4)**2))

    print(" Ej/Ec: \t"+ str(EJ/EC))


sEC.on_changed(update)
sEJ.on_changed(update)

resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')

#resets circuit to start point
def reset(event):
    sEC.reset()
    sEJ.reset()

button.on_clicked(reset)
plt.show()