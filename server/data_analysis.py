import plotly.express as px
import plotly.io as pio
import pandas as pd


def generate_plot():
    x = pd.read_csv('./country_vaccinations.csv')
    #Replacing NaN values with 0
    x.fillna(0, inplace = True)
    x.drop(x.index[x['iso_code'] == 0], inplace = True)
    #Copying the dataframe for further use
    x_copy = x.copy()
    #Changing datatype of date column into date-time format
    x['date'] = pd.to_datetime(x['date'], format='%Y-%m-%d')
    x.columns
    #Removing the columns of 'source name' and 'source website' from the dataframe
    x.drop(["source_name","source_website"], axis=1, inplace=True)
    #Removing all rows with value of total vaccinations being 0 since it doesnt seem to be correct data
    x.drop(x.index[x["total_vaccinations"] == 0], inplace=True)
    #Plotting total vaccinations done monthly for each country as a line graph through plotly
    fig = px.line(x, x="date", y="total_vaccinations", color="country", line_group="country", hover_name="country",line_shape="spline", render_mode="svg",title="Total vaccinations monthly for each country")
    # fig.update_layout(title_x=0.5)
    # fig.show()

    # Example plot generation
    # df = px.data.iris()
    # fig = px.scatter(df, x='sepal_width', y='sepal_length', color='species', title='Iris Dataset')

    # Convert figure to JSON
    plot_json = pio.to_json(fig)

    return plot_json
