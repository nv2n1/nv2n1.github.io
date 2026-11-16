---
title: "net2kiss(8)"
name: "net2kiss"
section: "8"
letter: "n"
url: "/docs/linux/man/8-net2kiss/"
description: "net2kiss – convert a network AX.25 driver to a KISS stream on a pseudo-tty"
---

<p>net2kiss &#8211; convert a network AX.25 driver to a KISS stream on a pseudo-tty</p>
<h2>Synopsis</h2>
<p><code>net2kiss [-sfzva] [-i ifname] ptyname</code></p>
<h2>Description</h2>
<p><code>net2kiss</code> takes AX.25 packets from an AX.25 kernel network interface and converts them into a KISS data stream via a pseudo-tty.</p>
<h2>Parameters</h2>
<dl>
<dt><code>ptyname</code></dt>
<dd>specifies the path to the pseudo-tty. If you use the special name &quot;/dev/ptmx&quot;, then a Unix98-PTY pair is used; the pty name is written to stdout.</dd></dl>
<h2>Options</h2>
<dl>
<dt><code>-i ifname</code></dt>
<dd>specifies the name of the kernel AX.25 network interface. The default is bc0.</dd>
<dt><code>-s</code></dt>
<dd>tells net2kiss to search by itself for a free pseudoterminal, open the master side and create a symlink named by -p to the slave side.</dd>
<dt><code>-f</code></dt>
<dd>can be used in conjunction with -s to force the creation of the symlink even if the target file does already exist. *DANGEROUS*</dd>
<dt><code>-v</code></dt>
<dd>Verbose output. Displays error messages during operation and decoded packets to stdout.</dd>
<dt><code>-z</code></dt>
<dd>put the network interface into promiscious mode.</dd>
<dt><code>-a</code></dt>
<dd>receive every packet instead of only AX.25 from the kernel AX.25 network interface.</dd></dl>
<h2>Bugs</h2>
<p>None known.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ifconfig/">ifconfig</a></code>(8), <code><a href="/docs/linux/man/8-kissattach/">kissattach</a></code>(8).</p>
<h2>Authors</h2>
<p>Thomas M. Sailer, HB9JNX/AE4WA, &lt;t.sailer [at] alumni.ethz.ch&gt;</p>
