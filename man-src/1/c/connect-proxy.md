---
title: "connect-proxy(1)"
name: "connect-proxy"
section: "1"
letter: "c"
url: "/docs/linux/man/1-connect-proxy/"
description: "connect-proxy — connect over SOCKS4/5 proxy"
---

<h2>NAME</h2>
<p> connect-proxy &#8212; connect over SOCKS4/5 proxy</p>
<h2>SYNOPSIS</h2>
<p> <code>connect-proxy</code> [<code>-dnhst45</code>] [<code>-R </code><i>resolve</i> ] [<code>-p </code><i>local-port</i> ] [<code>-w </code><i>secs</i> ] [<code>-H </code><i>[user@]proxy-server[:port]]</i> ] [<code>-S </code><i>[user@]socks-server[:port]]</i> ] [<code>-T </code><i>proxy-server[:port]</i> ] [<code>-c </code><i>telnet-proxy-command</i> ] [host] [port]</p>
<h2>DESCRIPTION</h2>
<p> <code>connect-proxy</code> open connection over SOCKS4/5 proxies </p>
<p> Please, note that any HTTP-Proxy tunnel won&#8217;t work with content-inspection firewall (unless using SSL).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-H</code></p>
<dd> specifies a hostname and port number of the http proxy server to relay. If port is omitted, 80 is used. You can specify this value in the environment variable HTTP_PROXY and pass the -h option to use it.</p>
<dt><code>-S</code></p>
<dd> specifies the hostname and port number of the SOCKS server to relay. Like -H, port number can be omitted and the default is 1080. You can also specify this value pair in the environment variable SOCKS5_SERVER and give the -s option to use it.</p>
<dt><code>-4</code></p>
<dd> specifies SOCKS relaying and indicates protocol version to use. It is valid only when used with &#8216;-s&#8217; or &#8216;-S&#8217;. Default is &#8216;-5&#8217; (protocol version 5)</p>
<dt><code>-R</code></p>
<dd> method to resolve the hostname. Three keywords (&quot;local&quot;, &quot;remote&quot;, &quot;both&quot;) or dot-notation IP address are acceptable. The keyword &quot;both&quot; means, &quot;Try local first, then remote&quot;. If a dot-notation IP address is specified, use this host as nameserver. The default is &quot;remote&quot; for SOCKS5 or &quot;local&quot; for others. On SOCKS4 protocol, remote resolving method (&quot;remote&quot; and &quot;both&quot;) requires protocol 4a supported server.</p>
<dt><code>-p</code></p>
<dd> will forward a local TCP port instead of using the standard input and output.</p>
<dt><code>-P</code></p>
<dd> same to &#8216;-p&#8217; except keep remote session. The program repeats waiting the port with holding remote session without disconnecting. To connect the remote session, send EOF to stdin or kill the program.</p>
<dt><code>-w</code></p>
<dd> timeout in seconds for making connection with TARGET host.</p>
<dt><code>-d</code></p>
<dd> used for debug. If you fail to connect, use this and check request to and response from server.</dl>
<h2>USAGE</h2>
<p> To use proxy, this example is for SOCKS5 connection to connect to<br />
&nbsp;<wbr> <code>connect-proxy -S firewall host 25</code><br />
&nbsp;<wbr> <code>SOCKS5_SERVER=firewall; export SOCKS5_SERVER; connect-proxy -s host 25</code> </p>
<p> For a HTTP-PROXY connection:<br />
&nbsp;<wbr> <code>connect-proxy -H proxy-server:8080 host 25</code><br />
&nbsp;<wbr> <code>HTTP_PROXY=proxy-server:8080; export HTTP_PROXY; connect-proxy -h host 25</code> </p>
<p> To forward a local port, for example to use ssh:<br />
&nbsp;<wbr> <code>connect-proxy -H proxy-server:8080 host 22 </code> <code>ssh -l user -p 5550 localhost</code> </p>
<p> To use it along ssh transparently: <code> # file://~/.ssh/config Host * ProxyCommand connect-proxy -H proxy-server:8080 %h %p</code></p>
<h2>ENVIRONMENT</h2>
<p> SOCKS5_USER, LOGNAME, USER HTTP_PROXY_USER, LOGNAME, USER</p>
<h2>SEE ALSO</h2>
<p> ssh (1).</p>
<h2>WWW</h2>
<p> <a rel="nofollow" href="http://www.taiyo.co.jp/~gotoh/ssh/connect.html">http://www.taiyo.co.jp/~gotoh/ssh/connect.html</a></p>
<h2>AUTHOR</h2>
<p> This manual page was written by Philippe COVAL Philippe.COVAL [at] laposte.net for the <code>Debian</code> system (but may be used by others). Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 any later version published by the Free Software Foundation.<br />
&nbsp;<wbr> </p>
<p> On Debian systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL.<br />
&nbsp;<wbr> </p>
<h2>Index</h2>
