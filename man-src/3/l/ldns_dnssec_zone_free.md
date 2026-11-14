---
title: "ldns_dnssec_zone_free(3)"
name: "ldns_dnssec_zone_free"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldns_dnssec_zone_free/"
description: "ldns_dnssec_zone_find_rrset, ldns_dnssec_zone_new, ldns_dnssec_zone_free, ldns_dnssec_zone_add_rr, ldns_dnssec_zone_names_print, ldns_dnssec_zone_print, ldns_dnssec_zone_add_empty_nonterminals"
---

<h2>NAME</h2>
<p> ldns_dnssec_zone_find_rrset, ldns_dnssec_zone_new, ldns_dnssec_zone_free, ldns_dnssec_zone_add_rr, ldns_dnssec_zone_names_print, ldns_dnssec_zone_print, ldns_dnssec_zone_add_empty_nonterminals </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;stdint.h&gt;<br />
 #include &lt;stdbool.h&gt; </p>
<p> #include &lt;ldns/ldns.h&gt; </p>
<p> ldns_dnssec_rrsets* ldns_dnssec_zone_find_rrset(ldns_dnssec_zone *zone, ldns_rdf *dname, ldns_rr_type type); </p>
<p> ldns_dnssec_zone* ldns_dnssec_zone_new(); </p>
<p> void ldns_dnssec_zone_free(ldns_dnssec_zone *zone); </p>
<p> ldns_status ldns_dnssec_zone_add_rr(ldns_dnssec_zone *zone, ldns_rr *rr); </p>
<p> void ldns_dnssec_zone_names_print(FILE *out, ldns_rbtree_t *tree, bool print_soa); </p>
<p> void ldns_dnssec_zone_print(FILE *out, ldns_dnssec_zone *zone); </p>
<p> ldns_status ldns_dnssec_zone_add_empty_nonterminals(ldns_dnssec_zone *zone); </p>
<h2>DESCRIPTION</h2>
<dl>
<dt> <i>ldns_dnssec_zone_find_rrset</i>()</p>
<dd>Find the RRset with the given name and type in the zone </p>
<p> .br <code>zone</code>: the zone structure to find the RRset in .br <code>dname</code>: the domain name of the RRset to find .br <code>type</code>: the type of the RRset to find .br Returns the RRset, or NULL if not present</dl>
<dl>
<dt> <i>ldns_dnssec_zone_new</i>()</p>
<dd>Creates a new dnssec_zone structure .br Returns the allocated structure</dl>
<dl>
<dt> <i>ldns_dnssec_zone_free</i>()</p>
<dd>Frees the given zone structure, and its rbtree of dnssec_names Individual ldns_rr RRs within those names are *not* freed .br <code>*zone</code>: the zone to free</dl>
<dl>
<dt> <i>ldns_dnssec_zone_add_rr</i>()</p>
<dd>Adds the given RR to the zone. It find whether there is a dnssec_name with that name present. If so, add it to that, if not create a new one. Special handling of NSEC and RRSIG provided </p>
<p> .br <code>zone</code>: the zone to add the RR to .br <code>rr</code>: The RR to add .br Returns LDNS_STATUS_OK on success, an error code otherwise</dl>
<dl>
<dt> <i>ldns_dnssec_zone_names_print</i>()</p>
<dd>Prints the rbtree of ldns_dnssec_name structures to the file descriptor </p>
<p> .br <code>out</code>: the file descriptor to print the names to .br <code>tree</code>: the tree of ldns_dnssec_name structures to print .br <code>print_soa</code>: if true, print SOA records, if false, skip them</dl>
<dl>
<dt> <i>ldns_dnssec_zone_print</i>()</p>
<dd>Prints the complete zone to the given file descriptor </p>
<p> .br <code>out</code>: the file descriptor to print to .br <code>zone</code>: the dnssec_zone to print</dl>
<dl>
<dt> <i>ldns_dnssec_zone_add_empty_nonterminals</i>()</p>
<dd>Adds explicit dnssec_name structures for the empty nonterminals in this zone. (this is needed for NSEC3 generation) </p>
<p> .br <code>zone</code>: the zone to check for empty nonterminals return LDNS_STATUS_OK on success.</dl>
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
