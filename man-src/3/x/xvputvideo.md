---
title: "xvputvideo(3)"
name: "xvputvideo"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xvputvideo/"
description: "XvPutVideo – write video into a drawable"
---

<p>XvPutVideo &#8211; write video into a drawable</p>
<h2>Synopsis</h2>
<p><code>#include &lt;X11/extensions/Xvlib.h&gt;</code> </p>
<pre><code>int XvPutVideo(Display *</code><i>dpy</i><code>, XvPortID </code><i>port</i><code>, Drawable </code><i>d</i><code>, GC </code><i>gc</i><code>,</code>
<code> int </code><i>vx</i><code>, int </code><i>vy</i><code>, unsigned int </code><i>vw</i><code>, unsigned int </code><i>vh</i><code>,</code>
<code> int </code><i>dx</i><code>, int </code><i>dy</i><code>, unsigned int </code><i>dw</i><code>, unsigned int </code><i>dh</i><code>);</code></pre>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>dpy</i></dt>
<dd>Specifies the connection to the X server.</dd>
<dt><i>port</i></dt>
<dd>Defines the port from which to get video.</dd>
<dt><i>d</i></dt>
<dd>Defines the drawable (window) into which video is to be written.</dd>
<dt><i>gc</i></dt>
<dd>Defines the graphical context. GC components are: <i>subwindow-mode</i>, <i>clip-x-origin</i>, <i>clip-y-origin</i>, and <i>clip-mask</i>.</dd>
<dt><i>vx,vy,vw,vh</i></dt>
<dd>Define the size and location of the source (video) region to be written. <i>vx</i> and <i>vy</i> define the upper-left pixel of the region. <i>vw</i> and <i>vh</i> define the width and height, in pixels, of the region.</dd>
<dt><i>dx,dy,dw,dh</i></dt>
<dd>Define the location and size of the destination (drawable) region into which the video image is written. <i>dx</i> and <i>dy</i> define the upper-left pixel of the region. <i>dw</i> and <i>dh</i> define the width and height, in pixels, of the region.</dd></dl>
<h2>Description</h2>
<p>XvPutVideo writes video into a drawable. The position and size of the source (video) rectangle is specified by <i>vx</i>, <i>vy</i>, <i>vw</i>, and <i>vh</i>. The position and size of the destination (drawable) rectangle is specified by <i>dx</i>, <i>dy</i>, <i>dw</i>, and <i>dh</i>. </p>
<p> Video data is clipped to the bounds of the video encoding, scaled to the requested drawable region size (or the closest size supported) and clipped to the bounds of the drawable. </p>
<p> If video is successfully initiated, an XvVideoNotify event with detail XvStarted is generated for the drawable. If the port is already in use, its video is preempted, and if the new drawable is different than the old, an XvVideoNotify event with detail XvPreempted is generated for the old drawable. If the port is grabbed by another client, this request is ignored, and an XvVideoNotify event with detail XvBusy is generated for the drawable. If the port is not receiving a valid video signal or if the video signal is interrupted while video is active a VideoNotify event with detail XvHardError is generated for the drawable.</p>
<h2>Return Values</h2>
<dl COMPACT>
<dt>[Success]</dt>
<dd>Returned if <code><a href="/docs/linux/man/3-xvputvideo/">XvPutVideo</a></code>(3) completed successfully.</dd>
<dt>[XvBadExtension]</dt>
<dd>Returned if the Xv extension is unavailable.</dd>
<dt>[XvBadAlloc]</dt>
<dd>Returned if there were insufficient resources to process the request.</dd></dl>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt>[XvBadPort]</dt>
<dd>Generated if the requested port does not exist.</dd>
<dt>[BadDrawable]</dt>
<dd>Generated if the requested drawable does not exist.</dd>
<dt>[BadGC]</dt>
<dd>Generated if the requested graphics context does not exist.</dd>
<dt>[BadAlloc]</dt>
<dd>Generated if there were insufficient resources to process the request.</dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xvputstill/">XvPutStill</a></code>(3), <code><a href="/docs/linux/man/3-xvgetvideo/">XvGetVideo</a></code>(3), <code><a href="/docs/linux/man/3-xvvideonotify/">XvVideoNotify</a></code>(3)</p>
