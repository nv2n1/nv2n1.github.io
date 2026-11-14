---
title: "swapoff(2)"
name: "swapoff"
section: "2"
letter: "s"
url: "/docs/linux/man/2-swapoff/"
description: "swapon, swapoff – start/stop swapping to file/device"
---

<h2 class="name">NAME</h2>
<p> swapon, swapoff &#8211; start/stop swapping to file/device </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;unistd.h&gt;</code><br />
 <code>#include &lt;sys/swap.h&gt;</code> </p>
<p> <code>int swapon(const char *</code><i>path</i><code>, int </code><i>swapflags</i><code>);</code><br />
 <code>int swapoff(const char *</code><i>path</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> <code>swapon</code>() sets the swap area to the file or block device specified by <i>path</i>. <code>swapoff</code>() stops swapping to the file or block device specified by <i>path</i>. </p>
<p> If the <code>SWAP_FLAG_PREFER</code> flag is specified in the <code>swapon</code>() <i>swapflags</i> argument, the new swap area will have a higher priority than default. The priority is encoded within <i>swapflags</i> as: </p>
<p> <i>(prio &lt;&lt; SWAP_FLAG_PRIO_SHIFT) &amp; SWAP_FLAG_PRIO_MASK</i> </p>
<p> If the <code>SWAP_FLAG_DISCARD</code> flag is specified in the <code>swapon</code>() <i>swapflags</i> argument, freed swap pages will be discarded before they are reused, if the swap device supports the discard or trim operation. (This may improve performance on some Solid State Devices, but often it does not.) See also NOTES. </p>
<p> These functions may be used only by a privileged process (one having the <code>CAP_SYS_ADMIN</code> capability).</p>
<h3>Priority</h3>
<p> Each swap area has a priority, either high or low. The default priority is low. Within the low-priority areas, newer areas are even lower priority than older areas. </p>
<p> All priorities set with <i>swapflags</i> are high-priority, higher than default. They may have any nonnegative value chosen by the caller. Higher numbers mean higher priority. </p>
<p> Swap pages are allocated from areas in priority order, highest priority first. For areas with different priorities, a higher-priority area is exhausted before using a lower-priority area. If two or more areas have the same priority, and it is the highest priority available, pages are allocated on a round-robin basis between them. </p>
<p> As of Linux 1.3.6, the kernel usually follows these rules, but there are exceptions.</p>
<h2>RETURN VALUE</h2>
<p> On success, zero is returned. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EBUSY</code></p>
<dd> (for <code>swapon</code>()) The specified <i>path</i> is already being used as a swap area.</p>
<dt><code>EINVAL</code></p>
<dd> The file <i>path</i> exists, but refers neither to a regular file nor to a block device;</p>
<dt><code>EINVAL</code></p>
<dd> (<code>swapon</code>()) The indicated path does not contain a valid swap signature or resides on an in-memory filesystem such as <code><a href="/docs/linux/man/5-tmpfs/">tmpfs</a></code>(5).</p>
<dt><code>EINVAL</code> (since Linux 3.4)</p>
<dd> (<code>swapon</code>()) An invalid flag value was specified in <i>swapflags</i>.</p>
<dt><code>EINVAL</code></p>
<dd> (<code>swapoff</code>()) <i>path</i> is not currently a swap area.</p>
<dt><code>ENFILE</code></p>
<dd> The system-wide limit on the total number of open files has been reached.</p>
<dt><code>ENOENT</code></p>
<dd> The file <i>path</i> does not exist.</p>
<dt><code>ENOMEM</code></p>
<dd> The system has insufficient memory to start swapping.</p>
<dt><code>EPERM</code></p>
<dd> The caller does not have the <code>CAP_SYS_ADMIN</code> capability. Alternatively, the maximum number of swap files are already in use; see NOTES below.</dl>
<h2>CONFORMING TO</h2>
<p> These functions are Linux-specific and should not be used in programs intended to be portable. The second <i>swapflags</i> argument was introduced in Linux 1.3.2.</p>
<h2>NOTES</h2>
<p> The partition or path must be prepared with <code><a href="/docs/linux/man/8-mkswap/">mkswap</a></code>(8). </p>
<p> There is an upper limit on the number of swap files that may be used, defined by the kernel constant <code>MAX_SWAPFILES</code>. Before kernel 2.4.10, <code>MAX_SWAPFILES</code> has the value 8; since kernel 2.4.10, it has the value 32. Since kernel 2.6.18, the limit is decreased by 2 (thus: 30) if the kernel is built with the <code>CONFIG_MIGRATION</code> option (which reserves two swap table entries for the page migration features of <code><a href="/docs/linux/man/2-mbind/">mbind</a></code>(2) and <code><a href="/docs/linux/man/2-migrate_pages/">migrate_pages</a></code>(2)). Since kernel 2.6.32, the limit is further decreased by 1 if the kernel is built with the <code>CONFIG_MEMORY_FAILURE</code> option. </p>
<p> Discard of swap pages was introduced in kernel 2.6.29, then made conditional on the <code>SWAP_FLAG_DISCARD</code> flag in kernel 2.6.36, which still discards the entire swap area when <code>swapon</code>() is called, even if that flag bit is not set.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-mkswap/">mkswap</a></code>(8), <code><a href="/docs/linux/man/8-swapoff/">swapoff</a></code>(8), <code><a href="/docs/linux/man/8-swapon/">swapon</a></code>(8)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
