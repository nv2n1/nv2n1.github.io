---
title: "arptables-nft-save(8)"
name: "arptables-nft-save"
section: "8"
letter: "a"
url: "/docs/linux/man/8-arptables-nft-save/"
description: "arptables-save – dump arptables rules to stdout (nft-based)"
---

<p>arptables-save &#8211; dump arptables rules to stdout (nft-based)</p>
<h2>Synopsis</h2>
<p><code>arptables-save</code> [<code>-M</code> <i>modprobe</i>] [<code>-c</code>] </p>
<p> <code>arptables-save</code> [<code>-V</code>]</p>
<h2>Description</h2>
<p><code>arptables-save</code> is used to dump the contents of an ARP Table in easily parseable format to STDOUT. Use I/O-redirection provided by your shell to write to a file.</p>
<dl>
<dt><code>-M</code>, <code>&#8211;modprobe</code> <i>modprobe_program</i></p>
<dd>Specify the path to the modprobe program. By default, arptables-save will inspect /proc/sys/kernel/modprobe to determine the executable&#8217;s path.</p>
<dt><code>-c</code>, <code>&#8211;counters</code></p>
<dd>Include the current values of all packet and byte counters in the output.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>Print version information and exit.</dl>
<h2>Author</h2>
<p>Jesper Dangaard Brouer &lt;brouer [at] redhat.com&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-arptables-restore/">arptables-restore</a></code>(8), <code><a href="/docs/linux/man/8-arptables/">arptables</a></code>(8) </p>
