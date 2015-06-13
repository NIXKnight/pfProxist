#!/usr/bin/env python
# -*- coding: utf-8 -*-

# +--------------------------------------------------------------------------------------------------------------+
# + pfProxist is a bit of a rewrite and extension of proxist.py @ https://github.com/OffensivePython/Proxist.git +
# + which is GPL license code.                                                                                   +
# +--------------------------------------------------------------------------------------------------------------+

from ProxistCoreFunctions import *

if __name__ == '__main__':

  MAINURL = urllib2.urlopen(str(URL)).read()
  COUNT = PagesCount(MAINURL)

  for PAGE_NUM in range(1,COUNT+1):
    PAGE = ProxistGetPage(PAGE_NUM)
    ENTRIES = ExtractEntries(PAGE)
    for ENTRY in ENTRIES:
      NONES = ['display:none'] + re.findall(IP_INFO_PATTERN['none'], ENTRY)
      ENTRY = ENTRY.replace('<span></span>', '')
      IP = GetIP(ENTRY, NONES)
      print IP
