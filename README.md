# floatrange

[![Build Status](https://travis-ci.com/DESY-P02-1/floatrange.svg?branch=master)](https://travis-ci.com/DESY-P02-1/floatrange)

floatrange implements a safe range for floating point numbers

It is a port of the Julia frange function from the following issue comment:
https://github.com/JuliaLang/julia/issues/2333#issuecomment-33830575

The Julia test suite for floating point ranges is ported as well:
https://github.com/JuliaLang/julia/blob/master/test/ranges.jl#L537


## Usage

For example

```
>>> from floatrange import frange
>>> frange(0.1, 0.3, 0.1)
array([ 0.1,  0.2])
```


## Installation

floatrange requires

* python >= 2.7

Download the latest release and extract it. Run

```
$ cd floatrange
$ pip3 install .
```


## Contribution

Please feel free to open issues or pull requests.


## Acknowledgement

All credit goes to Stefan Karpinski and the other Julia developers
