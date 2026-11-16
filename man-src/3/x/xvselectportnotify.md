---
title: "xvselectportnotify(3)"
name: "xvselectportnotify"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xvselectportnotify/"
description: "XvSelectPortNotify – enable or disable XvPortNotify events"
---

<p>XvSelectPortNotify &#8211; enable or disable XvPortNotify events</p>
<h2>Synopsis</h2>
<p><code>#include &lt;X11/extensions/Xvlib.h&gt;</code> </p>
<pre><code>int XvSelectPortNotify(Display *</code><i>dpy</i><code>, XvPortID </code><i>port</i><code>, Bool </code><i>onoff</i><code>);</code></pre>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>dpy</i></dt>
<dd>Specifies the connection to the X server.</dd>
<dt><i>port</i></dt>
<dd>Specifies the port for which PortNotify events are to be generated when its attributes are changed using <code><a href="/docs/linux/man/3-xvsetportattribute/">XvSetPortAttribute</a></code>(3)</dd>
<dt><i>onoff</i></dt>
<dd>Specifies whether notification is to be enabled or disabled.</dd></dl>
<h2>Description</h2>
<p><code><a href="/docs/linux/man/3-xvselectportnotify/">XvSelectPortNotify</a></code>(3) enables or disables PortNotify event delivery to the requesting client. <code><a href="/docs/linux/man/3-xvportnotify/">XvPortNotify</a></code>(3) events are generated when port attributes are changed using <code><a href="/docs/linux/man/3-xvsetportattribute/">XvSetPortAttribute</a></code>(3).</p>
<h2>Return Values</h2>
<dl COMPACT>
<dt>[Success]</dt>
<dd>Returned if <code><a href="/docs/linux/man/3-xvselectportnotify/">XvSelectPortNotify</a></code>(3) completed successfully.</dd>
<dt>[XvBadExtension]</dt>
<dd>Returned if the Xv extension is unavailable.</dd>
<dt>[XvBadAlloc]</dt>
<dd>Returned if <code><a href="/docs/linux/man/3-xvselectportnotify/">XvSelectPortNotify</a></code>(3) failed to allocate memory to process the request.</dd></dl>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt>[XvBadPort]</dt>
<dd>Generated if the requested port does not exist.</dd></dl>
<h2>See Also</h2>
<p><code>XvSetPortNotify</code>(3), <code><a href="/docs/linux/man/3-xvsetportattribute/">XvSetPortAttribute</a></code>(3), <code><a href="/docs/linux/man/3-xvportnotify/">XvPortNotify</a></code>(3)</p>
