---
title: "ck_array_length(3)"
name: "ck_array_length"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_array_length/"
description: "ck_array_length – returns the number of pointers committed to an array"
---

<h2>NAME</h2>
<p> <code>ck_array_length</code> &#8211; returns the number of pointers committed to an array</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_array.h Ft unsigned int Fn ck_array_length ck_array_t *array</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_array_length 3 function returns the number of items a concurrent traversal operation would encounter at completion time.</p>
<h2>RETURN VALUES</h2>
<p> The number of traversal-visible pointers is returned.</p>
<h2>SEE ALSO</h2>
<p> ck_array_commit3, ck_array_put3, ck_array_put_unique3, ck_array_remove3, ck_array_init3 ck_array_deinit3, ck_array_buffer3, ck_array_initialized3, CK_ARRAY_FOREACH3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
