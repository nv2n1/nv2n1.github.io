---
title: "skipdelete(3)"
name: "skipdelete"
section: "3"
letter: "s"
url: "/docs/linux/man/3-skipdelete/"
description: "skipDelete – delete an item."
---

<p>skipDelete &#8211; delete an item. </p>
<h2>Synopsis</h2>
<pre>
#include &lt;util/skiplist.h&gt;
</pre>
<pre>
void skipDelete(skipList list, UINT32 key);
</pre>
<h2>Arguments</h2>
<p> list &#8211; list to delete item from.<br />
 key &#8211; key identifying value to delete. </p>
<h2>Description</h2>
<p> Delete the item associated with &lt;key&gt; from &lt;list&gt;. </p>
<p> MT-Level: Safe if &lt;list&gt; thread-safe. </p>
<h2>Return Value</h2>
<p> None. </p>
<h2>See Also</h2>
<p> <code><a href="/docs/linux/man/3-skipdelete/">skipDelete</a></code>(3), <a href="/docs/linux/man/3-skipfreelist/">skipFreeList</a><code>(3), <a href="/docs/linux/man/3-skiprelease/">skipRelease</a></code>(3), <a href="/docs/linux/man/3-skipinsert/">skipInsert</a><code>(3), <a href="/docs/linux/man/3-skipsearch/">skipSearch</a></code>(3), <a href="/docs/linux/man/3-skipnext/">skipNext</a><code>(3), skipNewList</code></p>
