---
title: "errno(3)"
name: "errno"
section: "3"
letter: "e"
url: "/docs/linux/man/3-errno/"
description: "errno – number of last error"
---

<h2 class="name">NAME</h2>
<p> errno &#8211; number of last error </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;errno.h&gt;</code></p>
<h2>DESCRIPTION</h2>
<p> The <i>&lt;errno.h&gt;</i> header file defines the integer variable <i>errno</i>, which is set by system calls and some library functions in the event of an error to indicate what went wrong.</p>
<h3>errno</h3>
<p> The value in <i>errno</i> is significant only when the return value of the call indicated an error (i.e., -1 from most system calls; -1 or NULL from most library functions); a function that succeeds <i>is</i> allowed to change <i>errno</i>. The value of <i>errno</i> is never set to zero by any system call or library function. </p>
<p> For some system calls and library functions (e.g., <code><a href="/docs/linux/man/2-getpriority/">getpriority</a></code>(2)), -1 is a valid return on success. In such cases, a successful return can be distinguished from an error return by setting <i>errno</i> to zero before the call, and then, if the call returns a status that indicates that an error may have occurred, checking to see if <i>errno</i> has a nonzero value. </p>
<p> <i>errno</i> is defined by the ISO C standard to be a modifiable lvalue of type <i>int</i>, and must not be explicitly declared; <i>errno</i> may be a macro. <i>errno</i> is thread-local; setting it in one thread does not affect its value in any other thread.</p>
<h3>Error numbers and names</h3>
<p> Valid error numbers are all positive numbers. The <i>&lt;errno.h&gt;</i> header file defines symbolic names for each of the possible error numbers that may appear in <i>errno</i>. </p>
<p> All the error names specified by POSIX.1 must have distinct values, with the exception of <code>EAGAIN</code> and <code>EWOULDBLOCK</code>, which may be the same. On Linux, these two have the same value on all architectures. </p>
<p> The error numbers that correspond to each symbolic name vary across UNIX systems, and even across different architectures on Linux. Therefore, numeric values are not included as part of the list of error names below. The <code><a href="/docs/linux/man/3-perror/">perror</a></code>(3) and <code><a href="/docs/linux/man/3-strerror/">strerror</a></code>(3) functions can be used to convert these names to corresponding textual error messages. </p>
<p> On any particular Linux system, one can obtain a list of all symbolic error names and the corresponding error numbers using the <code><a href="/docs/linux/man/1-errno/">errno</a></code>(1) command (part of the <i>moreutils</i> package): </p>
<p> $ <code>errno -l</code> EPERM 1 Operation not permitted ENOENT 2 No such file or directory ESRCH 3 No such process EINTR 4 Interrupted system call EIO 5 Input/output error &#8230; </p>
<p> The <code><a href="/docs/linux/man/1-errno/">errno</a></code>(1) command can also be used to look up individual error numbers and names, and to search for errors using strings from the error description, as in the following examples: </p>
<p> $ <code>errno 2</code> ENOENT 2 No such file or directory $ <code>errno ESRCH</code> ESRCH 3 No such process $ <code>errno -s permission</code> EACCES 13 Permission denied</p>
<h3>List of error names</h3>
<p> In the list of the symbolic error names below, various names are marked as follows:</p>
<dl>
<dt>*</dt>
<dd> <i>POSIX.1-2001</i>: The name is defined by POSIX.1-2001, and is defined in later POSIX.1 versions, unless otherwise indicated.</dd>
<dt>*</dt>
<dd> <i>POSIX.1-2008</i>: The name is defined in POSIX.1-2008, but was not present in earlier POSIX.1 standards.</dd>
<dt>*</dt>
<dd> <i>C99</i>: The name is defined by C99.</dd></dl>
<p> Below is a list of the symbolic error names that are defined on Linux:</p>
<dl>
<dt><code>E2BIG</code></dt>
<dd> Argument list too long (POSIX.1-2001).</dd>
<dt><code>EACCES</code></dt>
<dd> Permission denied (POSIX.1-2001).</dd>
<dt><code>EADDRINUSE</code></dt>
<dd> Address already in use (POSIX.1-2001).</dd>
<dt><code>EADDRNOTAVAIL</code></dt>
<dd> Address not available (POSIX.1-2001).</dd>
<dt><code>EAFNOSUPPORT</code></dt>
<dd> Address family not supported (POSIX.1-2001).</dd>
<dt><code>EAGAIN</code></dt>
<dd> Resource temporarily unavailable (may be the same value as <code>EWOULDBLOCK</code>) (POSIX.1-2001).</dd>
<dt><code>EALREADY</code></dt>
<dd> Connection already in progress (POSIX.1-2001).</dd>
<dt><code>EBADE</code></dt>
<dd> Invalid exchange.</dd>
<dt><code>EBADF</code></dt>
<dd> Bad file descriptor (POSIX.1-2001).</dd>
<dt><code>EBADFD</code></dt>
<dd> File descriptor in bad state.</dd>
<dt><code>EBADMSG</code></dt>
<dd> Bad message (POSIX.1-2001).</dd>
<dt><code>EBADR</code></dt>
<dd> Invalid request descriptor.</dd>
<dt><code>EBADRQC</code></dt>
<dd> Invalid request code.</dd>
<dt><code>EBADSLT</code></dt>
<dd> Invalid slot.</dd>
<dt><code>EBUSY</code></dt>
<dd> Device or resource busy (POSIX.1-2001).</dd>
<dt><code>ECANCELED</code></dt>
<dd> Operation canceled (POSIX.1-2001).</dd>
<dt><code>ECHILD</code></dt>
<dd> No child processes (POSIX.1-2001).</dd>
<dt><code>ECHRNG</code></dt>
<dd> Channel number out of range.</dd>
<dt><code>ECOMM</code></dt>
<dd> Communication error on send.</dd>
<dt><code>ECONNABORTED</code></dt>
<dd> Connection aborted (POSIX.1-2001).</dd>
<dt><code>ECONNREFUSED</code></dt>
<dd> Connection refused (POSIX.1-2001).</dd>
<dt><code>ECONNRESET</code></dt>
<dd> Connection reset (POSIX.1-2001).</dd>
<dt><code>EDEADLK</code></dt>
<dd> Resource deadlock avoided (POSIX.1-2001).</dd>
<dt><code>EDEADLOCK</code></dt>
<dd> On most architectures, a synonym for <code>EDEADLK</code>. On some architectures (e.g., Linux MIPS, PowerPC, SPARC), it is a separate error code &quot;File locking deadlock error&quot;.</dd>
<dt><code>EDESTADDRREQ</code></dt>
<dd> Destination address required (POSIX.1-2001).</dd>
<dt><code>EDOM</code></dt>
<dd> Mathematics argument out of domain of function (POSIX.1, C99).</dd>
<dt><code>EDQUOT</code></dt>
<dd> Disk quota exceeded (POSIX.1-2001).</dd>
<dt><code>EEXIST</code></dt>
<dd> File exists (POSIX.1-2001).</dd>
<dt><code>EFAULT</code></dt>
<dd> Bad address (POSIX.1-2001).</dd>
<dt><code>EFBIG</code></dt>
<dd> File too large (POSIX.1-2001).</dd>
<dt><code>EHOSTDOWN</code></dt>
<dd> Host is down.</dd>
<dt><code>EHOSTUNREACH</code></dt>
<dd> Host is unreachable (POSIX.1-2001).</dd>
<dt><code>EHWPOISON</code></dt>
<dd> Memory page has hardware error.</dd>
<dt><code>EIDRM</code></dt>
<dd> Identifier removed (POSIX.1-2001).</dd>
<dt><code>EILSEQ</code></dt>
<dd> Invalid or incomplete multibyte or wide character (POSIX.1, C99).</dd>
<dt>
</dt><dd> The text shown here is the glibc error description; in POSIX.1, this error is described as &quot;Illegal byte sequence&quot;.</dd>
<dt><code>EINPROGRESS</code></dt>
<dd> Operation in progress (POSIX.1-2001).</dd>
<dt><code>EINTR</code></dt>
<dd> Interrupted function call (POSIX.1-2001); see <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7).</dd>
<dt><code>EINVAL</code></dt>
<dd> Invalid argument (POSIX.1-2001).</dd>
<dt><code>EIO</code></dt>
<dd> Input/output error (POSIX.1-2001).</dd>
<dt><code>EISCONN</code></dt>
<dd> Socket is connected (POSIX.1-2001).</dd>
<dt><code>EISDIR</code></dt>
<dd> Is a directory (POSIX.1-2001).</dd>
<dt><code>EISNAM</code></dt>
<dd> Is a named type file.</dd>
<dt><code>EKEYEXPIRED</code></dt>
<dd> Key has expired.</dd>
<dt><code>EKEYREJECTED</code></dt>
<dd> Key was rejected by service.</dd>
<dt><code>EKEYREVOKED</code></dt>
<dd> Key has been revoked.</dd>
<dt><code>EL2HLT</code></dt>
<dd> Level 2 halted.</dd>
<dt><code>EL2NSYNC</code></dt>
<dd> Level 2 not synchronized.</dd>
<dt><code>EL3HLT</code></dt>
<dd> Level 3 halted.</dd>
<dt><code>EL3RST</code></dt>
<dd> Level 3 reset.</dd>
<dt><code>ELIBACC</code></dt>
<dd> Cannot access a needed shared library.</dd>
<dt><code>ELIBBAD</code></dt>
<dd> Accessing a corrupted shared library.</dd>
<dt><code>ELIBMAX</code></dt>
<dd> Attempting to link in too many shared libraries.</dd>
<dt><code>ELIBSCN</code></dt>
<dd> .lib section in a.out corrupted</dd>
<dt><code>ELIBEXEC</code></dt>
<dd> Cannot exec a shared library directly.</dd>
<dt><code>ELNRANGE</code></dt>
<dd> Link number out of range.</dd>
<dt><code>ELOOP</code></dt>
<dd> Too many levels of symbolic links (POSIX.1-2001).</dd>
<dt><code>EMEDIUMTYPE</code></dt>
<dd> Wrong medium type.</dd>
<dt><code>EMFILE</code></dt>
<dd> Too many open files (POSIX.1-2001). Commonly caused by exceeding the <code>RLIMIT_NOFILE</code> resource limit described in <code><a href="/docs/linux/man/2-getrlimit/">getrlimit</a></code>(2). Can also be caused by exceeding the limit specified in <i>/proc/sys/fs/nr_open</i>.</dd>
<dt><code>EMLINK</code></dt>
<dd> Too many links (POSIX.1-2001).</dd>
<dt><code>EMSGSIZE</code></dt>
<dd> Message too long (POSIX.1-2001).</dd>
<dt><code>EMULTIHOP</code></dt>
<dd> Multihop attempted (POSIX.1-2001).</dd>
<dt><code>ENAMETOOLONG</code></dt>
<dd> Filename too long (POSIX.1-2001).</dd>
<dt><code>ENETDOWN</code></dt>
<dd> Network is down (POSIX.1-2001).</dd>
<dt><code>ENETRESET</code></dt>
<dd> Connection aborted by network (POSIX.1-2001).</dd>
<dt><code>ENETUNREACH</code></dt>
<dd> Network unreachable (POSIX.1-2001).</dd>
<dt><code>ENFILE</code></dt>
<dd> Too many open files in system (POSIX.1-2001). On Linux, this is probably a result of encountering the <i>/proc/sys/fs/file-max</i> limit (see <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5)).</dd>
<dt><code>ENOANO</code></dt>
<dd> No anode.</dd>
<dt><code>ENOBUFS</code></dt>
<dd> No buffer space available (POSIX.1 (XSI STREAMS option)).</dd>
<dt><code>ENODATA</code></dt>
<dd> No message is available on the STREAM head read queue (POSIX.1-2001).</dd>
<dt><code>ENODEV</code></dt>
<dd> No such device (POSIX.1-2001).</dd>
<dt><code>ENOENT</code></dt>
<dd> No such file or directory (POSIX.1-2001).</dd>
<dt>
</dt><dd> Typically, this error results when a specified pathname does not exist, or one of the components in the directory prefix of a pathname does not exist, or the specified pathname is a dangling symbolic link.</dd>
<dt><code>ENOEXEC</code></dt>
<dd> Exec format error (POSIX.1-2001).</dd>
<dt><code>ENOKEY</code></dt>
<dd> Required key not available.</dd>
<dt><code>ENOLCK</code></dt>
<dd> No locks available (POSIX.1-2001).</dd>
<dt><code>ENOLINK</code></dt>
<dd> Link has been severed (POSIX.1-2001).</dd>
<dt><code>ENOMEDIUM</code></dt>
<dd> No medium found.</dd>
<dt><code>ENOMEM</code></dt>
<dd> Not enough space/cannot allocate memory (POSIX.1-2001).</dd>
<dt><code>ENOMSG</code></dt>
<dd> No message of the desired type (POSIX.1-2001).</dd>
<dt><code>ENONET</code></dt>
<dd> Machine is not on the network.</dd>
<dt><code>ENOPKG</code></dt>
<dd> Package not installed.</dd>
<dt><code>ENOPROTOOPT</code></dt>
<dd> Protocol not available (POSIX.1-2001).</dd>
<dt><code>ENOSPC</code></dt>
<dd> No space left on device (POSIX.1-2001).</dd>
<dt><code>ENOSR</code></dt>
<dd> No STREAM resources (POSIX.1 (XSI STREAMS option)).</dd>
<dt><code>ENOSTR</code></dt>
<dd> Not a STREAM (POSIX.1 (XSI STREAMS option)).</dd>
<dt><code>ENOSYS</code></dt>
<dd> Function not implemented (POSIX.1-2001).</dd>
<dt><code>ENOTBLK</code></dt>
<dd> Block device required.</dd>
<dt><code>ENOTCONN</code></dt>
<dd> The socket is not connected (POSIX.1-2001).</dd>
<dt><code>ENOTDIR</code></dt>
<dd> Not a directory (POSIX.1-2001).</dd>
<dt><code>ENOTEMPTY</code></dt>
<dd> Directory not empty (POSIX.1-2001).</dd>
<dt><code>ENOTRECOVERABLE</code></dt>
<dd> State not recoverable (POSIX.1-2008).</dd>
<dt><code>ENOTSOCK</code></dt>
<dd> Not a socket (POSIX.1-2001).</dd>
<dt><code>ENOTSUP</code></dt>
<dd> Operation not supported (POSIX.1-2001).</dd>
<dt><code>ENOTTY</code></dt>
<dd> Inappropriate I/O control operation (POSIX.1-2001).</dd>
<dt><code>ENOTUNIQ</code></dt>
<dd> Name not unique on network.</dd>
<dt><code>ENXIO</code></dt>
<dd> No such device or address (POSIX.1-2001).</dd>
<dt><code>EOPNOTSUPP</code></dt>
<dd> Operation not supported on socket (POSIX.1-2001).</dd>
<dt>
</dt><dd> (<code>ENOTSUP</code> and <code>EOPNOTSUPP</code> have the same value on Linux, but according to POSIX.1 these error values should be distinct.)</dd>
<dt><code>EOVERFLOW</code></dt>
<dd> Value too large to be stored in data type (POSIX.1-2001).</dd>
<dt><code>EOWNERDEAD</code></dt>
<dd> Owner died (POSIX.1-2008).</dd>
<dt><code>EPERM</code></dt>
<dd> Operation not permitted (POSIX.1-2001).</dd>
<dt><code>EPFNOSUPPORT</code></dt>
<dd> Protocol family not supported.</dd>
<dt><code>EPIPE</code></dt>
<dd> Broken pipe (POSIX.1-2001).</dd>
<dt><code>EPROTO</code></dt>
<dd> Protocol error (POSIX.1-2001).</dd>
<dt><code>EPROTONOSUPPORT</code></dt>
<dd> Protocol not supported (POSIX.1-2001).</dd>
<dt><code>EPROTOTYPE</code></dt>
<dd> Protocol wrong type for socket (POSIX.1-2001).</dd>
<dt><code>ERANGE</code></dt>
<dd> Result too large (POSIX.1, C99).</dd>
<dt><code>EREMCHG</code></dt>
<dd> Remote address changed.</dd>
<dt><code>EREMOTE</code></dt>
<dd> Object is remote.</dd>
<dt><code>EREMOTEIO</code></dt>
<dd> Remote I/O error.</dd>
<dt><code>ERESTART</code></dt>
<dd> Interrupted system call should be restarted.</dd>
<dt><code>ERFKILL</code></dt>
<dd> Operation not possible due to RF-kill.</dd>
<dt><code>EROFS</code></dt>
<dd> Read-only filesystem (POSIX.1-2001).</dd>
<dt><code>ESHUTDOWN</code></dt>
<dd> Cannot send after transport endpoint shutdown.</dd>
<dt><code>ESPIPE</code></dt>
<dd> Invalid seek (POSIX.1-2001).</dd>
<dt><code>ESOCKTNOSUPPORT</code></dt>
<dd> Socket type not supported.</dd>
<dt><code>ESRCH</code></dt>
<dd> No such process (POSIX.1-2001).</dd>
<dt><code>ESTALE</code></dt>
<dd> Stale file handle (POSIX.1-2001).</dd>
<dt>
</dt><dd> This error can occur for NFS and for other filesystems.</dd>
<dt><code>ESTRPIPE</code></dt>
<dd> Streams pipe error.</dd>
<dt><code>ETIME</code></dt>
<dd> Timer expired (POSIX.1 (XSI STREAMS option)).</dd>
<dt>
</dt><dd> (POSIX.1 says &quot;STREAM <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) timeout&quot;.)</dd>
<dt><code>ETIMEDOUT</code></dt>
<dd> Connection timed out (POSIX.1-2001).</dd>
<dt><code>ETOOMANYREFS</code></dt>
<dd> Too many references: cannot splice.</dd>
<dt><code>ETXTBSY</code></dt>
<dd> Text file busy (POSIX.1-2001).</dd>
<dt><code>EUCLEAN</code></dt>
<dd> Structure needs cleaning.</dd>
<dt><code>EUNATCH</code></dt>
<dd> Protocol driver not attached.</dd>
<dt><code>EUSERS</code></dt>
<dd> Too many users.</dd>
<dt><code>EWOULDBLOCK</code></dt>
<dd> Operation would block (may be same value as <code>EAGAIN</code>) (POSIX.1-2001).</dd>
<dt><code>EXDEV</code></dt>
<dd> Improper link (POSIX.1-2001).</dd>
<dt><code>EXFULL</code></dt>
<dd> Exchange full.</dd></dl>
<h2>NOTES</h2>
<p> A common mistake is to do </p>
<p> if (somecall() == -1) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;somecall()&nbsp;failed
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(errno&nbsp;==&nbsp;&#8230;)&nbsp;{&nbsp;&#8230;&nbsp;} } </p>
<p> where <i>errno</i> no longer needs to have the value it had upon return from <i>somecall</i>() (i.e., it may have been changed by the <code><a href="/docs/linux/man/3-printf/">printf</a></code>(3)). If the value of <i>errno</i> should be preserved across a library call, it must be saved: </p>
<p> if (somecall() == -1) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int errsv&nbsp;=&nbsp;errno;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;somecall()&nbsp;failed
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(errsv&nbsp;==&nbsp;&#8230;)&nbsp;{&nbsp;&#8230;&nbsp;} } </p>
<p> Note that the POSIX threads APIs do <i>not</i> set <i>errno</i> on error. Instead, on failure they return an error number as the function result. These error numbers have the same meanings as the error numbers returned in <i>errno</i> by other APIs. </p>
<p> On some ancient systems, <i>&lt;errno.h&gt;</i> was not present or did not declare <i>errno</i>, so that it was necessary to declare <i>errno</i> manually (i.e., <i>extern int errno</i>). <code>Do not do this</code>. It long ago ceased to be necessary, and it will cause problems with modern versions of the C library.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-errno/">errno</a></code>(1), <code><a href="/docs/linux/man/3-err/">err</a></code>(3), <code><a href="/docs/linux/man/3-error/">error</a></code>(3), <code><a href="/docs/linux/man/3-perror/">perror</a></code>(3), <code><a href="/docs/linux/man/3-strerror/">strerror</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
