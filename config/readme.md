## 数据部分说明
结构分为:
+ config:  config_file.yml
+ utils: config.py
+ utils: file_reader.py

其中，config文件里面只是存放数据，是数据结构的最底层组基础部分，每次需要根据用例修改<br>
utils里的config.py文件是存放上面存储的数据的全局变量名称和相对位置的，如果有文件追加，则需要对应追加<br>
utils里的file_reader.py是存放实现调用的基本方法的，包括两种调用，yml类型和excel类型，这部分一般不需要修改<br>

## 调用的方法
1 生成一个Config类，去实例化，类里面（）里写这个实例化的yml文件<br>
2 数据类型分为两部分，：左侧通过get（左侧内容）获取<br>
3 右侧部分通过[右侧内容]获取<br>
根据存储数据时的结构可以分为三种：<br>
+ user = Config(utils.config.CONFIG_LOGIN).get('user')["admin"]
```
user:
        admin: admin
        日本代行ユーザー1: "700001"
        日本代行ユーザー2: "700002"
        口振振替ユーザー1: "160001"
        口振振替ユーザー2: "160001"
        火災ユーザー: "120001"
        fireRole2: "120002"
        fireRole3: "120003"
        営業点検ユーザー1: "400001"
```
+ select_date = Config(utils.config.CONFIG_DATA).get(self.case_no)
```
"001": "19600000135"
```
+ path = Config(utils.config.CONFIG_DISPLAY_PATH).get(self.branch)[self.node]["証券番号"]
````
fire:
      点検1回目:
            証券番号: "/html/body/section/main/div/section/main/div[1]/div/div[1]/div/div[2]/div/div/form/div[7]/div/div/input"
            検索: "/html/body/section/main/div/section/main/div[1]/div/div[1]/div/div[2]/div/div/form/div[35]/div/button[1]"
            処理: "/html/body/section/main/div/section/main/div[2]/div[5]/div[2]/table/tbody/tr[1]/td[38]/div/button[1]"
            display: "/html/body/section/main/div/section/main/div[2]/div[5]/div[2]/table/tbody/tr[1]/td[38]/div/button[2]"
```