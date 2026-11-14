---
title: "ck_array_buffer(3)"
name: "ck_array_buffer"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_array_buffer/"
description: "ck_array_buffer – return length and pointer to array of reader-visible pointers"
---

<h2>NAME</h2>
<p> <code>ck_array_buffer</code> &#8211; return length and pointer to array of reader-visible pointers</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_array.h Ft void * Fn ck_array_buffer ck_array_t *array unsigned int *length</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_array_buffer 3 returns a pointer to the array of pointers currently visible to readers after the last commit operation in Fa array . The unsigned integer pointed to by Fa length is updated to reflect the length of the array.</p>
<h2>RETURN VALUES</h2>
<p> This function returns a pointer to an array of pointers.</p>
<h2>SEE ALSO</h2>
<p> ck_array_commit3, ck_array_put3, ck_array_put_unique3, ck_array_remove3, ck_array_init3 ck_array_deinit3, ck_array_length3, ck_array_initialized3, CK_ARRAY_FOREACH3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
