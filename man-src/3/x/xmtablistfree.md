---
title: "xmtablistfree(3)"
name: "xmtablistfree"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtablistfree/"
description: "XmTabListFree — A convenience function that frees the memory of a new tab list"
---

<p><code>XmTabListFree</code> &#8212; A convenience function that frees the memory of a new tab list</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>void XmTabListFree</code>(
<code>XmTabList tablist</code>);</pre>
<h2>Description</h2>
<p><code>XmTabListFree</code> recovers memory used by a tab list. In addition, this function frees all contained tabs. If the <i>tablist</i> is NULL, the function returns immediately.</p>
<dl COMPACT>
<dt><i>tablist</i></p>
<dd>Specifies the tab list to be freed.</dl>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtablist/">XmTabList</a></code>(3).</p>
