---
title: "skiprelease(3)"
name: "skiprelease"
section: "3"
letter: "s"
url: "/docs/linux/man/3-skiprelease/"
description: "skipRelease – release lock on value."
---

<p>skipRelease &#8211; release lock on value.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;util/skiplist.h&gt;

void skipRelease(skipList list, void *lock);
</code></pre>
<h2>Arguments</h2>
<p>list &#8211; list containing value to release.<br />
 lock &#8211; lock to release.</p>
<h2>Description</h2>
<p>Releases the lock on the value associated with &lt;lock&gt;. Once the lock is released, the freeValue callback can be called and the item freed (see skipNewList()). MT-Level: Safe if &lt;list&gt; thread-safe. </p>
<h2>Return Value</h2>
<p>None. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-skipdelete/">skipDelete</a></code>(3), <a href="/docs/linux/man/3-skipfreelist/">skipFreeList</a><code>(3), <a href="/docs/linux/man/3-skiprelease/">skipRelease</a></code>(3), <a href="/docs/linux/man/3-skipinsert/">skipInsert</a><code>(3), <a href="/docs/linux/man/3-skipsearch/">skipSearch</a></code>(3), <a href="/docs/linux/man/3-skipnext/">skipNext</a><code>(3), skipNewList</code> </p>
