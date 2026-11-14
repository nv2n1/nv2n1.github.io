---
title: "skipinsert(3)"
name: "skipinsert"
section: "3"
letter: "s"
url: "/docs/linux/man/3-skipinsert/"
description: "skipInsert – insert an item."
---

<p>skipInsert &#8211; insert an item.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;util/skiplist.h&gt;
</code></pre>
<pre>NEOERR *skipInsert(skipList list, UINT32 key, void *value, int allowUpdate);</pre>
<h2>Arguments</h2>
<p>list &#8211; list to add pair to.<br />
 key &#8211; key identifying &lt;value&gt;.<br />
 value &#8211; value to store (may NOT be NULL)</p>
<h2>Description</h2>
<p>Inserts the &lt;key&gt;/&lt;value&gt; pair into the &lt;list&gt;. Key values 0 and -1 are reserved (and illegal). If key is already in list, and &lt;allowUpdate&gt; is true, value is updated, otherwise SKIPERR_EXISTS is returned. MT-Level: Safe if &lt;list&gt; thread-safe. </p>
<h2>Return Value</h2>
<p>None. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-skipdelete/">skipDelete</a></code>(3), <a href="/docs/linux/man/3-skipfreelist/">skipFreeList</a><code>(3), <a href="/docs/linux/man/3-skiprelease/">skipRelease</a></code>(3), <a href="/docs/linux/man/3-skipinsert/">skipInsert</a><code>(3), <a href="/docs/linux/man/3-skipsearch/">skipSearch</a></code>(3), <a href="/docs/linux/man/3-skipnext/">skipNext</a><code>(3), skipNewList</code> </p>
