---
title: "xmgetdestination(3)"
name: "xmgetdestination"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmgetdestination/"
description: "XmGetDestination — A function that returns the widget ID of the widget to be used as the current destination for quick paste and certain clipboard operations"
---

<p><code>XmGetDestination</code> &#8212; A function that returns the widget ID of the widget to be used as the current destination for quick paste and certain clipboard operations</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>Widget XmGetDestination</code>(
<code>Display *display</code>);</pre>
<h2>Description</h2>
<p><code>XmGetDestination</code> returns the widget that is the current destination on the specified display. The destination is generally the last editable widget on which a select, edit, insert, or paste operation was performed and is the destination for quick paste and certain clipboard functions. The destination is NULL until a keyboard or mouse operation has been done on an editable widget. Refer to the <i>Motif Programmer&#8217;s Guide</i> for a description of keyboard focus.</p>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the display whose destination widget is to be queried</dl>
<h2>Return</h2>
<p>Returns the widget ID for the current destination or NULL if there is no current destination.</p>
