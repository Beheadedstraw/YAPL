# YAPL
Yet Another Programming Language

YAPL was created purely out of boredom and a few beers. I wanted something that was pretty simple and in a coding format most people would recognize (YAML).

Currently it does the basic things, takes input, stores variables, prints static strings and/or variables, the extremely buggy beginnings of a loop and if/else function along with general math equations.

A basic exmaple is like this:
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

What I'm hoping to get done is:
* fix the if/else so it works with things other than integers
* flesh out the loop a bit more
* maybe, possibly, implement some exception handling and actually let the user know where the hell they went wrong.
* Documentation. God I hate writing documentation.

# There's currently zero exception handling right now and little to no error feedback besides Python crash dumps.
![image](https://github.com/Beheadedstraw/YAPL/assets/5951719/64fec37c-4ccc-440a-b1d5-f0f92c416f1d)

