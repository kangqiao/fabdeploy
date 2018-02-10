# Auto deploy tripitaka projects
--
自动化部署项目.

### How to use
##### 列出可用任务
`fab -l`
##### 指定配置文件
`fab config:'./config.ini'`
or
`fab config:path='./config.ini'`
##### 初始化服务器环境
`fab init:'./config.ini'`
or
`fab config:'./config.ini' init`
##### 安装需要软件包
`fab setup:'./config.ini'`
##### 部署项目
`fab deploy:'./config.ini'`
##### 一键部署项目到服务器上
`fab one_step:'./config.ini'`

### 配置项说明
##### 项目名称
`project=tripitaka`
##### 项目代码仓
```
repository=https://github.com/CoinLQ/fabdeploy.git
default_branch = 'deploy'
```
##### 服务器ssh连接
```
login_user=root
target_ips=['192.168.1.1']
stage=product
```
##### Nginx域名
```
nginx_server_name = 'api.lqdzj.cn'
nginx_webpage_name = 'www.lqdzj.cn'
```
