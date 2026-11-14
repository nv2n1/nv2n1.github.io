---
title: "ck_array_remove(3)"
name: "ck_array_remove"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_array_remove/"
description: "ck_array_remove – attempt immediate or deferred removal of a pointer from an array"
---

<h2>NAME</h2>
<p> <code>ck_array_remove</code> &#8211; attempt immediate or deferred removal of a pointer from an array</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_array.h Ft bool Fn ck_array_remove ck_array_t *array void *pointer</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_array_remove 3 function will attempt to remove the value of Fa pointer into the array pointed to by Fa array . The operation is also free to apply the operation immediately if there is an opportunity for elimination with a pending (uncommitted) put operation. If no elimination was possible, the function may require to allocate more memory.</p>
<h2>RETURN VALUES</h2>
<p> This function returns true if the remove operation succeeded. It will return false otherwise due to internal allocation failures or because the value did not exist.</p>
<h2>SEE ALSO</h2>
<p> ck_array_init3, ck_array_commit3, ck_array_remove3, ck_array_put_unique3, ck_array_deinit3 ck_array_length3, ck_array_buffer3, ck_array_initialized3, CK_ARRAY_FOREACH3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
