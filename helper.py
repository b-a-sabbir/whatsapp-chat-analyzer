from urlextract import URLExtract
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from banglish_stopwords import BanglishStopwords
from collections import Counter
import re
from nltk.corpus import stopwords
import nltk
import pandas as pd


def get_user_stats(df, user):
    total_messages = 0
    word_total = 0
    if user != "Overall":
        df = df[df['users'] == user]
    
    # 1. Total Messages
    total_messages = df.shape[0]

    # 2. Total Words
    for u_msg in df['messages'].str.split():
        word_total += len(u_msg)
    
    # 3. Media Shared
    media_shared = df[df['messages'] == '<Media omitted>\n'].shape[0]

    # 4. Links shared
    links = 0
    for msg in df['messages']:
        extractor = URLExtract()
        urls = extractor.find_urls(msg)
        links += len(urls)

    return total_messages, word_total, media_shared, links


def busiest_users(df):
    x = df['users'].value_counts().head()
    df_busy = round((df['users'].value_counts() / df.shape[0]) * 100, 2).reset_index().rename(columns={'index': 'name', 'users': 'percent'})
    return x, df_busy




def wordcloud(df, user):
    if user != 'Overall':
        df = df[df['users'] == user]

    df = df.dropna(subset=['messages'])

    if df.empty:
        return None, None, None

    bsw = BanglishStopwords()
    nltk.download('stopwords', quiet=True)

    # emoji pattern
    emoji_pattern = re.compile(
        "[" 
        "\U0001F600-\U0001F64F"
        "\U0001F300-\U0001F5FF"
        "\U0001F680-\U0001F6FF"
        "\U0001F1E0-\U0001F1FF"
        "\U00002700-\U000027BF"
        "\U000024C2-\U0001F251"
        "]",
        flags=re.UNICODE
    )

    stop_words = set(stopwords.words('english'))

    cleaned_words = []
    emojis = []

    for msg in df['messages']:
        # Banglish stopwords remove
        msg = bsw.remove_stopwords(msg)

        # emoji collect
        emojis.extend(emoji_pattern.findall(msg))

        # emoji remove
        msg = emoji_pattern.sub('', msg)

        for word in msg.split():
            word = word.lower()
            word = re.sub(r'[^a-z]', '', word)

            if word and word not in stop_words:
                cleaned_words.append(word)

    if not cleaned_words:
        return None, None, None

    # --------------------
    # WORD FREQUENCY
    # --------------------
    word_freq = Counter(cleaned_words)
    word_df = (
        pd.DataFrame(word_freq.items(), columns=['word', 'count'])
        .sort_values(by='count', ascending=False)
        .reset_index(drop=True)
    )


    # --------------------
    # EMOJI FREQUENCY
    # --------------------
    emoji_freq = Counter(emojis)
    emoji_df = (
        pd.DataFrame(emoji_freq.items(), columns=['emoji', 'count'])
        .sort_values(by='count', ascending=False)
        .reset_index(drop=True)
    )


    # --------------------
    # WORDCLOUD
    # --------------------
    wc = WordCloud(
        width=500,
        height=500,
        background_color='white',
        min_font_size=10
    )

    wc = wc.generate_from_frequencies(word_freq)

    return wc, word_df, emoji_df


