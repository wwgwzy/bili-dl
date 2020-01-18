import urllib

class bili_up_dl():
    
    def __init__(self, upid):
        self.upid = upid
    
    def dump_page_url(self):
        for page in range(1, 51):
            page_url = "https://space.bilibili.com/%s/video?tid=0&page=%s&keyword=&order=pubdate"%(self.upid, page)
            yield page_url

def main():

    upid = "35359510"
    aUpdl = bili_up_dl(upid)
    print(next(aUpdl.dump_page_url()))


main()