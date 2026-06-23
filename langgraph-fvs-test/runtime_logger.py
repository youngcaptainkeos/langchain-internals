import json
from datetime import datetime

def log_edge(src, dst):
    with open("runtime_edges.jsonl", "a") as f:
        f.write(
            json.dumps({
                "source": src,
                "target": dst,
                "timestamp": datetime.utcnow().isoformat()
            }) + "\n"
        )