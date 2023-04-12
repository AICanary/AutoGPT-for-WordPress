from duckduckgo_images_api import search
results = search("nike")

print([r["image"] for r in results["results"]])