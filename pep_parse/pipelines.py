import csv
from collections import defaultdict
from datetime import datetime as dt

from .settings import BASE_DIR

RESULT_DIR = BASE_DIR / "results"
RESULT_FILE = "status_summary_{time}.csv"


class PepParsePipeline:
    def __init__(self):
        self.results_dir = RESULT_DIR
        self.results_dir.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.counter = defaultdict(int)

    def process_item(self, item, spider):
        self.total = len(item['status'])
        self.counter[item["status"]] += 1
        return item

    def close_spider(self, spider):
        file_path = self.results_dir / RESULT_FILE.format(
            time=dt.now().strftime("%Y-%m-%d_%H-%M-%S")
        )
        with open(file_path, mode="w", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile, dialect="unix")
            writer.writerows(
                [
                    ["Статус", "Количество"],
                    *(self.counter.items()),
                    ["Total", sum(self.counter.values())],
                ]
            )
