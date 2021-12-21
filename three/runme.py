from dataclasses import dataclass
from datetime import time


@dataclass
class User:
    first_name: str
    utc_offset: int


# fmt: off
data = {
 # user_id : user details
         1 : User("Ernest",    -7),     # MT
         2 : User("Isaul",     -5),     # ET
         3 : User("Himabindu", -8),     # PT
         4 : User("Matt",      -8),     # PT
         5 : User("Jyotsana",  +5.5),   # IST
         6 : User("Trevor",    -7),     # MT
         7 : User("Kelechi",   +1),     # WAT
         8 : User("Vidhi",     +5.5),   # IST
}
# fmt: on

working_hours = (9, 17)  # 9 AM - 5 PM, user's local time


def get_working_user_ids(query_time, from_offset=0, working_hours=working_hours):

    # TODO: instead of returning all of the user_id's
    # only return the ones whose working hours include the query_time
    return data.keys()


def announce(description, working_users):

    print(f"At {description}, these users might be working:")
    for user_id in working_users:
        print("    ", data[user_id].first_name)
    print("")


def test_one():

    # noon, MT
    working_users = get_working_user_ids(
        time(hour=12, minute=0, second=0), from_offset=-7
    )

    announce("At 12:00 PM, mountain time", working_users)
    expected = [1, 2, 3, 4, 6]
    assert set(working_users) == set(expected)


def test_two():

    # noon, IST
    working_users = get_working_user_ids(
        time(hour=14, minute=0, second=0), from_offset=+5.5
    )

    announce("At 2:00 PM, India time", working_users)
    expected = [5, 7, 8]
    assert set(working_users) == set(expected)


if __name__ == "__main__":
    test_one()
    test_two()
