---

title: "gnutls_x509_crt_set_proxy_dn(3)"
name: "gnutls_x509_crt_set_proxy_dn"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_crt_set_proxy_dn/"
description: "gnutls_x509_crt_set_proxy_dn – API function"
---

<p> gnutls_x509_crt_set_proxy_dn &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509.h&gt;</code> </p>
<p> <code>int gnutls_x509_crt_set_proxy_dn(gnutls_x509_crt_t </code><i>crt</i><code>, gnutls_x509_crt_t </code><i>eecrt</i><code>, unsigned int </code><i>raw_flag</i><code>, const void * </code><i>name</i><code>, unsigned int </code><i>sizeof_name</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_x509_crt_t crt</dt>
<dd> a gnutls_x509_crt_t structure with the new proxy cert</dd>
<dt>gnutls_x509_crt_t eecrt</dt>
<dd> the end entity certificate that will be issuing the proxy</dd>
<dt>unsigned int raw_flag</dt>
<dd> must be 0, or 1 if the CN is DER encoded</dd>
<dt>const void * name</dt>
<dd> a pointer to the CN name, may be NULL (but MUST then be added later)</dd>
<dt>unsigned int sizeof_name</dt>
<dd> holds the size of <i>name</i></dd></dl>
<h2>DESCRIPTION</h2>
<p> This function will set the subject in <i>crt</i> to the end entity&#8217;s<br/>
&nbsp;<wbr><i>eecrt</i>&nbsp;<wbr>subject name, and add a single Common Name component&nbsp;<wbr>&nbsp;<wbr><i>name</i>&nbsp;<wbr>of size&nbsp;<wbr>&nbsp;<wbr><i>sizeof_name</i>&nbsp;<wbr>.&nbsp;<wbr>&nbsp;<wbr>This corresponds to the required proxy certificate naming style. Note that if <i>name</i> is <code>NULL</code>, you MUST set it later by using <code>gnutls_x509_crt_set_dn_by_oid()</code> or similar.</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, otherwise a negative error value.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;bugs [at] gnutls.org&gt;.<br/>
 Home page: <a rel="nofollow" href="http://www.gnutls.org">http://www.gnutls.org</a> </p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2001-2014 Free Software Foundation, Inc..<br/>
 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>gnutls</code> is maintained as a Texinfo manual. If the /usr/share/doc/gnutls/ directory does not contain the HTML form visit <code></p>
<dl>
<dt><a rel="nofollow" href="http://www.gnutls.org/manual/">http://www.gnutls.org/manual/</a></dt>
<dd> </code></dd></dl>
