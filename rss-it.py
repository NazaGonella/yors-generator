import subprocess
import json
from pathlib import Path

with open("metadata.json", "r", encoding="utf-8") as f:
    metadata = json.load(f)

posts_path = metadata["posts_path"]

markdown_files = [md for md in Path(posts_path).rglob("*.md")]

print("\n### Converting to RSS ###")

md_string : list[str] = []

for md in markdown_files:
    md_string.append(str(md))
    print(md)

print("")

with open("feed.xml", "w", encoding="utf-8") as f:
    subprocess.run([
        "pandoc-rss", "-s",
        "-t", "Blog Title",
        "-d", "Descriptiong of the feed",
        "-l", "https://yourblog.something/",
        "-w", "yourmail@somemail.com (Your Name)",
        *md_string
    ],
    stdout=f, check=True)
