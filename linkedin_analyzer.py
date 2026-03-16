from textblob import TextBlob
from wordcloud import WordCloud
import matplotlib.pyplot as plt
comments = ["This is such an insightful post on AI trends!",
           "Can you explain how the library works?",
           "Python is truly the best language for data.",
           ]
def analyze_vibe(data):
    print("--- Sentiment Analysis ---")
    for text in data:
        analysis = TextBlob(text)
        vibe = "Positive" if analysis.sentiment.polarity > 0 else "Neutral/Questioning"
        print(f"Comment: {text[:30]}... | Vibe: {vibe}")
def generate_cloud(data):
    text_combined = " ".join(data)
    cloud = WordCloud(width=800, height=400, background_color='white').generate(text_combined)
    plt.figure(figsize=(10, 5))
    plt.imshow(cloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()
analyze_vibe(comments)
generate_cloud(comments)
