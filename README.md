# buzzline-04-monsuru

We can analyze and visualize different types of streaming data as the information arrives.

This project uses Kafka for real-time data streaming and Matplotlib for dynamic visualization. It generates live charts to illustrate key insights from streaming data.

This project consists of the following features:
1. A producer that streams JSON messages to a Kafka topic (`project_json`).
2. A consumer that:
   - Processes the messages in real time.
   - Generates three live visualizations:
     - Line Chart: Tracks sentiment scores over time.
     - Bar Chart: Displays average sentiment by category.
     - Histogram: Shows the distribution of sentiment scores.

##  Tools and Setup
Before starting, ensure the following tools are installed:
- Python 3.11 or later
- Kafka and Zookeeper
- Python libraries (`matplotlib`, `kafka-python`,.)

### Prerequisites
1. Clone the repository to your local machine.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
 
    

##  Manage Local Project Virtual Environment

1. Create your .venv
2. Activate .venv


## Start Zookeeper and Kafka (2 Terminals)

### Start Zookeeper Service
```bash
bin/zookeeper-server-start.sh config/zookeeper.properties

### Start Kafka Service
bin/kafka-server-start.sh config/server.properties

## Start the Producer and Consumer Applications

This will require two terminals:

- One to run the producer.
- Another to run the consumer.

### Step 1: Start the Producer
The producer generates JSON messages and sends them to the Kafka topic (`project_json`).

#### Command to Run:

**Windows:**
```bash
.venv\Scripts\activate
python -m producers.project_producer_case


Mac/Linux:
```source .venv/bin/activate
python3 -m producers.project_producer_case

```

### Consumer Terminal

Start the associated consumer that will process and visualize the messages. 

In VS Code, open a NEW terminal in your root project folder. 
Use the commands below to activate .venv, and start the consumer. 

Windows:
```bash 
.venv\Scripts\activate
python -m consumers.project_consumer_monsuru

```bash

Mac/Linux:
```source .venv/bin/activate
python3 -m consumers.project_consumer_monsuru
```


## Save Space
To save disk space, you can delete the .venv folder when not actively working on this project.
You can always recreate it, activate it, and reinstall the necessary packages later. 
Managing Python virtual environments is a valuable skill. 

## License
This project is licensed under the MIT License as an example project. 
You are encouraged to fork, copy, explore, and modify the code as you like. 
See the [LICENSE](LICENSE.txt) file for more.



