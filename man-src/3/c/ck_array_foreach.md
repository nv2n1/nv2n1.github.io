---
title: "ck_array_foreach(3)"
name: "ck_array_foreach"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_array_foreach/"
description: "CK_ARRAY_FOREACH – iterate through an array"
---

<p><code>CK_ARRAY_FOREACH</code> &#8211; iterate through an array</p>
<h2>Library</h2>
<p>Concurrency Kit (libck, -lck)</p>
<h2>Synopsis</h2>
<p>In ck_array.h Ft bool Fn CK_ARRAY_FOREACH ck_array_t *array ck_array_iterator_t *iterator void **b</p>
<h2>Description</h2>
<p>The Fn CK_ARRAY_FOREACH 3 macro iterates through the array pointed to by Fa array . A pointer to an iterator object must be specified by Fa iterator and Fa b must point to a void pointer.</p>
<h2>Example</h2>
<blockquote>
<pre>#include &lt;ck_array.h&gt;
/* Assume this was already previously initialized. */
ck_array_t array;
void
example(void)
{
 ck_array_iterator_t iterator;
 void *pointer;
 CK_ARRAY_FOREACH(&amp;array, &amp;iterator, &amp;pointer) {
 do_something(pointer);
 }
}</pre>
</blockquote>
<h2>Return Values</h2>
<p>This macro has no return value.</p>
<h2>See Also</h2>
<p>ck_array_init3, ck_array_commit3, ck_array_put3, ck_array_put_unique3, ck_array_remove3, ck_array_deinit3 ck_array_length3, ck_array_buffer3, ck_array_initialized3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a></p>
