---
title: "xmtextfieldgetselectionwcs(3)"
name: "xmtextfieldgetselectionwcs"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtextfieldgetselectionwcs/"
description: "XmTextFieldGetSelectionWcs — A TextField function that retrieves the value of a wide character encoded primary selection"
---

<p><code>XmTextFieldGetSelectionWcs</code> &#8212; A TextField function that retrieves the value of a wide character encoded primary selection</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/TextF.h&gt;
<code>wchar_t * XmTextFieldGetSelectionWcs</code>(
<code>Widget widget</code>);</pre>
<h2>Description</h2>
<p><code>XmTextFieldGetSelectionWcs</code> retrieves the value of the primary selection, encoded in a wide character format. It returns a NULL pointer if no text is selected in the widget. The application is responsible for freeing the storage associated with the wide character buffer by calling <code>XtFree</code>.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the TextField widget ID</dl>
<p> For a complete definition of TextField and its associated resources, see <code><a href="/docs/linux/man/3-xmtextfield/">XmTextField</a></code>(3).</p>
<h2>Return</h2>
<p>Returns the wide character string that is associated with the primary selection in the TextField widget.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtextfield/">XmTextField</a></code>(3) and <code><a href="/docs/linux/man/3-xmtextfieldgetselection/">XmTextFieldGetSelection</a></code>(3).</p>
