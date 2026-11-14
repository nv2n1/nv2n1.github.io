---
title: "ldns_key2rr(3)"
name: "ldns_key2rr"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldns_key2rr/"
description: "ldns_key2rr"
---

<h2>NAME</h2>
<p> ldns_key2rr </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;stdint.h&gt;<br />
 #include &lt;stdbool.h&gt; </p>
<p> #include &lt;ldns/ldns.h&gt; </p>
<p> ldns_rr* ldns_key2rr(const ldns_key *k); </p>
<h2>DESCRIPTION</h2>
<dl>
<dt> <i>ldns_key2rr</i>()</p>
<dd>converts a ldns_key to a public key rr If the key data exists at an external point, the corresponding rdata field must still be added with ldns_rr_rdf_push() to the result rr of this function </p>
<p> .br <code>k</code>: the ldns_key to convert .br Returns ldns_rr representation of the key</dl>
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
