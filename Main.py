
import numpy as np
import matplotlib.pyplot as plt
from Diag_trans import trans
plotly.tools.set_credentials_file(username='SantiagoVargas',api_key='JXpnCfKgjB1ZXDf72nsT')





E0=np.array(E0)
E1=np.array(E1)
E2=np.array(E2)

print(E0)
print(E1)
print(E2)

plt.plot(np.array(range(-20,20,1)),E0)
plt.plot(np.array(range(-20,20,1)),E1)
plt.plot(np.array(range(-20,20,1)),E2)
plt.show()

max=np.argmax(E2)
min=np.argmin(E0)
print(E2[max],E0[min])

trace1=dict(type='scatter', x=np.array(range(-20,20,1)), y=E0)
trace2=dict(type='scatter', x=np.array(range(-20,20,1)), y=E1)
trace3=dict(type='scatter', x=np.array(range(-20,20,1)), y=E2)

steps = [None, None]
steps[0] = dict(method='restyle', args=['visible', [False, True]],)
steps[1] = dict(method='restyle', args=['visible', [True, False]],)

sliders = dict(steps=steps)

layout = dict(sliders=[sliders], xaxis=dict(range=[-2, 2],), yaxis=dict(range=[E0[min],E2[max]],))

data = go.Data([trace1, trace2, trace3])

fig = go.Figure(data=data, layout=layout)

def update(val):
    amp = samp.val
    freq = sfreq.val
    l.set_ydata(amp*np.sin(2*np.pi*freq*t))
    fig.canvas.draw_idle()
sfreq.on_changed(update)
samp.on_changed(update)

resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')




"""

1) create an instance of the individual circuit-->potentially to be generalized


2) input to a display class that prints out a seaborn console with sliders 
			
3) create an optimization class for the transmon

4) potentially make the optimimzation port to various different techniques

"""
