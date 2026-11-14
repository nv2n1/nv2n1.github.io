---
title: "dictreleaselock(3)"
name: "dictreleaselock"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dictreleaselock/"
description: "dictReleaseLock – release lock on value."
---

<p>dictReleaseLock &#8211; release lock on value. </p>
<h2>Synopsis</h2>
<pre>
#include &lt;util/dict.h&gt;
</pre>
<pre>
void dictReleaseLock(dictCtx dict, void *lock);
</pre>
<h2>Arguments</h2>
<p> dict &#8211; dictionary containing value to release.<br />
 lock &#8211; lock to release. </p>
<h2>Description</h2>
<p> Releases the lock on the value associated with &lt;lock&gt;. Once the lock is released, the dictCleanupFunc callback can be called for the value (see dictCleanup()). </p>
<p> MT-Level: Safe if &lt;dict&gt; thread-safe. </p>
<h2>Return Value</h2>
<p> None. </p>
<h2>See Also</h2>
<p> <code><a href="/docs/linux/man/3-dictdestroy/">dictDestroy</a></code>(3), <a href="/docs/linux/man/3-dictcleanup/">dictCleanup</a><code>(3), <a href="/docs/linux/man/3-dictreleaselock/">dictReleaseLock</a></code>(3), <a href="/docs/linux/man/3-dictremove/">dictRemove</a><code>(3), <a href="/docs/linux/man/3-dictnext/">dictNext</a></code>(3), <a href="/docs/linux/man/3-dictcreate/">dictCreate</a><code>(3), <a href="/docs/linux/man/3-dictsetvalue/">dictSetValue</a></code>(3), <a href="/docs/linux/man/3-dictmodifyvalue/">dictModifyValue</a><code>(3), dictSearch</code></p>
