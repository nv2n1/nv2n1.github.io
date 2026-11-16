---
title: "ip-mroute(8)"
name: "ip-mroute"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ip-mroute/"
description: "ip-mroute – multicast routing cache management"
---

<p>ip-mroute &#8211; multicast routing cache management</p>
<h2>Synopsis</h2>
<p><code>ip mroute show</code> [ [ <code> to </code> ] <i>PREFIX</i> ] [ <code>from</code> <i>PREFIX</i> ] [ <code>iif</code> <i>DEVICE</i> ] [ <code>table</code> <i>TABLE_ID</i> ] </p>
<h2>Description</h2>
<p><code>mroute</code> objects are multicast routing cache entries created by a user-level mrouting daemon (f.e. <code>pimd</code> or <code>mrouted</code> ). Due to the limitations of the current interface to the multicast routing engine, it is impossible to change <code>mroute</code> objects administratively, so we can only display them. This limitation will be removed in the future.</p>
<h3>ip mroute show &#8211; list mroute cache entries</h3>
<dl>
<dt><code>to</code><i> PREFIX </i><code>(default)</code></dt>
<dd>the prefix selecting the destination multicast addresses to list.</dd>
<dt><code>iif</code><i> NAME</i></dt>
<dd>the interface on which multicast packets are received.</dd>
<dt><code>from</code><i> PREFIX</i></dt>
<dd>the prefix selecting the IP source addresses of the multicast route.</dd>
<dt><code>table</code><i> TABLE_ID</i></dt>
<dd>the table id selecting the multicast table. It can be <code>local</code>, <code>main</code>, <code>default</code>, <code>all</code> or a number. </dd>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ip/">ip</a></code>(8) </p>
<h2>Author</h2>
<p>Original Manpage by Michail Litvak &lt;mci [at] owl.openwall.com&gt;</p>
</dl>