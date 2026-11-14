---
title: "ip-maddress(8)"
name: "ip-maddress"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ip-maddress/"
description: "ip-maddress – multicast addresses management"
---

<p>ip-maddress &#8211; multicast addresses management</p>
<h2>Synopsis</h2>
<pre><code>ip

[ OPTIONS ]

maddress

{ COMMAND |

    help }
</code></pre>
<p> <code>ip maddress</code> [ <code>add</code> | <code>del</code> ] <i>MULTIADDR</i><code> dev </code><i>NAME</i><br />
 <code>ip maddress show</code> [ <code>dev</code> <i>NAME</i> ] </p>
<h2>Description</h2>
<p><code>maddress</code> objects are multicast addresses.</p>
<h3>ip maddress show &#8211; list multicast addresses</h3>
<dl>
<dt><code>dev</code><i> NAME </i><code>(default)</code></p>
<dd>the device name.</p>
<dt><code>ip maddress add &#8211; add a multicast address</code></p>
<dd>
<dt><code>ip maddress delete &#8211; delete a multicast address</code></p>
<dd>These commands attach/detach a static link-layer multicast address to listen on the interface. Note that it is impossible to join protocol multicast groups statically. This command only manages link-layer addresses.</p>
<dl>
<dd>
<dl>
<dt><code>address</code><i> LLADDRESS </i><code>(default)</code></p>
<dd>the link-layer multicast address.</p>
<dt><code>dev</code><i> NAME</i></p>
<dd>the device to join/leave this multicast address.</dl>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ip/">ip</a></code>(8) </p>
<h2>Author</h2>
<p>Original Manpage by Michail Litvak &lt;mci [at] owl.openwall.com&gt;</p>
