---
title: "ldns_dnssec_name_name(3)"
name: "ldns_dnssec_name_name"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldns_dnssec_name_name/"
description: "ldns_dnssec_name_new, ldns_dnssec_name_new_frm_rr, ldns_dnssec_name_free, ldns_dnssec_name_name, ldns_dnssec_name_set_name, ldns_dnssec_name_set_nsec, ldns_dnssec_name_cmp, ldns_dnssec_name_add_rr,..."
---

<h2>NAME</h2>
<p> ldns_dnssec_name_new, ldns_dnssec_name_new_frm_rr, ldns_dnssec_name_free, ldns_dnssec_name_name, ldns_dnssec_name_set_name, ldns_dnssec_name_set_nsec, ldns_dnssec_name_cmp, ldns_dnssec_name_add_rr, ldns_dnssec_name_find_rrset, ldns_dnssec_name_print </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;stdint.h&gt;<br />
 #include &lt;stdbool.h&gt; </p>
<p> #include &lt;ldns/ldns.h&gt; </p>
<p> ldns_dnssec_name* ldns_dnssec_name_new(); </p>
<p> ldns_dnssec_name* ldns_dnssec_name_new_frm_rr(ldns_rr *rr); </p>
<p> void ldns_dnssec_name_free(ldns_dnssec_name *name); </p>
<p> ldns_rdf* ldns_dnssec_name_name(ldns_dnssec_name *name); </p>
<p> void ldns_dnssec_name_set_name(ldns_dnssec_name *name, ldns_rdf *dname); </p>
<p> void ldns_dnssec_name_set_nsec(ldns_dnssec_name *name, ldns_rr *nsec); </p>
<p> int ldns_dnssec_name_cmp(const void *a, const void *b); </p>
<p> ldns_status ldns_dnssec_name_add_rr(ldns_dnssec_name *name, ldns_rr *rr); </p>
<p> ldns_dnssec_rrsets* ldns_dnssec_name_find_rrset(ldns_dnssec_name *name, ldns_rr_type type); </p>
<p> void ldns_dnssec_name_print(FILE *out, ldns_dnssec_name *name); </p>
<h2>DESCRIPTION</h2>
<dl>
<dt> <i>ldns_dnssec_name_new</i>()</p>
<dd>Create a new data structure for a dnssec name .br Returns the allocated structure</dl>
<dl>
<dt> <i>ldns_dnssec_name_new_frm_rr</i>()</p>
<dd>Create a new data structure for a dnssec name for the given RR </p>
<p> .br <code>rr</code>: the RR to derive properties from, and to add to the name</dl>
<dl>
<dt> <i>ldns_dnssec_name_free</i>()</p>
<dd>Frees the name structure and its rrs and rrsets. Individual ldns_rr records therein are not freed </p>
<p> .br <code>name</code>: the structure to free</dl>
<dl>
<dt> <i>ldns_dnssec_name_name</i>()</p>
<dd>Returns the domain name of the given dnssec_name structure </p>
<p> .br <code>name</code>: the dnssec name to get the domain name from .br Returns the domain name</dl>
<dl>
<dt> <i>ldns_dnssec_name_set_name</i>()</p>
<dd>Sets the domain name of the given dnssec_name structure </p>
<p> .br <code>name</code>: the dnssec name to set the domain name of .br <code>dname</code>: the domain name to set it to. This data is *not* copied.</dl>
<dl>
<dt> <i>ldns_dnssec_name_set_nsec</i>()</p>
<dd>Sets the <a href="/docs/linux/man/3-nsec/">NSEC</a>(3) RR of the given dnssec_name structure </p>
<p> .br <code>name</code>: the dnssec name to set the domain name of .br <code>nsec</code>: the nsec rr to set it to. This data is *not* copied.</dl>
<dl>
<dt> <i>ldns_dnssec_name_cmp</i>()</p>
<dd>Compares the domain names of the two arguments in their canonical ordening. </p>
<p> .br <code>a</code>: The first dnssec_name to compare .br <code>b</code>: The second dnssec_name to compare .br Returns -1 if the domain name of a comes before that of b in canonical ordening, 1 if it is the other way around, and 0 if they are equal</dl>
<dl>
<dt> <i>ldns_dnssec_name_add_rr</i>()</p>
<dd>Inserts the given rr at the right place in the current dnssec_name No checking is done whether the name matches </p>
<p> .br <code>name</code>: The ldns_dnssec_name to add the RR to .br <code>rr</code>: The RR to add .br Returns LDNS_STATUS_OK on success, error code otherwise</dl>
<dl>
<dt> <i>ldns_dnssec_name_find_rrset</i>()</p>
<dd>Find the RRset with the given type in within this name structure </p>
<p> .br <code>name</code>: the name to find the RRset in .br <code>type</code>: the type of the RRset to find .br Returns the RRset, or NULL if not present</dl>
<dl>
<dt> <i>ldns_dnssec_name_print</i>()</p>
<dd>Prints the RRs in the dnssec name structure to the given file descriptor </p>
<p> .br <code>out</code>: the file descriptor to print to .br <code>name</code>: the name structure to print the contents of</dl>
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
