---
title: "rdistd(8)"
name: "rdistd"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rdistd/"
description: "rdistd – remote file distribution server program"
---

<p>rdistd &#8211; remote file distribution server program</p>
<h2>Synopsis</h2>
<p><code>rdistd</code> <code>-S</code> [ <code>-D</code> ] </p>
<p> <code>rdistd</code> <code>-V</code></p>
<h2>Description</h2>
<p><i>Rdistd</i> is the server program for the <i>rdist</i> command. It is normally run by <i>rdist</i> via <i><a href="/docs/linux/man/1-rsh/">rsh</a>(1).</i> </p>
<p> The <code>-S</code> argument must be specified. The option is required so that <i>rdistd</i> is not accidentally started since it normally resides somewhere in a normal user&#8217;s <code>$PATH.</code></p>
<h2>Options</h2>
<dl>
<dt><code>-D</code></p>
<dd>Enable debugging messages. Messages are logged via <i><a href="/docs/linux/man/3-syslog/">syslog</a>(3).</i></p>
<dt><code>-V</code></p>
<dd>Print version information and exit.</dl>
<h2>Files</h2>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-rdist/">rdist</a>(1), <a href="/docs/linux/man/1-rsh/">rsh</a>(1)</p>
<h2>Bugs</h2>
