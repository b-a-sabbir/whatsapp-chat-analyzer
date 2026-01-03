import streamlit as st
import preprocessors, helper
import matplotlib.pyplot as plt

st.sidebar.title("Whatsapp Chat Analyzer")

uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    
    data = bytes_data.decode("utf-8")
    
    df = preprocessors.preprocess(data)
    options = df['users'].unique().tolist()
    options.sort()
    options.insert(0, "Overall")
    user_selected = st.sidebar.selectbox("Show Analysis WRT", options)

    if st.sidebar.button("Show Analysis"):
        total_messages, total_words, media_shared, links = helper.get_user_stats(df, user_selected)
        st.title(user_selected + " Statistics")
        

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.subheader("Total Messages", divider=True)
            st.title(total_messages)

        with col2:
            st.subheader("Total Words", divider=True)
            st.title(total_words)
        
        with col3:
            st.subheader("Media Shared", divider=True)
            st.title(media_shared)
        
        with col4:
            st.subheader("Links Shared", divider=True)
            st.title(links)

        # only for group level
        if user_selected == "Overall":
            col1, col2 = st.columns(2)
            x, df_busy = helper.busiest_users(df)
            with col1:
                st.header("Most Busy Users")
                st.bar_chart(x, color='#ffaa00')

            with col2:
                st.header("Percentage of Messages")
                st.dataframe(df_busy)

        # wordcloud
        df = df[df['messages'] != '<Media omitted>\n']
        wc, word_df, emoji_df = helper.wordcloud(df, user_selected)

        # WordCloud
        if wc:
            fig, ax = plt.subplots()
            ax.imshow(wc)
            ax.axis('off')
            st.pyplot(fig)

        col1, col2 = st.columns(2)

        # Word frequency bar chart
        with col1:
            if word_df is not None:
                st.subheader("Most Used Words")
                st.bar_chart(word_df.head().set_index('word'), use_container_width=True, horizontal=True, color="#238d34")

        # Word frequency table
        with col2:
            if word_df is not None:
                st.subheader("Most Used Words")
                st.dataframe(word_df.head())
        
        col1, col2 = st.columns(2)
        # Emoji frequency bar chart
        with col1:
            if emoji_df is not None:
                st.subheader("Most Used Emojis")
                st.bar_chart(emoji_df.head().set_index('emoji'), use_container_width=True, horizontal=True, color='#ffaa00')
        # Emoji frequency table
        with col2:
            if emoji_df is not None:
                st.subheader("Most Used Emojis")
                st.dataframe(emoji_df.head())
