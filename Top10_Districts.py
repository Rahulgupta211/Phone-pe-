import pandas as pd

import plotly.express as px

import streamlit as st

df1=pd.read_csv("top_tran_distname.csv")
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

st.title("Transaction DashBoard for top districts as per year and quater")

st.sidebar.header("Filter By Year & Quater:")

category=st.sidebar.multiselect("Filter By Year:",
                                options=df1["Year"].unique(),
                                default=df1["Year"].unique())

Category=st.sidebar.multiselect("Filter By Quater:",
                                options=df1["Quater"].unique(),
                                default=df1["Quater"].unique())

Category1=st.sidebar.multiselect("Filter By State:",
                                options=df1["State"].unique())
                                #default=df1["State"].unique())


selection_query=df1.query("Year== @category & Quater== @Category")

selection_query1=df1.query("Year== @category & Quater== @Category & State== @Category1")

Total_Transaction_Amount=(selection_query['Transaction_amount'].sum())

Total_Transaction_count=(selection_query['Transaction_count'].sum())

first_column,second_column=st.columns(2)

with first_column:
    st.markdown("### Total Transaction Amount:")
    st.subheader(f'{Total_Transaction_Amount}')

with second_column:
    st.markdown("### Total Transaction Count:")
    st.subheader(f'{Total_Transaction_count}')

#try:
fig=(selection_query.groupby(by=["State"]).sum()[["Transaction_amount","Transaction_count"]])
#except Exception:
 #   pass

fig=px.bar(fig,
           x="Transaction_amount",
           y=fig.index,
           color=fig.index,
           #orientation='h',
           hover_data=["Transaction_amount","Transaction_count"],
          title="Transaction bar graph by overall years for top districts for states")
fig.update_layout(yaxis=(dict(showgrid=False)),width = 1000, height = 700)

st.plotly_chart(fig)

st.markdown("---")

fig7=(selection_query1.groupby(by=['Top_Dist_Name']).sum()[["Transaction_amount","Transaction_count"]])

fig7=px.bar(fig7,
           y=fig7.index,
           x="Transaction_amount",
           color=fig7.index,
           hover_data=["Transaction_amount","Transaction_count"],
          title="Top districts in a state")
fig7.update_layout(width = 900, height = 500)

st.plotly_chart(fig7)

st.markdown("---")

st.title("User DashBoard for top districts as per year and quater")

df=pd.read_csv("top_user_distname.csv")
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

#st.title("User DashBoard for District as per year and quater")

st.sidebar.header("Filter By Year & Quater for users:")

category1=st.sidebar.multiselect("Filter By Year for users:",
                                options=df["Year"].unique(),
                                default=df["Year"].unique())

Category2=st.sidebar.multiselect("Filter By Quater for users:",
                                options=df["Quater"].unique(),
                                default=df["Quater"].unique())

Category3=st.sidebar.multiselect("Filter By State for users:",
                                options=df["State"].unique())
                                #default=df1["State"].unique())


selection_query3=df.query("Year== @category1 & Quater== @Category2")

selection_query4=df.query("Year== @category1 & Quater== @Category2 & State== @Category3")

Total_Users_count=(selection_query3['Top_Dist_users'].sum())

st.markdown("### Total_Users_count:")
st.subheader(f'{Total_Users_count}')

fig8=(selection_query3.groupby(by=["State"]).sum()[["Top_Dist_users"]])

fig8=px.bar(fig8,
           x="Top_Dist_users",
           y=fig8.index,
           color=fig8.index,
           orientation='h',
           hover_data=["Top_Dist_users"],
          title="User bar graph for top districts")
fig8.update_layout(yaxis=(dict(showgrid=False)),width = 1000, height = 700)

st.plotly_chart(fig8)

st.markdown("---")

fig8=(selection_query4.groupby(by=["Top_Dist_Name"]).sum()[["Top_Dist_users"]])

fig8=px.pie(fig8,
           values="Top_Dist_users",
           names=fig8.index,
           color=fig8.index,
           #orientation='h',
          # hover_data=["Top_Dist_users"],
          title="User pie chart for top Districts in a state")
fig8.update_layout(yaxis=(dict(showgrid=False)),width = 900, height = 500)

st.plotly_chart(fig8)

