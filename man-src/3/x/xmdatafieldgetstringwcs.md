---
title: "xmdatafieldgetstringwcs(3)"
name: "xmdatafieldgetstringwcs"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmdatafieldgetstringwcs/"
description: "XmDataFieldGetStringWcs — A DataField function that retrieves a copy of the wide character string value of a DataField widget"
---

<p><code>XmDataFieldGetStringWcs</code> &#8212; A DataField function that retrieves a copy of the wide character string value of a DataField widget</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/DataF.h&gt;
<code>wchar_t * XmDataFieldGetStringWcs</code>(
<code>Widget widget</code>);</pre>
<h2>Description</h2>
<p><code>XmDataFieldGetStringWcs</code> retrieves a copy of the wide character string value of the DataField widget. The application is responsible for freeing the storage associated with the string by calling <code>XtFree</code>.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the DataField widget ID</dl>
<p> For a complete definition of DataField and its associated resources, see <code><a href="/docs/linux/man/3-xmdatafield/">XmDataField</a></code>(3).</p>
<h2>Return</h2>
<p>Returns the wide character string value of the DataField widget. The function returns an empty string if the length of the DataField widget&#8217;s string is 0 (zero).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmdatafield/">XmDataField</a></code>(3) and <code><a href="/docs/linux/man/3-xmdatafieldgetstring/">XmDataFieldGetString</a></code>(3).</p>
