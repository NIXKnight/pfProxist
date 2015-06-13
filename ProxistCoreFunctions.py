#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import urllib2

VERSION = 0.1
URL = 'http://proxylist.hidemyass.com/'
HEADERS = {'User-Agent':'ModProxist %s'%VERSION,'Accept':'application/json','Connection':'keep-alive','X-Requested-With':'XMLHttpRequest'}
REQUEST_PATTERN = {'entry':r'<tr class=".+?" rel="\d+?">(.+?)</tr>','pages':r'<a href="/\d+?">(\d+?)</a>'}
IP_INFO_PATTERN = {'ip':r'</style>(.+?)</span></td>','port':r'<td>(\d+?)</td>','country':r'"country":"(.+?)"','none':r'\.(\S+?){display:none}','tags':r'<(\w+?) (\w+?)="(.+?)">(.+?)</(\w+?)>','info':r'({"id":.+?})'}

# This fuction gets proxy list page and removes Python escape characters from it
def ProxistGetPage(PAGE_NUM):
  PAGE = urllib2.urlopen(str(URL) + str(PAGE_NUM) + '#listable').read()
  PAGE = PAGE = PAGE.replace(r'\"', '"')
  PAGE = PAGE.replace(r'\/', '/')
  PAGE = PAGE.replace(r'\n', '')
  return PAGE

# This function counts the total number of pages on http://proxylist.hidemyass.com/
def PagesCount(UNESCAPED_PAGE):
  PAGES = re.findall(REQUEST_PATTERN['pages'], UNESCAPED_PAGE)
  return int(PAGES[-1])


def ExtractEntries(PAGE):
  ENTRIES = re.findall(REQUEST_PATTERN['entry'], PAGE, re.DOTALL)
  return ENTRIES

def StripNONES(IP, TAG):
  STRIP_PATTERN = r'<{} {}="{}">{}</{}>'.format(TAG[0], TAG[1], TAG[2], TAG[3], TAG[4])
  return IP.replace(STRIP_PATTERN, '')

def StripTrash(IP, TAG):
  STRIP_PATTERN = r'<{} {}="{}">'.format(TAG[0], TAG[1], TAG[2])
  return IP.replace(STRIP_PATTERN, '')

# This function gets IP address by parsing the page and striping NONES
def GetIP(ENTRY, NONES):
  IP = re.search(IP_INFO_PATTERN['ip'], ENTRY, re.DOTALL).group(1)
  TAGS = re.findall(IP_INFO_PATTERN['tags'], IP)
  for TAG in TAGS:
    if TAG[2] in NONES:
      IP = StripNONES(IP, TAG)
    else:
      IP = StripTrash(IP, TAG)
  IP = IP.replace('</span>', '')
  return IP
