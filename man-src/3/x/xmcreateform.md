---
title: "xmcreateform(3)"
name: "xmcreateform"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmcreateform/"
description: "XmCreateForm — The Form widget creation function"
---

<p><code>XmCreateForm</code> &#8212; The Form widget creation function</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Form.h&gt;
<code>Widget XmCreateForm</code>(
<code>Widget parent</code>,
<code>String name</code>,
<code>ArgList arglist</code>,
<code>Cardinal argcount</code>);</pre>
<h2>Description</h2>
<p><code>XmCreateForm</code> creates an instance of a Form widget and returns the associated widget ID.</p>
<dl COMPACT>
<dt><i>parent</i></p>
<dd>Specifies the parent widget ID</p>
<dt><i>name</i></p>
<dd>Specifies the name of the created widget</p>
<dt><i>arglist</i></p>
<dd>Specifies the argument list</p>
<dt><i>argcount</i></p>
<dd>Specifies the number of attribute/value pairs in the argument list (<i>arglist</i>)</dl>
<p> For a complete definition of Form and its associated resources, see <code><a href="/docs/linux/man/3-xmform/">XmForm</a></code>(3).</p>
<h2>Return</h2>
<p>Returns the Form widget ID.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmform/">XmForm</a></code>(3).</p>
