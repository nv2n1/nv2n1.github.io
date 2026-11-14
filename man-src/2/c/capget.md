---
title: "capget(2)"
name: "capget"
section: "2"
letter: "c"
url: "/docs/linux/man/2-capget/"
description: "capget, capset – set/get capabilities of thread(s)"
---

<h2 class="name">NAME</h2>
<p> capget, capset &#8211; set/get capabilities of thread(s) </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;sys/capability.h&gt;</code> </p>
<p> <code>int capget(cap_user_header_t </code><i>hdrp</i><code>, cap_user_data_t </code><i>datap</i><code>);</code> </p>
<p> <code>int capset(cap_user_header_t </code><i>hdrp</i><code>, const cap_user_data_t </code><i>datap</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> These two system calls are the raw kernel interface for getting and setting thread capabilities. Not only are these system calls specific to Linux, but the kernel API is likely to change and use of these system calls (in particular the format of the <i>cap_user_*_t</i> types) is subject to extension with each kernel revision, but old programs will keep working. </p>
<p> The portable interfaces are <code><a href="/docs/linux/man/3-cap_set_proc/">cap_set_proc</a></code>(3) and <code><a href="/docs/linux/man/3-cap_get_proc/">cap_get_proc</a></code>(3); if possible, you should use those interfaces in applications.</p>
<h3>Current details</h3>
<p> Now that you have been warned, some current kernel details. The structures are defined as follows. </p>
<p> #define _LINUX_CAPABILITY_VERSION_1 0x19980330 #define _LINUX_CAPABILITY_U32S_1 1 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;V2 added in Linux 2.6.25;&nbsp;deprecated&nbsp;*/ #define _LINUX_CAPABILITY_VERSION_2 0x20071026 #define _LINUX_CAPABILITY_U32S_2 2 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;V3 added in Linux 2.6.26&nbsp;*/ #define _LINUX_CAPABILITY_VERSION_3 0x20080522 #define _LINUX_CAPABILITY_U32S_3 2 </p>
<p> typedef struct __user_cap_header_struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32 version;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;int pid; } *cap_user_header_t; </p>
<p> typedef struct __user_cap_data_struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32 effective;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32 permitted;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32 inheritable; } *cap_user_data_t; </p>
<p> The <i>effective</i>, <i>permitted</i>, and <i>inheritable</i> fields are bit masks of the capabilities defined in <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7). Note that the <code>CAP_*</code> values are bit indexes and need to be bit-shifted before ORing into the bit fields. To define the structures for passing to the system call, you have to use the <i>struct __user_cap_header_struct</i> and <i>struct __user_cap_data_struct</i> names because the typedefs are only pointers. </p>
<p> Kernels prior to 2.6.25 prefer 32-bit capabilities with version <code>_LINUX_CAPABILITY_VERSION_1</code>. Linux 2.6.25 added 64-bit capability sets, with version <code>_LINUX_CAPABILITY_VERSION_2</code>. There was, however, an API glitch, and Linux 2.6.26 added <code>_LINUX_CAPABILITY_VERSION_3</code> to fix the problem. </p>
<p> Note that 64-bit capabilities use <i>datap[0]</i> and <i>datap[1]</i>, whereas 32-bit capabilities use only <i>datap[0]</i>. </p>
<p> On kernels that support file capabilities (VFS capabilities support), these system calls behave slightly differently. This support was added as an option in Linux 2.6.24, and became fixed (nonoptional) in Linux 2.6.33. </p>
<p> For <code>capget</code>() calls, one can probe the capabilities of any process by specifying its process ID with the <i>hdrp-&gt;pid</i> field value. </p>
<p> For details on the data, see <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7).</p>
<h3>With VFS capabilities support</h3>
<p> VFS capabilities employ a file extended attribute (see <code><a href="/docs/linux/man/7-xattr/">xattr</a></code>(7)) to allow capabilities to be attached to executables. This privilege model obsoletes kernel support for one process asynchronously setting the capabilities of another. That is, on kernels that have VFS capabilities support, when calling <code>capset</code>(), the only permitted values for <i>hdrp-&gt;pid</i> are 0 or, equivalently, the value returned by <code><a href="/docs/linux/man/2-gettid/">gettid</a></code>(2).</p>
<h3>Without VFS capabilities support</h3>
<p> On older kernels that do not provide VFS capabilities support <code>capset</code>() can, if the caller has the <code>CAP_SETPCAP</code> capability, be used to change not only the caller&#8217;s own capabilities, but also the capabilities of other threads. The call operates on the capabilities of the thread specified by the <i>pid</i> field of <i>hdrp</i> when that is nonzero, or on the capabilities of the calling thread if <i>pid</i> is 0. If <i>pid</i> refers to a single-threaded process, then <i>pid</i> can be specified as a traditional process ID; operating on a thread of a multithreaded process requires a thread ID of the type returned by <code><a href="/docs/linux/man/2-gettid/">gettid</a></code>(2). For <code>capset</code>(), <i>pid</i> can also be: -1, meaning perform the change on all threads except the caller and <code><a href="/docs/linux/man/1-init/">init</a></code>(1); or a value less than -1, in which case the change is applied to all members of the process group whose ID is &#8211;<i>pid</i>.</p>
<h2>RETURN VALUE</h2>
<p> On success, zero is returned. On error, -1 is returned, and <i>errno</i> is set appropriately. </p>
<p> The calls fail with the error <code>EINVAL</code>, and set the <i>version</i> field of <i>hdrp</i> to the kernel preferred value of <code>_LINUX_CAPABILITY_VERSION_?</code> when an unsupported <i>version</i> value is specified. In this way, one can probe what the current preferred capability revision is.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EFAULT</code></p>
<dd> Bad memory address. <i>hdrp</i> must not be NULL. <i>datap</i> may be NULL only when the user is trying to determine the preferred capability version format supported by the kernel.</p>
<dt><code>EINVAL</code></p>
<dd> One of the arguments was invalid.</p>
<dt><code>EPERM</code></p>
<dd> An attempt was made to add a capability to the permitted set, or to set a capability in the effective set that is not in the permitted set.</p>
<dt><code>EPERM</code></p>
<dd> An attempt was made to add a capability to the inheritable set, and either:</p>
<dl>
<dt>
<dd>
<dl>
<dt>*</p>
<dd> that capability was not in the caller&#8217;s bounding set; or</p>
<dt>*</p>
<dd> the capability was not in the caller&#8217;s permitted set and the caller lacked the <code>CAP_SETPCAP</code> capability in its effective set.</dl>
</dl>
<dt><code>EPERM</code></p>
<dd> The caller attempted to use <code>capset</code>() to modify the capabilities of a thread other than itself, but lacked sufficient privilege. For kernels supporting VFS capabilities, this is never permitted. For kernels lacking VFS support, the <code>CAP_SETPCAP</code> capability is required. (A bug in kernels before 2.6.11 meant that this error could also occur if a thread without this capability tried to change its own capabilities by specifying the <i>pid</i> field as a nonzero value (i.e., the value returned by <code><a href="/docs/linux/man/2-getpid/">getpid</a></code>(2)) instead of 0.)</p>
<dt><code>ESRCH</code></p>
<dd> No such thread.</dl>
<h2>CONFORMING TO</h2>
<p> These system calls are Linux-specific.</p>
<h2>NOTES</h2>
<p> The portable interface to the capability querying and setting functions is provided by the <i>libcap</i> library and is available here: </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2), <code><a href="/docs/linux/man/2-gettid/">gettid</a></code>(2), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
