---

title: "gnutls_ocsp_resp_get_signature(3)"
name: "gnutls_ocsp_resp_get_signature"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_ocsp_resp_get_signature/"
---

<p> gnutls_ocsp_resp_get_signature - API function  </p>

<p> <code>#include &lt;gnutls/ocsp.h&gt;</code> </p>
<p> <code>int gnutls_ocsp_resp_get_signature(gnutls_ocsp_resp_t </code><i>resp</i><code>, gnutls_datum_t * </code><i>sig</i><code>);</code>  </p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_ocsp_resp_t resp</dt>
<dd> <p> should contain a <code>gnutls_ocsp_resp_t</code> structure </p>
 </dd>
<dt>gnutls_datum_t * sig</dt>
<dd> <p> newly allocated output buffer with signature data </p>
 </dd></dl>
<h2>DESCRIPTION</h2>
<p> This function will extract the signature field of a OCSP response.  </p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, otherwise a negative error value.  </p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;bugs [at] gnutls.org&gt;. <br/>
 Home page: <a rel="nofollow" href="http://www.gnutls.org">http://www.gnutls.org</a> </p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2001-2014 Free Software Foundation, Inc.. <br/>
 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.  </p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>gnutls</code> is maintained as a Texinfo manual. If the /usr/share/doc/gnutls/ directory does not contain the HTML form visit <code> </p>
<dl>
<dt><a rel="nofollow" href="http://www.gnutls.org/manual/">http://www.gnutls.org/manual/</a></dt>
<dd> <p> </code> </p>
 </dd></dl>
