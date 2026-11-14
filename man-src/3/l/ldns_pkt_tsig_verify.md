---
title: "ldns_pkt_tsig_verify(3)"
name: "ldns_pkt_tsig_verify"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldns_pkt_tsig_verify/"
description: "ldns_pkt_tsig_verify, ldns_pkt_tsig_sign"
---

<h2>NAME</h2>
<p> ldns_pkt_tsig_verify, ldns_pkt_tsig_sign </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;stdint.h&gt;<br />
 #include &lt;stdbool.h&gt; </p>
<p> #include &lt;ldns/ldns.h&gt; </p>
<p> bool ldns_pkt_tsig_verify(ldns_pkt *pkt, uint8_t *wire, size_t wire_size, const char *key_name, const char *key_data, ldns_rdf *mac); </p>
<p> ldns_status ldns_pkt_tsig_sign(ldns_pkt *pkt, const char *key_name, const char *key_data, uint16_t fudge, const char *algorithm_name, ldns_rdf *query_mac); </p>
<h2>DESCRIPTION</h2>
<dl>
<dt> <i>ldns_pkt_tsig_verify</i>()</p>
<dd>verifies the tsig rr for the given packet and key. The wire must be given too because tsig does not sign normalized packets. .br <code>pkt</code>: the packet to verify .br <code>wire</code>: needed to verify the mac .br <code>wire_size</code>: size of wire .br <code>key_name</code>: the name of the shared key .br <code>key_data</code>: the key in base 64 format .br <code>mac</code>: original mac .br Returns true if tsig is correct, false if not, or if tsig is not set</dl>
<dl>
<dt> <i>ldns_pkt_tsig_sign</i>()</p>
<dd>creates a tsig rr for the given packet and key. .br <code>pkt</code>: the packet to sign .br <code>key_name</code>: the name of the shared key .br <code>key_data</code>: the key in base 64 format .br <code>fudge</code>: seconds of error permitted in time signed .br <code>algorithm_name</code>: the name of the algorithm used .br <code>query_mac</code>: is added to the digest if not NULL (so NULL is for signing queries, not NULL is for signing answers) .br Returns status (OK if success)</dl>
<h2>AUTHOR</h2>
<p> The ldns team at NLnet Labs. Which consists out of Jelte Jansen and Miek Gieben. </p>
<h2>REPORTING BUGS</h2>
<p> Please report bugs to ldns-team [at] nlnetlabs.nl or in our bugzilla at <a rel="nofollow" href="http://www.nlnetlabs.nl/bugs/index.html">http://www.nlnetlabs.nl/bugs/index.html</a> </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2004 &#8211; 2006 NLnet Labs. </p>
<p> Licensed under the BSD License. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>SEE ALSO</h2>
<p> <i>ldns_key</i>. And <code>perldoc Net::DNS</code>, <code>RFC1034</code>, <code>RFC1035</code>, <code>RFC4033</code>, <code>RFC4034</code> and <code>RFC4035</code>.</p>
<h2>REMARKS</h2>
<p> This manpage was automaticly generated from the ldns source code by use of Doxygen and some perl. </p>
<h2>Index</h2>
