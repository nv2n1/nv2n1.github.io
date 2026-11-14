---
title: "dictsearch(3)"
name: "dictsearch"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dictsearch/"
description: "dictSearch – search for value in dictionary."
---

<p>dictSearch &#8211; search for value in dictionary. </p>
<h2>Synopsis</h2>
<pre>
#include &lt;util/dict.h&gt;
</pre>
<pre>
void *dictSearch(dictCtx dict, const char *id, void **plock);
</pre>
<h2>Arguments</h2>
<p> dict &#8211; dictionary to search in.<br />
 id &#8211; identifier of item to find.<br />
 plock &#8211; place for value lock (or NULL). </p>
<h2>Description</h2>
<p> Searches for &lt;id&gt; in &lt;dict&gt;, and returns value if found, or NULL if not. If &lt;plock&gt; is non-NULL, then the lock returned in &lt;plock&gt; will be associated with the returned value. Until this lock is passed to dictReleaseLock(), the value will not be passed to the dictCleanupFunc callback (see dictCleanup()). </p>
<p> MT-Level: Safe if &lt;dict&gt; thread-safe. </p>
<h2>Return Value</h2>
<p> plock &#8211; set to value lock. </p>
<h2>See Also</h2>
<p> <code><a href="/docs/linux/man/3-dictdestroy/">dictDestroy</a></code>(3), <a href="/docs/linux/man/3-dictcleanup/">dictCleanup</a><code>(3), <a href="/docs/linux/man/3-dictreleaselock/">dictReleaseLock</a></code>(3), <a href="/docs/linux/man/3-dictremove/">dictRemove</a><code>(3), <a href="/docs/linux/man/3-dictnext/">dictNext</a></code>(3), <a href="/docs/linux/man/3-dictcreate/">dictCreate</a><code>(3), <a href="/docs/linux/man/3-dictsetvalue/">dictSetValue</a></code>(3), <a href="/docs/linux/man/3-dictmodifyvalue/">dictModifyValue</a><code>(3), dictSearch</code></p>
