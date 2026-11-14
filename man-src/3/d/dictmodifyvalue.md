---
title: "dictmodifyvalue(3)"
name: "dictmodifyvalue"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dictmodifyvalue/"
description: "dictModifyValue – create/modify an item."
---

<p>dictModifyValue &#8211; create/modify an item. </p>
<h2>Synopsis</h2>
<pre>
#include &lt;util/dict.h&gt;
</pre>
<pre>
NEOERR *dictModifyValue(dictCtx dict, const char *id, dictNewValueCB new_cb, 
                     dictUpdateValueCB update, void *rock);
</pre>
<h2>Arguments</h2>
<p> dict &#8211; dictionary to add pair to.<br />
 id &#8211; identifier of value<br />
 new &#8211; function to call to create new value (may be NULL)<br />
 update &#8211; function to call to modify value (if NULL, the old<br />
 value is freed, and &lt;new&gt; is used)<br />
 rock &#8211; context to pass to &lt;new&gt; or &lt;update&gt;. </p>
<h2>Description</h2>
<p> Finds &lt;id&gt;&#8217;s value and calls &lt;update&gt;. If &lt;id&gt; is not in &lt;dict&gt;, calls &lt;new&gt; to obtain a new value. </p>
<p> MT-Level: Safe if &lt;dict&gt; thread-safe. </p>
<h2>Return Value</h2>
<p> None. </p>
<h2>See Also</h2>
<p> <code><a href="/docs/linux/man/3-dictdestroy/">dictDestroy</a></code>(3), <a href="/docs/linux/man/3-dictcleanup/">dictCleanup</a><code>(3), <a href="/docs/linux/man/3-dictreleaselock/">dictReleaseLock</a></code>(3), <a href="/docs/linux/man/3-dictremove/">dictRemove</a><code>(3), <a href="/docs/linux/man/3-dictnext/">dictNext</a></code>(3), <a href="/docs/linux/man/3-dictcreate/">dictCreate</a><code>(3), <a href="/docs/linux/man/3-dictsetvalue/">dictSetValue</a></code>(3), <a href="/docs/linux/man/3-dictmodifyvalue/">dictModifyValue</a><code>(3), dictSearch</code></p>
