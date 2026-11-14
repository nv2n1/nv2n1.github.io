---
title: "xvungrabport(3)"
name: "xvungrabport"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xvungrabport/"
description: "XvUngrabPort – release port grabbed for video operation"
---

<p>XvUngrabPort &#8211; release port grabbed for video operation</p>
<h2>Synopsis</h2>
<p><code>#include &lt;X11/extensions/Xvlib.h&gt;</code> </p>
<pre><code>int XvUngrabPort(Display *</code><i>dpy</i><code>, XvPortID </code><i>port</i><code>, Time </code><i>time</i><code>);</code></pre>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>dpy</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>port</i></p>
<dd>Specifies the port to be released. If the port had not been previously grabbed, the request is ignored.</p>
<dt><i>time</i></p>
<dd>Specifies the request timestamp.</dl>
<h2>Description</h2>
<p><code><a href="/docs/linux/man/3-xvungrabport/">XvUngrabPort</a></code>(3)<br />
&nbsp;<wbr>releases a grabbed port.&nbsp;<wbr>&nbsp;<wbr>If&nbsp;<wbr><i>time</i>&nbsp;<wbr>specifies a time before the last <code><a href="/docs/linux/man/3-xvgrabport/">XvGrabPort</a></code>(3) was executed, the request is ignored.</p>
<h2>Return Values</h2>
<dl COMPACT>
<dt>[Success]</p>
<dd>Returned if <code><a href="/docs/linux/man/3-xvungrabport/">XvUngrabPort</a></code>(3) completed successfully.</p>
<dt>[XvBadExtension]</p>
<dd>Returned if the Xv extension is unavailable.</p>
<dt>[XvBadAlloc]</p>
<dd>Returned if <code><a href="/docs/linux/man/3-xvungrabport/">XvUngrabPort</a></code>(3) failed to allocate memory to process the request.</dl>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt>[XvBadPort]</p>
<dd>Generated if the requested port does not exist.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xvgrabport/">XvGrabPort</a></code>(3)</p>
