---
title: "ck_array_init(3)"
name: "ck_array_init"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_array_init/"
description: "ck_array_init – initialize a pointer array"
---

<h2>NAME</h2>
<p> <code>ck_array_init</code> &#8211; initialize a pointer array</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_array.h Ft bool Fn ck_array_init ck_array_t *array unsigned int mode struct ck_malloc *allocator unsigned int initial_length</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_array_init 3 function initializes the array pointed to by the argument Fa array . The mode value must be <code>CK_ARRAY_MODE_SPMC</code> The Fa allocator argument must point to a ck_malloc data structure with valid non-NULL function pointers initialized for malloc, free and realloc. The Fa initial_length specifies the initial length of the array. The value of Fa initial_length must be greater than or equal to 2. An array allows for one concurrent put or remove operations in the presence of any number of concurrent CK_ARRAY_FOREACH operations.</p>
<h2>RETURN VALUES</h2>
<p> This function returns true if the array was successfully created. It returns false if the creation failed. Failure may occur due to internal memory allocation failures or invalid arguments.</p>
<h2>SEE ALSO</h2>
<p> ck_array_commit3, ck_array_put3, ck_array_put_unique3, ck_array_remove3, ck_array_deinit3 ck_array_length3, ck_array_buffer3, ck_array_initialized3, CK_ARRAY_FOREACH3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
