from typing import List

from openrecall.config import db_path
import chromadb

client = chromadb.PersistentClient(path=db_path)
collection = client.get_or_create_collection(name="recollection")

def get_timestamps() -> List[int]:
    count = collection.count()
    batch_size = 16
    timestamps = []
    for i in range(0, count, batch_size):
        batch = collection.get(
            include=[],
            limit=batch_size,
            offset = i,
        )

        for ids in batch['ids']:
            timestamps.append(int(ids))
    return timestamps

def insert_entry(
    text: str, timestamp: int, app: str, title: str
) -> None:
    collection.add(
        documents=text,
        ids=[str(timestamp)],
        metadatas={'app': app, 'title': title}
    )
