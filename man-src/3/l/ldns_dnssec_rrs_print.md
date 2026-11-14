---
title: "ldns_dnssec_rrs_print(3)"
name: "ldns_dnssec_rrs_print"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldns_dnssec_rrs_print/"
description: "ldns_dnssec_rrs_new, ldns_dnssec_rrs_free, ldns_dnssec_rrs_add_rr, ldns_dnssec_rrs_print"
---

<h2>NAME</h2>
<p> ldns_dnssec_rrs_new, ldns_dnssec_rrs_free, ldns_dnssec_rrs_add_rr, ldns_dnssec_rrs_print </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;stdint.h&gt;<br />
 #include &lt;stdbool.h&gt; </p>
<p> #include &lt;ldns/ldns.h&gt; </p>
<p>&nbsp;<wbr>ldns_dnssec_rrs_new(); </p>
<p> void ldns_dnssec_rrs_free(ldns_dnssec_rrs *rrs); </p>
<p> ldns_status ldns_dnssec_rrs_add_rr(ldns_dnssec_rrs *rrs, ldns_rr *rr); </p>
<p> void ldns_dnssec_rrs_print(FILE *out, ldns_dnssec_rrs *rrs); </p>
<h2>DESCRIPTION</h2>
<dl>
<dt> <i>ldns_dnssec_rrs_new</i>()</dl>
<dl>
<dt> <i>ldns_dnssec_rrs_free</i>()</p>
<dd>Frees the list of rrs, but *not* the individual ldns_rr records contained in the list </p>
<p> .br <code>rrs</code>: the data structure to free</dl>
<dl>
<dt> <i>ldns_dnssec_rrs_add_rr</i>()</p>
<dd>Adds an RR to the list of RRs. The list will remain ordered </p>
<p> .br <code>rrs</code>: the list to add to .br <code>rr</code>: the RR to add .br Returns LDNS_STATUS_OK on success</dl>
<dl>
<dt> <i>ldns_dnssec_rrs_print</i>()</p>
<dd>Prints the given rrs to the file descriptor </p>
<p> .br <code>out</code>: the file descriptor to print to .br <code>rrs</code>: the list of RRs to print</dl>
<h2>AUTHOR</h2>
<p> The ldns team at NLnet Labs. Which consists out of Jelte Jansen and Miek Gieben. </p>
<h2>REPORTING BUGS</h2>
<p> Please report bugs to ldns-team [at] nlnetlabs.nl or in our bugzilla at <a rel="nofollow" href="http://www.nlnetlabs.nl/bugs/index.html">http://www.nlnetlabs.nl/bugs/index.html</a> </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2004 &#8211; 2006 NLnet Labs. </p>
<p> Licensed under the BSD License. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>SEE ALSO</h2>
<p> <i>ldns_dnssec_zone</i>. And <code>perldoc Net::DNS</code>, <code>RFC1034</code>, <code>RFC1035</code>, <code>RFC4033</code>, <code>RFC4034</code> and <code>RFC4035</code>.</p>
<h2>REMARKS</h2>
<p> This manpage was automaticly generated from the ldns source code by use of Doxygen and some perl. </p>
<h2>Index</h2>
