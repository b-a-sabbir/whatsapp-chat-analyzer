import re
import pandas as pd
import numpy as np

def preprocess(data):
    pattern = r"\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s\bam|\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s\bpm\b\s-\s"
    
    msg = re.split(pattern, data)
    msg = msg[1:]

    dates = re.findall(pattern, data)
    df = pd.DataFrame({'user_message':msg, 'message_date': dates})
    df['message_date'] = (
        df['message_date']
        .str.replace(r'\s*-\s*$', '', regex=True)
    )

    df['message_date'] = pd.to_datetime(
        df['message_date'],
        format='%m/%d/%y, %I:%M %p'
    )

    df.rename(columns={'message_date':'date'}, inplace=True)

    users = []
    messages = []

    for message in df['user_message']:
        entry = re.split(r"([\w\W]+?):\s", message)
        if entry[1:]:
            users.append(entry[1])
            messages.append(entry[2])
        else:
            users.append('group notifications')
            messages.append(entry[0])
    df['users'] = users
    df['messages'] = messages
    df.drop(columns='user_message', inplace=True)

    df['year'] = df['date'].dt.year

    df['month'] = df['date'].dt.month_name()

    df['day'] = df['date'].dt.day

    df['hour'] = df['date'].dt.hour

    df['minute'] = df['date'].dt.minute
    df['users'] = df['users'].apply(lambda x: re.sub(r'^[^A-Za-z+]*([A-Za-z].*|\+880.*)', r'\1', x, flags=re.MULTILINE))
    df = df[df['users'] != 'group notifications']
    return df 

