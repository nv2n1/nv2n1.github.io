---
title: "xmtextgetstringwcs(3)"
name: "xmtextgetstringwcs"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtextgetstringwcs/"
description: "XmTextGetStringWcs — A Text function that retrieves a copy of the wide character string value of a Text widget"
---

<p><code>XmTextGetStringWcs</code> &#8212; A Text function that retrieves a copy of the wide character string value of a Text widget</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Text.h&gt;
<code>wchar_t * XmTextGetStringWcs</code>(
<code>Widget widget</code>);</pre>
<h2>Description</h2>
<p><code>XmTextGetStringWcs</code> retrieves a copy of the wide character string value of the Text widget. The application is responsible for freeing the storage associated with the string by calling <code>XtFree</code>.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the Text widget ID</dl>
<p> For a complete definition of Text and its associated resources, see <code><a href="/docs/linux/man/3-xmtext/">XmText</a></code>(3).</p>
<h2>Return</h2>
<p>Returns the wide character string value of the Text widget. The function returns an empty string if the length of the Text widget&#8217;s string is 0 (zero).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtext/">XmText</a></code>(3) and <code><a href="/docs/linux/man/3-xmtextgetstring/">XmTextGetString</a></code>(3).</p>
