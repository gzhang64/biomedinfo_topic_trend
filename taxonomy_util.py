import torch
from transformers import AutoTokenizer, AutoModel
from sklearn.cluster import KMeans
import numpy as np
import json

def cluster_keywords_with_bert(model_name, keywords, num_clusters, output_path="clustering_results.json"):
    # Load tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModel.from_pretrained(model_name)

    # Function to embed each keyword
    def embed_text(text):
        inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
        with torch.no_grad():
            outputs = model(**inputs)
        cls_embedding = outputs.last_hidden_state[:, 0, :].squeeze().numpy()
        return cls_embedding

    # Embed all keywords
    embeddings = np.array([embed_text(kw) for kw in keywords])

    # Perform KMeans clustering
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    kmeans.fit(embeddings)

    # Prepare results
    results = [
        {"keyword": keyword, "cluster": int(kmeans.labels_[i])}
        for i, keyword in enumerate(keywords)
    ]

    # Save to JSON
    with open(output_path, "w") as f:
        json.dump(results, f, indent=2)

