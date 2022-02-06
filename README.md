# Wikipedia-Philosophy - Getting To Philosophy

Getting To Philosophy is a simple python script created to find a path between a given Wikipedia article and the article on [Philosophy](https://en.wikipedia.org/wiki/Philosophy). This is inspired by the Wikipedia article appropriately named [Getting to Philosophy](https://en.wikipedia.org/wiki/Wikipedia:Getting_to_Philosophy) which contains its origins and history.

## Installation
```sh
$ git clone https://github.com/MrJHBauer/Wikipedia-Philosophy.git
```
Getting To Philosophy requires two python modules [requests](http://docs.python-requests.org/en/master/) and [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/)
### Install required modules via pip
```sh
$ pip install requests
$ pip install beautifulsoup4
```


## Usage
Default depature article [/wiki/J/22](https://en.wikipedia.org/J/22) is used if no command line argument is passed. To define your own depature article pass the last part of the url /wiki/article_name as a command line argument.
```sh
$ python3 getting_to_philosophy.py
Visiting: /wiki/Keel
Visiting: /wiki/Fluid_dynamics
Visiting: /wiki/Physics
Visiting: /wiki/Natural_science
Visiting: /wiki/Science
Visiting: /wiki/Knowledge
Visiting: /wiki/Awareness
Visiting: /wiki/Conscious
Visiting: /wiki/Quality_(philosophy)
Visiting: /wiki/Philosophy
```
```sh
$ python3 getting_to_philosophy.py /wiki/Python
Visiting: /wiki/High-level_programming_language
Visiting: /wiki/Computer_science
Visiting: /wiki/Computation
Visiting: /wiki/Calculation
Visiting: /wiki/Arithmetic
Visiting: /wiki/Number
Visiting: /wiki/Mathematical_object
Visiting: /wiki/Abstract_object
Visiting: /wiki/Referent
Visiting: /wiki/Linguistics
Visiting: /wiki/Science
Visiting: /wiki/Knowledge
Visiting: /wiki/Awareness
Visiting: /wiki/Conscious
Visiting: /wiki/Quality_(philosophy)
Visiting: /wiki/Philosophy
```

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D