---
title: "gnutls_record_recv_seq(3)"
name: "gnutls_record_recv_seq"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_record_recv_seq/"
description: "gnutls_record_recv_seq – API function"
---

<h2>NAME</h2>
<p> gnutls_record_recv_seq &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>ssize_t gnutls_record_recv_seq(gnutls_session_t </code><i>session</i><code>, void * </code><i>data</i><code>, size_t </code><i>data_size</i><code>, unsigned char * </code><i>seq</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_session_t session</p>
<dd> is a <code>gnutls_session_t</code> structure.</p>
<dt>void * data</p>
<dd> the buffer that the data will be read into</p>
<dt>size_t data_size</p>
<dd> the number of requested bytes</p>
<dt>unsigned char * seq</p>
<dd> is the packet&#8217;s 64-bit sequence number. Should have space for 8 bytes.</dl>
<h2>DESCRIPTION</h2>
<p> This function is the same as <code>gnutls_record_recv()</code>, except that it returns in addition to data, the sequence number of the data. This is useful in DTLS where record packets might be received out-of-order. The returned 8-byte sequence number is an integer in big-endian format and should be treated as a unique message identification.</p>
<h2>RETURNS</h2>
<p> The number of bytes received and zero on EOF. A negative error code is returned in case of an error. The number of bytes received might be less than <i>data_size</i> .</p>
<h2>SINCE</h2>
<p> 3.0</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;bugs [at] gnutls.org&gt;.<br />
 Home page: <a rel="nofollow" href="http://www.gnutls.org">http://www.gnutls.org</a> </p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2001-2014 Free Software Foundation, Inc..<br />
 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>gnutls</code> is maintained as a Texinfo manual. If the /usr/share/doc/gnutls/ directory does not contain the HTML form visit <code></p>
<dl>
<dt><a rel="nofollow" href="http://www.gnutls.org/manual/">http://www.gnutls.org/manual/</a></p>
<dd> </code></dl>
<h2>Index</h2>
