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
<dt><i>dpy</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>drawable</i></p>
<dd>Defines the drawable in which video activity is to be reported.</p>
<dt><i>onoff</i></p>
<dd>Selects whether video notification is enabled or disabled.</dl>
<h2>Description</h2>
<p><code><a href="/docs/linux/man/3-xvselectvideonotify/">XvSelectVideoNotify</a></code>(3) enables or disables <code><a href="/docs/linux/man/3-xvvideonotify/">XvVideoNotify</a></code>(3) events to be reported for video activity in a drawable.</p>
<h2>Return Values</h2>
<dl COMPACT>
<dt>[Success]</p>
<dd>Returned if <code><a href="/docs/linux/man/3-xvselectvideonotify/">XvSelectVideoNotify</a></code>(3) completed successfully.</p>
<dt>[XvBadExtension]</p>
<dd>Returned if the Xv extension is unavailable.</p>
<dt>[XvBadAlloc]</p>
<dd>Returned if <code><a href="/docs/linux/man/3-xvselectvideonotify/">XvSelectVideoNotify</a></code>(3) failed to allocate memory to process the request.</dl>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt>[BadDrawable]</p>
<dd>Generated if the requested drawable does not exist.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xvvideonotify/">XvVideoNotify</a></code>(3)</p>
