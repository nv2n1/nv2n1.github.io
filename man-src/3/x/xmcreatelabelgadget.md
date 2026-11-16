---
title: "xmcreatelabelgadget(3)"
name: "xmcreatelabelgadget"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmcreatelabelgadget/"
description: "XmCreateLabelGadget — The LabelGadget creation function"
---

<p><code>XmCreateLabelGadget</code> &#8212; The LabelGadget creation function</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/LabelG.h&gt;
<code>Widget XmCreateLabelGadget</code>(
<code>Widget parent</code>,
<code>String name</code>,
<code>ArgList arglist</code>,
<code>Cardinal argcount</code>);</pre>
<h2>Description</h2>
<p><code>XmCreateLabelGadget</code> creates an instance of a LabelGadget widget and returns the associated widget ID.</p>
<dl COMPACT>
<dt><i>parent</i></dt>
<dd>Specifies the parent widget ID</dd>
<dt><i>name</i></dt>
<dd>Specifies the name of the created widget</dd>
<dt><i>arglist</i></dt>
<dd>Specifies the argument list</dd>
<dt><i>argcount</i></dt>
<dd>Specifies the number of attribute/value pairs in the argument list (<i>arglist</i>)</dd></dl>
<p> For a complete definition of LabelGadget and its associated resources, see <code><a href="/docs/linux/man/3-xmlabelgadget/">XmLabelGadget</a></code>(3).</p>
<h2>Return</h2>
<p>Returns the LabelGadget widget ID.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmlabelgadget/">XmLabelGadget</a></code>(3).</p>
