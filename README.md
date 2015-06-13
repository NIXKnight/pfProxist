**pfProxist**
==================
pfProxist is a Python tool that extracts a list of IP address of IP:PORT proxies available at [HideMyAss free IP:PORT proxies lists page][3] that can later be used for blocking in firewalls such as pfSense.

**Dependencies**
------------
The tool requires a standard Python installation for now. It uses Puthon's **`re`** and **`urllib2`** libraries.

**Usage**
-----

Use the script as follows:

    python pfProxist.py
    

**Planned Features**
------------

 - Database backend to save the list.
 - Proxy port verification.

**Credits**
-------

[OffensivePython][1] - Author of the original **`proxist.py`** at [GitHub][4]

[Saad Ali][2] - Linux/BSD Admin

**License**
-------

 - The script continues GPLv3 license from the original author.

  [1]: http://www.pythonforpentesting.com/2014/12/updated-proxist-bot-hidemyass-proxy.html
  [2]: https://github.com/nixknight
  [3]: http://proxylist.hidemyass.com/
  [4]: https://github.com/OffensivePython/Proxist
