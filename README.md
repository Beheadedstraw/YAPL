# YAPL
Yet Another ~~Programming~~ sKrPtYnG Language

YAPL was created purely out of boredom and a few beers. I wanted something that was pretty simple and in a coding format most people would recognize (YAML).

A basic example is like this:
```yaml
START:
  - [PRINT, ["PRINTING TOTAL"]]
  - [ADD, [2,2], total_add]
  - [PRINT, [$total_add," this is the total"]]
  - [OPEN, "test.txt", test]
  - [PRINT, [$test]]
  - [CALC, 2+4*2, total_sub]
  - [PRINT, [$total_sub]]
  - [INPUT, total_sub]
  - [IF, $total_sub, LT, 20, PRINT, "It's less than 20"]
  - [LOOP, $test, [
        [PRINT, [line]],
        [ADD, [2,5], total_add2],
        [PRINT, [$total_add2]]
    ]]
```

Then we'd run it with `python main.py main.yaml`. 

Currently YAPL is under heavily drunken development. Some of the Python dev's out there might scream at this code, be shocked, have a stroke, or maybe get a good chuckle. That's OK, because YAPL wasn't written to:

* Be performant like C/Rust/Go/C++ or god forbid Java.
* Have all the fancy bells and whistles like pointers, classes, or mutable/non-mutable variables (at least not yet)
* Static/Private functions/variables? Lol, look elsewhere my friend.

It's a pretty bare basic language. The basics of the basics.
![image](https://github.com/Beheadedstraw/YAPL/assets/5951719/4ea36513-d4b3-4d00-ba1f-6ec72ffdf8f9)


Anyways, if you wanna learn how this dog shit language works, check out the barely updated docs [here](https://github.com/Beheadedstraw/YAPL/wiki).

# There's currently zero exception handling right now and little to no error feedback besides Python crash dumps.
![image](https://github.com/Beheadedstraw/YAPL/assets/5951719/64fec37c-4ccc-440a-b1d5-f0f92c416f1d)

