# bitbucket_crawl_mnbvc

## Introduction

This script is used to crawl source code from bitbucket repos.

## Dataset

try download **clone_url** from [bitbucket_download_mnbvc](https://github.com/L1aoXingyu/bitbucket_download_mnbvc/releases/tag/v0.1).

## Usage

```
python3 bitbucket.py -u [USERNAME] -p [BITbucket_APP_TOKEN] -o [OUTPUT_DIR] -i [INPUT_FILE]
```

* [USERNAME]: your bitbucket username.
* [BITbucket_APP_TOKEN]: bitbucket app password, setuped in [app-password](https://bitbucket.org/account/settings/app-passwords/) adn you can follow the [tutorial](https://support.atlassian.com/bitbucket-cloud/docs/app-passwords/).
* [OUTPUT_DIR]: default value is `./bitbucket`, which is used to store source code compressed packages `xxx.zip` and running logs `res.txt`.
* [INPUT_FILE]: default value is `clone_url`, which is a list of bitbucket repos.

## Comment
You can contact me via email [knediny@gmail.com](mailto:knediny@gmail.com).


