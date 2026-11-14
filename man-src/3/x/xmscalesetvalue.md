---
title: "xmscalesetvalue(3)"
name: "xmscalesetvalue"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmscalesetvalue/"
description: "XmScaleSetValue — A Scale function that sets a slider value"
---

<p><code>XmScaleSetValue</code> &#8212; A Scale function that sets a slider value</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Scale.h&gt;
<code>void XmScaleSetValue</code>(
<code>Widget widget</code>,
<code>int value</code>);</pre>
<h2>Description</h2>
<p><code>XmScaleSetValue</code> sets the slider <i>value</i> within the Scale widget.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the Scale widget ID.</p>
<dt><i>value</i></p>
<dd>Specifies the slider position along the scale. This sets the <code>XmNvalue</code> resource.</dl>
<p> For a complete definition of Scale and its associated resources, see <code><a href="/docs/linux/man/3-xmscale/">XmScale</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmscale/">XmScale</a></code>(3).</p>
