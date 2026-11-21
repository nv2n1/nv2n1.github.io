---

title: "unix(7)"
name: "unix"
section: "7"
letter: "u"
url: "/docs/linux/man/7-unix/"
description: "unix – sockets for local interprocess communication"
---

<p>unix &#8211; sockets for local interprocess communication </p>
<p> <code>#include &lt;sys/socket.h&gt;</code> <br />
 <code>#include &lt;sys/un.h&gt;</code> </p>
<p> <i>unix_socket</i><code> = socket(AF_UNIX, type, 0);</code> <br />
 <i>error</i><code> = socketpair(AF_UNIX, type, 0, int *</code><i>sv</i><code>);</code>  </p>
<p> The <code>AF_UNIX</code> (also known as <code>AF_LOCAL</code>) socket family is used to communicate between processes on the same machine efficiently. Traditionally, UNIX domain sockets can be either unnamed, or bound to a filesystem pathname (marked as being of type socket). Linux also supports an abstract namespace which is independent of the filesystem. </p>
<p>Valid socket types in the UNIX domain are: <code>SOCK_STREAM</code>, for a stream-oriented socket; <code>SOCK_DGRAM</code>, for a datagram-oriented socket that preserves message boundaries (as on most UNIX implementations, UNIX domain datagram sockets are always reliable and don&#8217;t reorder datagrams); and (since Linux 2.6.4) <code>SOCK_SEQPACKET</code>, for a sequenced-packet socket that is connection-oriented, preserves message boundaries, and delivers messages in the order that they were sent. </p>
<p>UNIX domain sockets support passing file descriptors or process credentials to other processes using ancillary data.  </p>
<h3>Address format</h3>
<p> A UNIX domain socket address is represented in the following structure: </p>
<p>struct sockaddr_un { <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sa_family_t sun_family;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;AF_UNIX&nbsp;*/ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sun_path[108];&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Pathname&nbsp;*/ }; </p>
<p>The <i>sun_family</i> field always contains <code>AF_UNIX</code>. On Linux, <i>sun_path</i> is 108 bytes in size; see also NOTES, below. </p>
<p>Various systems calls (for example, <code><a href="/docs/linux/man/2-bind/">bind</a></code>(2), <code><a href="/docs/linux/man/2-connect/">connect</a></code>(2), and <code><a href="/docs/linux/man/2-sendto/">sendto</a></code>(2)) take a <i>sockaddr_un</i> argument as input. Some other system calls (for example, <code><a href="/docs/linux/man/2-getsockname/">getsockname</a></code>(2), <code><a href="/docs/linux/man/2-getpeername/">getpeername</a></code>(2), <code><a href="/docs/linux/man/2-recvfrom/">recvfrom</a></code>(2), and <code><a href="/docs/linux/man/2-accept/">accept</a></code>(2)) return an argument of this type. </p>
<p>Three types of address are distinguished in the <i>sockaddr_un</i> structure: </p>
<dl>
<dt>*</dt>
<dd> <p> <i>pathname</i>: a UNIX domain socket can be bound to a null-terminated filesystem pathname using <code><a href="/docs/linux/man/2-bind/">bind</a></code>(2). When the address of a pathname socket is returned (by one of the system calls noted above), its length is </p>
 </dd>
<dd> <p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;offsetof(struct sockaddr_un, sun_path)&nbsp;+&nbsp;strlen(sun_path)&nbsp;+&nbsp;1 </p>
 </dd>
<dd> <p> and <i>sun_path</i> contains the null-terminated pathname. (On Linux, the above <code>offsetof</code>() expression equates to the same value as <i>sizeof(sa_family_t)</i>, but some other implementations include other fields before <i>sun_path</i>, so the <code>offsetof</code>() expression more portably describes the size of the address structure.) </p>
 </dd>
<dd> <p> For further details of pathname sockets, see below. </p>
 </dd>
<dt>*</dt>
<dd> <p> <i>unnamed</i>: A stream socket that has not been bound to a pathname using <code><a href="/docs/linux/man/2-bind/">bind</a></code>(2) has no name. Likewise, the two sockets created by <code><a href="/docs/linux/man/2-socketpair/">socketpair</a></code>(2) are unnamed. When the address of an unnamed socket is returned, its length is <i>sizeof(sa_family_t)</i>, and <i>sun_path</i> should not be inspected. </p>
 </dd>
<dt>*</dt>
<dd> <p> <i>abstract</i>: an abstract socket address is distinguished (from a pathname socket) by the fact that <i>sun_path[0]</i> is a null byte (&#8216;\0&#8217;). The socket&#8217;s address in this namespace is given by the additional bytes in <i>sun_path</i> that are covered by the specified length of the address structure. (Null bytes in the name have no special significance.) The name has no connection with filesystem pathnames. When the address of an abstract socket is returned, the returned <i>addrlen</i> is greater than <i>sizeof(sa_family_t)</i> (i.e., greater than 2), and the name of the socket is contained in the first <i>(addrlen - sizeof(sa_family_t))</i> bytes of <i>sun_path</i>. </p>
 </dd></dl>
<h3>Pathname sockets</h3>
<p> When binding a socket to a pathname, a few rules should be observed for maximum portability and ease of coding: </p>
<dl>
<dt>*</dt>
<dd> <p> The pathname in <i>sun_path</i> should be null-terminated. </p>
 </dd>
<dt>*</dt>
<dd> <p> The length of the pathname, including the terminating null byte, should not exceed the size of <i>sun_path</i>. </p>
 </dd>
<dt>*</dt>
<dd> <p> The <i>addrlen</i> argument that describes the enclosing <i>sockaddr_un</i> structure should have a value of at least: </p>
 </dd>
<dd> <pre><code>    offsetof(struct sockaddr_un, sun_path)+strlen(addr.sun_path)+1
</code></pre>
 </dd>
<dd> <p> or, more simply, <i>addrlen</i> can be specified as <i>sizeof(struct sockaddr_un)</i>. </p>
 </dd></dl>
<p>There is some variation in how implementations handle UNIX domain socket addresses that do not follow the above rules. For example, some (but not all) implementations append a null terminator if none is present in the supplied <i>sun_path</i>. </p>
<p>When coding portable applications, keep in mind that some implementations have <i>sun_path</i> as short as 92 bytes. </p>
<p>Various system calls (<code><a href="/docs/linux/man/2-accept/">accept</a></code>(2), <code><a href="/docs/linux/man/2-recvfrom/">recvfrom</a></code>(2), <code><a href="/docs/linux/man/2-getsockname/">getsockname</a></code>(2), <code><a href="/docs/linux/man/2-getpeername/">getpeername</a></code>(2)) return socket address structures. When applied to UNIX domain sockets, the value-result <i>addrlen</i> argument supplied to the call should be initialized as above. Upon return, the argument is set to indicate the <i>actual</i> size of the address structure. The caller should check the value returned in this argument: if the output value exceeds the input value, then there is no guarantee that a null terminator is present in <i>sun_path</i>. (See BUGS.)  </p>
<h3>Pathname socket ownership and permissions</h3>
<p> In the Linux implementation, pathname sockets honor the permissions of the directory they are in. Creation of a new socket fails if the process does not have write and search (execute) permission on the directory in which the socket is created. </p>
<p>On Linux, connecting to a stream socket object requires write permission on that socket; sending a datagram to a datagram socket likewise requires write permission on that socket. POSIX does not make any statement about the effect of the permissions on a socket file, and on some systems (e.g., older BSDs), the socket permissions are ignored. Portable programs should not rely on this feature for security. </p>
<p>When creating a new socket, the owner and group of the socket file are set according to the usual rules. The socket file has all permissions enabled, other than those that are turned off by the process <code><a href="/docs/linux/man/2-umask/">umask</a></code>(2). </p>
<p>The owner, group, and permissions of a pathname socket can be changed (using <code><a href="/docs/linux/man/2-chown/">chown</a></code>(2) and <code><a href="/docs/linux/man/2-chmod/">chmod</a></code>(2)).  </p>
<h3>Abstract sockets</h3>
<p> Socket permissions have no meaning for abstract sockets: the process <code><a href="/docs/linux/man/2-umask/">umask</a></code>(2) has no effect when binding an abstract socket, and changing the ownership and permissions of the object (via <code><a href="/docs/linux/man/2-fchown/">fchown</a></code>(2) and <code><a href="/docs/linux/man/2-fchmod/">fchmod</a></code>(2)) has no effect on the accessibility of the socket. </p>
<p>Abstract sockets automatically disappear when all open references to the socket are closed. </p>
<p>The abstract socket namespace is a nonportable Linux extension.  </p>
<h3>Socket options</h3>
<p> For historical reasons, these socket options are specified with a <code>SOL_SOCKET</code> type even though they are <code>AF_UNIX</code> specific. They can be set with <code><a href="/docs/linux/man/2-setsockopt/">setsockopt</a></code>(2) and read with <code><a href="/docs/linux/man/2-getsockopt/">getsockopt</a></code>(2) by specifying <code>SOL_SOCKET</code> as the socket family. </p>
<dl>
<dt><code>SO_PASSCRED</code></dt>
<dd> <p> Enabling this socket option causes receipt of the credentials of the sending process in an <code>SCM_CREDENTIALS ancillary</code> message in each subsequently received message. The returned credentials are those specified by the sender using <code>SCM_CREDENTIALS</code>, or a default that includes the sender&#8217;s PID, real user ID, and real group ID, if the sender did not specify <code>SCM_CREDENTIALS</code> ancillary data. </p>
 </dd>
<dd> <p> When this option is set and the socket is not yet connected, a unique name in the abstract namespace will be generated automatically. </p>
 </dd>
<dd> <p> The value given as an argument to <code><a href="/docs/linux/man/2-setsockopt/">setsockopt</a></code>(2) and returned as the result of <code><a href="/docs/linux/man/2-getsockopt/">getsockopt</a></code>(2) is an integer boolean flag. </p>
 </dd>
<dt><code>SO_PASSSEC</code></dt>
<dd> <p> Enables receiving of the SELinux security label of the peer socket in an ancillary message of type <code>SCM_SECURITY</code> (see below). </p>
 </dd>
<dd> <p> The value given as an argument to <code><a href="/docs/linux/man/2-setsockopt/">setsockopt</a></code>(2) and returned as the result of <code><a href="/docs/linux/man/2-getsockopt/">getsockopt</a></code>(2) is an integer boolean flag. </p>
 </dd>
<dd> <p> The <code>SO_PASSSEC</code> option is supported for UNIX domain datagram sockets since Linux 2.6.18; support for UNIX domain stream sockets was added in Linux 4.2. </p>
 </dd>
<dt><code>SO_PEEK_OFF</code></dt>
<dd> <p> See <code><a href="/docs/linux/man/7-socket/">socket</a></code>(7). </p>
 </dd>
<dt><code>SO_PEERCRED</code></dt>
<dd> <p> This read-only socket option returns the credentials of the peer process connected to this socket. The returned credentials are those that were in effect at the time of the call to <code><a href="/docs/linux/man/2-connect/">connect</a></code>(2) or <code><a href="/docs/linux/man/2-socketpair/">socketpair</a></code>(2). </p>
 </dd>
<dd> <p> The argument to <code><a href="/docs/linux/man/2-getsockopt/">getsockopt</a></code>(2) is a pointer to a <i>ucred</i> structure; define the <code>_GNU_SOURCE</code> feature test macro to obtain the definition of that structure from <i>&lt;sys/socket.h&gt;</i>. </p>
 </dd>
<dd> <p> The use of this option is possible only for connected <code>AF_UNIX</code> stream sockets and for <code>AF_UNIX</code> stream and datagram socket pairs created using <code><a href="/docs/linux/man/2-socketpair/">socketpair</a></code>(2). </p>
 </dd>
<dt><code>SO_PEERSEC</code></dt>
<dd> <p> This read-only socket option returns the security context of the peer socket connected to this socket. By default, this will be the same as the security context of the process that created the peer socket unless overridden by the policy or by a process with the required permissions. </p>
 </dd>
<dd> <p> The argument to <code><a href="/docs/linux/man/2-getsockopt/">getsockopt</a></code>(2) is a pointer to a buffer of the specified length in bytes into which the security context string will be copied. If the buffer length is less than the length of the security context string, then <code><a href="/docs/linux/man/2-getsockopt/">getsockopt</a></code>(2) returns -1, sets <i>errno</i> to <code>ERANGE</code>, and returns the required length via <i>optlen</i>. The caller should allocate at least <code>NAME_MAX</code> bytes for the buffer initially, although this is not guaranteed to be sufficient. Resizing the buffer to the returned length and retrying may be necessary. </p>
 </dd>
<dd> <p> The security context string may include a terminating null character in the returned length, but is not guaranteed to do so: a security context &quot;foo&quot; might be represented as either {&#8216;f&#8217;,&#8216;o&#8217;,&#8216;o&#8217;} of length 3 or {&#8216;f&#8217;,&#8216;o&#8217;,&#8216;o&#8217;,&#8216;\0&#8217;} of length 4, which are considered to be interchangeable. The string is printable, does not contain non-terminating null characters, and is in an unspecified encoding (in particular, it is not guaranteed to be ASCII or UTF-8). </p>
 </dd>
<dd> <p> The use of this option for sockets in the <code>AF_UNIX</code> address family is supported since Linux 2.6.2 for connected stream sockets, and since Linux 4.18 also for stream and datagram socket pairs created using <code><a href="/docs/linux/man/2-socketpair/">socketpair</a></code>(2). </p>
 </dd></dl>
<h3>Autobind feature</h3>
<p> If a <code><a href="/docs/linux/man/2-bind/">bind</a></code>(2) call specifies <i>addrlen</i> as <i>sizeof(sa_family_t)</i>, or the <code>SO_PASSCRED</code> socket option was specified for a socket that was not explicitly bound to an address, then the socket is autobound to an abstract address. The address consists of a null byte followed by 5 bytes in the character set <i>[0-9a-f]</i>. Thus, there is a limit of 2^20 autobind addresses. (From Linux 2.1.15, when the autobind feature was added, 8 bytes were used, and the limit was thus 2^32 autobind addresses. The change to 5 bytes came in Linux 2.3.15.)  </p>
<h3>Sockets API</h3>
<p> The following paragraphs describe domain-specific details and unsupported features of the sockets API for UNIX domain sockets on Linux. </p>
<p>UNIX domain sockets do not support the transmission of out-of-band data (the <code>MSG_OOB</code> flag for <code><a href="/docs/linux/man/2-send/">send</a></code>(2) and <code><a href="/docs/linux/man/2-recv/">recv</a></code>(2)). </p>
<p>The <code><a href="/docs/linux/man/2-send/">send</a></code>(2) <code>MSG_MORE</code> flag is not supported by UNIX domain sockets. </p>
<p>Before Linux 3.4, the use of <code>MSG_TRUNC</code> in the <i>flags</i> argument of <code><a href="/docs/linux/man/2-recv/">recv</a></code>(2) was not supported by UNIX domain sockets. </p>
<p>The <code>SO_SNDBUF</code> socket option does have an effect for UNIX domain sockets, but the <code>SO_RCVBUF</code> option does not. For datagram sockets, the <code>SO_SNDBUF</code> value imposes an upper limit on the size of outgoing datagrams. This limit is calculated as the doubled (see <code><a href="/docs/linux/man/7-socket/">socket</a></code>(7)) option value less 32 bytes used for overhead.  </p>
<h3>Ancillary messages</h3>
<p> Ancillary data is sent and received using <code><a href="/docs/linux/man/2-sendmsg/">sendmsg</a></code>(2) and <code><a href="/docs/linux/man/2-recvmsg/">recvmsg</a></code>(2). For historical reasons, the ancillary message types listed below are specified with a <code>SOL_SOCKET</code> type even though they are <code>AF_UNIX</code> specific. To send them, set the <i>cmsg_level</i> field of the struct <i>cmsghdr</i> to <code>SOL_SOCKET</code> and the <i>cmsg_type</i> field to the type. For more information, see <code><a href="/docs/linux/man/3-cmsg/">cmsg</a></code>(3). </p>
<dl>
<dt><code>SCM_RIGHTS</code></dt>
<dd> <p> Send or receive a set of open file descriptors from another process. The data portion contains an integer array of the file descriptors. </p>
 </dd>
<dd> <p> Commonly, this operation is referred to as &quot;passing a file descriptor&quot; to another process. However, more accurately, what is being passed is a reference to an open file description (see <code><a href="/docs/linux/man/2-open/">open</a></code>(2)), and in the receiving process it is likely that a different file descriptor number will be used. Semantically, this operation is equivalent to duplicating (<code><a href="/docs/linux/man/2-dup/">dup</a></code>(2)) a file descriptor into the file descriptor table of another process. </p>
 </dd>
<dd> <p> If the buffer used to receive the ancillary data containing file descriptors is too small (or is absent), then the ancillary data is truncated (or discarded) and the excess file descriptors are automatically closed in the receiving process. </p>
 </dd>
<dd> <p> If the number of file descriptors received in the ancillary data would cause the process to exceed its <code>RLIMIT_NOFILE</code> resource limit (see <code><a href="/docs/linux/man/2-getrlimit/">getrlimit</a></code>(2)), the excess file descriptors are automatically closed in the receiving process. </p>
 </dd>
<dd> <p> The kernel constant <code>SCM_MAX_FD</code> defines a limit on the number of file descriptors in the array. Attempting to send an array larger than this limit causes <code><a href="/docs/linux/man/2-sendmsg/">sendmsg</a></code>(2) to fail with the error <code>EINVAL</code>. <code>SCM_MAX_FD</code> has the value 253 (or 255 in kernels before 2.6.38). </p>
 </dd>
<dt><code>SCM_CREDENTIALS</code></dt>
<dd> <p> Send or receive UNIX credentials. This can be used for authentication. The credentials are passed as a <i>struct ucred</i> ancillary message. This structure is defined in <i>&lt;sys/socket.h&gt;</i> as follows: </p>
 </dd>
<dd> <p> struct ucred { <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pid_t pid;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Process ID of the sending process&nbsp;*/ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uid_t uid;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;User ID of the sending process&nbsp;*/ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gid_t gid;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Group ID of the sending process&nbsp;*/ }; </p>
 </dd>
<dd> <p> Since glibc 2.8, the <code>_GNU_SOURCE</code> feature test macro must be defined (before including <i>any</i> header files) in order to obtain the definition of this structure. </p>
 </dd>
<dd> <p> The credentials which the sender specifies are checked by the kernel. A privileged process is allowed to specify values that do not match its own. The sender must specify its own process ID (unless it has the capability <code>CAP_SYS_ADMIN</code>, in which case the PID of any existing process may be specified), its real user ID, effective user ID, or saved set-user-ID (unless it has <code>CAP_SETUID</code>), and its real group ID, effective group ID, or saved set-group-ID (unless it has <code>CAP_SETGID</code>). </p>
 </dd>
<dd> <p> To receive a <i>struct ucred</i> message, the <code>SO_PASSCRED</code> option must be enabled on the socket. </p>
 </dd>
<dt><code>SCM_SECURITY</code></dt>
<dd> <p> Receive the SELinux security context (the security label) of the peer socket. The received ancillary data is a null-terminated string containing the security context. The receiver should allocate at least <code>NAME_MAX</code> bytes in the data portion of the ancillary message for this data. </p>
 </dd>
<dd> <p> To receive the security context, the <code>SO_PASSSEC</code> option must be enabled on the socket (see above). </p>
 </dd></dl>
<p>When sending ancillary data with <code><a href="/docs/linux/man/2-sendmsg/">sendmsg</a></code>(2), only one item of each of the above types may be included in the sent message. </p>
<p>At least one byte of real data should be sent when sending ancillary data. On Linux, this is required to successfully send ancillary data over a UNIX domain stream socket. When sending ancillary data over a UNIX domain datagram socket, it is not necessary on Linux to send any accompanying real data. However, portable applications should also include at least one byte of real data when sending ancillary data over a datagram socket. </p>
<p>When receiving from a stream socket, ancillary data forms a kind of barrier for the received data. For example, suppose that the sender transmits as follows: </p>
<dl>
<dd>  </dd>
<dl>
<dt>1.</dt>
<dd> <p> <code><a href="/docs/linux/man/2-sendmsg/">sendmsg</a></code>(2) of four bytes, with no ancillary data. </p>
 </dd>
<dt>2.</dt>
<dd> <p> <code><a href="/docs/linux/man/2-sendmsg/">sendmsg</a></code>(2) of one byte, with ancillary data. </p>
 </dd>
<dt>3.</dt>
<dd> <p> <code><a href="/docs/linux/man/2-sendmsg/">sendmsg</a></code>(2) of four bytes, with no ancillary data. </p>
 </dd></dl>
</dl>
<p>Suppose that the receiver now performs <code><a href="/docs/linux/man/2-recvmsg/">recvmsg</a></code>(2) calls each with a buffer size of 20 bytes. The first call will receive five bytes of data, along with the ancillary data sent by the second <code><a href="/docs/linux/man/2-sendmsg/">sendmsg</a></code>(2) call. The next call will receive the remaining four bytes of data. </p>
<p>If the space allocated for receiving incoming ancillary data is too small then the ancillary data is truncated to the number of headers that will fit in the supplied buffer (or, in the case of an <code>SCM_RIGHTS</code> file descriptor list, the list of file descriptors may be truncated). If no buffer is provided for incoming ancillary data (i.e., the <i>msg_control</i> field of the <i>msghdr</i> structure supplied to <code><a href="/docs/linux/man/2-recvmsg/">recvmsg</a></code>(2) is NULL), then the incoming ancillary data is discarded. In both of these cases, the <code>MSG_CTRUNC</code> flag will be set in the <i>msg.msg_flags</i> value returned by <code><a href="/docs/linux/man/2-recvmsg/">recvmsg</a></code>(2).  </p>
<h3>Ioctls</h3>
<p> The following <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) calls return information in <i>value</i>. The correct syntax is: </p>
<dl>
<dd> <pre><code>
 int   value; 
 error   = ioctl(  unix_socket  ,  ioctl_type  , &amp;  value  ); 
</code></pre>
 </dd></dl>
<p> <i>ioctl_type</i> can be: </p>
<dl>
<dt><code>SIOCINQ</code></dt>
<dd> <p> For <code>SOCK_STREAM</code> sockets, this call returns the number of unread bytes in the receive buffer. The socket must not be in LISTEN state, otherwise an error (<code>EINVAL</code>) is returned. <code>SIOCINQ</code> is defined in <i>&lt;linux/sockios.h&gt;</i>. Alternatively, you can use the synonymous <code>FIONREAD</code>, defined in <i>&lt;sys/ioctl.h&gt;</i>. For <code>SOCK_DGRAM</code> sockets, the returned value is the same as for Internet domain datagram sockets; see <code><a href="/docs/linux/man/7-udp/">udp</a></code>(7). </p>
 </dd></dl>
<h2>ERRORS</h2>
<dl>
<dt><code>EADDRINUSE</code></dt>
<dd> <p> The specified local address is already in use or the filesystem socket object already exists. </p>
 </dd>
<dt><code>EBADF</code></dt>
<dd> <p> This error can occur for <code><a href="/docs/linux/man/2-sendmsg/">sendmsg</a></code>(2) when sending a file descriptor as ancillary data over a UNIX domain socket (see the description of <code>SCM_RIGHTS</code>, above), and indicates that the file descriptor number that is being sent is not valid (e.g., it is not an open file descriptor). </p>
 </dd>
<dt><code>ECONNREFUSED</code></dt>
<dd> <p> The remote address specified by <code><a href="/docs/linux/man/2-connect/">connect</a></code>(2) was not a listening socket. This error can also occur if the target pathname is not a socket. </p>
 </dd>
<dt><code>ECONNRESET</code></dt>
<dd> <p> Remote socket was unexpectedly closed. </p>
 </dd>
<dt><code>EFAULT</code></dt>
<dd> <p> User memory address was not valid. </p>
 </dd>
<dt><code>EINVAL</code></dt>
<dd> <p> Invalid argument passed. A common cause is that the value <code>AF_UNIX</code> was not specified in the <i>sun_type</i> field of passed addresses, or the socket was in an invalid state for the applied operation. </p>
 </dd>
<dt><code>EISCONN</code></dt>
<dd> <p> <code><a href="/docs/linux/man/2-connect/">connect</a></code>(2) called on an already connected socket or a target address was specified on a connected socket. </p>
 </dd>
<dt><code>ENOENT</code></dt>
<dd> <p> The pathname in the remote address specified to <code><a href="/docs/linux/man/2-connect/">connect</a></code>(2) did not exist. </p>
 </dd>
<dt><code>ENOMEM</code></dt>
<dd> <p> Out of memory. </p>
 </dd>
<dt><code>ENOTCONN</code></dt>
<dd> <p> Socket operation needs a target address, but the socket is not connected. </p>
 </dd>
<dt><code>EOPNOTSUPP</code></dt>
<dd> <p> Stream operation called on non-stream oriented socket or tried to use the out-of-band data option. </p>
 </dd>
<dt><code>EPERM</code></dt>
<dd> <p> The sender passed invalid credentials in the <i>struct ucred</i>. </p>
 </dd>
<dt><code>EPIPE</code></dt>
<dd> <p> Remote socket was closed on a stream socket. If enabled, a <code>SIGPIPE</code> is sent as well. This can be avoided by passing the <code>MSG_NOSIGNAL</code> flag to <code><a href="/docs/linux/man/2-send/">send</a></code>(2) or <code><a href="/docs/linux/man/2-sendmsg/">sendmsg</a></code>(2). </p>
 </dd>
<dt><code>EPROTONOSUPPORT</code></dt>
<dd> <p> Passed protocol is not <code>AF_UNIX</code>. </p>
 </dd>
<dt><code>EPROTOTYPE</code></dt>
<dd> <p> Remote socket does not match the local socket type (<code>SOCK_DGRAM</code> versus <code>SOCK_STREAM</code>). </p>
 </dd>
<dt><code>ESOCKTNOSUPPORT</code></dt>
<dd> <p> Unknown socket type. </p>
 </dd>
<dt><code>ESRCH</code></dt>
<dd> <p> While sending an ancillary message containing credentials (<code>SCM_CREDENTIALS</code>), the caller specified a PID that does not match any existing process. </p>
 </dd>
<dt><code>ETOOMANYREFS</code></dt>
<dd> <p> This error can occur for <code><a href="/docs/linux/man/2-sendmsg/">sendmsg</a></code>(2) when sending a file descriptor as ancillary data over a UNIX domain socket (see the description of <code>SCM_RIGHTS</code>, above). It occurs if the number of &quot;in-flight&quot; file descriptors exceeds the <code>RLIMIT_NOFILE</code> resource limit and the caller does not have the <code>CAP_SYS_RESOURCE</code> capability. An in-flight file descriptor is one that has been sent using <code><a href="/docs/linux/man/2-sendmsg/">sendmsg</a></code>(2) but has not yet been accepted in the recipient process using <code><a href="/docs/linux/man/2-recvmsg/">recvmsg</a></code>(2). </p>
 </dd>
<dd> <p> This error is diagnosed since mainline Linux 4.5 (and in some earlier kernel versions where the fix has been backported). In earlier kernel versions, it was possible to place an unlimited number of file descriptors in flight, by sending each file descriptor with <code><a href="/docs/linux/man/2-sendmsg/">sendmsg</a></code>(2) and then closing the file descriptor so that it was not accounted against the <code>RLIMIT_NOFILE</code> resource limit. </p>
 </dd></dl>
<p>Other errors can be generated by the generic socket layer or by the filesystem while generating a filesystem socket object. See the appropriate manual pages for more information.  </p>
<h2>VERSIONS</h2>
<p> <code>SCM_CREDENTIALS</code> and the abstract namespace were introduced with Linux 2.2 and should not be used in portable programs. (Some BSD-derived systems also support credential passing, but the implementation details differ.)  </p>
<h2>NOTES</h2>
<p> Binding to a socket with a filename creates a socket in the filesystem that must be deleted by the caller when it is no longer needed (using <code><a href="/docs/linux/man/2-unlink/">unlink</a></code>(2)). The usual UNIX close-behind semantics apply; the socket can be unlinked at any time and will be finally removed from the filesystem when the last reference to it is closed. </p>
<p>To pass file descriptors or credentials over a <code>SOCK_STREAM</code> socket, you must to send or receive at least one byte of nonancillary data in the same <code><a href="/docs/linux/man/2-sendmsg/">sendmsg</a></code>(2) or <code><a href="/docs/linux/man/2-recvmsg/">recvmsg</a></code>(2) call. </p>
<p>UNIX domain stream sockets do not support the notion of out-of-band data.  </p>
<h2>BUGS</h2>
<p> When binding a socket to an address, Linux is one of the implementations that appends a null terminator if none is supplied in <i>sun_path</i>. In most cases this is unproblematic: when the socket address is retrieved, it will be one byte longer than that supplied when the socket was bound. However, there is one case where confusing behavior can result: if 108 non-null bytes are supplied when a socket is bound, then the addition of the null terminator takes the length of the pathname beyond <i>sizeof(sun_path)</i>. Consequently, when retrieving the socket address (for example, via <code><a href="/docs/linux/man/2-accept/">accept</a></code>(2)), if the input <i>addrlen</i> argument for the retrieving call is specified as <i>sizeof(struct sockaddr_un)</i>, then the returned address structure <i>won&#8217;t</i> have a null terminator in <i>sun_path</i>. </p>
<p>In addition, some implementations don&#8217;t require a null terminator when binding a socket (the <i>addrlen</i> argument is used to determine the length of <i>sun_path</i>) and when the socket address is retrieved on these implementations, there is no null terminator in <i>sun_path</i>. </p>
<p>Applications that retrieve socket addresses can (portably) code to handle the possibility that there is no null terminator in <i>sun_path</i> by respecting the fact that the number of valid bytes in the pathname is: </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;strnlen(addr.sun_path, addrlen - offsetof(sockaddr_un, sun_path)) </p>
<p>Alternatively, an application can retrieve the socket address by allocating a buffer of size <i>sizeof(struct sockaddr_un)+1</i> that is zeroed out before the retrieval. The retrieving call can specify <i>addrlen</i> as <i>sizeof(struct sockaddr_un)</i>, and the extra zero byte ensures that there will be a null terminator for the string returned in <i>sun_path</i>: </p>
<p>void *addrp; </p>
<p>addrlen = sizeof(struct sockaddr_un); addrp = malloc(addrlen + 1); if (addrp == NULL) <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Handle error&nbsp;*/&nbsp;; memset(addrp, 0, addrlen + 1); </p>
<p>if (getsockname(sfd, (struct sockaddr *) addrp, &amp;addrlen)) == -1) <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;handle error&nbsp;*/&nbsp;; </p>
<p>printf(&quot;sun_path = %s\n&quot;, ((struct sockaddr_un *) addrp)-&gt;sun_path); </p>
<p>This sort of messiness can be avoided if it is guaranteed that the applications that <i>create</i> pathname sockets follow the rules outlined above under <i>Pathname sockets</i>.  </p>
<h2>EXAMPLES</h2>
<p> The following code demonstrates the use of sequenced-packet sockets for local interprocess communication. It consists of two programs. The server program waits for a connection from the client program. The client sends each of its command-line arguments in separate messages. The server treats the incoming messages as integers and adds them up. The client sends the command string &quot;END&quot;. The server sends back a message containing the sum of the client&#8217;s integers. The client prints the sum and exits. The server waits for the next client to connect. To stop the server, the client is called with the command-line argument &quot;DOWN&quot;. </p>
<p>The following output was recorded while running the server in the background and repeatedly executing the client. Execution of the server program ends when it receives the &quot;DOWN&quot; command.  </p>
<h3>Example output</h3>
<p> $ <code>./server &amp;</code> [1] 25887 $ <code>./client 3 4</code> Result = 7 $ <code>./client 11 -5</code> Result = 6 $ <code>./client DOWN</code> Result = 0 [1]+ Done ./server $  </p>
<h3>Program source</h3>
<p> /* <br />
&nbsp;*&nbsp;File connection.h <br />
&nbsp;*/ </p>
<p>#define SOCKET_NAME &quot;/tmp/9Lq7BNBnBycd6nxy.socket&quot; #define BUFFER_SIZE 12 </p>
<p>/* <br />
&nbsp;*&nbsp;File server.c <br />
&nbsp;*/ </p>
<p>#include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; #include &lt;string.h&gt; #include &lt;sys/socket.h&gt; #include &lt;sys/un.h&gt; #include &lt;unistd.h&gt; #include &quot;connection.h&quot; </p>
<p>int main(int argc, char *argv[]) { <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct sockaddr_un name; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int down_flag&nbsp;=&nbsp;0; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int ret; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int connection_socket; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int data_socket; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int result; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char buffer[BUFFER_SIZE]; </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Create local socket.&nbsp;*/ </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;connection_socket&nbsp;=&nbsp;socket(AF_UNIX, SOCK_SEQPACKET, 0); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(connection_socket&nbsp;==&nbsp;-1)&nbsp;{ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;socket&quot;); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/* <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*&nbsp;For portability clear the whole structure, since some <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*&nbsp;implementations have additional&nbsp;(nonstandard)&nbsp;fields in <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*&nbsp;the structure. <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*/ </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;memset(&amp;name, 0, sizeof(name)); </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Bind socket to socket name.&nbsp;*/ </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;name.sun_family&nbsp;=&nbsp;AF_UNIX; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;strncpy(name.sun_path, SOCKET_NAME, sizeof(name.sun_path)&nbsp;- 1); </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ret&nbsp;=&nbsp;bind(connection_socket,&nbsp;(const struct sockaddr&nbsp;*)&nbsp;&amp;name, <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sizeof(name)); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(ret&nbsp;==&nbsp;-1)&nbsp;{ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;bind&quot;); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/* <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*&nbsp;Prepare for accepting connections. The backlog size is set <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*&nbsp;to 20. So while one request is being processed other requests <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*&nbsp;can be waiting. <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*/ </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ret&nbsp;=&nbsp;listen(connection_socket, 20); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(ret&nbsp;==&nbsp;-1)&nbsp;{ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;listen&quot;); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;This is the main loop for handling connections.&nbsp;*/ </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for&nbsp;(;;)&nbsp;{ </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Wait for incoming connection.&nbsp;*/ </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;data_socket&nbsp;=&nbsp;accept(connection_socket, NULL, NULL); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(data_socket&nbsp;==&nbsp;-1)&nbsp;{ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;accept&quot;); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;result&nbsp;=&nbsp;0; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for&nbsp;(;;)&nbsp;{ </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Wait for next data packet.&nbsp;*/ </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ret&nbsp;=&nbsp;read(data_socket, buffer, sizeof(buffer)); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(ret&nbsp;==&nbsp;-1)&nbsp;{ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;read&quot;); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Ensure buffer is 0-terminated.&nbsp;*/ </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;buffer[sizeof(buffer)&nbsp;- 1]&nbsp;=&nbsp;0; </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Handle commands.&nbsp;*/ </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(!strncmp(buffer,&nbsp;&quot;DOWN&quot;, sizeof(buffer)))&nbsp;{ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;down_flag&nbsp;=&nbsp;1; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;break; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(!strncmp(buffer,&nbsp;&quot;END&quot;, sizeof(buffer)))&nbsp;{ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;break; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Add received summand.&nbsp;*/ </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;result&nbsp;+=&nbsp;atoi(buffer); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Send result.&nbsp;*/ </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sprintf(buffer,&nbsp;&quot;%d&quot;, result); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ret&nbsp;=&nbsp;write(data_socket, buffer, sizeof(buffer)); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(ret&nbsp;==&nbsp;-1)&nbsp;{ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;write&quot;); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Close socket.&nbsp;*/ </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;close(data_socket); </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Quit on DOWN command.&nbsp;*/ </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(down_flag)&nbsp;{ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;break; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;close(connection_socket); </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Unlink the socket.&nbsp;*/ </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unlink(SOCKET_NAME); </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); } </p>
<p>/* <br />
&nbsp;*&nbsp;File client.c <br />
&nbsp;*/ </p>
<p>#include &lt;errno.h&gt; #include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; #include &lt;string.h&gt; #include &lt;sys/socket.h&gt; #include &lt;sys/un.h&gt; #include &lt;unistd.h&gt; #include &quot;connection.h&quot; </p>
<p>int main(int argc, char *argv[]) { <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct sockaddr_un addr; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int ret; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int data_socket; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char buffer[BUFFER_SIZE]; </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Create local socket.&nbsp;*/ </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;data_socket&nbsp;=&nbsp;socket(AF_UNIX, SOCK_SEQPACKET, 0); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(data_socket&nbsp;==&nbsp;-1)&nbsp;{ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;socket&quot;); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/* <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*&nbsp;For portability clear the whole structure, since some <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*&nbsp;implementations have additional&nbsp;(nonstandard)&nbsp;fields in <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*&nbsp;the structure. <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*/ </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;memset(&amp;addr, 0, sizeof(addr)); </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Connect socket to socket address&nbsp;*/ </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;addr.sun_family&nbsp;=&nbsp;AF_UNIX; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;strncpy(addr.sun_path, SOCKET_NAME, sizeof(addr.sun_path)&nbsp;- 1); </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ret&nbsp;=&nbsp;connect(data_socket,&nbsp;(const struct sockaddr&nbsp;*)&nbsp;&amp;addr, <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sizeof(addr)); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(ret&nbsp;==&nbsp;-1)&nbsp;{ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;The server is down.\n&quot;); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Send arguments.&nbsp;*/ </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for&nbsp;(int i&nbsp;=&nbsp;1;&nbsp;i&nbsp;&lt;&nbsp;argc;&nbsp;++i)&nbsp;{ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ret&nbsp;=&nbsp;write(data_socket, argv[i], strlen(argv[i])&nbsp;+&nbsp;1); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(ret&nbsp;==&nbsp;-1)&nbsp;{ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;write&quot;); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;break; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Request result.&nbsp;*/ </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;strcpy(buffer,&nbsp;&quot;END&quot;); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ret&nbsp;=&nbsp;write(data_socket, buffer, strlen(buffer)&nbsp;+&nbsp;1); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(ret&nbsp;==&nbsp;-1)&nbsp;{ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;write&quot;); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Receive result.&nbsp;*/ </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ret&nbsp;=&nbsp;read(data_socket, buffer, sizeof(buffer)); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(ret&nbsp;==&nbsp;-1)&nbsp;{ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;read&quot;); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Ensure buffer is 0-terminated.&nbsp;*/ </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;buffer[sizeof(buffer)&nbsp;- 1]&nbsp;=&nbsp;0; </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Result&nbsp;=&nbsp;%s\n&quot;, buffer); </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Close socket.&nbsp;*/ </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;close(data_socket); </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); } </p>
<p>For an example of the use of <code>SCM_RIGHTS</code> see <code><a href="/docs/linux/man/3-cmsg/">cmsg</a></code>(3).  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-recvmsg/">recvmsg</a></code>(2), <code><a href="/docs/linux/man/2-sendmsg/">sendmsg</a></code>(2), <code><a href="/docs/linux/man/2-socket/">socket</a></code>(2), <code><a href="/docs/linux/man/2-socketpair/">socketpair</a></code>(2), <code><a href="/docs/linux/man/3-cmsg/">cmsg</a></code>(3), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7), <code><a href="/docs/linux/man/7-credentials/">credentials</a></code>(7), <code><a href="/docs/linux/man/7-socket/">socket</a></code>(7), <code><a href="/docs/linux/man/7-udp/">udp</a></code>(7)  </p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
