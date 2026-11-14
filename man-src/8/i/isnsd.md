---
title: "isnsd(8)"
name: "isnsd"
section: "8"
letter: "i"
url: "/docs/linux/man/8-isnsd/"
description: "isnsd – iSNS server daemon"
---

<p>isnsd &#8211; iSNS server daemon</p>
<h2>Synopsis</h2>
<p><code>isnsd</code> [<code>-f</code>] [<code>-4</code>] [<code>-6</code>] [<code>-c </code><i>filename</i>] [<code>-d </code><i>debug-facility</i>] [<code>&#8211;dump-db</code>] [<code>&#8211;init</code>] </p>
<h2>Description</h2>
<p><code>Isnsd</code> implements the iSNS protocol as defined in RFC 4171. iSNS is a discovery protocol for iSCSI and iFCP.</p>
<h2>Options</h2>
<p>By default, <code>isnsd</code> will take most of its settings from the configuration file <code>/etc/isns/isnsd.conf</code>, with the exception of the following options:</p>
<dl>
<dt><code>&#8211;config</code><i> filename</i>, <code>-c</code><i> filename</i></p>
<dd>This option overrides the default configuration file.</p>
<dt><code>&#8211;foreground</code>,<code>-f</code></p>
<dd>By default, <code>isnsd</code> will put itself into the background. By specifying this option, you can tell it to run in the foreground. Any error messages or debug output will be printed to the console rather than being sent to syslog.</p>
<dt><code>-4</code></p>
<dd>tells <code>isnsd</code> to create an IPv4 socket only. Normally, it defaults to IPv6 (which will accept both IPv4 and IPv6 connections).</p>
<dt><code>-6</code></p>
<dd>tells <code>isnsd</code> explicitly to create an IPv6 socket only. Since it defaults to IPv6 anyway, this is really a no-op.</p>
<dt><code>&#8211;debug</code><i> facility</i>, <code>-d</code><i> facility</i></p>
<dd>enables debugging. Valid facilities are</dl>
<p> <center></p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td><code>socket</code></td>
<td>network send/receive</td>
<td ALIGN=right>
</td>
</tr>
<tr VALIGN=top>
<td><code>auth</code></td>
<td>authentication and security related information</td>
<td ALIGN=right>
</td>
</tr>
<tr VALIGN=top>
<td><code>message</code></td>
<td>iSNS protocol layer</td>
<td ALIGN=right>
</td>
</tr>
<tr VALIGN=top>
<td><code>state</code></td>
<td>database state</td>
<td ALIGN=right>
</td>
</tr>
<tr VALIGN=top>
<td><code>scn</code></td>
<td>SCN (state change notification) messages</td>
<td ALIGN=right>
</td>
</tr>
<tr VALIGN=top>
<td><code>esi</code></td>
<td>ESI (entity status inquiry) messages</td>
<td ALIGN=right>
</td>
</tr>
<tr VALIGN=top>
<td><code>all</code></td>
<td>all of the above</td>
<td ALIGN=right>
</td>
</tr>
</table>
</table>
<p></center> </p>
<dl>
<dt><code>&#8211;dump-db</code></p>
<dd>This is a helper function that will read the database from the file system, and display it in human readable form. When using this option, <code>isnsd</code> will not open any sockets, and terminate immediately after display the database.</p>
<dd>This option is intended to be used by the administrator when suspecting that the database contains bad/inconsistent information.</p>
<dt><code>&#8211;init</code></p>
<dd>This option will create the server&#8217;s authentication key, and the required DSA parameters. The private key is stored in the file specified by the <code>AuthKey</code> option (usually <code>/etc/isns/auth_key</code>). The public portion of the key is written to same directory, with the suffix <code>.pub</code> appended to the key file name.</dl>
<h2>See Also</h2>
<p>RFC 4171, <code><a href="/docs/linux/man/8-isnsadm/">isnsadm</a></code>(8), <code><a href="/docs/linux/man/8-isnsdd/">isnsdd</a></code>(8), <code><a href="/docs/linux/man/5-isns_config/">isns_config</a></code>(5).</p>
<h2>Authors</h2>
<p>Olaf Kirch &lt;olaf.kirch [at] oracle.com&gt;</p>
