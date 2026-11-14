---
title: "xmcreatescrollbar(3)"
name: "xmcreatescrollbar"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmcreatescrollbar/"
description: "XmCreateScrollBar — The ScrollBar widget creation function"
---

<p><code>XmCreateScrollBar</code> &#8212; The ScrollBar widget creation function</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/ScrollBar.h&gt;
<code>Widget XmCreateScrollBar</code>(
<code>Widget parent</code>,
<code>String name</code>,
<code>ArgList arglist</code>,
<code>Cardinal argcount</code>);</pre>
<h2>Description</h2>
<p><code>XmCreateScrollBar</code> creates an instance of a ScrollBar widget and returns the associated widget ID.</p>
<dl COMPACT>
<dt><i>parent</i></p>
<dd>Specifies the parent widget ID</p>
<dt><i>name</i></p>
<dd>Specifies the name of the created widget</p>
<dt><i>arglist</i></p>
<dd>Specifies the argument list</p>
<dt><i>argcount</i></p>
<dd>Specifies the number of attribute/value pairs in the argument list (<i>arglist</i>)</dl>
<p> For a complete definition of ScrollBar and its associated resources, see <code><a href="/docs/linux/man/3-xmscrollbar/">XmScrollBar</a></code>(3).</p>
<h2>Return</h2>
<p>Returns the ScrollBar widget ID.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmscrollbar/">XmScrollBar</a></code>(3).</p>
