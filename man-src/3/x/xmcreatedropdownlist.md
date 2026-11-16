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
<dt><i>parent</i></dt>
<dd>Specifies the parent widget ID.</dd>
<dt><i>name</i></dt>
<dd>Specifies the name of the created widget.</dd>
<dt><i>arglist</i></dt>
<dd>Specifies the argument list.</dd>
<dt><code>arg_count</code></dt>
<dd>Specifies the number of attribute/value pairs in the argument list (<i>arglist</i>).</dd></dl>
<p> For a complete definition of ComboBox and its associated resources, see <code><a href="/docs/linux/man/3-xmcombobox/">XmComboBox</a></code>(3).</p>
<h2>Return</h2>
<p>Returns the ComboBox widget ID.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmcombobox/">XmComboBox</a></code>(3).</p>
