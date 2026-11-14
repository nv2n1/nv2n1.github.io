---
title: "ck_array_deinit(3)"
name: "ck_array_deinit"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_array_deinit/"
description: "ck_array_deinit – destroy and deinitialize a pointer array"
---

<h2>NAME</h2>
<p> <code>ck_array_deinit</code> &#8211; destroy and deinitialize a pointer array</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_array.h Ft void Fn ck_array_deinit ck_array_t *array bool defer</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_array_deinit 3 destroys the memory associated with the array pointed to by Fa array . The Fa defer argument is true if the allocator must destroy the memory using safe memory reclamation or false if the allocator can destroy this memory immediately.</p>
<h2>RETURN VALUES</h2>
<p> This function has no return value.</p>
<h2>SEE ALSO</h2>
<p> ck_array_commit3, ck_array_put3, ck_array_put_unique3, ck_array_remove3, ck_array_init3 ck_array_length3, ck_array_buffer3, ck_array_initialized3, CK_ARRAY_FOREACH3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
