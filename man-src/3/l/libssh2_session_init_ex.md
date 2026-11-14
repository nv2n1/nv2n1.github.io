---
title: "libssh2_session_init_ex(3)"
name: "libssh2_session_init_ex"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_session_init_ex/"
description: "libssh2_session_init_ex – initializes an SSH session object"
---

<h2>NAME</h2>
<p> libssh2_session_init_ex &#8211; initializes an SSH session object</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; </p>
<p> LIBSSH2_SESSION * libssh2_session_init_ex(LIBSSH2_ALLOC_FUNC((*myalloc)), LIBSSH2_FREE_FUNC((*myfree)), LIBSSH2_REALLOC_FUNC((*myrealloc)), void *abstract); </p>
<p> LIBSSH2_SESSION * libssh2_session_init(void); </p>
<h2>DESCRIPTION</h2>
<p> <i>myalloc</i> &#8211; Custom allocator function. Refer to the section on Callbacks for implementing an allocator callback. Pass a value of NULL to use the default system allocator. </p>
<p> <i>myfree</i> &#8211; Custom de-allocator function. Refer to the section on Callbacks for implementing a deallocator callback. Pass a value of NULL to use the default system deallocator. </p>
<p> <i>myrealloc</i> &#8211; Custom re-allocator function. Refer to the section on Callbacks for implementing a reallocator callback. Pass a value of NULL to use the default system reallocator. </p>
<p> <i>abstract</i> &#8211; Arbitrary pointer to application specific callback data. This value will be passed to any callback function associated with the named session instance. </p>
<p> Initializes an SSH session object. By default system memory allocators (malloc(), free(), realloc()) will be used for any dynamically allocated memory blocks. Alternate memory allocation functions may be specified using the extended version of this API call, and/or optional application specific data may be attached to the session object. </p>
<p> This method must be called first, prior to configuring session options or starting up an SSH session with a remote server.</p>
<h2>RETURN VALUE</h2>
<p> Pointer to a newly allocated LIBSSH2_SESSION instance, or NULL on errors.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_session_free/">libssh2_session_free</a>(3)</code> <code><a href="/docs/linux/man/3-libssh2_session_handshake/">libssh2_session_handshake</a>(3)</code> </p>
<h2>Index</h2>
