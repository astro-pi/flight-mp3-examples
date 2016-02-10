# Flight MP3 Examples

ESA have informed us that, due to the operational constraints surrounding approved file types, we are not permitted to upload new Raspbian or Pip packages to the ISS to support the new coding challenges.

This means that, for the MP3 player challenge, entrants must not submit code that depends on non default packages installed via `apt-get` or `pip`. Because we cannot upload them to the ISS the packages cannot be installed on the Astro Pis on board and therefore your code would just crash with the following error:

`ImportError: No module named X`

So what can you use? There are numerous modules built into Python that are known as the *Standard Library*, commonly used modules like `time`, `os`, `math` and `threading` are all part of this. So those modules, and many others, can be used without issue.





## Python 2.7

[Standard Library modules](https://docs.python.org/2.7/py-modindex.html)

Module | Version
---|---


## Python 3.2

[Standard Library modules](https://docs.python.org/3.2/py-modindex.html)

Module | Version
---|---

