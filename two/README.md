Palendrome Checker
==================

A [palendrome](https://en.wikipedia.org/wiki/Palindrome) is a string which says the same thing if you read it backwards.
Sometimes, non-letter characters are added to point out that it forms a sentance.
For example:

#### How to Draw a Pyramid
```
A Zig. Now one zag. Gaze now on Giza!

azignowonezaggazenowongiza
<----- same backwards ----
------ as forwards------->
```

#### How to Complete this Challenge

[runme.py](runme.py) has a long list of strings.
Only one is not a palendrome, and your job is to find it.
If you run that script as-is, you'll see:

```
❯ python3 runme.py
453 strings found that were not palendromes
most recently: Zeus was deified, saw Suez.
```

But that's not true, `zeuswasdeifiedsawsuez` is a palendrome.  Complete the TODO on line 465:
```
def is_a_palendrome(string):

    # TODO: make this function return True if the string is a palendrome
    return False
```

The challenge is complete when [runem.py](runme.py) produces output like below (except it will tell you which one was the non-palendrome).
```
❯ python3 two/runme.py
1 strings found that were not palendromes
most recently: __________
```

Once you're done, create a pull request against this repo that includes your changes.

