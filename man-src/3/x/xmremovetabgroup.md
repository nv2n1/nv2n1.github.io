---
title: "xmremovetabgroup(3)"
name: "xmremovetabgroup"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmremovetabgroup/"
description: "XmRemoveTabGroup — A function that removes a tab group"
---

<p><code>XmRemoveTabGroup</code> &#8212; A function that removes a tab group</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>void XmRemoveTabGroup</code>(
<code>Widget tab_group</code>);</pre>
<h2>Description</h2>
<p>This function is obsolete and its behavior is replaced by setting <code>XmNnavigationType</code> to <code>XmNONE</code>. <code>XmRemoveTabGroup</code> removes a widget from the list of tab groups associated with a particular widget hierarchy and sets the widget&#8217;s <code>XmNnavigationType</code> to <code>XmNONE</code>.</p>
<dl COMPACT>
<dt><i>tab_group</i></p>
<dd>Specifies the widget ID</dl>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmaddtabgroup/">XmAddTabGroup</a></code>(3), <code><a href="/docs/linux/man/3-xmmanager/">XmManager</a></code>(3), and <code><a href="/docs/linux/man/3-xmprimitive/">XmPrimitive</a></code>(3).</p>
