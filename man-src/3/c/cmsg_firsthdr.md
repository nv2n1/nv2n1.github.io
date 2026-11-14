---
title: "cmsg_firsthdr(3)"
name: "cmsg_firsthdr"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cmsg_firsthdr/"
description: "CMSG_ALIGN, CMSG_SPACE, CMSG_NXTHDR, CMSG_FIRSTHDR – access ancillary data"
---

<p>CMSG_ALIGN, CMSG_SPACE, CMSG_NXTHDR, CMSG_FIRSTHDR &#8211; access ancillary data </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;sys/socket.h&gt;</code>
<code>struct cmsghdr *CMSG_FIRSTHDR(struct msghdr *</code><i>msgh</i><code>);</code>
<code>struct cmsghdr *CMSG_NXTHDR(struct msghdr *</code><i>msgh</i><code>,</code>
<code> struct cmsghdr *</code>cmsg<code>);</code>
<code>size_t CMSG_ALIGN(size_t </code><i>length</i><code>);</code>
<code>size_t CMSG_SPACE(size_t </code><i>length</i><code>);</code>
<code>size_t CMSG_LEN(size_t </code><i>length</i><code>);</code>
<code>unsigned char *CMSG_DATA(struct cmsghdr *</code><i>cmsg</i><code>);</code></pre>
<h2>Description</h2>
<p>These macros are used to create and access control messages (also called ancillary data) that are not a part of the socket payload. This control information may include the interface the packet was received on, various rarely used header fields, an extended error description, a set of file descriptors, or UNIX credentials. For instance, control messages can be used to send additional header fields such as IP options. Ancillary data is sent by calling <code><a href="/docs/linux/man/2-sendmsg/">sendmsg</a></code>(2) and received by calling <code><a href="/docs/linux/man/2-recvmsg/">recvmsg</a></code>(2). See their manual pages for more information. </p>
<p> Ancillary data is a sequence of <i>cmsghdr</i> structures with appended data. See the specific protocol man pages for the available control message types. The maximum ancillary buffer size allowed per socket can be set using <i>/proc/sys/net/core/optmem_max</i>; see <code><a href="/docs/linux/man/7-socket/">socket</a></code>(7). </p>
<p> The <i>cmsghdr</i> structure is defined as follows: </p>
<p> struct cmsghdr {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;size_t cmsg_len;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Data byte count, including header<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(type is socklen_t in POSIX)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;cmsg_level;&nbsp;<wbr>&nbsp;/*&nbsp;Originating protocol&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;cmsg_type;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Protocol-specific type&nbsp;*/ /* followed by<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned char cmsg_data[];&nbsp;*/ }; </p>
<p> The sequence of <i>cmsghdr</i> structures should never be accessed directly. Instead, use only the following macros:</p>
<dl COMPACT>
<dt>*</p>
<dd><code>CMSG_FIRSTHDR</code>() returns a pointer to the first <i>cmsghdr</i> in the ancillary data buffer associated with the passed <i>msghdr</i>. It returns NULL if there isn&#8217;t enough space for a <i>cmsghdr</i> in the buffer.</p>
<dt>*</p>
<dd><code>CMSG_NXTHDR</code>() returns the next valid <i>cmsghdr</i> after the passed <i>cmsghdr</i>. It returns NULL when there isn&#8217;t enough space left in the buffer.</p>
<dd>When initializing a buffer that will contain a series of <i>cmsghdr</i> structures (e.g., to be sent with <code><a href="/docs/linux/man/2-sendmsg/">sendmsg</a></code>(2)), that buffer should first be zero-initialized to ensure the correct operation of <code>CMSG_NXTHDR</code>().</p>
<dt>*</p>
<dd><code>CMSG_ALIGN</code>(), given a length, returns it including the required alignment. This is a constant expression.</p>
<dt>*</p>
<dd><code>CMSG_SPACE</code>() returns the number of bytes an ancillary element with payload of the passed data length occupies. This is a constant expression.</p>
<dt>*</p>
<dd><code>CMSG_DATA</code>() returns a pointer to the data portion of a <i>cmsghdr</i>. The pointer returned cannot be assumed to be suitably aligned for accessing arbitrary payload data types. Applications should not cast it to a pointer type matching the payload, but should instead use <code><a href="/docs/linux/man/3-memcpy/">memcpy</a></code>(3) to copy data to or from a suitably declared object.</p>
<dt>*</p>
<dd><code>CMSG_LEN</code>() returns the value to store in the <i>cmsg_len</i> member of the <i>cmsghdr</i> structure, taking into account any necessary alignment. It takes the data length as an argument. This is a constant expression.</dl>
<p> To create ancillary data, first initialize the <i>msg_controllen</i> member of the <i>msghdr</i> with the length of the control message buffer. Use <code>CMSG_FIRSTHDR</code>() on the <i>msghdr</i> to get the first control message and <code>CMSG_NXTHDR</code>() to get all subsequent ones. In each control message, initialize <i>cmsg_len</i> (with <code>CMSG_LEN</code>()), the other <i>cmsghdr</i> header fields, and the data portion using <code>CMSG_DATA</code>(). Finally, the <i>msg_controllen</i> field of the <i>msghdr</i> should be set to the sum of the <code>CMSG_SPACE</code>() of the length of all control messages in the buffer. For more information on the <i>msghdr</i>, see <code><a href="/docs/linux/man/2-recvmsg/">recvmsg</a></code>(2).</p>
<h2>Conforming To</h2>
<p>This ancillary data model conforms to the POSIX.1g draft, 4.4BSD-Lite, the IPv6 advanced API described in RFC 2292 and SUSv2. <code>CMSG_FIRSTHDR</code>(), <code>CMSG_NXTHDR</code>(), and <code>CMSG_DATA</code>() are specified in POSIX.1-2008. <code>CMSG_SPACE</code>() and <code>CMSG_LEN</code>() will be included in the next POSIX release (Issue 8). </p>
<p> <code>CMSG_ALIGN</code>() is a Linux extension.</p>
<h2>Notes</h2>
<p>For portability, ancillary data should be accessed using only the macros described here. <code>CMSG_ALIGN</code>() is a Linux extension and should not be used in portable programs. </p>
<p> In Linux, <code>CMSG_LEN</code>(), <code>CMSG_DATA</code>(), and <code>CMSG_ALIGN</code>() are constant expressions (assuming their argument is constant), meaning that these values can be used to declare the size of global variables. This may not be portable, however.</p>
<h2>Examples</h2>
<p>This code looks for the <code>IP_TTL</code> option in a received ancillary buffer: </p>
<p> struct msghdr msgh; struct cmsghdr *cmsg; int received_ttl; </p>
<p> /* Receive auxiliary data in msgh */ </p>
<p> for (cmsg = CMSG_FIRSTHDR(&amp;msgh); cmsg != NULL;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;cmsg&nbsp;=&nbsp;CMSG_NXTHDR(&amp;msgh, cmsg))&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(cmsg-&gt;cmsg_level&nbsp;==&nbsp;IPPROTO_IP<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&amp;&amp;&nbsp;cmsg-&gt;cmsg_type&nbsp;==&nbsp;IP_TTL)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;memcpy(&amp;receive_ttl, CMSG_DATA(cmsg), sizeof(received_ttl));<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;break;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} } </p>
<p> if (cmsg == NULL) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Error: IP_TTL not enabled or small buffer or I/O error&nbsp;*/ } </p>
<p> The code below passes an array of file descriptors over a UNIX domain socket using <code>SCM_RIGHTS</code>: </p>
<p> struct msghdr msg = { 0 }; struct cmsghdr *cmsg; int myfds[NUM_FD]; /* Contains the file descriptors to pass */ char iobuf[1]; struct iovec io = {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.iov_base&nbsp;=&nbsp;iobuf,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.iov_len&nbsp;=&nbsp;sizeof(iobuf) }; union { /* Ancillary data buffer, wrapped in a union<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;in order to ensure it is suitably aligned&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char buf[CMSG_SPACE(sizeof(myfds))];<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct cmsghdr align; } u; </p>
<p> msg.msg_iov = &amp;io; msg.msg_iovlen = 1; msg.msg_control = u.buf; msg.msg_controllen = sizeof(u.buf); cmsg = CMSG_FIRSTHDR(&amp;msg); cmsg-&gt;cmsg_level = SOL_SOCKET; cmsg-&gt;cmsg_type = SCM_RIGHTS; cmsg-&gt;cmsg_len = CMSG_LEN(sizeof(myfds)); memcpy(CMSG_DATA(cmsg), myfds, sizeof(myfds));</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-recvmsg/">recvmsg</a></code>(2), <code><a href="/docs/linux/man/2-sendmsg/">sendmsg</a></code>(2) </p>
<p> RFC 2292</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a></p>
