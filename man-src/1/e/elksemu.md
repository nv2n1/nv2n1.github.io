---
title: "elksemu(1)"
name: "elksemu"
section: "1"
letter: "e"
url: "/docs/linux/man/1-elksemu/"
description: "elksemu – Embedded Linux Kernel Subset emulator"
---

<h2 class="name">NAME</h2>
<p> elksemu &#8211; Embedded Linux Kernel Subset emulator </p>
<h2>SYNOPSIS</h2>
<p> <code>/lib/elksemu</code> <code>program</code> [<code>arguments</code>]</p>
<h2>DESCRIPTION</h2>
<p> <code>Elksemu</code> is a program that allows 8086 <code>ELKS</code> programs to be run under Linux-i386. These programs can be compiled using the <code><a href="/docs/linux/man/1-bcc/">bcc</a>(1)</code> C compiler. </p>
<p> Yom may use the <i>binfmt-misc</i> module under Linux 2.1.43 or greater as described in the elksemu README which will cause the kernel to run <i>elksemu</i> with the correct arguments whenever the user tries to execute an ELKS executable directly. </p>
<h2>OPTIONS</h2>
<p> There are no flag options to elksemu, the first argument is the name of the program to run the rest are arguments that are passed to the Elks program. </p>
<h2>SECURITY</h2>
<p> The <code>elksemu</code> program may be installed suid-root and in this event it is able to run execute only (chmod 111) elks executables and act correctly on the suid permission bits on any executable. This should be considered a security hazard so elksemu does <i>not</i> have to be installed suid-root. If you consider using this facility you should also be aware that it will override the &#8216;nosuid&#8217; <a href="/docs/linux/man/8-mount/">mount</a>(8) option. </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-bcc/">bcc</a>(1), <a href="/docs/linux/man/1-as86/">as86</a>(1), <a href="/docs/linux/man/1-ld86/">ld86</a>(1)</p>
<h2>BUGS</h2>
<p> Elksemu is incomplete. </p>
<p> The program may still have security bugs! </p>
<h2>Index</h2>
