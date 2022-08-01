
![Logo](https://raw.githubusercontent.com/zandora-space/zanx/main/zanx.png)


# Emscraper

An module which helps to scrape emails from Google Search and mail it to the given email address after email validation for getting deleverable email ids.


## Badges

![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)

![Python](https://img.shields.io/badge/python-v3.7-blue?)

![PyPi](https://img.shields.io/badge/pypi-v0.0.3-blue?)

## Features

- You can build your own free email list.
- You can get valid emails from Google.
- We validate each emails before sending the list to your mail.
- Easy to use & free.

## Installation

Install my-project with pip

```bash
  pip install emscraper
```
    
## Dependency
Emscraper requires following programs to run properly :

- requests
- BeautifulSoup
- smtplib

Install selenium using pip command :

```bash
pip install requests
```

```bash
pip install BeautifulSoup
```

```bash
pip install secure-smtplib
```
## Usage/Examples

```python
from emscraper import scrape

scrape('Your_Audience_Niche', 'Your Email ID')
```


## Roadmap

- Add more feactures.
- Get HTML Page on Mail.


## Authors

- [@zandora-space](https://www.github.com/zandora-space)


## Support

For support, email professor@zandora.space or follow our Instagram Page [@zanx.coders](https://instagram.com/zanx.coders)


## Feedback/Issues

If you have any feedback, please reach out to us at professor@zandora.space

If you have facing any issues, please report via [Report Issues](https://github.com/zandora-space/emscraper/issues)



## License

[MIT](https://github.com/zandora-space/emscraper/blob/main/LICENSE)