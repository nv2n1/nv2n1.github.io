---
title: "ldns_rr_rdata2buffer_wire(3)"
name: "ldns_rr_rdata2buffer_wire"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldns_rr_rdata2buffer_wire/"
description: "ldns_pkt2buffer_str, ldns_pktheader2buffer_str, ldns_rr2buffer_str, ldns_rr_list2buffer_str, ldns_rdf2buffer_str, ldns_key2buffer_str, ldns_pkt2buffer_wire, ldns_rr2buffer_wire, ldns_rdf2buffer_wir..."
---

<h2>NAME</h2>
<p> ldns_pkt2buffer_str, ldns_pktheader2buffer_str, ldns_rr2buffer_str, ldns_rr_list2buffer_str, ldns_rdf2buffer_str, ldns_key2buffer_str, ldns_pkt2buffer_wire, ldns_rr2buffer_wire, ldns_rdf2buffer_wire, ldns_rrsig2buffer_wire, ldns_rr_rdata2buffer_wire </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;stdint.h&gt;<br />
 #include &lt;stdbool.h&gt; </p>
<p> #include &lt;ldns/ldns.h&gt; </p>
<p> ldns_status ldns_pkt2buffer_str(ldns_buffer *output, const ldns_pkt *pkt); </p>
<p> ldns_status ldns_pktheader2buffer_str(ldns_buffer *output, const ldns_pkt *pkt); </p>
<p> ldns_status ldns_rr2buffer_str(ldns_buffer *output, const ldns_rr *rr); </p>
<p> ldns_status ldns_rr_list2buffer_str(ldns_buffer *output, const ldns_rr_list *list); </p>
<p> ldns_status ldns_rdf2buffer_str(ldns_buffer *output, const ldns_rdf *rdf); </p>
<p> ldns_status ldns_key2buffer_str(ldns_buffer *output, const ldns_key *k); </p>
<p> ldns_status ldns_pkt2buffer_wire(ldns_buffer *output, const ldns_pkt *pkt); </p>
<p> ldns_status ldns_rr2buffer_wire(ldns_buffer *output, const ldns_rr *rr, int section); </p>
<p> ldns_status ldns_rdf2buffer_wire(ldns_buffer *output, const ldns_rdf *rdf); </p>
<p> ldns_status ldns_rrsig2buffer_wire(ldns_buffer *output, const ldns_rr *sigrr); </p>
<p> ldns_status ldns_rr_rdata2buffer_wire(ldns_buffer *output, const ldns_rr *rr); </p>
<h2>DESCRIPTION</h2>
<dl>
<dt> <i>ldns_pkt2buffer_str</i>()</p>
<dd>Converts the data in the DNS packet to presentation format (as char *) and appends it to the given buffer </p>
<p> .br <code>output</code>: pointer to the buffer to append the data to .br <code>pkt</code>: the pointer to the packet to convert .br Returns status</dl>
<dl>
<dt> <i>ldns_pktheader2buffer_str</i>()</p>
<dd>Converts the header of a packet to presentation format and appends it to the output buffer .br <code>output</code>: the buffer to append output to .br <code>pkt</code>: the packet to convert the header of .br Returns ldns_status</dl>
<dl>
<dt> <i>ldns_rr2buffer_str</i>()</p>
<dd>Converts the data in the resource record to presentation format (as char *) and appends it to the given buffer. The presentation format of DNSKEY record is annotated with comments giving the id, type and size of the key. </p>
<p> .br <code>output</code>: pointer to the buffer to append the data to .br <code>rr</code>: the pointer to the rr field to convert .br Returns status</dl>
<dl>
<dt> <i>ldns_rr_list2buffer_str</i>()</p>
<dd>Converts a rr_list to presentation format and appends it to the output buffer .br <code>output</code>: the buffer to append output to .br <code>list</code>: the ldns_rr_list to print .br Returns ldns_status</dl>
<dl>
<dt> <i>ldns_rdf2buffer_str</i>()</p>
<dd>Converts the data in the rdata field to presentation format (as char *) and appends it to the given buffer </p>
<p> .br <code>output</code>: pointer to the buffer to append the data to .br <code>rdf</code>: the pointer to the rdafa field containing the data .br Returns status</dl>
<dl>
<dt> <i>ldns_key2buffer_str</i>()</p>
<dd>Converts the data in the DNS packet to presentation format (as char *) and appends it to the given buffer </p>
<p> .br <code>output</code>: pointer to the buffer to append the data to .br <code>k</code>: the pointer to the private key to convert .br Returns status</dl>
<dl>
<dt> <i>ldns_pkt2buffer_wire</i>()</p>
<dd>Copies the packet data to the buffer in wire format .br <code>*output</code>: buffer to append the result to .br <code>*pkt</code>: packet to convert .br Returns ldns_status</dl>
<dl>
<dt> <i>ldns_rr2buffer_wire</i>()</p>
<dd>Copies the rr data to the buffer in wire format .br <code>*output</code>: buffer to append the result to .br <code>*rr</code>: resource record to convert .br <code>section</code>: the section in the packet this rr is supposed to be in (to determine whether to add rdata or not) .br Returns ldns_status</dl>
<dl>
<dt> <i>ldns_rdf2buffer_wire</i>()</p>
<dd>Copies the rdata data to the buffer in wire format .br <code>*output</code>: buffer to append the result to .br <code>*rdf</code>: rdata to convert .br Returns ldns_status</dl>
<dl>
<dt> <i>ldns_rrsig2buffer_wire</i>()</p>
<dd>Converts a rrsig to wireformat BUT EXCLUDE the rrsig rdata This is needed in DNSSEC verification .br <code>output</code>: buffer to append the result to .br <code>sigrr</code>: signature rr to operate on .br Returns ldns_status</dl>
<dl>
<dt> <i>ldns_rr_rdata2buffer_wire</i>()</p>
<dd>Converts an rr&#8217;s rdata to wireformat, while excluding the ownername and all the stuff before the rdata. This is needed in DNSSEC keytag calculation, the ds calcalution from the key and maybe elsewhere. </p>
<p> .br <code>*output</code>: buffer where to put the result .br <code>*rr</code>: rr to operate on .br Returns ldns_status</dl>
<h2>AUTHOR</h2>
<p> The ldns team at NLnet Labs. Which consists out of Jelte Jansen and Miek Gieben. </p>
<h2>REPORTING BUGS</h2>
<p> Please report bugs to ldns-team [at] nlnetlabs.nl or in our bugzilla at <a rel="nofollow" href="http://www.nlnetlabs.nl/bugs/index.html">http://www.nlnetlabs.nl/bugs/index.html</a> </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2004 &#8211; 2006 NLnet Labs. </p>
<p> Licensed under the BSD License. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>SEE ALSO</h2>
<p> <i>ldns_pkt2str</i>, <i>ldns_rr2str</i>, <i>ldns_rdf2str</i>, <i>ldns_rr_list2str</i>, <i>ldns_key2str</i>. And <code>perldoc Net::DNS</code>, <code>RFC1034</code>, <code>RFC1035</code>, <code>RFC4033</code>, <code>RFC4034</code> and <code>RFC4035</code>.</p>
<h2>REMARKS</h2>
<p> This manpage was automaticly generated from the ldns source code by use of Doxygen and some perl. </p>
<h2>Index</h2>
