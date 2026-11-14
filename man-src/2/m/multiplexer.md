---
title: "multiplexer(2)"
name: "multiplexer"
section: "2"
letter: "m"
url: "/docs/linux/man/2-multiplexer/"
description: "afs_syscall, break, fattach, fdetach, ftime, getmsg, getpmsg, gtty, isastream, lock, madvise1, mpx, multiplexer, prof, profil, putmsg, putpmsg, security, stty, tuxcall, ulimit, vserver – unimplemen..."
---

<h2>NAME</h2>
<p> afs_syscall, break, fattach, fdetach, ftime, getmsg, getpmsg, gtty, isastream, lock, madvise1, mpx, multiplexer, prof, profil, putmsg, putpmsg, security, stty, tuxcall, ulimit, vserver &#8211; unimplemented system calls</p>
<h2>SYNOPSIS</h2>
<p> Unimplemented system calls.</p>
<h2>DESCRIPTION</h2>
<p> These system calls are not implemented in the Linux 2.6.22 kernel.</p>
<h2>RETURN VALUE</h2>
<p> These system calls always return -1 and set <i>errno</i> to <code>ENOSYS</code>.</p>
<h2>NOTES</h2>
<p> Note that <code><a href="/docs/linux/man/3-ftime/">ftime</a></code>(3), <code><a href="/docs/linux/man/3-profil/">profil</a></code>(3) and <code><a href="/docs/linux/man/3-ulimit/">ulimit</a></code>(3) are implemented as library functions. </p>
<p> Some system calls, like <code><a href="/docs/linux/man/2-alloc_hugepages/">alloc_hugepages</a></code>(2), <code><a href="/docs/linux/man/2-free_hugepages/">free_hugepages</a></code>(2), <code><a href="/docs/linux/man/2-ioperm/">ioperm</a></code>(2), <code><a href="/docs/linux/man/2-iopl/">iopl</a></code>(2), and <code><a href="/docs/linux/man/2-vm86/">vm86</a></code>(2) only exist on certain architectures. </p>
<p> Some system calls, like <code><a href="/docs/linux/man/2-ipc/">ipc</a></code>(2), <code><a href="/docs/linux/man/2-create_module/">create_module</a></code>(2), <code><a href="/docs/linux/man/2-init_module/">init_module</a></code>(2), and <code><a href="/docs/linux/man/2-delete_module/">delete_module</a></code>(2) only exist when the Linux kernel was built with support for them.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-syscalls/">syscalls</a></code>(2)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 3.35 of the Linux <i>man-pages</i> project. A description of the project, and information about reporting bugs, can be found at <a rel="nofollow" href="http://man7.org/linux/man-pages/.">http://man7.org/linux/man-pages/.</a> </p>
<h2>Index</h2>
