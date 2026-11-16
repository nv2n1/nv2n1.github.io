---
title: "xvquerybestsize(3)"
name: "xvquerybestsize"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xvquerybestsize/"
description: "XvQueryBestSize – determine the optimum drawable region size"
---

<p>XvQueryBestSize &#8211; determine the optimum drawable region size</p>
<h2>Synopsis</h2>
<p><code>#include &lt;X11/extensions/Xvlib.h&gt;</code> </p>
<pre><code>int XvQueryBestSize(Display *</code><i>dpy</i><code>, XvPort </code><i>port</i><code>, Bool </code><i>motion</i><code>,</code>
<code> unsigned int </code><i>vw</i><code>, unsigned int </code><i>vh</i><code>,</code>
<code> unsigned int </code><i>dw</i><code>, unsigned int </code><i>dh</i><code>,</code>
<code> unsigned int *</code><i>p_dw</i><code>, unsigned int *</code><i>p_dh</i><code>);</code></pre>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>dpy</i></dt>
<dd>Specifies the connection to the X server.</dd>
<dt><i>port</i></dt>
<dd>Defines the port associated with the display and adaptor for which the optimum size is to be calculated.</dd>
<dt><i>motion</i></dt>
<dd>Specifies <i>True</i> if the destination size needs to support full motion, and <i>False</i> if the destination size need only support still images.</dd>
<dt><i>vw,vh</i></dt>
<dd>Specifies the size of the source video region desired.</dd>
<dt><i>dw,dh</i></dt>
<dd>Specifies the size of the destination drawable region desired.</dd>
<dt><i>p_dw,p_dh</i></dt>
<dd>Pointers to where the closest destination sizes supported by the server are returned.</dd></dl>
<h2>Description</h2>
<p>Some ports may be able to scale incoming or outgoing video. <code><a href="/docs/linux/man/3-xvquerybestsize/">XvQueryBestSize</a></code>(3) returns the size of the closest destination region that is supported by the adaptor. The returned size is guaranteed to be smaller than the requested size if a smaller size is supported.</p>
<h2>Return Values</h2>
<dl COMPACT>
<dt>[Success]</dt>
<dd>Returned if <code><a href="/docs/linux/man/3-xvquerybestsize/">XvQueryBestSize</a></code>(3) completed successfully.</dd>
<dt>[XvBadExtension]</dt>
<dd>Returned if the Xv extension is unavailable.</dd>
<dt>[XvBadAlloc]</dt>
<dd>Returned if <code><a href="/docs/linux/man/3-xvquerybestsize/">XvQueryBestSize</a></code>(3) failed to allocate memory to process the request.</dd></dl>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt>[XvBadPort]</dt>
<dd>Generated if the requested port does not exist. </dd>
</dl>
