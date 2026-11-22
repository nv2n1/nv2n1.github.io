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
<p>The request starts with a <i>struct nlmsghdr</i> header described in <code><a href="/docs/linux/man/7-netlink/">netlink</a></code>(7) with <i>nlmsg_type</i> field set to <code>SOCK_DIAG_BY_FAMILY</code>. It is followed by a header specific to the address family that starts with a common part shared by all address families: struct inet_diag_msg {<br/>
    __u8 idiag_family;<br/>
    __u8 idiag_state;<br/>
    __u8 idiag_timer;<br/>
    __u8 idiag_retrans;<br/>
    struct inet_diag_sockid id;<br/>
    __u32 idiag_expires;<br/>
    __u32 idiag_rqueue;<br/>
    __u32 idiag_wqueue;<br/>
    __u32 idiag_uid;<br/>
    __u32 idiag_inode;<br/>
}; The fields of this structure are as follows:</p>
<dl>
<dt><i>sdiag_family</i></dt>
<dd>An address family. It should be set to the appropriate <code>AF_*</code> constant.</dd>
<dt><i>sdiag_protocol</i></dt>
<dd>Depends on <i>sdiag_family</i>. It should be set to the appropriate <code>IPPROTO_*</code> constant for <code>AF_INET</code> and <code>AF_INET6</code>, and to 0 otherwise.</dd></dl>
<p> If the <i>nlmsg_flags</i> field of the <i>struct nlmsghdr</i> header has the <code>NLM_F_DUMP</code> flag set, it means that a list of sockets is being requested; otherwise it is a query about an individual socket.</p>
<h3>Response</h3>
<p>The response starts with a <i>struct nlmsghdr</i> header and is followed by an array of objects specific to the address family. The array is to be accessed with the standard <code>NLMSG_*</code> macros from the <code><a href="/docs/linux/man/3-netlink/">netlink</a></code>(3) API. Each object is the NLA (netlink attributes) list that is to be accessed with the <code>RTA_*</code> macros from <code><a href="/docs/linux/man/3-rtnetlink/">rtnetlink</a></code>(3) API.</p>
<h3>UNIX domain sockets</h3>
<p>For UNIX domain sockets the request is represented in the following structure: struct inet_diag_msg {<br/>
    __u8 idiag_family;<br/>
    __u8 idiag_state;<br/>
    __u8 idiag_timer;<br/>
    __u8 idiag_retrans;<br/>
    struct inet_diag_sockid id;<br/>
    __u32 idiag_expires;<br/>
    __u32 idiag_rqueue;<br/>
    __u32 idiag_wqueue;<br/>
    __u32 idiag_uid;<br/>
    __u32 idiag_inode;<br/>
}; The fields of this structure are as follows:</p>
<dl>
<dt><i>sdiag_family</i></dt>
<dd>The address family; it should be set to <code>AF_UNIX</code>.</dd></dl>
<p> <i>sdiag_protocol</i></p>
<dl>
<dd><i>pad</i> These fields should be set to 0.</dd>
<dt><i>udiag_states</i></dt>
<dd>This is a bit mask that defines a filter of sockets states. Only those sockets whose states are in this mask will be reported. Ignored when querying for an individual socket. Supported values are:</dd></dl>
<dl>
<dd>1 &lt;&lt; <code>TCP_ESTABLISHED</code> 1 &lt;&lt; <code>TCP_LISTEN</code></dd></dl>
<dl>
<dt><i>udiag_ino</i></dt>
<dd>This is an inode number when querying for an individual socket. Ignored when querying for a list of sockets.</dd>
<dt><i>udiag_show</i></dt>
<dd>This is a set of flags defining what kind of information to report. Each requested kind of information is reported back as a netlink attribute as described below:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>UDIAG_SHOW_NAME</code></dt>
<dd>The attribute reported in answer to this request is <code>UNIX_DIAG_NAME</code>. The payload associated with this attribute is the pathname to which the socket was bound (a sequence of bytes up to <code>UNIX_PATH_MAX</code> length).</dd>
<dt><code>UDIAG_SHOW_VFS</code></dt>
<dd>The attribute reported in answer to this request is <code>UNIX_DIAG_VFS</code>. The payload associated with this attribute is represented in the following structure:</dd>
<dd>struct unix_diag_vfs {<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32 udiag_vfs_dev;<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32 udiag_vfs_ino; };</dd>
<dd>The fields of this structure are as follows:</dd>
<dl>
<dd>
</dd><dl>
<dt><i>udiag_vfs_dev</i></dt>
<dd>The device number of the corresponding on-disk socket inode.</dd>
<dt><i>udiag_vfs_ino</i></dt>
<dd>The inode number of the corresponding on-disk socket inode.</dd></dl>
</dl>
<dt><code>UDIAG_SHOW_PEER</code></dt>
<dd>The attribute reported in answer to this request is <code>UNIX_DIAG_PEER</code>. The payload associated with this attribute is a __u32 value which is the peer&#8217;s inode number. This attribute is reported for connected sockets only.</dd>
<dt><code>UDIAG_SHOW_ICONS</code></dt>
<dd>The attribute reported in answer to this request is <code>UNIX_DIAG_ICONS</code>. The payload associated with this attribute is an array of __u32 values which are inode numbers of sockets that has passed the <code><a href="/docs/linux/man/2-connect/">connect</a></code>(2) call, but hasn&#8217;t been processed with <code><a href="/docs/linux/man/2-accept/">accept</a></code>(2) yet. This attribute is reported for listening sockets only.</dd>
<dt><code>UDIAG_SHOW_RQLEN</code></dt>
<dd>The attribute reported in answer to this request is <code>UNIX_DIAG_RQLEN</code>. The payload associated with this attribute is represented in the following structure:</dd>
<dd>struct unix_diag_rqlen {<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32 udiag_rqueue;<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32 udiag_wqueue; };</dd>
<dd>The fields of this structure are as follows:</dd>
<dl>
<dd>
</dd><dl>
<dt><i>udiag_rqueue</i></dt>
<dd>For listening sockets: the number of pending connections. The length of the array associated with the <code>UNIX_DIAG_ICONS</code> response attribute is equal to this value.</dd>
<dd>For established sockets: the amount of data in incoming queue.</dd>
<dt><i>udiag_wqueue</i></dt>
<dd>For listening sockets: the backlog length which equals to the value passed as the second argument to <code><a href="/docs/linux/man/2-listen/">listen</a></code>(2).</dd>
<dd>For established sockets: the amount of memory available for sending.</dd></dl>
</dl>
<dt><code>UDIAG_SHOW_MEMINFO</code></dt>
<dd>The attribute reported in answer to this request is <code>UNIX_DIAG_MEMINFO</code>. The payload associated with this attribute is an array of __u32 values described below in the subsection &quot;Socket memory information&quot;.</dd></dl>
<p> The following attributes are reported back without any specific request:</p>
<dl>
<dt><code>UNIX_DIAG_SHUTDOWN</code></dt>
<dd>The payload associated with this attribute is __u8 value which represents bits of <code><a href="/docs/linux/man/2-shutdown/">shutdown</a></code>(2) state.</dd></dl>
</dl>
<dt><i>udiag_cookie</i></dt>
<dd>This is an array of opaque identifiers that could be used along with <i>udiag_ino</i> to specify an individual socket. It is ignored when querying for a list of sockets, as well as when all its elements are set to -1.</dd></dl>
<p> The response to a query for UNIX domain sockets is represented as an array of struct inet_diag_msg {<br/>
    __u8 idiag_family;<br/>
    __u8 idiag_state;<br/>
    __u8 idiag_timer;<br/>
    __u8 idiag_retrans;<br/>
    struct inet_diag_sockid id;<br/>
    __u32 idiag_expires;<br/>
    __u32 idiag_rqueue;<br/>
    __u32 idiag_wqueue;<br/>
    __u32 idiag_uid;<br/>
    __u32 idiag_inode;<br/>
}; followed by netlink attributes. The fields of this structure are as follows:</p>
<dl>
<dt><i>udiag_family</i></dt>
<dd>This field has the same meaning as in <i>struct unix_diag_req</i>.</dd>
<dt><i>udiag_type</i></dt>
<dd>This is set to one of <code>SOCK_PACKET</code>, <code>SOCK_STREAM</code>, or <code>SOCK_SEQPACKET</code>.</dd>
<dt><i>udiag_state</i></dt>
<dd>This is set to one of <code>TCP_LISTEN</code> or <code>TCP_ESTABLISHED</code>.</dd>
<dt><i>pad</i></dt>
<dd>This field is set to 0.</dd>
<dt><i>udiag_ino</i></dt>
<dd>This is the socket inode number.</dd>
<dt><i>udiag_cookie</i></dt>
<dd>This is an array of opaque identifiers that could be used in subsequent queries.</dd></dl>
<h3>IPv4 and IPv6 sockets</h3>
<p>For IPv4 and IPv6 sockets, the request is represented in the following structure: struct inet_diag_msg {<br/>
    __u8 idiag_family;<br/>
    __u8 idiag_state;<br/>
    __u8 idiag_timer;<br/>
    __u8 idiag_retrans;<br/>
    struct inet_diag_sockid id;<br/>
    __u32 idiag_expires;<br/>
    __u32 idiag_rqueue;<br/>
    __u32 idiag_wqueue;<br/>
    __u32 idiag_uid;<br/>
    __u32 idiag_inode;<br/>
}; where <i>struct inet_diag_sockid</i> is defined as follows: struct inet_diag_msg {<br/>
    __u8 idiag_family;<br/>
    __u8 idiag_state;<br/>
    __u8 idiag_timer;<br/>
    __u8 idiag_retrans;<br/>
    struct inet_diag_sockid id;<br/>
    __u32 idiag_expires;<br/>
    __u32 idiag_rqueue;<br/>
    __u32 idiag_wqueue;<br/>
    __u32 idiag_uid;<br/>
    __u32 idiag_inode;<br/>
}; The fields of <i>struct inet_diag_req_v2</i> are as follows:</p>
<dl>
<dt><i>sdiag_family</i></dt>
<dd>This should be set to either <code>AF_INET</code> or <code>AF_INET6</code> for IPv4 or IPv6 sockets respectively.</dd>
<dt><i>sdiag_protocol</i></dt>
<dd>This should be set to one of <code>IPPROTO_TCP</code>, <code>IPPROTO_UDP</code>, or <code>IPPROTO_UDPLITE</code>.</dd>
<dt><i>idiag_ext</i></dt>
<dd>This is a set of flags defining what kind of extended information to report. Each requested kind of information is reported back as a netlink attribute as described below:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>INET_DIAG_TOS</code></dt>
<dd>The payload associated with this attribute is a __u8 value which is the TOS of the socket.</dd>
<dt><code>INET_DIAG_TCLASS</code></dt>
<dd>The payload associated with this attribute is a __u8 value which is the TClass of the socket. IPv6 sockets only. For LISTEN and CLOSE sockets, this is followed by <code>INET_DIAG_SKV6ONLY</code> attribute with associated __u8 payload value meaning whether the socket is IPv6-only or not.</dd>
<dt><code>INET_DIAG_MEMINFO</code></dt>
<dd>The payload associated with this attribute is represented in the following structure:</dd>
<dd>struct inet_diag_meminfo {<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32 idiag_rmem;<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32 idiag_wmem;<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32 idiag_fmem;<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32 idiag_tmem; };</dd>
<dd>The fields of this structure are as follows:</dd>
<dl>
<dd>
</dd><dl>
<dt><i>idiag_rmem</i></dt>
<dd>The amount of data in the receive queue.</dd>
<dt><i>idiag_wmem</i></dt>
<dd>The amount of data that is queued by TCP but not yet sent.</dd>
<dt><i>idiag_fmem</i></dt>
<dd>The amount of memory scheduled for future use (TCP only).</dd>
<dt><i>idiag_tmem</i></dt>
<dd>The amount of data in send queue.</dd></dl>
</dl>
<dt><code>INET_DIAG_SKMEMINFO</code></dt>
<dd>The payload associated with this attribute is an array of __u32 values described below in the subsection &quot;Socket memory information&quot;.</dd>
<dt><code>INET_DIAG_INFO</code></dt>
<dd>The payload associated with this attribute is specific to the address family. For TCP sockets, it is an object of type <i>struct tcp_info</i>.</dd>
<dt><code>INET_DIAG_CONG</code></dt>
<dd>The payload associated with this attribute is a string that describes the congestion control algorithm used. For TCP sockets only.</dd></dl>
</dl>
<dt><i>pad</i></dt>
<dd>This should be set to 0.</dd>
<dt><i>idiag_states</i></dt>
<dd>This is a bit mask that defines a filter of socket states. Only those sockets whose states are in this mask will be reported. Ignored when querying for an individual socket.</dd>
<dt><i>id</i></dt>
<dd>This is a socket ID object that is used in dump requests, in queries about individual sockets, and is reported back in each response. Unlike UNIX domain sockets, IPv4 and IPv6 sockets are identified using addresses and ports. All values are in network byte order.</dd></dl>
<p> The fields of <i>struct inet_diag_sockid</i> are as follows:</p>
<dl>
<dt><i>idiag_sport</i></dt>
<dd>The source port.</dd>
<dt><i>idiag_dport</i></dt>
<dd>The destination port.</dd>
<dt><i>idiag_src</i></dt>
<dd>The source address.</dd>
<dt><i>idiag_dst</i></dt>
<dd>The destination address.</dd>
<dt><i>idiag_if</i></dt>
<dd>The interface number the socket is bound to.</dd>
<dt><i>idiag_cookie</i></dt>
<dd>This is an array of opaque identifiers that could be used along with other fields of this structure to specify an individual socket. It is ignored when querying for a list of sockets, as well as when all its elements are set to -1.</dd></dl>
<p> The response to a query for IPv4 or IPv6 sockets is represented as an array of struct inet_diag_msg {<br/>
    __u8 idiag_family;<br/>
    __u8 idiag_state;<br/>
    __u8 idiag_timer;<br/>
    __u8 idiag_retrans;<br/>
    struct inet_diag_sockid id;<br/>
    __u32 idiag_expires;<br/>
    __u32 idiag_rqueue;<br/>
    __u32 idiag_wqueue;<br/>
    __u32 idiag_uid;<br/>
    __u32 idiag_inode;<br/>
}; followed by netlink attributes. The fields of this structure are as follows:</p>
<dl>
<dt><i>idiag_family</i></dt>
<dd>This is the same field as in <i>struct inet_diag_req_v2</i>.</dd>
<dt><i>idiag_state</i></dt>
<dd>This denotes socket state as in <i>struct inet_diag_req_v2</i>.</dd>
<dt><i>idiag_timer</i></dt>
<dd>For TCP sockets, this field describes the type of timer that is currently active for the socket. It is set to one of the following constants:</dd>
<dd>
</dd><dl>
<dd>
</dd><dl>
<dt><code>0</code></dt>
<dd>no timer is active</dd>
<dt><code>1</code></dt>
<dd>a retransmit timer</dd>
<dt><code>2</code></dt>
<dd>a keep-alive timer</dd>
<dt><code>3</code></dt>
<dd>a TIME_WAIT timer</dd>
<dt><code>4</code></dt>
<dd>a zero window probe timer</dd></dl>
</dl>
<dd>For non-TCP sockets, this field is set to 0.</dd>
<dt><i>idiag_retrans</i></dt>
<dd>For <i>idiag_timer</i> values 1, 2, and 4, this field contains the number of retransmits. For other <i>idiag_timer</i> values, this field is set to 0.</dd>
<dt><i>idiag_expires</i></dt>
<dd>For TCP sockets that have an active timer, this field describes its expiration time in milliseconds. For other sockets, this field is set to 0.</dd>
<dt><i>idiag_rqueue</i></dt>
<dd>For listening sockets: the number of pending connections.</dd>
<dd>For other sockets: the amount of data in the incoming queue.</dd>
<dt><i>idiag_wqueue</i></dt>
<dd>For listening sockets: the backlog length.</dd>
<dd>For other sockets: the amount of memory available for sending.</dd>
<dt><i>idiag_uid</i></dt>
<dd>This is the socket owner UID.</dd>
<dt><i>idiag_inode</i></dt>
<dd>This is the socket inode number.</dd></dl>
<h3>Socket memory information</h3>
<p>The payload associated with <code>UNIX_DIAG_MEMINFO</code> and <code>INET_DIAG_SKMEMINFO</code> netlink attributes is an array of the following __u32 values:</p>
<dl>
<dt><code>SK_MEMINFO_RMEM_ALLOC</code></dt>
<dd>The amount of data in receive queue.</dd>
<dt><code>SK_MEMINFO_RCVBUF</code></dt>
<dd>The receive socket buffer as set by <code>SO_RCVBUF</code>.</dd>
<dt><code>SK_MEMINFO_WMEM_ALLOC</code></dt>
<dd>The amount of data in send queue.</dd>
<dt><code>SK_MEMINFO_SNDBUF</code></dt>
<dd>The send socket buffer as set by <code>SO_SNDBUF</code>.</dd>
<dt><code>SK_MEMINFO_FWD_ALLOC</code></dt>
<dd>The amount of memory scheduled for future use (TCP only).</dd>
<dt><code>SK_MEMINFO_WMEM_QUEUED</code></dt>
<dd>The amount of data queued by TCP, but not yet sent.</dd>
<dt><code>SK_MEMINFO_OPTMEM</code></dt>
<dd>The amount of memory allocated for the socket&#8217;s service needs (e.g., socket filter).</dd>
<dt><code>SK_MEMINFO_BACKLOG</code></dt>
<dd>The amount of packets in the backlog (not yet processed).</dd></dl>
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
                path[path_len] = '</code>\0';

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;break;


&nbsp;<p> <wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;case UNIX_DIAG_PEER:

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(RTA_PAYLOAD(attr)&nbsp;&gt;=&nbsp;sizeof(peer))

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;peer&nbsp;=&nbsp;*(unsigned int&nbsp;*)&nbsp;RTA_DATA(attr);

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;break;

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}
 </p>


&nbsp;<p> <wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;inode=%u&quot;, diag-&gt;udiag_ino);
 </p>


&nbsp;<p> <wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(peer)

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;, peer=%u&quot;, peer);
 </p>


&nbsp;<p> <wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(path_len)

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;, name=%s%s&quot;,&nbsp;*path&nbsp;?&nbsp;&quot;&quot;&nbsp;:&nbsp;&quot;@&quot;,

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*path&nbsp;?&nbsp;path : path&nbsp;+&nbsp;1);
 </p>


&nbsp;<p> <wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;putchar('\n');

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return 0;
}
 </p>
static int
receive_responses(int fd)
{

&nbsp;<p> <wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long buf[8192&nbsp;/&nbsp;sizeof(long)];

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct sockaddr_nl nladdr&nbsp;=&nbsp;{

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.nl_family&nbsp;=&nbsp;AF_NETLINK

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;};

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct iovec iov&nbsp;=&nbsp;{

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.iov_base&nbsp;=&nbsp;buf,

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.iov_len&nbsp;=&nbsp;sizeof(buf)

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;};

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int flags&nbsp;=&nbsp;0;
 </p>


&nbsp;<p> <wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for&nbsp;(;;)&nbsp;{

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct msghdr msg&nbsp;=&nbsp;{

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.msg_name&nbsp;=&nbsp;&amp;nladdr,

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.msg_namelen&nbsp;=&nbsp;sizeof(nladdr),

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.msg_iov&nbsp;=&nbsp;&amp;iov,

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.msg_iovlen&nbsp;=&nbsp;1

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;};
 </p>


&nbsp;<p> <wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ssize_t ret&nbsp;=&nbsp;recvmsg(fd,&nbsp;&amp;msg, flags);
 </p>


&nbsp;<p> <wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(ret&nbsp;&lt;&nbsp;0)&nbsp;{

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(errno&nbsp;==&nbsp;EINTR)

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;continue;
 </p>


&nbsp;<p> <wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;recvmsg&quot;);

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return -1;

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(ret&nbsp;==&nbsp;0)

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return 0;
 </p>


&nbsp;<p> <wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;const struct nlmsghdr&nbsp;*h&nbsp;=&nbsp;(struct nlmsghdr&nbsp;*)&nbsp;buf;
 </p>


&nbsp;<p> <wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(!NLMSG_OK(h, ret))&nbsp;{

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fputs(&quot;!NLMSG_OK\n&quot;, stderr);

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return -1;

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}
 </p>


&nbsp;<p> <wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for&nbsp;(;&nbsp;NLMSG_OK(h, ret);&nbsp;h&nbsp;=&nbsp;NLMSG_NEXT(h, ret))&nbsp;{

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(h-&gt;nlmsg_type&nbsp;==&nbsp;NLMSG_DONE)

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return 0;
 </p>


&nbsp;<p> <wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(h-&gt;nlmsg_type&nbsp;==&nbsp;NLMSG_ERROR)&nbsp;{

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;const struct nlmsgerr&nbsp;*err&nbsp;=&nbsp;NLMSG_DATA(h);
 </p>


&nbsp;<p> <wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(h-&gt;nlmsg_len&nbsp;&lt;&nbsp;NLMSG_LENGTH(sizeof(*err)))&nbsp;{

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fputs(&quot;NLMSG_ERROR\n&quot;, stderr);

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}&nbsp;else&nbsp;{

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errno&nbsp;=&nbsp;-err-&gt;error;

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;NLMSG_ERROR&quot;);

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}
 </p>


&nbsp;<p> <wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return -1;

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}
 </p>


&nbsp;<p> <wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(h-&gt;nlmsg_type&nbsp;!=&nbsp;SOCK_DIAG_BY_FAMILY)&nbsp;{

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;unexpected nlmsg_type&nbsp;%u\n&quot;,

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(unsigned)&nbsp;h-&gt;nlmsg_type);

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return -1;

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}
 </p>


&nbsp;<p> <wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(print_diag(NLMSG_DATA(h), h-&gt;nlmsg_len))

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return -1;

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}
}
 </p>
int
main(void)
{

&nbsp;<p> <wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int fd&nbsp;=&nbsp;socket(AF_NETLINK, SOCK_RAW, NETLINK_SOCK_DIAG);
 </p>


&nbsp;<p> <wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(fd&nbsp;&lt;&nbsp;0)&nbsp;{

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;socket&quot;);

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return 1;

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}
 </p>


&nbsp;<p> <wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int ret&nbsp;=&nbsp;send_query(fd)&nbsp;|| receive_responses(fd);
 </p>


&nbsp;<p> <wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;close(fd);

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return ret;
}

 </p>
<h2>SEE ALSO</h2>

 netlink (3),
 rtnetlink (3),
 netlink (7),
 tcp (7)

<h2>COLOPHON</h2>
This page is part of release 5.10 of the Linux
 man-pages project.
A description of the project,
information about reporting bugs,
and the latest version of this page,
can be found at
https://www.kernel.org/doc/man-pages/.
