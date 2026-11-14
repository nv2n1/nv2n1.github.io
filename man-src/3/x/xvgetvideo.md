---
title: "xvgetvideo(3)"
name: "xvgetvideo"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xvgetvideo/"
description: "XvGetVideo – capture video from a drawable"
---

<p>XvGetVideo &#8211; capture video from a drawable</p>
<h2>Synopsis</h2>
<p><code>#include &lt;X11/extensions/Xvlib.h&gt;</code> </p>
<pre><code>int XvGetVideo(Display *</code><i>dpy</i><code>, XvPortID </code><i>port</i><code>, Drawable </code><i>d</i><code>, GC </code><i>gc</i><code>,</code>
<code> int </code><i>vx</i><code>, int </code><i>vy</i><code>, unsigned int </code><i>vw</i><code>, unsigned int </code><i>vh</i><code>,</code>
<code> int </code><i>dx</i><code>, int </code><i>dy</i><code>, unsigned int </code><i>dw</i><code>, unsigned int </code><i>dh</i><code>);</code></pre>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>dpy</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>port</i></p>
<dd>Defines the port to which video output is sent.</p>
<dt><i>d</i></p>
<dd>Defines the drawable (window) from which video output is to be obtained.</p>
<dt><i>gc</i></p>
<dd>Defines the graphical context. GC components are: <i>subwindow-mode</i>, <i>clip-x-origin</i>, <i>clip-y-origin</i>, and <i>clip-mask</i>.</p>
<dt><i>vx,vy,vw,vh</i></p>
<dd>Define the location and size of the video region is to be written. <i>vx</i> and <i>vy</i> define the <i>x</i>and <i>y</i> coordinates of the upper-left corner of the video region; <i>vw</i>and <i>vh</i> define the width and height, in pixels, of the video region.</p>
<dt><i>dx,dy,dw,dh</i></p>
<dd>Define the location of the source drawable from which the video image is to be taken. <i>dx</i>and <i>dy</i> define the <i>x</i>and <i>y</i> coordinates of the upper-left corner of the drawable region; <i>dw</i>and <i>dh</i> define the width and height, in pixels, of the drawable region.</dl>
<h2>Description</h2>
<p>outputs video from a drawable. The position and size of the destination rectangle is specified by <i>vx</i>, <i>vy</i>, <i>vw</i>, and <i>vh</i>. The position and size of the source rectangle is specified by <i>dx</i>, <i>dy</i>, <i>dw</i>, and <i>dh</i>. </p>
<p> Drawable data is clipped to the bounds of the drawable, scaled to the requested video region size (or the closest size supported) and clipped to the bounds of the video encoding. The contents of any region not updated with drawable data is undefined. </p>
<p> If video is successfully initiated, an XvVideoNotify event with detail XvStarted is generated for the drawable. If the port is already in use, its video is preempted, and if the new drawable is different than the old, an XvVideoNotify event with detail XvPreempted is generated for the old drawable. If the port is grabbed by another client, this request is ignored, and an XvVideoNotify event with detail XvBusy is generated for the drawable.</p>
<h2>Return Values</h2>
<dl COMPACT>
<dt>[Success]</p>
<dd>Returned if <code><a href="/docs/linux/man/3-xvgetvideo/">XvGetVideo</a></code>(3) completed successfully.</p>
<dt>[XvBadExtension]</p>
<dd>Returned if the Xv extension is unavailable.</p>
<dt>[XvBadAlloc]</p>
<dd>Returned if <code><a href="/docs/linux/man/3-xvgetvideo/">XvGetVideo</a></code>(3) failed to allocate memory to process the request.</dl>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt>[XvBadPort]</p>
<dd>Generated if the requested port does not exist.</p>
<dt>[BadGC]</p>
<dd>Generated if the requested graphics context does not exist.</p>
<dt>[BadDrawable]</p>
<dd>Generated if the requested drawable does not exist.</p>
<dt>[BadAlloc]</p>
<dd>Generated if there were insufficient resources to process the request.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xvgetstill/">XvGetStill</a></code>(3), <code><a href="/docs/linux/man/3-xvputvideo/">XvPutVideo</a></code>(3), <code><a href="/docs/linux/man/3-xvvideonotify/">XvVideoNotify</a></code>(3)</p>
