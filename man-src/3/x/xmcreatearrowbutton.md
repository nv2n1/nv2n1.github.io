---
title: "xmcreatearrowbutton(3)"
name: "xmcreatearrowbutton"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmcreatearrowbutton/"
description: "XmCreateArrowButton — The ArrowButton widget creation function"
---

<p><code>XmCreateArrowButton</code> &#8212; The ArrowButton widget creation function</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/ArrowB.h&gt;
<code>Widget XmCreateArrowButton</code>(
<code>Widget parent</code>,
<code>String name</code>,
<code>ArgList arglist</code>,
<code>Cardinal argcount</code>);</pre>
<h2>Description</h2>
<p><code>XmCreateArrowButton</code> creates an instance of an ArrowButton widget and returns the associated widget ID.</p>
<dl COMPACT>
<dt><i>parent</i></p>
<dd>Specifies the parent widget ID</p>
<dt><i>name</i></p>
<dd>Specifies the name of the created widget</p>
<dt><i>arglist</i></p>
<dd>Specifies the argument list</p>
<dt><i>argcount</i></p>
<dd>Specifies the number of attribute/value pairs in the argument list (<i>arglist</i>)</dl>
<p> For a complete definition of ArrowButton and its associated resources, see <code><a href="/docs/linux/man/3-xmarrowbutton/">XmArrowButton</a></code>(3).</p>
<h2>Return</h2>
<p>Returns the ArrowButton widget ID.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmarrowbutton/">XmArrowButton</a></code>(3).</p>
