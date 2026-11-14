---
title: "ipcalc(1)"
name: "ipcalc"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ipcalc/"
description: "ipcalc – perform simple manipulation of IP addresses"
---

<h2>NAME</h2>
<p> ipcalc &#8211; perform simple manipulation of IP addresses</p>
<h2>SYNOPSIS</h2>
<p> <code>ipcalc</code> [<i>OPTION</i>]&#8230; &lt;<code>IP address</code>&gt;[<i>/prefix</i>] [<i>netmask</i>] </p>
<h2>DESCRIPTION</h2>
<p> <code>ipcalc</code> provides a simple way to calculate IP information for a host. The various options specify what information <code>ipcalc</code> should display on standard out. Multiple options may be specified. An IP address to operate on must always be specified. Most operations also require a netmask or a CIDR prefix as well. </p>
<h2>OPTIONS</h2>
<dl>
<dt>
<dt><code>-c</code>, <code>&#8211;check</code></p>
<dd>
<dd> Validate the IP address under the specified family. If no address family is specified, IPv4 is assumed. </p>
<dt><code>-4</code>, <code>&#8211;ipv4</code></p>
<dd> Specify IPv4 address family (default). </p>
<dt><code>-6</code>, <code>&#8211;ipv6</code></p>
<dd> Specify IPv6 address family. </p>
<dt><code>-b</code>, <code>&#8211;broadcast</code></p>
<dd> Display the broadcast address for the given IP address and netmask. </p>
<dt><code>-h</code>, <code>&#8211;hostname</code></p>
<dd> Display the hostname for the given IP address. </p>
<dt><code>-m</code>, <code>&#8211;netmask</code></p>
<dd> Calculate the netmask for the given IP address. It assumes that the IP address is in a complete class A, B, or C network. Many networks do not use the default netmasks, in which case an inappropriate value will be returned. </p>
<dt><code>-p</code>, <code>&#8211;prefix</code></p>
<dd> Show the prefix for the given mask/IP address. </p>
<dt><code>-n</code>, <code>&#8211;network</code></p>
<dd> Display the network address for the given IP address and netmask. </p>
<dt><code>-s</code>, <code>&#8211;silent</code></p>
<dd> Don&#8217;t ever display error messages. </p>
</dl>
<h2>AUTHORS</h2>
<pre><code>
Erik Troan&lt;ewt[at] redhat.com&gt;
    Preston Brown&lt;pbrown[at] redhat.com&gt;

        IPv6 supported wedged in by David Cantrell&lt;dcantrell[at] redhat.com&gt;</code></pre>
</dl>
<h2>REPORTING BUGS</h2>
<p> Report bugs at <a rel="nofollow" href="http://bugzilla.redhat.com/">http://bugzilla.redhat.com/</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 1997-2008 Red Hat, Inc.<br />
 This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>Index</h2>
