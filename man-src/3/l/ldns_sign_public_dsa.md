---
title: "ldns_sign_public_dsa(3)"
name: "ldns_sign_public_dsa"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldns_sign_public_dsa/"
description: "ldns_sign_public_dsa, ldns_sign_public_rsamd5, ldns_sign_public_rsasha1"
---

<h2>NAME</h2>
<p> ldns_sign_public_dsa, ldns_sign_public_rsamd5, ldns_sign_public_rsasha1 </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;stdint.h&gt;<br />
 #include &lt;stdbool.h&gt; </p>
<p> #include &lt;ldns/ldns.h&gt; </p>
<p> ldns_rdf* ldns_sign_public_dsa(ldns_buffer *to_sign, DSA *key); </p>
<p> ldns_rdf* ldns_sign_public_rsamd5(ldns_buffer *to_sign, RSA *key); </p>
<p> ldns_rdf* ldns_sign_public_rsasha1(ldns_buffer *to_sign, RSA *key); </p>
<h2>DESCRIPTION</h2>
<dl>
<dt> <i>ldns_sign_public_dsa</i>()</p>
<dd>Sign a buffer with the DSA key (hash with SHA1) .br <code>to_sign</code>: buffer with the data .br <code>key</code>: the key to use .br Returns a ldns_rdf with the signed data</dl>
<dl>
<dt> <i>ldns_sign_public_rsamd5</i>()</p>
<dd>Sign a buffer with the RSA key (hash with MD5) .br <code>to_sign</code>: buffer with the data .br <code>key</code>: the key to use .br Returns a ldns_rdf with the signed data</dl>
<dl>
<dt> <i>ldns_sign_public_rsasha1</i>()</p>
<dd>Sign a buffer with the RSA key (hash with SHA1) .br <code>to_sign</code>: buffer with the data .br <code>key</code>: the key to use .br Returns a ldns_rdf with the signed data</dl>
<h2>AUTHOR</h2>
<p> The ldns team at NLnet Labs. Which consists out of Jelte Jansen and Miek Gieben. </p>
<h2>REPORTING BUGS</h2>
<p> Please report bugs to ldns-team [at] nlnetlabs.nl or in our bugzilla at <a rel="nofollow" href="http://www.nlnetlabs.nl/bugs/index.html">http://www.nlnetlabs.nl/bugs/index.html</a> </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2004 &#8211; 2006 NLnet Labs. </p>
<p> Licensed under the BSD License. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>SEE ALSO</h2>
<p> <i>ldns_sign_public</i>. And <code>perldoc Net::DNS</code>, <code>RFC1034</code>, <code>RFC1035</code>, <code>RFC4033</code>, <code>RFC4034</code> and <code>RFC4035</code>.</p>
<h2>REMARKS</h2>
<p> This manpage was automaticly generated from the ldns source code by use of Doxygen and some perl. </p>
<h2>Index</h2>
