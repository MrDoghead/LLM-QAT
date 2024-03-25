# from datasets import load_dataset
import pandas as pd
import json

def parquet2jsonl(parquet_file_path, output_path):
    print(f"Load from {parquet_file_path}")
    data = pd.read_parquet(parquet_file_path)
    with open(output_path, 'w', encoding='utf-8') as f:
        for text in data['text']:
            if text:
                json_line = json.dumps({'text': text})
                f.write(json_line + '\n')
    print(f"Save jsonl at {output_path}")

if __name__ == "__main__":
    file_path = '/data/datasets/wikitext/wikitext-2-raw-v1/validation-00000-of-00001.parquet'
    output_path = '/workspace/LLM-QAT/gen_data/wiki2_val.jsonl'
    parquet2jsonl(file_path, output_path)