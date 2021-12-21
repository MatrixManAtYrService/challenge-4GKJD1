#!/usr/bin/env python3
# -*- coding: utf-8
import json
import base64

from enum import Enum, auto


# Code Under Test
#################


class Fail(Enum):
    bad_input = auto()
    bad_gibberish = auto()


def to_gibberish(obj):
    try:
        json_str = json.dumps(obj)
        b64_str = base64.b64encode(json_str.encode()).decode("utf-8")
        return b64_str
    except Exception as err:
        raise Exception(Fail.bad_input)


def from_gibberish(gibberish):
    try:
        json_str = base64.b64decode(gibberish)
        obj = json.loads(json_str)
        return obj
    except Exception as err:
        raise Exception(Fail.bad_gibberish)


# Tests
#######


def test_out():
    """
    Given valid gibberish, do we find the correct object?
    """

    g = "eyJmb28iOiB7ImJhciI6ICJiYXIifX0K"
    out_obj = from_gibberish(g)
    if out_obj == {"foo": {"bar": "bar"}}:
        print("TEST out PASSED:", g, "->", out_obj)
    else:
        print("TEST out FAILED")


def test_in():
    """
    Given a valid object, do we find the correct gibberish?
    """

    in_obj = {"wakka": {"bang": "splat"}}
    g = to_gibberish(in_obj)
    if g == "eyJ3YWtrYSI6IHsiYmFuZyI6ICJzcGxhdCJ9fQ==":
        print("TEST in PASSED:", in_obj, "->", g)
    else:
        print("TEST in FAILED")


def test_both():
    """
    Given an object, does it survive the transistion to gibberish and back?
    """

    in_obj = [1, 2, 3, 4, 5]
    g = to_gibberish(in_obj)
    out_obj = from_gibberish(g)
    if in_obj == out_obj:
        print("TEST both PASSED:", in_obj, "->", g, "->", out_obj)
    else:
        print("TEST both FAILED")


def test_bad_input():
    """
    Given input that can't be converted to gibberish, do we raise the right error?
    """

    # TODO: come up with test input that causes a bad_input excetion
    bad_input = "this input isn't bad enough"

    try:
        to_gibberish(bad_input)
    except Exception as err:
        if err.args[0] == Fail.bad_input:
            print("TEST bad_input PASSED:", bad_input, "is invalid")
        else:
            print("TEST bad_input FAILED, raised the wrong exception")
    else:
        print("TEST bad_input FAILED, should have raised an exception")


def test_bad_gibberish():
    """
    Given gibberishj that can't be converted to an object, do we raise the right error?
    """

    # TODO: come up with test input that causes a bad_gibberish excetion
    bad_gibberish = "eyJmb28iOiB7ImJhciI6ICJiYXIifX0K"

    try:
        from_gibberish(bad_gibberish)
    except Exception as err:
        if err.args[0] == Fail.bad_gibberish:
            print("TEST bad_gibberish PASSED:", bad_gibberish, "is invalid")
        else:
            print("TEST bad_gibberish FAILED, raised the wrong exception")
    else:
        print("TEST bad_gibberish FAILED, should have raised an exception")


if __name__ == "__main__":
    test_in()
    test_out()
    test_both()
    test_bad_input()
    test_bad_gibberish()
