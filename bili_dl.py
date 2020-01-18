import urllib

class bili_up_dl():
    
    def __init__(self, upid):
        self.upid = upid
    
    def dump_page_url(self, upid):
        for page in range(1, 51):
            page_url = "https://space.bilibili.com/%s/video?tid=0&page=%s&keyword=&order=pubdate"%(upid, page)
            

def main():

    upid = "35359510"
    aUpdl = bili_up_dl(upid)
    aUpdl.

main()