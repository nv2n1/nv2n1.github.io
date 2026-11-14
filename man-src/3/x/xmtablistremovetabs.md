---
title: "xmtablistremovetabs(3)"
name: "xmtablistremovetabs"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtablistremovetabs/"
description: "XmTabListRemoveTabs — A convenience function that removes noncontiguous tabs"
---

<p><code>XmTabListRemoveTabs</code> &#8212; A convenience function that removes noncontiguous tabs</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>XmTabList XmTabListRemoveTabs</code>(
<code>XmTabList oldlist</code>,
<code>Cardinal *position_list</code>,
<code>Cardinal position_count</code>);</pre>
<h2>Description</h2>
<p><code>XmTabListRemoveTabs</code> removes noncontiguous tabs from a tab list. The function creates a new tab list by copying the contents of <i>oldlist</i> and removing all tabs whose corresponding positions appear in the <i>position_list</i> array. A warning message is displayed if a specified position is invalid; for example, if the value is a number greater than the number of tabs in the tab list.</p>
<dl COMPACT>
<dt><i>tablist</i></p>
<dd>Specifies the tab list. The function deallocates <i>oldlist</i> and the tabs it contains after extracting the required information.</p>
<dt><i>position_list</i></p>
<dd>Specifies an array of the tab positions to be removed. The position of the first tab in the list is 0 (zero), the position of the second tab is 1, and so on.</p>
<dt><i>position_count</i></p>
<dd>Specifies the number of elements in the <i>position_list</i>.</dl>
<h2>Return</h2>
<p>If <i>oldlist</i> or <i>position_list</i> is NULL, or <i>position_count</i> is 0 (zero), returns <i>oldlist</i>. Otherwise, this function returns the new tab list. The function allocates space to hold the returned tab list. The application is responsible for managing the allocated space. The application can recover the allocated space by calling <code>XmTabListFree</code>.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtablist/">XmTabList</a></code>(3) and <code><a href="/docs/linux/man/3-xmtablistfree/">XmTabListFree</a></code>(3).</p>
