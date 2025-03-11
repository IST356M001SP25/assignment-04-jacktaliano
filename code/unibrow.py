'''
Solution unibrow.py
'''
import pandas as pd
import streamlit as st
import pandaslib as pl

def main():
    st.title("UniBrow")
    st.caption("The Universal data browser")
    
    uploaded_file = st.file_uploader("Upload a file:", type=["csv", "xlsx", "json"])
    
    if uploaded_file is not None:
        file_extension = pl.get_file_extension(uploaded_file.name)    # Load the file into a DataFrame based on its extension
        data_frame = pl.load_file(uploaded_file, file_extension)
        all_columns = pl.get_column_names(data_frame)             # Get all column names from the DataFrame
        display_columns = st.multiselect("Select columns to display", options=all_columns, default=all_columns)
        
        if st.toggle("Filter data"):   # allows user to filter the data
            col1, col2, col3 = st.columns(3)
            text_columns = pl.get_columns_of_type(data_frame, 'object') # Get columns with text data
            filter_by = col1.selectbox("Select column to filter", options=text_columns) # allows users to filter the column
            if filter_by:        # iIf value is from the selected filter column
                unique_values = pl.get_unique_values(data_frame, filter_by)
                selected_value = col2.selectbox("Select value to filter on", options=unique_values)
                filtered_data = data_frame[data_frame[filter_by] == selected_value][display_columns]
            else:
                filtered_data = data_frame[display_columns]
        else:
            filtered_data = data_frame[display_columns]
        
        # display the resulting DataFrame and its summary statistics
        st.dataframe(filtered_data)
        st.dataframe(filtered_data.describe())

if __name__ == '__main__':
    main()