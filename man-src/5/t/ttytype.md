---
title: "ttytype(5)"
name: "ttytype"
section: "5"
letter: "t"
url: "/docs/linux/man/5-ttytype/"
description: "ttytype – terminal device to default terminal type mapping"
---

<p>ttytype &#8211; terminal device to default terminal type mapping</p>
<h2>Description</h2>
<p>The <i>/etc/ttytype</i> file associates <code><a href="/docs/linux/man/5-termcap/">termcap</a></code>(5)/<code><a href="/docs/linux/man/5-terminfo/">terminfo</a></code>(5) terminal type names with tty lines. Each line consists of a terminal type, followed by whitespace, followed by a tty name (a device name without the <i>/dev/</i>) prefix. </p>
<p> This association is used by the program <code><a href="/docs/linux/man/1-tset/">tset</a></code>(1) to set the environment variable <code>TERM</code> to the default terminal name for the user&#8217;s current tty. </p>
<p> This facility was designed for a traditional time-sharing environment featuring character-cell terminals hardwired to a UNIX minicomputer. It is little used on modern workstation and personal UNIX systems.</p>
<h2>Files</h2>
<dl>
<dt><i>/etc/ttytype</i></p>
<dd>the tty definitions file.</dl>
<h2>Examples</h2>
<p>A typical <i>/etc/ttytype</i> is: </p>
<p> con80x25 tty1 vt320 ttys0</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-termcap/">termcap</a></code>(5), <code><a href="/docs/linux/man/5-terminfo/">terminfo</a></code>(5), <code><a href="/docs/linux/man/8-agetty/">agetty</a></code>(8), <code><a href="/docs/linux/man/8-mingetty/">mingetty</a></code>(8)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
