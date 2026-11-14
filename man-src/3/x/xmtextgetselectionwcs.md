---
title: "xmtextgetselectionwcs(3)"
name: "xmtextgetselectionwcs"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtextgetselectionwcs/"
description: "XmTextGetSelectionWcs — A Text function that retrieves the value of a wide character encoded primary selection"
---

<p><code>XmTextGetSelectionWcs</code> &#8212; A Text function that retrieves the value of a wide character encoded primary selection</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Text.h&gt;
<code>wchar_t * XmTextGetSelectionWcs</code>(
<code>Widget widget</code>);</pre>
<h2>Description</h2>
<p><code>XmTextGetSelectionWcs</code> retrieves the value of the primary selection that is encoded in a wide character format. It returns a NULL pointer if no text is selected in the widget. The application is responsible for freeing the storage associated with the wide character buffer by calling <code>XtFree</code>.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the Text widget ID</dl>
<p> For a complete definition of Text and its associated resources, see <code><a href="/docs/linux/man/3-xmtext/">XmText</a></code>(3).</p>
<h2>Return</h2>
<p>Returns the wide character string that is associated with the primary selection in the Text widget.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtext/">XmText</a></code>(3) and <code><a href="/docs/linux/man/3-xmtextgetselection/">XmTextGetSelection</a></code>(3).</p>
