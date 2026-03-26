import csv
import json
from typing import List, Dict

class FileHandler:

    @staticmethod
    def save_csv(data: List[Dict], filename: str):
        if not data:
            print("No data to save.")
            return
        
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerrows(data)
        print(f"Data saved to {filename}")
    
    @staticmethod
    def save_json(data: List[Dict], filename: str):
        with open(filename,"w", encoding="utf-8") as f:
            json.dump(data if isinstance(data, list) else [data],f, indent=2, ensure_ascii=False)
        print(f"Data saved to {filename}")