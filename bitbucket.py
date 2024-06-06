# # Shallow clone repos from bitbucket.
# # Usage:
#    # python3 bitbucket.py -u [USERNAME] -p [BITbucket_APP_TOKEN] -o [OUTPUT_DIR] -i [INPUT_FILE]
# # 1. Setup app password in Bitbucket
# # Tutorial: https://support.atlassian.com/bitbucket-cloud/docs/app-passwords/
# # Goto: https://bitbucket.org/account/settings/app-passwords/

from requests.auth import HTTPBasicAuth
import os
import requests

        
def login(user, pwd):
    roles = 'owner member contributor admin'.split()
    for role in roles:
        print(f'Checking role {role}')
        url = f'https://api.bitbucket.org/2.0/repositories?pagelen=100&role={role}'
        rs = requests.get(url, auth=HTTPBasicAuth(user, pwd)).json()
        print(rs)
        if 'values' not in rs:
            print(f'Role {role} is invalid')
            continue
        else:
            print(f'Role {role} is valid')
            return True
    return False

def load_repos(input):
    debug = os.environ.get('DEBUG', 'False')
    if debug.lower() in ('true', '1'):
        debug = True
    else:
        debug = False
    if debug:
        urls = [
            "https://bitbucket.org/michalbel/saxs-mlv.git",
            'https://bitbucket.org/kmccall_appacademy/3d8e2e08-william.lemus-data-structure-exercises.git',
            'https://bitbucket.org/ammppp/edb_examples.git',
            'https://bitbucket.org/lerzinski1969l9/albert1969besides.git',
            'https://bitbucket.org/isysd/dotfiles-lele85.git'
        ]
        return urls
    with open(input, 'r') as f:
        urls = f.readlines()
    return urls

def download_repo(urls, output):
    for url in urls:
        # Bitbucket的源代码ZIP文件的URL格式是
        # https://bitbucket.org/{owner}/{repo}/get/{branch}.zip
        # 我们假设你想要下载master分支的源代码
        url = url.strip()
        zip_url = url.replace('.git', '/get/master.zip')

        try:
            # r = requests.get(zip_url, allow_redirects=True)
            r = requests.get(zip_url, allow_redirects=True, verify=False, timeout=60)

            output = "./bitbucket/"
            if os.path.exists(output) is False:
                os.makedirs(output)
            # 我们使用URL的最后一部分（不包括.git）作为文件名
            filename = url.split('/')[-1].replace('.git', '.zip')

            with open(output + filename, 'wb') as f:
                f.write(r.content)

            # 存储一个下载结果方便二次检索
            with open(output + 'res.txt', 'a') as f:
                f.write(f"{url}, {zip_url}, {r}, {output + filename}\n")
                print(f"{url}, {zip_url}, {r}, {output + filename}")

        except requests.exceptions.RequestException as e:
            print(f'An error occurred: {e}')
            status = 600

            # 存储一个下载结果方便二次检索
            with open(output + 'res.txt', 'a') as f:
                f.write(f"{url}, {zip_url}, {status}\n")
                print(f"{url}, {zip_url}, {status}")

def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("-u", "--user", help="Bitbucket username", type=str, required=True)
    ap.add_argument("-p", "--password", help="Bitbucket app password", type=str, required=True)
    ap.add_argument("-i", "--input", help="Bitbucket urls file path", type=str, default='./clone_urls')
    ap.add_argument("-o", "--output", help="Output directory", type=str, default='./bitbucket')
    args = vars(ap.parse_args())

    user = args['user']
    pwd = args['password']
    input = args['input']
    output = args['output']

    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    login_flag = False
    while not login_flag:
        login_flag = login(user, pwd)

    urls = load_repos(input)

    download_repo(urls, output)


if __name__ == "__main__":
    main()
