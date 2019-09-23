#import plotly.plotly as py
import chart_studio.plotly as py
from plotly.graph_objs import *
import datetime
import random

py.sign_in('L_JUHEE','rkIkhJkcbyUI9bap0pFZ')

axis=Scatter(
        x=datetime.datetime.now(),
        #y=random.randrange(0,100)
        y=10
        )

data=Data([axis])

py.plot(data, filename='Graph', fileopt='extend')
