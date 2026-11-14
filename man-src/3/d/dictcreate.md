---
title: "dictcreate(3)"
name: "dictcreate"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dictcreate/"
description: "dictCreate – create new dictionary."
---

<p>dictCreate &#8211; create new dictionary. </p>
<h2>Synopsis</h2>
<pre>
#include &lt;util/dict.h&gt;
</pre>
<pre>
NEOERR *dictCreate(dictCtx *dict, BOOL threaded, UINT32 root, UINT32 maxLevel, 
    UINT32 flushLimit, BOOL useCase, 
    dictFreeValueFunc freeValue, void *freeRock);
</pre>
<h2>Arguments</h2>
<p> threaded &#8211; true if list should be thread-safe.<br />
 root &#8211; performance parameter (see above).<br />
 maxLevel &#8211; performance parameter (see above).<br />
 flushLimit &#8211; max deleted items to keep cached before<br />
 forcing a flush.<br />
 useCase &#8211; true to be case sensitive in identifiers<br />
 freeValue &#8211; callback when freeing a value<br />
 freeRock &#8211; context for freeValue callback </p>
<h2>Description</h2>
<p> Returns a dictionary. If &lt;threaded&gt; is true, list is multi-thread safe. &lt;root&gt;, &lt;maxLevel&gt;, and &lt;flushLimit&gt; act as for skipNewList() (see skiplist.h) </p>
<p> MT-Level: Safe. </p>
<h2>Return Value</h2>
<p> None. </p>
<h2>See Also</h2>
<p> <code><a href="/docs/linux/man/3-dictdestroy/">dictDestroy</a></code>(3), <a href="/docs/linux/man/3-dictcleanup/">dictCleanup</a><code>(3), <a href="/docs/linux/man/3-dictreleaselock/">dictReleaseLock</a></code>(3), <a href="/docs/linux/man/3-dictremove/">dictRemove</a><code>(3), <a href="/docs/linux/man/3-dictnext/">dictNext</a></code>(3), <a href="/docs/linux/man/3-dictcreate/">dictCreate</a><code>(3), <a href="/docs/linux/man/3-dictsetvalue/">dictSetValue</a></code>(3), <a href="/docs/linux/man/3-dictmodifyvalue/">dictModifyValue</a><code>(3), dictSearch</code></p>
