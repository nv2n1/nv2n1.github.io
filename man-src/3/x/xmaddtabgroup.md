---
title: "xmaddtabgroup(3)"
name: "xmaddtabgroup"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmaddtabgroup/"
description: "XmAddTabGroup — A function that adds a manager or a primitive widget to the list of tab groups"
---

<p><code>XmAddTabGroup</code> &#8212; A function that adds a manager or a primitive widget to the list of tab groups</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>void XmAddTabGroup</code>(
<code>Widget tab_group</code>);</pre>
<h2>Description</h2>
<p>This function is obsolete and its behavior is replaced by setting <code>XmNnavigationType</code> to <code>XmEXCLUSIVE_TAB_GROUP</code>. When the keyboard is used to traverse through a widget hierarchy, primitive or manager widgets are grouped together into what are known as <code>tab groups</code>. Any manager or primitive widget can be a tab group. Within a tab group, move the focus to the next widget in the tab group by using the arrow keys. To move to another tab group, use <code>KNextField</code> or <code>KPrevField</code>. </p>
<p> Tab groups are ordinarily specified by the <code>XmNnavigationType</code> resource. <code>XmAddTabGroup</code> is called to control the order of traversal of tab groups. The widget specified by <i>tab_group</i> is appended to the list of tab groups to be traversed, and the widget&#8217;s <code>XmNnavigationType</code> is set to <code>XmEXCLUSIVE_TAB_GROUP</code>.</p>
<dl COMPACT>
<dt><i>tab_group</i></p>
<dd>Specifies the manager or primitive widget ID</dl>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmmanager/">XmManager</a></code>(3), <code><a href="/docs/linux/man/3-xmgettabgroup/">XmGetTabGroup</a></code>(3), <code><a href="/docs/linux/man/3-xmprimitive/">XmPrimitive</a></code>(3), and <code><a href="/docs/linux/man/3-xmremovetabgroup/">XmRemoveTabGroup</a></code>(3).</p>
