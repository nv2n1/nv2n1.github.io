---
title: "xmimfreexic(3)"
name: "xmimfreexic"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmimfreexic/"
description: "XmImFreeXIC — An input manager function that unregisters widgets for an XIC"
---

<p><code>XmImFreeXIC</code> &#8212; An input manager function that unregisters widgets for an XIC</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/XmIm.h&gt;
<code>void XmImFreeXIC</code>(
<code>Widget widget</code>,
<code>XIC xic</code>);</pre>
<h2>Description</h2>
<p><code>XmImFreeXIC</code> unregisters all widgets associated with the specified X Input Context (XIC). The specified <i>widget</i> must be associated with the specified <i>xic</i>. </p>
<p> After unregistering the associated widgets, this call frees the <i>xic</i>.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the ID of a widget used to identify the <code>VendorShell</code> and <code>XmDisplay</code> that maintain the widget-XIC registry.</p>
<dt><i>xic</i></p>
<dd>Specifies the Input Context associated with the widget.</dl>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmimgetxic/">XmImGetXIC</a></code>(3) and <code><a href="/docs/linux/man/3-xmimsetxic/">XmImSetXIC</a></code>(3).</p>
