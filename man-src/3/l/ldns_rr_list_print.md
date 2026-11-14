---
title: "ldns_rr_list_print(3)"
name: "ldns_rr_list_print"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldns_rr_list_print/"
description: "ldns_rr_print, ldns_rdf_print, ldns_pkt_print, ldns_rr_list_print, ldns_resolver_print, ldns_zone_print"
---

<h2>NAME</h2>
<p> ldns_rr_print, ldns_rdf_print, ldns_pkt_print, ldns_rr_list_print, ldns_resolver_print, ldns_zone_print </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;stdint.h&gt;<br />
 #include &lt;stdbool.h&gt; </p>
<p> #include &lt;ldns/ldns.h&gt; </p>
<p> void ldns_rr_print(FILE *output, const ldns_rr *rr); </p>
<p> void ldns_rdf_print(FILE *output, const ldns_rdf *rdf); </p>
<p> void ldns_pkt_print(FILE *output, const ldns_pkt *pkt); </p>
<p> void ldns_rr_list_print(FILE *output, const ldns_rr_list *list); </p>
<p> void ldns_resolver_print(FILE *output, const ldns_resolver *r); </p>
<p> void ldns_zone_print(FILE *output, const ldns_zone *z); </p>
<h2>DESCRIPTION</h2>
<dl>
<dt> <i>ldns_rr_print</i>()</p>
<dd>Prints the data in the resource record to the given file stream (in presentation format) </p>
<p> .br <code>output</code>: the file stream to print to .br <code>rr</code>: the resource record to print .br Returns void</dl>
<dl>
<dt> <i>ldns_rdf_print</i>()</p>
<dd>Prints the data in the rdata field to the given file stream (in presentation format) </p>
<p> .br <code>output</code>: the file stream to print to .br <code>rdf</code>: the rdata field to print .br Returns void</dl>
<dl>
<dt> <i>ldns_pkt_print</i>()</p>
<dd>Prints the data in the DNS packet to the given file stream (in presentation format) </p>
<p> .br <code>output</code>: the file stream to print to .br <code>pkt</code>: the packet to print .br Returns void</dl>
<dl>
<dt> <i>ldns_rr_list_print</i>()</p>
<dd>print a rr_list to output .br <code>output</code>: the fd to print to .br <code>list</code>: the rr_list to print</dl>
<dl>
<dt> <i>ldns_resolver_print</i>()</p>
<dd>Print a resolver (in sofar that is possible) state to output. .br <code>output</code>: the fd to print to .br <code>r</code>: the resolver to print</dl>
<dl>
<dt> <i>ldns_zone_print</i>()</p>
<dd>Print a zone structure * to output. Note the SOA record is included in this output .br <code>output</code>: the fd to print to .br <code>z</code>: the zone to print</dl>
<h2>AUTHOR</h2>
<p> The ldns team at NLnet Labs. Which consists out of Jelte Jansen and Miek Gieben. </p>
<h2>REPORTING BUGS</h2>
<p> Please report bugs to ldns-team [at] nlnetlabs.nl or in our bugzilla at <a rel="nofollow" href="http://www.nlnetlabs.nl/bugs/index.html">http://www.nlnetlabs.nl/bugs/index.html</a> </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2004 &#8211; 2006 NLnet Labs. </p>
<p> Licensed under the BSD License. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>SEE ALSO</h2>
<p> <i>ldns_rr2str</i>, <i>ldns_rdf2str</i>, <i>ldns_pkt2str</i>, <i>ldns_rr_list2str</i>, <i>ldns_key2str</i>. And <code>perldoc Net::DNS</code>, <code>RFC1034</code>, <code>RFC1035</code>, <code>RFC4033</code>, <code>RFC4034</code> and <code>RFC4035</code>.</p>
<h2>REMARKS</h2>
<p> This manpage was automaticly generated from the ldns source code by use of Doxygen and some perl. </p>
<h2>Index</h2>
