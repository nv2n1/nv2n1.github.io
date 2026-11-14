---
title: "skipsearch(3)"
name: "skipsearch"
section: "3"
letter: "s"
url: "/docs/linux/man/3-skipsearch/"
description: "skipSearch – search a skip list."
---

<p>skipSearch &#8211; search a skip list. </p>
<h2>Synopsis</h2>
<pre>
#include &lt;util/skiplist.h&gt;
</pre>
<pre>
void *skipSearch(skipList list, UINT32 key, void **plock);
</pre>
<h2>Arguments</h2>
<p> list &#8211; list to search in.<br />
 key &#8211; key to look for.<br />
 plock &#8211; place for value lock (or NULL). </p>
<h2>Description</h2>
<p> Searches for &lt;key&gt; in &lt;list&gt;, and returns value if found, or NULL if not. If &lt;plock&gt; is non-NULL, then the lock returned in &lt;plock&gt; will be associated with the returned value. Until this lock is passed to skipRelease(), the value will not be freed with the freeValue callback (see skipNewList()). </p>
<p> MT-Level: Safe if &lt;list&gt; thread-safe. </p>
<h2>Return Value</h2>
<p> plock &#8211; set to value lock. </p>
<h2>See Also</h2>
<p> <code><a href="/docs/linux/man/3-skipdelete/">skipDelete</a></code>(3), <a href="/docs/linux/man/3-skipfreelist/">skipFreeList</a><code>(3), <a href="/docs/linux/man/3-skiprelease/">skipRelease</a></code>(3), <a href="/docs/linux/man/3-skipinsert/">skipInsert</a><code>(3), <a href="/docs/linux/man/3-skipsearch/">skipSearch</a></code>(3), <a href="/docs/linux/man/3-skipnext/">skipNext</a><code>(3), skipNewList</code></p>
