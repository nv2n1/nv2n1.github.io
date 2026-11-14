---
title: "dictremove(3)"
name: "dictremove"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dictremove/"
description: "dictRemove – remove item from dictionary."
---

<p>dictRemove &#8211; remove item from dictionary. </p>
<h2>Synopsis</h2>
<pre>
#include &lt;util/dict.h&gt;
</pre>
<pre>
BOOL dictRemove(dictCtx dict, const char *id);
</pre>
<h2>Arguments</h2>
<p> dict &#8211; dictionary to search in.<br />
 id &#8211; identifier of item to remove. </p>
<h2>Description</h2>
<p> Removes item identified by &lt;id&gt; from &lt;dict&gt;. </p>
<p> MT-Level: Safe if &lt;dict&gt; thread-safe. </p>
<h2>Return Value</h2>
<p> None. </p>
<h2>See Also</h2>
<p> <code><a href="/docs/linux/man/3-dictdestroy/">dictDestroy</a></code>(3), <a href="/docs/linux/man/3-dictcleanup/">dictCleanup</a><code>(3), <a href="/docs/linux/man/3-dictreleaselock/">dictReleaseLock</a></code>(3), <a href="/docs/linux/man/3-dictremove/">dictRemove</a><code>(3), <a href="/docs/linux/man/3-dictnext/">dictNext</a></code>(3), <a href="/docs/linux/man/3-dictcreate/">dictCreate</a><code>(3), <a href="/docs/linux/man/3-dictsetvalue/">dictSetValue</a></code>(3), <a href="/docs/linux/man/3-dictmodifyvalue/">dictModifyValue</a><code>(3), dictSearch</code></p>
