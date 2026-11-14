---
title: "gnutls_openpgp_crt_export-2(3)"
name: "gnutls_openpgp_crt_export-2"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_openpgp_crt_export-2/"
---

gnutls_openpgp_crt_export - API function
<h2>Synopsis</h2><b>#include &lt;gnutls/openpgp.h&gt;</b> 

 <b>int gnutls_openpgp_crt_export(gnutls_openpgp_crt_t </b><i>key</i><b>, gnutls_openpgp_crt_fmt_t </b><i>format</i><b>, void * </b><i>output_data</i><b>, size_t * </b><i>output_data_size</i><b>);</b>
<h2>Arguments</h2><dl COMPACT><dt>gnutls_openpgp_crt_t key
<dd>Holds the key.
<dt>gnutls_openpgp_crt_fmt_t format
<dd>One of gnutls_openpgp_crt_fmt_t elements.
<dt>void * output_data
<dd>will contain the raw or base64 encoded key
<dt>size_t * output_data_size
<dd>holds the size of output_data (and will be replaced by the actual size of parameters)</dl><h2>Description</h2>This function will convert the given key to RAW or Base64 format. If the buffer provided is not long enough to hold the output, then <b>GNUTLS_E_SHORT_MEMORY_BUFFER</b> will be returned.
<h2>Returns</h2><b>GNUTLS_E_SUCCESS</b> on success, or an error code.
<h2>Reporting Bugs</h2>Report bugs to &lt;bugs [at] gnutls.org&gt;. 
 Home page: <a rel="nofollow" HREF="http://www.gnutls.org">http://www.gnutls.org</a> 

<h2>Copyright</h2>Copyright &#169; 2001-2014 Free Software Foundation, Inc.. 
 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.
<h2>See Also</h2>The full documentation for <b>gnutls</b> is maintained as a Texinfo manual. If the /usr/share/doc/gnutls/ directory does not contain the HTML form visit <b>
<dl COMPACT><dt><a rel="nofollow" HREF="http://www.gnutls.org/manual/">http://www.gnutls.org/manual/</a>
<dd></b></dl>
