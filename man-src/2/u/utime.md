---
title: "utime(2)"
name: "utime"
section: "2"
letter: "u"
url: "/docs/linux/man/2-utime/"
description: "utime, utimes – change file last access and modification times"
---

<h2 class="name">NAME</h2>
<p> utime, utimes &#8211; change file last access and modification times </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;sys/types.h&gt;
#include &lt;utime.h&gt;
int utime(const char *filename, const struct utimbuf *times);
#include &lt;sys/time.h&gt;
int utimes(const char *filename, const struct timeval times[2]);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>Note:</code> modern applications may prefer to use the interfaces described in <code><a href="/docs/linux/man/2-utimensat/">utimensat</a></code>(2). </p>
<p> The <code>utime</code>() system call changes the access and modification times of the inode specified by <i>filename</i> to the <i>actime</i> and <i>modtime</i> fields of <i>times</i> respectively. </p>
<p> If <i>times</i> is NULL, then the access and modification times of the file are set to the current time. </p>
<p> Changing timestamps is permitted when: either the process has appropriate privileges, or the effective user ID equals the user ID of the file, or <i>times</i> is NULL and the process has write permission for the file. </p>
<p> The <i>utimbuf</i> structure is: </p>
<p> struct utimbuf {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;time_t actime;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;access time&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;time_t modtime;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;modification time&nbsp;*/ }; </p>
<p> The <code>utime</code>() system call allows specification of timestamps with a resolution of 1 second. </p>
<p> The <code>utimes</code>() system call is similar, but the <i>times</i> argument refers to an array rather than a structure. The elements of this array are <i>timeval</i> structures, which allow a precision of 1 microsecond for specifying timestamps. The <i>timeval</i> structure is: </p>
<p> struct timeval {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long tv_sec;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;seconds&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long tv_usec;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;microseconds&nbsp;*/ }; </p>
<p> <i>times[0]</i> specifies the new access time, and <i>times[1]</i> specifies the new modification time. If <i>times</i> is NULL, then analogously to <code>utime</code>(), the access and modification times of the file are set to the current time.</p>
<h2>RETURN VALUE</h2>
<p> On success, zero is returned. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EACCES</code></p>
<dd> Search permission is denied for one of the directories in the path prefix of <i>path</i> (see also <code><a href="/docs/linux/man/7-path_resolution/">path_resolution</a></code>(7)).</p>
<dt><code>EACCES</code></p>
<dd> <i>times</i> is NULL, the caller&#8217;s effective user ID does not match the owner of the file, the caller does not have write access to the file, and the caller is not privileged (Linux: does not have either the <code>CAP_DAC_OVERRIDE</code> or the <code>CAP_FOWNER</code> capability).</p>
<dt><code>ENOENT</code></p>
<dd> <i>filename</i> does not exist.</p>
<dt><code>EPERM</code></p>
<dd> <i>times</i> is not NULL, the caller&#8217;s effective UID does not match the owner of the file, and the caller is not privileged (Linux: does not have the <code>CAP_FOWNER</code> capability).</p>
<dt><code>EROFS</code></p>
<dd> <i>path</i> resides on a read-only filesystem.</dl>
<h2>CONFORMING TO</h2>
<p> <code>utime</code>(): SVr4, POSIX.1-2001. POSIX.1-2008 marks <code>utime</code>() as obsolete. </p>
<p> <code>utimes</code>(): 4.3BSD, POSIX.1-2001.</p>
<h2>NOTES</h2>
<p> Linux does not allow changing the timestamps on an immutable file, or setting the timestamps to something other than the current time on an append-only file.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-chattr/">chattr</a></code>(1), <code><a href="/docs/linux/man/1-touch/">touch</a></code>(1), <code><a href="/docs/linux/man/2-futimesat/">futimesat</a></code>(2), <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2), <code><a href="/docs/linux/man/2-utimensat/">utimensat</a></code>(2), <code><a href="/docs/linux/man/3-futimens/">futimens</a></code>(3), <code><a href="/docs/linux/man/3-futimes/">futimes</a></code>(3), <code><a href="/docs/linux/man/7-inode/">inode</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
