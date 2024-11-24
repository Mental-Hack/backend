import os
import pandas as pd
import json
import torch
from flask import Flask, request, jsonify
from kafka import KafkaProducer, KafkaConsumer
from sqlalchemy import create_engine
from nbconvert.preprocessors import ExecutePreprocessor
import nbformat

app = Flask(__name__)

# Paths to assets
NOTEBOOK_PATH = "cow_analysis.ipynb"
BREEDING_MODEL_PATH = "breeding_model.pth"
COWS_MODEL_PATH = "cows_model.ipynb"

# Step 1: Load Breeding Model
def load_breeding_model(model_path):
    """
    Loads the breeding model (PyTorch).
    """
    try:
        model = torch.load(model_path)
        model.eval()
        return model
    except Exception as e:
        raise ValueError(f"Error loading breeding model: {e}")

# Step 2: Predict Breeding Matches
def predict_matches(model, data):
    """
    Uses the breeding model to predict the best match for cows.
    """
    try:
        # Assuming the model takes specific input features
        input_features = data[["feature1", "feature2", "feature3"]].values  # Update with actual features
        input_tensor = torch.tensor(input_features, dtype=torch.float32)
        predictions = model(input_tensor).detach().numpy()
        data["match_score"] = predictions
        return data
    except Exception as e:
        raise ValueError(f"Error in predicting matches: {e}")

# Step 3: Postprocess Data (Cows Model)
def postprocess_data(data):
    """
    Postprocesses the data using external logic from `cows_model`.
    """
    try:
        # Dynamically execute the external cows_model logic
        # Assuming cows_model.py has a `postprocess` function
        import cows_model
        processed_data = cows_model.postprocess(data)
        return processed_data
    except Exception as e:
        raise ValueError(f"Error in postprocessing data: {e}")

# Step 4: Clean Data
def clean_data(file_path):
    """
    Cleans the merged cow data.
    - Removes duplicates
    - Fills NaN values with column mean
    """
    try:
        data = pd.read_csv(file_path)
        data = data.drop_duplicates()
        for column in data.select_dtypes(include=["float64", "int64"]).columns:
            data[column].fillna(data[column].mean(), inplace=True)
        return data
    except Exception as e:
        raise ValueError(f"Error while cleaning data: {e}")

# Step 5: Save Data
def save_data(data, excel_path, sql_connection_string):
    """
    Saves cleaned data to an Excel file and SQL database.
    """
    data.to_csv(excel_path, index=False)
    print(f"Data saved to {excel_path}")
    engine = create_engine(sql_connection_string)
    table_name = "cow_data"
    data.to_sql(table_name, engine, if_exists="replace", index=False)
    print(f"Data saved to SQL table: {table_name}")

# Step 6: Execute Notebook
def execute_notebook(notebook_path, cell_range=None):
    """
    Executes a Jupyter Notebook or a specific range of cells and captures the output.
    """
    try:
        with open(notebook_path) as f:
            notebook = nbformat.read(f, as_version=4)
        if cell_range:
            notebook["cells"] = [notebook["cells"][i] for i in cell_range]
        ep = ExecutePreprocessor(timeout=600, kernel_name="python3")
        ep.preprocess(notebook, {"metadata": {"path": os.path.dirname(notebook_path)}})
        outputs = []
        for cell in notebook["cells"]:
            if cell.cell_type == "code" and "outputs" in cell:
                outputs.append(cell.outputs)
        return outputs
    except Exception as e:
        return {"error": str(e)}

# Step 7: Kafka Producer
def send_to_kafka(data, topic, kafka_server):
    """
    Sends processed data to Kafka topic as JSON messages.
    """
    producer = KafkaProducer(
        bootstrap_servers=[kafka_server],
        value_serializer=lambda v: json.dumps(v).encode("utf-8")
    )
    for _, row in data.iterrows():
        producer.send(topic, row.to_dict())
    producer.flush()
    print(f"Data sent to Kafka topic: {topic}")

# Flask Endpoints
@app.route("/process", methods=["POST"])
def process_data_request():
    """
    Endpoint to process cow data.
    """
    try:
        # Parse request
        data = request.json
        input_file = data.get("file_path", "merged_cow_df.csv")
        excel_output = data.get("excel_output", "processed_cow_data.csv")
        sql_connection = data.get("sql_connection", "sqlite:///cow_data.db")
        kafka_topic = data.get("kafka_topic", "cow_data_topic")
        kafka_server = data.get("kafka_server", "localhost:9092")

        # Step 1: Clean data
        cleaned_data = clean_data(input_file)

        # Step 2: Execute notebook
        notebook_output = execute_notebook(NOTEBOOK_PATH)

        # Step 3: Load breeding model and predict matches
        breeding_model = load_breeding_model(BREEDING_MODEL_PATH)
        matched_data = predict_matches(breeding_model, cleaned_data)

        # Step 4: Postprocess data
        final_data = postprocess_data(matched_data)

        # Step 5: Save data
        save_data(final_data, excel_output, sql_connection)

        # Step 6: Send to Kafka
        send_to_kafka(final_data, kafka_topic, kafka_server)

        return jsonify({"status": "success", "notebook_output": notebook_output})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
