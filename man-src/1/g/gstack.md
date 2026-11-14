---
title: "gstack(1)"
name: "gstack"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gstack/"
description: "gstack – print a stack trace of a running process"
---

<h2 class="name">NAME</h2>
<p> gstack &#8211; print a stack trace of a running process</p>
<h2>SYNOPSIS</h2>
<p> <code>gstack</code> pid </p>
<h2>DESCRIPTION</h2>
<p> <code>gstack</code> attaches to the active process named by the <code>pid</code> on the command line, and prints out an execution stack trace. If ELF symbols exist in the binary (usually the case unless you have run <a href="/docs/linux/man/1-strip/">strip</a>(1)), then symbolic addresses are printed as well. </p>
<p> If the process is part of a thread group, then <code>gstack</code> will print out a stack trace for each of the threads in the group. </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-nm/">nm</a>(1), <a href="/docs/linux/man/2-ptrace/">ptrace</a>(2), <a href="/docs/linux/man/1-gdb/">gdb</a>(1) </p>
<h2>AUTHORS</h2>
<p> Ross Thompson &lt;ross [at] whatsis.com&gt; </p>
<p> Red Hat, Inc. &lt;<a rel="nofollow" href="http://bugzilla.redhat.com/bugzilla">http://bugzilla.redhat.com/bugzilla</a>&gt; </p>
<h2>Index</h2>
