---
title: "xmtextfieldgetstring(3)"
name: "xmtextfieldgetstring"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtextfieldgetstring/"
description: "XmTextFieldGetString — A TextField function that accesses the string value"
---

<p><code>XmTextFieldGetString</code> &#8212; A TextField function that accesses the string value</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/TextF.h&gt;
<code>char * XmTextFieldGetString</code>(
<code>Widget widget</code>);</pre>
<h2>Description</h2>
<p><code>XmTextFieldGetString</code> accesses the string value of the TextField widget. The application is responsible for freeing the storage associated with the string by calling <code>XtFree</code>.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the TextField widget ID</dl>
<p> For a complete definition of TextField and its associated resources, see <code><a href="/docs/linux/man/3-xmtextfield/">XmTextField</a></code>(3).</p>
<h2>Return</h2>
<p>Returns a character pointer to the string value of the TextField widget. This returned value is a copy of the value of the <code>XmNvalue</code> resource. Returns an empty string if the length of the TextField widget&#8217;s string is 0 (zero).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtextfield/">XmTextField</a></code>(3) and <code><a href="/docs/linux/man/3-xmtextfieldgetstringwcs/">XmTextFieldGetStringWcs</a></code>(3).</p>
