---
title: "xmscalegetvalue(3)"
name: "xmscalegetvalue"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmscalegetvalue/"
description: "XmScaleGetValue — A Scale function that returns the current slider position"
---

<p><code>XmScaleGetValue</code> &#8212; A Scale function that returns the current slider position</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Scale.h&gt;
<code>void XmScaleGetValue</code>(
<code>Widget widget</code>,
<code>int * value_return</code>);</pre>
<h2>Description</h2>
<p><code>XmScaleGetValue</code> returns the current slider position value displayed in the scale.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the Scale widget ID</p>
<dt><i>value_return</i></p>
<dd>Returns the current slider position value</dl>
<p> For a complete definition of Scale and its associated resources, see <code><a href="/docs/linux/man/3-xmscale/">XmScale</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmscale/">XmScale</a></code>(3).</p>
