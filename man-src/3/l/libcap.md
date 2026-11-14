---
title: "libcap(3)"
name: "libcap"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libcap/"
description: "cap_clear, cap_clear_flag, cap_compare, cap_copy_ext, cap_copy_int, cap_free, cap_from_name, cap_from_text, cap_get_fd, cap_get_file, cap_get_flag, cap_get_pid, cap_get_proc, cap_set_fd, cap_set_fi..."
---

<h2>NAME</h2>
<p> cap_clear, cap_clear_flag, cap_compare, cap_copy_ext, cap_copy_int, cap_free, cap_from_name, cap_from_text, cap_get_fd, cap_get_file, cap_get_flag, cap_get_pid, cap_get_proc, cap_set_fd, cap_set_file, cap_set_flag, cap_set_proc, cap_size, cap_to_name, cap_to_text, cap_get_pid, cap_dup &#8211; capability data object manipulation</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;sys/capability.h&gt;
int cap_clear(cap_t cap_p);
int cap_clear_flag(cap_t cap_p, cap_flag_t flag);
int cap_compare(cap_t cap_a, cap_t cap_b);
ssize_t cap_copy_ext(void *ext_p, cap_t cap_p, ssize_t size);
cap_t cap_copy_int(const void *ext_p);
int cap_free(void *obj_d);
int cap_from_name(const char *name, cap_value_t *cap_p);
cap_t cap_from_text(const char *buf_p);
cap_t cap_get_fd(int fd);
cap_t cap_get_file(const char *path_p);
int cap_get_flag(cap_t cap_p, cap_value_t cap,
                 cap_flag_t flag, cap_flag_value_t *value_p);
#include &lt;sys/types.h&gt;
cap_t cap_get_pid(pid_t pid);
cap_t cap_get_proc(void);
int cap_set_fd(int fd, cap_t caps);
int cap_set_file(const char *path_p, cap_t cap_p);
int cap_set_flag(cap_t cap_p, cap_flag_t flag, int ncap,
                 const cap_value_t *caps, cap_flag_value_t value);
int cap_set_proc(cap_t cap_p);
ssize_t cap_size(cap_t cap_p);
char *cap_to_name(cap_value_t cap);
char *cap_to_text(cap_t caps, ssize_t *length_p);
cap_t cap_get_pid(pid_t pid);
cap_t cap_dup(cap_t cap_p);
Link with - lcap.
</code></pre>
<h2>DESCRIPTION</h2>
<p> These functions work on a capability state held in working storage. A <i>cap_t</i> holds information about the capabilities in each of the three sets, Permitted, Inheritable, and Effective. Each capability in a set may be clear (disabled, 0) or set (enabled, 1). </p>
<p> These functions work with the following data types:</p>
<dl>
<dt><i>cap_value_t</i></p>
<dd> identifies a capability, such as <code>CAP_CHOWN</code>.</p>
<dt><i>cap_flag_t</i></p>
<dd> identifies one of the three flags associated with a capability (i.e., it identifies one of the three capability sets). Valid values for this type are <code>CAP_EFFECTIVE</code>, <code>CAP_INHERITABLE</code> or <code>CAP_PERMITTED</code>.</p>
<dt><i>cap_flag_value_t</i></p>
<dd> identifies the setting of a particular capability flag (i.e, the value of a capability in a set). Valid values for this type are <code>CAP_CLEAR</code>(0) or <code><a href="/docs/linux/man/1-cap_set/">CAP_SET</a></code>(1).</dl>
<h2>RETURN VALUE</h2>
<p> The return value is generally specific to the individual function called. On failure, <i>errno</i> is set appropriately.</p>
<h2>CONFORMING TO</h2>
<p> These functions are as per the withdrawn POSIX.1e draft specification. The following functions are Linux extensions: <code>cap_clear_flag</code>(), <code>cap_compare</code>(), <code>cap_from_name</code>(), <code>cap_to_name</code>(), and <code>cap_compare</code>().</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cap_clear/">cap_clear</a></code>(3), <code><a href="/docs/linux/man/3-cap_copy_ext/">cap_copy_ext</a></code>(3), <code><a href="/docs/linux/man/3-cap_from_text/">cap_from_text</a></code>(3), <code><a href="/docs/linux/man/3-cap_get_file/">cap_get_file</a></code>(3), <code><a href="/docs/linux/man/3-cap_get_proc/">cap_get_proc</a></code>(3), <code><a href="/docs/linux/man/3-cap_init/">cap_init</a></code>(3), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7), <code><a href="/docs/linux/man/2-getpid/">getpid</a></code>(2) <code><a href="/docs/linux/man/1-capsh/">capsh</a></code>(1) </p>
<h2>Index</h2>
