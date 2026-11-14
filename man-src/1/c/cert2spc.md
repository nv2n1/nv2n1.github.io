---
title: "cert2spc(1)"
name: "cert2spc"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cert2spc/"
description: "cert2spc – Transform multiple X.509 certificates to a Software Publisher Certificate"
---

<h2>NAME</h2>
<p> cert2spc &#8211; Transform multiple X.509 certificates to a Software Publisher Certificate</p>
<h2>SYNOPSIS</h2>
<p> <code>cert2spc certificate|crl [certificate|crl &#8230;] outputfile.spc</code></p>
<h2>DESCRIPTION</h2>
<p> Combine a list of X.509 certificates or X.509 CRL (Certificate Revocation List) into a Software Publisher Certificate (PKCS#7 file). The SPC file is required for signing a PE file (like an assembly) using signcode.</p>
<h2>PARAMETERS</h2>
<dl>
<dt><i>certificate</i></p>
<dd> One (or more) X.509 certificate to add (space separated).</p>
<dt><i>crl</i></p>
<dd> One (or more) X.509 CRL to add (space separated).</p>
<dt><i>output.spc</i></p>
<dd> Software Publisher Certificate to output. If the specified file exists it will be overwritten.</dl>
<h2>AUTHOR</h2>
<p> Written by Sebastien Pouliot</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2002, 2003 Motus Technologies. Released under BSD license.</p>
<h2>MAILING LISTS</h2>
<p> Visit <a rel="nofollow" href="http://lists.ximian.com/mailman/listinfo/mono-devel-list">http://lists.ximian.com/mailman/listinfo/mono-devel-list</a> for details.</p>
<h2>WEB SITE</h2>
<p> Visit <a rel="nofollow" href="http://www.mono-project.com">http://www.mono-project.com</a> for details</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-makecert/">makecert</a>(1),</code><a href="/docs/linux/man/1-signcode/">signcode</a>(1) </p>
<h2>Index</h2>
