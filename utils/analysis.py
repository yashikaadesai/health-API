from textblob import TextBlob
import numpy as np

def analyze_sentiment(message):
    sentiments = [TextBlob(msg).sentiment.polarity for msg in messages]
    avg_sentiment = np.mean(sentiments)

    if avg_sentiment<-0.2:
        return " Ngeative"
    elif avg_sentiment<0.2:
        return "Neutral"
    else:
        return "positive"
    
def analyze_velocity(time_logs):
    if len(time_logs<3):
        return "Low"
    return "Normal"

def analyze_completion(task_progress):
    avg=sum(t['percent complete'] for t in task_progress)/len(task_progress)
    if avg<50:
        return "Behind"
    return "On track"

    