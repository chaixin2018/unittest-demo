import string
import zipfile
from time import sleep
from selenium import webdriver


def create_proxy_auth_extension(proxy_host, proxy_port, proxy_username, proxy_password, scheme='http',
                                plugin_path=None):
    if plugin_path is None:
        plugin_path = r'{}_{}@http-dyn.dobel.com_9020.zip'.format(proxy_username, proxy_password)

    manifest_json = """
    {
        "version": "1.0.0",
        "manifest_version": 2,
        "name": "Dobel Proxy",
        "permissions": [
            "proxy",
            "tabs",
            "unlimitedStorage",
            "storage",
            "<all_urls>",
            "webRequest",
            "webRequestBlocking"
        ],
        "background": {
            "scripts": ["background.js"]
        },
        "minimum_chrome_version":"22.0.0"
    }
    """

    background_js = string.Template(
        """
        var config = {
            mode: "fixed_servers",
            rules: {
                singleProxy: {
                    scheme: "${scheme}",
                    host: "${host}",
                    port: parseInt(${port})
                },
                bypassList: ["foobar.com"]
            }
          };

        chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

        function callbackFn(details) {
            return {
                authCredentials: {
                    username: "${username}",
                    password: "${password}"
                }
            };
        }

        chrome.webRequest.onAuthRequired.addListener(
            callbackFn,
            {urls: ["<all_urls>"]},
            ['blocking']
        );
        """
    ).substitute(
        host=proxy_host,
        port=proxy_port,
        username=proxy_username,
        password=proxy_password,
        scheme=scheme,
    )

    with zipfile.ZipFile(plugin_path, 'w') as zp:
        zp.writestr("manifest.json", manifest_json)
        zp.writestr("background.js", background_js)

    return plugin_path


def from_proxy_get_daili(proxy):
    # proxy是这种格式 user:pass@ip:port
    user_pass_str, ip_port_str = proxy.split('@')
    proxyHost, proxyPort = ip_port_str.split(':')
    proxyUser, proxyPass = user_pass_str.split(':')
    return proxyHost, proxyPort, proxyUser, proxyPass


def get_driver(proxy):
    proxyHost, proxyPort, proxyUser, proxyPass = from_proxy_get_daili(proxy)
    proxy_auth_plugin_path = create_proxy_auth_extension(
        proxy_host=proxyHost,
        proxy_port=proxyPort,
        proxy_username=proxyUser,
        proxy_password=proxyPass)
    option = webdriver.ChromeOptions()
    option.add_extension(proxy_auth_plugin_path)
    driver = webdriver.Chrome(chrome_options=option)
    return driver


if __name__ == '__main__':
    # 代理服务器
    proxy = 'test001:123qwe.com@172.16.0.8:808'
    driver = get_driver(proxy)
    driver.get("https://rakuten-sonpo-stg.comitx.co.jp/jimu/front/home")
    print("代理无密码登录成功")
    print(driver.find_element_by_xpath("/html/body/section/section/main/div/div/div[2]/div/div/form/div[1]/label").text)

    driver.quit()