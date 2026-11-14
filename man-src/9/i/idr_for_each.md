---
title: "idr_for_each(9)"
name: "idr_for_each"
section: "9"
letter: "i"
url: "/docs/linux/man/9-idr_for_each/"
description: "idr_for_each – iterate through all stored pointers"
---

<p>idr_for_each &#8211; iterate through all stored pointers</p>
<h2>Synopsis</h2>
<pre><code>int idr_for_each(struct idr *idp, int (*fn)(int id, void *p, void *data), void *data);</code></pre>
<h2>Arguments</h2>
<p><i>idp</i></p>
<dl>
<dd>
<dd>idr handle</dl>
<p> <i>fn</i></p>
<dl>
<dd>function to be called for each pointer</dl>
<p> <i>data</i></p>
<dl>
<dd>data passed back to callback function</dl>
<h2>Description</h2>
<p>Iterate over the pointers registered with the given idr. The callback function will be called for each pointer currently registered, passing the id, the pointer and the data pointer passed to this function. It is not safe to modify the idr tree while in the callback, so functions such as idr_get_new and idr_remove are not allowed. </p>
<p> We check the return of <i>fn</i> each time. If it returns anything other than <code>0</code>, we break out and return that value. </p>
<p> The caller must serialize <code>idr_for_each</code> vs <code>idr_get_new</code> and <code>idr_remove</code>.</p>
<h2>Copyright</h2>
