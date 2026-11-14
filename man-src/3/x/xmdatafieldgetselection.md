---
title: "xmdatafieldgetselection(3)"
name: "xmdatafieldgetselection"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmdatafieldgetselection/"
description: "XmDataFieldGetSelection — A DataField function that retrieves the value of the primary selection"
---

<p><code>XmDataFieldGetSelection</code> &#8212; A DataField function that retrieves the value of the primary selection</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/DataF.h&gt;
<code>char * XmDataFieldGetSelection</code>(
<code>Widget widget</code>);</pre>
<h2>Description</h2>
<p><code>XmDataFieldGetSelection</code> retrieves the value of the primary selection. It returns a NULL pointer if no text is selected in the widget. The application is responsible for freeing the storage associated with the string by calling <code>XtFree</code>.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the DataField widget ID</dl>
<p> For a complete definition of DataField and its associated resources, see <code><a href="/docs/linux/man/3-xmdatafield/">XmDataField</a></code>(3).</p>
<h2>Return</h2>
<p>Returns a character pointer to the string that is associated with the primary selection.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmdatafield/">XmDataField</a></code>(3) and <code><a href="/docs/linux/man/3-xmdatafieldgetselectionwcs/">XmDataFieldGetSelectionWcs</a></code>(3).</p>
