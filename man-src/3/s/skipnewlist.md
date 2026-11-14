---
title: "skipnewlist(3)"
name: "skipnewlist"
section: "3"
letter: "s"
url: "/docs/linux/man/3-skipnewlist/"
description: "skipNewList – create a skip list."
---

<p>skipNewList &#8211; create a skip list.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;util/skiplist.h&gt;
</code></pre>
<pre>NEOERR *skipNewList(skipList *skip, int threaded, int root, int maxLevel,
 int flushLimit, skipFreeValue freeValue, void *ctx);</pre>
<h2>Arguments</h2>
<p>threaded &#8211; true if list should be thread-safe.<br />
 root &#8211; performance parameter (see above).<br />
 maxLevel &#8211; performance parameter (see above).<br />
 flushLimit &#8211; max deleted items to keep cached before<br />
 forcing a flush.<br />
 freeValue &#8211; callback made whenever a value is flushed.<br />
 ctx &#8211; context to pass to &lt;freeValue&gt;.</p>
<h2>Description</h2>
<p>Returns a new skip list. If &lt;threaded&gt; is true, list is multi-thread safe. &lt;root&gt; and &lt;maxLevel&gt; determine performance and expected size (see discussion above). &lt;flushLimit&gt; is for threaded lists and determines the maximum number of deleted items to keep cached during concurrent searches. Once the limit is reached, new concurrent reads are blocked until all deleted items are flushed. MT-Level: Safe. </p>
<h2>Return Value</h2>
<p>None. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-skipdelete/">skipDelete</a></code>(3), <a href="/docs/linux/man/3-skipfreelist/">skipFreeList</a><code>(3), <a href="/docs/linux/man/3-skiprelease/">skipRelease</a></code>(3), <a href="/docs/linux/man/3-skipinsert/">skipInsert</a><code>(3), <a href="/docs/linux/man/3-skipsearch/">skipSearch</a></code>(3), <a href="/docs/linux/man/3-skipnext/">skipNext</a><code>(3), skipNewList</code> </p>
