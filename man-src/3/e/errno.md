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
<dt>*</p>
<dd> <i>POSIX.1-2001</i>: The name is defined by POSIX.1-2001, and is defined in later POSIX.1 versions, unless otherwise indicated.</p>
<dt>*</p>
<dd> <i>POSIX.1-2008</i>: The name is defined in POSIX.1-2008, but was not present in earlier POSIX.1 standards.</p>
<dt>*</p>
<dd> <i>C99</i>: The name is defined by C99.</dl>
<p> Below is a list of the symbolic error names that are defined on Linux:</p>
<dl>
<dt><code>E2BIG</code></p>
<dd> Argument list too long (POSIX.1-2001).</p>
<dt><code>EACCES</code></p>
<dd> Permission denied (POSIX.1-2001).</p>
<dt><code>EADDRINUSE</code></p>
<dd> Address already in use (POSIX.1-2001).</p>
<dt><code>EADDRNOTAVAIL</code></p>
<dd> Address not available (POSIX.1-2001).</p>
<dt><code>EAFNOSUPPORT</code></p>
<dd> Address family not supported (POSIX.1-2001).</p>
<dt><code>EAGAIN</code></p>
<dd> Resource temporarily unavailable (may be the same value as <code>EWOULDBLOCK</code>) (POSIX.1-2001).</p>
<dt><code>EALREADY</code></p>
<dd> Connection already in progress (POSIX.1-2001).</p>
<dt><code>EBADE</code></p>
<dd> Invalid exchange.</p>
<dt><code>EBADF</code></p>
<dd> Bad file descriptor (POSIX.1-2001).</p>
<dt><code>EBADFD</code></p>
<dd> File descriptor in bad state.</p>
<dt><code>EBADMSG</code></p>
<dd> Bad message (POSIX.1-2001).</p>
<dt><code>EBADR</code></p>
<dd> Invalid request descriptor.</p>
<dt><code>EBADRQC</code></p>
<dd> Invalid request code.</p>
<dt><code>EBADSLT</code></p>
<dd> Invalid slot.</p>
<dt><code>EBUSY</code></p>
<dd> Device or resource busy (POSIX.1-2001).</p>
<dt><code>ECANCELED</code></p>
<dd> Operation canceled (POSIX.1-2001).</p>
<dt><code>ECHILD</code></p>
<dd> No child processes (POSIX.1-2001).</p>
<dt><code>ECHRNG</code></p>
<dd> Channel number out of range.</p>
<dt><code>ECOMM</code></p>
<dd> Communication error on send.</p>
<dt><code>ECONNABORTED</code></p>
<dd> Connection aborted (POSIX.1-2001).</p>
<dt><code>ECONNREFUSED</code></p>
<dd> Connection refused (POSIX.1-2001).</p>
<dt><code>ECONNRESET</code></p>
<dd> Connection reset (POSIX.1-2001).</p>
<dt><code>EDEADLK</code></p>
<dd> Resource deadlock avoided (POSIX.1-2001).</p>
<dt><code>EDEADLOCK</code></p>
<dd> On most architectures, a synonym for <code>EDEADLK</code>. On some architectures (e.g., Linux MIPS, PowerPC, SPARC), it is a separate error code &quot;File locking deadlock error&quot;.</p>
<dt><code>EDESTADDRREQ</code></p>
<dd> Destination address required (POSIX.1-2001).</p>
<dt><code>EDOM</code></p>
<dd> Mathematics argument out of domain of function (POSIX.1, C99).</p>
<dt><code>EDQUOT</code></p>
<dd> Disk quota exceeded (POSIX.1-2001).</p>
<dt><code>EEXIST</code></p>
<dd> File exists (POSIX.1-2001).</p>
<dt><code>EFAULT</code></p>
<dd> Bad address (POSIX.1-2001).</p>
<dt><code>EFBIG</code></p>
<dd> File too large (POSIX.1-2001).</p>
<dt><code>EHOSTDOWN</code></p>
<dd> Host is down.</p>
<dt><code>EHOSTUNREACH</code></p>
<dd> Host is unreachable (POSIX.1-2001).</p>
<dt><code>EHWPOISON</code></p>
<dd> Memory page has hardware error.</p>
<dt><code>EIDRM</code></p>
<dd> Identifier removed (POSIX.1-2001).</p>
<dt><code>EILSEQ</code></p>
<dd> Invalid or incomplete multibyte or wide character (POSIX.1, C99).</p>
<dt>
<dd> The text shown here is the glibc error description; in POSIX.1, this error is described as &quot;Illegal byte sequence&quot;.</p>
<dt><code>EINPROGRESS</code></p>
<dd> Operation in progress (POSIX.1-2001).</p>
<dt><code>EINTR</code></p>
<dd> Interrupted function call (POSIX.1-2001); see <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7).</p>
<dt><code>EINVAL</code></p>
<dd> Invalid argument (POSIX.1-2001).</p>
<dt><code>EIO</code></p>
<dd> Input/output error (POSIX.1-2001).</p>
<dt><code>EISCONN</code></p>
<dd> Socket is connected (POSIX.1-2001).</p>
<dt><code>EISDIR</code></p>
<dd> Is a directory (POSIX.1-2001).</p>
<dt><code>EISNAM</code></p>
<dd> Is a named type file.</p>
<dt><code>EKEYEXPIRED</code></p>
<dd> Key has expired.</p>
<dt><code>EKEYREJECTED</code></p>
<dd> Key was rejected by service.</p>
<dt><code>EKEYREVOKED</code></p>
<dd> Key has been revoked.</p>
<dt><code>EL2HLT</code></p>
<dd> Level 2 halted.</p>
<dt><code>EL2NSYNC</code></p>
<dd> Level 2 not synchronized.</p>
<dt><code>EL3HLT</code></p>
<dd> Level 3 halted.</p>
<dt><code>EL3RST</code></p>
<dd> Level 3 reset.</p>
<dt><code>ELIBACC</code></p>
<dd> Cannot access a needed shared library.</p>
<dt><code>ELIBBAD</code></p>
<dd> Accessing a corrupted shared library.</p>
<dt><code>ELIBMAX</code></p>
<dd> Attempting to link in too many shared libraries.</p>
<dt><code>ELIBSCN</code></p>
<dd> .lib section in a.out corrupted</p>
<dt><code>ELIBEXEC</code></p>
<dd> Cannot exec a shared library directly.</p>
<dt><code>ELNRANGE</code></p>
<dd> Link number out of range.</p>
<dt><code>ELOOP</code></p>
<dd> Too many levels of symbolic links (POSIX.1-2001).</p>
<dt><code>EMEDIUMTYPE</code></p>
<dd> Wrong medium type.</p>
<dt><code>EMFILE</code></p>
<dd> Too many open files (POSIX.1-2001). Commonly caused by exceeding the <code>RLIMIT_NOFILE</code> resource limit described in <code><a href="/docs/linux/man/2-getrlimit/">getrlimit</a></code>(2). Can also be caused by exceeding the limit specified in <i>/proc/sys/fs/nr_open</i>.</p>
<dt><code>EMLINK</code></p>
<dd> Too many links (POSIX.1-2001).</p>
<dt><code>EMSGSIZE</code></p>
<dd> Message too long (POSIX.1-2001).</p>
<dt><code>EMULTIHOP</code></p>
<dd> Multihop attempted (POSIX.1-2001).</p>
<dt><code>ENAMETOOLONG</code></p>
<dd> Filename too long (POSIX.1-2001).</p>
<dt><code>ENETDOWN</code></p>
<dd> Network is down (POSIX.1-2001).</p>
<dt><code>ENETRESET</code></p>
<dd> Connection aborted by network (POSIX.1-2001).</p>
<dt><code>ENETUNREACH</code></p>
<dd> Network unreachable (POSIX.1-2001).</p>
<dt><code>ENFILE</code></p>
<dd> Too many open files in system (POSIX.1-2001). On Linux, this is probably a result of encountering the <i>/proc/sys/fs/file-max</i> limit (see <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5)).</p>
<dt><code>ENOANO</code></p>
<dd> No anode.</p>
<dt><code>ENOBUFS</code></p>
<dd> No buffer space available (POSIX.1 (XSI STREAMS option)).</p>
<dt><code>ENODATA</code></p>
<dd> No message is available on the STREAM head read queue (POSIX.1-2001).</p>
<dt><code>ENODEV</code></p>
<dd> No such device (POSIX.1-2001).</p>
<dt><code>ENOENT</code></p>
<dd> No such file or directory (POSIX.1-2001).</p>
<dt>
<dd> Typically, this error results when a specified pathname does not exist, or one of the components in the directory prefix of a pathname does not exist, or the specified pathname is a dangling symbolic link.</p>
<dt><code>ENOEXEC</code></p>
<dd> Exec format error (POSIX.1-2001).</p>
<dt><code>ENOKEY</code></p>
<dd> Required key not available.</p>
<dt><code>ENOLCK</code></p>
<dd> No locks available (POSIX.1-2001).</p>
<dt><code>ENOLINK</code></p>
<dd> Link has been severed (POSIX.1-2001).</p>
<dt><code>ENOMEDIUM</code></p>
<dd> No medium found.</p>
<dt><code>ENOMEM</code></p>
<dd> Not enough space/cannot allocate memory (POSIX.1-2001).</p>
<dt><code>ENOMSG</code></p>
<dd> No message of the desired type (POSIX.1-2001).</p>
<dt><code>ENONET</code></p>
<dd> Machine is not on the network.</p>
<dt><code>ENOPKG</code></p>
<dd> Package not installed.</p>
<dt><code>ENOPROTOOPT</code></p>
<dd> Protocol not available (POSIX.1-2001).</p>
<dt><code>ENOSPC</code></p>
<dd> No space left on device (POSIX.1-2001).</p>
<dt><code>ENOSR</code></p>
<dd> No STREAM resources (POSIX.1 (XSI STREAMS option)).</p>
<dt><code>ENOSTR</code></p>
<dd> Not a STREAM (POSIX.1 (XSI STREAMS option)).</p>
<dt><code>ENOSYS</code></p>
<dd> Function not implemented (POSIX.1-2001).</p>
<dt><code>ENOTBLK</code></p>
<dd> Block device required.</p>
<dt><code>ENOTCONN</code></p>
<dd> The socket is not connected (POSIX.1-2001).</p>
<dt><code>ENOTDIR</code></p>
<dd> Not a directory (POSIX.1-2001).</p>
<dt><code>ENOTEMPTY</code></p>
<dd> Directory not empty (POSIX.1-2001).</p>
<dt><code>ENOTRECOVERABLE</code></p>
<dd> State not recoverable (POSIX.1-2008).</p>
<dt><code>ENOTSOCK</code></p>
<dd> Not a socket (POSIX.1-2001).</p>
<dt><code>ENOTSUP</code></p>
<dd> Operation not supported (POSIX.1-2001).</p>
<dt><code>ENOTTY</code></p>
<dd> Inappropriate I/O control operation (POSIX.1-2001).</p>
<dt><code>ENOTUNIQ</code></p>
<dd> Name not unique on network.</p>
<dt><code>ENXIO</code></p>
<dd> No such device or address (POSIX.1-2001).</p>
<dt><code>EOPNOTSUPP</code></p>
<dd> Operation not supported on socket (POSIX.1-2001).</p>
<dt>
<dd> (<code>ENOTSUP</code> and <code>EOPNOTSUPP</code> have the same value on Linux, but according to POSIX.1 these error values should be distinct.)</p>
<dt><code>EOVERFLOW</code></p>
<dd> Value too large to be stored in data type (POSIX.1-2001).</p>
<dt><code>EOWNERDEAD</code></p>
<dd> Owner died (POSIX.1-2008).</p>
<dt><code>EPERM</code></p>
<dd> Operation not permitted (POSIX.1-2001).</p>
<dt><code>EPFNOSUPPORT</code></p>
<dd> Protocol family not supported.</p>
<dt><code>EPIPE</code></p>
<dd> Broken pipe (POSIX.1-2001).</p>
<dt><code>EPROTO</code></p>
<dd> Protocol error (POSIX.1-2001).</p>
<dt><code>EPROTONOSUPPORT</code></p>
<dd> Protocol not supported (POSIX.1-2001).</p>
<dt><code>EPROTOTYPE</code></p>
<dd> Protocol wrong type for socket (POSIX.1-2001).</p>
<dt><code>ERANGE</code></p>
<dd> Result too large (POSIX.1, C99).</p>
<dt><code>EREMCHG</code></p>
<dd> Remote address changed.</p>
<dt><code>EREMOTE</code></p>
<dd> Object is remote.</p>
<dt><code>EREMOTEIO</code></p>
<dd> Remote I/O error.</p>
<dt><code>ERESTART</code></p>
<dd> Interrupted system call should be restarted.</p>
<dt><code>ERFKILL</code></p>
<dd> Operation not possible due to RF-kill.</p>
<dt><code>EROFS</code></p>
<dd> Read-only filesystem (POSIX.1-2001).</p>
<dt><code>ESHUTDOWN</code></p>
<dd> Cannot send after transport endpoint shutdown.</p>
<dt><code>ESPIPE</code></p>
<dd> Invalid seek (POSIX.1-2001).</p>
<dt><code>ESOCKTNOSUPPORT</code></p>
<dd> Socket type not supported.</p>
<dt><code>ESRCH</code></p>
<dd> No such process (POSIX.1-2001).</p>
<dt><code>ESTALE</code></p>
<dd> Stale file handle (POSIX.1-2001).</p>
<dt>
<dd> This error can occur for NFS and for other filesystems.</p>
<dt><code>ESTRPIPE</code></p>
<dd> Streams pipe error.</p>
<dt><code>ETIME</code></p>
<dd> Timer expired (POSIX.1 (XSI STREAMS option)).</p>
<dt>
<dd> (POSIX.1 says &quot;STREAM <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) timeout&quot;.)</p>
<dt><code>ETIMEDOUT</code></p>
<dd> Connection timed out (POSIX.1-2001).</p>
<dt><code>ETOOMANYREFS</code></p>
<dd> Too many references: cannot splice.</p>
<dt><code>ETXTBSY</code></p>
<dd> Text file busy (POSIX.1-2001).</p>
<dt><code>EUCLEAN</code></p>
<dd> Structure needs cleaning.</p>
<dt><code>EUNATCH</code></p>
<dd> Protocol driver not attached.</p>
<dt><code>EUSERS</code></p>
<dd> Too many users.</p>
<dt><code>EWOULDBLOCK</code></p>
<dd> Operation would block (may be same value as <code>EAGAIN</code>) (POSIX.1-2001).</p>
<dt><code>EXDEV</code></p>
<dd> Improper link (POSIX.1-2001).</p>
<dt><code>EXFULL</code></p>
<dd> Exchange full.</dl>
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
