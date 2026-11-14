---
title: "ldns_rr_compare_ds(3)"
name: "ldns_rr_compare_ds"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldns_rr_compare_ds/"
description: "ldns_rr_compare, ldns_rr_compare_ds"
---

<h2>NAME</h2>
<p> ldns_rr_compare, ldns_rr_compare_ds </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;stdint.h&gt;<br />
 #include &lt;stdbool.h&gt; </p>
<p> #include &lt;ldns/ldns.h&gt; </p>
<p> int ldns_rr_compare(const ldns_rr *rr1, const ldns_rr *rr2); </p>
<p> bool ldns_rr_compare_ds(const ldns_rr *rr1, const ldns_rr *rr2); </p>
<h2>DESCRIPTION</h2>
<dl>
<dt> <i>ldns_rr_compare</i>()</p>
<dd>compares two rrs. The TTL is not looked at. .br <code>rr1</code>: the first one .br <code>rr2</code>: the second one .br Returns 0 if equal -1 if rr1 comes before rr2 +1 if rr2 comes before rr1</dl>
<dl>
<dt> <i>ldns_rr_compare_ds</i>()</p>
<dd>returns true of the given rr&#8217;s are equal. Also returns true if one record is a DS that represents the same DNSKEY record as the other record .br <code>rr1</code>: the first rr .br <code>rr2</code>: the second rr .br Returns true if equal otherwise false</dl>
<h2>AUTHOR</h2>
<p> The ldns team at NLnet Labs. Which consists out of Jelte Jansen and Miek Gieben. </p>
<h2>REPORTING BUGS</h2>
<p> Please report bugs to ldns-team [at] nlnetlabs.nl or in our bugzilla at <a rel="nofollow" href="http://www.nlnetlabs.nl/bugs/index.html">http://www.nlnetlabs.nl/bugs/index.html</a> </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2004 &#8211; 2006 NLnet Labs. </p>
<p> Licensed under the BSD License. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>SEE ALSO</h2>
<p> <i>ldns_rr</i>, <i>ldns_rr_list</i>. And <code>perldoc Net::DNS</code>, <code>RFC1034</code>, <code>RFC1035</code>, <code>RFC4033</code>, <code>RFC4034</code> and <code>RFC4035</code>.</p>
<h2>REMARKS</h2>
<p> This manpage was automaticly generated from the ldns source code by use of Doxygen and some perl. </p>
<h2>Index</h2>
