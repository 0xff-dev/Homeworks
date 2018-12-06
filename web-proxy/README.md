
### 正常直接请求的报头
```bash
GET / HTTP/1.1
Accept: */*
Accept-Language: zh-cn
UA-CPU: x86
Accept-Encoding: gzip, deflate
User-Agent: Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)
Host: www.baidu.com
Connection: Keep-Alive
```

### 使用代理的连接方法
```
先连接代理服务器（IP地址、端口）,然后向代理服务器提交这样的HTTP头
GET http://www.baidu.com/ HTTP/1.0
Accept: */*
Accept-Language: zh-cn
UA-CPU: x86
Accept-Encoding: gzip, deflate
User-Agent: Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)
Host: www.baidu.com
Proxy-Connection: Keep-Alive
```
