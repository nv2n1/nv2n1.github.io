---
title: "ldns_pkt2str(3)"
name: "ldns_pkt2str"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldns_pkt2str/"
description: "ldns_rr2str, ldns_pkt2str, ldns_rdf2str, ldns_rr_list2str, ldns_key2str"
---

<h2>NAME</h2>
<p> ldns_rr2str, ldns_pkt2str, ldns_rdf2str, ldns_rr_list2str, ldns_key2str </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;stdint.h&gt;<br />
 #include &lt;stdbool.h&gt; </p>
<p> #include &lt;ldns/ldns.h&gt; </p>
<p> char* ldns_rr2str(const ldns_rr *rr); </p>
<p> char* ldns_pkt2str(const ldns_pkt *pkt); </p>
<p> char* ldns_rdf2str(const ldns_rdf *rdf); </p>
<p> char* ldns_rr_list2str(const ldns_rr_list *rr_list); </p>
<p> char* ldns_key2str(const ldns_key *k); </p>
<h2>DESCRIPTION</h2>
<dl>
<dt> <i>ldns_rr2str</i>()</p>
<dd>Converts the data in the resource record to presentation format and returns that as a char *. Remember to free it. </p>
<p> .br <code>rr</code>: The rdata field to convert .br Returns null terminated char * data, or NULL on error</dl>
<dl>
<dt> <i>ldns_pkt2str</i>()</p>
<dd>Converts the data in the DNS packet to presentation format and returns that as a char *. Remember to free it. </p>
<p> .br <code>pkt</code>: The rdata field to convert .br Returns null terminated char * data, or NULL on error</dl>
<dl>
<dt> <i>ldns_rdf2str</i>()</p>
<dd>Converts the data in the rdata field to presentation format and returns that as a char *. Remember to free it. </p>
<p> .br <code>rdf</code>: The rdata field to convert .br Returns null terminated char * data, or NULL on error</dl>
<dl>
<dt> <i>ldns_rr_list2str</i>()</p>
<dd>Converts a list of resource records to presentation format and returns that as a char *. Remember to free it. </p>
<p> .br <code>rr_list</code>: the rr_list to convert to text .br Returns null terminated char * data, or NULL on error</dl>
<dl>
<dt> <i>ldns_key2str</i>()</p>
<dd>Converts a private key to the test presentation fmt and returns that as a char *. Remember to free it. </p>
<p> .br <code>k</code>: the key to convert to text .br Returns null terminated char * data, or NULL on error</dl>
<h2>AUTHOR</h2>
<p> The ldns team at NLnet Labs. Which consists out of Jelte Jansen and Miek Gieben. </p>
<h2>REPORTING BUGS</h2>
<p> Please report bugs to ldns-team [at] nlnetlabs.nl or in our bugzilla at <a rel="nofollow" href="http://www.nlnetlabs.nl/bugs/index.html">http://www.nlnetlabs.nl/bugs/index.html</a> </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2004 &#8211; 2006 NLnet Labs. </p>
<p> Licensed under the BSD License. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>SEE ALSO</h2>
<p> <i>ldns_rr_print</i>, <i>ldns_rdf_print</i>, <i>ldns_pkt_print</i>, <i>ldns_rr_list_print</i>, <i>ldns_resolver_print</i>, <i>ldns_zone_print</i>. And <code>perldoc Net::DNS</code>, <code>RFC1034</code>, <code>RFC1035</code>, <code>RFC4033</code>, <code>RFC4034</code> and <code>RFC4035</code>.</p>
<h2>REMARKS</h2>
<p> This manpage was automaticly generated from the ldns source code by use of Doxygen and some perl. </p>
<h2>Index</h2>
