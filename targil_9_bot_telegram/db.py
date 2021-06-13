from dataclasses import dataclass
from tinydb import TinyDB, Query, table
from tinydb.operations import increment

DB_PATH = 'number-amount-db.json'
db = TinyDB(DB_PATH)
amount_number = db.table('numbers')


@dataclass
class NumberTime:
    number: str
    count: int


class NumberModelWrapper:

    @classmethod
    def get_number(cls, num: str):
        return amount_number.search(Query().number.matches(num))

    @classmethod
    def create(cls, num: str):
        if cls.get_number(num):
            amount_number.update(increment('count'), Query().number.matches(num))
        else:
            amount_number.insert({"number": num, "count": 1})

    @classmethod
    def get_max_number_count(cls):
        """
        check the max count number
        :return:
        """
        all_number = amount_number.all()
        max_count = 0
        current_number = ""
        for i in all_number:  # check the max count number
            if i["count"] > max_count:
                max_count = i["count"]
                current_number = i["number"]
        return current_number
