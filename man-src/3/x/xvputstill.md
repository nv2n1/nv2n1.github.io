---
title: "xvputstill(3)"
name: "xvputstill"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xvputstill/"
description: "XvPutStill – write a single frame of video to a drawable"
---

<p>XvPutStill &#8211; write a single frame of video to a drawable</p>
<h2>Synopsis</h2>
<p><code>#include &lt;X11/extensions/Xvlib.h&gt;</code> </p>
<pre><code>int XvPutStill(Display *</code><i>dpy</i><code>, XvPortID </code><i>port</i><code>, Drawable </code><i>d</i><code>, GC </code><i>gc</i><code>,</code>
<code> int </code><i>vx</i><code>, int </code><i>vy</i><code>, unsigned int </code><i>vw</i><code>, unsigned int </code><i>vh</i><code>,</code>
<code> int </code><i>dx</i><code>, int </code><i>dy</i><code>, unsigned int </code><i>dw</i><code>, unsigned int </code><i>dh</i><code>);</code></pre>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>dpy</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>port</i></p>
<dd>Defines the port from which to get the still.</p>
<dt><i>d</i></p>
<dd>Defines the drawable into which the still is to be written. Pixmaps are currently not supported.</p>
<dt><i>gc</i></p>
<dd>Defines the graphical context. GC components are: <i>subwindow-mode</i>, <i>clip-x-origin</i>, <i>clip-y-origin</i>, and <i>clip-mask</i>.</p>
<dt><i>vx,vy,vw,vh</i></p>
<dd>Define the location and size of the video region to be written. <i>vx</i> and <i>vy</i> define the upper-left pixel of the region. <i>vw</i> and <i>vh</i> define the width and height, in pixels, of the region.</p>
<dt><i>dx,dy,dw,dh</i></p>
<dd>Define the location and size of the destination region into which the still image is written. <i>dx</i> and <i>dy</i> define the upper-left corner of the region. <i>dw</i> and <i>dh</i> define the width and height, in pixels, of the region.</dl>
<h2>Description</h2>
<p><code><a href="/docs/linux/man/3-xvputstill/">XvPutStill</a></code>(3) writes a single frame of video to a drawable. The position and size of the source (video) rectangle is specified by <i>vx</i>, <i>vy</i>, <i>vw</i>, and <i>vh</i>. The position and size of the destination (drawable) rectangle is specified by <i>dx</i>, <i>dy</i>, <i>dw</i>, and <i>dh</i>. </p>
<p> Video data is clipped to the bounds of the video encoding, scaled to the requested drawable region size (or the closest size supported) and clipped to the bounds of the drawable. </p>
<p> If the port is grabbed by another client, this request is ignored, and an XvVideoNotify event with detail XvBusy is generated for the drawable. If the port is not receiving a valid video signal a VideoNotify event with detail XvHardError is generated for the drawable.</p>
<h2>Return Values</h2>
<dl COMPACT>
<dt>[Success]</p>
<dd>Returned if <code><a href="/docs/linux/man/3-xvputstill/">XvPutStill</a></code>(3) completed successfully.</p>
<dt>[XvBadExtension]</p>
<dd>Returned if the Xv extension is unavailable.</p>
<dt>[XvBadAlloc]</p>
<dd>Returned if <code><a href="/docs/linux/man/3-xvgetstill/">XvGetStill</a></code>(3) failed to allocate memory to process the request.</dl>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt>[XvBadPort]</p>
<dd>Generated if the requested port does not exist.</p>
<dt>[BadDrawable]</p>
<dd>Generated if the requested drawable does not exist.</p>
<dt>[BadGC]</p>
<dd>Generated if the requested graphics context does not exist.</p>
<dt>[BadAlloc]</p>
<dd>Generated if there were insufficient resources to process the request.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xvputvideo/">XvPutVideo</a></code>(3), <code><a href="/docs/linux/man/3-xvgetstill/">XvGetStill</a></code>(3), <code><a href="/docs/linux/man/3-xvvideonotify/">XvVideoNotify</a></code>(3)</p>
