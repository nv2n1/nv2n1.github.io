---
title: "gnutls_record_get_direction(3)"
name: "gnutls_record_get_direction"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_record_get_direction/"
description: "gnutls_record_get_direction – API function"
---

<h2>NAME</h2>
<p> gnutls_record_get_direction &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>int gnutls_record_get_direction(gnutls_session_t </code><i>session</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_session_t session</p>
<dd> is a <code>gnutls_session_t</code> structure.</dl>
<h2>DESCRIPTION</h2>
<p> This function provides information about the internals of the record protocol and is only useful if a prior gnutls function call (e.g. <code>gnutls_handshake()</code>) was interrupted for some reason, that is, if a function returned <code>GNUTLS_E_INTERRUPTED</code> or <code>GNUTLS_E_AGAIN</code>. In such a case, you might want to call <code>select()</code> or <code>poll()</code> before calling the interrupted gnutls function again. To tell you whether a file descriptor should be selected for either reading or writing, <code>gnutls_record_get_direction()</code> returns 0 if the interrupted function was trying to read data, and 1 if it was trying to write data. </p>
<p> This function&#8217;s output is unreliable if you are using the<br />
&nbsp;<wbr><i>session</i>&nbsp;<wbr>in different threads, for sending and receiving.</p>
<h2>RETURNS</h2>
<p> 0 if trying to read data, 1 if trying to write data.</p>
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
