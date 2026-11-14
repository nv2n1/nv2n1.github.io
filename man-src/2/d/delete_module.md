---
title: "delete_module(2)"
name: "delete_module"
section: "2"
letter: "d"
url: "/docs/linux/man/2-delete_module/"
description: "delete_module – unload a kernel module"
---

<h2 class="name">NAME</h2>
<p> delete_module &#8211; unload a kernel module </p>
<h2>SYNOPSIS</h2>
<pre><code>
int delete_module(const char *name, int flags);
</code></pre>
<p> <i>Note</i>: No declaration of this system call is provided in glibc headers; see NOTES.</p>
<h2>DESCRIPTION</h2>
<p> The <code>delete_module</code>() system call attempts to remove the unused loadable module entry identified by <i>name</i>. If the module has an <i>exit</i> function, then that function is executed before unloading the module. The <i>flags</i> argument is used to modify the behavior of the system call, as described below. This system call requires privilege. </p>
<p> Module removal is attempted according to the following rules:</p>
<dl>
<dt>1.</p>
<dd> If there are other loaded modules that depend on (i.e., refer to symbols defined in) this module, then the call fails.</p>
<dt>2.</p>
<dd> Otherwise, if the reference count for the module (i.e., the number of processes currently using the module) is zero, then the module is immediately unloaded.</p>
<dt>3.</p>
<dd> If a module has a nonzero reference count, then the behavior depends on the bits set in <i>flags</i>. In normal usage (see NOTES), the <code>O_NONBLOCK</code> flag is always specified, and the <code>O_TRUNC</code> flag may additionally be specified.</p>
<dt>
<dd> The various combinations for <i>flags</i> have the following effect:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>flags == O_NONBLOCK</code></p>
<dd> The call returns immediately, with an error.</p>
<dt><code>flags == (O_NONBLOCK | O_TRUNC)</code></p>
<dd> The module is unloaded immediately, regardless of whether it has a nonzero reference count.</p>
<dt><code>(flags &amp; O_NONBLOCK) == 0</code></p>
<dd> If <i>flags</i> does not specify <code>O_NONBLOCK</code>, the following steps occur:</p>
<dl>
<dt>
<dd>
<dl>
<dt>*</p>
<dd> The module is marked so that no new references are permitted.</p>
<dt>*</p>
<dd> If the module&#8217;s reference count is nonzero, the caller is placed in an uninterruptible sleep state (<code>TASK_UNINTERRUPTIBLE</code>) until the reference count is zero, at which point the call unblocks.</p>
<dt>*</p>
<dd> The module is unloaded in the usual way.</dl>
</dl>
</dl>
</dl>
</dl>
<p> The <code>O_TRUNC</code> flag has one further effect on the rules described above. By default, if a module has an <i>init</i> function but no <i>exit</i> function, then an attempt to remove the module fails. However, if <code>O_TRUNC</code> was specified, this requirement is bypassed. </p>
<p> Using the <code>O_TRUNC</code> flag is dangerous! If the kernel was not built with <code>CONFIG_MODULE_FORCE_UNLOAD</code>, this flag is silently ignored. (Normally, <code>CONFIG_MODULE_FORCE_UNLOAD</code> is enabled.) Using this flag taints the kernel (TAINT_FORCED_RMMOD).</p>
<h2>RETURN VALUE</h2>
<p> On success, zero is returned. On error, -1 is returned and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EBUSY</code></p>
<dd> The module is not &quot;live&quot; (i.e., it is still being initialized or is already marked for removal); or, the module has an <i>init</i> function but has no <i>exit</i> function, and <code>O_TRUNC</code> was not specified in <i>flags</i>.</p>
<dt><code>EFAULT</code></p>
<dd> <i>name</i> refers to a location outside the process&#8217;s accessible address space.</p>
<dt><code>ENOENT</code></p>
<dd> No module by that name exists.</p>
<dt><code>EPERM</code></p>
<dd> The caller was not privileged (did not have the <code>CAP_SYS_MODULE</code> capability), or module unloading is disabled (see <i>/proc/sys/kernel/modules_disabled</i> in <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5)).</p>
<dt><code>EWOULDBLOCK</code></p>
<dd> Other modules depend on this module; or, <code>O_NONBLOCK</code> was specified in <i>flags</i>, but the reference count of this module is nonzero and <code>O_TRUNC</code> was not specified in <i>flags</i>.</dl>
<h2>CONFORMING TO</h2>
<p> <code>delete_module</code>() is Linux-specific.</p>
<h2>NOTES</h2>
<p> The <code>delete_module</code>() system call is not supported by glibc. No declaration is provided in glibc headers, but, through a quirk of history, glibc versions before 2.23 did export an ABI for this system call. Therefore, in order to employ this system call, it is (before glibc 2.23) sufficient to manually declare the interface in your code; alternatively, you can invoke the system call using <code><a href="/docs/linux/man/2-syscall/">syscall</a></code>(2). </p>
<p> The uninterruptible sleep that may occur if <code>O_NONBLOCK</code> is omitted from <i>flags</i> is considered undesirable, because the sleeping process is left in an unkillable state. As at Linux 3.7, specifying <code>O_NONBLOCK</code> is optional, but in future kernels it is likely to become mandatory.</p>
<h3>Linux 2.4 and earlier</h3>
<p> In Linux 2.4 and earlier, the system call took only one argument: </p>
<p> <code> int delete_module(const char *</code><i>name</i><code>);</code> </p>
<p> If <i>name</i> is NULL, all unused modules marked auto-clean are removed. </p>
<p> Some further details of differences in the behavior of <code>delete_module</code>() in Linux 2.4 and earlier are <i>not</i> currently explained in this manual page.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-create_module/">create_module</a></code>(2), <code><a href="/docs/linux/man/2-init_module/">init_module</a></code>(2), <code><a href="/docs/linux/man/2-query_module/">query_module</a></code>(2), <code><a href="/docs/linux/man/8-lsmod/">lsmod</a></code>(8), <code><a href="/docs/linux/man/8-modprobe/">modprobe</a></code>(8), <code><a href="/docs/linux/man/8-rmmod/">rmmod</a></code>(8)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
