---
title: "skipnext(3)"
name: "skipnext"
section: "3"
letter: "s"
url: "/docs/linux/man/3-skipnext/"
description: "skipNext – find next item."
---

<p>skipNext &#8211; find next item.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;util/skiplist.h&gt;

void *skipNext(skipList list, UINT32 *pkey, void **plock);
</code></pre>
<h2>Arguments</h2>
<p>list &#8211; list to search in.<br />
 pkey &#8211; pointer to previous key (0 to start).<br />
 plock &#8211; place for value lock (or NULL).</p>
<h2>Description</h2>
<p>Searches in list &lt;list&gt; for item with key next larger that the one in &lt;pkey&gt;, and returns its value if found, or NULL if not. If &lt;plock&gt; is non-NULL, then the lock returned in &lt;plock&gt; will be associated with the returned value. Until this lock is passed to skipRelease(), the value will not be freed with the freeValue callback (see skipNewList()). MT-Level: Safe if &lt;list&gt; thread-safe. </p>
<h2>Return Value</h2>
<p>pkey &#8211; set to new key.<br />
 plock &#8211; set to value lock. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-skipdelete/">skipDelete</a></code>(3), <a href="/docs/linux/man/3-skipfreelist/">skipFreeList</a><code>(3), <a href="/docs/linux/man/3-skiprelease/">skipRelease</a></code>(3), <a href="/docs/linux/man/3-skipinsert/">skipInsert</a><code>(3), <a href="/docs/linux/man/3-skipsearch/">skipSearch</a></code>(3), <a href="/docs/linux/man/3-skipnext/">skipNext</a><code>(3), skipNewList</code> </p>
