---
title: "ldns_rr_dnskey_protocol(3)"
name: "ldns_rr_dnskey_protocol"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldns_rr_dnskey_protocol/"
description: "ldns_rr_dnskey_flags, ldns_rr_dnskey_set_flags, ldns_rr_dnskey_protocol, ldns_rr_dnskey_set_protocol, ldns_rr_dnskey_algorithm, ldns_rr_dnskey_set_algorithm, ldns_rr_dnskey_key, ldns_rr_dnskey_set_key"
---

<h2>NAME</h2>
<p> ldns_rr_dnskey_flags, ldns_rr_dnskey_set_flags, ldns_rr_dnskey_protocol, ldns_rr_dnskey_set_protocol, ldns_rr_dnskey_algorithm, ldns_rr_dnskey_set_algorithm, ldns_rr_dnskey_key, ldns_rr_dnskey_set_key </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;stdint.h&gt;<br />
 #include &lt;stdbool.h&gt; </p>
<p> #include &lt;ldns/ldns.h&gt; </p>
<p> ldns_rdf* ldns_rr_dnskey_flags(const ldns_rr *r); </p>
<p> bool ldns_rr_dnskey_set_flags(ldns_rr *r, ldns_rdf *f); </p>
<p> ldns_rdf* ldns_rr_dnskey_protocol(const ldns_rr *r); </p>
<p> bool ldns_rr_dnskey_set_protocol(ldns_rr *r, ldns_rdf *f); </p>
<p> ldns_rdf* ldns_rr_dnskey_algorithm(const ldns_rr *r); </p>
<p> bool ldns_rr_dnskey_set_algorithm(ldns_rr *r, ldns_rdf *f); </p>
<p> ldns_rdf* ldns_rr_dnskey_key(const ldns_rr *r); </p>
<p> bool ldns_rr_dnskey_set_key(ldns_rr *r, ldns_rdf *f); </p>
<h2>DESCRIPTION</h2>
<dl>
<dt> <i>ldns_rr_dnskey_flags</i>()</p>
<dd>returns the flags of a LDNS_RR_TYPE_DNSKEY rr .br <code>r</code>: the resource record .br Returns a ldns_rdf* with the flags or NULL on failure</dl>
<dl>
<dt> <i>ldns_rr_dnskey_set_flags</i>()</p>
<dd>sets the flags of a LDNS_RR_TYPE_DNSKEY rr .br <code>r</code>: the rr to use .br <code>f</code>: the flags to set .br Returns true on success, false otherwise</dl>
<dl>
<dt> <i>ldns_rr_dnskey_protocol</i>()</p>
<dd>returns the protocol of a LDNS_RR_TYPE_DNSKEY rr .br <code>r</code>: the resource record .br Returns a ldns_rdf* with the protocol or NULL on failure</dl>
<dl>
<dt> <i>ldns_rr_dnskey_set_protocol</i>()</p>
<dd>sets the protocol of a LDNS_RR_TYPE_DNSKEY rr .br <code>r</code>: the rr to use .br <code>f</code>: the protocol to set .br Returns true on success, false otherwise</dl>
<dl>
<dt> <i>ldns_rr_dnskey_algorithm</i>()</p>
<dd>returns the algorithm of a LDNS_RR_TYPE_DNSKEY rr .br <code>r</code>: the resource record .br Returns a ldns_rdf* with the algorithm or NULL on failure</dl>
<dl>
<dt> <i>ldns_rr_dnskey_set_algorithm</i>()</p>
<dd>sets the algorithm of a LDNS_RR_TYPE_DNSKEY rr .br <code>r</code>: the rr to use .br <code>f</code>: the algorithm to set .br Returns true on success, false otherwise</dl>
<dl>
<dt> <i>ldns_rr_dnskey_key</i>()</p>
<dd>returns the key data of a LDNS_RR_TYPE_DNSKEY rr .br <code>r</code>: the resource record .br Returns a ldns_rdf* with the key data or NULL on failure</dl>
<dl>
<dt> <i>ldns_rr_dnskey_set_key</i>()</p>
<dd>sets the key data of a LDNS_RR_TYPE_DNSKEY rr .br <code>r</code>: the rr to use .br <code>f</code>: the key data to set .br Returns true on success, false otherwise</dl>
<h2>AUTHOR</h2>
<p> The ldns team at NLnet Labs. Which consists out of Jelte Jansen and Miek Gieben. </p>
<h2>REPORTING BUGS</h2>
<p> Please report bugs to ldns-team [at] nlnetlabs.nl or in our bugzilla at <a rel="nofollow" href="http://www.nlnetlabs.nl/bugs/index.html">http://www.nlnetlabs.nl/bugs/index.html</a> </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2004 &#8211; 2006 NLnet Labs. </p>
<p> Licensed under the BSD License. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>SEE ALSO</h2>
<p> <i>ldns_rr</i>. And <code>perldoc Net::DNS</code>, <code>RFC1034</code>, <code>RFC1035</code>, <code>RFC4033</code>, <code>RFC4034</code> and <code>RFC4035</code>.</p>
<h2>REMARKS</h2>
<p> This manpage was automaticly generated from the ldns source code by use of Doxygen and some perl. </p>
<h2>Index</h2>
