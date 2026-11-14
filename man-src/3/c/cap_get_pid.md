---
title: "cap_get_pid(3)"
name: "cap_get_pid"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cap_get_pid/"
description: "cap_get_proc, cap_set_proc, capgetp, cap_get_bound, cap_drop_bound – capability manipulation on processes"
---

<h2>NAME</h2>
<p> cap_get_proc, cap_set_proc, capgetp, cap_get_bound, cap_drop_bound &#8211; capability manipulation on processes</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;sys/capability.h&gt;</code> </p>
<p> <code>cap_t cap_get_proc(void);</code> </p>
<p> <code>int cap_set_proc(cap_t </code><i>cap_p</i><code>);</code> </p>
<p> <code>int cap_get_bound(cap_value_t </code><i>cap</i><code>);</code> </p>
<p> <code>CAP_IS_SUPPORTED(cap_value_t </code><i>cap</i><code>);</code> </p>
<p> <code>int cap_drop_bound(cap_value_t </code><i>cap</i><code>);</code> </p>
<p> <code>#include &lt;sys/types.h&gt;</code> </p>
<p> <code>cap_t cap_get_pid(pid_t </code><i>pid</i><code>);</code> </p>
<p> Link with <i>-lcap</i>.</p>
<h2>DESCRIPTION</h2>
<p> <code>cap_get_proc</code>() allocates a capability state in working storage, sets its state to that of the calling process, and returns a pointer to this newly created capability state. The caller should free any releasable memory, when the capability state in working storage is no longer required, by calling <code>cap_free</code>() with the <i>cap_t</i> as an argument. </p>
<p> <code>cap_set_proc</code>() sets the values for all capability flags for all capabilities to the capability state identified by <i>cap_p</i>. The new capability state of the process will be completely determined by the contents of <i>cap_p</i> upon successful return from this function. If any flag in <i>cap_p</i> is set for any capability not currently permitted for the calling process, the function will fail, and the capability state of the process will remain unchanged. </p>
<p> <code>cap_get_pid</code>() returns <i>cap_d</i>, see <code><a href="/docs/linux/man/3-cap_init/">cap_init</a></code>(3), with the process capabilities of the process indicated by <i>pid</i>. This information can also be obtained from the <i>/proc/&lt;pid&gt;/status</i> file. </p>
<p> <code>cap_get_bound</code>() with a <i>cap</i> as an argument returns the current value of this bounding set capability flag in effect for the current process. This operation is unpriveged. Note, a macro function <code>CAP_IS_SUPPORTED(cap_value_t </code><i>cap</i><code>)</code> is provided that evaluates to true (1) if the system supports the specified capability, <i>cap</i>. If the system does not support the capability, this function returns 0. This macro works by testing for an error condition with <code>cap_get_bound</code>(). </p>
<p> <code>cap_drop_bound</code>() can be used to lower the specified bounding set capability, <code>cap</code>, To complete successfully, the prevailing <i>effective</i> capability set must have a raised <code>CAP_SETPCAP</code>.</p>
<h2>RETURN VALUE</h2>
<p> The functions <code>cap_get_proc</code>() and <code>cap_get_pid</code>() return a non-NULL value on success, and NULL on failure. </p>
<p> The function <code>cap_get_bound</code>() returns -1 if the requested capability is unknown, otherwise the return value reflects the current state of that capability in the prevailing bounding set. Note, a macro function, </p>
<p> The functions <code>cap_set_proc</code>() and <code>cap_drop_bound</code>() return zero for success, and -1 on failure. </p>
<p> On failure, <i>errno</i> is set to <code>EINVAL</code>, <code>EPERM,</code> or <code>ENOMEM</code>.</p>
<h2>CONFORMING TO</h2>
<p> <code>cap_set_proc</code>() and <code>cap_get_proc</code>() are specified in the withdrawn POSIX.1e draft specification. <code>cap_get_pid</code>() is a Linux extension.</p>
<h2>NOTES</h2>
<p> The library also supports the deprecated functions: </p>
<p> <code>int capgetp(pid_t </code><i>pid</i><code>, cap_t </code><i>cap_d</i><code>);</code> </p>
<p> <code>int capsetp(pid_t </code><i>pid</i><code>, cap_t </code><i>cap_d</i><code>);</code> </p>
<p> <code>capgetp</code>() attempts to obtain the capabilities of some other process; storing the capabilities in a pre-allocated <i>cap_d</i>.<i>See</i> <code>cap_init</code>() for information on allocating an empty capability set. This function, <code>capgetp</code>(), is deprecated, you should use <code>cap_get_pid</code>(). </p>
<p> <code>capsetp</code>() attempts to set the capabilities of some other process(es), <i>pid</i>. If <i>pid</i> is positive it refers to a specific process; if it is zero, it refers to the current process; -1 refers to all processes other than the current process and process &#8216;1&#8217; (typically <code><a href="/docs/linux/man/8-init/">init</a></code>(8)); other negative values refer to the <i>-pid</i> process group. In order to use this function, the kernel must support it and the current process must have <code>CAP_SETPCAP</code> raised in its Effective capability set. The capabilities set in the target process(es) are those contained in <i>cap_d</i>. Kernels that support filesystem capabilities redefine the semantics of <code>CAP_SETPCAP</code> and on such systems this function will always fail for any target not equal to the current process. <code>capsetp</code>() returns zero for success, and -1 on failure. </p>
<p> Where supported by the kernel, the function <code>capsetp</code>() should be used with care. It existed, primarily, to overcome an early lack of support for capabilities in the filesystems supported by Linux. Note that, by default, the only processes that have <code>CAP_SETPCAP</code> available to them are processes started as a kernel thread. (Typically this includes <code><a href="/docs/linux/man/8-init/">init</a></code>(8), kflushd and kswapd). You will need to recompile the kernel to modify this default.</p>
<h2>EXAMPLE</h2>
<p> The code segment below raises the <code>CAP_FOWNER</code> and <code>CAP_SETFCAP</code> effective capabilities for the caller: </p>
<pre><code>
cap_t caps;
cap_value_t cap_list[2];
if (!CAP_IS_SUPPORTED(CAP_SETFCAP))
    /* handle error */
    caps = cap_get_proc();
if (caps == NULL)
    /* handle error */;
cap_list[0] = CAP_FOWNER;
cap_list[1] = CAP_SETFCAP;
if (cap_set_flag(caps, CAP_EFFECTIVE, 2, cap_list, CAP_SET) == -1)
    /* handle error */;
if (cap_set_proc(caps) == -1)
    /* handle error */;
if (cap_free(caps) == -1)
    /* handle error */;
</code></pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libcap/">libcap</a></code>(3), <code><a href="/docs/linux/man/3-cap_clear/">cap_clear</a></code>(3), <code><a href="/docs/linux/man/3-cap_copy_ext/">cap_copy_ext</a></code>(3), <code><a href="/docs/linux/man/3-cap_from_text/">cap_from_text</a></code>(3), <code><a href="/docs/linux/man/3-cap_get_file/">cap_get_file</a></code>(3), <code><a href="/docs/linux/man/3-cap_init/">cap_init</a></code>(3), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7) </p>
<h2>Index</h2>
