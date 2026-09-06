"""简易词频统计（教学版 MapReduce 思路）。

用法（Windows 用 python，macOS/Linux 用 python3）：
    python word_count.py < input.txt
    echo "AI is fun. AI is powerful." | python word_count.py
"""
from collections import Counter
import re
import sys

def tokenize(text: str) -> list[str]:
    return re.findall(r"[A-Za-z']+", text.lower())

def word_count(text: str) -> Counter:
    return Counter(tokenize(text))

if __name__ == "__main__":
    text = sys.stdin.read() if not sys.stdin.isatty() else \
        "AI is fun. AI is powerful. Big data fuels AI."
    for word, count in word_count(text).most_common(5):
        print(f"{word}\t{count}")
