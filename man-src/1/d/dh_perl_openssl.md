---
title: "dh_perl_openssl(1)"
name: "dh_perl_openssl"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dh_perl_openssl/"
description: "dh_perl_openssl – add dependencies required for OpenSSL modules"
---

<h2 class="name">NAME</h2>
<p> dh_perl_openssl &#8211; add dependencies required for OpenSSL modules </p>
<h2>SYNOPSIS</h2>
<p> <code>dh_perl_openssl</code> [<i>debhelper options</i>]</p>
<h2>DESCRIPTION</h2>
<p> dh_perl_openssl is a debhelper program that is responsible for adding a dependency on perl-openssl-abi-* to the ${perl:Depends} substitution variable. Such a dependency is needed for packages that expose the OpenSSL binary interface to Perl code, such as pointers to <tt>&quot;SSL_CTX&quot;</tt> structs. </p>
<p> A debhelper addon is also provided. This makes it possible to just use </p>
<pre>
  #!/usr/bin/make -f
  %:
          dh $@ --with perl_openssl
</pre>
<p> for <i>debian/rules</i>. </p>
<p> Alternatively, since perl-openssl-defaults/4 you can just build depend on <code>dh-sequence-perl-openssl</code> and omit the <tt>&quot;--with perl_openssl&quot;</tt> part.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-debhelper/">debhelper</a></code>(7) </p>
<p> &lt;<a rel="nofollow" href="http://bugs.debian.org/848113">http://bugs.debian.org/848113</a>&gt;</p>
<h2>COPYRIGHT AND LICENSE</h2>
<p> Based on <i>dh_perl_dbi</i> in the <i>libdbi-perl</i> package by Angar Buchardt. </p>
<p> Copyright 2010, Ansgar Burchardt &lt;ansgar [at] debian.org&gt; </p>
<p> Copyright 2016, Niko Tyni &lt;ntyni [at] debian.org&gt; </p>
<p> This program is free software, you can redistribute it and/or modify it under the same terms as Perl itself. </p>
<h2>Index</h2>
