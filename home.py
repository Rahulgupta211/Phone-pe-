import streamlit as st

st.set_page_config(
    page_title="Aggregate Transaction & Users"
)

st.title("Transaction DashBoard as per year and quater")

import pandas as pd

import plotly.express as px

df1=pd.read_csv("agg_trans.csv")
df1["State"]=df1["State"].str.capitalize()
df1 = df1.replace('-',' ', regex=True)
df1['State'] = df1['State'].str.replace('Jammu & kashmir','Jammu & Kashmir')
df1['State'] = df1['State'].str.replace('Uttar pradesh','Uttar Pradesh')
df1['State'] = df1['State'].str.replace('Himachal pradesh','Himachal Pradesh')
df1['State'] = df1['State'].str.replace('Tamil nadu','Tamil Nadu')
df1['State'] = df1['State'].str.replace('Andhra pradesh','Andhra Pradesh')
df1['State'] = df1['State'].str.replace('Andaman & nicobar islands','Andaman & Nicobar')
df1['State'] = df1['State'].str.replace('Dadra & nagar haveli & daman & diu','Dadra and Nagar Haveli and Daman and Diu')
df1['State'] = df1['State'].str.replace('Arunachal pradesh','Arunanchal Pradesh')
df1['State'] = df1['State'].str.replace('West bengal','West Bengal')
df1['State'] = df1['State'].str.replace('Madhya pradesh','Madhya Pradesh')
#using pandas for conversion of State names
st.sidebar.header("Filter By Year & Quater:")#creating a filter by year and quater for user

category=st.sidebar.multiselect("Filter By Year:",
                                options=df1["Year"].unique(),
                                default=df1["Year"].unique())

Category=st.sidebar.multiselect("Filter By Quater:",
                                options=df1["Quater"].unique(),
                                default=df1["Quater"].unique())

selection_query=df1.query("Year== @category & Quater== @Category")

Total_Transaction_Amount=(selection_query['Transacion_amount'].sum())#displaying the total transaction amount 

Total_Transaction_count=(selection_query['Transacion_count'].sum())#displaying the total transaction count 

first_column,second_column=st.columns(2)

with first_column:
    st.markdown("### Total Transaction Amount:")
    st.subheader(f'{Total_Transaction_Amount}')

with second_column:
    st.markdown("### Total Transaction Count:")
    st.subheader(f'{Total_Transaction_count}')

fig=(selection_query.groupby(by=["State"]).sum()[["Transacion_amount","Transacion_count"]])
#creating a map with the help of plotly 
fig = px.choropleth(
    fig,
    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
    featureidkey='properties.ST_NM',
    locations=fig.index,
    color=fig.index,
    #color_continuous_scale='Reds'
    #hover_name="State",
    hover_data=["Transacion_amount","Transacion_count"],
    title="Phone Pe transaction Data"
    )
fig.update_geos(fitbounds="locations", visible=False)

st.plotly_chart(fig)

st.markdown("---")

fig1=(selection_query.groupby(by=["Transacion_type"]).sum()[["Transacion_amount","Transacion_count"]])
#creating a bar graph so user can see which type of transaction are done and its count
fig1=px.bar(fig1,
           x=fig1.index,
           y="Transacion_amount",
           color=fig1.index,
           #orientation='h',
           hover_data=["Transacion_amount","Transacion_count"],
          title="Transaction type graph by overall years")
fig1.update_layout(yaxis=(dict(showgrid=False)),width = 900, height = 500)

st.plotly_chart(fig1)

st.markdown("---")

st.title("User DashBoard as per year and quater")

df=pd.read_csv("agg_user.csv")
df["State"]=df["State"].str.capitalize()
df = df.replace('-',' ', regex=True)
df['State'] = df['State'].str.replace('Jammu & kashmir','Jammu & Kashmir')
df['State'] = df['State'].str.replace('Uttar pradesh','Uttar Pradesh')
df['State'] = df['State'].str.replace('Himachal pradesh','Himachal Pradesh')
df['State'] = df['State'].str.replace('Tamil nadu','Tamil Nadu')
df['State'] = df['State'].str.replace('Andhra pradesh','Andhra Pradesh')
df['State'] = df['State'].str.replace('Andaman & nicobar islands','Andaman & Nicobar')
df['State'] = df['State'].str.replace('Dadra & nagar haveli & daman & diu','Dadra and Nagar Haveli and Daman and Diu')
df['State'] = df['State'].str.replace('Arunachal pradesh','Arunanchal Pradesh')
df['State'] = df['State'].str.replace('West bengal','West Bengal')
df['State'] = df['State'].str.replace('Madhya pradesh','Madhya Pradesh')


st.sidebar.header("Filter By Year & Quater for users:")#creating a filter for the users that used phone pe

category1=st.sidebar.multiselect("Filter By Year for user:",
                                options=df["Year"].unique(),
                                default=df["Year"].unique())

Category1=st.sidebar.multiselect("Filter By Quater for user:",
                                options=df["Quater"].unique(),
                                default=df["Quater"].unique())

selection_query1=df.query("Year== @category1 & Quater== @Category1")

Total_User_Count=(selection_query1['Users_count'].sum())

st.markdown("### Total User Count:")
st.subheader(f'{Total_User_Count}')

try:
    fig4=(selection_query1.groupby(by=["State"]).sum()[["Users_count"]])
    #(selection_query.groupby(by=["Transacion_type"]).sum()[["Transacion_amount","Transacion_count"]])
except Exception:
    pass
#creating a map to identify in which part the users have used phone pe
fig4 = px.choropleth(
    fig4,
    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
    featureidkey='properties.ST_NM',
    locations=fig4.index,
    color=fig4.index,
    #color_continuous_scale='Reds'
    #hover_name="State or union territory",
    hover_data=["Users_count"],
    title="India phonepe Users",
)
fig4.update_geos(fitbounds="locations", visible=False)
st.plotly_chart(fig4)

st.markdown("---")

#try:
fig6=(selection_query1.groupby(by=['State']).sum()[["Users_count"]])
#except Exception:
 #   pass
#creating a graph to identify in which year and quater there is a rise
fig6=px.bar(fig6,
           y=fig6.index,
           x="Users_count",
           orientation='h',
           #labels=fig6.index,
           color=fig6.index,
           hover_data=["Users_count"],
          title="Users graph by overall years")
fig6.update_layout(yaxis=(dict(showgrid=False)),width = 900, height = 500)
st.plotly_chart(fig6)

st.markdown("---")

#try:
fig8=(selection_query1.groupby(by=["Brand_Name"]).sum()[["Users_count"]])
#except Exception:
 #   pass
#creating a pie so that the we can know which brand users have used phone pe the most
fig8=px.pie(fig8,
           names=fig8.index,
           values="Users_count",
           color=fig8.index,
           #orientation='h',
           hover_data=["Users_count"],
          title="Pie chart of brands and its users")
fig8.update_layout(yaxis=(dict(showgrid=False)),width = 900, height = 500)

st.plotly_chart(fig8)
