---
title: "netlink(3)"
name: "netlink"
section: "3"
letter: "n"
url: "/docs/linux/man/3-netlink/"
description: "netlink – Netlink macros"
---

<p>netlink &#8211; Netlink macros</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;asm/types.h&gt;
#include &lt;linux/netlink.h&gt;

int NLMSG_ALIGN(size_t len);
int NLMSG_LENGTH(size_t len);
int NLMSG_SPACE(size_t len);
void *NLMSG_DATA(struct nlmsghdr *nlh);
struct nlmsghdr *NLMSG_NEXT(struct nlmsghdr *nlh, int len);
int NLMSG_OK(struct nlmsghdr *nlh, int len);
int NLMSG_PAYLOAD(struct nlmsghdr *nlh, int len);</code></pre>
<h2>Description</h2>
<p><i>&lt;linux/netlink.h&gt;</i> defines several standard macros to access or create a netlink datagram. They are similar in spirit to the macros defined in <code><a href="/docs/linux/man/3-cmsg/">cmsg</a></code>(3) for auxiliary data. The buffer passed to and from a netlink socket should be accessed using only these macros.</p>
<dl>
<dt><code>NLMSG_ALIGN</code>()</p>
<dd>Round the length of a netlink message up to align it properly.</p>
<dt><code>NLMSG_LENGTH</code>()</p>
<dd>Given the payload length, <i>len</i>, this macro returns the aligned length to store in the <i>nlmsg_len</i> field of the <i>nlmsghdr</i>.</p>
<dt><code>NLMSG_SPACE</code>()</p>
<dd>Return the number of bytes that a netlink message with payload of <i>len</i> would occupy.</p>
<dt><code>NLMSG_DATA</code>()</p>
<dd>Return a pointer to the payload associated with the passed <i>nlmsghdr</i>.</p>
<dd><code>NLMSG_NEXT</code>() Get the next <i>nlmsghdr</i> in a multipart message. The caller must check if the current <i>nlmsghdr</i> didn&#8217;t have the <code>NLMSG_DONE</code> set&#8212;this function doesn&#8217;t return NULL on end. The <i>len</i> argument is an lvalue containing the remaining length of the message buffer. This macro decrements it by the length of the message header.</p>
<dt><code>NLMSG_OK</code>()</p>
<dd>Return true if the netlink message is not truncated and is in a form suitable for parsing.</p>
<dt><code>NLMSG_PAYLOAD</code>()</p>
<dd>Return the length of the payload associated with the <i>nlmsghdr</i>.</dl>
<h2>Conforming To</h2>
<p>These macros are nonstandard Linux extensions.</p>
<h2>Notes</h2>
<p>It is often better to use netlink via <i>libnetlink</i> than via the low-level kernel interface.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-libnetlink/">libnetlink</a></code>(3), <code><a href="/docs/linux/man/7-netlink/">netlink</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
