---
title: "cap_free(3)"
name: "cap_free"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cap_free/"
description: "cap_init, cap_free, cap_dup – capability data object storage management"
---

<h2>NAME</h2>
<p> cap_init, cap_free, cap_dup &#8211; capability data object storage management</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;sys/capability.h&gt;</code> </p>
<p> <code>cap_t cap_init(void);</code> </p>
<p> <code>int cap_free(void *</code><i>obj_d</i><code>);</code> </p>
<p> <code>cap_t cap_dup(cap_t </code><i>cap_p</i><code>);</code> </p>
<p> Link with <i>-lcap</i>.</p>
<h2>DESCRIPTION</h2>
<p> The capabilities associated with a file or process are never edited directly. Instead, working storage is allocated to contain a representation of the capability state. Capabilities are edited and manipulated only within this working storage area. Once editing of the capability state is complete, the updated capability state is used to replace the capability state associated with the file or process. </p>
<p> <code>cap_init</code>() creates a capability state in working storage and returns a pointer to the capability state. The initial value of all flags are cleared. The caller should free any releasable memory, when the capability state in working storage is no longer required, by calling <code>cap_free</code>() with the <i>cap_t</i> as an argument. </p>
<p> <code>cap_free</code>() liberates any releasable memory that has been allocated to the capability state identified by <i>obj_d</i>. The <i>obj_d</i> argument may identify either a <i>cap_t</i> entity, or a <i>char *</i> entity allocated by the <code>cap_to_text</code>() function. </p>
<p> <code>cap_dup</code>() returns a duplicate capability state in working storage given by the source object <i>cap_p</i>, allocating any memory necessary, and returning a pointer to the newly created capability state. Once duplicated, no operation on either capability state affects the other in any way. When the duplicated capability state in working storage is no longer required, the caller should free any releasable memory by calling <code>cap_free</code>() with the <i>cap_t</i> as an argument.</p>
<h2>RETURN VALUE</h2>
<p> <code>cap_init</code>() and <code>cap_dup</code>() return a non-NULL value on success, and NULL on failure. </p>
<p> <code>cap_free</code>() returns zero on success, and -1 on failure. </p>
<p> On failure, <i>errno</i> is set to <code>EINVAL</code> or <code>ENOMEM</code>.</p>
<h2>CONFORMING TO</h2>
<p> These functions are specified in the withdrawn POSIX.1e draft specification.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libcap/">libcap</a></code>(3), <code><a href="/docs/linux/man/3-cap_clear/">cap_clear</a></code>(3), <code><a href="/docs/linux/man/3-cap_copy_ext/">cap_copy_ext</a></code>(3), <code><a href="/docs/linux/man/3-cap_from_text/">cap_from_text</a></code>(3), <code><a href="/docs/linux/man/3-cap_get_file/">cap_get_file</a></code>(3), <code><a href="/docs/linux/man/3-cap_get_proc/">cap_get_proc</a></code>(3), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7) </p>
<h2>Index</h2>
