---
title: "utimensat(2)"
name: "utimensat"
section: "2"
letter: "u"
url: "/docs/linux/man/2-utimensat/"
description: "utimensat, futimens – change file timestamps with nanosecond precision"
---

<h2 class="name">NAME</h2>
<p> utimensat, futimens &#8211; change file timestamps with nanosecond precision </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;fcntl.h&gt; /* Definition of AT_* constants */
#include &lt;sys/stat.h&gt;
int utimensat(int dirfd, const char *pathname,
              const struct timespec times[2], int flags);
int futimens(int fd, const struct timespec times[2]);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>utimensat</code>():</p>
<dl>
<dt>
<dd>
<dl>
<dt>Since glibc 2.10:</p>
<dd> _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200809L</p>
<dt>Before glibc 2.10:</p>
<dd> _ATFILE_SOURCE</dl>
</dl>
<p> <code>futimens</code>():</p>
<dl>
<dt>
<dd>
<dl>
<dt>Since glibc 2.10:</p>
<dd> _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200809L</p>
<dt>Before glibc 2.10:</p>
<dd> _GNU_SOURCE</dl>
</dl>
<h2>DESCRIPTION</h2>
<p> <code>utimensat</code>() and <code>futimens</code>() update the timestamps of a file with nanosecond precision. This contrasts with the historical <code><a href="/docs/linux/man/2-utime/">utime</a></code>(2) and <code><a href="/docs/linux/man/2-utimes/">utimes</a></code>(2), which permit only second and microsecond precision, respectively, when setting file timestamps. </p>
<p> With <code>utimensat</code>() the file is specified via the pathname given in <i>pathname</i>. With <code>futimens</code>() the file whose timestamps are to be updated is specified via an open file descriptor, <i>fd</i>. </p>
<p> For both calls, the new file timestamps are specified in the array <i>times</i>: <i>times[0]</i> specifies the new &quot;last access time&quot; (<i>atime</i>); <i>times[1]</i> specifies the new &quot;last modification time&quot; (<i>mtime</i>). Each of the elements of <i>times</i> specifies a time as the number of seconds and nanoseconds since the Epoch, 1970-01-01 00:00:00 +0000 (UTC). This information is conveyed in a structure of the following form: </p>
<p> struct timespec {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;time_t tv_sec;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;seconds&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long&nbsp;<wbr>&nbsp;<wbr>&nbsp;tv_nsec;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;nanoseconds&nbsp;*/ }; </p>
<p> Updated file timestamps are set to the greatest value supported by the filesystem that is not greater than the specified time. </p>
<p> If the <i>tv_nsec</i> field of one of the <i>timespec</i> structures has the special value <code>UTIME_NOW</code>, then the corresponding file timestamp is set to the current time. If the <i>tv_nsec</i> field of one of the <i>timespec</i> structures has the special value <code>UTIME_OMIT</code>, then the corresponding file timestamp is left unchanged. In both of these cases, the value of the corresponding <i>tv_sec</i> field is ignored. </p>
<p> If <i>times</i> is NULL, then both timestamps are set to the current time.</p>
<h3>Permissions requirements</h3>
<p> To set both file timestamps to the current time (i.e., <i>times</i> is NULL, or both <i>tv_nsec</i> fields specify <code>UTIME_NOW</code>), either:</p>
<dl>
<dt>1.</p>
<dd> the caller must have write access to the file;</p>
<dt>2.</p>
<dd> the caller&#8217;s effective user ID must match the owner of the file; or</p>
<dt>3.</p>
<dd> the caller must have appropriate privileges.</dl>
<p> To make any change other than setting both timestamps to the current time (i.e., <i>times</i> is not NULL, and neither <i>tv_nsec</i> field is <code>UTIME_NOW</code> and neither <i>tv_nsec</i> field is <code>UTIME_OMIT</code>), either condition 2 or 3 above must apply. </p>
<p> If both <i>tv_nsec</i> fields are specified as <code>UTIME_OMIT</code>, then no file ownership or permission checks are performed, and the file timestamps are not modified, but other error conditions may still be detected.</p>
<h3>utimensat() specifics</h3>
<p> If <i>pathname</i> is relative, then by default it is interpreted relative to the directory referred to by the open file descriptor, <i>dirfd</i> (rather than relative to the current working directory of the calling process, as is done by <code><a href="/docs/linux/man/2-utimes/">utimes</a></code>(2) for a relative pathname). See <code><a href="/docs/linux/man/2-openat/">openat</a></code>(2) for an explanation of why this can be useful. </p>
<p> If <i>pathname</i> is relative and <i>dirfd</i> is the special value <code>AT_FDCWD</code>, then <i>pathname</i> is interpreted relative to the current working directory of the calling process (like <code><a href="/docs/linux/man/2-utimes/">utimes</a></code>(2)). </p>
<p> If <i>pathname</i> is absolute, then <i>dirfd</i> is ignored. </p>
<p> The <i>flags</i> field is a bit mask that may be 0, or include the following constant, defined in <i>&lt;fcntl.h&gt;</i>:</p>
<dl>
<dt><code>AT_SYMLINK_NOFOLLOW</code></p>
<dd> If <i>pathname</i> specifies a symbolic link, then update the timestamps of the link, rather than the file to which it refers.</dl>
<h2>RETURN VALUE</h2>
<p> On success, <code>utimensat</code>() and <code>futimens</code>() return 0. On error, -1 is returned and <i>errno</i> is set to indicate the error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EACCES</code></p>
<dd> <i>times</i> is NULL, or both <i>tv_nsec</i> values are <code>UTIME_NOW</code>, and the effective user ID of the caller does not match the owner of the file, the caller does not have write access to the file, and the caller is not privileged (Linux: does not have either the <code>CAP_FOWNER</code> or the <code>CAP_DAC_OVERRIDE</code> capability).</p>
<dt><code>EBADF</code></p>
<dd> (<code>futimens</code>()) <i>fd</i> is not a valid file descriptor.</p>
<dt><code>EBADF</code></p>
<dd> (<code>utimensat</code>()) <i>pathname</i> is a relative pathname, but <i>dirfd</i> is neither <code>AT_FDCWD</code> nor a valid file descriptor.</p>
<dt><code>EFAULT</code></p>
<dd> <i>times</i> pointed to an invalid address; or, <i>dirfd</i> was <code>AT_FDCWD</code>, and <i>pathname</i> is NULL or an invalid address.</p>
<dt><code>EINVAL</code></p>
<dd> Invalid value in <i>flags</i>.</p>
<dt><code>EINVAL</code></p>
<dd> Invalid value in one of the <i>tv_nsec</i> fields (value outside range 0 to 999,999,999, and not <code>UTIME_NOW</code> or <code>UTIME_OMIT</code>); or an invalid value in one of the <i>tv_sec</i> fields.</p>
<dt><code>EINVAL</code></p>
<dd> <i>pathname</i> is NULL, <i>dirfd</i> is not <code>AT_FDCWD</code>, and <i>flags</i> contains <code>AT_SYMLINK_NOFOLLOW</code>.</p>
<dt><code>ELOOP</code></p>
<dd> (<code>utimensat</code>()) Too many symbolic links were encountered in resolving <i>pathname</i>.</p>
<dt><code>ENAMETOOLONG</code></p>
<dd> (<code>utimensat</code>()) <i>pathname</i> is too long.</p>
<dt><code>ENOENT</code></p>
<dd> (<code>utimensat</code>()) A component of <i>pathname</i> does not refer to an existing directory or file, or <i>pathname</i> is an empty string.</p>
<dt><code>ENOTDIR</code></p>
<dd> (<code>utimensat</code>()) <i>pathname</i> is a relative pathname, but <i>dirfd</i> is neither <code>AT_FDCWD</code> nor a file descriptor referring to a directory; or, one of the prefix components of <i>pathname</i> is not a directory.</p>
<dt><code>EPERM</code></p>
<dd> The caller attempted to change one or both timestamps to a value other than the current time, or to change one of the timestamps to the current time while leaving the other timestamp unchanged, (i.e., <i>times</i> is not NULL, neither <i>tv_nsec</i> field is <code>UTIME_NOW</code>, and neither <i>tv_nsec</i> field is <code>UTIME_OMIT</code>) and either:</p>
<dl>
<dt>
<dd>
<dl>
<dt>*</p>
<dd> the caller&#8217;s effective user ID does not match the owner of file, and the caller is not privileged (Linux: does not have the <code>CAP_FOWNER</code> capability); or,</p>
<dt>*</p>
<dd> the file is marked append-only or immutable (see <code><a href="/docs/linux/man/1-chattr/">chattr</a></code>(1)).</dl>
</dl>
<dt><code>EROFS</code></p>
<dd> The file is on a read-only filesystem.</p>
<dt><code>ESRCH</code></p>
<dd> (<code>utimensat</code>()) Search permission is denied for one of the prefix components of <i>pathname</i>.</dl>
<h2>VERSIONS</h2>
<p> <code>utimensat</code>() was added to Linux in kernel 2.6.22; glibc support was added with version 2.6. </p>
<p> Support for <code>futimens</code>() first appeared in glibc 2.6.</p>
<h2>ATTRIBUTES</h2>
<p> For an explanation of the terms used in this section, see <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7). </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Attribute</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>utimensat</code>(), <code>futimens</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> <code>futimens</code>() and <code>utimensat</code>() are specified in POSIX.1-2008.</p>
<h2>NOTES</h2>
<p> <code>utimensat</code>() obsoletes <code><a href="/docs/linux/man/2-futimesat/">futimesat</a></code>(2). </p>
<p> On Linux, timestamps cannot be changed for a file marked immutable, and the only change permitted for files marked append-only is to set the timestamps to the current time. (This is consistent with the historical behavior of <code><a href="/docs/linux/man/2-utime/">utime</a></code>(2) and <code><a href="/docs/linux/man/2-utimes/">utimes</a></code>(2) on Linux.) </p>
<p> If both <i>tv_nsec</i> fields are specified as <code>UTIME_OMIT</code>, then the Linux implementation of <code>utimensat</code>() succeeds even if the file referred to by <i>dirfd</i> and <i>pathname</i> does not exist.</p>
<h3>C library/kernel ABI differences</h3>
<p> On Linux, <code>futimens</code>() is a library function implemented on top of the <code>utimensat</code>() system call. To support this, the Linux <code>utimensat</code>() system call implements a nonstandard feature: if <i>pathname</i> is NULL, then the call modifies the timestamps of the file referred to by the file descriptor <i>dirfd</i> (which may refer to any type of file). Using this feature, the call <i>futimens(fd, times)</i> is implemented as: </p>
<p> utimensat(fd, NULL, times, 0); </p>
<p> Note, however, that the glibc wrapper for <code>utimensat</code>() disallows passing NULL as the value for <i>pathname</i>: the wrapper function returns the error <code>EINVAL</code> in this case.</p>
<h2>BUGS</h2>
<p> Several bugs afflict <code>utimensat</code>() and <code>futimens</code>() on kernels before 2.6.26. These bugs are either nonconformances with the POSIX.1 draft specification or inconsistencies with historical Linux behavior.</p>
<dl>
<dt>*</p>
<dd> POSIX.1 specifies that if one of the <i>tv_nsec</i> fields has the value <code>UTIME_NOW</code> or <code>UTIME_OMIT</code>, then the value of the corresponding <i>tv_sec</i> field should be ignored. Instead, the value of the <i>tv_sec</i> field is required to be 0 (or the error <code>EINVAL</code> results).</p>
<dt>*</p>
<dd> Various bugs mean that for the purposes of permission checking, the case where both <i>tv_nsec</i> fields are set to <code>UTIME_NOW</code> isn&#8217;t always treated the same as specifying <i>times</i> as NULL, and the case where one <i>tv_nsec</i> value is <code>UTIME_NOW</code> and the other is <code>UTIME_OMIT</code> isn&#8217;t treated the same as specifying <i>times</i> as a pointer to an array of structures containing arbitrary time values. As a result, in some cases: a) file timestamps can be updated by a process that shouldn&#8217;t have permission to perform updates; b) file timestamps can&#8217;t be updated by a process that should have permission to perform updates; and c) the wrong <i>errno</i> value is returned in case of an error.</p>
<dt>*</p>
<dd> POSIX.1 says that a process that has <i>write access to the file</i> can make a call with <i>times</i> as NULL, or with <i>times</i> pointing to an array of structures in which both <i>tv_nsec</i> fields are <code>UTIME_NOW</code>, in order to update both timestamps to the current time. However, <code>futimens</code>() instead checks whether the <i>access mode of the file descriptor allows writing</i>.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-chattr/">chattr</a></code>(1), <code><a href="/docs/linux/man/1-touch/">touch</a></code>(1), <code><a href="/docs/linux/man/2-futimesat/">futimesat</a></code>(2), <code><a href="/docs/linux/man/2-openat/">openat</a></code>(2), <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2), <code><a href="/docs/linux/man/2-utimes/">utimes</a></code>(2), <code><a href="/docs/linux/man/3-futimes/">futimes</a></code>(3), <code><a href="/docs/linux/man/7-inode/">inode</a></code>(7), <code><a href="/docs/linux/man/7-path_resolution/">path_resolution</a></code>(7), <code><a href="/docs/linux/man/7-symlink/">symlink</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
