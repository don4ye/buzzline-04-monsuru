import json
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from kafka import KafkaConsumer
from collections import defaultdict, deque
import datetime
import os

# Kafka configuration
KAFKA_TOPIC = "project_json"
KAFKA_BOOTSTRAP_SERVERS = "localhost:9092"

# Create Kafka Consumer
try:
    consumer = KafkaConsumer(
        KAFKA_TOPIC,
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        value_deserializer=lambda x: json.loads(x.decode("utf-8"))
    )
    print(f"Connected to Kafka topic: {KAFKA_TOPIC}")
except Exception as e:
    print(f"Failed to connect to Kafka: {e}")
    consumer = None

# Data storage
time_window = deque(maxlen=50)  # Store timestamps
sentiment_scores = deque(maxlen=50)  # Store sentiment scores
category_sentiments = defaultdict(list)  # Store sentiment scores by category

# Setup the plots
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 12))

# Line chart for sentiment over time
line, = ax1.plot([], [], 'b-', label="Sentiment Score")
ax1.set_ylim(0, 1)  # Sentiment scores range from 0 to 1
ax1.set_xlim(0, 50)  # Keep the last 50 messages
ax1.set_xlabel("Time (Last 50 Messages)")
ax1.set_ylabel("Sentiment Score")
ax1.set_title("Live Sentiment Analysis (Line Chart)")
ax1.legend()

# Bar chart for average sentiment by category
bar_categories = []  # Categories for the x-axis
bar_heights = []  # Heights for the bars
ax2.set_ylim(0, 1)  # Sentiment scores range from 0 to 1
ax2.set_title("Average Sentiment by Category (Bar Chart)")
ax2.set_ylabel("Average Sentiment")

# Histogram for sentiment distribution
ax3.set_xlim(0, 1)  # Sentiment scores range from 0 to 1
ax3.set_title("Sentiment Distribution (Histogram)")
ax3.set_xlabel("Sentiment Score")
ax3.set_ylabel("Frequency")

def update_chart(frame):
    """
    Update all three charts dynamically with new data.
    """
    if not consumer:
        print("No Kafka consumer available. Exiting...")
        return
    
    try:
        # Fetch the next Kafka message
        message = next(consumer)
        data = message.value
        print(f"Received message: {data}")

        # Extract timestamp, sentiment, and category
        timestamp = datetime.datetime.strptime(data["timestamp"], "%Y-%m-%d %H:%M:%S")
        sentiment = data["sentiment"]
        category = data["category"]

        # Append to line chart data
        time_window.append(timestamp)
        sentiment_scores.append(sentiment)

        # Update category sentiments
        category_sentiments[category].append(sentiment)

        # Calculate average sentiment by category
        avg_sentiments = {cat: sum(vals) / len(vals) for cat, vals in category_sentiments.items()}

        # Update line chart
        line.set_xdata(range(len(sentiment_scores)))
        line.set_ydata(sentiment_scores)
        ax1.set_xlim(max(0, len(sentiment_scores) - 50), len(sentiment_scores))

        # Update bar chart
        ax2.clear()
        ax2.bar(avg_sentiments.keys(), avg_sentiments.values(), color='orange')
        ax2.set_ylim(0, 1)
        ax2.set_title("Average Sentiment by Category (Bar Chart)")
        ax2.set_ylabel("Average Sentiment")
        ax2.set_xlabel("Category")

        # Update histogram
        ax3.clear()
        ax3.hist(sentiment_scores, bins=10, range=(0, 1), color='green', alpha=0.7, edgecolor='black')
        ax3.set_xlim(0, 1)
        ax3.set_title("Sentiment Distribution (Histogram)")
        ax3.set_xlabel("Sentiment Score")
        ax3.set_ylabel("Frequency")

        print(f"Updated averages: {avg_sentiments}")
    except StopIteration:
        print("No more messages to process.")
    except Exception as e:
        print(f"Error during update: {e}")

# Start the animation with the warning fix
try:
    ani = animation.FuncAnimation(fig, update_chart, interval=1000, cache_frame_data=False)
    plt.tight_layout()
    plt.show()
except Exception as e:
    print(f"Error starting animation: {e}")
