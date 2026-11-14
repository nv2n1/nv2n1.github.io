---
title: "ck_array_put(3)"
name: "ck_array_put"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_array_put/"
description: "ck_array_put – attempt immediate or deferred insertion of a pointer into array"
---

<h2>NAME</h2>
<p> <code>ck_array_put</code> &#8211; attempt immediate or deferred insertion of a pointer into array</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_array.h Ft bool Fn ck_array_put ck_array_t *array void *pointer</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_array_put 3 function will attempt to insert the value of Fa pointer into the array pointed to by Fa array . This function may incur additional memory allocations if not enough memory has been allocated in the array for a new entry. The operation is also free to apply the operation immediately if there is an opportunity for elimination with a pending (uncommitted) remove operation.</p>
<h2>RETURN VALUES</h2>
<p> This function returns true if the put operation succeeded. It will return false otherwise due to internal allocation failures.</p>
<h2>SEE ALSO</h2>
<p> ck_array_init3, ck_array_commit3, ck_array_put_unique3, ck_array_remove3, ck_array_deinit3 ck_array_length3, ck_array_buffer3, ck_array_initialized3, CK_ARRAY_FOREACH3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
