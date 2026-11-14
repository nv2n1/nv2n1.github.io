---
title: "ldns_send(3)"
name: "ldns_send"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldns_send/"
description: "ldns_send"
---

<h2>NAME</h2>
<p> ldns_send </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;stdint.h&gt;<br />
 #include &lt;stdbool.h&gt; </p>
<p> #include &lt;ldns/ldns.h&gt; </p>
<p> ldns_status ldns_send(ldns_pkt **pkt, ldns_resolver *r, const ldns_pkt *query_pkt); </p>
<h2>DESCRIPTION</h2>
<dl>
<dt> <i>ldns_send</i>()</p>
<dd>Sends ptk to the nameserver at the resolver object. Returns the data as a ldns_pkt </p>
<p> .br <code>pkt</code>: packet received from the nameserver .br <code>r</code>: the resolver to use .br <code>query_pkt</code>: the query to send .br Returns status</dl>
<h2>AUTHOR</h2>
<p> The ldns team at NLnet Labs. Which consists out of Jelte Jansen and Miek Gieben. </p>
<h2>REPORTING BUGS</h2>
<p> Please report bugs to ldns-team [at] nlnetlabs.nl or in our bugzilla at <a rel="nofollow" href="http://www.nlnetlabs.nl/bugs/index.html">http://www.nlnetlabs.nl/bugs/index.html</a> </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2004 &#8211; 2006 NLnet Labs. </p>
<p> Licensed under the BSD License. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>SEE ALSO</h2>
<p> <i>ldns_pkt</i>, <i>ldns_resolver</i>. And <code>perldoc Net::DNS</code>, <code>RFC1034</code>, <code>RFC1035</code>, <code>RFC4033</code>, <code>RFC4034</code> and <code>RFC4035</code>.</p>
<h2>REMARKS</h2>
<p> This manpage was automaticly generated from the ldns source code by use of Doxygen and some perl. </p>
<h2>Index</h2>
