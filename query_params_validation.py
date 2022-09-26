from typing import Union, List

from fastapi import FastAPI, Query
from pydantic import Required

app = FastAPI()


@app.get("/items")
async def read_item(q: Union[str, None] = Query(default=Required, min_length=3, max_length=50)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/items/{item_id}")
async def read_items(q: List[str] = Query(default=["foo", "bar"])):
    query_items = {"q": q}
    return query_items
