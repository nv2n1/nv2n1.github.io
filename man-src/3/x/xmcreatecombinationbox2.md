---
title: "xmcreatecombinationbox2(3)"
name: "xmcreatecombinationbox2"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmcreatecombinationbox2/"
description: "XmCreateCombinationBox2 — The CombinationBox2 widget creation function"
---

<p><code>XmCreateCombinationBox2</code> &#8212; The CombinationBox2 widget creation function</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/ArrowB.h&gt;
<code>Widget XmCreateCombinationBox2</code>(
<code>Widget parent</code>,
<code>String name</code>,
<code>ArgList arglist</code>,
<code>Cardinal argcount</code>);</pre>
<h2>Description</h2>
<p><code>XmCreateCombinationBox2</code> creates an instance of an ArrowButton widget and returns the associated widget ID.</p>
<dl COMPACT>
<dt><i>parent</i></dt>
<dd>Specifies the parent widget ID</dd>
<dt><i>name</i></dt>
<dd>Specifies the name of the created widget</dd>
<dt><i>arglist</i></dt>
<dd>Specifies the argument list</dd>
<dt><i>argcount</i></dt>
<dd>Specifies the number of attribute/value pairs in the argument list (<i>arglist</i>)</dd></dl>
<p> For a complete definition of ArrowButton and its associated resources, see <code>XmCombinationBox2</code>(3).</p>
<h2>Return</h2>
<p>Returns the CombinationBox2 widget ID.</p>
<h2>Related</h2>
<p><code>XmCombinationBox2</code>(3).</p>
