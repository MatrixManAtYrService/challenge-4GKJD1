Gibberish Converter
===================

The first two functions in [runme.py](runme.py) [serialize](https://en.wikipedia.org/wiki/Serialization) python objects to strings.

- `to_gibberish()`
    - takes a python object like `{"foo": {"bar": "bar"}}`
    - returns a string like `eyJmb28iOiB7ImJhciI6ICJiYXIifX0K`
- `from_gibberish()`
    - takes a string like `eyJmb28iOiB7ImJhciI6ICJiYXIifX0K`
    - returns a python object like `{"foo": {"bar": "bar"}}`


The rest of the functions in that file test these two functions to make sure they work.  If you run them as-is, you'll see something like this:
```
❯ python3 one/runme.py
TEST in PASSED: {'wakka': {'bang': 'splat'}} -> eyJ3YWtrYSI6IHsiYmFuZyI6ICJzcGxhdCJ9fQ==
TEST out PASSED: eyJmb28iOiB7ImJhciI6ICJiYXIifX0K -> {'foo': {'bar': 'bar'}}
TEST both PASSED: [1, 2, 3, 4, 5] -> WzEsIDIsIDMsIDQsIDVd -> [1, 2, 3, 4, 5]
TEST bad_input FAILED, should have raised an exception
TEST bad_gibberish FAILED, should have raised an exception
```

There are two TODO's.  One on line 85:
```
    # TODO: come up with test input that causes a bad_input exception
    bad_input = "this input isn't bad enough"
```

And one on line 104:
```
    # TODO: come up with test input that causes a bad_gibberish exception
    bad_gibberish = "eyJmb28iOiB7ImJhciI6ICJiYXIifX0K"
```

Examine `to_gibberish()` and `from_gibberish()`.  Come up with test datal that makes all tests pass.
You'll know the challenge is complete when you can run it and get output like below, except instead of `__________`, you'll see your data.
```
❯ python3 one/runme.py
TEST in PASSED: {'wakka': {'bang': 'splat'}} -> eyJ3YWtrYSI6IHsiYmFuZyI6ICJzcGxhdCJ9fQ==
TEST out PASSED: eyJmb28iOiB7ImJhciI6ICJiYXIifX0K -> {'foo': {'bar': 'bar'}}
TEST both PASSED: [1, 2, 3, 4, 5] -> WzEsIDIsIDMsIDQsIDVd -> [1, 2, 3, 4, 5]
TEST bad_input PASSED: __________ is invalid
TEST bad_gibberish PASSED: __________ is invalid
```

When you're done, create a pull request against this repo with your changes.

