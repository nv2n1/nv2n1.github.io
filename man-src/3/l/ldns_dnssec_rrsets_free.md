---
title: "ldns_dnssec_rrsets_free(3)"
name: "ldns_dnssec_rrsets_free"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldns_dnssec_rrsets_free/"
description: "ldns_dnssec_rrsets_new, ldns_dnssec_rrsets_free, ldns_dnssec_rrsets_type, ldns_dnssec_rrsets_set_type, ldns_dnssec_rrsets_add_rr, ldns_dnssec_rrsets_print"
---

<h2>NAME</h2>
<p> ldns_dnssec_rrsets_new, ldns_dnssec_rrsets_free, ldns_dnssec_rrsets_type, ldns_dnssec_rrsets_set_type, ldns_dnssec_rrsets_add_rr, ldns_dnssec_rrsets_print </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;stdint.h&gt;<br />
 #include &lt;stdbool.h&gt; </p>
<p> #include &lt;ldns/ldns.h&gt; </p>
<p> ldns_dnssec_rrsets* ldns_dnssec_rrsets_new(); </p>
<p> void ldns_dnssec_rrsets_free(ldns_dnssec_rrsets *rrsets); </p>
<p> ldns_rr_type ldns_dnssec_rrsets_type(ldns_dnssec_rrsets *rrsets); </p>
<p> ldns_status ldns_dnssec_rrsets_set_type(ldns_dnssec_rrsets *rrsets, ldns_rr_type type); </p>
<p> ldns_status ldns_dnssec_rrsets_add_rr(ldns_dnssec_rrsets *rrsets, ldns_rr *rr); </p>
<p> void ldns_dnssec_rrsets_print(FILE *out, ldns_dnssec_rrsets *rrsets, bool follow); </p>
<h2>DESCRIPTION</h2>
<dl>
<dt> <i>ldns_dnssec_rrsets_new</i>()</p>
<dd>Creates a new list (entry) of RRsets .br Returns the newly allocated structure</dl>
<dl>
<dt> <i>ldns_dnssec_rrsets_free</i>()</p>
<dd>Frees the list of rrsets and their rrs, but *not* the ldns_rr records in the sets </p>
<p> .br <code>rrsets</code>: the data structure to free</dl>
<dl>
<dt> <i>ldns_dnssec_rrsets_type</i>()</p>
<dd>Returns the rr type of the rrset (that is head of the given list) </p>
<p> .br <code>rrsets</code>: the rrset to get the type of .br Returns the rr type</dl>
<dl>
<dt> <i>ldns_dnssec_rrsets_set_type</i>()</p>
<dd>Sets the RR type of the rrset (that is head of the given list) </p>
<p> .br <code>rrsets</code>: the rrset to set the type of .br <code>type</code>: the type to set .br Returns LDNS_STATUS_OK on success</dl>
<dl>
<dt> <i>ldns_dnssec_rrsets_add_rr</i>()</p>
<dd>Add an ldns_rr to the corresponding RRset in the given list of RRsets. If it is not present, add it as a new RRset with 1 record. </p>
<p> .br <code>rrsets</code>: the list of rrsets to add the RR to .br <code>rr</code>: the rr to add to the list of rrsets .br Returns LDNS_STATUS_OK on success</dl>
<dl>
<dt> <i>ldns_dnssec_rrsets_print</i>()</p>
<dd>Print the given list of rrsets to the fiven file descriptor </p>
<p> .br <code>out</code>: the file descriptor to print to .br <code>rrsets</code>: the list of RRsets to print .br <code>follow</code>: if set to false, only print the first RRset</dl>
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
