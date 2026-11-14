---
title: "ipx_ticks(5)"
name: "ipx_ticks"
section: "5"
letter: "i"
url: "/docs/linux/man/5-ipx_ticks/"
description: "ipx_ticks – Configuration file for ipxd"
---

<p>ipx_ticks &#8211; Configuration file for ipxd</p>
<h2>Synopsis</h2>
<p><code>/etc/ipx_ticks</code> </p>
<h2>Description</h2>
<p>The <code>ipx_ticks</code> file contains the configuration information required by ipxd, the IPX RIP/SAP daemon. The RIP/SAP daemon can find out nearly all information it needs to run properly by scanning the file /proc/net/ipx_interfaces, and by asking other routers and servers on the net. The only information it can not get this way is the time it takes to send a packet over the different interfaces. This information is required by the IPX RIP protocol. It is specified in so-called ticks, which is about 55 ms per tick. The format of this file is very simple. On each line of the file the tick value for a physical interface is specified. The first field is the name of the interface, and the ticks value follows after a white-space. Empty lines as well as lines starting with &#8216;#&#8217; are ignored. A possible example is the following:<br />
#&nbsp;<wbr>Tick values for IPX interfaces<br />
#<br />
#&nbsp;<wbr>device name&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>ticks value<br />
eth0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1<br />
ppp0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>7 The default ticks value for devices not specified in /etc/ipx_ticks is 1. </p>
<h2>Author</h2>
<p>Volker Lendecke &lt;lendecke [at] namu01.gwdg.de&gt;</p>
