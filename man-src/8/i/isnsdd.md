---
title: "isnsdd(8)"
name: "isnsdd"
section: "8"
letter: "i"
url: "/docs/linux/man/8-isnsdd/"
description: "isnsdd – iSNS discovery daemon"
---

<p>isnsdd &#8211; iSNS discovery daemon</p>
<h2>Synopsis</h2>
<p><code>isnsdd</code> [<code>-f</code>] [<code>-c </code><i>filename</i>] [<code>-d </code><i>debug-facility</i>] </p>
<h2>Description</h2>
<p><code>Isnsdd</code> is a client side daemon for iSNS. It registers storage nodes and portals with the iSNS service, and refreshes these registrations in a timely manner. </p>
<p> The daemon also registers itself to receive SCN notifications, and processes these. It can be configured to invoke an external helper application for each status notification received. The path name of the helper application can be specified via the <code>SCNCallout</code> option in the configuration file.</p>
<h2>Options</h2>
<p>By default, <code>isnsd</code> will take most of its settings from the configuration file <code>/etc/isns/isnsdd.conf</code>, with the addition of the following command line options:</p>
<dl>
<dt><code>&#8211;config</code><i> filename</i>, <code>-c</code><i> filename</i></p>
<dd>This option overrides the default configuration file.</p>
<dt><code>&#8211;foreground</code>,<code>-f</code></p>
<dd>By default, <code>isnsd</code> will put itself into the background. By specifying this option, you can tell it to run in the foreground. Any error messages or debug output will be printed to the console rather than being sent to syslog.</p>
<dt><code>&#8211;role</code><i> role</i></p>
<dd>This tells the discovery daemon in which capacity is should register itself with the iSNS server. <i>Role</i> can be either <code>initiator</code>, or <code>control</code>. The default is to register as an initiator.</p>
<dd>Registering target nodes needs to use a different mechanism, as the iSCSI target server needs to inform the discovery daemon about each exported target separately. This is not implemented yet.</p>
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
<p></center></p>
<h2>See Also</h2>
<p>RFC 4171, <code><a href="/docs/linux/man/8-isnsd/">isnsd</a></code>(8), <code><a href="/docs/linux/man/8-isnsadm/">isnsadm</a></code>(8), <code><a href="/docs/linux/man/5-isns_config/">isns_config</a></code>(5).</p>
<h2>Authors</h2>
<p>Olaf Kirch &lt;olaf.kirch [at] oracle.com&gt;</p>
