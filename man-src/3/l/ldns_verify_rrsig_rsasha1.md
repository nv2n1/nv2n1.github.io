---
title: "ldns_verify_rrsig_rsasha1(3)"
name: "ldns_verify_rrsig_rsasha1"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldns_verify_rrsig_rsasha1/"
description: "ldns_verify_rrsig_dsa, ldns_verify_rrsig_rsasha1, ldns_verify_rrsig_rsamd5"
---

<h2>NAME</h2>
<p> ldns_verify_rrsig_dsa, ldns_verify_rrsig_rsasha1, ldns_verify_rrsig_rsamd5 </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;stdint.h&gt;<br />
 #include &lt;stdbool.h&gt; </p>
<p> #include &lt;ldns/ldns.h&gt; </p>
<p> ldns_status ldns_verify_rrsig_dsa(ldns_buffer *sig, ldns_buffer *rrset, ldns_buffer *key); </p>
<p> ldns_status ldns_verify_rrsig_rsasha1(ldns_buffer *sig, ldns_buffer *rrset, ldns_buffer *key); </p>
<p> ldns_status ldns_verify_rrsig_rsamd5(ldns_buffer *sig, ldns_buffer *rrset, ldns_buffer *key); </p>
<h2>DESCRIPTION</h2>
<dl>
<dt> <i>ldns_verify_rrsig_dsa</i>()</p>
<dd>verifies a buffer with signature data (DSA) for a buffer with rrset data with a buffer with key data. </p>
<p> .br <code>sig</code>: the signature data .br <code>rrset</code>: the rrset data, sorted and processed for verification .br <code>key</code>: the key data</dl>
<dl>
<dt> <i>ldns_verify_rrsig_rsasha1</i>()</p>
<dd>verifies a buffer with signature data (RSASHA1) for a buffer with rrset data with a buffer with key data. </p>
<p> .br <code>sig</code>: the signature data .br <code>rrset</code>: the rrset data, sorted and processed for verification .br <code>key</code>: the key data</dl>
<dl>
<dt> <i>ldns_verify_rrsig_rsamd5</i>()</p>
<dd>verifies a buffer with signature data (RSAMD5) for a buffer with rrset data with a buffer with key data. </p>
<p> .br <code>sig</code>: the signature data .br <code>rrset</code>: the rrset data, sorted and processed for verification .br <code>key</code>: the key data</dl>
<h2>AUTHOR</h2>
<p> The ldns team at NLnet Labs. Which consists out of Jelte Jansen and Miek Gieben. </p>
<h2>REPORTING BUGS</h2>
<p> Please report bugs to ldns-team [at] nlnetlabs.nl or in our bugzilla at <a rel="nofollow" href="http://www.nlnetlabs.nl/bugs/index.html">http://www.nlnetlabs.nl/bugs/index.html</a> </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2004 &#8211; 2006 NLnet Labs. </p>
<p> Licensed under the BSD License. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>SEE ALSO</h2>
<p> <i>ldns_key</i>, <i>ldns_sign_public</i>, <i>ldns_zone_sign</i>, <i>ldns_verify</i>, <i>ldns_verify_rrsig</i>. And <code>perldoc Net::DNS</code>, <code>RFC1034</code>, <code>RFC1035</code>, <code>RFC4033</code>, <code>RFC4034</code> and <code>RFC4035</code>.</p>
<h2>REMARKS</h2>
<p> This manpage was automaticly generated from the ldns source code by use of Doxygen and some perl. </p>
<h2>Index</h2>
