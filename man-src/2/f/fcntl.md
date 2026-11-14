---
title: "fcntl(2)"
name: "fcntl"
section: "2"
letter: "f"
url: "/docs/linux/man/2-fcntl/"
description: "fcntl – manipulate file descriptor"
---

<h2 class="name">NAME</h2>
<p> fcntl &#8211; manipulate file descriptor </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;fcntl.h&gt;
#include &lt;unistd.h&gt;
int fcntl(int fd, int cmd, ... /* arg */);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>fcntl</code>() performs one of the operations described below on the open file descriptor <i>fd</i>. The operation is determined by <i>cmd</i>. </p>
<p> <code>fcntl</code>() can take an optional third argument. Whether or not this argument is required is determined by <i>cmd</i>. The required argument type is indicated in parentheses after each <i>cmd</i> name (in most cases, the required type is <i>int</i>, and we identify the argument using the name <i>arg</i>), or <i>void</i> is specified if the argument is not required. </p>
<p> Certain of the operations below are supported only since a particular Linux kernel version. The preferred method of checking whether the host kernel supports a particular operation is to invoke <code>fcntl</code>() with the desired <i>cmd</i> value and then test whether the call failed with <code>EINVAL</code>, indicating that the kernel does not recognize this value.</p>
<h3>Duplicating a file descriptor</h3>
<dl>
<dt><code>F_DUPFD</code> (<i>int</i>)</p>
<dd> Duplicate the file descriptor <i>fd</i> using the lowest-numbered available file descriptor greater than or equal to <i>arg</i>. This is different from <code><a href="/docs/linux/man/2-dup2/">dup2</a></code>(2), which uses exactly the file descriptor specified.</p>
<dt>
<dd> On success, the new file descriptor is returned.</p>
<dt>
<dd> See <code><a href="/docs/linux/man/2-dup/">dup</a></code>(2) for further details.</p>
<dt><code>F_DUPFD_CLOEXEC</code> (<i>int</i>; since Linux 2.6.24)</p>
<dd> As for <code>F_DUPFD</code>, but additionally set the close-on-exec flag for the duplicate file descriptor. Specifying this flag permits a program to avoid an additional <code>fcntl</code>() <code>F_SETFD</code> operation to set the <code>FD_CLOEXEC</code> flag. For an explanation of why this flag is useful, see the description of <code>O_CLOEXEC</code> in <code><a href="/docs/linux/man/2-open/">open</a></code>(2).</dl>
<h3>File descriptor flags</h3>
<p> The following commands manipulate the flags associated with a file descriptor. Currently, only one such flag is defined: <code>FD_CLOEXEC</code>, the close-on-exec flag. If the <code>FD_CLOEXEC</code> bit is set, the file descriptor will automatically be closed during a successful <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2). (If the <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) fails, the file descriptor is left open.) If the <code>FD_CLOEXEC</code> bit is not set, the file descriptor will remain open across an <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2).</p>
<dl>
<dt><code>F_GETFD</code> (<i>void</i>)</p>
<dd> Return (as the function result) the file descriptor flags; <i>arg</i> is ignored.</p>
<dt><code>F_SETFD</code> (<i>int</i>)</p>
<dd> Set the file descriptor flags to the value specified by <i>arg</i>.</dl>
<p> In multithreaded programs, using <code>fcntl</code>() <code>F_SETFD</code> to set the close-on-exec flag at the same time as another thread performs a <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) plus <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) is vulnerable to a race condition that may unintentionally leak the file descriptor to the program executed in the child process. See the discussion of the <code>O_CLOEXEC</code> flag in <code><a href="/docs/linux/man/2-open/">open</a></code>(2) for details and a remedy to the problem.</p>
<h3>File status flags</h3>
<p> Each open file description has certain associated status flags, initialized by <code><a href="/docs/linux/man/2-open/">open</a></code>(2) and possibly modified by <code>fcntl</code>(). Duplicated file descriptors (made with <code><a href="/docs/linux/man/2-dup/">dup</a></code>(2), <code>fcntl</code>(F_DUPFD), <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2), etc.) refer to the same open file description, and thus share the same file status flags. </p>
<p> The file status flags and their semantics are described in <code><a href="/docs/linux/man/2-open/">open</a></code>(2).</p>
<dl>
<dt><code>F_GETFL</code> (<i>void</i>)</p>
<dd> Return (as the function result) the file access mode and the file status flags; <i>arg</i> is ignored.</p>
<dt><code>F_SETFL</code> (<i>int</i>)</p>
<dd> Set the file status flags to the value specified by <i>arg</i>. File access mode (<code>O_RDONLY</code>, <code>O_WRONLY</code>, <code>O_RDWR</code>) and file creation flags (i.e., <code>O_CREAT</code>, <code>O_EXCL</code>, <code>O_NOCTTY</code>, <code>O_TRUNC</code>) in <i>arg</i> are ignored. On Linux, this command can change only the <code>O_APPEND</code>, <code>O_ASYNC</code>, <code>O_DIRECT</code>, <code>O_NOATIME</code>, and <code>O_NONBLOCK</code> flags. It is not possible to change the <code>O_DSYNC</code> and <code>O_SYNC</code> flags; see BUGS, below.</dl>
<h3>Advisory record locking</h3>
<p> Linux implements traditional (&quot;process-associated&quot;) UNIX record locks, as standardized by POSIX. For a Linux-specific alternative with better semantics, see the discussion of open file description locks below. </p>
<p> <code>F_SETLK</code>, <code>F_SETLKW</code>, and <code>F_GETLK</code> are used to acquire, release, and test for the existence of record locks (also known as byte-range, file-segment, or file-region locks). The third argument, <i>lock</i>, is a pointer to a structure that has at least the following fields (in unspecified order). </p>
<p> struct flock {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8230;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;short l_type;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Type of lock: F_RDLCK,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;F_WRLCK, F_UNLCK&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;short l_whence;&nbsp;<wbr>&nbsp;/*&nbsp;How to interpret l_start:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;SEEK_SET, SEEK_CUR, SEEK_END&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;off_t l_start;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Starting offset for lock&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;off_t l_len;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Number of bytes to lock&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pid_t l_pid;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;PID of process blocking our lock<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(set by F_GETLK and F_OFD_GETLK)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8230; }; </p>
<p> The <i>l_whence</i>, <i>l_start</i>, and <i>l_len</i> fields of this structure specify the range of bytes we wish to lock. Bytes past the end of the file may be locked, but not bytes before the start of the file. </p>
<p> <i>l_start</i> is the starting offset for the lock, and is interpreted relative to either: the start of the file (if <i>l_whence</i> is <code>SEEK_SET</code>); the current file offset (if <i>l_whence</i> is <code>SEEK_CUR</code>); or the end of the file (if <i>l_whence</i> is <code>SEEK_END</code>). In the final two cases, <i>l_start</i> can be a negative number provided the offset does not lie before the start of the file. </p>
<p> <i>l_len</i> specifies the number of bytes to be locked. If <i>l_len</i> is positive, then the range to be locked covers bytes <i>l_start</i> up to and including <i>l_start</i>+<i>l_len</i>-1. Specifying 0 for <i>l_len</i> has the special meaning: lock all bytes starting at the location specified by <i>l_whence</i> and <i>l_start</i> through to the end of file, no matter how large the file grows. </p>
<p> POSIX.1-2001 allows (but does not require) an implementation to support a negative <i>l_len</i> value; if <i>l_len</i> is negative, the interval described by <i>lock</i> covers bytes <i>l_start</i>+<i>l_len</i> up to and including <i>l_start</i>-1. This is supported by Linux since kernel versions 2.4.21 and 2.5.49. </p>
<p> The <i>l_type</i> field can be used to place a read (<code>F_RDLCK</code>) or a write (<code>F_WRLCK</code>) lock on a file. Any number of processes may hold a read lock (shared lock) on a file region, but only one process may hold a write lock (exclusive lock). An exclusive lock excludes all other locks, both shared and exclusive. A single process can hold only one type of lock on a file region; if a new lock is applied to an already-locked region, then the existing lock is converted to the new lock type. (Such conversions may involve splitting, shrinking, or coalescing with an existing lock if the byte range specified by the new lock does not precisely coincide with the range of the existing lock.)</p>
<dl>
<dt><code>F_SETLK</code> (<i>struct flock *</i>)</p>
<dd> Acquire a lock (when <i>l_type</i> is <code>F_RDLCK</code> or <code>F_WRLCK</code>) or release a lock (when <i>l_type</i> is <code>F_UNLCK</code>) on the bytes specified by the <i>l_whence</i>, <i>l_start</i>, and <i>l_len</i> fields of <i>lock</i>. If a conflicting lock is held by another process, this call returns -1 and sets <i>errno</i> to <code>EACCES</code> or <code>EAGAIN</code>. (The error returned in this case differs across implementations, so POSIX requires a portable application to check for both errors.)</p>
<dt><code>F_SETLKW</code> (<i>struct flock *</i>)</p>
<dd> As for <code>F_SETLK</code>, but if a conflicting lock is held on the file, then wait for that lock to be released. If a signal is caught while waiting, then the call is interrupted and (after the signal handler has returned) returns immediately (with return value -1 and <i>errno</i> set to <code>EINTR</code>; see <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7)).</p>
<dt><code>F_GETLK</code> (<i>struct flock *</i>)</p>
<dd> On input to this call, <i>lock</i> describes a lock we would like to place on the file. If the lock could be placed, <code>fcntl</code>() does not actually place it, but returns <code>F_UNLCK</code> in the <i>l_type</i> field of <i>lock</i> and leaves the other fields of the structure unchanged.</p>
<dt>
<dd> If one or more incompatible locks would prevent this lock being placed, then <code>fcntl</code>() returns details about one of those locks in the <i>l_type</i>, <i>l_whence</i>, <i>l_start</i>, and <i>l_len</i> fields of <i>lock</i>. If the conflicting lock is a traditional (process-associated) record lock, then the <i>l_pid</i> field is set to the PID of the process holding that lock. If the conflicting lock is an open file description lock, then <i>l_pid</i> is set to -1. Note that the returned information may already be out of date by the time the caller inspects it.</dl>
<p> In order to place a read lock, <i>fd</i> must be open for reading. In order to place a write lock, <i>fd</i> must be open for writing. To place both types of lock, open a file read-write. </p>
<p> When placing locks with <code>F_SETLKW</code>, the kernel detects <i>deadlocks</i>, whereby two or more processes have their lock requests mutually blocked by locks held by the other processes. For example, suppose process A holds a write lock on byte 100 of a file, and process B holds a write lock on byte 200. If each process then attempts to lock the byte already locked by the other process using <code>F_SETLKW</code>, then, without deadlock detection, both processes would remain blocked indefinitely. When the kernel detects such deadlocks, it causes one of the blocking lock requests to immediately fail with the error <code>EDEADLK</code>; an application that encounters such an error should release some of its locks to allow other applications to proceed before attempting regain the locks that it requires. Circular deadlocks involving more than two processes are also detected. Note, however, that there are limitations to the kernel&#8217;s deadlock-detection algorithm; see BUGS. </p>
<p> As well as being removed by an explicit <code>F_UNLCK</code>, record locks are automatically released when the process terminates. </p>
<p> Record locks are not inherited by a child created via <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2), but are preserved across an <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2). </p>
<p> Because of the buffering performed by the <code><a href="/docs/linux/man/3-stdio/">stdio</a></code>(3) library, the use of record locking with routines in that package should be avoided; use <code><a href="/docs/linux/man/2-read/">read</a></code>(2) and <code><a href="/docs/linux/man/2-write/">write</a></code>(2) instead. </p>
<p> The record locks described above are associated with the process (unlike the open file description locks described below). This has some unfortunate consequences:</p>
<dl>
<dt>*</p>
<dd> If a process closes <i>any</i> file descriptor referring to a file, then all of the process&#8217;s locks on that file are released, regardless of the file descriptor(s) on which the locks were obtained. This is bad: it means that a process can lose its locks on a file such as <i>/etc/passwd</i> or <i>/etc/mtab</i> when for some reason a library function decides to open, read, and close the same file.</p>
<dt>*</p>
<dd> The threads in a process share locks. In other words, a multithreaded program can&#8217;t use record locking to ensure that threads don&#8217;t simultaneously access the same region of a file.</dl>
<p> Open file description locks solve both of these problems.</p>
<h3>Open file description locks (non-POSIX)</h3>
<p> Open file description locks are advisory byte-range locks whose operation is in most respects identical to the traditional record locks described above. This lock type is Linux-specific, and available since Linux 3.15. (There is a proposal with the Austin Group to include this lock type in the next revision of POSIX.1.) For an explanation of open file descriptions, see <code><a href="/docs/linux/man/2-open/">open</a></code>(2). </p>
<p> The principal difference between the two lock types is that whereas traditional record locks are associated with a process, open file description locks are associated with the open file description on which they are acquired, much like locks acquired with <code><a href="/docs/linux/man/2-flock/">flock</a></code>(2). Consequently (and unlike traditional advisory record locks), open file description locks are inherited across <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) (and <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) with <code>CLONE_FILES</code>), and are only automatically released on the last close of the open file description, instead of being released on any close of the file. </p>
<p> Conflicting lock combinations (i.e., a read lock and a write lock or two write locks) where one lock is an open file description lock and the other is a traditional record lock conflict even when they are acquired by the same process on the same file descriptor. </p>
<p> Open file description locks placed via the same open file description (i.e., via the same file descriptor, or via a duplicate of the file descriptor created by <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2), <code><a href="/docs/linux/man/2-dup/">dup</a></code>(2), <code>fcntl</code>() <code>F_DUPFD</code>, and so on) are always compatible: if a new lock is placed on an already locked region, then the existing lock is converted to the new lock type. (Such conversions may result in splitting, shrinking, or coalescing with an existing lock as discussed above.) </p>
<p> On the other hand, open file description locks may conflict with each other when they are acquired via different open file descriptions. Thus, the threads in a multithreaded program can use open file description locks to synchronize access to a file region by having each thread perform its own <code><a href="/docs/linux/man/2-open/">open</a></code>(2) on the file and applying locks via the resulting file descriptor. </p>
<p> As with traditional advisory locks, the third argument to <code>fcntl</code>(), <i>lock</i>, is a pointer to an <i>flock</i> structure. By contrast with traditional record locks, the <i>l_pid</i> field of that structure must be set to zero when using the commands described below. </p>
<p> The commands for working with open file description locks are analogous to those used with traditional locks:</p>
<dl>
<dt><code>F_OFD_SETLK</code> (<i>struct flock *</i>)</p>
<dd> Acquire an open file description lock (when <i>l_type</i> is <code>F_RDLCK</code> or <code>F_WRLCK</code>) or release an open file description lock (when <i>l_type</i> is <code>F_UNLCK</code>) on the bytes specified by the <i>l_whence</i>, <i>l_start</i>, and <i>l_len</i> fields of <i>lock</i>. If a conflicting lock is held by another process, this call returns -1 and sets <i>errno</i> to <code>EAGAIN</code>.</p>
<dt><code>F_OFD_SETLKW</code> (<i>struct flock *</i>)</p>
<dd> As for <code>F_OFD_SETLK</code>, but if a conflicting lock is held on the file, then wait for that lock to be released. If a signal is caught while waiting, then the call is interrupted and (after the signal handler has returned) returns immediately (with return value -1 and <i>errno</i> set to <code>EINTR</code>; see <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7)).</p>
<dt><code>F_OFD_GETLK</code> (<i>struct flock *</i>)</p>
<dd> On input to this call, <i>lock</i> describes an open file description lock we would like to place on the file. If the lock could be placed, <code>fcntl</code>() does not actually place it, but returns <code>F_UNLCK</code> in the <i>l_type</i> field of <i>lock</i> and leaves the other fields of the structure unchanged. If one or more incompatible locks would prevent this lock being placed, then details about one of these locks are returned via <i>lock</i>, as described above for <code>F_GETLK</code>.</dl>
<p> In the current implementation, no deadlock detection is performed for open file description locks. (This contrasts with process-associated record locks, for which the kernel does perform deadlock detection.)</p>
<h3>Mandatory locking</h3>
<p> <i>Warning</i>: the Linux implementation of mandatory locking is unreliable. See BUGS below. Because of these bugs, and the fact that the feature is believed to be little used, since Linux 4.5, mandatory locking has been made an optional feature, governed by a configuration option (<code>CONFIG_MANDATORY_FILE_LOCKING</code>). This is an initial step toward removing this feature completely. </p>
<p> By default, both traditional (process-associated) and open file description record locks are advisory. Advisory locks are not enforced and are useful only between cooperating processes. </p>
<p> Both lock types can also be mandatory. Mandatory locks are enforced for all processes. If a process tries to perform an incompatible access (e.g., <code><a href="/docs/linux/man/2-read/">read</a></code>(2) or <code><a href="/docs/linux/man/2-write/">write</a></code>(2)) on a file region that has an incompatible mandatory lock, then the result depends upon whether the <code>O_NONBLOCK</code> flag is enabled for its open file description. If the <code>O_NONBLOCK</code> flag is not enabled, then the system call is blocked until the lock is removed or converted to a mode that is compatible with the access. If the <code>O_NONBLOCK</code> flag is enabled, then the system call fails with the error <code>EAGAIN</code>. </p>
<p> To make use of mandatory locks, mandatory locking must be enabled both on the filesystem that contains the file to be locked, and on the file itself. Mandatory locking is enabled on a filesystem using the &quot;-o mand&quot; option to <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8), or the <code>MS_MANDLOCK</code> flag for <code><a href="/docs/linux/man/2-mount/">mount</a></code>(2). Mandatory locking is enabled on a file by disabling group execute permission on the file and enabling the set-group-ID permission bit (see <code><a href="/docs/linux/man/1-chmod/">chmod</a></code>(1) and <code><a href="/docs/linux/man/2-chmod/">chmod</a></code>(2)). </p>
<p> Mandatory locking is not specified by POSIX. Some other systems also support mandatory locking, although the details of how to enable it vary across systems.</p>
<h3>Lost locks</h3>
<p> When an advisory lock is obtained on a networked filesystem such as NFS it is possible that the lock might get lost. This may happen due to administrative action on the server, or due to a network partition (i.e., loss of network connectivity with the server) which lasts long enough for the server to assume that the client is no longer functioning. </p>
<p> When the filesystem determines that a lock has been lost, future <code><a href="/docs/linux/man/2-read/">read</a></code>(2) or <code><a href="/docs/linux/man/2-write/">write</a></code>(2) requests may fail with the error <code>EIO</code>. This error will persist until the lock is removed or the file descriptor is closed. Since Linux 3.12, this happens at least for NFSv4 (including all minor versions). </p>
<p> Some versions of UNIX send a signal (<code>SIGLOST</code>) in this circumstance. Linux does not define this signal, and does not provide any asynchronous notification of lost locks.</p>
<h3>Managing signals</h3>
<p> <code>F_GETOWN</code>, <code>F_SETOWN</code>, <code>F_GETOWN_EX</code>, <code>F_SETOWN_EX</code>, <code>F_GETSIG</code>, and <code>F_SETSIG</code> are used to manage I/O availability signals:</p>
<dl>
<dt><code>F_GETOWN</code> (<i>void</i>)</p>
<dd> Return (as the function result) the process ID or process group ID currently receiving <code>SIGIO</code> and <code>SIGURG</code> signals for events on file descriptor <i>fd</i>. Process IDs are returned as positive values; process group IDs are returned as negative values (but see BUGS below). <i>arg</i> is ignored.</p>
<dt><code>F_SETOWN</code> (<i>int</i>)</p>
<dd> Set the process ID or process group ID that will receive <code>SIGIO</code> and <code>SIGURG</code> signals for events on the file descriptor <i>fd</i>. The target process or process group ID is specified in <i>arg</i>. A process ID is specified as a positive value; a process group ID is specified as a negative value. Most commonly, the calling process specifies itself as the owner (that is, <i>arg</i> is specified as <code><a href="/docs/linux/man/2-getpid/">getpid</a></code>(2)).</p>
<dt>
<dd> As well as setting the file descriptor owner, one must also enable generation of signals on the file descriptor. This is done by using the <code>fcntl</code>() <code>F_SETFL</code> command to set the <code>O_ASYNC</code> file status flag on the file descriptor. Subsequently, a <code>SIGIO</code> signal is sent whenever input or output becomes possible on the file descriptor. The <code>fcntl</code>() <code>F_SETSIG</code> command can be used to obtain delivery of a signal other than <code>SIGIO</code>.</p>
<dt>
<dd> Sending a signal to the owner process (group) specified by <code>F_SETOWN</code> is subject to the same permissions checks as are described for <code><a href="/docs/linux/man/2-kill/">kill</a></code>(2), where the sending process is the one that employs <code>F_SETOWN</code> (but see BUGS below). If this permission check fails, then the signal is silently discarded. <i>Note</i>: The <code>F_SETOWN</code> operation records the caller&#8217;s credentials at the time of the <code>fcntl</code>() call, and it is these saved credentials that are used for the permission checks.</p>
<dt>
<dd> If the file descriptor <i>fd</i> refers to a socket, <code>F_SETOWN</code> also selects the recipient of <code>SIGURG</code> signals that are delivered when out-of-band data arrives on that socket. (<code>SIGURG</code> is sent in any situation where <code><a href="/docs/linux/man/2-select/">select</a></code>(2) would report the socket as having an &quot;exceptional condition&quot;.)</p>
<dt>
<dd> The following was true in 2.6.x kernels up to and including kernel 2.6.11:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> If a nonzero value is given to <code>F_SETSIG</code> in a multithreaded process running with a threading library that supports thread groups (e.g., NPTL), then a positive value given to <code>F_SETOWN</code> has a different meaning: instead of being a process ID identifying a whole process, it is a thread ID identifying a specific thread within a process. Consequently, it may be necessary to pass <code>F_SETOWN</code> the result of <code><a href="/docs/linux/man/2-gettid/">gettid</a></code>(2) instead of <code><a href="/docs/linux/man/2-getpid/">getpid</a></code>(2) to get sensible results when <code>F_SETSIG</code> is used. (In current Linux threading implementations, a main thread&#8217;s thread ID is the same as its process ID. This means that a single-threaded program can equally use <code><a href="/docs/linux/man/2-gettid/">gettid</a></code>(2) or <code><a href="/docs/linux/man/2-getpid/">getpid</a></code>(2) in this scenario.) Note, however, that the statements in this paragraph do not apply to the <code>SIGURG</code> signal generated for out-of-band data on a socket: this signal is always sent to either a process or a process group, depending on the value given to <code>F_SETOWN</code>.</dl>
</dl>
<dt>
<dd> The above behavior was accidentally dropped in Linux 2.6.12, and won&#8217;t be restored. From Linux 2.6.32 onward, use <code>F_SETOWN_EX</code> to target <code>SIGIO</code> and <code>SIGURG</code> signals at a particular thread.</p>
<dt><code>F_GETOWN_EX</code> (<i>struct f_owner_ex *</i>) (since Linux 2.6.32)</p>
<dd> Return the current file descriptor owner settings as defined by a previous <code>F_SETOWN_EX</code> operation. The information is returned in the structure pointed to by <i>arg</i>, which has the following form:</p>
<dt>
<dd> struct f_owner_ex {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;type;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pid_t pid; };</p>
<dt>
<dd> The <i>type</i> field will have one of the values <code>F_OWNER_TID</code>, <code>F_OWNER_PID</code>, or <code>F_OWNER_PGRP</code>. The <i>pid</i> field is a positive integer representing a thread ID, process ID, or process group ID. See <code>F_SETOWN_EX</code> for more details.</p>
<dt><code>F_SETOWN_EX</code> (<i>struct f_owner_ex *</i>) (since Linux 2.6.32)</p>
<dd> This operation performs a similar task to <code>F_SETOWN</code>. It allows the caller to direct I/O availability signals to a specific thread, process, or process group. The caller specifies the target of signals via <i>arg</i>, which is a pointer to a <i>f_owner_ex</i> structure. The <i>type</i> field has one of the following values, which define how <i>pid</i> is interpreted:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>F_OWNER_TID</code></p>
<dd> Send the signal to the thread whose thread ID (the value returned by a call to <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) or <code><a href="/docs/linux/man/2-gettid/">gettid</a></code>(2)) is specified in <i>pid</i>.</p>
<dt><code>F_OWNER_PID</code></p>
<dd> Send the signal to the process whose ID is specified in <i>pid</i>.</p>
<dt><code>F_OWNER_PGRP</code></p>
<dd> Send the signal to the process group whose ID is specified in <i>pid</i>. (Note that, unlike with <code>F_SETOWN</code>, a process group ID is specified as a positive value here.)</dl>
</dl>
<dt><code>F_GETSIG</code> (<i>void</i>)</p>
<dd> Return (as the function result) the signal sent when input or output becomes possible. A value of zero means <code>SIGIO</code> is sent. Any other value (including <code>SIGIO</code>) is the signal sent instead, and in this case additional info is available to the signal handler if installed with <code>SA_SIGINFO</code>. <i>arg</i> is ignored.</p>
<dt><code>F_SETSIG</code> (<i>int</i>)</p>
<dd> Set the signal sent when input or output becomes possible to the value given in <i>arg</i>. A value of zero means to send the default <code>SIGIO</code> signal. Any other value (including <code>SIGIO</code>) is the signal to send instead, and in this case additional info is available to the signal handler if installed with <code>SA_SIGINFO</code>.</p>
<dt>
<dd> By using <code>F_SETSIG</code> with a nonzero value, and setting <code>SA_SIGINFO</code> for the signal handler (see <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2)), extra information about I/O events is passed to the handler in a <i>siginfo_t</i> structure. If the <i>si_code</i> field indicates the source is <code>SI_SIGIO</code>, the <i>si_fd</i> field gives the file descriptor associated with the event. Otherwise, there is no indication which file descriptors are pending, and you should use the usual mechanisms (<code><a href="/docs/linux/man/2-select/">select</a></code>(2), <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2), <code><a href="/docs/linux/man/2-read/">read</a></code>(2) with <code>O_NONBLOCK</code> set etc.) to determine which file descriptors are available for I/O.</p>
<dt>
<dd> Note that the file descriptor provided in <i>si_fd</i> is the one that was specified during the <code>F_SETSIG</code> operation. This can lead to an unusual corner case. If the file descriptor is duplicated (<code><a href="/docs/linux/man/2-dup/">dup</a></code>(2) or similar), and the original file descriptor is closed, then I/O events will continue to be generated, but the <i>si_fd</i> field will contain the number of the now closed file descriptor.</p>
<dt>
<dd> By selecting a real time signal (value &gt;= <code>SIGRTMIN</code>), multiple I/O events may be queued using the same signal numbers. (Queuing is dependent on available memory.) Extra information is available if <code>SA_SIGINFO</code> is set for the signal handler, as above.</p>
<dt>
<dd> Note that Linux imposes a limit on the number of real-time signals that may be queued to a process (see <code><a href="/docs/linux/man/2-getrlimit/">getrlimit</a></code>(2) and <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7)) and if this limit is reached, then the kernel reverts to delivering <code>SIGIO</code>, and this signal is delivered to the entire process rather than to a specific thread.</dl>
<p> Using these mechanisms, a program can implement fully asynchronous I/O without using <code><a href="/docs/linux/man/2-select/">select</a></code>(2) or <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2) most of the time. </p>
<p> The use of <code>O_ASYNC</code> is specific to BSD and Linux. The only use of <code>F_GETOWN</code> and <code>F_SETOWN</code> specified in POSIX.1 is in conjunction with the use of the <code>SIGURG</code> signal on sockets. (POSIX does not specify the <code>SIGIO</code> signal.) <code>F_GETOWN_EX</code>, <code>F_SETOWN_EX</code>, <code>F_GETSIG</code>, and <code>F_SETSIG</code> are Linux-specific. POSIX has asynchronous I/O and the <i>aio_sigevent</i> structure to achieve similar things; these are also available in Linux as part of the GNU C Library (Glibc).</p>
<h3>Leases</h3>
<p> <code>F_SETLEASE</code> and <code>F_GETLEASE</code> (Linux 2.4 onward) are used to establish a new lease, and retrieve the current lease, on the open file description referred to by the file descriptor <i>fd</i>. A file lease provides a mechanism whereby the process holding the lease (the &quot;lease holder&quot;) is notified (via delivery of a signal) when a process (the &quot;lease breaker&quot;) tries to <code><a href="/docs/linux/man/2-open/">open</a></code>(2) or <code><a href="/docs/linux/man/2-truncate/">truncate</a></code>(2) the file referred to by that file descriptor.</p>
<dl>
<dt><code>F_SETLEASE</code> (<i>int</i>)</p>
<dd> Set or remove a file lease according to which of the following values is specified in the integer <i>arg</i>:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>F_RDLCK</code></p>
<dd> Take out a read lease. This will cause the calling process to be notified when the file is opened for writing or is truncated. A read lease can be placed only on a file descriptor that is opened read-only.</p>
<dt><code>F_WRLCK</code></p>
<dd> Take out a write lease. This will cause the caller to be notified when the file is opened for reading or writing or is truncated. A write lease may be placed on a file only if there are no other open file descriptors for the file.</p>
<dt><code>F_UNLCK</code></p>
<dd> Remove our lease from the file.</dl>
</dl>
</dl>
<p> Leases are associated with an open file description (see <code><a href="/docs/linux/man/2-open/">open</a></code>(2)). This means that duplicate file descriptors (created by, for example, <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) or <code><a href="/docs/linux/man/2-dup/">dup</a></code>(2)) refer to the same lease, and this lease may be modified or released using any of these descriptors. Furthermore, the lease is released by either an explicit <code>F_UNLCK</code> operation on any of these duplicate file descriptors, or when all such file descriptors have been closed. </p>
<p> Leases may be taken out only on regular files. An unprivileged process may take out a lease only on a file whose UID (owner) matches the filesystem UID of the process. A process with the <code>CAP_LEASE</code> capability may take out leases on arbitrary files.</p>
<dl>
<dt><code>F_GETLEASE</code> (<i>void</i>)</p>
<dd> Indicates what type of lease is associated with the file descriptor <i>fd</i> by returning either <code>F_RDLCK</code>, <code>F_WRLCK</code>, or <code>F_UNLCK</code>, indicating, respectively, a read lease , a write lease, or no lease. <i>arg</i> is ignored.</dl>
<p> When a process (the &quot;lease breaker&quot;) performs an <code><a href="/docs/linux/man/2-open/">open</a></code>(2) or <code><a href="/docs/linux/man/2-truncate/">truncate</a></code>(2) that conflicts with a lease established via <code>F_SETLEASE</code>, the system call is blocked by the kernel and the kernel notifies the lease holder by sending it a signal (<code>SIGIO</code> by default). The lease holder should respond to receipt of this signal by doing whatever cleanup is required in preparation for the file to be accessed by another process (e.g., flushing cached buffers) and then either remove or downgrade its lease. A lease is removed by performing an <code>F_SETLEASE</code> command specifying <i>arg</i> as <code>F_UNLCK</code>. If the lease holder currently holds a write lease on the file, and the lease breaker is opening the file for reading, then it is sufficient for the lease holder to downgrade the lease to a read lease. This is done by performing an <code>F_SETLEASE</code> command specifying <i>arg</i> as <code>F_RDLCK</code>. </p>
<p> If the lease holder fails to downgrade or remove the lease within the number of seconds specified in <i>/proc/sys/fs/lease-break-time</i>, then the kernel forcibly removes or downgrades the lease holder&#8217;s lease. </p>
<p> Once a lease break has been initiated, <code>F_GETLEASE</code> returns the target lease type (either <code>F_RDLCK</code> or <code>F_UNLCK</code>, depending on what would be compatible with the lease breaker) until the lease holder voluntarily downgrades or removes the lease or the kernel forcibly does so after the lease break timer expires. </p>
<p> Once the lease has been voluntarily or forcibly removed or downgraded, and assuming the lease breaker has not unblocked its system call, the kernel permits the lease breaker&#8217;s system call to proceed. </p>
<p> If the lease breaker&#8217;s blocked <code><a href="/docs/linux/man/2-open/">open</a></code>(2) or <code><a href="/docs/linux/man/2-truncate/">truncate</a></code>(2) is interrupted by a signal handler, then the system call fails with the error <code>EINTR</code>, but the other steps still occur as described above. If the lease breaker is killed by a signal while blocked in <code><a href="/docs/linux/man/2-open/">open</a></code>(2) or <code><a href="/docs/linux/man/2-truncate/">truncate</a></code>(2), then the other steps still occur as described above. If the lease breaker specifies the <code>O_NONBLOCK</code> flag when calling <code><a href="/docs/linux/man/2-open/">open</a></code>(2), then the call immediately fails with the error <code>EWOULDBLOCK</code>, but the other steps still occur as described above. </p>
<p> The default signal used to notify the lease holder is <code>SIGIO</code>, but this can be changed using the <code>F_SETSIG</code> command to <code>fcntl</code>(). If a <code>F_SETSIG</code> command is performed (even one specifying <code>SIGIO</code>), and the signal handler is established using <code>SA_SIGINFO</code>, then the handler will receive a <i>siginfo_t</i> structure as its second argument, and the <i>si_fd</i> field of this argument will hold the file descriptor of the leased file that has been accessed by another process. (This is useful if the caller holds leases against multiple files.)</p>
<h3>File and directory change notification (dnotify)</h3>
<dl>
<dt><code>F_NOTIFY</code> (<i>int</i>)</p>
<dd> (Linux 2.4 onward) Provide notification when the directory referred to by <i>fd</i> or any of the files that it contains is changed. The events to be notified are specified in <i>arg</i>, which is a bit mask specified by ORing together zero or more of the following bits:</dl>
<dl>
<dt>
<dd>
<dl>
<dt><code>DN_ACCESS</code></p>
<dd> A file was accessed (<code><a href="/docs/linux/man/2-read/">read</a></code>(2), <code><a href="/docs/linux/man/2-pread/">pread</a></code>(2), <code><a href="/docs/linux/man/2-readv/">readv</a></code>(2), and similar)</p>
<dt><code>DN_MODIFY</code></p>
<dd> A file was modified (<code><a href="/docs/linux/man/2-write/">write</a></code>(2), <code><a href="/docs/linux/man/2-pwrite/">pwrite</a></code>(2), <code><a href="/docs/linux/man/2-writev/">writev</a></code>(2), <code><a href="/docs/linux/man/2-truncate/">truncate</a></code>(2), <code><a href="/docs/linux/man/2-ftruncate/">ftruncate</a></code>(2), and similar).</p>
<dt><code>DN_CREATE</code></p>
<dd> A file was created (<code><a href="/docs/linux/man/2-open/">open</a></code>(2), <code><a href="/docs/linux/man/2-creat/">creat</a></code>(2), <code><a href="/docs/linux/man/2-mknod/">mknod</a></code>(2), <code><a href="/docs/linux/man/2-mkdir/">mkdir</a></code>(2), <code><a href="/docs/linux/man/2-link/">link</a></code>(2), <code><a href="/docs/linux/man/2-symlink/">symlink</a></code>(2), <code><a href="/docs/linux/man/2-rename/">rename</a></code>(2) into this directory).</p>
<dt><code>DN_DELETE</code></p>
<dd> A file was unlinked (<code><a href="/docs/linux/man/2-unlink/">unlink</a></code>(2), <code><a href="/docs/linux/man/2-rename/">rename</a></code>(2) to another directory, <code><a href="/docs/linux/man/2-rmdir/">rmdir</a></code>(2)).</p>
<dt><code>DN_RENAME</code></p>
<dd> A file was renamed within this directory (<code><a href="/docs/linux/man/2-rename/">rename</a></code>(2)).</p>
<dt><code>DN_ATTRIB</code></p>
<dd> The attributes of a file were changed (<code><a href="/docs/linux/man/2-chown/">chown</a></code>(2), <code><a href="/docs/linux/man/2-chmod/">chmod</a></code>(2), <code><a href="/docs/linux/man/2-utime/">utime</a></code>(2), <code><a href="/docs/linux/man/2-utimensat/">utimensat</a></code>(2), and similar).</dl>
</dl>
<dl>
<dt>
<dd> (In order to obtain these definitions, the <code>_GNU_SOURCE</code> feature test macro must be defined before including <i>any</i> header files.)</p>
<dt>
<dd> Directory notifications are normally &quot;one-shot&quot;, and the application must reregister to receive further notifications. Alternatively, if <code>DN_MULTISHOT</code> is included in <i>arg</i>, then notification will remain in effect until explicitly removed.</p>
<dt>
<dd> A series of <code>F_NOTIFY</code> requests is cumulative, with the events in <i>arg</i> being added to the set already monitored. To disable notification of all events, make an <code>F_NOTIFY</code> call specifying <i>arg</i> as 0.</p>
<dt>
<dd> Notification occurs via delivery of a signal. The default signal is <code>SIGIO</code>, but this can be changed using the <code>F_SETSIG</code> command to <code>fcntl</code>(). (Note that <code>SIGIO</code> is one of the nonqueuing standard signals; switching to the use of a real-time signal means that multiple notifications can be queued to the process.) In the latter case, the signal handler receives a <i>siginfo_t</i> structure as its second argument (if the handler was established using <code>SA_SIGINFO</code>) and the <i>si_fd</i> field of this structure contains the file descriptor which generated the notification (useful when establishing notification on multiple directories).</p>
<dt>
<dd> Especially when using <code>DN_MULTISHOT</code>, a real time signal should be used for notification, so that multiple notifications can be queued.</p>
<dt>
<dd> <code>NOTE:</code> New applications should use the <i>inotify</i> interface (available since kernel 2.6.13), which provides a much superior interface for obtaining notifications of filesystem events. See <code><a href="/docs/linux/man/7-inotify/">inotify</a></code>(7).</dl>
<h3>Changing the capacity of a pipe</h3>
<dl>
<dt><code>F_SETPIPE_SZ</code> (<i>int</i>; since Linux 2.6.35)</p>
<dd> Change the capacity of the pipe referred to by <i>fd</i> to be at least <i>arg</i> bytes. An unprivileged process can adjust the pipe capacity to any value between the system page size and the limit defined in <i>/proc/sys/fs/pipe-max-size</i> (see <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5)). Attempts to set the pipe capacity below the page size are silently rounded up to the page size. Attempts by an unprivileged process to set the pipe capacity above the limit in <i>/proc/sys/fs/pipe-max-size</i> yield the error <code>EPERM</code>; a privileged process (<code>CAP_SYS_RESOURCE</code>) can override the limit.</p>
<dt>
<dd> When allocating the buffer for the pipe, the kernel may use a capacity larger than <i>arg</i>, if that is convenient for the implementation. (In the current implementation, the allocation is the next higher power-of-two page-size multiple of the requested size.) The actual capacity (in bytes) that is set is returned as the function result.</p>
<dt>
<dd> Attempting to set the pipe capacity smaller than the amount of buffer space currently used to store data produces the error <code>EBUSY</code>.</p>
<dt>
<dd> Note that because of the way the pages of the pipe buffer are employed when data is written to the pipe, the number of bytes that can be written may be less than the nominal size, depending on the size of the writes.</p>
<dt><code>F_GETPIPE_SZ</code> (<i>void</i>; since Linux 2.6.35)</p>
<dd> Return (as the function result) the capacity of the pipe referred to by <i>fd</i>.</dl>
<h3>File Sealing</h3>
<p> File seals limit the set of allowed operations on a given file. For each seal that is set on a file, a specific set of operations will fail with <code>EPERM</code> on this file from now on. The file is said to be sealed. The default set of seals depends on the type of the underlying file and filesystem. For an overview of file sealing, a discussion of its purpose, and some code examples, see <code><a href="/docs/linux/man/2-memfd_create/">memfd_create</a></code>(2). </p>
<p> Currently, file seals can be applied only to a file descriptor returned by <code><a href="/docs/linux/man/2-memfd_create/">memfd_create</a></code>(2) (if the <code>MFD_ALLOW_SEALING</code> was employed). On other filesystems, all <code>fcntl</code>() operations that operate on seals will return <code>EINVAL</code>. </p>
<p> Seals are a property of an inode. Thus, all open file descriptors referring to the same inode share the same set of seals. Furthermore, seals can never be removed, only added.</p>
<dl>
<dt><code>F_ADD_SEALS</code> (<i>int</i>; since Linux 3.17)</p>
<dd> Add the seals given in the bit-mask argument <i>arg</i> to the set of seals of the inode referred to by the file descriptor <i>fd</i>. Seals cannot be removed again. Once this call succeeds, the seals are enforced by the kernel immediately. If the current set of seals includes <code>F_SEAL_SEAL</code> (see below), then this call will be rejected with <code>EPERM</code>. Adding a seal that is already set is a no-op, in case <code>F_SEAL_SEAL</code> is not set already. In order to place a seal, the file descriptor <i>fd</i> must be writable.</p>
<dt><code>F_GET_SEALS</code> (<i>void</i>; since Linux 3.17)</p>
<dd> Return (as the function result) the current set of seals of the inode referred to by <i>fd</i>. If no seals are set, 0 is returned. If the file does not support sealing, -1 is returned and <i>errno</i> is set to <code>EINVAL</code>.</dl>
<p> The following seals are available:</p>
<dl>
<dt><code>F_SEAL_SEAL</code></p>
<dd> If this seal is set, any further call to <code>fcntl</code>() with <code>F_ADD_SEALS</code> fails with the error <code>EPERM</code>. Therefore, this seal prevents any modifications to the set of seals itself. If the initial set of seals of a file includes <code>F_SEAL_SEAL</code>, then this effectively causes the set of seals to be constant and locked.</p>
<dt><code>F_SEAL_SHRINK</code></p>
<dd> If this seal is set, the file in question cannot be reduced in size. This affects <code><a href="/docs/linux/man/2-open/">open</a></code>(2) with the <code>O_TRUNC</code> flag as well as <code><a href="/docs/linux/man/2-truncate/">truncate</a></code>(2) and <code><a href="/docs/linux/man/2-ftruncate/">ftruncate</a></code>(2). Those calls fail with <code>EPERM</code> if you try to shrink the file in question. Increasing the file size is still possible.</p>
<dt><code>F_SEAL_GROW</code></p>
<dd> If this seal is set, the size of the file in question cannot be increased. This affects <code><a href="/docs/linux/man/2-write/">write</a></code>(2) beyond the end of the file, <code><a href="/docs/linux/man/2-truncate/">truncate</a></code>(2), <code><a href="/docs/linux/man/2-ftruncate/">ftruncate</a></code>(2), and <code><a href="/docs/linux/man/2-fallocate/">fallocate</a></code>(2). These calls fail with <code>EPERM</code> if you use them to increase the file size. If you keep the size or shrink it, those calls still work as expected.</p>
<dt><code>F_SEAL_WRITE</code></p>
<dd> If this seal is set, you cannot modify the contents of the file. Note that shrinking or growing the size of the file is still possible and allowed. Thus, this seal is normally used in combination with one of the other seals. This seal affects <code><a href="/docs/linux/man/2-write/">write</a></code>(2) and <code><a href="/docs/linux/man/2-fallocate/">fallocate</a></code>(2) (only in combination with the <code>FALLOC_FL_PUNCH_HOLE</code> flag). Those calls fail with <code>EPERM</code> if this seal is set. Furthermore, trying to create new shared, writable memory-mappings via <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) will also fail with <code>EPERM</code>.</p>
<dt>
<dd> Using the <code>F_ADD_SEALS</code> operation to set the <code>F_SEAL_WRITE</code> seal fails with <code>EBUSY</code> if any writable, shared mapping exists. Such mappings must be unmapped before you can add this seal. Furthermore, if there are any asynchronous I/O operations (<code><a href="/docs/linux/man/2-io_submit/">io_submit</a></code>(2)) pending on the file, all outstanding writes will be discarded.</p>
<dt><code>F_SEAL_FUTURE_WRITE</code> (since Linux 5.1)</p>
<dd> The effect of this seal is similar to <code>F_SEAL_WRITE</code>, but the contents of the file can still be modified via shared writable mappings that were created prior to the seal being set. Any attempt to create a new writable mapping on the file via <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) will fail with <code>EPERM</code>. Likewise, an attempt to write to the file via <code><a href="/docs/linux/man/2-write/">write</a></code>(2) will fail with <code>EPERM</code>.</p>
<dt>
<dd> Using this seal, one process can create a memory buffer that it can continue to modify while sharing that buffer on a &quot;read-only&quot; basis with other processes.</dl>
<h3>File read/write hints</h3>
<p> Write lifetime hints can be used to inform the kernel about the relative expected lifetime of writes on a given inode or via a particular open file description. (See <code><a href="/docs/linux/man/2-open/">open</a></code>(2) for an explanation of open file descriptions.) In this context, the term &quot;write lifetime&quot; means the expected time the data will live on media, before being overwritten or erased. </p>
<p> An application may use the different hint values specified below to separate writes into different write classes, so that multiple users or applications running on a single storage back-end can aggregate their I/O patterns in a consistent manner. However, there are no functional semantics implied by these flags, and different I/O classes can use the write lifetime hints in arbitrary ways, so long as the hints are used consistently. </p>
<p> The following operations can be applied to the file descriptor, <i>fd</i>:</p>
<dl>
<dt><code>F_GET_RW_HINT</code> (<i>uint64_t *</i>; since Linux 4.13)</p>
<dd> Returns the value of the read/write hint associated with the underlying inode referred to by <i>fd</i>.</p>
<dt><code>F_SET_RW_HINT</code> (<i>uint64_t *</i>; since Linux 4.13)</p>
<dd> Sets the read/write hint value associated with the underlying inode referred to by <i>fd</i>. This hint persists until either it is explicitly modified or the underlying filesystem is unmounted.</p>
<dt><code>F_GET_FILE_RW_HINT</code> (<i>uint64_t *</i>; since Linux 4.13)</p>
<dd> Returns the value of the read/write hint associated with the open file description referred to by <i>fd</i>.</p>
<dt><code>F_SET_FILE_RW_HINT</code> (<i>uint64_t *</i>; since Linux 4.13)</p>
<dd> Sets the read/write hint value associated with the open file description referred to by <i>fd</i>.</dl>
<p> If an open file description has not been assigned a read/write hint, then it shall use the value assigned to the inode, if any. </p>
<p> The following read/write hints are valid since Linux 4.13:</p>
<dl>
<dt><code>RWH_WRITE_LIFE_NOT_SET</code></p>
<dd> No specific hint has been set. This is the default value.</p>
<dt><code>RWH_WRITE_LIFE_NONE</code></p>
<dd> No specific write lifetime is associated with this file or inode.</p>
<dt><code>RWH_WRITE_LIFE_SHORT</code></p>
<dd> Data written to this inode or via this open file description is expected to have a short lifetime.</p>
<dt><code>RWH_WRITE_LIFE_MEDIUM</code></p>
<dd> Data written to this inode or via this open file description is expected to have a lifetime longer than data written with <code>RWH_WRITE_LIFE_SHORT</code>.</p>
<dt><code>RWH_WRITE_LIFE_LONG</code></p>
<dd> Data written to this inode or via this open file description is expected to have a lifetime longer than data written with <code>RWH_WRITE_LIFE_MEDIUM</code>.</p>
<dt><code>RWH_WRITE_LIFE_EXTREME</code></p>
<dd> Data written to this inode or via this open file description is expected to have a lifetime longer than data written with <code>RWH_WRITE_LIFE_LONG</code>.</dl>
<p> All the write-specific hints are relative to each other, and no individual absolute meaning should be attributed to them.</p>
<h2>RETURN VALUE</h2>
<p> For a successful call, the return value depends on the operation:</p>
<dl>
<dt><code>F_DUPFD</code></p>
<dd> The new file descriptor.</p>
<dt><code>F_GETFD</code></p>
<dd> Value of file descriptor flags.</p>
<dt><code>F_GETFL</code></p>
<dd> Value of file status flags.</p>
<dt><code>F_GETLEASE</code></p>
<dd> Type of lease held on file descriptor.</p>
<dt><code>F_GETOWN</code></p>
<dd> Value of file descriptor owner.</p>
<dt><code>F_GETSIG</code></p>
<dd> Value of signal sent when read or write becomes possible, or zero for traditional <code>SIGIO</code> behavior.</p>
<dt><code>F_GETPIPE_SZ</code>, <code>F_SETPIPE_SZ</code></p>
<dd> The pipe capacity.</p>
<dt><code>F_GET_SEALS</code></p>
<dd> A bit mask identifying the seals that have been set for the inode referred to by <i>fd</i>.</p>
<dt>All other commands</p>
<dd> Zero.</dl>
<p> On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EACCES</code> or <code>EAGAIN</code></p>
<dd> Operation is prohibited by locks held by other processes.</p>
<dt><code>EAGAIN</code></p>
<dd> The operation is prohibited because the file has been memory-mapped by another process.</p>
<dt><code>EBADF</code></p>
<dd> <i>fd</i> is not an open file descriptor</p>
<dt><code>EBADF</code></p>
<dd> <i>cmd</i> is <code>F_SETLK</code> or <code>F_SETLKW</code> and the file descriptor open mode doesn&#8217;t match with the type of lock requested.</p>
<dt><code>EBUSY</code></p>
<dd> <i>cmd</i> is <code>F_SETPIPE_SZ</code> and the new pipe capacity specified in <i>arg</i> is smaller than the amount of buffer space currently used to store data in the pipe.</p>
<dt><code>EBUSY</code></p>
<dd> <i>cmd</i> is <code>F_ADD_SEALS</code>, <i>arg</i> includes <code>F_SEAL_WRITE</code>, and there exists a writable, shared mapping on the file referred to by <i>fd</i>.</p>
<dt><code>EDEADLK</code></p>
<dd> It was detected that the specified <code>F_SETLKW</code> command would cause a deadlock.</p>
<dt><code>EFAULT</code></p>
<dd> <i>lock</i> is outside your accessible address space.</p>
<dt><code>EINTR</code></p>
<dd> <i>cmd</i> is <code>F_SETLKW</code> or <code>F_OFD_SETLKW</code> and the operation was interrupted by a signal; see <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7).</p>
<dt><code>EINTR</code></p>
<dd> <i>cmd</i> is <code>F_GETLK</code>, <code>F_SETLK</code>, <code>F_OFD_GETLK</code>, or <code>F_OFD_SETLK</code>, and the operation was interrupted by a signal before the lock was checked or acquired. Most likely when locking a remote file (e.g., locking over NFS), but can sometimes happen locally.</p>
<dt><code>EINVAL</code></p>
<dd> The value specified in <i>cmd</i> is not recognized by this kernel.</p>
<dt><code>EINVAL</code></p>
<dd> <i>cmd</i> is <code>F_ADD_SEALS</code> and <i>arg</i> includes an unrecognized sealing bit.</p>
<dt><code>EINVAL</code></p>
<dd> <i>cmd</i> is <code>F_ADD_SEALS</code> or <code>F_GET_SEALS</code> and the filesystem containing the inode referred to by <i>fd</i> does not support sealing.</p>
<dt><code>EINVAL</code></p>
<dd> <i>cmd</i> is <code>F_DUPFD</code> and <i>arg</i> is negative or is greater than the maximum allowable value (see the discussion of <code>RLIMIT_NOFILE</code> in <code><a href="/docs/linux/man/2-getrlimit/">getrlimit</a></code>(2)).</p>
<dt><code>EINVAL</code></p>
<dd> <i>cmd</i> is <code>F_SETSIG</code> and <i>arg</i> is not an allowable signal number.</p>
<dt><code>EINVAL</code></p>
<dd> <i>cmd</i> is <code>F_OFD_SETLK</code>, <code>F_OFD_SETLKW</code>, or <code>F_OFD_GETLK</code>, and <i>l_pid</i> was not specified as zero.</p>
<dt><code>EMFILE</code></p>
<dd> <i>cmd</i> is <code>F_DUPFD</code> and the per-process limit on the number of open file descriptors has been reached.</p>
<dt><code>ENOLCK</code></p>
<dd> Too many segment locks open, lock table is full, or a remote locking protocol failed (e.g., locking over NFS).</p>
<dt><code>ENOTDIR</code></p>
<dd> <code>F_NOTIFY</code> was specified in <i>cmd</i>, but <i>fd</i> does not refer to a directory.</p>
<dt><code>EPERM</code></p>
<dd> <i>cmd</i> is <code>F_SETPIPE_SZ</code> and the soft or hard user pipe limit has been reached; see <code><a href="/docs/linux/man/7-pipe/">pipe</a></code>(7).</p>
<dt><code>EPERM</code></p>
<dd> Attempted to clear the <code>O_APPEND</code> flag on a file that has the append-only attribute set.</p>
<dt><code>EPERM</code></p>
<dd> <i>cmd</i> was <code>F_ADD_SEALS</code>, but <i>fd</i> was not open for writing or the current set of seals on the file already includes <code>F_SEAL_SEAL</code>.</dl>
<h2>CONFORMING TO</h2>
<p> SVr4, 4.3BSD, POSIX.1-2001. Only the operations <code>F_DUPFD</code>, <code>F_GETFD</code>, <code>F_SETFD</code>, <code>F_GETFL</code>, <code>F_SETFL</code>, <code>F_GETLK</code>, <code>F_SETLK</code>, and <code>F_SETLKW</code> are specified in POSIX.1-2001. </p>
<p> <code>F_GETOWN</code> and <code>F_SETOWN</code> are specified in POSIX.1-2001. (To get their definitions, define either <code>_XOPEN_SOURCE</code> with the value 500 or greater, or <code>_POSIX_C_SOURCE</code> with the value 200809L or greater.) </p>
<p> <code>F_DUPFD_CLOEXEC</code> is specified in POSIX.1-2008. (To get this definition, define <code>_POSIX_C_SOURCE</code> with the value 200809L or greater, or <code>_XOPEN_SOURCE</code> with the value 700 or greater.) </p>
<p> <code>F_GETOWN_EX</code>, <code>F_SETOWN_EX</code>, <code>F_SETPIPE_SZ</code>, <code>F_GETPIPE_SZ</code>, <code>F_GETSIG</code>, <code>F_SETSIG</code>, <code>F_NOTIFY</code>, <code>F_GETLEASE</code>, and <code>F_SETLEASE</code> are Linux-specific. (Define the <code>_GNU_SOURCE</code> macro to obtain these definitions.) </p>
<p> <code>F_OFD_SETLK</code>, <code>F_OFD_SETLKW</code>, and <code>F_OFD_GETLK</code> are Linux-specific (and one must define <code>_GNU_SOURCE</code> to obtain their definitions), but work is being done to have them included in the next version of POSIX.1. </p>
<p> <code>F_ADD_SEALS</code> and <code>F_GET_SEALS</code> are Linux-specific.</p>
<h2>NOTES</h2>
<p> The errors returned by <code><a href="/docs/linux/man/2-dup2/">dup2</a></code>(2) are different from those returned by <code>F_DUPFD</code>.</p>
<h3>File locking</h3>
<p> The original Linux <code>fcntl</code>() system call was not designed to handle large file offsets (in the <i>flock</i> structure). Consequently, an <code>fcntl64</code>() system call was added in Linux 2.4. The newer system call employs a different structure for file locking, <i>flock64</i>, and corresponding commands, <code>F_GETLK64</code>, <code>F_SETLK64</code>, and <code>F_SETLKW64</code>. However, these details can be ignored by applications using glibc, whose <code>fcntl</code>() wrapper function transparently employs the more recent system call where it is available.</p>
<h3>Record locks</h3>
<p> Since kernel 2.0, there is no interaction between the types of lock placed by <code><a href="/docs/linux/man/2-flock/">flock</a></code>(2) and <code>fcntl</code>(). </p>
<p> Several systems have more fields in <i>struct flock</i> such as, for example, <i>l_sysid</i> (to identify the machine where the lock is held). Clearly, <i>l_pid</i> alone is not going to be very useful if the process holding the lock may live on a different machine; on Linux, while present on some architectures (such as MIPS32), this field is not used. </p>
<p> The original Linux <code>fcntl</code>() system call was not designed to handle large file offsets (in the <i>flock</i> structure). Consequently, an <code>fcntl64</code>() system call was added in Linux 2.4. The newer system call employs a different structure for file locking, <i>flock64</i>, and corresponding commands, <code>F_GETLK64</code>, <code>F_SETLK64</code>, and <code>F_SETLKW64</code>. However, these details can be ignored by applications using glibc, whose <code>fcntl</code>() wrapper function transparently employs the more recent system call where it is available.</p>
<h3>Record locking and NFS</h3>
<p> Before Linux 3.12, if an NFSv4 client loses contact with the server for a period of time (defined as more than 90 seconds with no communication), it might lose and regain a lock without ever being aware of the fact. (The period of time after which contact is assumed lost is known as the NFSv4 leasetime. On a Linux NFS server, this can be determined by looking at <i>/proc/fs/nfsd/nfsv4leasetime</i>, which expresses the period in seconds. The default value for this file is 90.) This scenario potentially risks data corruption, since another process might acquire a lock in the intervening period and perform file I/O. </p>
<p> Since Linux 3.12, if an NFSv4 client loses contact with the server, any I/O to the file by a process which &quot;thinks&quot; it holds a lock will fail until that process closes and reopens the file. A kernel parameter, <i>nfs.recover_lost_locks</i>, can be set to 1 to obtain the pre-3.12 behavior, whereby the client will attempt to recover lost locks when contact is reestablished with the server. Because of the attendant risk of data corruption, this parameter defaults to 0 (disabled).</p>
<h2>BUGS</h2>
<h3>F_SETFL</h3>
<p> It is not possible to use <code>F_SETFL</code> to change the state of the <code>O_DSYNC</code> and <code>O_SYNC</code> flags. Attempts to change the state of these flags are silently ignored.</p>
<h3>F_GETOWN</h3>
<p> A limitation of the Linux system call conventions on some architectures (notably i386) means that if a (negative) process group ID to be returned by <code>F_GETOWN</code> falls in the range -1 to -4095, then the return value is wrongly interpreted by glibc as an error in the system call; that is, the return value of <code>fcntl</code>() will be -1, and <i>errno</i> will contain the (positive) process group ID. The Linux-specific <code>F_GETOWN_EX</code> operation avoids this problem. Since glibc version 2.11, glibc makes the kernel <code>F_GETOWN</code> problem invisible by implementing <code>F_GETOWN</code> using <code>F_GETOWN_EX</code>.</p>
<h3>F_SETOWN</h3>
<p> In Linux 2.4 and earlier, there is bug that can occur when an unprivileged process uses <code>F_SETOWN</code> to specify the owner of a socket file descriptor as a process (group) other than the caller. In this case, <code>fcntl</code>() can return -1 with <i>errno</i> set to <code>EPERM</code>, even when the owner process (group) is one that the caller has permission to send signals to. Despite this error return, the file descriptor owner is set, and signals will be sent to the owner.</p>
<h3>Deadlock detection</h3>
<p> The deadlock-detection algorithm employed by the kernel when dealing with <code>F_SETLKW</code> requests can yield both false negatives (failures to detect deadlocks, leaving a set of deadlocked processes blocked indefinitely) and false positives (<code>EDEADLK</code> errors when there is no deadlock). For example, the kernel limits the lock depth of its dependency search to 10 steps, meaning that circular deadlock chains that exceed that size will not be detected. In addition, the kernel may falsely indicate a deadlock when two or more processes created using the <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) <code>CLONE_FILES</code> flag place locks that appear (to the kernel) to conflict.</p>
<h3>Mandatory locking</h3>
<p> The Linux implementation of mandatory locking is subject to race conditions which render it unreliable: a <code><a href="/docs/linux/man/2-write/">write</a></code>(2) call that overlaps with a lock may modify data after the mandatory lock is acquired; a <code><a href="/docs/linux/man/2-read/">read</a></code>(2) call that overlaps with a lock may detect changes to data that were made only after a write lock was acquired. Similar races exist between mandatory locks and <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2). It is therefore inadvisable to rely on mandatory locking.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-dup2/">dup2</a></code>(2), <code><a href="/docs/linux/man/2-flock/">flock</a></code>(2), <code><a href="/docs/linux/man/2-open/">open</a></code>(2), <code><a href="/docs/linux/man/2-socket/">socket</a></code>(2), <code><a href="/docs/linux/man/3-lockf/">lockf</a></code>(3), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7), <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7), <code><a href="/docs/linux/man/8-lslocks/">lslocks</a></code>(8) </p>
<p> <i>locks.txt</i>, <i>mandatory-locking.txt</i>, and <i>dnotify.txt</i> in the Linux kernel source directory <i>Documentation/filesystems/</i> (on older kernels, these files are directly under the <i>Documentation/</i> directory, and <i>mandatory-locking.txt</i> is called <i>mandatory.txt</i>)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
