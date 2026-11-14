---
title: "gnutls_global_init(3)"
name: "gnutls_global_init"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_global_init/"
description: "gnutls_global_init – API function"
---

<h2>NAME</h2>
<p> gnutls_global_init &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>int gnutls_global_init( </code><i>void</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt> void</p>
<dd></dl>
<h2>DESCRIPTION</h2>
<p> This function performs any required precalculations, detects the supported CPU capabilities and initializes the underlying cryptographic backend. In order to free any resources taken by this call you should <code>gnutls_global_deinit()</code> when gnutls usage is no longer needed. </p>
<p> This function increments a global counter, so that <code>gnutls_global_deinit()</code> only releases resources when it has been called as many times as <code>gnutls_global_init()</code>. This is useful when GnuTLS is used by more than one library in an application. This function can be called many times, but will only do something the first time. </p>
<p> Since GnuTLS 3.3.0 this function is only required in systems that do not support library constructors and static linking. This function also became thread safe. </p>
<p> A subsequent call of this function if the initial has failed will return the same error code.</p>
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
