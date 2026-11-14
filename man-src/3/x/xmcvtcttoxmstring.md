---
title: "xmcvtcttoxmstring(3)"
name: "xmcvtcttoxmstring"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmcvtcttoxmstring/"
description: "XmCvtCTToXmString — A compound string function that converts compound text to a compound string"
---

<p><code>XmCvtCTToXmString</code> &#8212; A compound string function that converts compound text to a compound string</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>XmString XmCvtCTToXmString</code>(
<code>char * text</code>);</pre>
<h2>Description</h2>
<p><code>XmCvtCTToXmString</code> converts a (<code>char *</code>) string in compound text format to a compound string. The application must call <code>XtAppInitialize</code> before calling this function. Conversion of compound text to compound strings is implementation dependent.</p>
<dl COMPACT>
<dt><i>text</i></p>
<dd>Specifies a string in compound text format to be converted to a compound string.</dl>
<h2>Return</h2>
<p>Returns a compound string derived from the compound text. The function allocates space to hold the returned compound string. The application is responsible for managing the allocated space. The application can recover the allocated space by calling <code>XmStringFree</code>. The compound text is assumed to be NULL-terminated; NULLs within the compound text are handled correctly. The handling of HORIZONTAL TABULATION (HT) control characters within the compound text is undefined. The compound text format is described in the X Consortium Standard <i>Compound Text Encoding</i>.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmcvtxmstringtoct/">XmCvtXmStringToCT</a></code>(3).</p>
