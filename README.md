Sudoku Solver
============

This is a naive attempt at a Sudoku Solver in Python. It takes input as 9 lines of digits 0-9 then iterates over all cells, trying to find potential values for a given cell. When it establishes that a cell can only have one possible value, it sets that value to that cell and carries on.

I've done no research on efficient algorithms for doing this, and wrote this in about 2 hours one evening, mainly to play with a bit of Python (which I haven't touched in some time), and because I've always wanted to write a Sudoku solver.

At present, it doesn't work - I seem to have some sort of catastrophic bug in my logic where the results aren't being updated from the original input. Oops.

## Usage

```
git clone https://github.com/adamsp/sudoku-solver.git
cd sudoku-solver
python sudokusolver.py
097080600
000000700
008012530
001540298
900307006
642098300
039670800
004000000
006030940

```

## License

    Copyright 2014 Adam Speakman

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.