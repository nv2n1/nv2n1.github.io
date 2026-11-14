---
title: "gnutls_record_uncork(3)"
name: "gnutls_record_uncork"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_record_uncork/"
description: "gnutls_record_uncork – API function"
---

<h2>NAME</h2>
<p> gnutls_record_uncork &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>int gnutls_record_uncork(gnutls_session_t </code><i>session</i><code>, unsigned int </code><i>flags</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_session_t session</p>
<dd> is a <code>gnutls_session_t</code> structure.</p>
<dt>unsigned int flags</p>
<dd> Could be zero or <code>GNUTLS_RECORD_WAIT</code></dl>
<h2>DESCRIPTION</h2>
<p> This resets the effect of <code>gnutls_record_cork()</code>, and flushes any pending data. If the <code>GNUTLS_RECORD_WAIT</code> flag is specified then this function will block until the data is sent or a fatal error occurs (i.e., the function will retry on <code>GNUTLS_E_AGAIN</code> and <code>GNUTLS_E_INTERRUPTED</code>). </p>
<p> If the flag <code>GNUTLS_RECORD_WAIT</code> is not specified and the function is interrupted then the <code>GNUTLS_E_AGAIN</code> or <code>GNUTLS_E_INTERRUPTED</code> errors will be returned. To obtain the data left in the corked buffer use <code>gnutls_record_check_corked()</code>.</p>
<h2>RETURNS</h2>
<p> On success the number of transmitted data is returned, or otherwise a negative error code.</p>
<h2>SINCE</h2>
<p> 3.1.9</p>
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
