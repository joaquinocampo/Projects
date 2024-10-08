import streamlit as st
import pandas as pd

first_name = st.sidebar.text_input("Enter your first name:").strip()
last_name = st.sidebar.text_input("Enter your last name:").strip()


def tower_sidebar(first_name, last_name):
    df = pd.read_excel("skyscrapers.xlsx")
    sidebar_empty = True

    if first_name != "" and last_name != "":
        sidebar_empty = False

    if sidebar_empty:
        st.sidebar.write("Please input information above and press enter once done.")


def map_function():
    df = pd.read_excel("skyscrapers.xlsx")
    df = df.rename(columns={"Lat": "lat", "Lon": "lon"})
    map_check = st.expander("Click this expander to view map of skyscrapers")
    with map_check:
        st.write("### Map of All Skyscraper Locations")
        map_data = pd.DataFrame(df)
        st.map(map_data)


def skyscraper_function():
    skyscraper_check = st.expander("Click this expander to see data visualization")
    with skyscraper_check:
        df = pd.read_excel("skyscrapers.xlsx")
        st.write("### Frequency Count of Skyscrapers in Each Country")
        n_by_country = df.groupby("Country")["Name"].count()
        st.bar_chart(n_by_country)

        st.write("### Mean value for height of a skyscraper in each country by feet")
        ft_skyscraper = df.groupby("Country")["Feet"].mean()

        ft_skyscraper


def filter_function():
    tower_count = 1

    filter_check = st.expander("Click this expander to filter out skyscraper data")
    with filter_check:
        df = pd.read_excel("skyscrapers.xlsx")

        userCountry = st.selectbox("Filter out tower(s) by selecting a country:", df.iloc[:, 6].drop_duplicates().sort_values())
        f"You selected {userCountry}."

        size_slider = st.slider("Choose size of tower in feet:", 1140, 2700, 1140)
        f"You selected {size_slider:,} feet."

        dfCountry = df[df["Country"] == userCountry]
        dfSizeAndCountry = dfCountry[dfCountry["Feet"] > size_slider]

        f"Displaying tower(s) with size greater than {size_slider:,} feet..."

        dfSizeAndCountry

        for i in dfSizeAndCountry.itertuples():
            if pd.isna(i[9]):
                st.write(
                    f"{tower_count}. The skyscraper {i[1]} is {i[2]:,} metres or {(i[3]):,} feet in size, year {i[4]}. \nIts type is {i[5]} and its main uses are: {i[6]}. \nIt is located in {i[8]}, {i[7]}. No remarks.")
                tower_count += 1
            else:
                st.write(
                    f"{tower_count}. The skyscraper {i[1]} is {i[2]:,} metres or {(i[3]):,} feet in size, year {i[4]}. \nIts type is {i[5]} and its main uses are: {i[6]}. \nIt is located in {i[8]}, {i[7]}. Remarks: {i[9]}")
                tower_count += 1


def main():
    tower_sidebar(first_name, last_name)

    if first_name != "" and last_name != "":
        st.sidebar.write(f"Welcome, {first_name} {last_name}.")
        st.sidebar.write("To minimize this sidebar, click the 'x' in the top right. \n\nThank you for using this app!")

        st.title("Skyscraper Data 🏗️")
        st.write("#### Web App by Joaquin Ocampo")
        st.write("")
        st.write(f"Hello, {first_name} {last_name}. \n\n To sort values in a table, click the desired column.")
        st.write(f"Each expander, if clicked, will display: a map, visualization of data, and a filter, referring to the skyscraper chart.")
        st.write("#### Table by Name, Metres, Feet, Year, Type, Main Use, Country, City, Remarks, and Coordinates")

        df = pd.read_excel("skyscrapers.xlsx")
        df = df.rename(columns={"Lat": "lat", "Lon": "lon"})

        st.write(df)
        
        st.write("#### Table Sorted by Year in Ascending Order")
        st.write(df.sort_values(by=["Year"], ascending=True))

        map_function()
        skyscraper_function()
        filter_function()


main()

# Streamlit Reference: https://docs.streamlit.io/en/stable/api.html


