---
title: "cap_copy_ext(3)"
name: "cap_copy_ext"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cap_copy_ext/"
description: "cap_copy_ext, cap_size, cap_copy_int – capability state external representation translation"
---

<h2>NAME</h2>
<p> cap_copy_ext, cap_size, cap_copy_int &#8211; capability state external representation translation</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;sys/capability.h&gt;</code> </p>
<p> <code>ssize_t cap_size(cap_t </code><i>cap_p</i><code>);</code> </p>
<p> <code>ssize_t cap_copy_ext(void *</code><i>ext_p</i><code>, cap_t </code><i>cap_p</i><code>, ssize_t </code><i>size</i><code>);</code> </p>
<p> <code>cap_t cap_copy_int(const void *</code><i>ext_p</i><code>);</code> </p>
<p> Link with <i>-lcap</i>.</p>
<h2>DESCRIPTION</h2>
<p> These functions translate between internal and external representations of a capability state. The external representation is an exportable, contiguous, persistent representation of a capability state in user-managed space. The internal representation is managed by the capability functions in working storage. </p>
<p> <code>cap_size</code>() returns the total length (in bytes) that the capability state in working storage identified by <i>cap_p</i> would require when converted by <code>cap_copy_ext</code>(). This function is used primarily to determine the amount of buffer space that must be provided to the <code>cap_copy_ext</code>() function in order to hold the capability data record created from <i>cap_p</i>. </p>
<p> <code>cap_copy_ext</code>() copies a capability state in working storage, identified by <i>cap_p</i>, from system managed space to user-managed space (pointed to by <i>ext_p</i>) and returns the length of the resulting data record. The size parameter represents the maximum size, in bytes, of the resulting data record. The <code>cap_copy_ext</code>() function will do any conversions necessary to convert the capability state from the undefined internal format to an exportable, contiguous, persistent data record. It is the responsibility of the user to allocate a buffer large enough to hold the copied data. The buffer length required to hold the copied data may be obtained by a call to the <code>cap_size</code>() function. </p>
<p> <code>cap_copy_int</code>() copies a capability state from a capability data record in user-managed space to a new capability state in working storage, allocating any memory necessary, and returning a pointer to the newly created capability state. The function initializes the capability state and then copies the capability state from the record pointed to by <i>ext_p</i> into the capability state, converting, if necessary, the data from a contiguous, persistent format to an undefined, internal format. Once copied into internal format, the object can be manipulated by the capability state manipulation functions (see <code><a href="/docs/linux/man/3-cap_clear/">cap_clear</a></code>(3)). Note that the record pointed to by <i>ext_p</i> must have been obtained from a previous, successful call to <code>cap_copy_ext</code>() for this function to work successfully. The caller should free any releasable memory, when the capability state in working storage is no longer required, by calling <code>cap_free</code>() with the <i>cap_t</i> as an argument.</p>
<h2>RETURN VALUE</h2>
<p> <code>cap_size</code>() returns the length required to hold a capability data record on success, and -1 on failure. </p>
<p> <code>cap_copy_ext</code>() returns the number of bytes placed in the user managed space pointed to by <i>ext_p </i> on success, and -1 on failure. </p>
<p> <code>cap_copy_int</code>() returns a pointer to the newly created capability state in working storage on success, and NULL on failure. </p>
<p> On failure, <code>errno</code> is set to <code>EINVAL</code>, <code>ENOMEM</code>, or <code>ERANGE</code>.</p>
<h2>CONFORMING TO</h2>
<p> These functions are specified in the withdrawn POSIX.1e draft specification.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libcap/">libcap</a></code>(3), <code><a href="/docs/linux/man/3-cap_clear/">cap_clear</a></code>(3), <code><a href="/docs/linux/man/3-cap_from_text/">cap_from_text</a></code>(3), <code><a href="/docs/linux/man/3-cap_get_file/">cap_get_file</a></code>(3), <code><a href="/docs/linux/man/3-cap_get_proc/">cap_get_proc</a></code>(3), <code><a href="/docs/linux/man/3-cap_init/">cap_init</a></code>(3), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7) </p>
<h2>Index</h2>
