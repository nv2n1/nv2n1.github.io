---
title: "dictdestroy(3)"
name: "dictdestroy"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dictdestroy/"
description: "dictDestroy – destroy dictionary."
---

<p>dictDestroy &#8211; destroy dictionary. </p>
<h2>Synopsis</h2>
<pre>
#include &lt;util/dict.h&gt;
</pre>
<pre>
void dictDestroy(dictCtx dict);
</pre>
<h2>Arguments</h2>
<p> dict &#8211; dictionary to destroy </p>
<h2>Description</h2>
<p> Release all resources used by &lt;dict&gt;. </p>
<p> MT-Level: Safe for unique &lt;dict&gt;. </p>
<h2>Return Value</h2>
<p> None. </p>
<h2>See Also</h2>
<p> <code><a href="/docs/linux/man/3-dictdestroy/">dictDestroy</a></code>(3), <a href="/docs/linux/man/3-dictcleanup/">dictCleanup</a><code>(3), <a href="/docs/linux/man/3-dictreleaselock/">dictReleaseLock</a></code>(3), <a href="/docs/linux/man/3-dictremove/">dictRemove</a><code>(3), <a href="/docs/linux/man/3-dictnext/">dictNext</a></code>(3), <a href="/docs/linux/man/3-dictcreate/">dictCreate</a><code>(3), <a href="/docs/linux/man/3-dictsetvalue/">dictSetValue</a></code>(3), <a href="/docs/linux/man/3-dictmodifyvalue/">dictModifyValue</a><code>(3), dictSearch</code></p>
