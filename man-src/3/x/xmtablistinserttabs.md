---
title: "xmtablistinserttabs(3)"
name: "xmtablistinserttabs"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtablistinserttabs/"
description: "XmTabListInsertTabs — A convenience function that inserts tabs into a tab list"
---

<p><code>XmTabListInsertTabs</code> &#8212; A convenience function that inserts tabs into a tab list</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>XmTabList XmTabListInsertTabs</code>(
<code>XmTabList oldlist</code>,
<code>XmTab *tabs</code>,
<code>Cardinal tab_count</code>,
<code>int position</code>);</pre>
<h2>Description</h2>
<p><code>XmTabListInsertTabs</code> creates a new tab list that includes the tabs in <i>oldlist</i>. This function copies specified tabs to the tab list at the given position. The first <i>tab_count</i> tabs of the <i>tabs</i> array are added to the tab list. If <i>oldlist</i> is NULL, <code>XmTabListInsertTabs</code> creates a new tab list containing only the tabs specified.</p>
<dl COMPACT>
<dt><i>oldlist</i></p>
<dd>Specifies the tab list to add the tabs to. The function deallocates <i>oldlist</i> after extracting the required information.</p>
<dt><i>tabs</i></p>
<dd>Specifies a pointer to the tabs to be added to the tab list. It is the caller&#8217;s responsibility to free the tabs in <i>tabs</i> by using <code>XmTabFree</code>.</p>
<dt><i>tab_count</i></p>
<dd>Specifies the number of tabs in <i>tabs</i>.</p>
<dt><i>position</i></p>
<dd>Specifies the position of the first new tab in the tab list. A value of 0 (zero) makes the first new tab the first tab in the tab list, a value of 1 makes it the second tab, and so on. If <i>position</i> is greater than the number of tabs in <i>oldlist</i>, then the tabs will be inserted at the end. If <i>position</i> is negative, the count will be backwards from the end. A value of -1 makes the first new tab the last tab, and so on.</dl>
<h2>Return</h2>
<p>If <i>tabs</i> is NULL or <i>tab_count</i> is 0 (zero), this function returns <i>oldlist</i>. Otherwise, it returns a new tab list. The function allocates space to hold the returned tab list. The application is responsible for managing the allocated space. The application can recover the allocated space by calling <code>XmTabListFree</code>.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtablist/">XmTabList</a></code>(3) and <code><a href="/docs/linux/man/3-xmtablistfree/">XmTabListFree</a></code>(3).</p>
