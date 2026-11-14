---
title: "arptables-restore(8)"
name: "arptables-restore"
section: "8"
letter: "a"
url: "/docs/linux/man/8-arptables-restore/"
description: "arptables-restore — Restore ARP Tables"
---

<p>arptables-restore &#8212; Restore ARP Tables</p>
<h2>Synopsis</h2>
<p><code>arptables-restore </code></p>
<h2>Description</h2>
<p><code>arptables-restore</code> is used to restore ARP Tables from data specified on STDIN or via a file as first argument. Use I/O redirection provided by your shell to read from a file</p>
<dl>
<dt><code>arptables-restore</code></p>
<dd>flushes (deletes) all previous contents of the respective ARP Table.</dl>
<h2>Bugs</h2>
<p>None known as of arptables-0.0.4 release</p>
<h2>Author</h2>
<p>Jesper Dangaard Brouer &lt;brouer [at] redhat.com&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-arptables-save/">arptables-save</a></code>(8), <code><a href="/docs/linux/man/8-arptables/">arptables</a></code>(8) </p>
