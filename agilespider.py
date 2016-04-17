import urllib

class AgileSpider(object):
    def __init__(self):
        print "init the spider "


    @classmethod
    def testStub(cls):
        print "hello aigle spider "

    @staticmethod
    def getWebPage(url):
        wp = urllib.urlopen(url)
        content = wp.read()
        return content