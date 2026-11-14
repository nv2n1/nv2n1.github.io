---
title: "xmreptypeaddreverse(3)"
name: "xmreptypeaddreverse"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmreptypeaddreverse/"
description: "XmRepTypeAddReverse — A representation type manager function that installs the reverse converter for a previously registered representation type"
---

<p><code>XmRepTypeAddReverse</code> &#8212; A representation type manager function that installs the reverse converter for a previously registered representation type</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/RepType.h&gt;
<code>void XmRepTypeAddReverse</code>(
<code>XmRepTypeId rep_type_id</code>);</pre>
<h2>Description</h2>
<p><code>XmRepTypeAddReverse</code> installs the reverse converter for a previously registered representation type. The reverse converter takes a numerical representation type value and returns its corresponding string value. Certain applications may require this capability to obtain a string value to display on a screen or to build a resource file. </p>
<p> The <i>values</i> argument of the <code>XmRepTypeRegister</code> function can be used to register representation types with nonconsecutive values or with duplicate names for the same value. If the list of numerical values for a representation type contains duplicate values, the reverse converter uses the first name in the <i>value_names</i> list that matches the specified numeric value. For example, if a <i>value_names</i> array has <i>cancel</i>, <i>proceed</i>, and <i>abort</i>, and the corresponding <i>values</i> array contains 0, 1, and 0, the reverse converter will return <i>cancel</i> instead of <i>abort</i> for an input value of 0.</p>
<dl COMPACT>
<dt><i>rep_type_id</i></p>
<dd>Specifies the identification number of the representation type</dl>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmreptypegetid/">XmRepTypeGetId</a></code>(3) and <code><a href="/docs/linux/man/3-xmreptyperegister/">XmRepTypeRegister</a></code>(3).</p>
