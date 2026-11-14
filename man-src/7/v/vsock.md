---
title: "vsock(7)"
name: "vsock"
section: "7"
letter: "v"
url: "/docs/linux/man/7-vsock/"
description: "vsock – Linux VSOCK address family"
---

<p>vsock &#8211; Linux VSOCK address family</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;sys/socket.h&gt;


#include &lt;linux/vm_sockets.h&gt;
stream_socket = socket(AF_VSOCK, SOCK_STREAM, 0);


datagram_socket = socket(AF_VSOCK, SOCK_DGRAM, 0);</code></pre>
<h2>Description</h2>
<p>The VSOCK address family facilitates communication between virtual machines and the host they are running on. This address family is used by guest agents and hypervisor services that need a communications channel that is independent of virtual machine network configuration. Valid socket types are <code>SOCK_STREAM</code> and <code>SOCK_DGRAM</code>. <code>SOCK_STREAM</code> provides connection-oriented byte streams with guaranteed, in-order delivery. <code>SOCK_DGRAM</code> provides a connectionless datagram packet service with best-effort delivery and best-effort ordering. Availability of these socket types is dependent on the underlying hypervisor. A new socket is created with struct sockaddr_vm {<br />
    sa_family_t svm_family; /* Address family: AF_VSOCK */<br />
    unsigned short svm_reserved1;<br />
    unsigned int svm_port; /* Port # in host byte order */<br />
    unsigned int svm_cid;  /* Address in host byte order */<br />
    unsigned char svm_zero[sizeof(struct sockaddr) &#8211;<br />
                           sizeof(sa_family_t) &#8211;<br />
                           sizeof(unsigned short) &#8211;<br />
                           sizeof(unsigned int) &#8211;<br />
                           sizeof(unsigned int)];<br />
}; When a process wants to establish a connection, it calls <code><a href="/docs/linux/man/2-connect/">connect</a></code>(2) with a given destination socket address. The socket is automatically bound to a free port if unbound. A process can listen for incoming connections by first binding to a socket address using <code><a href="/docs/linux/man/2-bind/">bind</a></code>(2) and then calling <code><a href="/docs/linux/man/2-listen/">listen</a></code>(2). Data is transmitted using the <code><a href="/docs/linux/man/2-send/">send</a></code>(2) or <code><a href="/docs/linux/man/2-write/">write</a></code>(2) families of system calls and data is received using the <code><a href="/docs/linux/man/2-recv/">recv</a></code>(2) or <code><a href="/docs/linux/man/2-read/">read</a></code>(2) families of system calls.</p>
<h3>Address format</h3>
<p>A socket address is defined as a combination of a 32-bit Context Identifier (CID) and a 32-bit port number. The CID identifies the source or destination, which is either a virtual machine or the host. The port number differentiates between multiple services running on a single machine. </p>
<pre><code>struct sockaddr_vm {
    sa_family_t svm_family; /* Address family: AF_VSOCK */
    unsigned short svm_reserved1;
    unsigned int svm_port; /* Port # in host byte order */
    unsigned int svm_cid;  /* Address in host byte order */
    unsigned char svm_zero[sizeof(struct sockaddr) -
                           sizeof(sa_family_t) -
                           sizeof(unsigned short) -
                           sizeof(unsigned int) -
                           sizeof(unsigned int)];
};</code></pre>
<p> <i>svm_family</i> is always set to <code>AF_VSOCK</code>. <i>svm_reserved1</i> is always set to 0. <i>svm_port</i> contains the port number in host byte order. The port numbers below 1024 are called <i>privileged ports</i>. Only a process with the <code>CAP_NET_BIND_SERVICE</code> capability may <code><a href="/docs/linux/man/2-bind/">bind</a></code>(2) to these port numbers. <i>svm_zero</i> must be zero-filled. There are several special addresses: <code>VMADDR_CID_ANY</code> (-1U) means any address for binding; <code>VMADDR_CID_HYPERVISOR</code> (0) is reserved for services built into the hypervisor; <code>VMADDR_CID_LOCAL</code> (1) is the well-known address for local communication (loopback); <code>VMADDR_CID_HOST</code> (2) is the well-known address of the host. The special constant <code>VMADDR_PORT_ANY</code> (-1U) means any port number for binding.</p>
<h3>Live migration</h3>
<p>Sockets are affected by live migration of virtual machines. Connected <code>SOCK_STREAM</code> sockets become disconnected when the virtual machine migrates to a new host. Applications must reconnect when this happens. The local CID may change across live migration if the old CID is not available on the new host. Bound sockets are automatically updated to the new CID.</p>
<h3>Ioctls</h3>
<dl>
<dt><code>IOCTL_VM_SOCKETS_GET_LOCAL_CID</code></p>
<dd>Get the CID of the local machine. The argument is a pointer to an <i>unsigned int</i>.</p>
<dd>ioctl(socket, IOCTL_VM_SOCKETS_GET_LOCAL_CID, &amp;cid);</p>
<dd>Consider using <code>VMADDR_CID_ANY</code> when binding instead of getting the local CID with <code>IOCTL_VM_SOCKETS_GET_LOCAL_CID</code>.</dl>
<h3>Local communication</h3>
<p><code>VMADDR_CID_LOCAL</code> (1) directs packets to the same host that generated them. This is useful for testing applications on a single host and for debugging. The local CID obtained with <code>IOCTL_VM_SOCKETS_GET_LOCAL_CID</code> can be used for the same purpose, but it is preferable to use <code>VMADDR_CID_LOCAL .</code></p>
<h2>Errors</h2>
<dl>
<dt><code>EACCES</code></p>
<dd>Unable to bind to a privileged port without the <code>CAP_NET_BIND_SERVICE</code> capability.</p>
<dt><code>EADDRINUSE</code></p>
<dd>Unable to bind to a port that is already in use.</p>
<dt><code>EADDRNOTAVAIL</code></p>
<dd>Unable to find a free port for binding or unable to bind to a nonlocal CID.</p>
<dt><code>EINVAL</code></p>
<dd>Invalid parameters. This includes: attempting to bind a socket that is already bound, providing an invalid struct <i>sockaddr_vm</i>, and other input validation errors.</p>
<dt><code>ENOPROTOOPT</code></p>
<dd>Invalid socket option in <code><a href="/docs/linux/man/2-setsockopt/">setsockopt</a></code>(2) or <code><a href="/docs/linux/man/2-getsockopt/">getsockopt</a></code>(2).</p>
<dt><code>ENOTCONN</code></p>
<dd>Unable to perform operation on an unconnected socket.</p>
<dt><code>EOPNOTSUPP</code></p>
<dd>Operation not supported. This includes: the <code>MSG_OOB</code> flag that is not implemented for the <code><a href="/docs/linux/man/2-send/">send</a></code>(2) family of syscalls and <code>MSG_PEEK</code> for the <code><a href="/docs/linux/man/2-recv/">recv</a></code>(2) family of syscalls.</p>
<dt><code>EPROTONOSUPPORT</code></p>
<dd>Invalid socket protocol number. The protocol should always be 0.</p>
<dt><code>ESOCKTNOSUPPORT</code></p>
<dd>Unsupported socket type in <code><a href="/docs/linux/man/2-socket/">socket</a></code>(2). Only <code>SOCK_STREAM</code> and <code>SOCK_DGRAM</code> are valid.</dl>
<h2>Versions</h2>
<p>Support for VMware (VMCI) has been available since Linux 3.9. KVM (virtio) is supported since Linux 4.8. Hyper-V is supported since Linux 4.14. </p>
<p> VMADDR_CID_LOCAL is supported since Linux 5.6. Local communication in the guest and on the host is available since Linux 5.6. Previous versions supported only local communication within a guest (not on the host), and with only some transports (VMCI and virtio).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-bind/">bind</a></code>(2), <code><a href="/docs/linux/man/2-connect/">connect</a></code>(2), <code><a href="/docs/linux/man/2-listen/">listen</a></code>(2), <code><a href="/docs/linux/man/2-recv/">recv</a></code>(2), <code><a href="/docs/linux/man/2-send/">send</a></code>(2), <code><a href="/docs/linux/man/2-socket/">socket</a></code>(2), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
