# Auto deploy tripitaka projects
自动化部署项目.

### How to use
##### 列出可用任务
`fab -l`
##### 指定配置文件
`fab config:'./config.ini'`
or
`fab config:path=./config.ini`
##### 初始化服务器环境
`fab config:./config.ini init`
##### 安装需要软件包
`fab config:./config.ini setup`
##### 部署项目
`fab config:./config.ini deploy`
##### 一键部署项目到服务器上
`fab config:./config.ini one_step`

### 配置项说明
##### 服务器ssh连接
```
login_user=root
target_ips=['192.168.1.1']
stage=product
```
##### 项目名称
`project=TripitakaPlatform`
##### 项目代码仓
```
repository=https://github.com/CoinLQ/TripitakaPlatform.git
default_branch = master
```
##### 配置Web项目
```
webapp_name = Z_PUB
webapp_repository = https://github.com/CoinLQ/Z_PUB.git
webapp_branch = master
```
##### Nginx域名
```
nginx_server_name = 'api.lqdzj.cn'
nginx_webpage_name = 'www.lqdzj.cn'
```
##### 配置数据库
```
#保持与django项目的settings配置一致.
db_name = tripitaka_platform
db_user = lqzj
db_password = xxxxxx
```
##### 配置amazon的SQS队列.
```
aws_access_key = please_change_it
aws_secret_key = please_change_it
email_pw = please_change_it
```

