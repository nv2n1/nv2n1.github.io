---
title: "xvgrabport(3)"
name: "xvgrabport"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xvgrabport/"
description: "XvGrabPort – lock port for exclusive use by client"
---

<p>XvGrabPort &#8211; lock port for exclusive use by client</p>
<h2>Synopsis</h2>
<p><code>#include &lt;X11/extensions/Xvlib.h&gt;</code> </p>
<pre><code>int XvGrabPort(Display *</code><i>dpy</i><code>, XvPortID </code><i>port</i><code>, Time </code><i>time</i><code>);</code></pre>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>dpy</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>port</i></p>
<dd>Defines the port to be grabbed.</p>
<dt><i>time</i></p>
<dd>Specifies the request timestamp.</dl>
<h2>Description</h2>
<p><code><a href="/docs/linux/man/3-xvgrabport/">XvGrabPort</a></code>(3) grabs a port. Once a client grabs a port, only that client can make video requests to that port. </p>
<p> If the time is before the current port time, the XvGrabPort request is ignored and XvInvalidTime is returned. If the port is already grabbed by another client, XvAlreadyGrabbed is returned. Otherwise it returns a status of <i>Success</i>. The port time is updated when the following requests are processed: <code><a href="/docs/linux/man/3-xvgrabport/">XvGrabPort</a></code>(3), <code><a href="/docs/linux/man/3-xvungrabport/">XvUngrabPort</a></code>(3), <code><a href="/docs/linux/man/3-xvputvideo/">XvPutVideo</a></code>(3), <code><a href="/docs/linux/man/3-xvputstill/">XvPutStill</a></code>(3), <code><a href="/docs/linux/man/3-xvgetvideo/">XvGetVideo</a></code>(3), <code><a href="/docs/linux/man/3-xvgetstill/">XvGetStill</a></code>(3). </p>
<p> If the port is actively processing video for another client, the video is preempted, and an XvVideoNotify event with detail XvPreempted is generated for its drawable.</p>
<h2>Return Values</h2>
<dl COMPACT>
<dt>[Success]</p>
<dd>Returned if <code><a href="/docs/linux/man/3-xvgrabport/">XvGrabPort</a></code>(3) completed successfully.</p>
<dt>[XvInvalidTime]</p>
<dd>Returned if requested time is older than the current port time.</p>
<dt>[XvAlreadyGrabbed]</p>
<dd>Returned if the port is already grabbed by another client.</p>
<dt>[XvBadExtension]</p>
<dd>Returned if the Xv extension is unavailable.</p>
<dt>[XvBadAlloc]</p>
<dd>Returned if <code><a href="/docs/linux/man/3-xvgrabport/">XvGrabPort</a></code>(3) failed to allocate memory to process the request.</dl>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt>[XvBadPort]</p>
<dd>Generated if the requested port does not exist.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xvungrabport/">XvUngrabPort</a></code>(3), <code><a href="/docs/linux/man/3-xvvideonotify/">XvVideoNotify</a></code>(3)</p>
