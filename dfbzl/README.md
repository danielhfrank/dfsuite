# dfbzl

Typeahead search to select bazel targets to test or build.

Usage: `dfbzl (test|build) [target]`.

When run without a `target` supplied, will pull up `fzf` to do typeahead search among available targets.
When one is selected, _it will copy that to your clipboard_ so that you can use it on subsequent runs.

Requirements:
* Make sure your computer has a glowing apple on the lid
* `brew install fzf`. Feel free to ignore the prompts about installing key bindings

Tips:
* `alias btest="/Users/df/code/dfsuite/dfbzl/dfbzl test $@"` in .bash_whatever

Good luck
