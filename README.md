# Recon tools

## Requirements

- Python 3
- numpy
- scipy
- gensim

## Name match

Match the field names of source and target using

```sh
./match.py file.txt
```

### Example

Source | Target
------------ | -------------
bitcoin | balance
stock | top
cash | cryptocurrency
rating | shares
start | weight
peak | begin

We can match the fields using
```sh
./match.py test/match.txt
```

and obtain
```sh
bitcoin --> cryptocurrency
stock --> shares
cash --> balance
rating --> weight
start --> begin
peak --> top
```
### Example 2

The embedding given by the model (Word2Vec) preserves semantic and syntactic relationships.

```sh
./derive.py high bear low
```
returns
> high is to bear like low is to bull

## Distribution

We can test if two different set of values are from the same population using
```sh
./ttest.py file1.txt file2.txt
```

### Example

The values in test/gauss1.txt and test/gauss2.txt are from a normal distribution with mean 1.0.
The values in test/gauss3.txt re from a normal distribution with mean 1.2.
Each file contains 1000 values.

```sh
./ttest.py test/gauss1.txt test/gauss2.txt
```
returns
> 0.34687060246574086
> Seems fine

```sh
./ttest.py test/gauss1.txt test/gauss3.txt
```
returns
> 0.002737789152809567
> Samples are from different populations
