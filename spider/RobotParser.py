from urllib.parse import urljoin, urlparse
import urllib.robotparser
import requests
import time

class RobotParser():
    def __init__(self, useragent='RobotParser', ttl=3600):
        self.useragent=useragent
        self.parsers={}
        self.ttl=ttl
    def read(self, url):
        url=urljoin(url, '/')
        roboturl=urljoin(url, '/robots.txt')
        rp=urllib.robotparser.RobotFileParser()
        rp.modified()
        r=requests.get(roboturl, headers={'User-Agent':self.useragent})
        if r.ok:
            rp.parse(r.text.splitlines())
        elif r.status_code==404:
            rp.allow_all=True
            print('404 for', roboturl)
        else:
            raise Exception('Status code %s for url %s unrecognised'
                            % (r.status_code, roboturl))
        self.parsers[urlparse(url).netloc]=rp
        self.parsers[urlparse(r.url).netloc]=rp
    def can_fetch(self, url):
        host=urlparse(url).netloc
        for i in list(self.parsers):
            if (self.parsers[i].mtime()+self.ttl)<time.time():
                print('Removing robots.txt for %s due to cache expiration...' % i)
                del self.parsers[i]
        if host not in self.parsers:
            print('Fetching robots.txt...')
            self.read(url)
        now=self.parsers[host]
        #Check both to stay on the safe side
        return now.can_fetch('*', url) and now.can_fetch(self.useragent, url)
