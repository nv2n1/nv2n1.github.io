---
title: "dictsetvalue(3)"
name: "dictsetvalue"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dictsetvalue/"
description: "dictSetValue – set/reset an items value."
---

<p>dictSetValue &#8211; set/reset an items value. </p>
<h2>Synopsis</h2>
<pre>
#include &lt;util/dict.h&gt;
</pre>
<pre>
NEOERR *dictSetValue(dictCtx dict, const char *id, void *value);
</pre>
<h2>Arguments</h2>
<p> dict &#8211; dictionary to add pair to.<br />
 id &#8211; identifier to insert/update<br />
 value &#8211; value to store (may NOT be NULL) </p>
<h2>Description</h2>
<p> Updates the &lt;id&gt;/&lt;value&gt; pair into &lt;dict&gt;. If &lt;id&gt; is not in &lt;dict&gt;, it is created. </p>
<p> MT-Level: Safe if &lt;dict&gt; thread-safe. </p>
<h2>Return Value</h2>
<p> None. </p>
<h2>See Also</h2>
<p> <code><a href="/docs/linux/man/3-dictdestroy/">dictDestroy</a></code>(3), <a href="/docs/linux/man/3-dictcleanup/">dictCleanup</a><code>(3), <a href="/docs/linux/man/3-dictreleaselock/">dictReleaseLock</a></code>(3), <a href="/docs/linux/man/3-dictremove/">dictRemove</a><code>(3), <a href="/docs/linux/man/3-dictnext/">dictNext</a></code>(3), <a href="/docs/linux/man/3-dictcreate/">dictCreate</a><code>(3), <a href="/docs/linux/man/3-dictsetvalue/">dictSetValue</a></code>(3), <a href="/docs/linux/man/3-dictmodifyvalue/">dictModifyValue</a><code>(3), dictSearch</code></p>
