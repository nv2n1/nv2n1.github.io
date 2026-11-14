---
title: "cap_set_file(3)"
name: "cap_set_file"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cap_set_file/"
description: "cap_get_file, cap_set_file, cap_get_fd, cap_set_fd – capability manipulation on files"
---

<h2>NAME</h2>
<p> cap_get_file, cap_set_file, cap_get_fd, cap_set_fd &#8211; capability manipulation on files</p>
<h2>SYNOPSIS</h2>
<p> <code></p>
<p> </code> <code>#include &lt;sys/capability.h&gt;</code> </p>
<p> <code>cap_t cap_get_file(const char *</code><i>path_p</i><code>);</code> </p>
<p> <code>int cap_set_file(const char *</code><i>path_p</i><code>, cap_t </code><i>cap_p</i><code>);</code> </p>
<p> <code>cap_t cap_get_fd(int </code><i>fd</i><code>);</code> </p>
<p> <code>int cap_set_fd(int </code><i>fd</i><code>, cap_t </code><i>caps</i><code>);</code> </p>
<p> Link with <i>-lcap</i>.</p>
<h2>DESCRIPTION</h2>
<p> <code>cap_get_file</code>() and <code>cap_get_fd</code>() allocate a capability state in working storage and set it to represent the capability state of the pathname pointed to by <i>path_p</i> or the file open on descriptor <i>fd</i>. These functions return a pointer to the newly created capability state. The effects of reading the capability state from any file other than a regular file is undefined. The caller should free any releasable memory, when the capability state in working storage is no longer required, by calling <code>cap_free</code>() with the used <i>cap_t</i> as an argument. </p>
<p> <code>cap_set_file</code>() and <code>cap_set_fd</code>() set the values for all capability flags for all capabilities for the pathname pointed to by <i>path_p</i> or the file open on descriptor <i>fd</i>, with the capability state identified by <i>cap_p</i>. The new capability state of the file is completely determined by the contents of <i>cap_p</i>. A NULL value for <i>cap_p</i> is used to indicate that capabilities for the file should be deleted. For these functions to succeed, the calling process must have the effective capability, <code>CAP_SETFCAP</code>, enabled and either the effective user ID of the process must match the file owner or the calling process must have the <code>CAP_FOWNER</code> flag in its effective capability set. The effects of writing the capability state to any file type other than a regular file are undefined.</p>
<h2>RETURN VALUE</h2>
<p> <code>cap_get_file</code>() and <code>cap_get_fd</code>() return a non-NULL value on success, and NULL on failure. </p>
<p> <code>cap_set_file</code>() and <code>cap_set_fd</code>() return zero on success, and -1 on failure. </p>
<p> On failure, <i>errno</i> is set to <code>EACCES</code>, <code>EBADFD</code>, <code>ENAMETOOLONG</code>, <code>ENOENT</code>, <code>ENOMEM</code>, <code>ENOTDIR</code>, <code>EPERM</code>, or <code>EROFS</code>.</p>
<h2>CONFORMING TO</h2>
<p> These functions are specified by withdrawn POSIX.1e draft specification.</p>
<h2>NOTES</h2>
<p> Support for file capabilities is provided on Linux since version 2.6.24. </p>
<p> On Linux, the file Effective set is a single bit. If it is enabled, then all Permitted capabilities are enabled in the Effective set of the calling process when the file is executed; otherwise, no capabilities are enabled in the process&#8217;s Effective set following an <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2). Because the file Effective set is a single bit, if any capability is enabled in the Effective set of the <i>cap_t</i> given to <code>cap_set_file</code>() or <code>cap_set_fd</code>(), then all capabilities whose Permitted or Inheritable flag is enabled must also have the Effective flag enabled. Conversely, if the Effective bit is enabled on a file, then the <i>cap_t</i> returned by <code>cap_get_file()</code> and <code>cap_get_fd()</code> will have the Effective flag enabled for each capability that has the Permitted or Inheritable flag enabled.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libcap/">libcap</a></code>(3), <code><a href="/docs/linux/man/3-cap_clear/">cap_clear</a></code>(3), <code><a href="/docs/linux/man/3-cap_copy_ext/">cap_copy_ext</a></code>(3), <code><a href="/docs/linux/man/3-cap_from_text/">cap_from_text</a></code>(3), <code><a href="/docs/linux/man/3-cap_get_proc/">cap_get_proc</a></code>(3), <code><a href="/docs/linux/man/3-cap_init/">cap_init</a></code>(3), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7) </p>
<h2>Index</h2>
