---
title: "xmdatafieldgetstring(3)"
name: "xmdatafieldgetstring"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmdatafieldgetstring/"
description: "XmDataFieldGetString — A DataField function that accesses the string value"
---

<p><code>XmDataFieldGetString</code> &#8212; A DataField function that accesses the string value</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/DataF.h&gt;
<code>char * XmDataFieldGetString</code>(
<code>Widget widget</code>);</pre>
<h2>Description</h2>
<p><code>XmDataFieldGetString</code> accesses the string value of the DataField widget. The application is responsible for freeing the storage associated with the string by calling <code>XtFree</code>.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the DataField widget ID</dl>
<p> For a complete definition of DataField and its associated resources, see <code><a href="/docs/linux/man/3-xmdatafield/">XmDataField</a></code>(3).</p>
<h2>Return</h2>
<p>Returns a character pointer to the string value of the DataField widget. This returned value is a copy of the value of the <code>XmNvalue</code> resource. Returns an empty string if the length of the DataField widget&#8217;s string is 0 (zero).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmdatafield/">XmDataField</a></code>(3) and <code><a href="/docs/linux/man/3-xmdatafieldgetstringwcs/">XmDataFieldGetStringWcs</a></code>(3).</p>
