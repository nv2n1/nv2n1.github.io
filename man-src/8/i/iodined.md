---
title: "iodined(8)"
name: "iodined"
section: "8"
letter: "i"
url: "/docs/linux/man/8-iodined/"
description: "iodined – tunnel IPv4 over DNS"
---

<p>iodined &#8211; tunnel IPv4 over DNS</p>
<h2>Synopsis</h2>
<p><code>iodined [-v]</code> </p>
<p> <code>iodined [-h]</code> </p>
<p> <code>iodined [-c] [-s] [-f] [-D] [-u</code> <i>user</i> <code>] [-t</code> <i>chrootdir</i> <code>] [-d</code> <i>device</i> <code>] [-m</code> <i>mtu</i> <code>] [-l</code> <i>listen_ip</i> <code>] [-p</code> <i>port</i> <code>] [-n</code> ( <code>auto</code> | <i>external_ip</i> ) <code>] [-b</code> <i>dnsport</i> <code>] [-P</code> <i>password</i> <code>] [-z</code> <i>context</i> <code>] [-F</code> <i>pidfile</i> <code>] [-i</code> <i>max_idle_time</i> <code>]</code> <i>tunnel_ip</i> <code>[</code> <i>/netmask</i> <code>]</code> <i>topdomain</i></p>
<h2>Description</h2>
<p><code>iodined</code> lets you tunnel IPv4 data through a DNS server. This can be useful in situations where Internet access is firewalled, but DNS queries are allowed. It needs a TUN/TAP device to operate. The bandwidth is asymmetrical, with a measured maximum of 680 kbit/s upstream and 2.3 Mbit/s downstream in a wired LAN test network. Realistic sustained throughput on a Wifi network using a carrier-grade DNS cache has been measured at some 50 kbit/s upstream and over 200 kbit/s downstream. <code>iodine</code> is the client application, <code>iodined</code> is the server. </p>
<p> Note: server and client are required to speak the exact same protocol. In most cases, this means running the same iodine[d] version. Unfortunately, implementing backward and forward protocol compatibility is usually not feasible.</p>
<h2>Options</h2>
<h3>Common Options:</h3>
<dl>
<dt><code>-v</code></p>
<dd>Print version info and exit.</p>
<dt><code>-h</code></p>
<dd>Print usage info and exit.</p>
<dt><code>-f</code></p>
<dd>Keep running in foreground.</p>
<dt><code>-u user</code></p>
<dd>Drop privileges and run as user &#8216;user&#8217; after setting up tunnel.</p>
<dt><code>-t chrootdir</code></p>
<dd>Chroot to &#8216;chrootdir&#8217; after setting up tunnel.</p>
<dt><code>-d device</code></p>
<dd>Use the TUN device &#8216;device&#8217; instead of the normal one, which is dnsX on Linux and otherwise tunX.</p>
<dt><code>-P password</code></p>
<dd>Use &#8216;password&#8217; to authenticate. If not used, <code>stdin</code> will be used as input. Only the first 32 characters will be used.</p>
<dt><code>-z context</code></p>
<dd>Apply SELinux &#8216;context&#8217; after initialization.</p>
<dt><code>-F pidfile</code></p>
<dd>Create &#8216;pidfile&#8217; and write process id in it.</dl>
<h3>Server Options:</h3>
<dl>
<dt><code>-c</code></p>
<dd>Disable checking the client IP address on all incoming requests. By default, requests originating from non-matching IP addresses will be rejected, however this will cause problems when requests are routed via a cluster of DNS servers.</p>
<dt><code>-s</code></p>
<dd>Don&#8217;t try to configure IP address or MTU. This should only be used if you have already configured the device that will be used.</p>
<dt><code>-D</code></p>
<dd>Increase debug level. Level 1 prints info about each RX/TX packet. Implies the <code>-f</code> option. On level 2 (-DD) or higher, DNS queries will be printed literally. When using Base128 upstream encoding, this is best viewed as ISO Latin-1 text instead of (illegal) UTF-8. This is easily done with : &quot;LC_ALL=C luit iodined -DD &#8230;&quot; (see <a href="/docs/linux/man/1-luit/">luit</a>(1)).</p>
<dt><code>-m mtu</code></p>
<dd>Set &#8216;mtu&#8217; as mtu size for the tun device. This will be sent to the client on login, and the client will use the same mtu for its tun device. Default 1130. Note that the DNS traffic will be automatically fragmented when needed.</p>
<dt><code>-l listen_ip</code></p>
<dd>Make the server listen only on &#8216;listen_ip&#8217; for incoming requests. By default, incoming requests are accepted from all interfaces.</p>
<dt><code>-p port</code></p>
<dd>Make the server listen on &#8216;port&#8217; instead of 53 for traffic. If &#8216;listen_ip&#8217; does not include localhost, this &#8216;port&#8217; can be the same as &#8216;dnsport&#8217;. <code>Note:</code> You must make sure the dns requests are forwarded to this port yourself.</p>
<dt><code>-n auto|external_ip</code></p>
<dd>The IP address to return in NS responses. Default is to return the address used as destination in the query. If external_ip is &#8216;auto&#8217;, iodined will use externalip.net web service to retrieve the external IP of the host and use that for NS responses.</p>
<dt><code>-b dnsport</code></p>
<dd>If this port is specified, all incoming requests not inside the tunnel domain will be forwarded to this port on localhost, to be handled by a real dns. If &#8216;listen_ip&#8217; does not include localhost, this &#8216;dnsport&#8217; can be the same as &#8216;port&#8217;. <code>Note:</code> The forwarding is not fully transparent, and not advised for use in production environments.</p>
<dt><code>-i max_idle_time</code></p>
<dd>Make the server stop itself after max_idle_time seconds if no traffic have been received. This should be combined with systemd or upstart on demand activation for being effective.</dl>
<h3>Client Arguments:</h3>
<dl>
<dt><code>nameserver</code></p>
<dd>The nameserver to use to relay the dns traffic. This can be any relaying nameserver or the server running iodined if reachable. This field can be given as an IPv4/IPv6 address or as a hostname. This argument is optional, and if not specified a nameserver will be read from the <i>/etc/resolv.conf</i> file.</p>
<dt><code>topdomain</code></p>
<dd>The dns traffic will be sent as queries for subdomains under &#8216;topdomain&#8217;. This is normally a subdomain to a domain you own. Use a short domain name to get better throughput. If <code>nameserver</code> is the iodined server, then the topdomain can be chosen freely. This argument must be the same on both the client and the server.</dl>
<h3>Server Arguments:</h3>
<dl>
<dt><code>tunnel_ip[/netmask]</code></p>
<dd>This is the server&#8217;s ip address on the tun interface. The client will be given the next ip number in the range. It is recommended to use the 10.0.0.0 or 172.16.0.0 ranges. The default netmask is /27, can be overridden by specifying it here. Using a smaller network will limit the number of concurrent users.</p>
<dt><code>topdomain</code></p>
<dd>The dns traffic is expected to arrive as queries for subdomains under &#8216;topdomain&#8217;. This is normally a subdomain to a domain you own. Use a short domain name to get better throughput. This argument must be the same on both the client and the server. Queries for domains other than &#8216;topdomain&#8217; will be forwarded when the -b option is given, otherwise they will be dropped.</dl>
<h2>Examples</h2>
<p>See the README file for both a quick test scenario, and a detailed description of real-world deployment.</p>
<h2>Security</h2>
<p>Login is a relatively secure challenge-response MD5 hash, with the password never passing the wire. However, all other data is <code>NOT</code> encrypted in any way. The DNS traffic is also vulnerable to replay, injection and man-in-the-middle attacks, especially when iodined is used with the -c option. Use of ssh or vpn tunneling is strongly recommended. On both server and client, use <i>iptables</i>, <i>pf</i> or other firewalls to block all traffic coming in from the tun interfaces, except to the used ssh or vpn ports.</p>
<h2>Environment</h2>
<h3>Iodined_Pass</h3>
<p>If the environment variable <code>IODINED_PASS</code> is set, iodined will use the value it is set to as password instead of asking for one. The <code>-P</code> option still has precedence.</p>
<h2>See Also</h2>
<p>The README file in the source distribution contains some more elaborate information.</p>
<h2>Bugs</h2>
<p>File bugs at <a rel="nofollow" href="http://dev.kryo.se/iodine/">http://dev.kryo.se/iodine/</a></p>
<h2>Authors</h2>
<p>Erik Ekman &lt;yarrick [at] kryo.se&gt; and Bjorn Andersson &lt;flex [at] kryo.se&gt;. Major contributions by Anne Bezemer.</p>
