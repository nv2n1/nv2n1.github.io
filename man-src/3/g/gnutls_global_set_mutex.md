---
title: "gnutls_global_set_mutex(3)"
name: "gnutls_global_set_mutex"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_global_set_mutex/"
description: "gnutls_global_set_mutex – API function"
---

<h2>NAME</h2>
<p> gnutls_global_set_mutex &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>void gnutls_global_set_mutex(mutex_init_func </code><i>init</i><code>, mutex_deinit_func </code><i>deinit</i><code>, mutex_lock_func </code><i>lock</i><code>, mutex_unlock_func </code><i>unlock</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>mutex_init_func init</p>
<dd> mutex initialization function</p>
<dt>mutex_deinit_func deinit</p>
<dd> mutex deinitialization function</p>
<dt>mutex_lock_func lock</p>
<dd> mutex locking function</p>
<dt>mutex_unlock_func unlock</p>
<dd> mutex unlocking function</dl>
<h2>DESCRIPTION</h2>
<p> With this function you are allowed to override the default mutex locks used in some parts of gnutls and dependent libraries. This function should be used if you have complete control of your program and libraries. Do not call this function from a library, or preferrably from any application unless really needed to. GnuTLS will use the appropriate locks for the running system. </p>
<p> This function must be called prior to any other gnutls function.</p>
<h2>SINCE</h2>
<p> 2.12.0</p>
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
