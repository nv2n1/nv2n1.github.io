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
<dt><i>dpy</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>port</i></p>
<dd>Specifies the port for which video is to be stopped.</p>
<dt><i>draw</i></p>
<dd>Specifies the drawable associated with the named port.</dl>
<h2>Description</h2>
<p><code><a href="/docs/linux/man/3-xvstopvideo/">XvStopVideo</a></code>(3) stops active video for the specified port and drawable. If the port is not processing video, or if it is processing video in a different drawable, the request is ignored. When video is stopped a <code><a href="/docs/linux/man/3-xvvideonotify/">XvVideoNotify</a></code>(3) event with detail XvStopped is generated for the associated drawable.</p>
<h2>Return Values</h2>
<dl COMPACT>
<dt>[Success]</p>
<dd>Returned if <code><a href="/docs/linux/man/3-xvstopvideo/">XvStopVideo</a></code>(3) completed successfully.</p>
<dt>[XvBadExtension]</p>
<dd>Returned if the Xv extension is unavailable.</p>
<dt>[XvBadAlloc]</p>
<dd>Returned if <code><a href="/docs/linux/man/3-xvstopvideo/">XvStopVideo</a></code>(3) failed to allocate memory to process the request.</dl>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt>[XvBadPort]</p>
<dd>Generated if the requested port does not exist.</p>
<dt>[BadDrawable]</p>
<dd>Generated if the requested drawable does not exist.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xvgetvideo/">XvGetVideo</a></code>(3), <code><a href="/docs/linux/man/3-xvputvideo/">XvPutVideo</a></code>(3), <code><a href="/docs/linux/man/3-xvvideonotify/">XvVideoNotify</a></code>(3)</p>
