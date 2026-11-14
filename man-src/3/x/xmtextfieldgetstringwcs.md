---
title: "xmtextfieldgetstringwcs(3)"
name: "xmtextfieldgetstringwcs"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtextfieldgetstringwcs/"
description: "XmTextFieldGetStringWcs — A TextField function that retrieves a copy of the wide character string value of a TextField widget"
---

<p><code>XmTextFieldGetStringWcs</code> &#8212; A TextField function that retrieves a copy of the wide character string value of a TextField widget</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/TextF.h&gt;
<code>wchar_t * XmTextFieldGetStringWcs</code>(
<code>Widget widget</code>);</pre>
<h2>Description</h2>
<p><code>XmTextFieldGetStringWcs</code> retrieves a copy of the wide character string value of the TextField widget. The application is responsible for freeing the storage associated with the string by calling <code>XtFree</code>.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the TextField widget ID</dl>
<p> For a complete definition of TextField and its associated resources, see <code><a href="/docs/linux/man/3-xmtextfield/">XmTextField</a></code>(3).</p>
<h2>Return</h2>
<p>Returns the wide character string value of the TextField widget. The function returns an empty string if the length of the TextField widget&#8217;s string is 0 (zero).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtextfield/">XmTextField</a></code>(3) and <code><a href="/docs/linux/man/3-xmtextfieldgetstring/">XmTextFieldGetString</a></code>(3).</p>
