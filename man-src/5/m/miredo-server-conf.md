---
title: "miredo-server-conf(5)"
name: "miredo-server-conf"
section: "5"
letter: "m"
url: "/docs/linux/man/5-miredo-server-conf/"
description: "miredo-server.conf – configuration for miredo-server"
---

<p>miredo-server.conf &#8211; configuration for miredo-server</p>
<h2>Synopsis</h2>
<p><code>miredo-server.conf</code> </p>
<h2>Descripton</h2>
<p><i>miredo-server.conf</i> is the configuration file for <code>miredo-server</code>. Each configuration directive consists of one directive name, possibly followed by one or several spaces and a value for the directive. White spaces, empty lines and lines starting with &#8216;#&#8217; are ignored. </p>
<p> Directives are case-insensitive. A comprehensive list of the supported directives follows:</p>
<h2>Server Options</h2>
<dl>
<dt><code>ServerBindAddress </code><i>server_ip</i></p>
<dd>Specifies the primary IPv4 address of the Teredo server. miredo-server will bind to UDP/IPv4 port 3544 on this address and waits for packets from Teredo clients. It will advertise the Teredo prefix which is defined with the <code>Prefix</code> directive. </p>
<p> A Teredo server needs two subsequent IPv4 addresses. It will wait for UDP IPv4 packets on port 3544 on both addresses. <i>server_ip</i> specifies the lowest of both IPv4 addresses, which is known as the primary IPv4 server address. The secondary IPv4 address should be <code>server_ip + 1</code> and must also be assigned to the server. </p>
<dt><code>ServerBindAddress2 </code><i>server_ip2</i></p>
<dd>It is possible to specify a secondary IPv4 server address manually. However, Miredo clients will need manual configuration (with the <code>ServerAddress2</code> directive in miredo.conf). Other Teredo clients are believed not to support such setup. </p>
<dt><code>Prefix </code><i>teredo_prefix</i></p>
<dd>This directive specifies the <code>Teredo prefix</code> which the Teredo relay and/or server will advertise. <i>teredo_prefix</i> must be a valid IPv6 prefix. </p>
<p> The default value is <code>2001:0000::</code>. A 32-bits prefix is required to use this option. Since you do not have such big an IPv6 prefix <code>YOU WILL NOT USE THIS OPTION.</code> Moreover, certain third party Teredo client implementations require the default prefix. </p>
<dt><code>InterfaceMTU </code><i>mtu</i></p>
<dd>This directive overrides the value of the MTU that is advertised to Teredo clients. The default value is 1280 bytes and should not be changed if the default Teredo prefix is used. </p>
<p> <code>YOU MUST NOT USE THIS OPTION with the default prefix.</code> This would break interoperability with most Teredo relays. </p>
<dt><code>SyslogFacility </code><i>facility</i></p>
<dd>Specify which syslog&#8217;s facility is to be used by miredo-server for logging. Possible values are: <code>daemon</code> (the default), <code>local0</code>, &#8230; <code>local7</code>, <code>kern</code> and <code>user</code> (see <a href="/docs/linux/man/2-syslog/">syslog</a>(2)). </p>
</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-miredo-server/">miredo-server</a>(8) </p>
<h2>Author</h2>
<p>R33mi Denis-Courmont &lt;remi at remlab dot net&gt; </p>
<p> <a rel="nofollow" href="http://www.remlab.net/miredo/">http://www.remlab.net/miredo/</a></p>
