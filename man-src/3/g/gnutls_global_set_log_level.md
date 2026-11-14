---
title: "gnutls_global_set_log_level(3)"
name: "gnutls_global_set_log_level"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_global_set_log_level/"
description: "gnutls_global_set_log_level – API function"
---

<h2>NAME</h2>
<p> gnutls_global_set_log_level &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>void gnutls_global_set_log_level(int </code><i>level</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>int level</p>
<dd> it&#8217;s an integer from 0 to 99.</dl>
<h2>DESCRIPTION</h2>
<p> This is the function that allows you to set the log level. The level is an integer between 0 and 9. Higher values mean more verbosity. The default value is 0. Larger values should only be used with care, since they may reveal sensitive information. </p>
<p> Use a log level over 10 to enable all debugging options.</p>
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
