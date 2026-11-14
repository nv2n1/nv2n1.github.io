---
title: "flopen(3)"
name: "flopen"
section: "3"
letter: "f"
url: "/docs/linux/man/3-flopen/"
description: "flopen – reliably open and lock a file"
---

<h2 class="name">NAME</h2>
<p> <code>flopen</code> &#8211; reliably open and lock a file </p>
<h2>LIBRARY</h2>
<p> Lb libbsd</p>
<h2>SYNOPSIS</h2>
<p> In sys/fcntl.h In bsd/libutil.h Ft int Fn flopen const char *path int flags Ft int Fn flopen const char *path int flags mode_t mode</p>
<h2>DESCRIPTION</h2>
<p> The Fn flopen function opens or creates a file and acquires an exclusive lock on it. It is essentially equivalent with calling Fn open with the same parameters followed by Fn flock with an <i>operation</i> argument of <code>LOCK_EX</code> except that Fn flopen will attempt to detect and handle races that may occur between opening / creating the file and locking it. Thus, it is well suited for opening lock files, PID files, spool files, mailboxes and other kinds of files which are used for synchronization between processes. </p>
<p> If <i>flags</i> includes <code>O_NONBLOCK</code> and the file is already locked, Fn flopen will fail and set <i>errno</i> to <code>EWOULDBLOCK</code> </p>
<p> As with Fn open , the additional <i>mode</i> argument is required if <i>flags</i> includes <code>O_CREAT</code></p>
<h2>RETURN VALUES</h2>
<p> If successful, Fn flopen returns a valid file descriptor. Otherwise, it returns -1, and sets <i>errno</i> as described in <a href="/docs/linux/man/2-flock/">flock</a>(2) and <a href="/docs/linux/man/2-open/">open</a>(2).</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/2-errno/">errno</a>(2), <a href="/docs/linux/man/2-flock/">flock</a>(2), <a href="/docs/linux/man/2-open/">open</a>(2)</p>
<h2>AUTHORS</h2>
<p> An -nosplit The function and this manual page were written by An Dag-Erling Sm&oslash;rgrav Aq des [at] FreeBSD.org . </p>
<h2>Index</h2>
