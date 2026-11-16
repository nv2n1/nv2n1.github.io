---
title: "xvselectvideonotify(3)"
name: "xvselectvideonotify"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xvselectvideonotify/"
description: "XvSelectVideoNotify – enable or disable VideoNotify events"
---

<p>XvSelectVideoNotify &#8211; enable or disable VideoNotify events</p>
<h2>Synopsis</h2>
<p><code>#include &lt;X11/extensions/Xvlib.h&gt;</code> </p>
<pre><code>int XvSelectVideoNotify(Display *</code><i>dpy</i><code>, Drawable </code><i>drawable</i><code>, Bool </code><i>onoff</i><code>);</code></pre>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>dpy</i></dt>
<dd>Specifies the connection to the X server.</dd>
<dt><i>drawable</i></dt>
<dd>Defines the drawable in which video activity is to be reported.</dd>
<dt><i>onoff</i></dt>
<dd>Selects whether video notification is enabled or disabled.</dd></dl>
<h2>Description</h2>
<p><code><a href="/docs/linux/man/3-xvselectvideonotify/">XvSelectVideoNotify</a></code>(3) enables or disables <code><a href="/docs/linux/man/3-xvvideonotify/">XvVideoNotify</a></code>(3) events to be reported for video activity in a drawable.</p>
<h2>Return Values</h2>
<dl COMPACT>
<dt>[Success]</dt>
<dd>Returned if <code><a href="/docs/linux/man/3-xvselectvideonotify/">XvSelectVideoNotify</a></code>(3) completed successfully.</dd>
<dt>[XvBadExtension]</dt>
<dd>Returned if the Xv extension is unavailable.</dd>
<dt>[XvBadAlloc]</dt>
<dd>Returned if <code><a href="/docs/linux/man/3-xvselectvideonotify/">XvSelectVideoNotify</a></code>(3) failed to allocate memory to process the request.</dd></dl>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt>[BadDrawable]</dt>
<dd>Generated if the requested drawable does not exist.</dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xvvideonotify/">XvVideoNotify</a></code>(3)</p>
