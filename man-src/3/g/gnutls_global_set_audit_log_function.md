---
title: "gnutls_global_set_audit_log_function(3)"
name: "gnutls_global_set_audit_log_function"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_global_set_audit_log_function/"
description: "gnutls_global_set_audit_log_function – API function"
---

<h2>NAME</h2>
<p> gnutls_global_set_audit_log_function &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>void gnutls_global_set_audit_log_function(gnutls_audit_log_func </code><i>log_func</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_audit_log_func log_func</p>
<dd> it is the audit log function</dl>
<h2>DESCRIPTION</h2>
<p> This is the function to set the audit logging function. This is a function to report important issues, such as possible attacks in the protocol. This is different from <code>gnutls_global_set_log_function()</code> because it will report also session-specific events. The session parameter will be null if there is no corresponding TLS session. </p>
<p>&nbsp;<wbr><i>gnutls_audit_log_func</i>&nbsp;<wbr>is of the form, void (*gnutls_audit_log_func)( gnutls_session_t, const char*);</p>
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
