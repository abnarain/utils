import re
import mechanize
from mechanize import Browser
from HTMLParser import HTMLParser
class MyHTMLParser(HTMLParser):
    doc=[]
    def handle_starttag(self, tag, attrs):
        for attr in attrs:
            self.doc.append(list(attr))
    def handle_endtag(self, tag):
        self.doc.append(list(tag))
    def handle_data(self, data):
        self.doc.append(list(data))
    def handle_comment(self, data):
        self.doc.append(list(data))



if __name__=='__main__':

    ll= ["www.facebook.com","www.gatech.edu", "www.porn.com"]
    browser = Browser()
    browser.open("https://www.trustedsource.org/en/feedback/url?action=checksingle")   
    # fill the select check form
    try:
        browser.select_form(name="single_check_form")
    except:
        print "catching error "
    browser.form["product"] =["12-ts-3"]  
    browser.form["url"]="www.gatech.edu"
    response = browser.submit()     
    #print response.read()
    print "================"
    # headers
    #forms_resp = mechanize.ParseResponse(response, backwards_compat=False)
    #print forms_resp["result"]
    parser = MyHTMLParser()
    s = parser.feed(response.read())
    print "ss"
    page = parser.doc
    print page[921]

    response.close()
