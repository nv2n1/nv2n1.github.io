---
title: "xmcreatedropdown(3)"
name: "xmcreatedropdown"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmcreatedropdown/"
description: "XmCreateDropDown — The default DropDown widget creation function"
---

<p><code>XmCreateDropDown</code> &#8212; The default DropDown widget creation function</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/DropDown.h&gt;
<code>Widget XmCreateDropDown</code>(
<code>Widget parent</code>,
<code>String name</code>,
<code>ArgList arglist</code>,
<code>Cardinal arg_count</code>);</pre>
<h2>Description</h2>
<p><code>XmCreateDropDown</code> creates an instance of a DropDown widget and returns the associated widget ID.</p>
<dl COMPACT>
<dt><i>parent</i></dt>
<dd>Specifies the parent widget ID.</dd>
<dt><i>name</i></dt>
<dd>Specifies the name of the created widget.</dd>
<dt><i>arglist</i></dt>
<dd>Specifies the argument list.</dd>
<dt><code>arg_count</code></dt>
<dd>Specifies the number of attribute/value pairs in the argument list (<i>arglist</i>).</dd></dl>
<p> For a complete definition of DropDown and its associated resources, see <code><a href="/docs/linux/man/3-xmdropdown/">XmDropDown</a></code>(3).</p>
<h2>Return</h2>
<p>Returns the DropDown widget ID.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmdropdown/">XmDropDown</a></code>(3).</p>
