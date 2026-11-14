---
title: "xmgettabgroup(3)"
name: "xmgettabgroup"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmgettabgroup/"
description: "XmGetTabGroup — Returns the widget ID of a tab group"
---

<p><code>XmGetTabGroup</code> &#8212; Returns the widget ID of a tab group</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>Widget XmGetTabGroup</code>(
<code>Widget widget</code>);</pre>
<h2>Description</h2>
<p><code>XmGetTabGroup</code> returns the widget ID of the tab group that contains the specified widget.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies a widget ID within a tab group</dl>
<h2>Return</h2>
<p>Returns the widget ID of a tab group or shell, determined as follows:</p>
<dl COMPACT>
<dt> &bull;</p>
<dd>If <i>widget</i> is a tab group or shell, returns <i>widget</i></p>
<dt> &bull;</p>
<dd>If neither <i>widget</i> nor any ancestor up to the nearest shell is a tab group, returns the nearest ancestor of <i>widget</i> that is a shell</p>
<dt> &bull;</p>
<dd>Otherwise, returns the nearest ancestor of <i>widget</i> that is a tab group</dl>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmaddtabgroup/">XmAddTabGroup</a></code>(3), <code><a href="/docs/linux/man/3-xmmanager/">XmManager</a></code>(3), and <code><a href="/docs/linux/man/3-xmprimitive/">XmPrimitive</a></code>(3).</p>
