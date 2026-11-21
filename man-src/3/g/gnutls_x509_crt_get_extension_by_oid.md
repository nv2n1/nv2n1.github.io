---

title: "gnutls_x509_crt_get_extension_by_oid(3)"
name: "gnutls_x509_crt_get_extension_by_oid"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_crt_get_extension_by_oid/"
description: "gnutls_x509_crt_get_extension_by_oid – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_crt_get_extension_by_oid &#8211; API function</p>
<p> <code>#include &lt;gnutls/x509.h&gt;</code> </p>
<p> <code>int gnutls_x509_crt_get_extension_by_oid(gnutls_x509_crt_t </code><i>cert</i><code>, const char * </code><i>oid</i><code>, int </code><i>indx</i><code>, void * </code><i>buf</i><code>, size_t * </code><i>buf_size</i><code>, unsigned int * </code><i>critical</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_x509_crt_t cert</dt>
<dd> should contain a <code>gnutls_x509_crt_t</code> structure</dd>
<dt>const char * oid</dt>
<dd> holds an Object Identified in null terminated string</dd>
<dt>int indx</dt>
<dd> In case multiple same OIDs exist in the extensions, this specifies which to send. Use (0) to get the first one.</dd>
<dt>void * buf</dt>
<dd> a pointer to a structure to hold the name (may be null)</dd>
<dt>size_t * buf_size</dt>
<dd> initially holds the size of <i>buf</i></dd>
<dt>unsigned int * critical</dt>
<dd> will be non-zero if the extension is marked as critical</dd></dl>
<p> This function will return the extension specified by the OID in the certificate. The extensions will be returned as binary data DER encoded, in the provided buffer.</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, otherwise a negative error code is returned. If the certificate does not contain the specified extension GNUTLS_E_REQUESTED_DATA_NOT_AVAILABLE will be returned.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;bugs [at] gnutls.org&gt;.<br />
 Home page: <a rel="nofollow" href="http://www.gnutls.org">http://www.gnutls.org</a> </p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2001-2014 Free Software Foundation, Inc..<br />
 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>gnutls</code> is maintained as a Texinfo manual. If the /usr/share/doc/gnutls/ directory does not contain the HTML form visit <code></p>
<dl>
<dt><a rel="nofollow" href="http://www.gnutls.org/manual/">http://www.gnutls.org/manual/</a></dt>
<dd> </code></dd></dl>
