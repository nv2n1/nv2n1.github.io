---
title: "sock_diag(7)"
name: "sock_diag"
section: "7"
letter: "s"
url: "/docs/linux/man/7-sock_diag/"
description: "sock_diag – obtaining information about sockets"
---

<p>sock_diag &#8211; obtaining information about sockets</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;linux/inet_diag.h&gt; /* for IPv4 and IPv6 sockets */
#include &lt;linux/sock_diag.h&gt;
#include &lt;linux/unix_diag.h&gt; /* for UNIX domain sockets */
#include &lt;sys/socket.h&gt;

diag_socket = socket(AF_NETLINK, socket_type, NETLINK_SOCK_DIAG);</code></pre>
<h2>Description</h2>
<p>The sock_diag netlink subsystem provides a mechanism for obtaining information about sockets of various address families from the kernel. This subsystem can be used to obtain information about individual sockets or request a list of sockets. In the request, the caller can specify additional information it would like to obtain about the socket, for example, memory information or information specific to the address family. When requesting a list of sockets, the caller can specify filters that would be applied by the kernel to select a subset of sockets to report. For now, there is only the ability to filter sockets by state (connected, listening, and so on.) Note that sock_diag reports only those sockets that have a name; that is, either sockets bound explicitly with <code><a href="/docs/linux/man/2-bind/">bind</a></code>(2) or sockets that were automatically bound to an address (e.g., by <code><a href="/docs/linux/man/2-connect/">connect</a></code>(2)). This is the same set of sockets that is available via <i>/proc/net/unix</i>, <i>/proc/net/tcp</i>, <i>/proc/net/udp</i>, and so on.</p>
<h3>Request</h3>
<p>The request starts with a <i>struct nlmsghdr</i> header described in <code><a href="/docs/linux/man/7-netlink/">netlink</a></code>(7) with <i>nlmsg_type</i> field set to <code>SOCK_DIAG_BY_FAMILY</code>. It is followed by a header specific to the address family that starts with a common part shared by all address families: struct inet_diag_msg {<br />
    __u8 idiag_family;<br />
    __u8 idiag_state;<br />
    __u8 idiag_timer;<br />
    __u8 idiag_retrans;<br />
    struct inet_diag_sockid id;<br />
    __u32 idiag_expires;<br />
    __u32 idiag_rqueue;<br />
    __u32 idiag_wqueue;<br />
    __u32 idiag_uid;<br />
    __u32 idiag_inode;<br />
}; The fields of this structure are as follows:</p>
<dl>
<dt><i>sdiag_family</i></p>
<dd>An address family. It should be set to the appropriate <code>AF_*</code> constant.</p>
<dt><i>sdiag_protocol</i></p>
<dd>Depends on <i>sdiag_family</i>. It should be set to the appropriate <code>IPPROTO_*</code> constant for <code>AF_INET</code> and <code>AF_INET6</code>, and to 0 otherwise.</dl>
<p> If the <i>nlmsg_flags</i> field of the <i>struct nlmsghdr</i> header has the <code>NLM_F_DUMP</code> flag set, it means that a list of sockets is being requested; otherwise it is a query about an individual socket.</p>
<h3>Response</h3>
<p>The response starts with a <i>struct nlmsghdr</i> header and is followed by an array of objects specific to the address family. The array is to be accessed with the standard <code>NLMSG_*</code> macros from the <code><a href="/docs/linux/man/3-netlink/">netlink</a></code>(3) API. Each object is the NLA (netlink attributes) list that is to be accessed with the <code>RTA_*</code> macros from <code><a href="/docs/linux/man/3-rtnetlink/">rtnetlink</a></code>(3) API.</p>
<h3>UNIX domain sockets</h3>
<p>For UNIX domain sockets the request is represented in the following structure: struct inet_diag_msg {<br />
    __u8 idiag_family;<br />
    __u8 idiag_state;<br />
    __u8 idiag_timer;<br />
    __u8 idiag_retrans;<br />
    struct inet_diag_sockid id;<br />
    __u32 idiag_expires;<br />
    __u32 idiag_rqueue;<br />
    __u32 idiag_wqueue;<br />
    __u32 idiag_uid;<br />
    __u32 idiag_inode;<br />
}; The fields of this structure are as follows:</p>
<dl>
<dt><i>sdiag_family</i></p>
<dd>The address family; it should be set to <code>AF_UNIX</code>.</dl>
<p> <i>sdiag_protocol</i></p>
<dl>
<dd><i>pad</i> These fields should be set to 0.</p>
<dt><i>udiag_states</i></p>
<dd>This is a bit mask that defines a filter of sockets states. Only those sockets whose states are in this mask will be reported. Ignored when querying for an individual socket. Supported values are:</dl>
<dl>
<dd>1 &lt;&lt; <code>TCP_ESTABLISHED</code> 1 &lt;&lt; <code>TCP_LISTEN</code></dl>
<dl>
<dt><i>udiag_ino</i></p>
<dd>This is an inode number when querying for an individual socket. Ignored when querying for a list of sockets.</p>
<dt><i>udiag_show</i></p>
<dd>This is a set of flags defining what kind of information to report. Each requested kind of information is reported back as a netlink attribute as described below:</p>
<dl>
<dd>
<dl>
<dt><code>UDIAG_SHOW_NAME</code></p>
<dd>The attribute reported in answer to this request is <code>UNIX_DIAG_NAME</code>. The payload associated with this attribute is the pathname to which the socket was bound (a sequence of bytes up to <code>UNIX_PATH_MAX</code> length).</p>
<dt><code>UDIAG_SHOW_VFS</code></p>
<dd>The attribute reported in answer to this request is <code>UNIX_DIAG_VFS</code>. The payload associated with this attribute is represented in the following structure:</p>
<dd>struct unix_diag_vfs {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32 udiag_vfs_dev;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32 udiag_vfs_ino; };</p>
<dd>The fields of this structure are as follows:</p>
<dl>
<dd>
<dl>
<dt><i>udiag_vfs_dev</i></p>
<dd>The device number of the corresponding on-disk socket inode.</p>
<dt><i>udiag_vfs_ino</i></p>
<dd>The inode number of the corresponding on-disk socket inode.</dl>
</dl>
<dt><code>UDIAG_SHOW_PEER</code></p>
<dd>The attribute reported in answer to this request is <code>UNIX_DIAG_PEER</code>. The payload associated with this attribute is a __u32 value which is the peer&#8217;s inode number. This attribute is reported for connected sockets only.</p>
<dt><code>UDIAG_SHOW_ICONS</code></p>
<dd>The attribute reported in answer to this request is <code>UNIX_DIAG_ICONS</code>. The payload associated with this attribute is an array of __u32 values which are inode numbers of sockets that has passed the <code><a href="/docs/linux/man/2-connect/">connect</a></code>(2) call, but hasn&#8217;t been processed with <code><a href="/docs/linux/man/2-accept/">accept</a></code>(2) yet. This attribute is reported for listening sockets only.</p>
<dt><code>UDIAG_SHOW_RQLEN</code></p>
<dd>The attribute reported in answer to this request is <code>UNIX_DIAG_RQLEN</code>. The payload associated with this attribute is represented in the following structure:</p>
<dd>struct unix_diag_rqlen {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32 udiag_rqueue;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32 udiag_wqueue; };</p>
<dd>The fields of this structure are as follows:</p>
<dl>
<dd>
<dl>
<dt><i>udiag_rqueue</i></p>
<dd>For listening sockets: the number of pending connections. The length of the array associated with the <code>UNIX_DIAG_ICONS</code> response attribute is equal to this value.</p>
<dd>For established sockets: the amount of data in incoming queue.</p>
<dt><i>udiag_wqueue</i></p>
<dd>For listening sockets: the backlog length which equals to the value passed as the second argument to <code><a href="/docs/linux/man/2-listen/">listen</a></code>(2).</p>
<dd>For established sockets: the amount of memory available for sending.</dl>
</dl>
<dt><code>UDIAG_SHOW_MEMINFO</code></p>
<dd>The attribute reported in answer to this request is <code>UNIX_DIAG_MEMINFO</code>. The payload associated with this attribute is an array of __u32 values described below in the subsection &quot;Socket memory information&quot;.</dl>
<p> The following attributes are reported back without any specific request:</p>
<dl>
<dt><code>UNIX_DIAG_SHUTDOWN</code></p>
<dd>The payload associated with this attribute is __u8 value which represents bits of <code><a href="/docs/linux/man/2-shutdown/">shutdown</a></code>(2) state.</dl>
</dl>
<dt><i>udiag_cookie</i></p>
<dd>This is an array of opaque identifiers that could be used along with <i>udiag_ino</i> to specify an individual socket. It is ignored when querying for a list of sockets, as well as when all its elements are set to -1.</dl>
<p> The response to a query for UNIX domain sockets is represented as an array of struct inet_diag_msg {<br />
    __u8 idiag_family;<br />
    __u8 idiag_state;<br />
    __u8 idiag_timer;<br />
    __u8 idiag_retrans;<br />
    struct inet_diag_sockid id;<br />
    __u32 idiag_expires;<br />
    __u32 idiag_rqueue;<br />
    __u32 idiag_wqueue;<br />
    __u32 idiag_uid;<br />
    __u32 idiag_inode;<br />
}; followed by netlink attributes. The fields of this structure are as follows:</p>
<dl>
<dt><i>udiag_family</i></p>
<dd>This field has the same meaning as in <i>struct unix_diag_req</i>.</p>
<dt><i>udiag_type</i></p>
<dd>This is set to one of <code>SOCK_PACKET</code>, <code>SOCK_STREAM</code>, or <code>SOCK_SEQPACKET</code>.</p>
<dt><i>udiag_state</i></p>
<dd>This is set to one of <code>TCP_LISTEN</code> or <code>TCP_ESTABLISHED</code>.</p>
<dt><i>pad</i></p>
<dd>This field is set to 0.</p>
<dt><i>udiag_ino</i></p>
<dd>This is the socket inode number.</p>
<dt><i>udiag_cookie</i></p>
<dd>This is an array of opaque identifiers that could be used in subsequent queries.</dl>
<h3>IPv4 and IPv6 sockets</h3>
<p>For IPv4 and IPv6 sockets, the request is represented in the following structure: struct inet_diag_msg {<br />
    __u8 idiag_family;<br />
    __u8 idiag_state;<br />
    __u8 idiag_timer;<br />
    __u8 idiag_retrans;<br />
    struct inet_diag_sockid id;<br />
    __u32 idiag_expires;<br />
    __u32 idiag_rqueue;<br />
    __u32 idiag_wqueue;<br />
    __u32 idiag_uid;<br />
    __u32 idiag_inode;<br />
}; where <i>struct inet_diag_sockid</i> is defined as follows: struct inet_diag_msg {<br />
    __u8 idiag_family;<br />
    __u8 idiag_state;<br />
    __u8 idiag_timer;<br />
    __u8 idiag_retrans;<br />
    struct inet_diag_sockid id;<br />
    __u32 idiag_expires;<br />
    __u32 idiag_rqueue;<br />
    __u32 idiag_wqueue;<br />
    __u32 idiag_uid;<br />
    __u32 idiag_inode;<br />
}; The fields of <i>struct inet_diag_req_v2</i> are as follows:</p>
<dl>
<dt><i>sdiag_family</i></p>
<dd>This should be set to either <code>AF_INET</code> or <code>AF_INET6</code> for IPv4 or IPv6 sockets respectively.</p>
<dt><i>sdiag_protocol</i></p>
<dd>This should be set to one of <code>IPPROTO_TCP</code>, <code>IPPROTO_UDP</code>, or <code>IPPROTO_UDPLITE</code>.</p>
<dt><i>idiag_ext</i></p>
<dd>This is a set of flags defining what kind of extended information to report. Each requested kind of information is reported back as a netlink attribute as described below:</p>
<dl>
<dd>
<dl>
<dt><code>INET_DIAG_TOS</code></p>
<dd>The payload associated with this attribute is a __u8 value which is the TOS of the socket.</p>
<dt><code>INET_DIAG_TCLASS</code></p>
<dd>The payload associated with this attribute is a __u8 value which is the TClass of the socket. IPv6 sockets only. For LISTEN and CLOSE sockets, this is followed by <code>INET_DIAG_SKV6ONLY</code> attribute with associated __u8 payload value meaning whether the socket is IPv6-only or not.</p>
<dt><code>INET_DIAG_MEMINFO</code></p>
<dd>The payload associated with this attribute is represented in the following structure:</p>
<dd>struct inet_diag_meminfo {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32 idiag_rmem;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32 idiag_wmem;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32 idiag_fmem;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32 idiag_tmem; };</p>
<dd>The fields of this structure are as follows:</p>
<dl>
<dd>
<dl>
<dt><i>idiag_rmem</i></p>
<dd>The amount of data in the receive queue.</p>
<dt><i>idiag_wmem</i></p>
<dd>The amount of data that is queued by TCP but not yet sent.</p>
<dt><i>idiag_fmem</i></p>
<dd>The amount of memory scheduled for future use (TCP only).</p>
<dt><i>idiag_tmem</i></p>
<dd>The amount of data in send queue.</dl>
</dl>
<dt><code>INET_DIAG_SKMEMINFO</code></p>
<dd>The payload associated with this attribute is an array of __u32 values described below in the subsection &quot;Socket memory information&quot;.</p>
<dt><code>INET_DIAG_INFO</code></p>
<dd>The payload associated with this attribute is specific to the address family. For TCP sockets, it is an object of type <i>struct tcp_info</i>.</p>
<dt><code>INET_DIAG_CONG</code></p>
<dd>The payload associated with this attribute is a string that describes the congestion control algorithm used. For TCP sockets only.</dl>
</dl>
<dt><i>pad</i></p>
<dd>This should be set to 0.</p>
<dt><i>idiag_states</i></p>
<dd>This is a bit mask that defines a filter of socket states. Only those sockets whose states are in this mask will be reported. Ignored when querying for an individual socket.</p>
<dt><i>id</i></p>
<dd>This is a socket ID object that is used in dump requests, in queries about individual sockets, and is reported back in each response. Unlike UNIX domain sockets, IPv4 and IPv6 sockets are identified using addresses and ports. All values are in network byte order.</dl>
<p> The fields of <i>struct inet_diag_sockid</i> are as follows:</p>
<dl>
<dt><i>idiag_sport</i></p>
<dd>The source port.</p>
<dt><i>idiag_dport</i></p>
<dd>The destination port.</p>
<dt><i>idiag_src</i></p>
<dd>The source address.</p>
<dt><i>idiag_dst</i></p>
<dd>The destination address.</p>
<dt><i>idiag_if</i></p>
<dd>The interface number the socket is bound to.</p>
<dt><i>idiag_cookie</i></p>
<dd>This is an array of opaque identifiers that could be used along with other fields of this structure to specify an individual socket. It is ignored when querying for a list of sockets, as well as when all its elements are set to -1.</dl>
<p> The response to a query for IPv4 or IPv6 sockets is represented as an array of struct inet_diag_msg {<br />
    __u8 idiag_family;<br />
    __u8 idiag_state;<br />
    __u8 idiag_timer;<br />
    __u8 idiag_retrans;<br />
    struct inet_diag_sockid id;<br />
    __u32 idiag_expires;<br />
    __u32 idiag_rqueue;<br />
    __u32 idiag_wqueue;<br />
    __u32 idiag_uid;<br />
    __u32 idiag_inode;<br />
}; followed by netlink attributes. The fields of this structure are as follows:</p>
<dl>
<dt><i>idiag_family</i></p>
<dd>This is the same field as in <i>struct inet_diag_req_v2</i>.</p>
<dt><i>idiag_state</i></p>
<dd>This denotes socket state as in <i>struct inet_diag_req_v2</i>.</p>
<dt><i>idiag_timer</i></p>
<dd>For TCP sockets, this field describes the type of timer that is currently active for the socket. It is set to one of the following constants:</p>
<dd>
<dl>
<dd>
<dl>
<dt><code>0</code></p>
<dd>no timer is active</p>
<dt><code>1</code></p>
<dd>a retransmit timer</p>
<dt><code>2</code></p>
<dd>a keep-alive timer</p>
<dt><code>3</code></p>
<dd>a TIME_WAIT timer</p>
<dt><code>4</code></p>
<dd>a zero window probe timer</dl>
</dl>
<dd>For non-TCP sockets, this field is set to 0.</p>
<dt><i>idiag_retrans</i></p>
<dd>For <i>idiag_timer</i> values 1, 2, and 4, this field contains the number of retransmits. For other <i>idiag_timer</i> values, this field is set to 0.</p>
<dt><i>idiag_expires</i></p>
<dd>For TCP sockets that have an active timer, this field describes its expiration time in milliseconds. For other sockets, this field is set to 0.</p>
<dt><i>idiag_rqueue</i></p>
<dd>For listening sockets: the number of pending connections.</p>
<dd>For other sockets: the amount of data in the incoming queue.</p>
<dt><i>idiag_wqueue</i></p>
<dd>For listening sockets: the backlog length.</p>
<dd>For other sockets: the amount of memory available for sending.</p>
<dt><i>idiag_uid</i></p>
<dd>This is the socket owner UID.</p>
<dt><i>idiag_inode</i></p>
<dd>This is the socket inode number.</dl>
<h3>Socket memory information</h3>
<p>The payload associated with <code>UNIX_DIAG_MEMINFO</code> and <code>INET_DIAG_SKMEMINFO</code> netlink attributes is an array of the following __u32 values:</p>
<dl>
<dt><code>SK_MEMINFO_RMEM_ALLOC</code></p>
<dd>The amount of data in receive queue.</p>
<dt><code>SK_MEMINFO_RCVBUF</code></p>
<dd>The receive socket buffer as set by <code>SO_RCVBUF</code>.</p>
<dt><code>SK_MEMINFO_WMEM_ALLOC</code></p>
<dd>The amount of data in send queue.</p>
<dt><code>SK_MEMINFO_SNDBUF</code></p>
<dd>The send socket buffer as set by <code>SO_SNDBUF</code>.</p>
<dt><code>SK_MEMINFO_FWD_ALLOC</code></p>
<dd>The amount of memory scheduled for future use (TCP only).</p>
<dt><code>SK_MEMINFO_WMEM_QUEUED</code></p>
<dd>The amount of data queued by TCP, but not yet sent.</p>
<dt><code>SK_MEMINFO_OPTMEM</code></p>
<dd>The amount of memory allocated for the socket&#8217;s service needs (e.g., socket filter).</p>
<dt><code>SK_MEMINFO_BACKLOG</code></p>
<dd>The amount of packets in the backlog (not yet processed).</dl>
<h2>Versions</h2>
<p><code>NETLINK_INET_DIAG</code> was introduced in Linux 2.6.14 and supported <code>AF_INET</code> and <code>AF_INET6</code> sockets only. In Linux 3.3, it was renamed to <code>NETLINK_SOCK_DIAG</code> and extended to support <code>AF_UNIX</code> sockets. </p>
<p> <code>UNIX_DIAG_MEMINFO</code> and <code>INET_DIAG_SKMEMINFO</code> were introduced in Linux 3.6.</p>
<h2>Conforming To</h2>
<p>The NETLINK_SOCK_DIAG API is Linux-specific.</p>
<h2>Examples</h2>
<p>The following example program prints inode number, peer&#8217;s inode number, and name of all UNIX domain sockets in the current namespace. </p>
<pre><code>#include &lt;errno.h&gt;
#include &lt;linux/netlink.h&gt;
#include &lt;linux/rtnetlink.h&gt;
#include &lt;linux/sock_diag.h&gt;
#include &lt;linux/unix_diag.h&gt;
#include &lt;stdio.h&gt;
#include &lt;string.h&gt;
#include &lt;sys/socket.h&gt;
#include &lt;sys/un.h&gt;
#include &lt;unistd.h&gt;
static int
send_query(int fd)
{
    struct sockaddr_nl nladdr = {
        .nl_family = AF_NETLINK};
    struct
    {
        struct nlmsghdr nlh;
        struct unix_diag_req udr;
    } req = {
        .nlh = {
            .nlmsg_len = sizeof(req),
            .nlmsg_type = SOCK_DIAG_BY_FAMILY,
            .nlmsg_flags = NLM_F_REQUEST | NLM_F_DUMP},
        .udr = {.sdiag_family = AF_UNIX, .udiag_states = -1, .udiag_show = UDIAG_SHOW_NAME | UDIAG_SHOW_PEER}};
    struct iovec iov = {
        .iov_base = &amp;req,
        .iov_len = sizeof(req)};
    struct msghdr msg = {
        .msg_name = &amp;nladdr,
        .msg_namelen = sizeof(nladdr),
        .msg_iov = &amp;iov,
        .msg_iovlen = 1};
    for (;;) {
        if (sendmsg(fd, &amp;msg, 0) &lt; 0) {
            if (errno == EINTR)
                continue;
            perror(&quot;sendmsg&quot;);
            return -1;
        }
        return 0;
    }
}
static int
print_diag(const struct unix_diag_msg *diag, unsigned int len)
{
    if (len &lt; NLMSG_LENGTH(sizeof(*diag))) {
        fputs(&quot;short response
&quot;, stderr);
        return -1;
    }
    if (diag-&gt;udiag_family != AF_UNIX) {
        fprintf(stderr, &quot;unexpected family %u
&quot;, diag-&gt;udiag_family);
        return -1;
    }
    unsigned int rta_len = len - NLMSG_LENGTH(sizeof(*diag));
    unsigned int peer = 0;
    size_t path_len = 0;
    char path[sizeof(((struct sockaddr_un *)0)-&gt;sun_path) + 1];
    for (struct rtattr *attr = (struct rtattr *)(diag + 1);
         RTA_OK(attr, rta_len); attr = RTA_NEXT(attr, rta_len)) {
        switch (attr-&gt;rta_type) {
        case UNIX_DIAG_NAME:
            if (!path_len) {
                path_len = RTA_PAYLOAD(attr);
                if (path_len &gt; sizeof(path) - 1)
                    path_len = sizeof(path) - 1;
                memcpy(path, RTA_DATA(attr), path_len);
                path[path_len] = '
