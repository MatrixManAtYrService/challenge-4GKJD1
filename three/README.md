Who is Awake?
=============

Our team lives in several different countries.
Sometimes you have to do time-zone math to know who is likely to be awake.

[runme.py](runme.py) has an incomplete function on line 31, `get_working_user_ids()`.
It claims to do that time-zone math.
Currently, running it produces output like this:
```
❯ python3 three/runme.py
At At 12:00 PM, mountain time, these users might be working:
     Ernest
     Isaul
     Himabindu
     Matt
     Jyotsana
     Trevor
     Kelechi
     Vidhi

Traceback (most recent call last):
  File "three/runme.py", line 76, in <module>
    test_one()
  File "three/runme.py", line 60, in test_one
    assert set(working_users) == set(expected)
AssertionError
```

That's because at 12:00 PM mountain time, it's 12:30 AM for Jyotsana--which is not during normal working hours.
The problem is pointed out with a TODO:
```
def get_working_user_ids(query_time, from_offset=0, working_hours=working_hours):

    # TODO: instead of returning all of the user_id's
    # only return the ones whose working hours include the query_time
    return data.keys()
```

Fix it so that it returns the right set of users.
When this challenge is complete, [runme.py](runme.py) will produce output like this:

```
❯ python3 three/runme.py
At At 12:00 PM, mountain time, these users might be working:
     Ernest
     Isaul
     Himabindu
     Matt
     Trevor

At At 2:00 PM, India time, these users might be working:
     Jyotsana
     Kelechi
     Vidhi
```

When you're done, create a pull request against this repo that includes your changes.

