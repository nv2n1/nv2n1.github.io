---
title: "gnutls_ocsp_req_add_cert_id(3)"
name: "gnutls_ocsp_req_add_cert_id"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_ocsp_req_add_cert_id/"
description: "gnutls_ocsp_req_add_cert_id – API function"
---

<h2>NAME</h2>
<p> gnutls_ocsp_req_add_cert_id &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/ocsp.h&gt;</code> </p>
<p> <code>int gnutls_ocsp_req_add_cert_id(gnutls_ocsp_req_t </code><i>req</i><code>, gnutls_digest_algorithm_t </code><i>digest</i><code>, const gnutls_datum_t * </code><i>issuer_name_hash</i><code>, const gnutls_datum_t * </code><i>issuer_key_hash</i><code>, const gnutls_datum_t * </code><i>serial_number</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_ocsp_req_t req</p>
<dd> should contain a <code>gnutls_ocsp_req_t</code> structure</p>
<dt>gnutls_digest_algorithm_t digest</p>
<dd> hash algorithm, a <code>gnutls_digest_algorithm_t</code> value</p>
<dt>const gnutls_datum_t * issuer_name_hash</p>
<dd> hash of issuer&#8217;s DN</p>
<dt>const gnutls_datum_t * issuer_key_hash</p>
<dd> hash of issuer&#8217;s public key</p>
<dt>const gnutls_datum_t * serial_number</p>
<dd> serial number of certificate to check</dl>
<h2>DESCRIPTION</h2>
<p> This function will add another request to the OCSP request for a particular certificate having the issuer name hash of<br />
&nbsp;<wbr><i>issuer_name_hash</i>&nbsp;<wbr>and issuer key hash of&nbsp;<wbr>&nbsp;<wbr><i>issuer_key_hash</i>&nbsp;<wbr>(both hashed using <i>digest</i> ) and serial number <i>serial_number</i> . </p>
<p> The information needed corresponds to the CertID structure: </p>
<p> &lt;informalexample&gt;&lt;programlisting&gt; CertID ::= SEQUENCE { hashAlgorithm AlgorithmIdentifier, issuerNameHash OCTET STRING, &#8212; Hash of Issuer&#8217;s DN issuerKeyHash OCTET STRING, &#8212; Hash of Issuers public key serialNumber CertificateSerialNumber } &lt;/programlisting&gt;&lt;/informalexample&gt;</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, otherwise a negative error code is returned.</p>
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
