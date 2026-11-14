---
title: "rtnetlink(3)"
name: "rtnetlink"
section: "3"
letter: "r"
url: "/docs/linux/man/3-rtnetlink/"
description: "rtnetlink – macros to manipulate rtnetlink messages"
---

<p>rtnetlink &#8211; macros to manipulate rtnetlink messages</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;asm/types.h&gt;

#include &lt;linux/netlink.h&gt;

#include &lt;linux/rtnetlink.h&gt;

#include &lt;sys/socket.h&gt;
rtnetlink_socket = socket(AF_NETLINK, int socket_type, NETLINK_ROUTE);
int RTA_OK(struct rtattr *rta, int rtabuflen);
void *RTA_DATA(struct rtattr *rta);
unsigned int RTA_PAYLOAD(struct rtattr *rta);
struct rtattr *RTA_NEXT(struct rtattr *rta, unsigned int rtabuflen);
unsigned int RTA_LENGTH(unsigned int length);
unsigned int RTA_SPACE(unsigned int length);</code></pre>
<h2>Description</h2>
<p>All <code><a href="/docs/linux/man/7-rtnetlink/">rtnetlink</a></code>(7) messages consist of a <code><a href="/docs/linux/man/7-netlink/">netlink</a></code>(7) message header and appended attributes. The attributes should be manipulated only using the macros provided here. </p>
<p> <code>RTA_OK(</code><i>rta</i><code>, </code><i>attrlen</i><code>)</code> returns true if <i>rta</i> points to a valid routing attribute; <i>attrlen</i> is the running length of the attribute buffer. When not true then you must assume there are no more attributes in the message, even if <i>attrlen</i> is nonzero. </p>
<p> <code>RTA_DATA(</code><i>rta</i><code>)</code> returns a pointer to the start of this attribute&#8217;s data. </p>
<p> <code>RTA_PAYLOAD(</code><i>rta</i><code>)</code> returns the length of this attribute&#8217;s data. </p>
<p> <code>RTA_NEXT(</code><i>rta</i><code>, </code><i>attrlen</i><code>)</code> gets the next attribute after <i>rta</i>. Calling this macro will update <i>attrlen</i>. You should use <code>RTA_OK</code> to check the validity of the returned pointer. </p>
<p> <code>RTA_LENGTH(</code><i>len</i><code>)</code> returns the length which is required for <i>len</i> bytes of data plus the header. </p>
<p> <code>RTA_SPACE(</code><i>len</i><code>)</code> returns the amount of space which will be needed in a message with <i>len</i> bytes of data.</p>
<h2>Conforming To</h2>
<p>These macros are nonstandard Linux extensions.</p>
<h2>Bugs</h2>
<p>This manual page is incomplete.</p>
<h2>Examples</h2>
<p>Creating a rtnetlink message to set the MTU of a device: struct {<br />
    struct nlmsghdr nh;<br />
    struct ifinfomsg if;<br />
    char attrbuf[512];<br />
} req;<br />
struct rtattr *rta;<br />
unsigned int mtu = 1000;<br />
int rtnetlink_sk = socket(AF_NETLINK, SOCK_DGRAM, NETLINK_ROUTE);<br />
memset(&amp;req, 0, sizeof(req));<br />
req.nh.nlmsg_len = NLMSG_LENGTH(sizeof(req.if));<br />
req.nh.nlmsg_flags = NLM_F_REQUEST;<br />
req.nh.nlmsg_type = RTM_NEWLINK;<br />
req.if.ifi_family = AF_UNSPEC;<br />
req.if.ifi_index = INTERFACE_INDEX;<br />
req.if.ifi_change = 0xffffffff; /* ??? */<br />
rta = (struct rtattr *)(((char *)&amp;req) +<br />
                        NLMSG_ALIGN(req.nh.nlmsg_len));<br />
rta-&gt;rta_type = IFLA_MTU;<br />
rta-&gt;rta_len = RTA_LENGTH(sizeof(mtu));<br />
req.nh.nlmsg_len = NLMSG_ALIGN(req.nh.nlmsg_len) +<br />
                   RTA_LENGTH(sizeof(mtu));<br />
memcpy(RTA_DATA(rta), &amp;mtu, sizeof(mtu));<br />
send(rtnetlink_sk, &amp;req, req.nh.nlmsg_len, 0); &#8230; </p>
<pre><code>struct {
    struct nlmsghdr nh;
    struct ifinfomsg if;
    char attrbuf[512];
} req;
struct rtattr *rta;
unsigned int mtu = 1000;
int rtnetlink_sk = socket(AF_NETLINK, SOCK_DGRAM, NETLINK_ROUTE);
memset(&amp;req, 0, sizeof(req));
req.nh.nlmsg_len = NLMSG_LENGTH(sizeof(req.if));
req.nh.nlmsg_flags = NLM_F_REQUEST;
req.nh.nlmsg_type = RTM_NEWLINK;
req.if.ifi_family = AF_UNSPEC;
req.if.ifi_index = INTERFACE_INDEX;
req.if.ifi_change = 0xffffffff; /* ??? */
rta = (struct rtattr *)(((char *)&amp;req) +
                        NLMSG_ALIGN(req.nh.nlmsg_len));
rta-&gt;rta_type = IFLA_MTU;
rta-&gt;rta_len = RTA_LENGTH(sizeof(mtu));
req.nh.nlmsg_len = NLMSG_ALIGN(req.nh.nlmsg_len) +
                   RTA_LENGTH(sizeof(mtu));
memcpy(RTA_DATA(rta), &amp;mtu, sizeof(mtu));
send(rtnetlink_sk, &amp;req, req.nh.nlmsg_len, 0);</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-netlink/">netlink</a></code>(3), <code><a href="/docs/linux/man/7-netlink/">netlink</a></code>(7), <code><a href="/docs/linux/man/7-rtnetlink/">rtnetlink</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
