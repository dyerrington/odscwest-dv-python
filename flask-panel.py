from flask import Flask, render_template

import pandas as pd, numpy as np
import matplotlib.pyplot as plt

from bokeh.embed import server_document
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
import param
import panel as pn
from bokeh.server.server import Server
from tornado.ioloop import IOLoop

df         = pd.read_csv("data/avocado.csv.zip").drop(columns = ["Unnamed: 0"])
df['Date'] = pd.to_datetime(df['Date'])
df         = df.set_index('Date')

class Test(param.Parameterized):
    offset    = param.Number(default=0.0, bounds=(-5.0, 5.0))
    N         = param.Integer(default=200, bounds=(0, None))
    amplitude = param.Number(default=1.0, bounds=(-5.0, 5.0))
    phase     = param.Number(default=0.0, bounds=(0.0, 2 * np.pi))
    frequency = param.Number(default=1.0, bounds=(0.1, 5.1))

    def sine(self):
        x = np.linspace(0, 4 * np.pi, self.N)
        y = self.amplitude * np.sin(self.frequency * x + self.phase) + self.offset
        return x, y
    
    @param.depends('N', 'frequency', 'amplitude', 'offset', 'phase')
    def plot(self):
        x, y = self.sine()
        self.df = pd.DataFrame(dict(x = x, y = y))
        # Plot
        fig = plt.figure(figsize = (15, 6))
        ax = fig.add_subplot(121);
        self.df.plot(x = "x", y = "y", ax = ax)
        fig.tight_layout();
        plt.close()
        return fig;
        
    def panel(self):
        return pn.Column(self.param, self.plot)

class Avocado(param.Parameterized):

    column = param.ObjectSelector(objects =  df.select_dtypes(exclude = ["object", "datetime64[ns]"]).columns.tolist())
    date   = param.DateRange(bounds = [df.index.min(), df.index.max()])
    
    
    @param.depends('column', 'date')
    def plot(self):
        
        if self.column:
            
            fig, ax = plt.subplots(nrows = 1, ncols = 1, figsize = (10, 5))
            
            if self.date:
                date_range     = (df.index > self.date[0]) & (df.index < self.date[1])
                date_range_str = f"- {self.date[0].strftime('%Y-%m-%d')} - {self.date[1].strftime('%Y-%m-%d')}"
                df_filtered    = df[date_range][self.column]
            else:
                date_range_str = ""
                df_filtered = df[self.column]
                
            df_filtered.plot(ax = ax, title = f"Column - {self.column} {date_range_str}")
            plt.close()
            return fig
    
    def panel(self):
        return pn.Row(self.param, self.plot)

# Begin Flask Config
app = Flask(__name__)

## Builds the document structure
def update_test(doc):
    test = Test()
    doc.add_root(test.panel().get_root(doc))

def update_avocado(doc):
    avocado = Avocado()
    avocado.add_root(test.panel().get_root(doc))

@app.route('/', methods=['GET'])
def index():
    test    = server_document('http://127.0.0.1:8080/test')
    avocado = server_document('http://127.0.0.1:8080/avocado')
    return render_template(
        "demo.html", 
        sine    = test, 
        avocado = avocado
    )

def test_worker():
    # Can't pass num_procs > 1 in this configuration. If you need to run multiple
    # processes, see e.g. flask_gunicorn_embed.py
    server = Server({'/test': update_test}, io_loop=IOLoop(), allow_websocket_origin=["127.0.0.1:8080"])
    server.start()
    server.io_loop.start()

def avocado_worker():
    # Can't pass num_procs > 1 in this configuration. If you need to run multiple
    # processes, see e.g. flask_gunicorn_embed.py
    server = Server({'/avocado': update_test}, io_loop=IOLoop(), allow_websocket_origin=["127.0.0.1:8080"])
    server.start()
    server.io_loop.start()

from threading import Thread
Thread(target=test_worker).start()
Thread(target=avocado_worker).start()

# # Server Config
# routes = {
#      # route/url : panel application / layout
#      'avocado':  avocdo.panel,
#      'test':     test.panel
# }

# pn.serve(routes, port = 8080, show = False, websocket_origin = "127.0.0.1:8080")
