---
title: "rdnssd(8)"
name: "rdnssd"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rdnssd/"
description: "rdnssd – IPv6 Recursive DNS Server discovery Daemon"
---

<p>rdnssd &#8211; IPv6 Recursive DNS Server discovery Daemon</p>
<h2>Synopsis</h2>
<p><code>rdnssd</code> [<code>-f</code>] [<code>-H merge-hook</code>] [<code>-r resolv-file</code>] [<code>-p pidfile</code>] [<code>-u username</code>] </p>
<h2>Descripton</h2>
<p><code>rdnssd</code> is a daemon program providing client-side support for DNS configuration using the Recursive DNS Server (RDNSS) option, as described in RFC 5006. Its purpose is to supply IPv6 DNS resolvers through stateless autoconfiguration, carried by Router Advertisements. </p>
<p> rdnssd parses RDNSS options and keeps track of resolvers to write nameservers entries to a <a href="/docs/linux/man/5-resolv-conf/">resolv.conf</a>(5) configuration file. By default, it writes its own separate file, and may call an external hook to merge it with the main /etc/resolv.conf. This is aimed at easing coexistence with concurrent daemons, especially IPv4 ones, updating /etc/resolv.conf too. </p>
<p> On Linux, since version 2.6.24, rdnssd takes advantage of a new netlink interface, forwarding RDNSS options validated by the kernel to userland. Otherwise, it merely listens to all ICMPv6 traffic through a raw socket.</p>
<h2>Options</h2>
<dl>
<dt><code>-f</code> or <code>&#8211;foreground</code></dt>
<dd>Do not detach from the console. Run the program in the foreground. </dd>
<dt><code>-H merge-hook</code> or <code>&#8211;merge-hook merge-hook</code></dt>
<dd>Execute this hook whenever resolv.conf is updated. If this option is not specified, then no hook will be called. </dd>
<dt><code>-h</code> or <code>&#8211;help</code></dt>
<dd>Display some help and exit. </dd>
<dt><code>-p pidfile</code> or <code>&#8211;pidfile pidfile</code></dt>
<dd>Override the location of the pidfile. </dd>
<dt><code>-r resolv-file</code> or <code>&#8211;resolv-file resolv-file</code></dt>
<dd>Set the path to the generated resolv.conf file. </dd>
<dt><code>-u username</code> or <code>&#8211;user username</code></dt>
<dd>Override the user that the program will run as. By default, it runs as <code>nobody</code>. </dd>
<dt><code>-V</code> or <code>&#8211;version</code></dt>
<dd>Display program version and license and exit. </dd>
</dl>
<h2>Files</h2>
<dl>
<dt><i>/etc/rdnssd/merge-hook</i></dt>
<dd>A basic merge hook shipped with rdnssd, to be called with the -H option. </dd>
<dt><i>/var/run/rdnssd/resolv.conf</i></dt>
<dd>The default <a href="/docs/linux/man/5-resolv-conf/">resolv.conf</a>(5) file that rdnssd writes its configuration to. </dd>
<dt><i>/var/run/rdnssd.pid</i></dt>
<dd>The process-id file. </dd>
</dl>
<h2>Bugs</h2>
<p>rdnssd does not keep track of the lifetimes of the routers associated with some DNS resolvers, whereas it should to strictly comply with RFC 5006. When rdnssd uses a raw socket instead of the netlink kernel interface, it does not validate received Neighbor Discovery traffic in any way. For example, it will always consider Router Advertisement packets, whereas it should not if the host is configured as a router. When the netlink interface is used, such validation is done by the kernel. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/5-resolv-conf/">resolv.conf</a>(5), <a href="/docs/linux/man/8-rdisc6/">rdisc6</a>(8), <a href="/docs/linux/man/7-ipv6/">ipv6</a>(7) </p>
<h2>Author</h2>
<p>Pierre Ynard &lt;linkfanel at yahoo.fr&gt; </p>
<p> <a rel="nofollow" href="http://www.remlab.net/ndisc6/">http://www.remlab.net/ndisc6/</a></p>
