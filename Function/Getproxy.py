import string
import zipfile
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
    proxy_host, proxy_port = ip_port_str.split(':')
    proxy_user, proxy_pass = user_pass_str.split(':')
    return proxy_host, proxy_port, proxy_user, proxy_pass


def get_driver(proxy):
    proxy_host, proxy_port, proxy_user, proxy_pass = from_proxy_get_daili(proxy)
    proxy_auth_plugin_path = create_proxy_auth_extension(
        proxy_host=proxy_host,
        proxy_port=proxy_port,
        proxy_username=proxy_user,
        proxy_password=proxy_pass)
    option = webdriver.ChromeOptions()
    option.add_extension(proxy_auth_plugin_path)
    driver = webdriver.Chrome(chrome_options=option)
    return driver

