---
title: "gnutls_packet_get(3)"
name: "gnutls_packet_get"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_packet_get/"
description: "gnutls_packet_get – API function"
---

<h2>NAME</h2>
<p> gnutls_packet_get &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>void gnutls_packet_get(gnutls_packet_t </code><i>packet</i><code>, gnutls_datum_t * </code><i>data</i><code>, unsigned char * </code><i>sequence</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_packet_t packet</p>
<dd> is a <code>gnutls_packet_t</code> structure.</p>
<dt>gnutls_datum_t * data</p>
<dd> will contain the data present in the <i>packet</i> structure (may be <code>NULL</code>)</p>
<dt>unsigned char * sequence</p>
<dd> the 8-bytes of the packet sequence number (may be <code>NULL</code>)</dl>
<h2>DESCRIPTION</h2>
<p> This function returns the data and sequence number associated with the received packet.</p>
<h2>SINCE</h2>
<p> 3.3.5</p>
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
