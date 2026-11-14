---
title: "gnutls_x509_crq_set_subject_alt_name(3)"
name: "gnutls_x509_crq_set_subject_alt_name"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_crq_set_subject_alt_name/"
description: "gnutls_x509_crq_set_subject_alt_name – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_crq_set_subject_alt_name &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509.h&gt;</code> </p>
<p> <code>int gnutls_x509_crq_set_subject_alt_name(gnutls_x509_crq_t </code><i>crq</i><code>, gnutls_x509_subject_alt_name_t </code><i>nt</i><code>, const void * </code><i>data</i><code>, unsigned int </code><i>data_size</i><code>, unsigned int </code><i>flags</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_x509_crq_t crq</p>
<dd> a certificate request of type <code>gnutls_x509_crq_t</code></p>
<dt>gnutls_x509_subject_alt_name_t nt</p>
<dd> is one of the <code>gnutls_x509_subject_alt_name_t</code> enumerations</p>
<dt>const void * data</p>
<dd> The data to be set</p>
<dt>unsigned int data_size</p>
<dd> The size of data to be set</p>
<dt>unsigned int flags</p>
<dd> <code>GNUTLS_FSAN_SET</code> to clear previous data or <code>GNUTLS_FSAN_APPEND</code> to append.</dl>
<h2>DESCRIPTION</h2>
<p> This function will set the subject alternative name certificate extension. It can set the following types:</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, otherwise a negative error value.</p>
<h2>SINCE</h2>
<p> 2.8.0</p>
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
