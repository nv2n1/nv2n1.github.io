---
title: "xmtablistgettab(3)"
name: "xmtablistgettab"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtablistgettab/"
description: "XmTabListGetTab — A convenience function that returns a copy of a tab"
---

<p><code>XmTabListGetTab</code> &#8212; A convenience function that returns a copy of a tab</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>XmTab XmTabListGetTab</code>(
<code>XmTabList tablist</code>,
<code>Cardinal position</code>);</pre>
<h2>Description</h2>
<p><code>XmTabListGetTab</code> returns a copy of the tab that is located at the specified position in the tab list.</p>
<dl COMPACT>
<dt><i>tablist</i></p>
<dd>Specifies the tab list.</p>
<dt><i>position</i></p>
<dd>Specifies the position of the tab to be returned. A value of 0 (zero) returns the first tab in the tab list, a value of 1 returns the second tab, and so on.</dl>
<h2>Return</h2>
<p>Returns a copy of the tab that is located at the specified position in the tab list. If <i>position</i> is greater than or equal to the number of tabs in the tab list, this function returns NULL. The application is responsible for managing the space allocted by the returned tab copy. The application can recover this allocated space by calling <code>XmTabFree</code>.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtabfree/">XmTabFree</a></code>(3) and <code><a href="/docs/linux/man/3-xmtablist/">XmTabList</a></code>(3).</p>
