---
title: "datagram_poll(9)"
name: "datagram_poll"
section: "9"
letter: "d"
url: "/docs/linux/man/9-datagram_poll/"
description: "datagram_poll – generic datagram poll"
---

<p>datagram_poll &#8211; generic datagram poll</p>
<h2>Synopsis</h2>
<pre><code>unsigned int datagram_poll(struct file *file, struct socket *sock, poll_table *wait);</code></pre>
<h2>Arguments</h2>
<p><i>file</i></p>
<dl>
<dd>
<dd>file struct</dl>
<p> <i>sock</i></p>
<dl>
<dd>socket</dl>
<p> <i>wait</i></p>
<dl>
<dd>poll table</dl>
<h2>Description</h2>
<p>Datagram poll: Again totally generic. This also handles sequenced packet sockets providing the socket receive queue is only ever holding data ready to receive.</p>
<h2>Note</h2>
<p>when you _don&#8217;t_ use this routine for this protocol, and you use a different write policy from <code>sock_writeable</code> then please supply your own write_space callback.</p>
<h2>Copyright</h2>
