---
title: "gnutls_load_file(3)"
name: "gnutls_load_file"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_load_file/"
description: "gnutls_load_file – API function"
---

<h2>NAME</h2>
<p> gnutls_load_file &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>int gnutls_load_file(const char * </code><i>filename</i><code>, gnutls_datum_t * </code><i>data</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>const char * filename</p>
<dd> the name of the file to load</p>
<dt>gnutls_datum_t * data</p>
<dd> Where the file will be stored</dl>
<h2>DESCRIPTION</h2>
<p> This function will load a file into a datum. The data are zero terminated but the terminating null is not included in length. The returned data are allocated using <code>gnutls_malloc()</code>.</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, otherwise an error code is returned. </p>
<p> Since 3.1.0</p>
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
