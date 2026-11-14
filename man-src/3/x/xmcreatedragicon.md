---
title: "xmcreatedragicon(3)"
name: "xmcreatedragicon"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmcreatedragicon/"
description: "XmCreateDragIcon — A Drag and Drop function that creates a DragIcon widget"
---

<p><code>XmCreateDragIcon</code> &#8212; A Drag and Drop function that creates a DragIcon widget</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/DragIcon.h&gt;
<code>Widget XmCreateDragIcon</code>(
<code>Widget widget</code>,
<code>String name</code>,
<code>ArgList arglist</code>,
<code>Cardinal argcount</code>);</pre>
<h2>Description</h2>
<p><code>XmCreateDragIcon</code> creates a DragIcon and returns the associated widget ID.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the ID of the widget that the function uses to access default values for visual attributes of the DragIcon. This widget may be different than the actual parent of the DragIcon.</p>
<dt><i>name</i></p>
<dd>Specifies the name of the DragIcon widget.</p>
<dt><i>arglist</i></p>
<dd>Specifies the argument list.</p>
<dt><i>argcount</i></p>
<dd>Specifies the number of attribute/value pairs in the argument list (<i>arglist</i>).</dl>
<p> For a complete definition of DragIcon and its associated resources, see <code><a href="/docs/linux/man/3-xmdragicon/">XmDragIcon</a></code>(3).</p>
<h2>Return</h2>
<p>The function creates a DragIcon and returns the associated widget ID.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmdragcontext/">XmDragContext</a></code>(3), <code><a href="/docs/linux/man/3-xmdragicon/">XmDragIcon</a></code>(3), and <code><a href="/docs/linux/man/3-xmscreen/">XmScreen</a></code>(3).</p>
