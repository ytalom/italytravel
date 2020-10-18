import pandas as pd
#import joblib
import pickle
import plotly.graph_objects as go

def show_results(res,filepath):
    #model = joblib.load('recommend.model')
    model = pickle.load(open('rec.model', 'rb'))
    class_pre = model.predict([res])[0]
    if class_pre == 12:
        model1 = pickle.load(open('11.model', 'rb'))
        class_pre1 = model1.predict([res])[0]
        data = pd.read_csv('1.csv')
        data_to_show = data.loc[data['class'] == class_pre1]
    else:
        data = pd.read_csv('result.csv')
        data_to_show = data.loc[data['class'] == class_pre]
        
    num = len(data_to_show)//4
    data1 = data_to_show.iloc[0:num]
    data2 = data_to_show.iloc[num : 2 * num]
    data3 = data_to_show.iloc[ 2 * num : 3 * num]
    data4 = data_to_show.iloc[3 * num:]
    fig = go.Figure()
    fig.add_trace(go.Scattergeo(lon = data1['lon'],lat = data1['lat'],text = data1['location'],marker_color='crimson',
                        marker = dict(size = data1['popularity'] * 5,color = 'crimson',line_color='rgb(40,40,40)',
                                      line_width=0.5,sizemode = 'area'),
                        name = 'Most popular'))
    fig.add_trace(go.Scattergeo(lon = data2['lon'],lat = data2['lat'],text = data2['location'],marker_color='orange',
                        marker = dict(size = data2['popularity'] * 5,color = 'orange',line_color='rgb(40,40,40)',
                                      line_width=0.5,sizemode = 'area'),
                        name = 'Popular'))
    fig.add_trace(go.Scattergeo(lon = data3['lon'],lat = data3['lat'],text = data3['location'], marker_color='lightseagreen',
                        marker = dict(size = data3['popularity'] * 5,color = 'lightseagreen',line_color='rgb(40,40,40)',
                                      line_width=0.5,sizemode = 'area'),
                    name = 'Not so popular'))
    fig.add_trace(go.Scattergeo(lon = data4['lon'],lat = data4['lat'],text = data4['location'],marker_color='royalblue',
                        marker = dict(size = data4['popularity'] * 5,color = 'royalblue',line_color='rgb(40,40,40)',
                                      line_width=0.5,sizemode = 'area'),
                        name = 'Least popular'))
    fig.update_layout(
            title_text = 'Recommendations',title_x=0.5,
            showlegend = True,
            geo = dict(
                scope = 'europe',
                resolution = 50,
                lonaxis_range= [ 6.6, 18.4 ],
                lataxis_range= [35.47, 47.25],
                landcolor = 'rgb(217, 217, 217)',
            )
        )
    fig.write_html(filepath)
