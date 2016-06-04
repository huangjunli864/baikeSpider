# coding:utf8
import urllib2


class HtmlDowaloader(object):

    def download(self, url):
        if url is None:
            return None
        resp = urllib2.urlopen(url, timeout=5)

        if resp.getcode() != 200:
            return None
        # print resp.read()
        return resp.read()