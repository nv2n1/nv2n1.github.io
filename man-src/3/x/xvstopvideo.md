---
title: "xvstopvideo(3)"
name: "xvstopvideo"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xvstopvideo/"
description: "XvStopVideo – stop active video"
---

<p>XvStopVideo &#8211; stop active video</p>
<h2>Synopsis</h2>
<p><code>#include &lt;X11/extensions/Xvlib.h&gt;</code> </p>
<pre><code>int XvStopVideo(Display *</code><i>dpy</i><code>, XvPortID </code><i>port</i><code>, Drawable </code><i>draw</i><code>);</code></pre>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>dpy</i></dt>
<dd>Specifies the connection to the X server.</dd>
<dt><i>port</i></dt>
<dd>Specifies the port for which video is to be stopped.</dd>
<dt><i>draw</i></dt>
<dd>Specifies the drawable associated with the named port.</dd></dl>
<h2>Description</h2>
<p><code><a href="/docs/linux/man/3-xvstopvideo/">XvStopVideo</a></code>(3) stops active video for the specified port and drawable. If the port is not processing video, or if it is processing video in a different drawable, the request is ignored. When video is stopped a <code><a href="/docs/linux/man/3-xvvideonotify/">XvVideoNotify</a></code>(3) event with detail XvStopped is generated for the associated drawable.</p>
<h2>Return Values</h2>
<dl COMPACT>
<dt>[Success]</dt>
<dd>Returned if <code><a href="/docs/linux/man/3-xvstopvideo/">XvStopVideo</a></code>(3) completed successfully.</dd>
<dt>[XvBadExtension]</dt>
<dd>Returned if the Xv extension is unavailable.</dd>
<dt>[XvBadAlloc]</dt>
<dd>Returned if <code><a href="/docs/linux/man/3-xvstopvideo/">XvStopVideo</a></code>(3) failed to allocate memory to process the request.</dd></dl>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt>[XvBadPort]</dt>
<dd>Generated if the requested port does not exist.</dd>
<dt>[BadDrawable]</dt>
<dd>Generated if the requested drawable does not exist.</dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xvgetvideo/">XvGetVideo</a></code>(3), <code><a href="/docs/linux/man/3-xvputvideo/">XvPutVideo</a></code>(3), <code><a href="/docs/linux/man/3-xvvideonotify/">XvVideoNotify</a></code>(3)</p>
