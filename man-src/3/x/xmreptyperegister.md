---
title: "xmreptyperegister(3)"
name: "xmreptyperegister"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmreptyperegister/"
description: "XmRepTypeRegister — A representation type manager function that registers a representation type resource"
---

<p><code>XmRepTypeRegister</code> &#8212; A representation type manager function that registers a representation type resource</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/RepType.h&gt;
<code>XmRepTypeId XmRepTypeRegister</code>(
<code>String rep_type</code>,
<code>String *value_names</code>,
<code>unsigned char *values</code>,
<code>unsigned char num_values</code>);</pre>
<h2>Description</h2>
<p><code>XmRepTypeRegister</code> registers a representation type resource with the representation type manager. All features of the representation type management facility become available for the specified representation type. The function installs a forward type converter to convert string values to numerical representation type values. </p>
<p> When the <i>values</i> argument is NULL, consecutive numerical values are assumed. The order of the strings in the <i>value_names</i> array determines the numerical values for the resource. For example, the first value name is 0 (zero); the second value name is 1; and so on. </p>
<p> If it is non-NULL, the <i>values</i> argument can be used to assign values to representation types that have nonconsecutive values or have duplicate names for the same value. Representation types registered in this manner will consume additional storage and will be slightly slower than representation types with consecutive values. </p>
<p> A representation type can only be registered once; if the same representation type name is registered more than once, the behavior is undefined. </p>
<p> The function <code>XmRepTypeAddReverse</code> installs a reverse converter for a registered representation type. The reverse converter takes a representation type numerical value and returns the corresponding string value. If the list of numerical values for a representation type contains duplicate values, the reverse converter uses the first name in the <i>value_names</i> list that matches the specified numeric value. For example, if a <i>value_names</i> array has <i>cancel</i>, <i>proceed</i>, and <i>abort</i>, and the corresponding <i>values</i> array contains 0, 1, and 0, the reverse converter will return <i>cancel</i> instead of <i>abort</i> for an input value of 0.</p>
<dl COMPACT>
<dt><i>rep_type</i></p>
<dd>Specifies the representation type name.</p>
<dt><i>value_names</i></p>
<dd>Specifies a pointer to an array of value names associated with the representation type. A value name is specified in lowercase characters without an <code>Xm</code> prefix. Words within a name are separated with underscores.</p>
<dt><i>values</i></p>
<dd>Specifies a pointer to an array of values associated with the representation type. A value in this array is associated with the value name in the corresponding position of the <i>value_names</i> array.</p>
<dt><i>num_values</i></p>
<dd>Specifies the number of entries in the <i>value_names</i> and <i>values</i> arrays.</dl>
<h2>Return</h2>
<p>Returns the identification number for the specified representation type.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmreptypeaddreverse/">XmRepTypeAddReverse</a></code>(3), <code><a href="/docs/linux/man/3-xmreptypegetid/">XmRepTypeGetId</a></code>(3), <code><a href="/docs/linux/man/3-xmreptypegetnamelist/">XmRepTypeGetNameList</a></code>(3), <code><a href="/docs/linux/man/3-xmreptypegetrecord/">XmRepTypeGetRecord</a></code>(3), <code><a href="/docs/linux/man/3-xmreptypegetregistered/">XmRepTypeGetRegistered</a></code>(3), and <code><a href="/docs/linux/man/3-xmreptypevalidvalue/">XmRepTypeValidValue</a></code>(3).</p>
