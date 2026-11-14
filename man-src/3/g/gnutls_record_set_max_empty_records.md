---
title: "gnutls_record_set_max_empty_records(3)"
name: "gnutls_record_set_max_empty_records"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_record_set_max_empty_records/"
description: "gnutls_record_set_max_empty_records – API function"
---

<h2>NAME</h2>
<p> gnutls_record_set_max_empty_records &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>void gnutls_record_set_max_empty_records(gnutls_session_t </code><i>session</i><code>, const unsigned int </code><i>i</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_session_t session</p>
<dd> is a <code>gnutls_session_t</code> structure.</p>
<dt>const unsigned int i</p>
<dd> is the desired value of maximum empty records that can be accepted in a row.</dl>
<h2>DESCRIPTION</h2>
<p> Used to set the maximum number of empty fragments that can be accepted in a row. Accepting many empty fragments is useful for receiving length-hidden content, where empty fragments filled with pad are sent to hide the real length of a message. However, a malicious peer could send empty fragments to mount a DoS attack, so as a safety measure, a maximum number of empty fragments is accepted by default. If you know your application must accept a given number of empty fragments in a row, you can use this function to set the desired value.</p>
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
