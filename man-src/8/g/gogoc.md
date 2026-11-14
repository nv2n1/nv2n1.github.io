---
title: "gogoc(8)"
name: "gogoc"
section: "8"
letter: "g"
url: "/docs/linux/man/8-gogoc/"
description: "gogoc – gogoCLIENT"
---

<p><code>gogoc</code> &#8211; gogoCLIENT</p>
<h2>Synopsis</h2>
<p><code>gogoc</code> [-<code>h</code> ] [-<code>?</code> ] [-<code>y</code> ] [-<code>n</code> ] [-<code>b</code> ]<br />
<code>gogoc</code> [-<code>f </code><i>config_file</i> ] [-<code>i </code><i>interface_name</i> ] [-<code>u </code><i>interface_name</i> ] [-<code>s </code><i>interface_name</i> ] [-<code>r </code><i>retry_delay</i> ]</p>
<h2>Description</h2>
<p><code>gogoc</code> provides a means to configure a tunnel obtained from a tunnel server that supports the tunnel setup protocol (TSP). <code>gogoc</code> will connect to a tunnel server and request a tunnel according to the specifications given in the configuration file. As a background process, it will then monitor the state of the tunnel. In the event of a timeout, gogoc will establish a new tunnel. <code>gogoc</code> currently supports three types of tunnels: </p>
<dt><code>&#8211; v6v4 (IPv6 over IPv4)</code></p>
<dd>Supported on FreeBSD, NetBSD, OpenBSD, Linux, Windows, Solaris, Darwin and OpenWRT.</p>
<dt><code>&#8211; v6udpv4 (IPv6 over UDP over IPv4)</code></p>
<dd>Supported on FreeBSD, Linux, Windows, Darwin and OpenWRT.</p>
<dt><code>&#8211; v4v6 (IPv4 over IPv6 (DSTM))</code></p>
<dd>Supported on FreeBSD and Windows. </p>
<h2>Arguments</h2>
<p>The following options are available:</p>
<dl>
<dt><code>-h, ?</code></p>
<dd>Displays a short usage summary and quits. </p>
<dt><code>-y</code></p>
<dd>Automatically accept server&#8217;s public key. </p>
<dt><code>-n</code></p>
<dd>Run as a foreground process. </p>
<dt><code>-b</code></p>
<dd>Stop trying to reconnect upon first error received. </p>
<dt><code>-f </code><i>configuration_file</i></p>
<dd>Specifies a different configuration file.<br />
 Default is /etc/gogoc/gogoc.conf. </p>
<dt><code>-s </code><i>interface_name</i></p>
<dd>Overrides <code>client_v4 </code> in gogoc.conf5 </p>
<dt><code>-i </code><i>interface_name</i></p>
<dd>Overrides <code>if_tunnel_v6v4 </code> in gogoc.conf5 </p>
<dt><code>-u </code><i>interface_name</i></p>
<dd>Overrides <code>if_tunnel_v6udpv4 </code> in gogoc.conf5 </p>
<dt><code>-r </code><i>retry_delay</i></p>
<dd>Overrides <code>retry_delay</code> in gogoc.conf5 </p>
</dl>
<h2>See Also</h2>
<p>gogoc.conf5<br />
 <a rel="nofollow" href="http://www.gogo6.com">http://www.gogo6.com</a></p>
<h2>Acknowledgment</h2>
<p>This software uses code taken from other organizations as :</p>
<dl>
<dt><code>&#8211; </code><i>RSA data security for md5.</i></p>
<dd>
<dt><code>&#8211; </code><i>The Apache Software Foundation for Base64 encoding and decoding.</i></p>
<dd></dl>
<h2>Authors</h2>
<p>gogo6 Inc.<br />
 <a rel="nofollow" href="http://www.gogo6.com">http://www.gogo6.com</a><br />
 support [at] gogo6.com</p>
