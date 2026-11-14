---
title: "ldns_rr_rrsig_algorithm(3)"
name: "ldns_rr_rrsig_algorithm"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldns_rr_rrsig_algorithm/"
description: "ldns_rr_rrsig_typecovered, ldns_rr_rrsig_set_typecovered, ldns_rr_rrsig_algorithm, ldns_rr_rrsig_set_algorithm, ldns_rr_rrsig_labels, ldns_rr_rrsig_set_labels, ldns_rr_rrsig_origttl, ldns_rr_rrsig_..."
---

<h2>NAME</h2>
<p> ldns_rr_rrsig_typecovered, ldns_rr_rrsig_set_typecovered, ldns_rr_rrsig_algorithm, ldns_rr_rrsig_set_algorithm, ldns_rr_rrsig_labels, ldns_rr_rrsig_set_labels, ldns_rr_rrsig_origttl, ldns_rr_rrsig_set_origttl, ldns_rr_rrsig_expiration, ldns_rr_rrsig_set_expiration, ldns_rr_rrsig_inception, ldns_rr_rrsig_set_inception, ldns_rr_rrsig_keytag, ldns_rr_rrsig_set_keytag, ldns_rr_rrsig_signame, ldns_rr_rrsig_set_signame, ldns_rr_rrsig_sig, ldns_rr_rrsig_set_sig </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;stdint.h&gt;<br />
 #include &lt;stdbool.h&gt; </p>
<p> #include &lt;ldns/ldns.h&gt; </p>
<p> ldns_rdf* ldns_rr_rrsig_typecovered(const ldns_rr *r); </p>
<p> bool ldns_rr_rrsig_set_typecovered(ldns_rr *r, ldns_rdf *f); </p>
<p> ldns_rdf* ldns_rr_rrsig_algorithm(const ldns_rr *r); </p>
<p> bool ldns_rr_rrsig_set_algorithm(ldns_rr *r, ldns_rdf *f); </p>
<p> ldns_rdf* ldns_rr_rrsig_labels(const ldns_rr *r); </p>
<p> bool ldns_rr_rrsig_set_labels(ldns_rr *r, ldns_rdf *f); </p>
<p> ldns_rdf* ldns_rr_rrsig_origttl(const ldns_rr *r); </p>
<p> bool ldns_rr_rrsig_set_origttl(ldns_rr *r, ldns_rdf *f); </p>
<p> ldns_rdf* ldns_rr_rrsig_expiration(const ldns_rr *r); </p>
<p> bool ldns_rr_rrsig_set_expiration(ldns_rr *r, ldns_rdf *f); </p>
<p> ldns_rdf* ldns_rr_rrsig_inception(const ldns_rr *r); </p>
<p> bool ldns_rr_rrsig_set_inception(ldns_rr *r, ldns_rdf *f); </p>
<p> ldns_rdf* ldns_rr_rrsig_keytag(const ldns_rr *r); </p>
<p> bool ldns_rr_rrsig_set_keytag(ldns_rr *r, ldns_rdf *f); </p>
<p> ldns_rdf* ldns_rr_rrsig_signame(const ldns_rr *r); </p>
<p> bool ldns_rr_rrsig_set_signame(ldns_rr *r, ldns_rdf *f); </p>
<p> ldns_rdf* ldns_rr_rrsig_sig(const ldns_rr *r); </p>
<p> bool ldns_rr_rrsig_set_sig(ldns_rr *r, ldns_rdf *f); </p>
<h2>DESCRIPTION</h2>
<dl>
<dt> <i>ldns_rr_rrsig_typecovered</i>()</p>
<dd>returns the type covered of a LDNS_RR_TYPE_RRSIG rr .br <code>r</code>: the resource record .br Returns a ldns_rdf* with the type covered or NULL on failure</dl>
<dl>
<dt> <i>ldns_rr_rrsig_set_typecovered</i>()</p>
<dd>sets the typecovered of a LDNS_RR_TYPE_RRSIG rr .br <code>r</code>: the rr to use .br <code>f</code>: the typecovered to set .br Returns true on success, false otherwise</dl>
<dl>
<dt> <i>ldns_rr_rrsig_algorithm</i>()</p>
<dd>returns the algorithm of a LDNS_RR_TYPE_RRSIG RR .br <code>r</code>: the resource record .br Returns a ldns_rdf* with the algorithm or NULL on failure</dl>
<dl>
<dt> <i>ldns_rr_rrsig_set_algorithm</i>()</p>
<dd>sets the algorithm of a LDNS_RR_TYPE_RRSIG rr .br <code>r</code>: the rr to use .br <code>f</code>: the algorithm to set .br Returns true on success, false otherwise</dl>
<dl>
<dt> <i>ldns_rr_rrsig_labels</i>()</p>
<dd>returns the number of labels of a LDNS_RR_TYPE_RRSIG RR .br <code>r</code>: the resource record .br Returns a ldns_rdf* with the number of labels or NULL on failure</dl>
<dl>
<dt> <i>ldns_rr_rrsig_set_labels</i>()</p>
<dd>sets the number of labels of a LDNS_RR_TYPE_RRSIG rr .br <code>r</code>: the rr to use .br <code>f</code>: the number of labels to set .br Returns true on success, false otherwise</dl>
<dl>
<dt> <i>ldns_rr_rrsig_origttl</i>()</p>
<dd>returns the original TTL of a LDNS_RR_TYPE_RRSIG RR .br <code>r</code>: the resource record .br Returns a ldns_rdf* with the original TTL or NULL on failure</dl>
<dl>
<dt> <i>ldns_rr_rrsig_set_origttl</i>()</p>
<dd>sets the original TTL of a LDNS_RR_TYPE_RRSIG rr .br <code>r</code>: the rr to use .br <code>f</code>: the original TTL to set .br Returns true on success, false otherwise</dl>
<dl>
<dt> <i>ldns_rr_rrsig_expiration</i>()</p>
<dd>returns the expiration time of a LDNS_RR_TYPE_RRSIG RR .br <code>r</code>: the resource record .br Returns a ldns_rdf* with the expiration time or NULL on failure</dl>
<dl>
<dt> <i>ldns_rr_rrsig_set_expiration</i>()</p>
<dd>sets the expireation date of a LDNS_RR_TYPE_RRSIG rr .br <code>r</code>: the rr to use .br <code>f</code>: the expireation date to set .br Returns true on success, false otherwise</dl>
<dl>
<dt> <i>ldns_rr_rrsig_inception</i>()</p>
<dd>returns the inception time of a LDNS_RR_TYPE_RRSIG RR .br <code>r</code>: the resource record .br Returns a ldns_rdf* with the inception time or NULL on failure</dl>
<dl>
<dt> <i>ldns_rr_rrsig_set_inception</i>()</p>
<dd>sets the inception date of a LDNS_RR_TYPE_RRSIG rr .br <code>r</code>: the rr to use .br <code>f</code>: the inception date to set .br Returns true on success, false otherwise</dl>
<dl>
<dt> <i>ldns_rr_rrsig_keytag</i>()</p>
<dd>returns the keytag of a LDNS_RR_TYPE_RRSIG RR .br <code>r</code>: the resource record .br Returns a ldns_rdf* with the keytag or NULL on failure</dl>
<dl>
<dt> <i>ldns_rr_rrsig_set_keytag</i>()</p>
<dd>sets the keytag of a LDNS_RR_TYPE_RRSIG rr .br <code>r</code>: the rr to use .br <code>f</code>: the keytag to set .br Returns true on success, false otherwise</dl>
<dl>
<dt> <i>ldns_rr_rrsig_signame</i>()</p>
<dd>returns the signers name of a LDNS_RR_TYPE_RRSIG RR .br <code>r</code>: the resource record .br Returns a ldns_rdf* with the signers name or NULL on failure</dl>
<dl>
<dt> <i>ldns_rr_rrsig_set_signame</i>()</p>
<dd>sets the signers name of a LDNS_RR_TYPE_RRSIG rr .br <code>r</code>: the rr to use .br <code>f</code>: the signers name to set .br Returns true on success, false otherwise</dl>
<dl>
<dt> <i>ldns_rr_rrsig_sig</i>()</p>
<dd>returns the signature data of a LDNS_RR_TYPE_RRSIG RR .br <code>r</code>: the resource record .br Returns a ldns_rdf* with the signature data or NULL on failure</dl>
<dl>
<dt> <i>ldns_rr_rrsig_set_sig</i>()</p>
<dd>sets the signature data of a LDNS_RR_TYPE_RRSIG rr .br <code>r</code>: the rr to use .br <code>f</code>: the signature data to set .br Returns true on success, false otherwise</dl>
<h2>AUTHOR</h2>
<p> The ldns team at NLnet Labs. Which consists out of Jelte Jansen and Miek Gieben. </p>
<h2>REPORTING BUGS</h2>
<p> Please report bugs to ldns-team [at] nlnetlabs.nl or in our bugzilla at <a rel="nofollow" href="http://www.nlnetlabs.nl/bugs/index.html">http://www.nlnetlabs.nl/bugs/index.html</a> </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2004 &#8211; 2006 NLnet Labs. </p>
<p> Licensed under the BSD License. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>SEE ALSO</h2>
<p> <code>perldoc Net::DNS</code>, <code>RFC1034</code>, <code>RFC1035</code>, <code>RFC4033</code>, <code>RFC4034</code> and <code>RFC4035</code>.</p>
<h2>REMARKS</h2>
<p> This manpage was automaticly generated from the ldns source code by use of Doxygen and some perl. </p>
<h2>Index</h2>
