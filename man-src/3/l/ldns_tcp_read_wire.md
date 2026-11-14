---
title: "ldns_tcp_read_wire(3)"
name: "ldns_tcp_read_wire"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldns_tcp_read_wire/"
description: "ldns_tcp_send_query, ldns_tcp_read_wire, ldns_tcp_connect"
---

<h2>NAME</h2>
<p> ldns_tcp_send_query, ldns_tcp_read_wire, ldns_tcp_connect </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;stdint.h&gt;<br />
 #include &lt;stdbool.h&gt; </p>
<p> #include &lt;ldns/ldns.h&gt; </p>
<p> ssize_t ldns_tcp_send_query(ldns_buffer *qbin, int sockfd, const struct sockaddr_storage *to, socklen_t tolen); </p>
<p> uint8_t* ldns_tcp_read_wire(int sockfd, size_t *size); </p>
<p> int ldns_tcp_connect(const struct sockaddr_storage *to, socklen_t tolen, struct timeval timeout); </p>
<h2>DESCRIPTION</h2>
<dl>
<dt> <i>ldns_tcp_send_query</i>()</p>
<dd>send a query via tcp to a server. Don&#8217;t want for the answer </p>
<p> .br <code>qbin</code>: the buffer to send .br <code>sockfd</code>: the socket to use .br <code>to</code>: which ip to send it .br <code>tolen</code>: socketlen .br Returns number of bytes sent</dl>
<dl>
<dt> <i>ldns_tcp_read_wire</i>()</p>
<dd>This routine may block. Use ldns_tcp_read_wire_timeout, it checks timeouts. Gives back a raw packet from the wire and reads the header data from the given socket. Allocates the data (of size size) itself, so don&#8217;t forget to free </p>
<p> .br <code>sockfd</code>: the socket to read from .br <code>size</code>: the number of bytes that are read .br Returns the data read</dl>
<dl>
<dt> <i>ldns_tcp_connect</i>()</p>
<dd>Create a tcp socket to the specified address .br <code>to</code>: ip and family .br <code>tolen</code>: length of to .br <code>timeout</code>: timeout for the connect attempt .br Returns a socket descriptor</dl>
<h2>AUTHOR</h2>
<p> The ldns team at NLnet Labs. Which consists out of Jelte Jansen and Miek Gieben. </p>
<h2>REPORTING BUGS</h2>
<p> Please report bugs to ldns-team [at] nlnetlabs.nl or in our bugzilla at <a rel="nofollow" href="http://www.nlnetlabs.nl/bugs/index.html">http://www.nlnetlabs.nl/bugs/index.html</a> </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2004 &#8211; 2006 NLnet Labs. </p>
<p> Licensed under the BSD License. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>SEE ALSO</h2>
<p> <i>ldns_send</i>, <i>ldns_pkt</i>, <i>ldns_resolver</i>. And <code>perldoc Net::DNS</code>, <code>RFC1034</code>, <code>RFC1035</code>, <code>RFC4033</code>, <code>RFC4034</code> and <code>RFC4035</code>.</p>
<h2>REMARKS</h2>
<p> This manpage was automaticly generated from the ldns source code by use of Doxygen and some perl. </p>
<h2>Index</h2>
