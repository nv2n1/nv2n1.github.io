---
title: "ck_array_commit(3)"
name: "ck_array_commit"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_array_commit/"
description: "ck_array_commit – linearization point for mutations before commit call"
---

<h2>NAME</h2>
<p> <code>ck_array_commit</code> &#8211; linearization point for mutations before commit call</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_array.h Ft bool Fn ck_array_commit ck_array_t *array</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_array_commit 3 function will commit any pending put or remove operations associated with the array. The function may end up requesting the safe reclamation of memory actively being iterated upon by other threads.</p>
<h2>RETURN VALUES</h2>
<p> This function returns true if the commit operation succeeded. It will return false otherwise, and pending operations will not be applied.</p>
<h2>SEE ALSO</h2>
<p> ck_array_init3, ck_array_put3, ck_array_put_unique3, ck_array_remove3, ck_array_deinit3 ck_array_length3, ck_array_buffer3, ck_array_initialized3, CK_ARRAY_FOREACH3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
