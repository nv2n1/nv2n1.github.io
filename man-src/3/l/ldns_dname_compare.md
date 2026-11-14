---
title: "ldns_dname_compare(3)"
name: "ldns_dname_compare"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldns_dname_compare/"
description: "ldns_dname_compare, ldns_dname_interval"
---

<h2>NAME</h2>
<p> ldns_dname_compare, ldns_dname_interval </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;stdint.h&gt;<br />
 #include &lt;stdbool.h&gt; </p>
<p> #include &lt;ldns/ldns.h&gt; </p>
<p> int ldns_dname_compare(const ldns_rdf *dname1, const ldns_rdf *dname2); </p>
<p> int ldns_dname_interval(const ldns_rdf *prev, const ldns_rdf *middle, const ldns_rdf *next); </p>
<h2>DESCRIPTION</h2>
<dl>
<dt> <i>ldns_dname_compare</i>()</p>
<dd>Compares the two dname rdf&#8217;s according to the algorithm for ordering in RFC4034 Section 6. .br <code>dname1</code>: First dname rdf to compare .br <code>dname2</code>: Second dname rdf to compare .br Returns -1 if dname1 comes before dname2, 1 if dname1 comes after dname2, and 0 if they are equal.</dl>
<dl>
<dt> <i>ldns_dname_interval</i>()</p>
<dd>check if middle lays in the interval defined by prev and next prev &lt;= middle &lt; next. This is usefull for nsec checking .br <code>prev</code>: the previous dname .br <code>middle</code>: the dname to check .br <code>next</code>: the next dname return 0 on error or unknown, -1 when middle is in the interval, +1 when not</dl>
<h2>AUTHOR</h2>
<p> The ldns team at NLnet Labs. Which consists out of Jelte Jansen and Miek Gieben. </p>
<h2>REPORTING BUGS</h2>
<p> Please report bugs to ldns-team [at] nlnetlabs.nl or in our bugzilla at <a rel="nofollow" href="http://www.nlnetlabs.nl/bugs/index.html">http://www.nlnetlabs.nl/bugs/index.html</a> </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2004 &#8211; 2006 NLnet Labs. </p>
<p> Licensed under the BSD License. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>SEE ALSO</h2>
<p> <i>ldns_dname_is_subdomain</i>. And <code>perldoc Net::DNS</code>, <code>RFC1034</code>, <code>RFC1035</code>, <code>RFC4033</code>, <code>RFC4034</code> and <code>RFC4035</code>.</p>
<h2>REMARKS</h2>
<p> This manpage was automaticly generated from the ldns source code by use of Doxygen and some perl. </p>
<h2>Index</h2>
