from crawler import Crawler



if __name__=="__main__":
    dom = ("arkas.com", "bimar.com")
    sub = ("my", "box", "mail")
    c = Crawler(dom, sub)
    c.get_domain_info_with_curl()