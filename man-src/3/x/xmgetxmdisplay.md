---
title: "xmgetxmdisplay(3)"
name: "xmgetxmdisplay"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmgetxmdisplay/"
description: "XmGetXmDisplay — A Display function that returns the XmDisplay object ID for a specified display"
---

<p><code>XmGetXmDisplay</code> &#8212; A Display function that returns the XmDisplay object ID for a specified display</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Display.h&gt;
<code>Widget XmGetXmDisplay</code>(
<code>Display *display</code>);</pre>
<h2>Description</h2>
<p><code>XmGetXmDisplay</code> returns the <code>XmDisplay</code> object ID associated with a display. The application can access Display resources with <code>XtGetValues</code>.</p>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the display for which the <code>XmDisplay</code> object ID is to be returned</dl>
<p> For a complete definition of Display and its associated resources, see <code><a href="/docs/linux/man/3-xmdisplay/">XmDisplay</a></code>(3).</p>
<h2>Return</h2>
<p>Returns the <code>XmDisplay</code> object ID for the specified display.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmdisplay/">XmDisplay</a></code>(3).</p>
