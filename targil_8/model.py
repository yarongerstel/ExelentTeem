from tinydb import TinyDB, Query, table
import time
from dataclasses import dataclass
from tinydb.operations import increment

DB_PATH = r'C:\Users\USER001\PycharmProjects\ExelentTeem\targil_8\DB.json'
users_table = TinyDB(DB_PATH)


@dataclass
class UserDetails:
    id: str
    user_name: str
    due_date: time
    insight: str
    count: int = 1


class UserDetailsWrapper:

    @classmethod
    def get_by_id(cls, user_id: str) -> UserDetails:
        """

        :param user_id: we looking for
        :return: the UserDetails or null
        """
        return users_table.search(Query().id.matches(user_id))

    @classmethod
    def create(cls, user_id: str, name: str, date: time.time(), insight: str):
        """
        create new user whit new insight
        :param user_id:
        :param name:
        :param date:
        :param insight:
        :return:
        """
        users_table.insert({"id": user_id, "user_name": name, "due_date": date, "insight": insight, "count": 1})

    @classmethod
    def get_all_users(cls):
        return users_table.all()

    @classmethod
    def republish(cls, user_id: str, user_name: str):
        """
        update the table whit the new republish
        :param user_id: what to republish
        :param user_name: how did that
        """
        if UserDetailsWrapper.get_by_id(user_id):
            users_table.update(increment('count'), Query().id.matches(user_id))
            users_table.upsert({'due_date': time.time(), 'user_name': user_name}, Query().id.matches(user_id))
        else:
            raise Exception('User dont exists')

    @classmethod
    def get_the_max_republish(cls):
        """
        check the max count number
        :return:
        """
        all_user = users_table.all()
        max_id = ""
        max_count = 0
        for i in all_user:  # check the max count number
            if i["count"] > max_count:
                max_count = i["count"]
                max_id = i['id']
        return UserDetailsWrapper.get_by_id(max_id)
