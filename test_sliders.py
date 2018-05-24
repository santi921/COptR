import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
from Diag_trans import trans

#there lines create the defaults of the plots
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.25)
EJ0 = 50.0
EC0 = 50.0
#delta_f = 5.0
t=np.arange(-10,10,1)

circuit_test=trans(10,EC0,EJ0)
E0,E1,E2=circuit_test.energies(terms=10)

mean=np.mean(E0),np.mean(E1),np.mean(E2)

E0-=mean[0]
E1-=mean[0]
E2-=mean[0]

l = plt.plot(t, E0, 'red', t, E1, 'blue', t, E2, 'green')

plt.axis([-10, 10, -50 ,3*E2[np.argmax(E2)]])

axcolor = 'lightgoldenrodyellow'

axfreq = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
axamp = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)

sEC = Slider(axfreq, 'EJ', 1, 100.0, valinit=EC0) 
sEJ = Slider(axamp, 'EC', 1, 100.0, valinit=EJ0)


def update(val):
    EC = sEC.val
    EJ = sEJ.val
    
    circuit_test=trans(10,EC,EJ)
    E0,E1,E2=circuit_test.energies(terms=10)
    mean=np.mean(E0),np.mean(E1),np.mean(E2)

   	
    
    l[0].set_ydata(E0-mean[0])
    l[1].set_ydata(E1-mean[0])
    l[2].set_ydata(E2-mean[0])
    fig.canvas.draw_idle()
    print(np.sqrt(8*EC*EJ),(mean[1]-mean[0]))
    

sEC.on_changed(update)
sEJ.on_changed(update)

resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')


def reset(event):
    sEC.reset()
    sEJ.reset()

button.on_clicked(reset)

#rax = plt.axes([0.025, 0.5, 0.15, 0.15], facecolor=axcolor)

plt.show()