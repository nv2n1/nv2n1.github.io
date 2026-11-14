---
title: "xrdp-dis(1)"
name: "xrdp-dis"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xrdp-dis/"
description: "xrdp-dis – xrdp disconnect utility"
---

<h2>NAME</h2>
<p> xrdp-dis &#8211; xrdp disconnect utility </p>
<h2>SYNOPSIS</h2>
<p> <code>xrdp-dis</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>xrdp-dis</code> is run with no parameters to disconnect your xrdp session. </p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>DISPLAY</code></p>
<dd> to get the default host and display number. </p>
</dl>
<h2>FILES</h2>
<dl>
<dt><i>/tmp/.xrdp/xrdp_disconnect_display_*</i></p>
<dd> UNIX socket used to communicate with the <code><a href="/docs/linux/man/8-xrdp/">xrdp</a></code>(8) session manager. </p>
</dl>
<h2>KNOWN ISSUES</h2>
<dl>
<dt>This utility doesn&#8217;t support disconnecting xorgxrdp sessions so far.</p>
<dd>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-xrdp/">xrdp</a></code>(8). </p>
<h2>Index</h2>
