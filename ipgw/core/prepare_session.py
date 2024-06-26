# GET /cgi-bin/rad_user_info?callback=jQuery1124017875094059174257_1635846793608&_=1635846793609 HTTP/1.1
# Host: ipgw.neu.edu.cn
# User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0
# Accept: text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01
# Accept-Language: zh-CN,en-US;q=0.8,en;q=0.5,ja;q=0.3
# Accept-Encoding: gzip, deflate
# X-Requested-With: XMLHttpRequest
# Connection: keep-alive
# Referer: http://ipgw.neu.edu.cn/srun_portal_pc?ac_id=1&theme=pro
# Cookie: lang=zh-CN
# Pragma: no-cache
# Cache-Control: no-cache
from requests import Session


def prepare_session() -> Session:
    sess = Session()
    sess.headers.update({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0",
        "Accept": "application/json",
        "Accept-Language": "zh-CN",
        "Accept-Encoding": "gzip, deflate",
        "X-Requested-With": "XMLHttpRequest",
        "Connection": "keep-alive"
    })
    return sess
