---
title: "gnutls_x509_crt_get_issuer_alt_name2(3)"
name: "gnutls_x509_crt_get_issuer_alt_name2"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_crt_get_issuer_alt_name2/"
description: "gnutls_x509_crt_get_issuer_alt_name2 – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_crt_get_issuer_alt_name2 &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509.h&gt;</code> </p>
<p> <code>int gnutls_x509_crt_get_issuer_alt_name2(gnutls_x509_crt_t </code><i>cert</i><code>, unsigned int </code><i>seq</i><code>, void * </code><i>ian</i><code>, size_t * </code><i>ian_size</i><code>, unsigned int * </code><i>ian_type</i><code>, unsigned int * </code><i>critical</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_x509_crt_t cert</p>
<dd> should contain a <code>gnutls_x509_crt_t</code> structure</p>
<dt>unsigned int seq</p>
<dd> specifies the sequence number of the alt name (0 for the first one, 1 for the second etc.)</p>
<dt>void * ian</p>
<dd> is the place where the alternative name will be copied to</p>
<dt>size_t * ian_size</p>
<dd> holds the size of ret.</p>
<dt>unsigned int * ian_type</p>
<dd> holds the type of the alternative name (one of gnutls_x509_subject_alt_name_t).</p>
<dt>unsigned int * critical</p>
<dd> will be non-zero if the extension is marked as critical (may be null)</dl>
<h2>DESCRIPTION</h2>
<p> This function will return the alternative names, contained in the given certificate. It is the same as <code>gnutls_x509_crt_get_issuer_alt_name()</code> except for the fact that it will return the type of the alternative name in <i>ian_type</i> even if the function fails for some reason (i.e. the buffer provided is not enough).</p>
<h2>RETURNS</h2>
<p> the alternative issuer name type on success, one of the enumerated <code>gnutls_x509_subject_alt_name_t</code>. It will return <code>GNUTLS_E_SHORT_MEMORY_BUFFER</code> if <i>ian_size</i> is not large enough to hold the value. In that case <i>ian_size</i> will be updated with the required size. If the certificate does not have an Alternative name with the specified sequence number then <code>GNUTLS_E_REQUESTED_DATA_NOT_AVAILABLE</code> is returned.</p>
<h2>SINCE</h2>
<p> 2.10.0</p>
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
