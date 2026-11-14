---
title: "xmcreatedropdownlist(3)"
name: "xmcreatedropdownlist"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmcreatedropdownlist/"
description: "XmCreateDropDownList — The Drop-down list ComboBox widget creation function"
---

<p><code>XmCreateDropDownList</code> &#8212; The Drop-down list ComboBox widget creation function</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/ComboBox.h&gt;
<code>Widget XmCreateDropDownList</code>(
<code>Widget parent</code>,
<code>String name</code>,
<code>ArgList arglist</code>,
<code>Cardinal arg_count</code>);</pre>
<h2>Description</h2>
<p><code>XmCreateDropDownList</code> creates an instance of a ComboBox widget of <code>XmNcomboBoxType</code> <code>XmDROP_DOWN_LIST</code> and returns the associated widget ID.</p>
<dl COMPACT>
<dt><i>parent</i></p>
<dd>Specifies the parent widget ID.</p>
<dt><i>name</i></p>
<dd>Specifies the name of the created widget.</p>
<dt><i>arglist</i></p>
<dd>Specifies the argument list.</p>
<dt><code>arg_count</code></p>
<dd>Specifies the number of attribute/value pairs in the argument list (<i>arglist</i>).</dl>
<p> For a complete definition of ComboBox and its associated resources, see <code><a href="/docs/linux/man/3-xmcombobox/">XmComboBox</a></code>(3).</p>
<h2>Return</h2>
<p>Returns the ComboBox widget ID.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmcombobox/">XmComboBox</a></code>(3).</p>
