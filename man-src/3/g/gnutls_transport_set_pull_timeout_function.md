---
title: "gnutls_transport_set_pull_timeout_function(3)"
name: "gnutls_transport_set_pull_timeout_function"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_transport_set_pull_timeout_function/"
description: "gnutls_transport_set_pull_timeout_function – API function"
---

<h2>NAME</h2>
<p> gnutls_transport_set_pull_timeout_function &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>void gnutls_transport_set_pull_timeout_function(gnutls_session_t </code><i>session</i><code>, gnutls_pull_timeout_func </code><i>func</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_session_t session</p>
<dd> is a <code>gnutls_session_t</code> structure.</p>
<dt>gnutls_pull_timeout_func func</p>
<dd> a callback function</dl>
<h2>DESCRIPTION</h2>
<p> This is the function where you set a function for gnutls to know whether data are ready to be received. It should wait for data a given time frame in milliseconds. The callback should return 0 on timeout, a positive number if data can be received, and -1 on error. You&#8217;ll need to override this function if <code>select()</code> is not suitable for the provided transport calls. </p>
<p> As with <code>select()</code>, if the timeout value is zero the callback should return zero if no data are immediately available. </p>
<p>&nbsp;<wbr><i>gnutls_pull_timeout_func</i>&nbsp;<wbr>is of the form, int (*gnutls_pull_timeout_func)(gnutls_transport_ptr_t, unsigned int ms);</p>
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
