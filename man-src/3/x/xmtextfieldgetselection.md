---
title: "xmtextfieldgetselection(3)"
name: "xmtextfieldgetselection"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtextfieldgetselection/"
description: "XmTextFieldGetSelection — A TextField function that retrieves the value of the primary selection"
---

<p><code>XmTextFieldGetSelection</code> &#8212; A TextField function that retrieves the value of the primary selection</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/TextF.h&gt;
<code>char * XmTextFieldGetSelection</code>(
<code>Widget widget</code>);</pre>
<h2>Description</h2>
<p><code>XmTextFieldGetSelection</code> retrieves the value of the primary selection. It returns a NULL pointer if no text is selected in the widget. The application is responsible for freeing the storage associated with the string by calling <code>XtFree</code>.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the TextField widget ID</dl>
<p> For a complete definition of TextField and its associated resources, see <code><a href="/docs/linux/man/3-xmtextfield/">XmTextField</a></code>(3).</p>
<h2>Return</h2>
<p>Returns a character pointer to the string that is associated with the primary selection.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtextfield/">XmTextField</a></code>(3) and <code><a href="/docs/linux/man/3-xmtextfieldgetselectionwcs/">XmTextFieldGetSelectionWcs</a></code>(3).</p>
