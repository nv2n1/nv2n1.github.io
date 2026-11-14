---
title: "gnutls_x509_crt_get_authority_info_access(3)"
name: "gnutls_x509_crt_get_authority_info_access"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_crt_get_authority_info_access/"
description: "gnutls_x509_crt_get_authority_info_access – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_crt_get_authority_info_access &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509.h&gt;</code> </p>
<p> <code>int gnutls_x509_crt_get_authority_info_access(gnutls_x509_crt_t </code><i>crt</i><code>, unsigned int </code><i>seq</i><code>, int </code><i>what</i><code>, gnutls_datum_t * </code><i>data</i><code>, unsigned int * </code><i>critical</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_x509_crt_t crt</p>
<dd> Holds the certificate</p>
<dt>unsigned int seq</p>
<dd> specifies the sequence number of the access descriptor (0 for the first one, 1 for the second etc.)</p>
<dt>int what</p>
<dd> what data to get, a <code>gnutls_info_access_what_t</code> type.</p>
<dt>gnutls_datum_t * data</p>
<dd> output data to be freed with <code>gnutls_free()</code>.</p>
<dt>unsigned int * critical</p>
<dd> pointer to output integer that is set to non-zero if the extension is marked as critical (may be <code>NULL</code>)</dl>
<h2>DESCRIPTION</h2>
<p> Note that a simpler API to access the authority info data is provided by <code>gnutls_x509_aia_get()</code> and <code>gnutls_x509_ext_import_aia()</code>. </p>
<p> This function extracts the Authority Information Access (AIA) extension, see RFC 5280 section 4.2.2.1 for more information. The AIA extension holds a sequence of AccessDescription (AD) data. </p>
<p> The <i>seq</i> input parameter is used to indicate which member of the sequence the caller is interested in. The first member is 0, the second member 1 and so on. When the <i>seq</i> value is out of bounds, <code>GNUTLS_E_REQUESTED_DATA_NOT_AVAILABLE</code> is returned. </p>
<p> The type of data returned in <i>data</i> is specified via <i>what</i> which should be <code>gnutls_info_access_what_t</code> values. </p>
<p> If <i>what</i> is <code>GNUTLS_IA_ACCESSMETHOD_OID</code> then <i>data</i> will hold the accessMethod OID (e.g., &quot;1.3.6.1.5.5.7.48.1&quot;). </p>
<p> If <i>what</i> is <code>GNUTLS_IA_ACCESSLOCATION_GENERALNAME_TYPE</code>, <i>data</i> will hold the accessLocation GeneralName type (e.g., &quot;uniformResourceIdentifier&quot;). </p>
<p> If <i>what</i> is <code>GNUTLS_IA_URI</code>, <i>data</i> will hold the accessLocation URI data. Requesting this <i>what</i> value leads to an error if the accessLocation is not of the &quot;uniformResourceIdentifier&quot; type. </p>
<p> If <i>what</i> is <code>GNUTLS_IA_OCSP_URI</code>, <i>data</i> will hold the OCSP URI. Requesting this <i>what</i> value leads to an error if the accessMethod is not 1.3.6.1.5.5.7.48.1 aka OSCP, or if accessLocation is not of the &quot;uniformResourceIdentifier&quot; type. In that case <code>GNUTLS_E_UNKNOWN_ALGORITHM</code> will be returned, and <i>seq</i> should be increased and this function called again. </p>
<p> If <i>what</i> is <code>GNUTLS_IA_CAISSUERS_URI</code>, <i>data</i> will hold the caIssuers URI. Requesting this <i>what</i> value leads to an error if the accessMethod is not 1.3.6.1.5.5.7.48.2 aka caIssuers, or if accessLocation is not of the &quot;uniformResourceIdentifier&quot; type. In that case handle as in <code>GNUTLS_IA_OCSP_URI</code>. </p>
<p> More <i>what</i> values may be allocated in the future as needed. </p>
<p> If <i>data</i> is NULL, the function does the same without storing the output data, that is, it will set <i>critical</i> and do error checking as usual. </p>
<p> The value of the critical flag is returned in * <i>critical</i> . Supply a NULL <i>critical</i> if you want the function to make sure the extension is non-critical, as required by RFC 5280.</p>
<h2>RETURNS</h2>
<p> <code>GNUTLS_E_SUCCESS</code> on success, <code>GNUTLS_E_INVALID_REQUEST</code> on invalid <i>crt</i> , <code>GNUTLS_E_CONSTRAINT_ERROR</code> if the extension is incorrectly marked as critical (use a non-NULL <i>critical</i> to override), <code>GNUTLS_E_UNKNOWN_ALGORITHM</code> if the requested OID does not match (e.g., when using <code>GNUTLS_IA_OCSP_URI</code>), otherwise a negative error code.</p>
<h2>SINCE</h2>
<p> 3.0</p>
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
