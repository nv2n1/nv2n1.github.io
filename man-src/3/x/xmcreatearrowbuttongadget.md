---
title: "xmcreatearrowbuttongadget(3)"
name: "xmcreatearrowbuttongadget"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmcreatearrowbuttongadget/"
description: "XmCreateArrowButtonGadget — The ArrowButtonGadget creation function"
---

<p><code>XmCreateArrowButtonGadget</code> &#8212; The ArrowButtonGadget creation function</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/ArrowBG.h&gt;
<code>Widget XmCreateArrowButtonGadget</code>(
<code>Widget parent</code>,
<code>String name</code>,
<code>ArgList arglist</code>,
<code>Cardinal argcount</code>);</pre>
<h2>Description</h2>
<p><code>XmCreateArrowButtonGadget</code> creates an instance of an ArrowButtonGadget widget and returns the associated widget ID.</p>
<dl COMPACT>
<dt><i>parent</i></dt>
<dd>Specifies the parent widget ID</dd>
<dt><i>name</i></dt>
<dd>Specifies the name of the created widget</dd>
<dt><i>arglist</i></dt>
<dd>Specifies the argument list</dd>
<dt><i>argcount</i></dt>
<dd>Specifies the number of attribute/value pairs in the argument list (<i>arglist</i>)</dd></dl>
<p> For a complete definition of ArrowButtonGadget and its associated resources, see <code><a href="/docs/linux/man/3-xmarrowbuttongadget/">XmArrowButtonGadget</a></code>(3).</p>
<h2>Return</h2>
<p>Returns the ArrowButtonGadget widget ID.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmarrowbuttongadget/">XmArrowButtonGadget</a></code>(3).</p>
