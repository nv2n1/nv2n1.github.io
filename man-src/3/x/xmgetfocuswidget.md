---
title: "xmgetfocuswidget(3)"
name: "xmgetfocuswidget"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmgetfocuswidget/"
description: "XmGetFocusWidget — Returns the ID of the widget that has keyboard focus"
---

<p><code>XmGetFocusWidget</code> &#8212; Returns the ID of the widget that has keyboard focus</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>Widget XmGetFocusWidget</code>(
<code>Widget widget</code>);</pre>
<h2>Description</h2>
<p><code>XmGetFocusWidget</code> examines the hierarchy that contains the specified widget and returns the ID of the widget that has keyboard focus. The function extracts the widget ID from the associated Shell widget; therefore, the specified widget can be located anywhere in the hierarchy.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies a widget ID within a given hierarchy</dl>
<h2>Return</h2>
<p>Returns the ID of the widget with keyboard focus. If no child of the Shell has focus, the function returns NULL.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmprocesstraversal/">XmProcessTraversal</a></code>(3).</p>
