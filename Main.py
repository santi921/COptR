
import plotly
plotly.tools.set_credentials_file(username='SantiagoVargas',api_key='JXpnCfKgjB1ZXDf72nsT')
import plotly.plotly as py
import plotly.graph_objs as go




trace1 = dict(type='scatter', x=[0, 1], y=[0, 0.5])
trace2 = dict(type='scatter', x=[0, 1], y=[0, -0.5])
trace3 = dict(type='scatter', x=[0, 1], y=[0, 1])
trace4 = dict(type='scatter', x=[0, 1], y=[0, -1])

steps = [None, None]
steps[0] = dict(method='restyle', args=['visible', [False, True]],)
steps[1] = dict(method='restyle', args=['visible', [True, False]],)

sliders = dict(steps=[steps,steps])

layout = dict(sliders=[sliders], xaxis=dict(range=[0, 1],), yaxis=dict( range=[-1, 1],))

data = go.Data([trace1, trace2, trace3, trace4])

fig = go.Figure(data=data, layout=layout)

py.iplot(fig, filename='test')


"""
1) create an instance of the individual circuit-->potentially to be generalized


2) input to a display class that prints out a seaborn console with sliders 
			
3) create an optimization class for the transmon

4) potentially make the optimimzation port to various different techniques

"""
