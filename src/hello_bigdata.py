"""课程示例：Hello 大数据。

运行（在仓库根目录下）：
    Windows:  python src/hello_bigdata.py
    macOS/Linux: python3 src/hello_bigdata.py
"""

def main() -> None:
    techs = ["Spark", "Hadoop", "Flink", "Kafka", "Beam"]
    print("=== 大数据与人工智能：开篇 ===")
    for i, name in enumerate(techs, 1):
        print(f"{i}. {name}")
    print("Welcome to the course!")

if __name__ == "__main__":
    main()
