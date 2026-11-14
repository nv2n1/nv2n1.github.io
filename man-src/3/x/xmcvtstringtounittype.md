---
title: "xmcvtstringtounittype(3)"
name: "xmcvtstringtounittype"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmcvtstringtounittype/"
description: "XmCvtStringToUnitType — A function that converts a string to a unit-type value"
---

<p><code>XmCvtStringToUnitType</code> &#8212; A function that converts a string to a unit-type value</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>void XmCvtStringToUnitType</code>(
<code>XrmValuePtr args</code>,
<code>Cardinal * num_args</code>,
<code>XrmValue * from_val</code>,
<code>XrmValue * to_val</code>);</pre>
<h2>Description</h2>
<p><code>XmCvtStringToUnitType</code> converts a string to a unit type. Refer to the reference pages for <code>XmGadget</code>, <code>XmManager</code>, or <code>XmPrimitive</code> for a description of the valid unit types. Use of this function as a resource converter is obsolete. It has been replaced by a new resource converter that uses the RepType facility.</p>
<dl COMPACT>
<dt><i>args</i></p>
<dd>Specifies a list of additional <code>XrmValue</code> arguments to the converter if additional context is needed to perform the conversion. For example, the string-to-font converter needs the widget&#8217;s screen and the string-to-pixel converter needs the widget&#8217;s screen and color map. This argument is often NULL.</p>
<dt><i>num_args</i></p>
<dd>Specifies the number of additional <code>XrmValue</code> arguments. This argument is often zero.</p>
<dt><i>from_val</i></p>
<dd>Specifies the value to convert</p>
<dt><i>to_val</i></p>
<dd>Specifies the descriptor to use to return the converted value</dl>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmgadget/">XmGadget</a></code>(3), <code><a href="/docs/linux/man/3-xmmanager/">XmManager</a></code>(3), and <code><a href="/docs/linux/man/3-xmprimitive/">XmPrimitive</a></code>(3).</p>
