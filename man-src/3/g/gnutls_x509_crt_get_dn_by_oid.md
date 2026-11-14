---
title: "gnutls_x509_crt_get_dn_by_oid(3)"
name: "gnutls_x509_crt_get_dn_by_oid"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_crt_get_dn_by_oid/"
description: "gnutls_x509_crt_get_dn_by_oid – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_crt_get_dn_by_oid &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509.h&gt;</code> </p>
<p> <code>int gnutls_x509_crt_get_dn_by_oid(gnutls_x509_crt_t </code><i>cert</i><code>, const char * </code><i>oid</i><code>, int </code><i>indx</i><code>, unsigned int </code><i>raw_flag</i><code>, void * </code><i>buf</i><code>, size_t * </code><i>buf_size</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_x509_crt_t cert</p>
<dd> should contain a <code>gnutls_x509_crt_t</code> structure</p>
<dt>const char * oid</p>
<dd> holds an Object Identified in null terminated string</p>
<dt>int indx</p>
<dd> In case multiple same OIDs exist in the RDN, this specifies which to send. Use (0) to get the first one.</p>
<dt>unsigned int raw_flag</p>
<dd> If non-zero returns the raw DER data of the DN part.</p>
<dt>void * buf</p>
<dd> a pointer where the DN part will be copied (may be null).</p>
<dt>size_t * buf_size</p>
<dd> initially holds the size of <i>buf</i></dl>
<h2>DESCRIPTION</h2>
<p> This function will extract the part of the name of the Certificate subject specified by the given OID. The output, if the raw flag is not used, will be encoded as described in RFC4514. Thus a string that is ASCII or UTF-8 encoded, depending on the certificate data. </p>
<p> Some helper macros with popular OIDs can be found in gnutls/x509.h If raw flag is (0), this function will only return known OIDs as text. Other OIDs will be DER encoded, as described in RFC4514 &#8212; in hex format with a &#8216;#&#8217; prefix. You can check about known OIDs using <code>gnutls_x509_dn_oid_known()</code>. </p>
<p> If <i>buf</i> is null then only the size will be filled. If the <i>raw_flag</i> is not specified the output is always null terminated, although the<br />
&nbsp;<wbr><i>buf_size</i>&nbsp;<wbr>will not include the null character.</p>
<h2>RETURNS</h2>
<p> <code>GNUTLS_E_SHORT_MEMORY_BUFFER</code> if the provided buffer is not long enough, and in that case the <i>buf_size</i> will be updated with the required size. <code>GNUTLS_E_REQUESTED_DATA_NOT_AVAILABLE</code> if there are no data in the current index. On success 0 is returned.</p>
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
