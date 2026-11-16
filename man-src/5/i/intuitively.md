---
title: "intuitively(5)"
name: "intuitively"
section: "5"
letter: "i"
url: "/docs/linux/man/5-intuitively/"
description: "intuitively.conf – Configuration file for intuitively"
---

<p>intuitively.conf &#8211; Configuration file for intuitively</p>
<h2>Synopsis</h2>
<p>intuitively.conf controls how intuitively behaves.</p>
<h3>Example Intuitively.Conf</h3>
<pre>[work]
myip = 192.168.1.253
netmask = 255.255.255.0
other_ip = 192.168.1.1 #router
other_ip = 192.168.1.2 = aa:bb:cc:dd:ee:ff #general server w/ethernet address
default_gw = 192.168.1.1
description = Work
#script = /usr/share/intuitively/work.sh
[home]
myip = 192.168.199.6
netmask = 255.255.255.0
other_ip = 192.168.199.2
other_ip = 192.168.199.3
other_ip = 192.168.199.4
other_mac = bb:cc:dd:ee:00:aa # sets which mac 192.168.199.4 must have
 # in order to match this location
default_gw = 192.168.199.4
description = Home
#script = /usr/share/intuitively/home.sh</pre>
<dl>
<dt><code>myip</code></dt>
<dd>The ip address you want for this interface, either on the form a.b.c.d, or with netmask, like a.b.c.d/e, where e represents how many bits you want masked off or on the form fff.ggg.hhh.iii, which allows for strange stuff like having 255.255.243.0 as your netmask (not recommended).</dd>
<dt><code>netmask</code></dt>
<dd>if the netmask isn&#8217;t set in myip, it must be set here. Allowed forms are single digit, specifying how many bits are to be masked off, or a full ip address whose bits will be masked off.</dd>
<dt><code>other_ip</code></dt>
<dd>The ip address of one of the peers you are looking for. Good choices include such things as file servers, NIS servers, routers and other equipment which you are sure that is always up. Note that it needs to be on the same LAN, since ARP requests are normally not routed. It may also include the MAC address of the machine, quite useful if you have multiple networks with overlapping IP addresses</dd>
<dt><code>othermac</code></dt>
<dd>The mac address of the previous other_ip. See otherip for more information.</dd>
<dt><code>defaultlocation</code></dt>
<dd>If this flag is set, this location is used as default location. That means if none of the descriped location is found, this location is used. other location matches, this is used. If several locations are marked with the flag defaultlocation, the first one defined in the configuration is chosen.</dd>
<dt><code>dontsetip</code></dt>
<dd>If this flag is set, and this location is detected, no interface configuration is done. You still have to provide myip, but it may be any ip in the subnet, even an ip already in use.</dd></dl>
<h2>Files</h2>
<p><i>/etc/intuitively/intuitively.conf</i></p>
