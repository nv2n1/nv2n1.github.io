---
title: "route(8)"
name: "route"
section: "8"
letter: "r"
url: "/docs/linux/man/8-route/"
description: "route – show / manipulate the IP routing table"
---

<p>route &#8211; show / manipulate the IP routing table</p>
<h2>Synopsis</h2>
<p><code>route</code> [<code>-CFvnNee</code>] [<code>-A</code> family |<code>-4</code>|<code>-6</code>]</p>
<dl>
<dt><code>route </code></dt>
<dd>[<code>-v</code>] [<code>-A</code> family |<code>-4</code>|<code>-6</code>] <code>add </code> [<code>-net</code>|<code>-host</code>] <i>target </i> [<code>netmask</code> <i>Nm</i>] [<code>gw</code> <i>Gw</i>] [<code>metric</code> <i>N</i>] [<code>mss</code> <i>M</i>] [<code>window</code> <i>W</i>] [<code>irtt</code> <i>I</i>] [<code>reject</code>] [<code>mod</code>] [<code>dyn</code>] [<code>reinstate</code>] [[<code>dev</code>] <i>If</i>]</dd>
<dt><code>route </code></dt>
<dd>[<code>-v</code>] [<code>-A</code> <i>family</i> |<code>-4</code>|<code>-6</code>] <code>del </code> [<code>-net</code>|<code>-host</code>] <i>target </i> [<code>gw</code> <i>Gw</i>] [<code>netmask</code> <i>Nm</i>] [<code>metric</code> <i>M</i>] [[<code>dev</code>] <i>If</i>]</dd>
<dt><code>route </code></dt>
<dd>[<code>-V</code>] [<code>&#8211;version</code>] [<code>-h</code>] [<code>&#8211;help</code>]</dd></dl>
<h2>Description</h2>
<p><code>Route</code> manipulates the kernel&#8217;s IP routing tables. Its primary use is to set up static routes to specific hosts or networks via an interface after it has been configured with the <code><a href="/docs/linux/man/8-ifconfig/">ifconfig</a></code>(8) program. When the <code>add</code> or <code>del</code> options are used, <code>route</code> modifies the routing tables. Without these options, <code>route</code> displays the current contents of the routing tables. </p>
<h2>Options</h2>
<dl>
<dt><code>-A </code><i>family</i></dt>
<dd>use the specified address family (eg `inet&#8217;). Use <code>route &#8211;help</code> for a full list. You can use <code>-6 </code> as an alias for <code>&#8211;inet6 </code> and <code>-4 </code> as an alias for <code>-A inet</code> </dd>
<dt><code>-F</code></dt>
<dd>operate on the kernel&#8217;s FIB (Forwarding Information Base) routing table. This is the default.</dd>
<dt><code>-C</code></dt>
<dd>operate on the kernel&#8217;s routing cache.</dd>
<dt><code>-v</code></dt>
<dd>select verbose operation.</dd>
<dt><code>-n</code></dt>
<dd>show numerical addresses instead of trying to determine symbolic host names. This is useful if you are trying to determine why the route to your nameserver has vanished.</dd>
<dt><code>-e</code></dt>
<dd>use <code><a href="/docs/linux/man/8-netstat/">netstat</a></code>(8)-format for displaying the routing table. <code>-ee </code> will generate a very long line with all parameters from the routing table.</dd>
<dt><code>del</code></dt>
<dd>delete a route.</dd>
<dt><code>add </code></dt>
<dd>add a new route.</dd>
<dt><i>target</i></dt>
<dd>the destination network or host. You can provide an addresses or symbolic network or host name. Optionally you can use <code>/</code><i>prefixlen</i> notation instead of using the <code>netmask</code> option.</dd>
<dt><code>-net</code></dt>
<dd>the <i>target</i> is a network.</dd>
<dt><code>-host</code></dt>
<dd>the <i>target </i> is a host.</dd>
<dt><code>netmask </code><i>NM</i></dt>
<dd>when adding a network route, the netmask to be used.</dd>
<dt><code>gw </code><i>GW</i></dt>
<dd>route packets via a gateway.<br/>
 <code>NOTE:</code> The specified gateway must be reachable first. This usually means that you have to set up a static route to the gateway beforehand. If you specify the address of one of your local interfaces, it will be used to decide about the interface to which the packets should be routed to. This is a BSDism compatibility hack.</dd>
<dt><code>metric </code><i>M</i></dt>
<dd>set the metric field in the routing table (used by routing daemons) to <i>M</i>. If this option is not specified the metric for inet6 (IPv6) address family defaults to &#8216;1&#8217;, for inet (IPv4) it defaults to &#8216;0&#8217;. You should always specify an explicit metric value to not rely on those defaults &#8211; they also differ from iproute2.</dd>
<dt><code>mss </code><i>M</i></dt>
<dd>sets MTU (Maximum Transmission Unit) of the route to <i>M</i> bytes. Note that the current implementation of the route command does not allow the option to set the Maximum Segment Size (MSS).</dd>
<dt><code>window </code><i>W</i></dt>
<dd>set the TCP window size for connections over this route to <i>W</i> bytes. This is typically only used on AX.25 networks and with drivers unable to handle back to back frames.</dd>
<dt><code>irtt </code><i>I</i></dt>
<dd>set the initial round trip time (irtt) for TCP connections over this route to <i>I</i> milliseconds (1-12000). This is typically only used on AX.25 networks. If omitted the RFC 1122 default of 300ms is used.</dd>
<dt><code>reject</code></dt>
<dd>install a blocking route, which will force a route lookup to fail. This is for example used to mask out networks before using the default route. This is NOT for firewalling.</dd>
<dt><code>mod, dyn, reinstate</code></dt>
<dd>install a dynamic or modified route. These flags are for diagnostic purposes, and are generally only set by routing daemons.</dd>
<dt><code>dev </code><i>If</i></dt>
<dd>force the route to be associated with the specified device, as the kernel will otherwise try to determine the device on its own (by checking already existing routes and device specifications, and where the route is added to). In most normal networks you won&#8217;t need this. </dd>
<p> If <code>dev </code><i>If</i> is the last option on the command line, the word <code>dev</code> may be omitted, as it&#8217;s the default. Otherwise the order of the route modifiers (<code>metric netmask gw dev</code>) doesn&#8217;t matter. </p>
</dl>
<h2>Examples</h2>
<dl>
<dt><code>route add -net 127.0.0.0 netmask 255.0.0.0 metric 1024 dev lo</code></dt>
<dd>adds the normal loopback entry, using netmask 255.0.0.0 and associated with the &quot;lo&quot; device (assuming this device was previously set up correctly with <code><a href="/docs/linux/man/8-ifconfig/">ifconfig</a></code>(8)).</dd>
<dt><code>route add -net 192.56.76.0 netmask 255.255.255.0 metric 1024 dev eth0</code></dt>
<dd>adds a route to the local network 192.56.76.x via &quot;eth0&quot;. The word &quot;dev&quot; can be omitted here.</dd>
<dt><code>route del default</code></dt>
<dd>deletes the current default route, which is labeled &quot;default&quot; or 0.0.0.0 in the destination field of the current routing table.</dd>
<dt><code>route del -net 192.56.76.0 netmask 255.255.255.0</code></dt>
<dd>deletes the route. Since the Linux routing kernel uses classless addressing, you pretty much always have to specify the netmask that is same as as seen in &#8216;route -n&#8217; listing.</dd>
<dt><code>route add default gw mango </code></dt>
<dd>adds a default route (which will be used if no other route matches). All packets using this route will be gatewayed through the address of a node named &quot;mango&quot;. The device which will actually be used for that route depends on how we can reach &quot;mango&quot; &#8211; &quot;mango&quot; must be on directly reachable route.</dd>
<dt><code>route add mango sl0</code></dt>
<dd>Adds the route to the host named &quot;mango&quot; via the SLIP interface (assuming that &quot;mango&quot; is the SLIP host).</dd>
<dt><code>route add -net 192.57.66.0 netmask 255.255.255.0 gw mango</code></dt>
<dd>This command adds the net &quot;192.57.66.x&quot; to be gatewayed through the former route to the SLIP interface.</dd>
<dt><code>route add -net 224.0.0.0 netmask 240.0.0.0 dev eth0</code></dt>
<dd>This is an obscure one documented so people know how to do it. This sets all of the class D (multicast) IP routes to go via &quot;eth0&quot;. This is the correct normal configuration line with a multicasting kernel.</dd>
<dt><code>route add -net 10.0.0.0 netmask 255.0.0.0 metric 1024 reject</code></dt>
<dd>This installs a rejecting route for the private network &quot;10.x.x.x.&quot;</dd>
<dt><code>route -6 add 2001:0002::/48 metric 1 dev eth0 </code></dt>
<dd>This adds a IPv6 route with the specified metric to be directly reachable via eth0. </dd>
<h2>Output</h2>
<p>The output of the kernel routing table is organized in the following columns</p>
<dl>
<dt><code>Destination </code></dt>
<dd>The destination network or destination host.</dd>
<dt><code>Gateway</code></dt>
<dd>The gateway address or &#8216;*&#8217; if none set.</dd>
<dt><code>Genmask </code></dt>
<dd>The netmask for the destination net; &#8216;255.255.255.255&#8217; for a host destination and &#8216;0.0.0.0&#8217; for the <code>default</code> route.</dd>
<dt><code>Flags </code></dt>
<dd>Possible flags include<br/>
 <code>U</code> (route is <code>up</code>)<br/>
 <code>H</code> (target is a <code>host</code>)<br/>
 <code>G</code> (use <code>gateway</code>)<br/>
 <code>R</code> (<code>reinstate</code> route for dynamic routing)<br/>
 <code>D</code> (<code>dynamically</code> installed by daemon or redirect)<br/>
 <code>M</code> (<code>modified</code> from routing daemon or redirect)<br/>
 <code>A</code> (installed by <code>addrconf</code>)<br/>
 <code>C</code> (<code>cache</code> entry)<br/>
 <code>!</code> (<code>reject</code> route)</dd>
<dt><code>Metric </code></dt>
<dd>The &#8216;distance&#8217; to the target (usually counted in hops).</dd>
<dt><code>Ref </code></dt>
<dd>Number of references to this route. (Not used in the Linux kernel.)</dd>
<dt><code>Use</code></dt>
<dd>Count of lookups for the route. Depending on the use of -F and -C this will be either route cache misses (-F) or hits (-C).</dd>
<dt><code>Iface</code></dt>
<dd>Interface to which packets for this route will be sent.</dd>
<dt><code>MSS </code></dt>
<dd>Default maximum segment size for TCP connections over this route.</dd>
<dt><code>Window </code></dt>
<dd>Default window size for TCP connections over this route.</dd>
<dt><code>irtt</code></dt>
<dd>Initial RTT (Round Trip Time). The kernel uses this to guess about the best TCP protocol parameters without waiting on (possibly slow) answers.</dd>
<dt><code>HH (cached only)</code></dt>
<dd>The number of ARP entries and cached routes that refer to the hardware header cache for the cached route. This will be -1 if a hardware address is not needed for the interface of the cached route (e.g. lo).</dd>
<dt><code>Arp (cached only)</code></dt>
<dd>Whether or not the hardware address for the cached route is up to date.</dd></dl>
<h2>Files</h2>
<p><i>/proc/net/ipv6_route</i><br/>
 <i>/proc/net/route</i><br/>
 <i>/proc/net/rt_cache</i></p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-ifconfig/">ifconfig</a></i>(8), <i><a href="/docs/linux/man/8-netstat/">netstat</a></i>(8), <i><a href="/docs/linux/man/8-arp/">arp</a></i>(8), <i><a href="/docs/linux/man/8-rarp/">rarp</a></i>(8), <i><a href="/docs/linux/man/8-ip/">ip</a></i>(8) </p>
<h2>History</h2>
<p><code>Route</code> for Linux was originally written by Fred N. van Kempen, &lt;waltje [at] uwalt.nl.mugnet.org&gt; and then modified by Johannes Stille and Linus Torvalds for pl15. Alan Cox added the mss and window options for Linux 1.1.22. irtt support and merged with netstat from Bernd Eckenfels.</p>
<h2>Author</h2>
<p>Currently maintained by Phil Blundell &lt;Philip.Blundell [at] pobox.com&gt; and Bernd Eckenfels &lt;net-tools [at] lina.inka.de&gt;.</p>
</dl>