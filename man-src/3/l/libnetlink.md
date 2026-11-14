---
title: "libnetlink(3)"
name: "libnetlink"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libnetlink/"
description: "libnetlink – A library for accessing the netlink service"
---

<h2 class="name">NAME</h2>
<p> libnetlink &#8211; A library for accessing the netlink service </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;asm/types.h&gt;

#include &lt;libnetlink.h&gt;

#include &lt;linux/netlink.h&gt;

#include &lt;linux/rtnetlink.h&gt;
int rtnl_open(struct rtnl_handle *rth, unsigned subscriptions) int rtnl_wilddump_request(struct rtnl_handle *rth, int family, int type) int rtnl_send(struct rtnl_handle *rth, char *buf, int len) int rtnl_dump_request(struct rtnl_handle *rth, int type, void *req, int len) int rtnl_dump_filter(struct rtnl_handle *rth,
                                                                                                                                                                                                                                                                                                     int (*filter)(struct sockaddr_nl *, struct nlmsghdr *n, void *),
                                                                                                                                                                                                                                                                                                     void *arg1,
                                                                                                                                                                                                                                                                                                     int (*junk)(struct sockaddr_nl *, struct nlmsghdr *n, void *),
                                                                                                                                                                                                                                                                                                     void *arg2) int rtnl_talk(struct rtnl_handle *rtnl, struct nlmsghdr *n, pid_t peer,
                                                                                                                                                                                                                                                                                                                               unsigned groups, struct nlmsghdr *answer,

                                                                                                                                                                                                                                                                                                                               int (*junk)(struct sockaddr_nl *, struct nlmsghdr *n, void *),

                                                                                                                                                                                                                                                                                                                               void *jarg) int rtnl_listen(struct rtnl_handle *rtnl,
                                                                                                                                                                                                                                                                                                                                                           int (*handler)(struct sockaddr_nl *, struct rtnl_ctrl_data *,
                                                                                                                                                                                                                                                                                                                                                                          struct nlmsghdr *n, void *),
                                                                                                                                                                                                                                                                                                                                                           void *jarg) int rtnl_from_file(FILE *rtnl,
                                                                                                                                                                                                                                                                                                                                                                                          int (*handler)(struct sockaddr_nl *, struct nlmsghdr *n, void *),
                                                                                                                                                                                                                                                                                                                                                                                          void *jarg) int addattr32(struct nlmsghdr *n, int maxlen, int type, __u32 data) int addattr_l(struct nlmsghdr *n, int maxlen, int type, void *data, int alen) int rta_addattr32(struct rtattr *rta, int maxlen, int type, __u32 data) int rta_addattr_l(struct rtattr *rta, int maxlen, int type, void *data, int alen)
</code></pre>
<h2>DESCRIPTION</h2>
<p> libnetlink provides a higher level interface to <code><a href="/docs/linux/man/7-rtnetlink/">rtnetlink</a></code>(7). The read functions return 0 on success and a negative errno on failure. The send functions return the amount of data sent, or -1 on error.</p>
<dl>
<dt>rtnl_open</p>
<dd> Open a rtnetlink socket and save the state into the <code>rth</code> handle. This handle is passed to all subsequent calls. <code>subscriptions</code> is a bitmap of the rtnetlink multicast groups the socket will be a member of. </p>
<dt>rtnl_wilddump_request</p>
<dd> Request a full dump of the <code>type</code> database for <code>family</code> addresses. <code>type</code> is a rtnetlink message type. </p>
<dt>rtnl_dump_request</p>
<dd> Request a full dump of the <code>type</code> data buffer into <code>buf</code> with maximum length of <code>len.</code> <code>type</code> is a rtnetlink message type. </p>
<dt>rtnl_dump_filter</p>
<dd> Receive netlink data after a request and filter it. The <code>filter</code> callback checks if the received message is wanted. It gets the source address of the message, the message itself and <code>arg1</code> as arguments. 0 as return means that the filter passed, a negative value is returned by <i>rtnl_dump_filter</i> in case of error. NULL for <i>filter</i> means to not use a filter. <code>junk</code> is used to filter messages not destined to the local socket. Only one message bundle is received. If there is a message pending, this function does not block. </p>
<dt>rtnl_listen</p>
<dd> Receive netlink data after a request and pass it to <i>handler.</i> <code>handler</code> is a callback that gets the message source address, anscillary data, the message itself, and the <code>jarg</code> cookie as arguments. It will get called for all received messages. Only one message bundle is received. If there is a message pending this function does not block. </p>
<dt>rtnl_from_file</p>
<dd> Works like <i>rtnl_listen,</i> but reads a netlink message bundle from the file <code>file</code> and passes the messages to <code>handler</code> for parsing. The file should contain raw data as received from a rtnetlink socket.</dl>
<p> The following functions are useful to construct custom rtnetlink messages. For simple database dumping with filtering it is better to use the higher level functions above. See <code><a href="/docs/linux/man/3-rtnetlink/">rtnetlink</a></code>(3) and <code><a href="/docs/linux/man/3-netlink/">netlink</a></code>(3) on how to generate a rtnetlink message. The following utility functions require a continuous buffer that already contains a netlink message header and a rtnetlink request. </p>
<dl>
<dt>rtnl_send</p>
<dd> Send the rtnetlink message in <code>buf</code> of length <code>len</code> to handle <code>rth.</code> </p>
<dt>addattr32</p>
<dd> Add a __u32 attribute of type <code>type</code> and with value <code>data</code> to netlink message <code>n,</code> which is part of a buffer of length <code>maxlen.</code> </p>
<dt>addattr_l</p>
<dd> Add a variable length attribute of type <code>type</code> and with value <code>data</code> and <code>alen</code> length to netlink message <code>n,</code> which is part of a buffer of length <code>maxlen.</code> <code>data</code> is copied. </p>
<dt>rta_addattr32</p>
<dd> Initialize the rtnetlink attribute <code>rta</code> with a __u32 data value. </p>
<dt>rta_addattr32</p>
<dd> Initialize the rtnetlink attribute <code>rta</code> with a variable length data value. </p>
</dl>
<h2>BUGS</h2>
<p> This library is meant for internal use, use libmnl for new programs. </p>
<p> The functions sometimes use fprintf and exit when a fatal error occurs. This library should be named librtnetlink. </p>
<h2>AUTHORS</h2>
<p> netlink/rtnetlink was designed and written by Alexey Kuznetsov. Andi Kleen wrote the man page. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-netlink/">netlink</a></code>(7), <code><a href="/docs/linux/man/7-rtnetlink/">rtnetlink</a></code>(7)<br />
 /usr/include/linux/rtnetlink.h </p>
<h2>Index</h2>
