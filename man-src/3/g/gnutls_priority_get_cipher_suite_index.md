---
title: "gnutls_priority_get_cipher_suite_index(3)"
name: "gnutls_priority_get_cipher_suite_index"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_priority_get_cipher_suite_index/"
description: "gnutls_priority_get_cipher_suite_index – API function"
---

<h2>NAME</h2>
<p> gnutls_priority_get_cipher_suite_index &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>int gnutls_priority_get_cipher_suite_index(gnutls_priority_t </code><i>pcache</i><code>, unsigned int </code><i>idx</i><code>, unsigned int * </code><i>sidx</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_priority_t pcache</p>
<dd> is a <code>gnutls_prioritity_t</code> structure.</p>
<dt>unsigned int idx</p>
<dd> is an index number.</p>
<dt>unsigned int * sidx</p>
<dd> internal index of cipher suite to get information about.</dl>
<h2>DESCRIPTION</h2>
<p> Provides the internal ciphersuite index to be used with <code>gnutls_cipher_suite_info()</code>. The index <i>idx</i> provided is an index kept at the priorities structure. It might be that a valid priorities index does not correspond to a ciphersuite and in that case <code>GNUTLS_E_UNKNOWN_CIPHER_SUITE</code> will be returned. Once the last available index is crossed then <code>GNUTLS_E_REQUESTED_DATA_NOT_AVAILABLE</code> will be returned.</p>
<h2>RETURNS</h2>
<p> On success it returns <code>GNUTLS_E_SUCCESS</code> (0), or a negative error value otherwise.</p>
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
