---
title: "xmimmbresetic(3)"
name: "xmimmbresetic"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmimmbresetic/"
description: "XmImMbResetIC — An input manager function that resets the input context for a widget"
---

<p><code>XmImMbResetIC</code> &#8212; An input manager function that resets the input context for a widget</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/XmIm.h&gt;
<code>void XmImMbResetIC</code>(
<code>Widget widget</code>,
<code>char **mb</code>);</pre>
<h2>Description</h2>
<p><code>XmImMbResetIC</code> gets the XIC of the widget and resets it. It puts a pointer to a string containing the current preedit string to <i>mb</i>. The caller should free the returned string after use by calling <code>Xfree</code>.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the ID of the widget.</p>
<dt><i>mb</i></p>
<dd>Contains a pointer to the preedit string upon return.</dl>
<h2>Return Value</h2>
<p>None</p>
<h2>See Also</h2>
