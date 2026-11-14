---
title: "gnutls_x509_name_constraints_get_excluded(3)"
name: "gnutls_x509_name_constraints_get_excluded"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_name_constraints_get_excluded/"
description: "gnutls_x509_name_constraints_get_excluded – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_name_constraints_get_excluded &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509.h&gt;</code> </p>
<p> <code>int gnutls_x509_name_constraints_get_excluded(gnutls_x509_name_constraints_t </code><i>nc</i><code>, unsigned </code><i>idx</i><code>, unsigned * </code><i>type</i><code>, gnutls_datum_t * </code><i>name</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_x509_name_constraints_t nc</p>
<dd> the extracted name constraints structure</p>
<dt>unsigned idx</p>
<dd> the index of the constraint</p>
<dt>unsigned * type</p>
<dd> the type of the constraint (of type gnutls_x509_subject_alt_name_t)</p>
<dt>gnutls_datum_t * name</p>
<dd> the name in the constraint (of the specific type)</dl>
<h2>DESCRIPTION</h2>
<p> This function will return an intermediate structure containing the name constraints of the provided CA certificate. That structure can be used in combination with <code>gnutls_x509_name_constraints_check()</code> to verify whether a server&#8217;s name is in accordance with the constraints. </p>
<p> The name should be treated as constant and valid for the lifetime of <i>nc</i> .</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, <code>GNUTLS_E_REQUESTED_DATA_NOT_AVAILABLE</code> if the extension is not present, otherwise a negative error value.</p>
<h2>SINCE</h2>
<p> 3.3.0</p>
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
