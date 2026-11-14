---
title: "notifier(7)"
name: "notifier"
section: "7"
letter: "n"
url: "/docs/linux/man/7-notifier/"
description: "notifier – cups notification interface"
---

<p>notifier &#8211; cups notification interface</p>
<h2>Synopsis</h2>
<p><code>notifier</code> <i>recipient</i> [ <i>user-data</i> ]</p>
<h2>Description</h2>
<p>The CUPS notifier interface provides a standard method for adding support for new event notification methods to CUPS. Each notifier delivers one or more IPP events from the standard input to the specified recipient. </p>
<p> Notifiers <code>MUST</code> read IPP messages from the standard input using the <code>ippNew</code>() and <code>ippReadFile</code>() functions and exit on error. Notifiers are encouraged to exit after a suitable period of inactivity, however they may exit after reading the first message or stay running until an error is seen. Notifiers inherit the environment and can use the logging mechanism documented in <code><a href="/docs/linux/man/7-filter/">filter</a></code>(7).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-cupsd/">cupsd</a></code>(8), <code><a href="/docs/linux/man/7-filter/">filter</a></code>(7), CUPS Online Help (<a rel="nofollow" href="http://localhost:631/help)">http://localhost:631/help)</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2021-2022 by OpenPrinting.</p>
