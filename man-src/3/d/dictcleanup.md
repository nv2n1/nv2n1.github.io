---
title: "dictcleanup(3)"
name: "dictcleanup"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dictcleanup/"
description: "dictCleanup – cleanup dictionary"
---

<p>dictCleanup &#8211; cleanup dictionary </p>
<h2>Synopsis</h2>
<pre>
#include &lt;util/dict.h&gt;
</pre>
<pre>
void dictCleanup(dictCtx dict, dictCleanupFunc cleanup, void *rock);
</pre>
<h2>Arguments</h2>
<p> dict &#8211; dictionary to cleanup<br />
 cleanup &#8211; cleanup callback<br />
 rock &#8211; to pass to &lt;cleanup&gt; </p>
<h2>Description</h2>
<p> Calls &lt;cleanup&gt; for every item in &lt;dict&gt;. If &lt;cleanup&gt; returns true, then item is removed from &lt;dict&gt;. </p>
<p> MT-Level: Safe if &lt;dict&gt; thread-safe. </p>
<h2>Return Value</h2>
<p> None. </p>
<h2>See Also</h2>
<p> <code><a href="/docs/linux/man/3-dictdestroy/">dictDestroy</a></code>(3), <a href="/docs/linux/man/3-dictcleanup/">dictCleanup</a><code>(3), <a href="/docs/linux/man/3-dictreleaselock/">dictReleaseLock</a></code>(3), <a href="/docs/linux/man/3-dictremove/">dictRemove</a><code>(3), <a href="/docs/linux/man/3-dictnext/">dictNext</a></code>(3), <a href="/docs/linux/man/3-dictcreate/">dictCreate</a><code>(3), <a href="/docs/linux/man/3-dictsetvalue/">dictSetValue</a></code>(3), <a href="/docs/linux/man/3-dictmodifyvalue/">dictModifyValue</a><code>(3), dictSearch</code></p>
