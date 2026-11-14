---
title: "gnutls_record_can_use_length_hiding(3)"
name: "gnutls_record_can_use_length_hiding"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_record_can_use_length_hiding/"
description: "gnutls_record_can_use_length_hiding – API function"
---

<h2>NAME</h2>
<p> gnutls_record_can_use_length_hiding &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>int gnutls_record_can_use_length_hiding(gnutls_session_t </code><i>session</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_session_t session</p>
<dd> is a <code>gnutls_session_t</code> structure.</dl>
<h2>DESCRIPTION</h2>
<p> If the session supports length-hiding padding, you can invoke <code>gnutls_range_send_message()</code> to send a message whose length is hidden in the given range. If the session does not support length hiding padding, you can use the standard <code>gnutls_record_send()</code> function, or <code>gnutls_range_send_message()</code> making sure that the range is the same as the length of the message you are trying to send.</p>
<h2>RETURNS</h2>
<p> true (1) if the current session supports length-hiding padding, false (0) if the current session does not.</p>
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
