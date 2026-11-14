---
title: "gnutls_tpm_key_list_get_url(3)"
name: "gnutls_tpm_key_list_get_url"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_tpm_key_list_get_url/"
description: "gnutls_tpm_key_list_get_url – API function"
---

<h2>NAME</h2>
<p> gnutls_tpm_key_list_get_url &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/tpm.h&gt;</code> </p>
<p> <code>int gnutls_tpm_key_list_get_url(gnutls_tpm_key_list_t </code><i>list</i><code>, unsigned int </code><i>idx</i><code>, char ** </code><i>url</i><code>, unsigned int </code><i>flags</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_tpm_key_list_t list</p>
<dd> a list of the keys</p>
<dt>unsigned int idx</p>
<dd> The index of the key (starting from zero)</p>
<dt>char ** url</p>
<dd> The URL to be returned</p>
<dt>unsigned int flags</p>
<dd> should be zero</dl>
<h2>DESCRIPTION</h2>
<p> This function will return for each given index a URL of the corresponding key. If the provided index is out of bounds then <code>GNUTLS_E_REQUESTED_DATA_NOT_AVAILABLE</code> is returned.</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, otherwise a negative error value.</p>
<h2>SINCE</h2>
<p> 3.1.0</p>
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
