---
title: "addr2name(1)"
name: "addr2name"
section: "1"
letter: "a"
url: "/docs/linux/man/1-addr2name/"
description: "addr2name, name2addr – perform DNS lookups from scripts"
---

<h2>NAME</h2>
<p> addr2name, name2addr &#8211; perform DNS lookups from scripts</p>
<h2>SYNOPSIS</h2>
<p> <code>addr2name</code> [<code>-46cmnr</code>] [<code>HOSTNAMES</code>] </p>
<p> <code>name2addr</code> [<code>-46cn</code>] [<code>HOSTNAMES</code>] </p>
<h2>DESCRIPTON</h2>
<p> Write addresses or canonical hostname of specified names to the standard output. If no names are specified via the command line, they are read from the standard input. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-4</code> or <code>&#8211;ipv4</code></p>
<dd> Only try to perform IPv4 lookups. </p>
<dt><code>-6</code> or <code>&#8211;ipv6</code></p>
<dd> Only try to perform IPv6 lookups. </p>
<dt><code>-c</code> or <code>&#8211;config</code></p>
<dd> Only lookup and print results for address families that match locally configured addresses (If the system has no IPv4 resp IPv6 address, then IPv4 resp IPv6 addresses are ignored). </p>
<dt><code>-h</code> or <code>&#8211;help</code></p>
<dd> Display some help and exit. </p>
<dt><code>-m</code> or <code>&#8211;multiple</code></p>
<dd> Normally, if a name yields multiple results, only the first one is printed. With this optional parameter, all results will be printed on a single line, separated by spaces. </p>
<dt><code>-n</code> or <code>&#8211;numeric</code></p>
<dd> Prevent forward hostname lookup. This ensures that the input names are numeric addresses, which do not need to be looked up. Typically used along with the &#8211;reverse option to convert numerical addresses to canonical hostnames. </p>
<dt><code>-r</code> or <code>&#8211;reverse</code></p>
<dd> Perform a reverse DNS lookup (enabled implicitly with <code>addr2name</code>). <code>addr2name</code> prints numerical resolved addresses by default instead. </p>
<dt><code>&#8211;version</code></p>
<dd> Display program version and license and exit. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-host/">host</a>(1), <a href="/docs/linux/man/3-getaddrinfo/">getaddrinfo</a>(3), <a href="/docs/linux/man/3-getnameinfo/">getnameinfo</a>(3), <a href="/docs/linux/man/5-resolv-conf/">resolv.conf</a>(5) </p>
<h2>AUTHOR</h2>
<p> R33mi Denis-Courmont &lt;remi at remlab dot net&gt; </p>
<p> <a rel="nofollow" href="http://www.remlab.net/ndisc6/">http://www.remlab.net/ndisc6/</a> </p>
<h2>Index</h2>
