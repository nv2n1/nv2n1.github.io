---
title: "gnutls_x509_crt_set_issuer_dn_by_oid(3)"
name: "gnutls_x509_crt_set_issuer_dn_by_oid"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_crt_set_issuer_dn_by_oid/"
description: "gnutls_x509_crt_set_issuer_dn_by_oid – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_crt_set_issuer_dn_by_oid &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509.h&gt;</code> </p>
<p> <code>int gnutls_x509_crt_set_issuer_dn_by_oid(gnutls_x509_crt_t </code><i>crt</i><code>, const char * </code><i>oid</i><code>, unsigned int </code><i>raw_flag</i><code>, const void * </code><i>name</i><code>, unsigned int </code><i>sizeof_name</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_x509_crt_t crt</p>
<dd> a certificate of type <code>gnutls_x509_crt_t</code></p>
<dt>const char * oid</p>
<dd> holds an Object Identifier in a null terminated string</p>
<dt>unsigned int raw_flag</p>
<dd> must be 0, or 1 if the data are DER encoded</p>
<dt>const void * name</p>
<dd> a pointer to the name</p>
<dt>unsigned int sizeof_name</p>
<dd> holds the size of <i>name</i></dl>
<h2>DESCRIPTION</h2>
<p> This function will set the part of the name of the Certificate issuer, specified by the given OID. The input string should be ASCII or UTF-8 encoded. </p>
<p> Some helper macros with popular OIDs can be found in gnutls/x509.h With this function you can only set the known OIDs. You can test for known OIDs using <code>gnutls_x509_dn_oid_known()</code>. For OIDs that are not known (by gnutls) you should properly DER encode your data, and call this function with <i>raw_flag</i> set. </p>
<p> Normally you do not need to call this function, since the signing operation will copy the signer&#8217;s name as the issuer of the certificate.</p>
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
