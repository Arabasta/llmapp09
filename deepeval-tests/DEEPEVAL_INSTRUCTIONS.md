# DeepEval evaluations

These tests call the four live backend endpoints and use OpenAI as the judge
for schema compliance, correctness, relevance, conciseness, and faithfulness.

```sh
python -m pip install -r requirements.txt
export OPENAI_API_KEY="your-key"
deepeval test run test_classify.py -v
deepeval test run test_sentiment.py -v
deepeval test run test_summarize.py -v
deepeval test run test_intent.py -v
```

The backend must be available at `http://localhost:8080` before collection,
because each test module builds cases from live API responses.
