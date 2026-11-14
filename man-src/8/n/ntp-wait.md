---
title: "ntp-wait(8)"
name: "ntp-wait"
section: "8"
letter: "n"
url: "/docs/linux/man/8-ntp-wait/"
description: "ntp-wait – waits until ntpd is in synchronized state"
---

<p>ntp-wait &#8211; waits until ntpd is in synchronized state</p>
<h2>&nbsp;<wbr></h2>
<h2>Synopsis</h2>
<p><code>ntp-wait [ -fv ] [ -n </code><i>tries</i><code> ] [ -s </code><i>seconds</i><code> ]</code> </p>
<h2>Description</h2>
<p>The <code>ntp-wait</code> program blocks until ntpd is in synchronized state. This can be useful at boot time, to delay the boot sequence until after &quot;ntpd -g&quot; has set the time. </p>
<h2>Command Line Options</h2>
<dl>
<dd>
<dl>
<dt><code>-f</code></p>
<dd>Return a non-zero exit code if the state is unknown.</p>
<dt><code>-n </code><i>tries</i></p>
<dd>Number of tries before giving up. The default is 1000.</p>
<dt><code>-s </code><i>seconds</i></p>
<dd>Seconds to sleep between tries. The default is 6 seconds.</p>
<dt><code>-v</code></p>
<dd>Be verbose.</dl>
</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-ntpd/">ntpd</a>(8) Primary source of documentation: /usr/share/doc/ntp-* This file was automatically generated from HTML source. </p>
