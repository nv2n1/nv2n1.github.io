---
title: "knopmd(8)"
name: "knopmd"
section: "8"
letter: "k"
url: "/docs/linux/man/8-knopmd/"
description: "knopmd – separates iptables messages from all other kernel messages."
---

<p><code>knopmd</code> &#8211; separates iptables messages from all other kernel messages.</p>
<h2>Synopsis</h2>
<p><code>knopmd</code></p>
<h2>Description</h2>
<p><code>knopmd</code> reads messages from the /var/lib/fwknop/fwknopfifo named pipe and prints any firewall related log messages to the fwknop data file &quot;/var/log/fwknop/fwdata&quot;. <code>Note</code> that knopmd is only used in the legacy port knocking mode, and the default authentication/authorization method used by fwknop is Single Packet Authorization (SPA). <code>fwknop</code> cannot detect port knocking sequences without knopmd running on the machine. <code>knopmd</code> references the fwknop.conf configuration file which by default is located at /etc/fwknop/fwknop.conf, but a different path can be specified on the command line. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-fwknop/">fwknop</a></code>(8), <code><a href="/docs/linux/man/8-fwknopd/">fwknopd</a></code>(8), <code><a href="/docs/linux/man/8-knopwatchd/">knopwatchd</a></code>(8),</p>
<h2>Author</h2>
<p>Michael Rash (mbr [at] cipherdyne.org)</p>
<h2>Distribution</h2>
<p><code>knopmd</code> is distributed under the GNU General Public License (GPL), and the latest version may be downloaded from <code><a rel="nofollow" href="http://www.cipherdyne.org">http://www.cipherdyne.org</a></code></p>
