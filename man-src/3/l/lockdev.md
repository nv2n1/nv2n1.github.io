---
title: "lockdev(3)"
name: "lockdev"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lockdev/"
description: "lockdev, liblockdev, dev_testlock, dev_lock, dev_relock, dev_unlock – manage device lockfiles"
---

<h2>NAME</h2>
<p> lockdev, liblockdev, dev_testlock, dev_lock, dev_relock, dev_unlock &#8211; manage device lockfiles</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;lockdev.h&gt;</code> </p>
<p> <code>pid_t dev_testlock( const char * </code><i>devname</i><code>);</code><br />
 <code>pid_t dev_lock( const char * </code><i>devname</i><code>);</code><br />
 <code>pid_t dev_relock( const char * </code><i>devname</i><code>, pid_t </code><i>pid</i><code>);</code><br />
 <code>pid_t dev_unlock( const char * </code><i>devname</i><code>, pid_t </code><i>pid</i><code>);</code> </p>
<p> <code>cc [ flag</code><i> &#8230; ] file</i><code> &#8230; -llockdev [ library</code><i> ] </i></p>
<h2>DESCRIPTION</h2>
<p> The <code>lockdev</code> functions act on device locks normally located in <code>/var/lock .</code> The lock is acquired creating a pair of files hardlinked between them and named after the device name (as mandated by FSSTND) and the device&#8217;s major and minor numbers (as in SVr4 locks). This permits to circumvent a problem using only the FSSTND lock method when the same device exists under different names (for convenience or when a device must be accessable by more than one group of users).<br />
 The lock file names are typically in the form <code>LCK..ttyS1</code> and <code>LK.000.004.065 ,</code> but is provided a way to easily modify them to use the library on different architectures. The content of those files is the pid of the process who owns the lock. </p>
<p> The <code>dev_testlock()</code> function simply checks if the device is in some way locked and if the owner of the lock is still active (otherwise it removes the lock). It recognise a valid lock even if only one of the two lock files exists (and is owned by an existing process), thus permitting a safe use of this library together with programs using only FSSTND or SVr4 lock style. </p>
<p> The <code>dev_lock() </code> function first checks if the device is already locked and then tries to acquire the lock building the two lock files. First it creates the file which name contains the major and minor numbers (in SVr4 style), then it creates the file with the device name in its name. This order reduces the clashes with other processes trying to lock the same device (even with a different name) and using this library. It has no problem with processes that uses only the FSSTND algorithm. </p>
<p> The <code>dev_relock() </code> function changes the owner of an existing lock; if the pid of the old owner is provided, then it checks if the lock was correctly assigned (otherwise there is the possibility of a process acquiring a lock which was owned by another unrelated process). If the device was not locked, locks it. </p>
<p> The <code>dev_unlock() </code> function removes the existing locks on the device. If the pid of the owner of the lock is provided, then it checks if the lock is assigned to that process, avoiding to remove locks assigned to other existing processes. </p>
<h2>RETURN VALUES</h2>
<p> All the functions in <code>lockdev</code> library return <code>ZERO </code> on successfull completion of the function (dev_testlock returns zero if there is no lock on the device), otherwise, if the device is currently locked by an existing process, they return the pid of the process owner of the lock. They return a negative number when some kind of error happens. Actually they all return only (-1). </p>
<h2>FILES</h2>
<p> /var/lock/LCK..&lt;device&gt;<br />
 /var/lock/LK.&lt;devmajor&gt;.&lt;major&gt;.&lt;minor&gt;<br />
 /usr/lib/liblockdev.so.1 </p>
<h2>HISTORY</h2>
<p> (c) 1997 by Fabrizio Polacco &lt;fab [at] prosa.it&gt;.<br />
 This program is free software; you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation; version 2 dated June, 1991. </p>
<h2>Index</h2>
