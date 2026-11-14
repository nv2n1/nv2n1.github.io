---
title: "xmtablistcopy(3)"
name: "xmtablistcopy"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtablistcopy/"
description: "XmTabListCopy — A convenience function that creates a new tab list from an existing list"
---

<p><code>XmTabListCopy</code> &#8212; A convenience function that creates a new tab list from an existing list</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>XmTabList XmTabListCopy</code>(
<code>XmTabList tablist</code>,
<code>int offset</code>,
<code>Cardinal count</code>);</pre>
<h2>Description</h2>
<p><code>XmTabListCopy</code> creates a new tab list consisting of a copy of a portion of the contents of the <i>tablist</i> argument. This function starts copying at the specified offset value of the tab list and copies <i>count</i> values.</p>
<dl COMPACT>
<dt><i>tablist</i></p>
<dd>Specifies a tab list to be copied.</p>
<dt><i>offset</i></p>
<dd>Specifies where to start copying. A value of 0 (zero) indicates begin at the beginning, a value of 1 indicates to skip the first tab, and so on. A negative indicates to begin counting backwards from the end. A value of -1 indicates to start copying from the last tab.</p>
<dt><i>count</i></p>
<dd>Specifies the number of tabs to copy. A value of 0 (zero) indicates to copy all elements from the starting point to the end (beginning if <i>offset</i> is negative) of the tab list.</dl>
<h2>Return</h2>
<p>If <i>tablist</i> is NULL, this function returns NULL. Otherwise, this function returns a newly allocated <code>XmTabList</code>. If the function does allocate an <code>XmTabList</code>, then the application is responsible for managing the allocated space. The application can recover the allocated space by calling <code>XmTabListFree</code>.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtablist/">XmTabList</a></code>(3) and <code><a href="/docs/linux/man/3-xmtablistfree/">XmTabListFree</a></code>(3).</p>
