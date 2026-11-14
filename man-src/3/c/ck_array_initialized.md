---
title: "ck_array_initialized(3)"
name: "ck_array_initialized"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_array_initialized/"
description: "ck_array_initialized – indicates whether an array was recently initialized or deinitialized"
---

<h2>NAME</h2>
<p> <code>ck_array_initialized</code> &#8211; indicates whether an array was recently initialized or deinitialized</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_array.h Ft bool Fn ck_array_initialized ck_array_t *array</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_array_initialized 3 can be used to determine whether an array was recently initialized with Fn ck_array_init 3 or deinitialized with Fn ck_array_deinit 3 . Behavior is undefined if a user allocates internal allocator data in through other means.</p>
<h2>RETURN VALUES</h2>
<p> This function returns true if the array is initialized, and false otherwise.</p>
<h2>SEE ALSO</h2>
<p> ck_array_commit3, ck_array_put3, ck_array_put_unique3, ck_array_remove3, ck_array_init3 ck_array_deinit3, ck_array_length3, ck_array_buffer3, CK_ARRAY_FOREACH3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
