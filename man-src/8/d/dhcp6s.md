---
title: "dhcp6s(8)"
name: "dhcp6s"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dhcp6s/"
description: "dhcp6s – DHCPv6 server"
---

<p><code>dhcp6s</code> &#8211; DHCPv6 server</p>
<h2>Synopsis</h2>
<p>[-<code>c </code><i>configfile</i> ] [-<code>Ddf</code> ] [-<code>k </code><i>ctlkeyfile</i> ] [-<code>p </code><i>ctlport</i> ] [-<code>P </code><i>pid-file</i> ] <i>interface</i></p>
<h2>Description</h2>
<p>replies to DHCPv6 client as DHCPv6 server. can give the following information to clients. </p>
<ul>
<li> IPv6 prefixes for the requesting site
<li> Non-temporary IPv6 addresses
<li> A list of the DNS server addresses
<li> DNS Domain Search List
<li> A list of the NTP server addresses
<li> A list of the SIP server addresses
<li> SIP Server domain name
<li> A list of the NIS server addresses
<li> NIS domain name
<li> A list of the NIS+ server addresses
<li> NIS+ domain name
<li> A list of the BCMCS server addresses
<li> BCMCS Server domain name </ul>
<p> Command line options are as below:</p>
<dl>
<dt><code>-c </code><i>configfile</i></p>
<dd>Use <i>configfile</i> as the configuration file.</p>
<dt><code>-d</code></p>
<dd>Print debugging messages.</p>
<dt><code>-D</code></p>
<dd>Even more debugging information is printed.</p>
<dt><code>-f</code></p>
<dd>Foreground mode (useful when debugging). Although usually prints warning, debugging, or error messages to <a href="/docs/linux/man/8-syslog/">syslog</a>(8), it prints the messages to standard error if this option is specified.</p>
<dt><code>-k </code><i>ctlkeyfile</i></p>
<dd>Use <i>ctlkeyfile</i> to store the shared secret to authenticate the communication with <code>dhcp6ctl</code> The default file name used when unspecified is /etc/wide-dhcpv6/dhcp6sctlkey The default name is intentionally same as that for <code>dhcp6ctl</code> so that the server and the control command can share the file when <code>dhcp6ctl</code> controls the server on the same node, which should be the typical case.</p>
<dt><code>-p </code><i>ctlport</i></p>
<dd>Use <i>ctlport</i> as the port number listening on to communicate with <code>dhcp6ctl</code></p>
<dt><code>-P </code><i>pid-file</i></p>
<dd>Use <i>pid-file</i> to dump the process ID of <code>.</code></dl>
<h2>Files</h2>
<dl>
<dt><code>/etc/wide-dhcpv6/dhcp6s.conf </code></p>
<dd>is the default configuration file.</p>
<dt><code>/var/lib/dhcpv6/dhcp6s_duid </code></p>
<dd>is the default file to store the server&#8217;s DUID.</p>
<dt><code>/etc/wide-dhcpv6/dhcp6sctlkey </code></p>
<dd>is the default key file to communicate with the control command. See <a href="/docs/linux/man/8-dhcp6ctl/">dhcp6ctl</a>(8) for the file format.</p>
<dt><code>/var/run/dhcp6s.pid </code></p>
<dd>is the default file that contains pid of the currently running <code>.</code></dl>
<h2>See Also</h2>
<p>dhcp6s.conf5, <a href="/docs/linux/man/8-dhcp6ctl/">dhcp6ctl</a>(8), <a href="/docs/linux/man/8-dhcp6c/">dhcp6c</a>(8)</p>
<dl>
<dd>Ralph Droms, Editor 2003 <i>Dynamic Host Configuration Protocol for IPv6 (DHCPv6)</i> <i>RFC 3315</i></dl>
<h2>History</h2>
<p>The command first appeared in WIDE/KAME IPv6 protocol stack kit. </p>
<p> The &#8211;<code>n </code><i>dnsserv</i> command-line option was obsoleted by introducing a configuration file.</p>
<h2>Bugs</h2>
<p>is incomplete and violates DHCPv6 protocol spec, in several aspects. To name a few: </p>
<ol>
<li> it does not assign temporary IPv6 addresses (nor will) </ol>
