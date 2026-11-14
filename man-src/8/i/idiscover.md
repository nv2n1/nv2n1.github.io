---
title: "idiscover(8)"
name: "idiscover"
section: "8"
letter: "i"
url: "/docs/linux/man/8-idiscover/"
description: "ipmiutil_discover – discover IPMI LAN-enabled nodes"
---

<p>ipmiutil_discover &#8211; discover IPMI LAN-enabled nodes</p>
<h2>Synopsis</h2>
<p><code>idiscover [-abegisx]</code> </p>
<h2>Description</h2>
<p><i>idiscover</i> is a program that uses IPMI LAN commands to discover any nodes on the LAN that are available, by probing the RMCP port (623.) on those nodes. This utility uses IPMI LAN, so no IPMI drivers are needed. There are three methods that can be used:<br />
 -a = broadcast RMCP ping method (default)<br />
 -g = GetChannelAuthCap command method<br />
 else = specific RMCP ping method A beginning IP address can be specified with -b for broadcast and specific methods. An ending IP can be specified for non-broadcast methods. </p>
<h2>Options</h2>
<p>Command line options are described below.</p>
<dl>
<dt>-a</p>
<dd>All nodes, use the broadcast ping method. This is the default if no options are specified. This will detect the first enabled ethernet interface, and defaults to the broadcast address x.x.x.255 (where x.x.x.x is IP address) unless -b is used to specify otherwise.</p>
<dt>-b &lt;ip&gt;</p>
<dd>Beginning IP address, required, unless using broadcast with defaults. This could be a specific IP address, or a broadcast address, ending in 255, if the broadcast method (-a) is used.</p>
<dt>-e &lt;ip&gt;</p>
<dd>Endign IP address of the range. Not used for broadcast method. If this is not specified, a range of one IP address matching the beginning IP is assumed.</p>
<dt>-g</p>
<dd>Use the GetChannelAuthenticationCapabilities command method over IPMI LAN instead of the RMCP ping. Not compatible with broadcast. This may be useful if the vendor BMC does not support RMCP ping for some reason.</p>
<dt>-i eth0</p>
<dd>The interface name to use when sending the probes. The default is to detect the first enabled ethernet interface (e.g. eth0).</p>
<dt>-m</p>
<dd>shows MAC address. Uses the broadcast ping method, but uses a raw socket so that the MAC address can be displayed. This detects the first enabled ethernet interface, and defaults to the broadcast address 255.255.255.255 like -a. Using -m with raw sockets requires root privilege.</p>
<dt>-r N</p>
<dd>Repeat the ping N times to each node. Default is to send 1 ping per node.</p>
<dt>-x</p>
<dd>Causes extra debug messages to be displayed. </p>
</dl>
<h2>Examples</h2>
<p>&nbsp;<wbr>idiscover -a -b 192.168.1.255<br />
 Sends a broadcast RMCP ping to discover IPMI LAN nodes on the specified subnet.<br />
&nbsp;<wbr>idiscover -b 192.168.1.100 -e 192.168.1.254<br />
 Sends RMCP pings to a range of IP addresses.<br />
&nbsp;<wbr>idiscover -g -b 192.168.1.100 -e 192.168.1.254<br />
 Sends GetChannelAuthCap commands to a range of IP addresses. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-ipmiutil/">ipmiutil</a>(8) <a href="/docs/linux/man/8-ialarms/">ialarms</a>(8) <a href="/docs/linux/man/8-iconfig/">iconfig</a>(8) <a href="/docs/linux/man/8-icmd/">icmd</a>(8) <a href="/docs/linux/man/8-ievents/">ievents</a>(8) <a href="/docs/linux/man/8-ifru/">ifru</a>(8) <a href="/docs/linux/man/8-igetevent/">igetevent</a>(8) <a href="/docs/linux/man/8-ihealth/">ihealth</a>(8) <a href="/docs/linux/man/8-ilan/">ilan</a>(8) <a href="/docs/linux/man/8-ireset/">ireset</a>(8) <a href="/docs/linux/man/8-isel/">isel</a>(8) <a href="/docs/linux/man/8-isensor/">isensor</a>(8) <a href="/docs/linux/man/8-iserial/">iserial</a>(8) <a href="/docs/linux/man/8-isol/">isol</a>(8) <a href="/docs/linux/man/8-iwdt/">iwdt</a>(8) </p>
<h2>Warnings</h2>
<p>See <a rel="nofollow" href="http://ipmiutil.sourceforge.net/">http://ipmiutil.sourceforge.net/</a> for the latest version of ipmiutil and any bug fix list.</p>
<h2>Copyright</h2>
<p>Copyright (C) 2009 Kontron America, Inc. </p>
<p> See the file COPYING in the distribution for more details regarding redistribution. </p>
<p> This utility is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY.</p>
<h2>Author</h2>
<p>Andy Cress &lt;arcress at users.sourceforge.net&gt;</p>
