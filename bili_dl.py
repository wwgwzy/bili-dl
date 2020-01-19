import urllib.request
import json
import youtube_dl

class up_dl():
    
    def __init__(self, upid):
        self.upid = upid

    def s_dl_demo():
        pass

    def start(self):
        for avid in self.get_all_avid():
            print(avid)

    def get_all_avid(self):
        for page_json_url in self.dump_page_json_url():
            for avid in self.get_page_avid(page_json_url):
                yield avid

    def dump_page_json_url(self):
        page = 0
        while True:
            page += 1
            page_json_url = "https://api.bilibili.com/x/space/arc/search?mid=%s&ps=30&tid=0&pn=%s&keyword=&order=pubdate&jsonp=jsonp"%(self.upid,
                                                                                                                                       page)
            yield page_json_url

    def get_page_avid(self, page_json_url):
        header = {"ccept"  : "application/json, text/plain, */*",
                  "Accept-Language" : "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7",
                  "Accept-Encoding" : "gzip, deflate, br",
                  "Connection" : "keep-alive",
                  "Cookie" : "INTVER=1; _uuid=FC292E50-FE42-E8E0-77A6-349CF8BB3DE007190infoc; buvid3=6FA787A5-69E8-4847-BAF6-CB5F12FE019253944infoc; CURRENT_FNVAL=16; sid=6newiull; LIVE_BUVID=AUTO7515793123629255; DedeUserID=33323750; DedeUserID__ckMd5=4af070d7656738c9; SESSDATA=85ef4717%2C1581991156%2C368d0911; bili_jct=869a5a63be8d791bdaeadd424b6c9828",
                  "Host" : "api.bilibili.com",
                  "Origin" : "https://message.bilibili.com",
                  "Referer" : "https://message.bilibili.com/pages/nav/index_new_pc_sync",
                  "Sec-Fetch-Mode" : "cors",
                  "Sec-Fetch-Site" : "same-site",
                  "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"}
        req = urllib.request.Request(page_json_url)
        with urllib.request.urlopen(req) as f:
            response = f.read()
            res_dict = json.loads(response)
            return (i["aid"] for i in res_dict["data"]["list"]["vlist"])

def main():

    upid = "35359510"
    aUpdl = up_dl(upid)
    # aUpdl.start()
    up_dl.s_dl_demo()

main()