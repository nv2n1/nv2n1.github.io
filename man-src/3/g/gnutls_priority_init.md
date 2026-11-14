---
title: "gnutls_priority_init(3)"
name: "gnutls_priority_init"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_priority_init/"
description: "gnutls_priority_init – API function"
---

<h2>NAME</h2>
<p> gnutls_priority_init &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>int gnutls_priority_init(gnutls_priority_t * </code><i>priority_cache</i><code>, const char * </code><i>priorities</i><code>, const char ** </code><i>err_pos</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_priority_t * priority_cache</p>
<dd> is a <code>gnutls_prioritity_t</code> structure.</p>
<dt>const char * priorities</p>
<dd> is a string describing priorities (may be <code>NULL</code>)</p>
<dt>const char ** err_pos</p>
<dd> In case of an error this will have the position in the string the error occurred</dl>
<h2>DESCRIPTION</h2>
<p> Sets priorities for the ciphers, key exchange methods, macs and compression methods. </p>
<p> The <code>priorities</code> option allows you to specify a colon separated list of the cipher priorities to enable. Some keywords are defined to provide quick access to common preferences. </p>
<p> Unless there is a special need, use the &quot;NORMAL&quot; keyword to apply a reasonable security level, or &quot;NORMAL:<code>COMPAT</code>&quot; for compatibility. </p>
<p> &quot;PERFORMANCE&quot; means all the &quot;secure&quot; ciphersuites are enabled, limited to 128 bit ciphers and sorted by terms of speed performance. </p>
<p> &quot;LEGACY&quot; the NORMAL settings for GnuTLS 3.2.x or earlier. There is no verification profile set, and the allowed DH primes are considered weak today. </p>
<p> &quot;NORMAL&quot; means all &quot;secure&quot; ciphersuites. The 256-bit ciphers are included as a fallback only. The ciphers are sorted by security margin. </p>
<p> &quot;PFS&quot; means all &quot;secure&quot; ciphersuites that support perfect forward secrecy. The 256-bit ciphers are included as a fallback only. The ciphers are sorted by security margin. </p>
<p> &quot;SECURE128&quot; means all &quot;secure&quot; ciphersuites of security level 128-bit or more. </p>
<p> &quot;SECURE192&quot; means all &quot;secure&quot; ciphersuites of security level 192-bit or more. </p>
<p> &quot;SUITEB128&quot; means all the NSA SuiteB ciphersuites with security level of 128. </p>
<p> &quot;SUITEB192&quot; means all the NSA SuiteB ciphersuites with security level of 192. </p>
<p> &quot;EXPORT&quot; means all ciphersuites are enabled, including the low-security 40 bit ciphers. </p>
<p> &quot;NONE&quot; means nothing is enabled. This disables even protocols and compression methods. </p>
<p> &quot; <i>KEYWORD</i> &quot; The system administrator imposed settings. The provided keywords will be expanded from a configuration-time provided file &#8211; default is: /etc/gnutls/default-priorities. Any keywords that follow it, will be appended to the expanded string. If there is no system string, then the function will fail. The system file should be formatted as &quot;KEYWORD=VALUE&quot;, e.g., &quot;SYSTEM=NORMAL:-ARCFOUR-128&quot;. </p>
<p> Special keywords are &quot;!&quot;, &quot;-&quot; and &quot;+&quot;. &quot;!&quot; or &quot;-&quot; appended with an algorithm will remove this algorithm. &quot;+&quot; appended with an algorithm will add this algorithm. </p>
<p> Check the GnuTLS manual section &quot;Priority strings&quot; for detailed information.</p>
<h2>EXAMPLES</h2>
<p> &quot;NONE:+VERS-TLS-ALL:+MAC-ALL:+RSA:+AES-128-CBC:+SIGN-ALL:+COMP-NULL&quot; </p>
<p> &quot;NORMAL:-ARCFOUR-128&quot; means normal ciphers except for ARCFOUR-128. </p>
<p> &quot;SECURE128:-VERS-SSL3.0:+COMP-DEFLATE&quot; means that only secure ciphers are enabled, SSL3.0 is disabled, and libz compression enabled. </p>
<p> &quot;NONE:+VERS-TLS-ALL:+AES-128-CBC:+RSA:+SHA1:+COMP-NULL:+SIGN-RSA-SHA1&quot;, </p>
<p> &quot;NONE:+VERS-TLS-ALL:+AES-128-CBC:+ECDHE-RSA:+SHA1:+COMP-NULL:+SIGN-RSA-SHA1:+CURVE-SECP256R1&quot;, </p>
<p> &quot;SECURE256:+SECURE128&quot;, </p>
<p> Note that &quot;NORMAL:<code>COMPAT</code>&quot; is the most compatible mode. </p>
<p> A <code>NULL</code> <i>priorities</i> string indicates the default priorities to be used (this is available since GnuTLS 3.3.0).</p>
<h2>RETURNS</h2>
<p> On syntax error <code>GNUTLS_E_INVALID_REQUEST</code> is returned, <code>GNUTLS_E_SUCCESS</code> on success, or an error code.</p>
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
