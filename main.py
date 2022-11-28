from flask import Flask, redirect, url_for, request
import pandas as pd
import numpy as np
import openai
from openai.embeddings_utils import get_embedding, cosine_similarity

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
	if request.method == 'POST':
		return 'Calling the ChairmanAI Python GET route'
	else:
		df = pd.read_csv('wiki_set.csv')
		df["babbage_search"] = df.babbage_search.apply(eval).apply(np.array)
		print(df)
		return 'Calling the ChairmanAI Python POST route'
			
app.run(host='0.0.0.0', port=81)
