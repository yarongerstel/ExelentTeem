import model
import time
import uuid


class UserController:

    @classmethod
    def create_user(cls, user_name: str, content):
        """
        create
        :param user_name:
        :param content: insight
        :return:
        """
        model.UserDetailsWrapper.create(str(uuid.uuid4()), user_name, time.time(), content)

    @classmethod
    def republish(cls, user_id: str, user_name):
        """
        :param user_id: what to republish
        :param user_name: hoe does the republish
        :return:
        """
        model.UserDetailsWrapper.republish(user_id, user_name)
        return "Success"


class Controller:

    @classmethod
    def get_all(cls):
        """
        :return: all db
        """
        return model.UserDetailsWrapper.get_all_users()

    @classmethod
    def get_most_publish(cls):
        """
        :return: the most republish ever
        """
        return model.UserDetailsWrapper.get_the_max_republish()
