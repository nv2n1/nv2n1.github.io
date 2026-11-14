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
<dt><i>parent</i></p>
<dd>Specifies the parent widget ID</p>
<dt><i>name</i></p>
<dd>Specifies the name of the created widget</p>
<dt><i>arglist</i></p>
<dd>Specifies the argument list</p>
<dt><i>argcount</i></p>
<dd>Specifies the number of attribute/value pairs in the argument list (<i>arglist</i>)</dl>
<p> For a complete definition of ArrowButtonGadget and its associated resources, see <code><a href="/docs/linux/man/3-xmarrowbuttongadget/">XmArrowButtonGadget</a></code>(3).</p>
<h2>Return</h2>
<p>Returns the ArrowButtonGadget widget ID.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmarrowbuttongadget/">XmArrowButtonGadget</a></code>(3).</p>
