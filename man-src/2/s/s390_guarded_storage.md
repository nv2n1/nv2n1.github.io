---
title: "s390_guarded_storage(2)"
name: "s390_guarded_storage"
section: "2"
letter: "s"
url: "/docs/linux/man/2-s390_guarded_storage/"
description: "s390_guarded_storage – operations with z/Architecture guarded storage facility"
---

<h2 class="name">NAME</h2>
<p> s390_guarded_storage &#8211; operations with z/Architecture guarded storage facility </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;asm/guarded_storage.h&gt;
int s390_guarded_storage(int command, struct gs_cb *gs_cb);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>s390_guarded_storage</code>() system call enables the use of the Guarded Storage Facility (a z/Architecture-specific feature) for user-space processes. </p>
<p> The guarded storage facility is a hardware feature that allows marking up to 64 memory regions (as of z14) as guarded; reading a pointer with a newly introduced &quot;Load Guarded&quot; (LGG) or &quot;Load Logical and Shift Guarded&quot; (LLGFSG) instructions will cause a range check on the loaded value and invoke a (previously set up) user-space handler if one of the guarded regions is affected. </p>
<p> The <i>command</i> argument indicates which function to perform. The following commands are supported:</p>
<dl>
<dt><code>GS_ENABLE</code></p>
<dd> Enable the guarded storage facility for the calling task. The initial content of the guarded storage control block will be all zeros. After enablement, user-space code can use the &quot;Load Guarded Storage Controls&quot; (LGSC) instruction (or the <code>load_gs_cb</code>() function wrapper provided in the <i>asm/guarded_storage.h</i> header) to load an arbitrary control block. While a task is enabled, the kernel will save and restore the calling content of the guarded storage registers on context switch.</p>
<dt><code>GS_DISABLE</code></p>
<dd> Disables the use of the guarded storage facility for the calling task. The kernel will cease to save and restore the content of the guarded storage registers, the task-specific content of these registers is lost.</p>
<dt><code>GS_SET_BC_CB</code></p>
<dd> Set a broadcast guarded storage control block to the one provided in the <i>gs_cb</i> argument. This is called per thread and associates a specific guarded storage control block with the calling task. This control block will be used in the broadcast command <code>GS_BROADCAST</code>.</p>
<dt><code>GS_CLEAR_BC_CB</code></p>
<dd> Clears the broadcast guarded storage control block. The guarded storage control block will no longer have the association established by the <code>GS_SET_BC_CB</code> command.</p>
<dt><code>GS_BROADCAST</code></p>
<dd> Sends a broadcast to all thread siblings of the calling task. Every sibling that has established a broadcast guarded storage control block will load this control block and will be enabled for guarded storage. The broadcast guarded storage control block is consumed; a second broadcast without a refresh of the stored control block with <code>GS_SET_BC_CB</code> will not have any effect.</dl>
<p> The <i>gs_cb</i> argument specifies the address of a guarded storage control block structure and is currently used only by the <code>GS_SET_BC_CB</code> command; all other aforementioned commands ignore this argument.</p>
<h2>RETURN VALUE</h2>
<p> On success, the return value of <code>s390_guarded_storage</code>() is 0. </p>
<p> On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EFAULT</code></p>
<dd> <i>command</i> was <code>GS_SET_BC_CB</code> and the copying of the guarded storage control block structure pointed by the <i>gs_cb</i> argument has failed.</p>
<dt><code>EINVAL</code></p>
<dd> The value provided in the <i>command</i> argument was not valid.</p>
<dt><code>ENOMEM</code></p>
<dd> <i>command</i> was one of <code>GS_ENABLE</code> or <code>GS_SET_BC_CB</code>, and the allocation of a new guarded storage control block has failed.</p>
<dt><code>EOPNOTSUPP</code></p>
<dd> The guarded storage facility is not supported by the hardware.</dl>
<h2>VERSIONS</h2>
<p> This system call is available since Linux 4.12.</p>
<h2>CONFORMING TO</h2>
<p> This Linux-specific system call is available only on the s390 architecture. </p>
<p> The guarded storage facility is available beginning with System z14.</p>
<h2>NOTES</h2>
<p> Glibc does not provide a wrapper for this system call, use <code><a href="/docs/linux/man/2-syscall/">syscall</a></code>(2) to call it. </p>
<p> The description of the guarded storage facility along with related instructions and Guarded Storage Control Block and Guarded Storage Event Parameter List structure layouts is available in &quot;z/Architecture Principles of Operations&quot; beginning from the twelfth edition. </p>
<p> The <i>gs_cb</i> structure has a field <i>gsepla</i> (Guarded Storage Event Parameter List Address), which is a user-space pointer to a Guarded Storage Event Parameter List structure (that contains the address of the aforementioned event handler in the <i>gseha</i> field), and its layout is available as a <code>gs_epl</code> structure type definition in the <i>asm/guarded_storage.h</i> header.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-syscall/">syscall</a></code>(2)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
