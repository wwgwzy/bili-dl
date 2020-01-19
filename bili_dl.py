import urllib.request
import re

class bili_up_dl():
    
    def __init__(self, upid):
        self.upid = upid
    
    def dump_page_url(self):
        page = 0
        while True:
            page += 1
            page_url = "https://space.bilibili.com/%s/video?tid=0&page=%s&keyword=&order=pubdate"%(self.upid, page)
            yield page_url

    def get_page_av(self, page_url):
        av_pattern = re.compile(r'<li data-aid="(\d+)" class="list-item clearfix fakeDanmu-item">')
        header = {"ccept"  : "application/json, text/plain, */*",
                   "Accept-Encoding" : "gzip, deflate, br",
                   "Accept-Language" : "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7",
                   "Connection" : "keep-alive",
                   "Cookie" : "INTVER=1; _uuid=FC292E50-FE42-E8E0-77A6-349CF8BB3DE007190infoc; buvid3=6FA787A5-69E8-4847-BAF6-CB5F12FE019253944infoc; CURRENT_FNVAL=16; sid=6newiull; LIVE_BUVID=AUTO7515793123629255; DedeUserID=33323750; DedeUserID__ckMd5=4af070d7656738c9; SESSDATA=85ef4717%2C1581991156%2C368d0911; bili_jct=869a5a63be8d791bdaeadd424b6c9828",
                   "Host" : "api.bilibili.com",
                   "Origin" : "https://message.bilibili.com",
                   "Referer" : "https://message.bilibili.com/pages/nav/index_new_pc_sync",
                   "Sec-Fetch-Mode" : "cors",
                   "Sec-Fetch-Site" : "same-site",
                   "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"}
        req = urllib.request.Request(page_url, headers=header)
        with urllib.request.urlopen(req) as f:
            response = f.read()
            print(response)
            # av_id_page = av_pattern.search(response)
            with open("res.html",mode="wb") as hf:
                hf.write(response)
            # return av_id_page

def main():

    upid = "35359510"
    aUpdl = bili_up_dl(upid)
    aUpdl.get_page_av(next(aUpdl.dump_page_url()))

main()