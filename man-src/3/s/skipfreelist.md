---
title: "skipfreelist(3)"
name: "skipfreelist"
section: "3"
letter: "s"
url: "/docs/linux/man/3-skipfreelist/"
description: "skipFreeList – free a skip list."
---

<p>skipFreeList &#8211; free a skip list.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;util/skiplist.h&gt;

void skipFreeList(skipList list);
</code></pre>
<h2>Arguments</h2>
<p>list &#8211; list to free.</p>
<h2>Description</h2>
<p>Release all resources used by &lt;list&gt; including all key/value pairs. MT-Level: Safe for unique &lt;list&gt;. </p>
<h2>Return Value</h2>
<p>None. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-skipdelete/">skipDelete</a></code>(3), <a href="/docs/linux/man/3-skipfreelist/">skipFreeList</a><code>(3), <a href="/docs/linux/man/3-skiprelease/">skipRelease</a></code>(3), <a href="/docs/linux/man/3-skipinsert/">skipInsert</a><code>(3), <a href="/docs/linux/man/3-skipsearch/">skipSearch</a></code>(3), <a href="/docs/linux/man/3-skipnext/">skipNext</a><code>(3), skipNewList</code> </p>
