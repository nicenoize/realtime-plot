
import dash
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
import dash_daq as daq
import random
from collections import deque
import plotly
import paho.mqtt.client as mqtt
from datetime import datetime


external_stylesheets = [dbc.themes.BOOTSTRAP]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

# Mockupvalues for CRYVISIL LIVE GRAPH
X = deque(maxlen = 20)
X.append(1)
Y = deque(maxlen = 20)
Y.append(1)

main_pressure = []
main_pressure_timestamps = []

mqtt_cryvisil = [
    '/EPICS_FHI/CRYVISIL/TPG256/MAIN/Pressure',
    '/EPICS_FHI/CRYVISIL/TPG256/PRE/Pressure',
    '/EPICS_FHI/CRYVISIL/TPG256/PREP/Pressure',
]
mqtt_fhimp = [
    '/EPICS_FHI/FHIMP/HeDrop/Droplet_Source_RAW',
    '/EPICS_FHI/FHIMP/HeDrop/Forepressure_Droplet_Src',
    '/EPICS_FHI/FHIMP/HeDrop/Forepressure_Excitation_Chamber',
]
mqtt_ppb = [
    '/EPICS_FHI/PPB/VmeCrateAfm/FanSpeed1',
    '/EPICS_FHI/PPB/VmeCrateAfm/IM12',
    '/EPICS_FHI/PPB/VmeCrateAfm/IP12',
    '/EPICS_FHI/PPB/VmeCrateAfm/IP3',
    '/EPICS_FHI/PPB/VmeCrateAfm/IP5',
    '/EPICS_FHI/PPB/VmeCrateAfm/temp1',
    '/EPICS_FHI/PPB/VmeCrateAfm/temp2',
    '/EPICS_FHI/PPB/VmeCrateAfm/temp3',
    '/EPICS_FHI/PPB/VmeCrateAfm/VM12',
    '/EPICS_FHI/PPB/VmeCrateAfm/VP12',
    '/EPICS_FHI/PPB/VmeCrateAfm/VP3',
    '/EPICS_FHI/PPB/VmeCrateAfm/VP5',
]

mqtt_simu = [
    '/EPICS_FHI/SIMU/Undulator/GetGap',
    '/EPICS_FHI/SIMU/Undulator/MoveStatus',
    '/EPICS_FHI/SIMU/Undulator/SetGap',
]

mqtt_ramp = [
    '/EPICS_FHI/ramp',
]
# RTEMS = Realtime Operating System
mqtt_rtems = [
    '/EPICS_FHI/rtems/calcExample2',
    '/EPICS_FHI/rtems/circle/tick',
    '/EPICS_FHI/rtems/circle/x',
    '/EPICS_FHI/rtems/circle/y',
    '/EPICS_FHI/rtems/line/a',
]

mqtt_updateStatus = '/EPICS_FHI/updateStatus'

mqtt_topics = mqtt_cryvisil + mqtt_fhimp + mqtt_ppb + mqtt_simu + mqtt_ramp + mqtt_rtems + [mqtt_updateStatus]

# Next we will initialize lists which will be filled by MQTT and the timestamp of each occurrence
main_pressure = [0]
pre_pressure = [0]
prep_pressure = [0]

droplect_source_raw = [0]
forepressure_droplet_source = [0]
forepressure_excitation_chamber = [0]

fanspeed_1 = [0]
temp1 = [0]
temp2 = [0]
temp3 = [0]

main_pressure_timestamps = [datetime.now()]
pre_pressure_timestamps = [datetime.now()]
prep_pressure_timestamps = [datetime.now()]

droplect_source_raw_timestamps = [datetime.now()]
forepressure_droplet_source_timestamps = [datetime.now()]
forepressure_excitation_chamber_timestamps = [datetime.now()]

fanspeed_1_timestamps = [datetime.now()]
temp1_timestamps = [datetime.now()]
temp2_timestamps = [datetime.now()]
temp3_timestamps = [datetime.now()]

timestamps_main_pressure = []

# Mockupvalues fo
import paho.mqtt.client as mqtt

mqttClient = mqtt.Client("P0") #create new instance

def on_connect(client, userdata, flags, rc): # The callback for when the client connects to the broker
    #print("Connected with result code {0}".format(str(rc))) # Print result of connection attempt
    for topic in mqtt_topics:
        mqttClient.subscribe(topic)

def on_message(client, userdata, msg): # The callback for when a PUBLISH message is received from the server.
    if msg.topic == '/EPICS_FHI/CRYVISIL/TPG256/MAIN/Pressure':
        main_pressure.append(float(msg.payload))
        main_pressure_timestamps.append(datetime.now())
        #print(main_pressure)
    elif msg.topic == "/EPICS_FHI/CRYVISIL/TPG256/PRE/Pressure":
        pre_pressure.append(float(msg.payload.decode()))
        pre_pressure_timestamps.append(datetime.now())
        #print(pre_pressure)
    elif msg.topic == "/EPICS_FHI/CRYVISIL/TPG256/PREP/Pressure":
        prep_pressure.append(float(msg.payload.decode()))
        prep_pressure_timestamps.append(datetime.now())
    elif msg.topic == "/EPICS_FHI/FHIMP/HeDrop/Droplet_Source_RAW":
        droplect_source_raw.append(float(msg.payload.decode()))
        droplect_source_raw_timestamps.append(datetime.now())
        print(msg.topic)
    elif msg.topic == "/EPICS_FHI/FHIMP/HeDrop/Forepressure_Droplet_Src":
        forepressure_droplet_source.append(float(msg.payload.decode()))
        forepressure_droplet_source_timestamps.append(datetime.now())
        print(msg.topic)
    elif msg.topic == "/EPICS_FHI/FHIMP/HeDrop/Forepressure_Excitation_Chamber":
        forepressure_excitation_chamber.append(float(msg.payload.decode()))
        forepressure_excitation_chamber_timestamps.append(datetime.now())
        print(msg.topic)
    elif msg.topic == "/EPICS_FHI/PPB/VmeCrateAfm/FanSpeed1":
        fanspeed_1.append(float(msg.payload.decode()))
        fanspeed_1_timestamps.append(datetime.now())
    elif msg.topic == "/EPICS_FHI/PPB/VmeCrateAfm/temp1":
        temp1.append(float(msg.payload.decode()))
        temp1_timestamps.append(datetime.now())
        print(msg.topic)
        print(msg)
    elif msg.topic == "/EPICS_FHI/PPB/VmeCrateAfm/temp2":
        temp2.append(float(msg.payload.decode()))
        temp2_timestamps.append(datetime.now())
        print(msg.topic)
        print(msg)
    elif msg.topic == "/EPICS_FHI/PPB/VmeCrateAfm/temp3":
        temp3.append(float(msg.payload.decode()))
        temp3_timestamps.append(datetime.now())
        print(msg.topic)
        print(msg)
    elif msg.topic == "'/EPICS_FHI/SIMU/Undulator/GetGap'":
        print(msg.topic)
        print(msg.payload)
    elif msg.topic == "'/EPICS_FHI/SIMU/Undulator/SetGap'":
        print(msg.topic)
        print(msg.payload)
    #print("Message received-> " + msg.topic + " " + str(msg.payload.decode())) # Print a received msg

mqttClient.on_connect = on_connect
mqttClient.on_message = on_message

mqttClient.connect("aav.rz-berlin.mpg.de", 1883, 60) #connect to broker

mqttClient.loop_start() # Start networking daemon non blocking




MQTT_TOPIC_Registration_Response = '#'

suffix_row = '_row'
suffix_button_id = '_button'
suffix_line_graph = '_line_graph'
suffix_count = '_count'
suffix_workload_n = '_WL_number'
suffix_workload_g = '_WL_graph'
suffix_indicator = '_indicator'

# Inline CSS
tabs_styles = {
    'height': '44px'
}
tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px',
    'fontWeight': 'bold'
}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#119DFF',
    'color': 'white',
    'padding': '6px'
}

# Mockupdata
mqtt_cryvisil = {
    '/EPICS_FHI/CRYVISIL/TPG256/MAIN/Pressure',
    '/EPICS_FHI/CRYVISIL/TPG256/PRE/Pressure',
    '/EPICS_FHI/CRYVISIL/TPG256/PREP/Pressure'
}
mqtt_fhimp = {
    '/EPICS_FHI/FHIMP/HeDrop/Droplet_Source_RAW',
    '/EPICS_FHI/FHIMP/HeDrop/Forepressure_Droplet_Src',
    '/EPICS_FHI/FHIMP/HeDrop/Forepressure_Excitation_Chamber'
}
mqtt_ppb = {
    '/EPICS_FHI/PPB/VmeCrateAfm/FanSpeed1',
    '/EPICS_FHI/PPB/VmeCrateAfm/IM12',
    '/EPICS_FHI/PPB/VmeCrateAfm/IP12',
    '/EPICS_FHI/PPB/VmeCrateAfm/IP3',
    '/EPICS_FHI/PPB/VmeCrateAfm/IP5',
    '/EPICS_FHI/PPB/VmeCrateAfm/temp1',
    '/EPICS_FHI/PPB/VmeCrateAfm/temp2',
    '/EPICS_FHI/PPB/VmeCrateAfm/temp3',
    '/EPICS_FHI/PPB/VmeCrateAfm/VM12',
    '/EPICS_FHI/PPB/VmeCrateAfm/VP12',
    '/EPICS_FHI/PPB/VmeCrateAfm/VP3',
    '/EPICS_FHI/PPB/VmeCrateAfm/VP5'
}
mqtt_simu = {
    '/EPICS_FHI/SIMU/Undulator/GetGap',
    '/EPICS_FHI/SIMU/Undulator/MoveStatus',
    '/EPICS_FHI/SIMU/Undulator/SetGap'
}
mqtt_ramp = {
    '/EPICS_FHI/ramp'
}
# RTEMS = Realtime Operating System
mqtt_rtems = {
    '/EPICS_FHI/rtems/calcExample2',
    '/EPICS_FHI/rtems/circle/tick',
    '/EPICS_FHI/rtems/circle/x',
    '/EPICS_FHI/rtems/circle/y',
    '/EPICS_FHI/rtems/line/a'
}

mqtt_updateStatus = '/EPICS_FHI/updateStatus'

# Build panels
def build_gauge_panel(id, name, min=0, max=10):
    return html.Div([
        daq.Gauge(
            color={"gradient":True,"ranges":{"green":[0,6],"yellow":[6,8],"red":[8,10]}},
            id='' + str(id),
            label=name,
            className='gauge',
            value=0,
            min=min,
            max=max,
        ),
    ])

def build_status_indicator(id, name, color='#119DFF', status='OK'):
    return html.Div([
        daq.Indicator(
            id='' + str(id),
            label=name,
            className='indicator',
            value=status,
            color='#119DFF',
            style={
                'margin-bottom': '5%'
            }
        ),
    ])

def build_temp_panel(id, name):
    return html.Div([
        daq.Thermometer(
            id='' + str(id),
            label=name,
            className='thermometer',
            value=0,
            min=0,
            max=10,
            scale={'start': 2, 'interval': 3,
            'labelInterval': 2, 'custom': {
                '2': 'ideal temperature',
                '5': 'projected temperature'
            }},
            style={
                'margin-bottom': '5%'
            }
        ),
    ])


def build_chart_panel(id):
    return html.Div(
        id='control-chart-container' + str(id),
        className='twelve columns',
        children=[
            dcc.Interval(
                id='interval-component' + str(id),
                interval=2 * 1000,  # in milliseconds
                n_intervals=0,
            ),

            dcc.Store(
                id='control-chart-state' + str(id)
            ),
            dcc.Graph(
                id="control-chart-live" + str(id),
                figure=go.Figure({
                    'data': [{'x': [], 'y': [], 'mode': 'lines+markers', 'name': params[1]}],
                    'layout': {
                        'paper_bgcolor': 'rgb(45, 48, 56)',
                        'plot_bgcolor': 'rgb(45, 48, 56)'
                    }
                }
                )
            )
        ]
    )

app.layout = html.Div([ 
    html.Div([
        dcc.Interval(
        id = 'graph-update',
            interval = 1000,
            n_intervals = 0
        ),
    html.Div(
    [
        # On this Tab, the user enters the data for the MQTT connection, which will fetch the data from the MQTT broker
        dcc.Tabs(id='tabs-with-classes', parent_className='custom-tabs', children = [
            dcc.Tab(id='tab1', label='Set Values & Limits', style=tab_style, selected_style=tab_selected_style, children=[
                html.Div([
                    html.Div([
                        dbc.Card(
                            dbc.CardBody([
                                dbc.Row([
                                    dbc.Col(
                                        dbc.Input(
                                            id='set-ideal-temp1',
                                            placeholder='Set ideal for Temp 1',
                                            debounce = True),
                                    ),
                                    dbc.Col(
                                        dbc.Input(
                                            id='set-critical-temp1',
                                            placeholder='Set critical treshold for Temp 1',
                                            debounce = True),
                                        ),
                                    dbc.Col(
                                        dbc.Button(
                                            'Set Limits',
                                            id='set-limits-button',
                                            color='primary',
                                            className='mr-1'
                                        ),
                                    ),
                                ]),
                                dbc.Row([
                                    dbc.Col(
                                        dbc.Input(
                                            id='set-ideal-temp2',
                                            placeholder='Set ideal for Temp 2',
                                            debounce = True),
                                    ),
                                    dbc.Col(
                                        dbc.Input(
                                            id='set-critical-temp2',
                                            placeholder='Set critical treshold for Temp 2',
                                            debounce = True),
                                        ),
                                    dbc.Col(
                                        dbc.Button(
                                            'Set Limits',
                                            id='set-limits-button-t2',
                                            color='primary',
                                            className='mr-1'
                                        ),
                                    ),
                                ], style={'margin-top': '3%'}),

                                dbc.Row([
                                    dbc.Col(
                                        dbc.Input(
                                            id='set-ideal-temp3',
                                            placeholder='Set ideal for Temp 3',
                                            debounce = True),
                                    ),
                                    dbc.Col(
                                        dbc.Input(
                                            id='set-critical-temp3',
                                            placeholder='Set critical treshold for Temp 3',
                                            debounce = True),
                                        ),
                                    dbc.Col(
                                        dbc.Button(
                                            'Set Limits',
                                            id='set-limits-button-t3',
                                            color='primary',
                                            className='mr-1'
                                        ),
                                    ),
                                ], style={'margin-top': '3%'}),
                            ]),
                        ),

                        dbc.Card(
                            dbc.CardBody([
                                dbc.Row([
                                    dbc.Col(
                                       dbc.Input(
                                            id='set-undulator-gap-input',
                                            placeholder='Set Undulator Gap',
                                            debounce = True),     
                                    ),
                                    dbc.Col(
                                        dbc.Button(
                                            'Set Gap',
                                            id='set-undulator-gap-button',
                                            color='primary',
                                            className='mr-1',
                                            n_clicks = 0
                                        ),
                                    ),
                                ]),
                            ], style={'margin-top': '1%'}),
                        ),
                    ], style={'width': '33%', 'margin': 20}),

                ], style={'width': '100%', 'margin': 20})

            ]),
            dcc.Tab(id='tab2', label='Dashboard', style=tab_style, selected_style=tab_selected_style, children=[
            # On this Tab, the user can see the data from the MQTT broker in the forms of plots. Also the user will see
            # whether the status of the devices is OK or needs attention. Also values can be changed here.

                dcc.Tabs(id='tabs-with-classeas', parent_className='custom-tabs', value = 'Dashboard', 
                        className='custom-tabs-container', children=[
                            dcc.Tab(label='CRYVISIL', style=tab_style, selected_style=tab_selected_style,  className='custom-tab', selected_className='custom-tab--selected', children=[
                                html.Div(
                                    [
                                dbc.Card(
                                        dbc.CardBody([
                                            dbc.Row([
                                                dbc.Col(build_gauge_panel(id='live-main-pressure', name='MAIN_PRESSURE'), md=4),
                                                dbc.Col(build_gauge_panel(
                                                    id='live-pre-pressure', name='PRE_PRESSURE'), md=4),
                                                dbc.Col(build_gauge_panel(
                                                    id='live-prep-pressure', name='PREP_PRESSURE'), md=4),
                                            ]),
                                        ]),
                                ),
                                    ], style={'width': '100%', 'margin': 20}),
                                html.Div(
                                    [
                                dbc.Card(
                                        dbc.CardBody([
                                            dbc.Row([
                                                dbc.Col(dcc.Graph(id = 'live-graph-main-pressure', animate = True), md=4),
                                                dbc.Col(dcc.Graph(id = 'live-graph-pre-pressure', animate = True), md=4),
                                                dbc.Col(dcc.Graph(id = 'live-graph-prep-pressure', animate = True), md=4),
                                            ]),
                                        ]),
                                ),
                                    ], style={'width': '100%', 'margin': 20}),
                            ]),
                            dcc.Tab(label='FHIMP', style=tab_style,  className='custom-tab', selected_className='custom-tab--selected', children=[
                                html.Div(
                                    [
                                dbc.Card(
                                        dbc.CardBody([
                                            dbc.Row([
                                                dbc.Col(build_gauge_panel(
                                                    id='forepressure_droplet_src', name='Forepressure_Droplet_Src'), md=6),
                                                dbc.Col(build_gauge_panel(
                                                    id='forepressure_excitation_chamber', name='Forepressure_Excitation_Chamber'), md=6)
                                            ]),
                                        ]),
                                ),
                                    ], style={'width': '100%', 'margin': 20}),
                            ]),
                            dcc.Tab(label='PPB', style=tab_style, selected_style=tab_selected_style, className='custom-tab', selected_className='custom-tab--selected', children=[
                                html.Div([
                                    dbc.Card(
                                        dbc.CardBody([
                                            dbc.Row([
                                                dbc.Col([
                                                    build_temp_panel(id='temp1', name='temp1'),
                                                    build_status_indicator(id='temp1_indicator', name='temp1'),
                                                ], md=4),
                                                
                                                dbc.Col([
                                                    build_temp_panel(id='temp2', name='temp2'),
                                                    build_status_indicator(id='temp2_indicator', name='temp2'),
                                                ], md=4),
                                                dbc.Col([
                                                    build_temp_panel(id='temp3', name='temp3'),
                                                    build_status_indicator(id='temp3_indicator', name='temp3'),
                                                ], md=4),
                                                
                                            ], style={'width': '100%', 'margin': 20}),

                                        ])
                                    ),
                                ]),
                                html.Div([
                                    dbc.Card(
                                        dbc.CardBody([
                                            dbc.Row([
                                                dbc.Col([
                                                    build_gauge_panel(id='fanSpeed1', name='FanSpeed1', max=10000),
                                                ])
                                            ], style={'width': '100%', 'margin': 20}),
                                        ])
                                    ),
                                ]),
                            ]),
                           
                            ]),

        ]),

    ])]
)])
])

# Callbacks for Cryvisil Tab
# Update live scatter plots for CRYVISIL PAGE
@app.callback(
	Output('live-graph-main-pressure', 'figure'),
	[ Input('graph-update', 'n_intervals') ]
)

def update_graph_scatter(n):
	X.append(X[-1]+1)
	Y.append(Y[-1]+Y[-1] * random.uniform(-0.1,0.1))
	data = plotly.graph_objs.Scatter(
			x=main_pressure_timestamps,
			y=main_pressure,
			name='Scatter',
			mode= 'lines+markers'
	)
    
	return {'data': [data],
			'layout' : go.Layout(xaxis=dict(range=[min(main_pressure_timestamps),max(main_pressure_timestamps)]),yaxis = dict(range = [main_pressure[1],max(main_pressure)]),)}

@app.callback(
	Output('live-graph-pre-pressure', 'figure'),
	[ Input('graph-update', 'n_intervals') ]
)

def update_graph_scatter(n):
	X.append(X[-1]+1)
	Y.append(Y[-1]+Y[-1] * random.uniform(-0.1,0.1))
	data = plotly.graph_objs.Scatter(
			x=pre_pressure_timestamps,
			y=pre_pressure,
			name='Scatter',
			mode= 'lines+markers'
	)
	return {'data': [data],
			'layout' : go.Layout(xaxis=dict(range=[min(pre_pressure_timestamps),max(pre_pressure_timestamps)]),yaxis = dict(range = [pre_pressure[1],max(pre_pressure)]),)}

# Update live scatter plots
@app.callback(
	Output('live-graph-prep-pressure', 'figure'),
	[ Input('graph-update', 'n_intervals') ]
)

def update_graph_scatter(n):
	X.append(X[-1]+1)
	Y.append(Y[-1]+Y[-1] * random.uniform(-0.1,0.1))
	data = plotly.graph_objs.Scatter(
			x=prep_pressure_timestamps,
			y=prep_pressure,
			name='Scatter',
			mode= 'lines+markers'
	)
	return {'data': [data],
			'layout' : go.Layout(xaxis=dict(range=[min(prep_pressure_timestamps),max(prep_pressure_timestamps)]),yaxis = dict(range = [prep_pressure[1],max(prep_pressure)]),)}


@app.callback(Output('live-main-pressure', 'value'), Output('live-main-pressure', 'max'), Input('graph-update', 'n_intervals'))
def update_output(n):
    if(len(main_pressure) > 0):
        value = main_pressure[-1]*10000000000
    else:
        pass
    #maximum = max(main_pressure)
    maximum = 100
    return value, maximum

@app.callback(Output('live-pre-pressure', 'value'), Output('live-pre-pressure', 'max'), Input('graph-update', 'n_intervals'))
def update_output(n):
    if(len(pre_pressure) > 0):
        pre_pr = pre_pressure[-1]
    else:
        pass
    maximum = 2000
    return pre_pr, maximum

@app.callback(Output('live-prep-pressure', 'value'), Output('live-prep-pressure', 'max'), Input('graph-update', 'n_intervals'))
def update_output(n):
    if(len(prep_pressure) > 0):
        prep_pr = prep_pressure[-1]*1000000000
    else:
        pass
    #maximum = max(main_pressure)
    maximum = 1000
    return prep_pr, maximum

# Callbacks for FHIMP Tab
@app.callback(Output('forepressure_droplet_src', 'value'), Input('graph-update', 'n_intervals'))
def update_output(n):
    #value = forepressure_droplet_source[-1]*1000000000
    #maximum = 100
    #return value, maximum
    return random.randint(0,10)

@app.callback(Output('forepressure_excitation_chamber', 'value'), Input('graph-update', 'n_intervals'))
def update_output(n):
    value = Y.append(Y[-1]+Y[-1] * random.uniform(-0.1,0.1))
    return random.randint(0,10)


# Callbacks for PPB Tab
@app.callback(Output('temp1', 'value'), Input('graph-update', 'n_intervals'))
def update_output(n):
    value = Y.append(Y[-1]+Y[-1] * random.uniform(-0.1,0.1))
    return random.randint(0,10)

@app.callback(Output('temp2', 'value'), Input('graph-update', 'n_intervals'))
def update_output(n):
    value = Y.append(Y[-1]+Y[-1] * random.uniform(-0.1,0.1))
    return random.randint(0,10)

@app.callback(Output('temp3', 'value'), Input('graph-update', 'n_intervals'))
def update_output(n):
    value = Y.append(Y[-1]+Y[-1] * random.uniform(-0.1,0.1))
    return random.randint(0,10)

@app.callback(
    Output('temp1_indicator', 'color'),
    Input('temp1', 'value'),
)
def update_output(value):
    # if value is bigger than 7 return red, else return green. Handle the case where value is None
    if value is None:
        return 'grey'
    elif value > 7:
        return 'red'
    else:
        return 'green'

@app.callback(
    Output('temp2_indicator', 'color'),
    Input('temp2', 'value'),
)
def update_output(value):
    # if value is bigger than 7 return red, else return green. Handle the case where value is None
    if value is None:
        return 'grey'
    elif value > 7:
        return 'red'
    else:
        return 'green'

@app.callback(
    Output('temp3_indicator', 'color'),
    Input('temp3', 'value'),
)
def update_output(value):
    # if value is bigger than 7 return red, else return green. Handle the case where value is None
    if value is None:
        return 'grey'
    elif value > 7:
        return 'red'
    else:
        return 'green'

@app.callback(Output('fanSpeed1', 'value'), Input('graph-update', 'n_intervals'))
def update_output(n):
    value = Y.append(Y[-1]+Y[-1] * random.uniform(-0.1,0.1))
    return fanspeed_1[-1]

# Callback for button with id 'set-undulator-gap-button'
@app.callback(
    Output('set-undulator-gap-input', 'value'),
    Input('set-undulator-gap-button', 'n_clicks'),
    State('set-undulator-gap-input', 'value'))
def set_undulator_gap(n_clicks, value):
    mqttClient.publish("/EPICS_FHI/SIMU/Undulator/SetGap", value)
    print("Set Gap to: " + str(value))
    return value

if __name__ == '__main__':
    app.run_server(debug=False)



