---
title: "ck_array_put_unique(3)"
name: "ck_array_put_unique"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_array_put_unique/"
description: "ck_array_put_unique – attempt immediate or deferred insertion of a unique pointer into array"
---

<h2>NAME</h2>
<p> <code>ck_array_put_unique</code> &#8211; attempt immediate or deferred insertion of a unique pointer into array</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_array.h Ft int Fn ck_array_put_unique ck_array_t *array void *pointer</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_array_put_unique 3 function will attempt to insert the value of Fa pointer into the array pointed to by Fa array . This function may incur additional memory allocations if not enough memory has been allocated in the array for a new entry. The operation is also free to apply the operation immediately if there is an opportunity for elimination with a pending (uncommitted) remove operation. The function will not make any modifications if the pointer already exists in the array.</p>
<h2>RETURN VALUES</h2>
<p> This function returns 1 if the pointer already exists in the array. It returns 0 if the put operation succeeded. It returns -1 on error due to internal memory allocation failures.</p>
<h2>SEE ALSO</h2>
<p> ck_array_init3, ck_array_commit3, ck_array_put3, ck_array_remove3, ck_array_deinit3 ck_array_length3, ck_array_buffer3, ck_array_initialized3, CK_ARRAY_FOREACH3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
