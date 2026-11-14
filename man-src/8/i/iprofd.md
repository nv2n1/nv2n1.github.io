---
title: "iprofd(8)"
name: "iprofd"
section: "8"
letter: "i"
url: "/docs/linux/man/8-iprofd/"
description: "iprofd – Modem-register daemon"
---

<p>iprofd &#8211; Modem-register daemon</p>
<h2>Synopsis</h2>
<p><code>iprofd</code><i> registerfile</i></p>
<h2>Description</h2>
<p><code>iprofd</code> is used to make the modem-register settings of the isdn-ttys AT-emulator permanent and restore them during boot-time. It is usually started from within a rc-script and puts itself into background. If <i>registerfile</i> already exists at startup, all modem-registers are restored from it&#8217;s contents. After that, <code>iprofd</code> waits for getting a signal from the isdn-subsystem. Every time, a &#8216;AT&amp;W0&#8217; command is given at an isdn-tty the isdn-subsystem sends a SIGIO and <code>iprofd</code> reads the current settings of the modem-registers and stores them into <i>registerfile</i>. </p>
<h2>Author</h2>
<p>Fritz Elfert &lt;fritz [at] isdn4linux.de&gt;</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/4-ttyi/">ttyI</a></i>(4), <i><a href="/docs/linux/man/8-isdnctrl/">isdnctrl</a></i>(8), <i><a href="/docs/linux/man/4-isdninfo/">isdninfo</a></i>(4). </p>
