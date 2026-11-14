---
title: "gnutls_x509_crq_set_dn_by_oid(3)"
name: "gnutls_x509_crq_set_dn_by_oid"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_crq_set_dn_by_oid/"
description: "gnutls_x509_crq_set_dn_by_oid – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_crq_set_dn_by_oid &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509.h&gt;</code> </p>
<p> <code>int gnutls_x509_crq_set_dn_by_oid(gnutls_x509_crq_t </code><i>crq</i><code>, const char * </code><i>oid</i><code>, unsigned int </code><i>raw_flag</i><code>, const void * </code><i>data</i><code>, unsigned int </code><i>sizeof_data</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_x509_crq_t crq</p>
<dd> should contain a <code>gnutls_x509_crq_t</code> structure</p>
<dt>const char * oid</p>
<dd> holds an Object Identifier in a (0)-terminated string</p>
<dt>unsigned int raw_flag</p>
<dd> must be 0, or 1 if the data are DER encoded</p>
<dt>const void * data</p>
<dd> a pointer to the input data</p>
<dt>unsigned int sizeof_data</p>
<dd> holds the size of <i>data</i></dl>
<h2>DESCRIPTION</h2>
<p> This function will set the part of the name of the Certificate request subject, specified by the given OID. The input string should be ASCII or UTF-8 encoded. </p>
<p> Some helper macros with popular OIDs can be found in gnutls/x509.h With this function you can only set the known OIDs. You can test for known OIDs using <code>gnutls_x509_dn_oid_known()</code>. For OIDs that are not known (by gnutls) you should properly DER encode your data, and call this function with raw_flag set.</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, otherwise a negative error value.</p>
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
