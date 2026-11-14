---
title: "xmcreatecascadebuttongadget(3)"
name: "xmcreatecascadebuttongadget"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmcreatecascadebuttongadget/"
description: "XmCreateCascadeButtonGadget — The CascadeButtonGadget creation function"
---

<p><code>XmCreateCascadeButtonGadget</code> &#8212; The CascadeButtonGadget creation function</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/CascadeBG.h&gt;
<code>Widget XmCreateCascadeButtonGadget</code>(
<code>Widget parent</code>,
<code>String name</code>,
<code>ArgList arglist</code>,
<code>Cardinal argcount</code>);</pre>
<h2>Description</h2>
<p><code>XmCreateCascadeButtonGadget</code> creates an instance of a CascadeButtonGadget and returns the associated widget ID.</p>
<dl COMPACT>
<dt><i>parent</i></p>
<dd>Specifies the parent widget ID. The parent must be a RowColumn widget.</p>
<dt><i>name</i></p>
<dd>Specifies the name of the created widget</p>
<dt><i>arglist</i></p>
<dd>Specifies the argument list</p>
<dt><i>argcount</i></p>
<dd>Specifies the number of attribute/value pairs in the argument list (<i>arglist</i>)</dl>
<p> For a complete definition of CascadeButtonGadget and its associated resources, see <code><a href="/docs/linux/man/3-xmcascadebuttongadget/">XmCascadeButtonGadget</a></code>(3).</p>
<h2>Return</h2>
<p>Returns the CascadeButtonGadget widget ID.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmcascadebuttongadget/">XmCascadeButtonGadget</a></code>(3).</p>
