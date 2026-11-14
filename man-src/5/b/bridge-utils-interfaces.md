---
title: "bridge-utils-interfaces(5)"
name: "bridge-utils-interfaces"
section: "5"
letter: "b"
url: "/docs/linux/man/5-bridge-utils-interfaces/"
description: "bridge-utils-interfaces – bridge-utils extensions for the"
---

<p>bridge-utils-interfaces &#8211; bridge-utils extensions for the <code></p>
<p> <a href="/docs/linux/man/5-interfaces/">interfaces</a></code>(5) file format</p>
<h2>Description</h2>
<p>/etc/network/interfaces contains network interface configuration information for the <code><a href="/docs/linux/man/8-ifup/">ifup</a></code>(8) and <code><a href="/docs/linux/man/8-ifdown/">ifdown</a></code>(8) commands. This manpage describes the bridge extensions to the standard <code><a href="/docs/linux/man/5-interfaces/">interfaces</a></code>(5) file format. </p>
<p> The main extension is the bridge_ports option, with it you describe that the interface is a bridge and what ports does it have. These ports are the interfaces that are part of the bridge, and they shouldn&#8217;t have any stanzas defining them on the interfaces file. Other extensions allow you to tune the bridge options or change a bridge behaviour. </p>
<p> We&#8217;ll see this with an example:</p>
<dl>
<dd>
<pre>auto br0
iface br0 inet static
 address 192.168.1.2
 network 192.168.1.0
 netmask 255.255.255.0
 broadcast 192.168.1.255
 gateway 192.168.1.1
 bridge_ports all</pre>
</dl>
<p> Well, after setting this, an ifup br0, or the next reboot, should let you have a bridge up and running, after waiting for the ports to get to the forwarding status, of course. This bridge will be using all your ethX interfaces, as we have stated on the bridge_ports line. </p>
<p> The Debian bridge setup scripts will wait for it to get ready to work. They do this by trying to guess the maximum time that the bridge will need to get to the forwarding status, and by default, they will wait for the bridge to get there, or for the estimated maximum time to go by. This is done so that the services that are loaded after the bridge setup have a working network interface and don&#8217;t fail because the bridge is still not working. See bridge_maxwait if you want to change this behaviour. </p>
<p> An example of how to setup a so called anonymous bridge (a bridge without an assigned IP) would look like this:</p>
<dl>
<dd>
<pre>iface br1 inet manual
 bridge_ports eth1 eth2
 bridge_maxwait 0</pre>
</dl>
<p> Here we select the interfaces eth1 and eth2 to be added to the bridge interface br1, which will be an anonymous bridge, we also tell the scripts not to wait, as we won&#8217;t be having any service running on that interface (it doesn&#8217;t even have an IP). </p>
<p> An example of a little more complex bridge setup could be:</p>
<dl>
<dd>
<pre>auto br0
iface br0 inet static
 address 192.168.1.2
 network 192.168.1.0
 netmask 255.255.255.0
 broadcast 192.168.1.255
 bridge_ports all weird0
 bridge_bridgeprio 32767
 bridge_portprio eth0 129
 bridge_fd 5
 pre-up ip addr flush dev eth0</pre>
</dl>
<p> In this example we select all the eth* devices plus a weird device to be added to the bridge, also we change the bridge default priority to a higher one so that this bridge becomes the root (if there are no bridges with higher priority on the net, that is) and also we lower priority of port eth0 so that it is not used if there are other ports with higher priority to reach the same destination, at the end we lower the default forward delay and we add a pre-up command to remove all addresses on eth0 as this interface had an address set up before (needed only on weird/broken setups). </p>
<p> If there is a need to set up any of the interfaces participating on the bridge and not the bridge itself, then we must add the commands to set up those settings in a &quot;pre-up&quot; or &quot;up&quot; statement. This means that if we have a wireless card that we want to add to a bridge and we want to set it to master, and select the essid, instead of using the typical wireless_* commands we could add to the bridge definition something like this:</p>
<dl>
<dd>
<pre>pre-up iwconfig wlan0 mode master essid myESSID</pre>
</dl>
<p> Be aware, however, that using wireless cards as part of a bridge is not a good idea if the card belonging to the bridge is in managed mode. Trying to bridge packets coming out of our LAN through a wireless card that is set in managed mode (the card is a client of an AP) is bound to give problems, as the AP will probably refuse packets with source MAC addresses which are not associated (this will be the case of other machines going through the wireless card of the bridge into the AP). </p>
<p> Multiple stanzas of a bridge definition are currently not supported, so if you want to add a ipv6 and a ipv4 to a bridge do it all in one definition by using the &quot;up&quot; option. If however you still want to use multiple stanzas or would like to read more on this bug you can see it at <a rel="nofollow" href="http://bugs.debian.org/319832">http://bugs.debian.org/319832</a></p>
<h2>Iface Options</h2>
<p>A little explanation on the new options that can be used on /etc/network/interfaces to setup the bridge, so you don&#8217;t have to go and look at the scripts&#8230;</p>
<dl>
<dt><code>bridge_ports</code><i> interface specification</i></p>
<dd>this option must exist for the scripts to setup the bridge, with it you specify the ports you want to add to your bridge, either using &quot;none&quot; if you want a bridge without any interfaces or you want to add them later using brctl, or a list of the interfaces you want to add separated by spaces, for example:</p>
<dl>
<dd>
<dl>
<dd>
<pre>bridge_ports eth0 eth4</pre>
</dl>
<p> You should not put any lines to configure the interfaces that will be used by the bridge, as this will be setup automatically by the scripts when bringing the bridge up. </p>
<p> If you need to specify the interfaces more flexibly, you can use the following syntax (most useful on a Xen dom0):</p>
<dl>
<dd>
<pre>bridge_ports regex (eth|vif).*</pre>
</dl>
<p> This means to evaluate (as in <code><a href="/docs/linux/man/1-egrep/">egrep</a></code>(1)) the expressions that follow after &quot;regex&quot; until either the end or a &quot;noregex&quot; statement is reached. The regular expressions are evaluated against all local interfaces and those that match are added. </p>
<p> Specifying &quot;all&quot; is short for &quot;regex eth.* em.* p[0-9].* noregex&quot; and will get all the ethX and biosdevname-format (emX and pX) interfaces added to the bridge. </p>
<p> Carrying this to the extremes, the following is valid syntax:</p>
<dl>
<dd>
<pre>bridge_ports all regex if.0 noregex ext0 regex vif.*</pre>
</dl>
<p> This will add all ethX interfaces, the ifX0 interfaces, the ext0 interface and all vifX interfaces.</dl>
</dl>
<h3>
<dt><code>bridge_ageing</code><i></i><code>time</code></p>
<dd></h3>
<p>set ageing time, default is 300, can have a fractional part.</p>
<dt><code>bridge_bridgeprio</code><i> priority</i></p>
<dd>set bridge priority, <i>priority</i> is between 0 and 65535, default is 32768, affects bridge id, lowest priority bridge will be the root.</p>
<dt><code>bridge_fd</code><i> time</i></p>
<dd>set bridge forward delay to <i>time</i> seconds, default is 15, can have a fractional part.</p>
<dt><code>bridge_gcint</code><i> time</i></p>
<dd>set garbage collection interval to <i>time</i> seconds, default is 4, can have a fractional part. Available on Linux kernel versions &lt; 2.6.0.</p>
<dt><code>bridge_hello</code><i> time</i></p>
<dd>set hello time to <i>time</i> seconds, default is 2, can have a fractional part.</p>
<dt><code>bridge_hw</code><i> MAC_address|interface</i></p>
<dd>set the Ethernet MAC address of the bridge to the specified one or to the address of the specified interface. There were some concerns of how this was done in the past but we are doing it on a new way now, it is currently not only considered safe but also necessary or recommended in a lot of scenarios like IPv6, DHCP reservations, &#8230; the ussage of bridge_hw setting if the recommended way of doing this.</p>
<dt><code>bridge_maxage</code><i> time</i></p>
<dd>set max message age to <i>time</i> seconds, default is 20, can have a fractional part.</p>
<dt><code>bridge_maxwait</code><i> time</i></p>
<dd>forces to <i>time</i> seconds the maximum time that the Debian bridge setup scripts will wait for the bridge ports to get to the forwarding status, doesn&#8217;t allow factional part. If it is equal to 0 then no waiting is done.</p>
<dt><code>bridge_pathcost</code><i> port cost</i></p>
<dd>set path cost for a port, from 1 to 65535, default is 100, <i>port</i> is the name of the interface to which this setting applies.</p>
<dt><code>bridge_portprio</code><i> port priority</i></p>
<dd>set port priority, from 0 (max) to 63 (min), default is 32, affects port id, <i>port</i> is the name of the interface to which this setting applies.</p>
<dt><code>bridge_stp</code><i> state</i></p>
<dd>turn spanning tree protocol on/off, <i>state</i> values are on or yes to turn stp on and any other thing to set it off, default has changed to off for security reasons in latest kernels, so you should specify if you want stp on or off with this option, and not rely on your kernel&#8217;s default behaviour. Setting stp to on will cause IPv6 address to be lost, see: <i><a rel="nofollow" href="http://bugs.debian.org/736336">http://bugs.debian.org/736336</a></i></p>
<dt><code>bridge_vlan_aware</code><i> yes/no</i></p>
<dd>specify if the bridge is vlan aware an thus needs vlan filtering to be activated or not.</p>
<dt><code>bridge_waitport</code><i> time [ports]</i></p>
<dd>wait for a max of <i>time</i> seconds for the specified <i>ports</i> to become available, if no ports are specified then those specified on bridge_ports will be used here. Specifying no ports here should not be used if we are using regex or &quot;all&quot; on bridge_ports, as it wouldn&#8217;t work.</dl>
<h2>Files</h2>
<dl>
<dt><i>/etc/network/interfaces</i></p>
<dd>definitions of network interfaces See <code><a href="/docs/linux/man/5-interfaces/">interfaces</a></code>(5) for more information.</p>
<dd></dl>
<h2>Known Bugs/Limitations</h2>
<p>The default values shown here are current values as of this writing, but as they are not related to this package but to the bridge code itself, can change anytime.</p>
<h2>Author</h2>
<p>This manpage was written by Santiago Garcia Mantinan &lt;manty [at] debian.org&gt; based on <i><a href="/docs/linux/man/5-interfaces/">interfaces</a></i>(5).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-brctl/">brctl</a></code>(8), <code><a href="/docs/linux/man/5-interfaces/">interfaces</a></code>(5), <code><a href="/docs/linux/man/8-ifup/">ifup</a></code>(8), <code><a href="/docs/linux/man/8-iwconfig/">iwconfig</a></code>(8), <code><a href="/docs/linux/man/8-run-parts/">run-parts</a></code>(8). </p>
