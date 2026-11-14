---
title: "xmgetxmscreen(3)"
name: "xmgetxmscreen"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmgetxmscreen/"
description: "XmGetXmScreen — A Screen function that returns the XmScreen object ID for a specified screen"
---

<p><code>XmGetXmScreen</code> &#8212; A Screen function that returns the XmScreen object ID for a specified screen</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Screen.h&gt;
<code>Widget XmGetXmScreen</code>(
<code>Screen *screen</code>);</pre>
<h2>Description</h2>
<p><code>XmGetXmScreen</code> returns the <code>XmScreen</code> object ID associated with a screen. The application can access and manipulate Screen resources with <code>XtGetValues</code> and <code>XtSetValues</code>.</p>
<dl COMPACT>
<dt><i>screen</i></p>
<dd>Specifies the screen for which the <code>XmScreen</code> ID is to be returned</dl>
<p> For a complete definition of Screen and its associated resources, see <code><a href="/docs/linux/man/3-xmscreen/">XmScreen</a></code>(3).</p>
<h2>Return</h2>
<p>Returns the <code>XmScreen</code> object ID.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmscreen/">XmScreen</a></code>(3).</p>
