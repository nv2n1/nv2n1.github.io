---
title: "xmtabstackxytowidget(3)"
name: "xmtabstackxytowidget"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtabstackxytowidget/"
description: "XmTabStackXYToWidget — A TabStack function that converts a pixel coordinate to the widget ID of the tab occupying that space"
---

<p><code>XmTabStackXYToWidget</code> &#8212; A TabStack function that converts a pixel coordinate to the widget ID of the tab occupying that space</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/TabStack.h&gt;
<code>Widget XmTabStackXYToWidget</code>(
<code>Widget widget</code>,
<code>int x,
int y);
</code></pre>
<h2>Description</h2>
<p><code>XmTabStackXYToWidget</code> converts an X/Y pixel coordinate in the window if TabStack to the widget ID of the tab occupying that space.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the TabStack widget ID</p>
<dt><i>x</i></p>
<dd>Specifies X coordinate to convert</p>
<dt><i>y</i></p>
<dd>Specifies Y coordinate to convert</dl>
<h2>Return</h2>
<p>Returns the widget ID of the tab occuring in the cpecified coordinate.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtabstack/">XmTabStack</a></code>(3).</p>
