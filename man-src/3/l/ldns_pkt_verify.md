---
title: "ldns_pkt_verify(3)"
name: "ldns_pkt_verify"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldns_pkt_verify/"
description: "ldns_pkt_verify"
---

<h2>NAME</h2>
<p> ldns_pkt_verify </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;stdint.h&gt;<br />
 #include &lt;stdbool.h&gt; </p>
<p> #include &lt;ldns/ldns.h&gt; </p>
<p> ldns_status ldns_pkt_verify(ldns_pkt *p, ldns_rr_type t, ldns_rdf *o, ldns_rr_list *k, ldns_rr_list *s, ldns_rr_list *good_keys); </p>
<h2>DESCRIPTION</h2>
<dl>
<dt> <i>ldns_pkt_verify</i>()</p>
<dd>verify a packet .br <code>p</code>: the packet .br <code>t</code>: the rr set type to check .br <code>o</code>: the rr set name to check .br <code>k</code>: list of keys .br <code>s</code>: list of sigs (may be null) .br <code>good_keys</code>: keys which validated the packet .br Returns status </p>
</dl>
<h2>AUTHOR</h2>
<p> The ldns team at NLnet Labs. Which consists out of Jelte Jansen and Miek Gieben. </p>
<h2>REPORTING BUGS</h2>
<p> Please report bugs to ldns-team [at] nlnetlabs.nl or in our bugzilla at <a rel="nofollow" href="http://www.nlnetlabs.nl/bugs/index.html">http://www.nlnetlabs.nl/bugs/index.html</a> </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2004 &#8211; 2006 NLnet Labs. </p>
<p> Licensed under the BSD License. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>SEE ALSO</h2>
<p> <i>ldns_verify</i>, <i>ldns_sign_public</i>, <i>ldns_zone_sign</i>. And <code>perldoc Net::DNS</code>, <code>RFC1034</code>, <code>RFC1035</code>, <code>RFC4033</code>, <code>RFC4034</code> and <code>RFC4035</code>.</p>
<h2>REMARKS</h2>
<p> This manpage was automaticly generated from the ldns source code by use of Doxygen and some perl. </p>
<h2>Index</h2>
