---
title: "ldns_key_algorithm(3)"
name: "ldns_key_algorithm"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldns_key_algorithm/"
description: "ldns_key_rsa_key, ldns_key_dsa_key, ldns_key_algorithm, ldns_key_hmac_key"
---

<h2>NAME</h2>
<p> ldns_key_rsa_key, ldns_key_dsa_key, ldns_key_algorithm, ldns_key_hmac_key </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;stdint.h&gt;<br />
 #include &lt;stdbool.h&gt; </p>
<p> #include &lt;ldns/ldns.h&gt; </p>
<p> RSA* ldns_key_rsa_key(const ldns_key *k); </p>
<p> DSA* ldns_key_dsa_key(const ldns_key *k); </p>
<p> ldns_signing_algorithm ldns_key_algorithm(const ldns_key *k); </p>
<p> unsigned char* ldns_key_hmac_key(const ldns_key *k); </p>
<h2>DESCRIPTION</h2>
<dl>
<dt> <i>ldns_key_rsa_key</i>()</p>
<dd>returns the (openssl) RSA struct contained in the key .br <code>k</code>: the key to look in .br Returns the RSA * structure in the key</dl>
<dl>
<dt> <i>ldns_key_dsa_key</i>()</p>
<dd>returns the (openssl) DSA struct contained in the key</dl>
<dl>
<dt> <i>ldns_key_algorithm</i>()</p>
<dd>return the signing alg of the key .br <code>k</code>: the key .br Returns the algorithm</dl>
<dl>
<dt> <i>ldns_key_hmac_key</i>()</p>
<dd>return the hmac key data .br <code>k</code>: the key .br Returns the hmac key data</dl>
<h2>AUTHOR</h2>
<p> The ldns team at NLnet Labs. Which consists out of Jelte Jansen and Miek Gieben. </p>
<h2>REPORTING BUGS</h2>
<p> Please report bugs to ldns-team [at] nlnetlabs.nl or in our bugzilla at <a rel="nofollow" href="http://www.nlnetlabs.nl/bugs/index.html">http://www.nlnetlabs.nl/bugs/index.html</a> </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2004 &#8211; 2006 NLnet Labs. </p>
<p> Licensed under the BSD License. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>SEE ALSO</h2>
<p> <i>ldns_key_list</i>, <i>ldns_key</i>. And <code>perldoc Net::DNS</code>, <code>RFC1034</code>, <code>RFC1035</code>, <code>RFC4033</code>, <code>RFC4034</code> and <code>RFC4035</code>.</p>
<h2>REMARKS</h2>
<p> This manpage was automaticly generated from the ldns source code by use of Doxygen and some perl. </p>
<h2>Index</h2>
